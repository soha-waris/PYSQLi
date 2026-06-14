# ✅ Fix: utils.py tha — detector.py "from utils.http_utils import" dhundh raha tha
#         isliye utils/http_utils.py mein move kiya
import requests
import random
import time
from config import USER_AGENTS, TIMEOUT, DELAY, MAX_RETRIES

def send_request(url, method="GET", data=None, payload="", retries=0):
    """Send HTTP request with payload"""
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    try:
        if method.upper() == "GET":
            separator = "&" if "?" in url else "?"
            target_url = url + separator + payload if payload else url
            response = requests.get(target_url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        else:
            response = requests.post(url, data=data, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        
        return response
    except requests.exceptions.RequestException:
        if retries < MAX_RETRIES:
            time.sleep(DELAY)
            return send_request(url, method, data, payload, retries + 1)
        return None
