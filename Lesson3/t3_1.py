# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
# from random import choices

# num = int(input())
# list_nums = choices(range(num * 2), k=num)
# print(list_nums)

# result = list_nums.count(int(input))
# print(result)

# list_nums = [int(input()) for _ in range(int(input()))]
# print(list_nums.count(int(input())))

n = int(input())
a = map(int(input()).split())
x = int(input())
print(sum(map(lambda z: int(z == x), a)))