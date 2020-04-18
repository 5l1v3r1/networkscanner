import scapy.all as scapy
import optparse

print("""            _                      _                                        
 _ __   ___| |___      _____  _ __| | _____  ___ __ _ _ __  _ __   ___ _ __ 
| '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| | | |  __/ |_ \ V  V / (_) | |  |   <\__ \ (_| (_| | | | | | | |  __/ |   
|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\___/\___\__,_|_| |_|_| |_|\___|_| """)

scanner_history_list = list()

def user_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ip_address",help="Enter name ip address : ")
    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP Address : ")
    return user_input

def my_scanner(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_scapy = broadcast_packet/arp_request_packet
    (answer_list,unanswer_list) = scapy.srp(combined_scapy,timeout=1)
    scanner_print = answer_list.summary()

    return scanner_print

user_ip = user_inputs()
my_scanner(user_ip.ip_address)

for x in scanner_history_list:
    pass

#scapy.ls(scapy.ARP())
#scapy.ls(scapy.Ether())
#send = scapy.srp(combined_scapy,timeout=1)
#print(send)

#1)arp_request_packet
#2)Broadcast
#3)Response
