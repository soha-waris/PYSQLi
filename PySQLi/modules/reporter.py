from rich.console import Console
import datetime

console = Console()

def generate_report(target_url, results, param=None, technique=None):
    """Generate HTML report"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""<html>
<head><title>PySQLi Report - {target_url}</title></head>
<body>
<h1>PySQLi v3.0 Advanced Report</h1>
<p><strong>Target:</strong> {target_url}</p>
<p><strong>Scan Time:</strong> {timestamp}</p>
<p><strong>Vulnerable Parameter:</strong> {param}</p>
<p><strong>Technique:</strong> {technique}</p>
<hr>
<h2>Results</h2>
<pre>{results}</pre>
</body>
</html>"""
    
    with open("sqli_report.html", "w", encoding="utf-8") as f:
        f.write(report)
    
    console.print("[green][+] Report saved as sqli_report.html[/green]")
