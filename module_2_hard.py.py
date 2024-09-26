for i in range(3, 21):
    sum = " "
    for j in range(1, i):
        for k in range(j+1, i):
            if i % (j+k) == 0:
                sum += str(j) + str(k)
    print(str(i) + " -" + str(sum))




