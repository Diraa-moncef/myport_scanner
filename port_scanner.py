print("                    ####                    ")
print("  port scanner     //  \\")
print("                ============")
print("      ?  ______?  (*    * )  ")
print("        /_____/|    ||||")
print("       |______|/   /    \ ")
print("                  |      |")

import socket
ip=str(input("pleas enter the IP address :"))
ports=[20,21,23,25,53,67,68,69,80,110,119,123,135,139,143,156,161,162,179,194,389,443,445,3389]
for p in ports:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    r=s.connect_ex((ip,p))
    if r == 0:
        service = socket.getservbyport(p)
        print("--[ * {} * is open --> {} ]".format(p,service))
    s.close()
