#!/usr/bin/env python3
# Name: Chanwoo Ray Bae
# Course: cse-30872-su23

def main():
    mat_num = 1

    N, M = map(int, input().split())
        # Terminating by final 0 0 as noted
    while ((N != 0) and (M != 0)):

        min_num = float('inf') # minimum sum value for comparison
        prev_row = list(map(int, input().split()))

        for r in range(1, N):
            curr_row = list(map(int, input().split()))
            for c in range(M - 1):
                four_sq_sum = prev_row[c] + prev_row[c + 1] + curr_row[c] + curr_row[c + 1]
                min_num = min(min_num, four_sq_sum)
            prev_row = curr_row
        
        print(f"{mat_num}. Minimum four square is: {min_num}")
        
        mat_num += 1
        # Next read
        N, M = map(int, input().split())


if __name__ == "__main__":
    main()
