# [print(chr(i), '', end='') for i in range(11, 128)]

for i in range(16):
	for j in range(8):
		print(chr(i*8+j+14), '', end='')
	print()