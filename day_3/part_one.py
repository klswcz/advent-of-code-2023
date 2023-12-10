import re


def has_adjacent_symbols(pos_x, pos_y):
    coordinates_to_check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for (x, y) in coordinates_to_check:
        if pos_x + x <= len(engine_schematic[pos_y]) - 1 and pos_y + y <= len(
                engine_schematic) - 1:
            char = engine_schematic[pos_y + y][pos_x + x]
            if char != '.' and not char.isalnum():
                return True
    return False


def get_part_numbers():
    part_numbers = []
    for row_index, line in enumerate(engine_schematic):
        numbers = re.finditer(r'\d+', line)
        for number in numbers:
            is_part_number = False
            for pos_x in range(number.start(), number.end()):
                res = has_adjacent_symbols(pos_x, row_index)
                if res:
                    is_part_number = True
                    break
            if is_part_number:
                part_numbers.append(int(number.group()))
    return part_numbers


engine_schematic = open("engine_schematic.txt", "r").read().splitlines()
print(sum(get_part_numbers()))
