from scapy.all import *
import time


target_ip = "192.168.86.22"  


covert_message = "Covert Channel Using ICMP"
data = covert_message.encode()


for i in range(len(data)):
    packet = IP(dst=target_ip) / ICMP(type=8) / Raw(load=data[i:i+1])
    send(packet, verbose=False)
    print(f"Sent packet with data: {data[i:i+1]}")
    time.sleep(1)