def solution(array):
    array.sort()
    middle_index = len(array)//2
    return array[middle_index]

# print(solution([1, 2, 7, 10, 11]))