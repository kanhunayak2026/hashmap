def find_duplicates(numbers):
    seen=set()
    duplicates=set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates
numbers=[1, 2, 3, 2, 4,4, 5, 1, 3]
print(find_duplicates(numbers))