from config import PAYLOADS

def get_payloads(technique="all"):
    """Return payloads based on technique"""
    if technique == "all":
        all_payloads = []
        for key in PAYLOADS:
            all_payloads.extend(PAYLOADS[key])
        return all_payloads
    # ✅ Fix: pehle technique + "_based" tha — config.py mein keys hain: "error", "boolean", "time", "union"
    return PAYLOADS.get(technique, PAYLOADS["error"])
