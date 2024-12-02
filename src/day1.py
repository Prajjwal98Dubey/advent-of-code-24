def solve(l1,l2):
    l1.sort()
    l2.sort()
    ans = 0
    for i in range(len(l1)):
        ans+=abs(l1[i]-l2[i])
    return ans
def main():
    list1 = []
    list2 = []
    while True:
        line = input()
        if line == "":
            break
        else:
            list1_element,list2_element = map(int,line.split())
            list1.append(list1_element)
            list2.append(list2_element)
    ans = solve(list1,list2)
    return ans
print(main())


'''
Tips for input:
    - after writing down the input press enter for coming to "next line" and then again press enter to get the result.

'''