def get_year() -> [int]:
	year = int(input("Enter the year > "))
	print(f"The year that you entered was {year:04}", end=" ")
	return [
		year // 1000 % 10,
		year // 100  % 10,
		year // 10   % 10,
		year         % 10
	]


def get_firsts(pattern_groups) -> {str}:
	out = set()
	for pattern_group in pattern_groups:
		out.add(pattern_group.split("\n")[0])
	return out


def float_list(str_list: [str]) -> [float]:
	return [float(s) for s in str_list]


def main():
	year_digits = get_year()
	print("which has digits",
		year_digits[0], year_digits[1], year_digits[2], year_digits[3],
	"\n")

	best4 = []
	second_best4 = []
	second_best3 = []
	second_best2 = []
	second_best1 = []
	worst3 = []
	worst2 = []
	worst1 = []

	with open("patterns.txt") as f:
		patterns_str = f.read()[:-1] \
			.replace("a", f"{year_digits[0]}") \
			.replace("b", f"{year_digits[1]}") \
			.replace("c", f"{year_digits[2]}") \
			.replace("d", f"{year_digits[3]}")
		patterns_groups = patterns_str.split("\n\n\n")

		best = {patterns_groups[0]}

		second_best = set(patterns_groups[1].split("\n"))

		no_decimals = patterns_groups[2].split("\n\n")
		decimals = patterns_groups[3].split("\n\n")

		second_best.update(get_firsts(no_decimals))
		second_best.update(get_firsts(decimals))
		second_best.difference_update(best)

		worst = set()
		for no_decimal in no_decimals:
			worst.update(no_decimal.split("\n"))
		for decimal in decimals:
			worst.update(decimal.split("\n"))
		worst.difference_update(best)
		worst.difference_update(second_best)


		best4.append(float_list(best.pop().split(" ")))
		if len(best) != 0: print("There is a problem with the patterns.")

		for pattern in second_best:
			pattern = float_list(pattern.split(" "))
			match len(pattern):
				case 4:
					second_best4.append(pattern)
				case 3:
					second_best3.append(pattern)
				case 2:
					second_best2.append(pattern)
				case 1:
					second_best1.append(pattern)
				case _: print("There is a problem with the patterns.")

		for pattern in worst:
			pattern = float_list(pattern.split(" "))
			match len(pattern):
				case 3:
					worst3.append(pattern)
				case 2:
					worst2.append(pattern)
				case 1:
					worst1.append(pattern)
				case _: print("There is a problem with the patterns.")

	with open("preprocessed0.cinject", "w") as f:
		pattern = best4[0]
		f.write(f"void evalAndUpdateBest() {{ /* Something with {pattern[0]},{pattern[1]},{pattern[2]},{pattern[3]} */ }}\n")

	with open("preprocessed1.cinject", "w") as f:
		out = "evalAndUpdateBest();\n"

		for pattern in second_best4:
			out += f"evalAndUpdateSecondBest4({pattern[0]},{pattern[1]},{pattern[2]},{pattern[3]});\n"
		for pattern in second_best3:
			out += f"evalAndUpdateSecondBest3({pattern[0]},{pattern[1]},{pattern[2]});\n"
		for pattern in second_best2:
			out += f"evalAndUpdateSecondBest2({pattern[0]},{pattern[1]});\n"
		for pattern in second_best1:
			out += f"evalAndUpdateSecondBest1({pattern[0]});\n"

		for pattern in worst3:
			out += f"evalAndUpdateWorst3({pattern[0]},{pattern[1]},{pattern[2]});\n"
		for pattern in worst2:
			out += f"evalAndUpdateWorst2({pattern[0]},{pattern[1]});\n"
		for pattern in worst1:
			out += f"evalAndUpdateWorst1({pattern[0]});\n"

		f.write(out)


if __name__ == "__main__":
	main()
