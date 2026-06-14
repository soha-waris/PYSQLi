<p align="center">
  <img src="banner.png" alt="PySQLi Banner" width="100%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7+-3fb950?style=for-the-badge&logo=python&logoColor=white&labelColor=0d1117"/>
  <img src="https://img.shields.io/badge/version-2.0-58a6ff?style=for-the-badge&labelColor=0d1117"/>
  <img src="https://img.shields.io/badge/license-MIT-8b949e?style=for-the-badge&labelColor=0d1117"/>
  <img src="https://img.shields.io/badge/use-ethical%20only-ff4444?style=for-the-badge&labelColor=0d1117"/>
</p>

---

```
██████╗ ██╗   ██╗███████╗ ██████╗ ██╗     ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗██║     ██║
██████╔╝ ╚████╔╝ ███████╗██║   ██║██║     ██║
██╔═══╝   ╚██╔╝  ╚════██║██║▄▄ ██║██║     ██║
██║        ██║   ███████║╚██████╔╝███████╗██║
╚═╝        ╚═╝   ╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝
                                 
```

---

## What is this?

PySQLi is a Python-based SQL injection scanner built for learning and practice. Give it a URL, it tries different payloads and tells you if the site is vulnerable. If it is, it can pull basic database info too. A report gets saved after every scan.

Use it on your own sites, local labs, or CTF challenges.

> ⚠️ Only test sites you own or have permission to test.

---

## Setup on Kali Linux

Python comes pre-installed on Kali. Just run:

```
git clone https://github.com/yourname/PySQLi.git
cd PySQLi
pip install -r requirements.txt --break-system-packages
```

---

## How to Run

**Check if a site is vulnerable:**
```
python main.py -u "http://site.com/page.php?id=1" --detect
```

**Pull database info if vulnerable:**
```
python main.py -u "http://site.com/page.php?id=1" --dump
```

**Test a login form:**
```
python main.py -u "http://site.com/login.php" --method POST --data "user=admin&pass=1"
```

**Use a specific technique:**
```
python main.py -u "http://site.com/page.php?id=1" --technique time
```

---

## Techniques

| Flag | What it does |
|------|-------------|
| `error` | Triggers database error messages |
| `boolean` | Compares true/false responses |
| `time` | Detects injection via response delay |
| `union` | Tries to extract data using UNION SELECT |
| `all` | Runs everything — this is the default |

---

## Project Structure

```
PySQLi/
├── main.py               # start here
├── config.py             # payloads and settings
├── requirements.txt
├── modules/
│   ├── detector.py       # finds the vulnerability
│   ├── exploiter.py      # tries to extract db info
│   ├── payloads.py       # loads payloads
│   └── reporter.py       # generates the HTML report
└── utils/
    └── http_utils.py     # handles requests
```

---

## Report

After every scan a file is saved automatically:

```
PySQLi_Report_20240101_120000.html
```

Open it in any browser — it shows the target, technique used, payload that worked, and the results.

---

> For learning purposes only. Do not use without permission.

---

<p align="center">Made by <strong>Soha Waris</strong></p>
