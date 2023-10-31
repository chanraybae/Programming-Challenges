# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Coding Quandary 14


def calculate_paths(target, tree):
    n = len(tree)
    dp = [{} for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        if i * 2 + 1 < n:
            for k, v in dp[i * 2 + 1].items():
                new_k = tree[i] + k
                if new_k in dp[i]:
                    dp[i][new_k] += v
                else:
                    dp[i][new_k] = v
        
        if i * 2 + 2 < n:
            for k, v in dp[i * 2 + 2].items():
                new_k = tree[i] + k
                if new_k in dp[i]:
                    dp[i][new_k] += v
                else:
                    dp[i][new_k] = v
        
        if tree[i] in dp[i]:
            dp[i][tree[i]] += 1
        else:
            dp[i][tree[i]] = 1

    return sum(dp[i].get(target, 0) for i in range(n))


def process_single_case(line):
    target, tree = line.split()
    target = bin(int(target))[2:]
    total_paths = calculate_paths(target, tree)

    print(f'Paths that form {int(target, 2)} in binary ({target}): {total_paths}')


def main():
    while True:
        try:
            line = input()
            if line == '':
                break

            process_single_case(line)
        except EOFError:
            break


if __name__ == "__main__":
    main()

