# SQLi.py 

A Python-based SQL Injection detection and analysis tool built for security testing and educational use. Test only on systems you own or have explicit permission to test.

---

## What It Does

- Detects SQL injection vulnerabilities using multiple techniques
- Supports GET and POST requests
- Generates an HTML report with scan results
- Rotates user agents to mimic real browser traffic

---

## Requirements

Python 3.7+ and the following packages:

```
pip install -r requirements.txt
```

---

## Project Structure

```
PySQLi/
├── main.py               # Entry point
├── config.py             # Payloads, timeouts, settings
├── requirements.txt
├── modules/
│   ├── detector.py       # Vulnerability detection logic
│   ├── exploiter.py      # Basic database enumeration
│   ├── payloads.py       # Payload loader
│   └── reporter.py       # HTML report generator
└── utils/
    └── http_utils.py     # HTTP request handler
```

---

## Usage

**Detect only:**
```bash
python main.py -u "http://target.com/page.php?id=1" --detect
```

**Detect + dump database info:**
```bash
python main.py -u "http://target.com/page.php?id=1" --dump
```

**POST request:**
```bash
python main.py -u "http://target.com/login.php" --method POST --data "user=admin&pass=1"
```

**Use a specific technique:**
```bash
python main.py -u "http://target.com/page.php?id=1" --technique time
```

---

## Techniques

| Flag | Description |
|------|-------------|
| `error` | Triggers database error messages |
| `boolean` | True/false response comparison |
| `time` | Detects blind injection via response delay |
| `union` | Extracts data using UNION SELECT |
| `all` | Runs all techniques (default) |

---

## Output

A timestamped HTML report is saved automatically after each scan:
```
PySQLi_Report_20240101_120000.html
```

---

## Disclaimer

This tool is for **educational and authorized testing only**. Unauthorized use against systems you don't own is illegal. The author is not responsible for any misuse.
