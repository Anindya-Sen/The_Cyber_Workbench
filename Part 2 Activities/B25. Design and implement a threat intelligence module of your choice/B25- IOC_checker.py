import re

# -----------------------------
# 1. Sample IOC database
# -----------------------------
# In a real-world system, this list could come from threat intelligence feeds.
KNOWN_IOCS = {
    "ips": [
        "185.220.101.32",
        "45.155.205.233",
        "91.219.236.222"
    ],
    "domains": [
        "malicious-example.com",
        "phishing-login.net",
        "bad-domain.org"
    ],
    "urls": [
        "http://malicious-example.com/login",
        "http://phishing-login.net/update"
    ],
    "hashes": [
        "44d88612fea8a8f36de82e1278abb02f",  # Example MD5
        "e99a18c428cb38d5f260853678922e03"   # Example MD5
    ]
}


# -----------------------------
# 2. Detection functions
# -----------------------------

def detect_ioc_type(value):
    """
    Detect whether the input is an IP, domain, URL, or hash.
    """

    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    url_pattern = r"^https?://"
    md5_pattern = r"^[a-fA-F0-9]{32}$"
    sha1_pattern = r"^[a-fA-F0-9]{40}$"
    sha256_pattern = r"^[a-fA-F0-9]{64}$"
    domain_pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(ip_pattern, value):
        return "ips"
    elif re.match(url_pattern, value):
        return "urls"
    elif re.match(md5_pattern, value) or re.match(sha1_pattern, value) or re.match(sha256_pattern, value):
        return "hashes"
    elif re.match(domain_pattern, value):
        return "domains"
    else:
        return "unknown"


def check_ioc(value):
    """
    Check whether the IOC exists in the known IOC database.
    """

    value = value.strip()
    ioc_type = detect_ioc_type(value)

    if ioc_type == "unknown":
        return {
            "ioc": value,
            "type": "unknown",
            "status": "Invalid or unsupported IOC format"
        }

    if value in KNOWN_IOCS[ioc_type]:
        return {
            "ioc": value,
            "type": ioc_type,
            "status": "MALICIOUS / FOUND"
        }
    else:
        return {
            "ioc": value,
            "type": ioc_type,
            "status": "Not found in IOC database"
        }


# -----------------------------
# 3. Main program
# -----------------------------

def main():
    print("Simple IOC Checker")
    print("------------------")
    print("Enter an IP, domain, URL, or file hash.")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("Enter IOC: ")

        if user_input.lower() == "exit":
            print("Exiting IOC Checker.")
            break

        result = check_ioc(user_input)

        print("\nResult:")
        print(f"IOC: {result['ioc']}")
        print(f"Type: {result['type']}")
        print(f"Status: {result['status']}")
        print("------------------\n")


if __name__ == "__main__":
    main()
