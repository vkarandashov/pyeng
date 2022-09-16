# interface = "Gi0/0"
#
# print(f"interface {interface}")
#
# cmd = "swithport trunk allowed vlan"
# vlan = "1,2,3,4"
#
# print(cmd + " " + vlan)
# print(f"{cmd} {vlan}")
# print(f"{cmd.upper()} {vlan.split(',')}")

oct1, oct2, oct3, oct4 = 192, 168, 100, 1
# print(oct1, oct2, oct3, oct4)

print(f"{oct1:<9}{oct2:<9}{oct3:<9}{oct4:<9}\n{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}")

