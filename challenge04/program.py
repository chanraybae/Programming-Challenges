# Name: Chanwoo Ray Bae
# Course: Programming Challenges
# Assignment: Challenge06
# Time, Space Complexity: O(logn), O(1)

def left_half(arr, lower, midpt, target):
    return arr[lower] <= target < arr[midpt]

def right_half(arr, midpt, upper, target):
    return arr[midpt] < target <= arr[upper]

def search_in_pivoted(arr, lower, upper, target):
    while lower <= upper:
        midpt = (lower + upper) // 2
        # Evaluation metrics for matching
        
        if arr[midpt] == target:
            return f"{target} found at index {midpt}"

        if arr[lower] <= arr[midpt]:
            if left_half(arr, lower, midpt, target):
                upper = midpt - 1
            else:
                lower = midpt + 1
        else:
            if right_half(arr, midpt, upper, target):
                lower = midpt + 1
            else:
                upper = midpt - 1

    return f"{target} was not found"

def main():
    while 1:
        try:
            arr = list(map(int, input().split()))
            # casting as int jic
            target = int(input())
            # Final output
            print(search_in_pivoted(arr, 0, len(arr) - 1, target))
        except EOFError:
            break

if __name__ == "__main__":
    main()
