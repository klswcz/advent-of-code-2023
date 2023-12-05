def get_calibration_value(line):
    # all numbers have ASCII value between 48 and 57
    numbers = list(filter(lambda char: 48 <= ord(char) <= 57, line))
    return numbers[0] + numbers[-1]


calibration_document = open("calibration_document.txt", "r").read().split("\n")
calibration_values = map(lambda text_line: int(get_calibration_value(text_line)), calibration_document)

print(sum(calibration_values))
