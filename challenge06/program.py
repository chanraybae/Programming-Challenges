# Name: Chanwoo Ray Bae
# Course: Programming Challenges
# Challenge06

# Could use defaultdict to increase efficiency by reducing manual
# insertions/deletions from collections import defaultdict

def longest_seq_uniq(froot):
    ptr, max_len = 0, 0
    max_froot = []
    fruit_baskset = set()

    for tail in range(len(froot)):
        while froot[tail] in fruit_baskset:
            fruit_baskset.remove(froot[ptr])
            ptr += 1

        fruit_baskset.add(froot[tail])

        if(tail - ptr + 1 > max_len):
            max_len = tail - ptr + 1
            max_froot = froot[ptr:tail + 1]

    return max_len, max_froot

def main():
    try:
        while 1:
            froot = input().split()

            length, subseq = longest_seq_uniq(froot)

            print(f"{length}: {', '.join(subseq)}")

    except EOFError:
        pass

if __name__ == "__main__":
    main()
