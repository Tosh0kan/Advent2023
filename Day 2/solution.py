import json
import timeit

elven_cubes = {'red': 12, 'green': 13, 'blue': 14}

def input_2_dict(inp_f: str) -> dict:
    with open(f"{inp_f}","r", encoding="utf-8") as f:
        puzzle: list[str] = f.read().splitlines()

    puzzle_split = {line.split(':')[0]:
        [e for e in line.split(':')[1].strip().split('; ')] for line in puzzle}

    puzzle_dict = {}
    for game, sets in puzzle_split.items():
        puzzle_dict.setdefault(game, [])
        for set in sets:
            t_list: list[str] = [e for e in set.split(', ')]
            d_list = []
            d_list.append({e.split()[1]: int(e.split()[0]) for e in t_list})
            puzzle_dict.setdefault(game, []).append(d_list)

    with open(rf"{inp_f.split('.')[0]}.json","w", encoding="utf-8") as f:
        f.write(json.dumps(puzzle_dict, indent=4))
    return puzzle_dict

def valid_game_sum(game:str, set_list: list[dict]) -> int:
    for set in set_list:
        for showing in set:
            for color, ammount in showing.items():
                if ammount > elven_cubes[color]:
                    return 0
    return int(game.split()[1])

def power_cubes(set_list: list[dict]) -> int:
    max_cubes = {'red': 0, 'blue': 0, 'green': 0}
    for set in set_list:
        for showing in set:
            for color, ammount in showing.items():
                if ammount > max_cubes[color]:
                    max_cubes[color] = ammount

    return max_cubes['red'] * max_cubes['blue'] * max_cubes['green']

def main():
    # game_registry = input_2_dict(r'D:\01 Libraries\Documents\Coding\Advent of Code\Advent2023\Day 2\input_example.txt')
    with open(r'.\Day 2\input.json', 'r', encoding='utf-8'
              ) as f:
        game_registry = json.loads(f.read())
    total = 0
    for game, set_list in game_registry.items():
        # total += valid_game_sum(game, set_list)
        total += power_cubes(set_list)
    print(total)

if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
