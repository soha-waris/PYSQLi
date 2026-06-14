#!/usr/bin/env python3
import argparse
import sys
from colorama import init, Fore, Style
from rich.console import Console
from modules.detector import detect_sql_injection
from modules.exploiter import exploit_database   # ✅ Fix: exploiters.py ko exploiter.py rename kiya
from modules.reporter import generate_report

init(autoreset=True)
console = Console()

def banner():
    console.print("""
[bold cyan]
=============================================
       PySQLi v2.0 - Advanced SQLi Tool
          Educational Purpose Only
=============================================
[/bold cyan]
    """)

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="PySQLi v2.0 - Advanced SQL Injection Tool")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g. http://testphp.vulnweb.com/listproducts.php?cat=1)")
    parser.add_argument("--method", choices=["GET", "POST"], default="GET", help="HTTP Method")
    parser.add_argument("--data", help="POST data (e.g. id=1&name=test)")
    parser.add_argument("--detect", action="store_true", help="Only detect vulnerability")
    parser.add_argument("--dump", action="store_true", help="Attempt exploitation")
    parser.add_argument("--technique", choices=["error", "boolean", "time", "union", "all"], default="all")
    
    args = parser.parse_args()

    console.print(f"[yellow][+] Target:[/yellow] {args.url}")

    is_vulnerable, injection_point, technique = detect_sql_injection(
        args.url, args.method, args.data, args.technique
    )

    if not is_vulnerable:
        console.print("[red][-] Target not vulnerable.[/red]")
        sys.exit(1)

    console.print("[green][+] Vulnerability Found![/green]")

    if args.detect:
        generate_report(args.url, {"status": "Detection Only"}, injection_point, technique)
        return

    if args.dump:
        console.print("[cyan][*] Starting Exploitation...[/cyan]")
        results = exploit_database(args.url, args.method, args.data, injection_point, technique)
        generate_report(args.url, results, injection_point, technique)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("[red]\n[!] Stopped by user.[/red]")
    except Exception as e:
        console.print(f"[red]\n[!] Error: {e}[/red]")
