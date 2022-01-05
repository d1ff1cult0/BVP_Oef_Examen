"""
Gegeven twee versies van het bubble sort-algoritme. Bereken de tijdscomplexiteit van beiden. Maakt het een
wezenlijk verschil welke versie je gebruikt? Presteren ze anders onder het `best case scenario' of het `worst case
scenario'?
"""


def bubble_sort_left_to_right_suboptimal(lst):
    sorted_until = 0
    it = 0
    while sorted_until != len(lst):
        it += 1
        index_min = len(lst) - 1
        while index_min != sorted_until:
            it += 1
            if lst[index_min - 1] > lst[index_min]:
                lst[index_min - 1], lst[index_min] = lst[index_min], lst[index_min - 1]
            index_min -= 1
        sorted_until += 1
    print(it)
    return lst

# Worst case: O(n^2)
# Best case: O(n^2)
# Overall: O(n^2)
bubble_sort_left_to_right_suboptimal([9, 8, 7, 6, 5, 4, 3, 2, 1])
bubble_sort_left_to_right_suboptimal([1, 2, 3])



def bubble_sort_left_to_right(lst):
    sorted_until = 0
    it = 0
    while sorted_until != len(lst):
        it += 1
        begin = len(lst) - 1
        end = begin + 1
        while begin != sorted_until:
            it += 1
            if lst[begin - 1] > lst[begin]:
                lst[begin - 1], lst[begin] = lst[begin], lst[begin - 1]
                end = begin - 1
            begin -= 1
        sorted_until = end

    print(it)
    return lst

# Worst case: O(n^2)
# Best case: O(n)
# Overall:
bubble_sort_left_to_right([9, 8, 7, 6, 5, 4, 3, 2, 1])
bubble_sort_left_to_right([1, 2, 3])
