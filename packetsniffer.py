from scapy.all import sniff, ICMP, IP

def packet_callback(packet):
    if ICMP in packet:
        print(f"ICMP Packet: {packet[IP].src} -> {packet[IP].dst}")
        print(packet)

# Capture ICMP packets
sniff(filter="icmp", prn=packet_callback, store=0)
