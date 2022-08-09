#!/usr/bin/env python
import requests

def request(url):
    try:
        return requests.get("http://" +url)
    except requests.exceptions.ConnectionError:
        pass

target_url = input("Enter Base URL (like example.com): ")

print("Subdomain Crawling Results:\n")
with open("C:\\Users\\User\\Desktop\\Wordlists\\subdomains-wodlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered Subdomain -->", test_url)
