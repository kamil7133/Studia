

def sortwstawianie(l):
    n = len(l)
    for j in range(1, n):
        x = l[j]
        i = j - 1
        while i>=0 and l[i]>x:
            l[i+1] = l[i]
            i -= 1
        l[i + 1] = x
        j += 1

    return l


l = [0,3,6,8,2,1,7,9,4,5,6]
sorted_list = sortwstawianie(l)
print(sorted_list)
