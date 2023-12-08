from functools import reduce

from day_2.helpers import get_game_log


def get_minimum_cubes_needed(game):
    min_cubes_counts = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for r in game['rounds']:
        for (color, count) in min_cubes_counts.items():
            matching_grab = next(iter(list(filter(lambda grab: grab['color'] == color, r))), None)
            if matching_grab and (matching_grab['score'] > count or count == 0):
                min_cubes_counts[color] = matching_grab['score']

    return reduce(lambda a, b: a * b, list(min_cubes_counts.values()))


game_log = get_game_log()
print(sum(list(map(lambda game: get_minimum_cubes_needed(game), game_log))))
