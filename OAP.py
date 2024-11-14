from scapy.all import *
import base64
import random
import time

target_ip = "192.168.86.22"
target_port = 20

source_ip = "192.168.86.27"

command = "echo 'hello'"

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

encrypted_command = xor_encrypt(command, 123)

encoded_command = base64.b64encode(encrypted_command.encode()).decode()

http_request = (
    f"POST / HTTP/1.1\r\n"
    f"Host: {target_ip}\r\n"
    f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\r\n"
    f"Connection: keep-alive\r\n"
    f"Content-Length: {len(encoded_command)}\r\n"
    f"Content-Type: application/x-www-form-urlencoded\r\n"
    f"X-Custom-Header: RandomValue\r\n\r\n"
    f"data={encoded_command}\r\n"
)

packet = IP(src=source_ip, dst=target_ip) / TCP(sport=RandShort(), dport=target_port, flags="PA") / Raw(load=http_request)

send(packet, verbose=False)

time.sleep(random.uniform(0.5, 2.0))
