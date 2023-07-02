from scapy.all import *
import requests
import time

def get_ip(pkt):
    ip = pkt[IP].src
    if ip[:4] == "192.":
        return
    req = requests.get(f"https://ipapi.co/{ip}/json/").json()
    print(f""" 
        IP: {req.get('ip')}
        Country: {req.get('country_name')}
        City: {req.get('city')}
        Region: {req.get('region')}
        ISP: {req.get('org')}
        {'-'*20}""")

while True:
    sniff(filter="udp", prn=get_ip, count=1)
    time.sleep(4)
