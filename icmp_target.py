from scapy.all import *


covert_data = []


def extract_icmp_payload(packet):
    # Check if packet has ICMP layer and is an Echo Request
    if ICMP in packet and packet[ICMP].type == 8:
        
        payload = packet[Raw].load
        covert_data.append(payload.decode(errors='ignore'))  
        print(f"Received covert data: {payload}")


print("Sniffing for covert ICMP packets...")
sniff(filter="icmp", prn=extract_icmp_payload, store=0, timeout=30)


full_message = ''.join(covert_data)
print("Full message received:", full_message)
