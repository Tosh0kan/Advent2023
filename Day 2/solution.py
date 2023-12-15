import json
import timeit
from pprint import pprint

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
            for e in t_list:
                d_list.append({e.split()[1]: int(e.split()[0])})
            puzzle_dict.setdefault(game, []).append(d_list)

    with open(rf"{inp_f.split('.')[0]}.json","w", encoding="utf-8") as f:
        f.write(json.dumps(puzzle_dict, indent=4))
    return puzzle_dict

def main():
    input_2_dict(r'D:\01 Libraries\Documents\Coding\Advent of Code\Advent2023\Day 2\input_example.txt')

if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
