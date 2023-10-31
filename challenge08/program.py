# Name: Chanwoo Ray Bae
# Course: Programming Challenges
# Challenge 08
# Used bitstream instead of bitmap, is O(NM) and meets

def convert_hex_to_bin(hex_string, bit_length=4):
    return bin(int(hex_string, 16))[2:].zfill(bit_length)


def convert_int_to_bin(int_value, bit_length=32):
    return bin(int_value)[2:].zfill(bit_length)


def count_substring_occurrences(bigstr, val):
    count = 0
    for i in range(len(bigstr) - len(val) + 1):
        if bigstr[i:i + len(val)] == val:
            count += 1
    return count


def count_mask_occurrences(mask_hex, bitstream_int):
    mask_bin = convert_hex_to_bin(mask_hex)
    bitstream_bin = convert_int_to_bin(bitstream_int)
    
    return count_substring_occurrences(bitstream_bin, mask_bin)


def main():
    test_cases = []
    
    while True:
        try:
            mask, bitstream = input().split()
            test_cases.append((mask, int(bitstream)))
        except EOFError:
            break

    for i, (mask, bitstream) in enumerate(test_cases):
        count = count_mask_occurrences(mask, bitstream)
        print(f"{i + 1}. {bitstream} contains 0x{mask} {count} times")


if __name__ == "__main__":
    main()




