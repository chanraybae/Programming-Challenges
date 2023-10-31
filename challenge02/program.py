# Chanwoo Ray Bae
# Programming Challenges

# counting freq of each letter in the word input
def count_letters(word):
    letter_ct = [0] * 26
    for letter in word:
        index = ord(letter) - ord('a')
        letter_ct[index] += 1
    
    return letter_ct

# Computing times s2 can be formed using letters
def compute_forming(s1_ct, s2):
    formed_num = float('inf')
    s2_ct = count_letters(s2)

    for s2_ct, s1_ct in zip(s2_ct, s1_ct):
        if s2_ct > 0:
            formed_num = min(formed_num, s1_ct // s2_ct)

    return formed_num

def main():
    while 1:
        try:
            s1, s2 = input().split()
        except EOFError:
            break

        s1_ct = count_letters(s1)

        print(compute_forming(s1_ct, s2))

if __name__ == "__main__":
    main()
