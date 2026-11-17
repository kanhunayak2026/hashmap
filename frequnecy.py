def count_freq(numbers):
    freq={}
    for num in numbers:
        freq[num]=freq.get(num,0)+1
    return freq
numbers=[10,20,10,30,20,10]
result=count_freq(numbers)
print(result)