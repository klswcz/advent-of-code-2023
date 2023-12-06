def get_calibration_value(line):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = []

    for letter_i in range(len(line)):
        for number_i, number in enumerate(numbers):
            if line[letter_i:].startswith((number, str(number_i + 1))):
                result.append(str(number_i + 1))

    return result[0] + result[-1]


calibration_document = open("calibration_document.txt", "r").read().split("\n")
calibration_values = map(lambda text_line: int(get_calibration_value(text_line)), calibration_document)
print(sum(calibration_values))
