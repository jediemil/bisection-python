testStart = -1000
testEnd = 1000
increment = 0.01
runs = 30

polynomArray = {}
calcprec = 1 / increment  # 10 ** -math.log10(increment) # precision
intervals = []
answers = []


def calcPolynom(x):
    sum = 0
    for aa in range(numberOfGrades + 1):
        sum += (x ** (numberOfGrades - aa)) * polynomArray[aa]

    return sum


def testIntervals(range1, range2):
    for i in range(int(range1 * calcprec), int(range2 * calcprec)):
        interval1 = i / calcprec
        interval2 = (i + 1) / calcprec
        if calcPolynom(interval1) * calcPolynom(interval2) < 0:
            intervals.append(interval1)
        if calcPolynom(interval1) == 0:
            answers.append(str(interval1))


def newIntervals(i1, i2, depth=0):
    depth += 1
    if depth >= runs:
        return i1, i2

    newInterval1 = (i1 + i2) / 2
    res = calcPolynom(newInterval1) * calcPolynom(i2)
    if res < 0:
        return newIntervals(newInterval1, i2, depth)
    elif res > 0:
        return newIntervals(i1, newInterval1, depth)


numberOfGrades = int(input("Hur stort är polynomet? (Andragrad, tredjegrad..?)\n"))

for i in range(0, numberOfGrades + 1):
    polynomArray[i] = int(input("Värde " + str(i + 1) + "\n"))

print("\n\nCalculating..")

testIntervals(testStart, testEnd)

print("\n-------------------------------------------------------\n")

for interval in intervals:
    answer1, answer2 = newIntervals(interval, interval + increment)
    answerText = "ANSWER: " + str((answer1 + answer2) / 2) + "  +- " + str((answer2 - answer1) / 2)
    answers.append(answerText)

for a in answers:
    print(a)
