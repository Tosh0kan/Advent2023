import re
import time
from numba import jit


# @jit(nopython=True)
def main() -> None:
    with open(r"D:\01 Libraries\Documents\Coding\Advent of Code\Advent2023\Day 1\puzzle.txt",
              "r", encoding="utf-8") as f:
        puzzle: str = f.read()

    puzzle: list = puzzle.split("\n")
    total: int = 0
    for line in puzzle:
        digits = re.findall(r"\d", line)
        if len(digits) == 0:
            pass
        else:
            temp_digit = digits[0] + digits[-1]
            total += int(temp_digit)
    print(total)

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print('\n', end - start)
