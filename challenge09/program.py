# Name: Chanwoo Ray Bae
# Course: Programming Challenges
# Challenge 09
# Using bit manipulation on top of greedy algo for funsies

import sys

def can_give_change(customers):
    counts = 0  
    # low 16 bits represent count of $5 bills, next 16 are $10 bills
    
    for bill in customers:
        if bill == 5:
            counts += 1
        elif bill == 10:
            if (counts & 0xFFFF) == 0:  # looking for $5 bills
                return False
            counts -= 1  # dec $5 count
            counts += (1 << 16)  # inc $10 count
        elif bill == 20:
            if (counts & 0xFFFF) > 0 and (counts >> 16) > 0:
                counts -= 1 + (1 << 16)
            elif (counts & 0xFFFF) >= 3:  # 3 $5 bills
                counts -= 3
            else:
                return False
    return True


def main():
    test_case = 1
    
    for line in sys.stdin:
        customers = list(map(int, line.split()))
        
        if can_give_change(customers):
            print(f"{test_case}. Yeah")
        else:
            print(f"{test_case}. Nope")
        test_case += 1


if __name__ == "__main__":
    main()


