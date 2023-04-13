array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(array)):
    index = i
    for j in range(i, len(array)):
        if array[index] > array[j]:
            index = j
    array[i], array[index] = array[index], array[i]

for k in range(len(array)):
    print(array[k], end=' ')

"""
선택 정렬 :
가장 작은 값을 선택해서 앞으로 보내는 방법

선택정렬의 시간 복잡도
10 + 9 + 8 + 7 + .. + 1
-> 10 * (10 + 1) / 2 = 55
-> n * (n + 1) /2
-> 대략적으로 O(n*n) 
"""
