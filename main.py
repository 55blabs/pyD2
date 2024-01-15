from scapy.all import sniff


def packet_handler(packet):
    # process and analyze the packet here
    print(packet.summary())


sniff(iface='eth0', prn=packet_handler, filter='tcp or udp', count=10)


def analyze_packet(packet):
    # Implement your packet analysis and detetection logic here

    if packet.haslayer('TCP'):
        # Example: Detect and print TCP packets

        print('Detected TCP packet: ')
        print(packet.show())


sniff(iface='eth0', prn=analyze_packet, filter='tcp or udp', count=10)

