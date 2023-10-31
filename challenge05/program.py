# Name: Chanwoo Ray bae
# Course: Programming Challenge
# Challenge05
# Time, space complexity met

# data maps
size_rank = {"small": 0, "medium": 1, "large": 2}
size_to_sil = {"small": ".", "medium": ":", "large": "|"}
type_rank = {"gel": 0, "tablet": 1}

def bottle_sort_criteria(bottle):
    med_name, bottle_size, pill_type =  bottle
    return type_rank[pill_type], med_name, size_rank[bottle_size]

def sort_then_sil(bottle_count, mini_stliams):
    mini_stliams.sort(key = bottle_sort_criteria)
    
    sil = "".join(size_to_sil[size] for name, size, type in mini_stliams)
    return sil

def main():
    while 1:
        try:
            n = int(input())
            mini_stliams = [input().split() for _ in range(n)]

            print(sort_then_sil(n, mini_stliams))
        except EOFError:
            break

if __name__ == "__main__":
    main()
