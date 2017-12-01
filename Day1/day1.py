
def main():
	fd = open('day1.txt','rU')
	numbers = []

	for line in fd:
		for c in line:
			numbers.append(c)

	totalSum = 0

	for idx, val in enumerate(numbers):
		if idx == len(numbers) - 1:
			if val == numbers[0]:
				totalSum += int(val)
		else:
			if val == numbers[idx+1]:
				totalSum += int(val)

	print('First task of the day SUM: ' + str(totalSum))

	totalSum = 0
	listLen = len(numbers) / 2

	for idx, val in enumerate(numbers):
		nextElmIndex = idx+listLen

		if nextElmIndex > len(numbers) - 1:

			nextElmVal = numbers[int(nextElmIndex) - len(numbers)]
		else:
			nextElmVal = numbers[nextElmIndex]

		if val == nextElmVal:
			totalSum += int(val)

	print('Second task of the day SUM: ' + str(totalSum))

if __name__ == "__main__":
    main()