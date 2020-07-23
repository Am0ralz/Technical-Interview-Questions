# 1.5 Implementation a method to perform basic string compression using the count of repeated characters.


def Compression(s):
    s = sorted(s)
    comp = []
    count = 0
    comp.append(s[0])
    ans = ""
    for i in s:
        if i == comp[-1]:
            count = count + 1
        else:
            comp.append(str(count))
            comp.append(i)
            count = 1
    comp.append(str(count))
    return ans.join(comp)


print(Compression("aaaaabbbcc"))
