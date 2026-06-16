#!/usr/bin/env python3
import argparse
import sys
from colorama import init
from rich.console import Console

init(autoreset=True)
console = Console()

# Import modules
from modules.detector import detect_sql_injection
from modules.exploiter import exploit_database
from modules.reporter import generate_report

def banner():
    console.print("""[bold cyan]
=============================================
       PySQLi v3.0 - Advanced Edition
       Educational Purpose Only
=============================================
[/bold cyan]""")

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="PySQLi v3.0 - Advanced SQL Injection Tool")
    parser.add_argument("-u", "--url", required=True, help="Target URL with parameter")
    parser.add_argument("--method", choices=["GET", "POST"], default="GET", help="HTTP Method")
    parser.add_argument("--data", help="POST data (key1=value1&key2=value2)")
    parser.add_argument("--detect", action="store_true", help="Only detect vulnerability")
    parser.add_argument("--dump", action="store_true", help="Exploit and dump data")
    parser.add_argument("--technique", choices=["error", "boolean", "time", "union", "all"], default="all")
    parser.add_argument("--proxy", help="Proxy (http://127.0.0.1:8080)")
    
    args = parser.parse_args()

    console.print(f"[yellow][+] Target: {args.url}[/yellow]")

    is_vuln, param, tech = detect_sql_injection(
        args.url, args.method, args.data, args.technique, args.proxy
    )

    if not is_vuln:
        console.print("[red][-] Target does not appear vulnerable.[/red]")
        sys.exit(0)

    console.print(f"[green][+] SQL Injection Found! Parameter: {param} | Technique: {tech}[/green]")

    if args.detect:
        generate_report(args.url, {"status": "Vulnerable"}, param, tech)
        return

    if args.dump:
        console.print("[cyan][*] Starting data extraction...[/cyan]")
        results = exploit_database(args.url, args.method, args.data, param, tech, args.proxy)
        generate_report(args.url, results, param, tech)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("[red]\n[!] Stopped by user[/red]")
    except Exception as e:
        console.print(f"[red]\n[!] Error: {str(e)}[/red]")
        console.print("[yellow]Make sure all modules are in place.[/yellow]")
