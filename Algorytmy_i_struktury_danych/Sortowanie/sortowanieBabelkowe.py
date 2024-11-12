

def sort_l(l):
    n = len(l)
    i = 1

    while i < n:
        j = n - 1

        while j >=i:
            if l[j - 1] > l[j]:
                bufor = l[j]
                l[j] = l[j -1]
                l[j - 1] = bufor
            j -= 1

        i += 1

    return l


l = [0,3,6,8,2,1,7,9,4,5,6]
sorted_list = sort_l(l)
print(sorted_list)
