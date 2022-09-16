config = []

config.append(1)
config.append(2)
config.append(3)
config.append(4)

print(config)

config = [1, 2, 3, 4, 5, 6, 7, 8]
config2 = [8, 7, 6, 5, 4]
config.extend(config2)
print(config)
config.extend([5, 5, 5555, 555, 555])
print(config)

