def list_conjugate(lijst1, lijst2):
    merged_list = []
    if len(lijst1) > len(lijst2):
        s_list, b_list = lijst2, lijst1
    else:
        s_list, b_list = lijst1, lijst2
    for i in range(len(s_list)):
        merged_list.append(lijst1[i])
        merged_list.append(lijst2[i])
    lenght_dif = len(b_list)-len(s_list)
    for i in b_list[-lenght_dif:]:
        merged_list.append(i)
    print(merged_list)

list_conjugate([1, 4, 9, 16], [9, 7, 4, 9, 11])
