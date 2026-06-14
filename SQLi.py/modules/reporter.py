from datetime import datetime
from rich.console import Console

console = Console()

def generate_report(url, results, payload, technique):
    """Generate HTML report"""
    filename = f"PySQLi_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PySQLi Scan Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }}
        h1 {{ color: #0066cc; }}
        .container {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <div class="container">
        <h1>PySQLi v2.0 - Scan Report</h1>
        <p><strong>Target URL:</strong> {url}</p>
        <p><strong>Scan Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p><strong>Technique:</strong> {technique}</p>
        <p><strong>Payload:</strong> {payload}</p>
        <hr>
        <h2>Results:</h2>
        <pre>{results}</pre>
    </div>
</body>
</html>"""

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        console.print(f"[green][+] Report successfully saved: {filename}[/green]")
    except Exception as e:
        console.print(f"[red][-] Failed to save report: {e}[/red]")
