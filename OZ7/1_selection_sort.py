"""
Schrijf een functie selection_sort dat een lijst in dalende volgorde sorteert m.b.v. selection sort.
"""
def selection_sort(lijst):
    for i in range(len(lijst)):
        max_idx = i
        for j in range(i+1, len(lijst)):
            if lijst[j] > lijst[max_idx]:
                max_idx = j
        lijst[i], lijst[max_idx] = lijst[max_idx], lijst[i]
    return lijst

assert(selection_sort([1, 3, 45, 32, 65, 34]) == [65, 45, 34, 32, 3, 1])
assert(selection_sort([1]) == [1])
assert(selection_sort([54, 29, 12, 92, 2, 100]) == [100, 92, 54, 29, 12, 2])
