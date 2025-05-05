def get_sum_of_valid_mul_commands():
	is_mul, do_mul = None, True
	sum_mul = 0

	with open("input.txt") as f:
		lines = f.readlines()
		for line in lines:
			for i in range(len(line)):
				if line[i:i + 4] == "do()":
					do_mul = True
				if line[i:i + 6] == "don't(":
					do_mul = False
				if line[i:i + 4] == "mul(":
					is_mul = i + 4
				elif line[i] == ")" and is_mul != None:
					try:
						a = list(map(int, line[is_mul:i].split(",")))
						if len(a) == 2:
							if do_mul:
								sum_mul += a[0] * a[1]
					except:
						pass
					is_mul = None

	return sum_mul

print(get_sum_of_valid_mul_commands())
