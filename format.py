# #format with "{}" example:
# cmd = 'interface G/{}'
#
# print(cmd.format('123'))
#
# func = """
# interface tunnel{}
# ip address{}
# tunel source{}
# """
#
# print(func.format(' 0', " 1.1.1.1", ' G10'))
#
# #format with alias example:
# func = """
# interface tunnel{tunel}
# ip address{ip}
# tunel source{src}
#  """
# print(func.format(tunel=" 1", ip=" 1.2.3.12", src=" root"))
#
# #get format func with " : " example:
# output = "{:5}{:10}{:10}"
# print(output.format("14", "192.168.1.12", " root"))
#
# #column width
# output = "{:4}{:4}{:4}\n"*2
# print(output.format("14", "192.168.1.12", " root", "14", "192.168.1.12", " root"))

# #to binary
# template = "{:b} {:b} {:b} {:b}"
# print(template.format(192, 168, 31, 104))
#
# #every octet got 8 symbols
# template = "{:08b} {:08b} {:08b} {:08b}"
# print(template.format(192, 168, 1, 254))

# template = "{:9}{:9}{:9}{:9}\n{:08b} {:08b} {:08b} {:08b}"
# print(template.format(192, 168, 1, 254, 192, 168, 1, 254))

# template = "{0:9}{1:9}{2:9}{3:9}\n{0:08b} {1:08b} {2:08b} {3:08b}"
# print(template.format(192, 168, 1, 254))

template = "{0:<9}{1:<9}{2:<9}{3:<9}\n{0:08b} {1:08b} {2:08b} {3:08b}"
print(template.format(192, 168, 1, 254))