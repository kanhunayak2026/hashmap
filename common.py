def find_common(arr1,arr2):
    set1=set(arr1)
    common=[]
    for num in arr2:
        if num in set1 and num not in common:
            common.append(num)
    return common
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

print(find_common(arr1, arr2))
