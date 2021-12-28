def stijgende_deellijsten(lijst):
    deellijsten = []
    for i in range(len(lijst)):
        temp_deellijst = []
        if lijst[i] < lijst[i-1] and i != 0:
            k = i-1
            print(k, lijst[k-1], lijst[k])
            while lijst[k-1] < lijst[k]:
                temp_deellijst.insert(0, lijst[k])
                k -= 1
            temp_deellijst.insert(0, lijst[k])
            deellijsten.append(temp_deellijst)
    print(deellijsten)

lijst1 = [1, 2, 3, 1, 2, 4, 8, 6]
stijgende_deellijsten(lijst1)


