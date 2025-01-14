def shell_sort(l):
    n = len(l)
    zamiana = False
    delta = n
    while not zamiana:
        if delta >= 1:
            delta = delta // 2
            while True:
                zamiana = False
                i = 0
                while i <= n - delta - 1:
                    if l[i] > l[i + delta]:
                        bufor = l[i + delta]
                        l[i + delta] = l[i]
                        l[i] = bufor
                        zamiana = True
                    i += 1
                if not zamiana:
                    break
        else:
            zamiana = True
    return l


l = [0,3,6,8,2,1,7,9,4,5,6]
sorted_list = shell_sort(l)
print(sorted_list)
