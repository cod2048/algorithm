array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(array)):
    for j in range(9-i):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp;

for i in range(10):
    print(array[i], end=" ")


"""
버블정렬:
옆에 있는 값과 비교해서 더 작은 값을 앞으로 보내는 방법
-> 한 번 반복 시 가장 큰 값이 맨 오른쪽으로 보내짐

버블정렬의 시간 복잡도:
10 + 9 + 8 + 7 + ... + 1
=> n*(n+1) / 2
=> O(n*n)
이지만 바로 옆과의 자리를 계속 바꿔야한다는 점에서 
실제로는 선택정렬보다 더 비효율적임
-> 정렬 알고리즘에서 가장 느림
"""