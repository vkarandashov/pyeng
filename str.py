cmd = "interface GA"
new_cmd = cmd.replace("GA", "FA")
print(new_cmd)

print(cmd.replace("GA", "FA"))

cmd = "\n\ninterface Gi0/0\n\t" # white space symbols
print(cmd)
#clean string for symbols
cmd.strip()
print(cmd)

str = "[1213123123/123123213]"
strip method for clean symbols
print(str.strip("[]")) #rstrip - right / lstrip left strip

cmd = ' swith trunk allowed vlan 1,2,2,3,34,4\n'
#for split resul ['swith', 'trunk', 'allowed', 'vlan', '1,2,2,3,34,4']
print(cmd.split())

vlan = "1,2,3,4,5,65,6,7,78,8,7,12"
result ['1', '2', '3', '4', '5', '65', '6', '7', '78', '8', '7', '12']
print(vlan.split(','))


ip = '10.1.1.1'
ip.split('.')
print(ip.split())

cmd = ' switch trunk allowed vlan 1,2,2,3,34,4\n'
print(cmd.replace("vlan", " asdasd").replace(" asdasd", "wow"))
