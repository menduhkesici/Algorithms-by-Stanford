values = [0] * (10**6 + 1)
x = 1
h = {}

with open('2 - 4 - 2-SUM algorithm.txt') as f:
	for line in f:
		values[x] = int(line)
		h[int(line)] = True
		x = x + 1

num_t = 0

for t in range(-10000, 10001):
	print(t)
	for x in values:
		if (t - x) in h:
			if x != t / 2:
				num_t += 1
				print(t, x, (t - x))
				break

print(num_t)

# Answer: 427