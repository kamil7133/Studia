def quick_sort(l):
    if len(l) <= 1:
        return l
    n = len(l)
    x = l[0]
    lewa_lista = []
    prawa_lista = []
    for i in range(1, n):
        if l[i] <= x:
            lewa_lista.append(l[i])
        else:
            prawa_lista.append(l[i])

    return quick_sort(lewa_lista) + [x] + quick_sort(prawa_lista)


l = [0, 3, 6, 8, 2, 1, 7, 9, 4, 5, 6]
sorted_list = quick_sort(l)
print(sorted_list)