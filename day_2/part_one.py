from typing import List


def normalize(round_details: List[str]):
    res = []
    for grab in round_details:
        space_pos = grab.index(' ')
        grab_obj = {'color': grab[space_pos + 1:], 'score': int(grab[:space_pos])}
        res.append(grab_obj)
    return res


def get_game_stats(game: str):
    game_id = int(game[game.index(' ') + 1:game.index(':')])
    rounds = game[game.index(': ') + 2:].split('; ')
    game_list = []
    result = {}
    for r in rounds:
        game_list.append(normalize(r.split(', ')))
    result['rounds'] = game_list
    result['id'] = game_id
    return result


def get_game_log():
    game_log = []
    for game in open("game_log.txt", "r").read().splitlines():
        game_log.append(get_game_stats(game))
    return game_log


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
