def longest_cos(numbers):
    num_set=set(numbers)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            current_num=num
            count=1
            while current_num +1 in num_set:
                current_num+=1
                count+=1
                longest=max(longest,count)
    return longest
numbers = [100, 4, 200, 1, 3, 2,5]

print(longest_cos(numbers))