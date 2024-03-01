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


def main():
	year_digits = get_year()
	print("which has digits",
		year_digits[0], year_digits[1], year_digits[2], year_digits[3],
	"\n")

	with open("patterns.txt") as f:
		patterns_str = f.read() \
			.replace("a", f"{year_digits[0]}") \
			.replace("b", f"{year_digits[1]}") \
			.replace("c", f"{year_digits[2]}") \
			.replace("d", f"{year_digits[3]}")
		patterns_groups = patterns_str.split("\n\n\n")

		best = set(patterns_groups[0])

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

	with open("preprocessed.cinject", "w") as f:
		f.write("")


if __name__ == "__main__":
	main()
