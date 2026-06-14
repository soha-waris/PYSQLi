import time
from utils.http_utils import send_request
from modules.payloads import get_payloads
from rich.console import Console

console = Console()

def detect_sql_injection(url, method="GET", data=None, technique="all"):
    """Detect SQL Injection vulnerability"""
    console.print("[cyan][*] Sending normal request...[/cyan]")
    normal_response = send_request(url, method, data)
    
    if not normal_response:
        console.print("[red][-] Cannot connect to target[/red]")
        return False, None, None

    payloads = get_payloads(technique)
    console.print(f"[cyan]Testing {len(payloads)} payloads...[/cyan]")
    
    for payload in payloads:
        start_time = time.time()
        response = send_request(url, method, data, payload)
        if not response:
            continue

        elapsed = time.time() - start_time

        # Detection logic
        if response.status_code != normal_response.status_code:
            return True, payload, technique
        
        content_diff = abs(len(response.text) - len(normal_response.text))
        if content_diff > 400 or any(err in response.text.lower() for err in ["sql syntax", "mysql", "sqlite", "error", "odbc"]):
            return True, payload, technique
        
        # Time-based detection
        if "sleep" in payload.lower() and elapsed > 3.5:
            return True, payload, "time"

    return False, None, None
