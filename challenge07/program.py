# Name: Chanwoo Ray Bae
# Course: Programming Challenges
# Challenge 07

import sys

def knight_hop_combos():
    return{
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [], #no combos
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }


# using DFS
def search(val, hops_left, curr, moves, output):
    if hops_left == 0:
        output.append(curr + str(val))
        return

    for next_val in moves[val]:
        search(next_val, hops_left - 1, curr + str(val), moves, output)


def knights_dialer(start, hops):
    moves = knight_hop_combos()
    output = []

    search(start, hops - 1, "", moves, output)
    output.sort()

    return output

def main():
    pairs = []

    for line in sys.stdin:
        start, hops = map(int, line.split())
        pairs.append((start, hops))

    for i, (start, hops) in enumerate(pairs):
        nums = knights_dialer(start, hops)
        for val in nums:
            print(val)

        if i < len(pairs) - 1:
            print()

if __name__ == "__main__":
    main()
