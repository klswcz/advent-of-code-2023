from day_2.helpers import get_game_log


def is_playable(rounds, point_limits):
    for (color, limit) in point_limits.items():
        for round in rounds:
            matching_grabs = list(filter(lambda grab: grab['color'] == color, round))
            if len(matching_grabs) > 0 and matching_grabs[0]['score'] > limit:
                return False
    return True


def get_playable_matches_ids(point_limits: dict[str, int]):
    game_log = get_game_log()
    playable_games_ids = []
    for game in game_log:
        if is_playable(game['rounds'], point_limits):
            playable_games_ids.append(game['id'])
    return playable_games_ids


limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

print(sum(get_playable_matches_ids(limits)))
