array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(9):
    j = i
    while array[j] > array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        j -= 1

for i in range(10):
    print(array[i], end = ' ')

'''
필요할 때만 위치를 바꾸는 방식
시간 복잡도는 마찬가지로 O(n*n)이지만,
최악의 경우를 제외하면, 버블, 선택정렬보다 효율적임
'''