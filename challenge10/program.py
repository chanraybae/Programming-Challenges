# Name: Chanwoo Ray Bae
# Course: Programming Challenges
# Challenge 10


def find_min_op(n, memoi):
    if n == 1:
        return 0
    
    if n not in memoi:
        if n % 2 == 0:
            memoi[n] = 1 + find_min_op(n // 2, memoi)
        else:
            memoi[n] = 1 + min(find_min_op(n + 1, memoi), find_min_op(n - 1, memoi))
    
    return memoi[n]


def main():
    test_case_num = 1
    memoi = {}
    
    while 1:
        try:
            n = int(input())
            output = find_min_op(n, memoi)
            
            print(f"{test_case_num}. {output}")
            test_case_num += 1
        
        except EOFError:
            break


if __name__ == "__main__":
    main()

