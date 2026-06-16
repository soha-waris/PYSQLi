from config import PAYLOADS, BYPASS

def get_payloads(technique="all"):
    if technique == "all":
        all_payloads = []
        for tech in PAYLOADS.values():
            all_payloads.extend(tech)
        return all_payloads
    return PAYLOADS.get(technique + "_based", [])

def inject_payload(base_url, param, payload, bypass=""):
    """Inject payload into URL parameter"""
    if "?" not in base_url:
        return base_url + "?" + param + "=" + bypass + payload
    else:
        if param in base_url:
            # Simple replacement for demo
            return base_url.replace(param + "=", param + "=" + bypass + payload)
        else:
            return base_url + "&" + param + "=" + bypass + payload
