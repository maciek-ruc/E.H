from scapy.all import *
import random
import time


target_ip = "192.168.86.22" 


ports_to_scan = [22, 80, 443, 8080, 3306] 


def scan_port(port):
    source_port = random.randint(1025, 65535)
    

    syn_packet = IP(dst=target_ip) / TCP(sport=source_port, dport=port, flags="S")
    

    response = sr1(syn_packet, timeout=1, verbose=False)
    

    if response is None:
        print(f"Port {port} is filtered (no response).")
    elif response.haslayer(TCP):
  
        if response.getlayer(TCP).flags == 0x12:  
            print(f"Port {port} is open.")
       
        elif response.getlayer(TCP).flags == 0x14: 
            print(f"Port {port} is closed.")
    else:
        print(f"Received an unexpected response for port {port}.")


for port in ports_to_scan:
    scan_port(port)
    time.sleep(random.uniform(1, 4))  
