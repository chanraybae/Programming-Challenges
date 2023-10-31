# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Quandary 11


def find_minimum_dogecoin_transactions(target_dogecoins):
    min_transactions = [0] * (2 * target_dogecoins + 2)
    
    queue = [(1, 1)]
    
    # BFS
    for dogecoins, transactions in queue:
        if dogecoins == target_dogecoins:
            return transactions
        
        next_states = [(dogecoins * 2, transactions + 1), (dogecoins + 1, transactions + 1)]
        for next_dogecoins, next_transactions in next_states:
            if next_dogecoins <= 2 * target_dogecoins:
                if min_transactions[next_dogecoins] == 0 or min_transactions[next_dogecoins] > next_transactions:
                    queue.append((next_dogecoins, next_transactions))
                    min_transactions[next_dogecoins] = next_transactions
                    
    return -1


def main():
    test_case_count = 1
    
    while True:
        try:
            target_dogecoins = int(input())

            if target_dogecoins == 0:  
                print(f"{test_case_count}. Minimum number of doge transactions: 0")
            else:
                min_transactions = find_minimum_dogecoin_transactions(target_dogecoins)
                print(f"{test_case_count}. Minimum number of doge transactions: {min_transactions}")
            
            test_case_count += 1
        
        except EOFError:
            break


if __name__ == "__main__":
    main()

