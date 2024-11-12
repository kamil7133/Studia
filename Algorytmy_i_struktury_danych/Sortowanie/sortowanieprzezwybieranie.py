def sort_select(l):
    n = len(l)

    for i in range(n - 1):
        k = i
        print(f"k pierwsza petla = {l[k]}")
        x = l[i]
        print(f"x pierwsza petla = {x}")

        for j in range(i + 1, n):
            if l[j] < x:
                k = j
                print(f"k druga petla = {l[k]}")
                x = l[j]
                print(f"x druga petla = {x}")

        l[k], l[i] = l[i], l[k]
        print(f"l[k]: {l[k]}, l[i]: {l[i]}")
        print(f"lista: {l}")

    return l

l = [1,2,3,4,5,6,7,8,9]
sort_selected = sort_select(l)
print(sort_selected)