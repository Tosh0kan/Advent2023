import re
import timeit

c_digs = {
    'one': '1', 'two': '2', 'three': '3',
    'four': '4', 'five': '5', 'six': '6',
    'seven': '7', 'eight': '8', 'nine': '9'
}

def main() -> None:
    with open(r"D:\01 Libraries\Documents\Coding\Advent of Code\Advent2023\Day 1\puzzle.txt",
              "r", encoding="utf-8") as f:
        puzzle: str = f.read()

    puzzle: list[str] = puzzle.splitlines()
    total = 0
    for line in puzzle:
        digits: list[str] = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        if digits[0].isdigit() and digits[-1].isdigit():
            temp_dig = int(digits[0] + digits[-1])
            total += temp_dig
        elif digits[0].isdigit() and not digits[-1].isdigit():
            temp_dig = int(digits[0] + c_digs[digits[-1]])
            total += temp_dig
        elif not digits[0].isdigit() and digits[-1].isdigit():
            temp_dig = int(c_digs[digits[0]] + digits[-1])
            total += temp_dig
        elif not digits[0].isdigit() and not digits[-1].isdigit():
            temp_dig = int(c_digs[digits[0]] + c_digs[digits[-1]])
            total += temp_dig
    print(total)

if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
