def find_sum(nums):
    positive_sum = 0
    negative_sum = 0
    for number in nums:
        if number > 0:
            positive_sum += number
        else:
            negative_sum += number

    strong = "The negatives are stronger than the positives" if abs(negative_sum) > abs(positive_sum) \
        else "The positives are stronger than the negatives"

    return negative_sum, positive_sum, strong


numbers_line = [int(x) for x in input().split()]

print(*find_sum(numbers_line), sep="\n")

# Input: 1 2 -3 -4 65 -98 12 57 -84
# Output:
# -189
# 137
# The negatives are stronger than the positives
