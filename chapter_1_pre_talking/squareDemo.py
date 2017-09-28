def sqrt(x):
	y = 1.0
	while abs(y * y - x) > 0.0000000001:
		y = (y + x/y) / 2
		return y


print(sqrt(2))