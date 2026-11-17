def two_sum(numbers,target):
    seen={}
    for i,num in enumerate(numbers):
        comp=target-num
        if comp in seen:
            return [seen[comp],i]
        seen[num]=i

    return None
numbers=[1,2,4,5,7,9]
target=6
print(two_sum(numbers,target))