# Find longest consecutive range of numbers in list

numbers = [1, 3, 11, 12, 14, 15, 16, 3, 4, 6]


def getMaxConsecutiveInd(index):
    if numbers[index] + 1 == numbers[index + 1]:
        # call the functions if values are consecutive to check next value
        return getMaxConsecutiveInd(index + 1)
    # return last index for consecutive numbers
    return index


max_length, start_index, end_index = 0, 0, 0

i = 0
while i < len(numbers) - 1:
    con_index = getMaxConsecutiveInd(i)
    # if available max_length is less than new_max_length(con_index - i)
    # then change start_index and end_index  
    if max_length < con_index - i:
        max_length = con_index - i
        start_index = i
        end_index = con_index
    # change value of i to latest con_index if i != con_index
    i = con_index if i != con_index else i + 1

print(start_index, end_index, max_length)
Output: (4, 6, 2)

numbers = [1, 2, 3, 4, 5, 6, 7, 11, 12, 14, 15, 16, 17, 18, 3, 4, 6]
Output: (0, 6, 6)
