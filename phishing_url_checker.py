#bin/python

import sys
from datetime import datetime

import re

def analyze_url(url):

    score = 0

    if re.search(r'(\d{1,3}\.){3}\d{1,3}', url):
        print("URL contains an IP address")
        score += 3

    if len(url) > 75:
        print("URL is unusually long")
        score += 2

    keywords = ["login","verify","secure","account","update","bank","signin"]

    for word in keywords:
        if word in url.lower():
            print(f"Suspicious keyword detected: {word}")
            score += 2
            break

    if not url.startswith("https"):
        print("HTTPS not used")
        score += 2

    special_chars = url.count("@") + url.count("-") + url.count("_")

    if special_chars > 3:
        print("Too many special characters in URL")
        score += 1

    print("\nRisk Score:", score,"/ 10")

    if score <= 3:
        print("Risk Level: LOW")
    elif score <= 6:
        print("Risk Level: MEDIUM")
    else:
        print("Risk Level: HIGH (Possible Phishing URL)")


if __name__ == "__main__":
    print("WELCOME TO MALACIOUS URL SCANNER")
    print("- " * 50)
    
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = input("Enter the url here: ")
        print("TIP: You can pass the url in the terminal")
        print("->python url_scanner.py URL")
        
    print("Scan initiated on:", datetime.now())
    print("Scanning the URL:", url)
    print("- " * 50)
    
    analyze_url(url)

