'''
def calibration_result(data):
    res = 0 
    for d in data:
        combinations = []
        curr = []
        def dfs(n):  # n = number of operators required  "+","*"
            if n == 0:
                combinations.append(curr.copy())
                return
            curr.append("+")
            dfs(n-1)
            curr.pop()
            curr.append("*")
            dfs(n-1)
            curr.pop()
            return
        dfs(len(d)-2)
        for combination in combinations:
            prev = 0
            if combination[0] == "+":
                prev = d[1] + d[2]
            else:
                prev = d[1] * d[2]
            index = 3
            i = 1
            while i < len(combination) and index < len(d):
                if combination[i] == "+":
                    prev = prev + d[index]
                else:
                    prev = prev * d[index]
                index+=1
                i+=1
            if prev == d[0]:
                res += prev
                break
    return res       

'''        

# Part 2
def calibration_result(data):
    res = 0 
    dp = {}
    for d in data:
        combinations = []
        curr = []
        def dfs(n):  # n = number of operators required  "+","*"
            if n == 0:
                combinations.append(curr.copy())
                return
            curr.append("+")
            dfs(n-1)
            curr.pop()
            curr.append("*")
            dfs(n-1)
            curr.pop()
            curr.append("||")
            dfs(n-1)
            curr.pop()
            return
        if (len(d)-2 in dp):
            combinations = dp[len(d)-2]
        else:
            dfs(len(d)-2)
            dp[len(d)-2] = combinations
        for combination in combinations:
            prev = 0
            if combination[0] == "+":
                prev = d[1] + d[2]
            elif combination[0] == "*":
                prev = d[1] * d[2]
            else:
                prev = int(str(d[1]) + str(d[2]))
            index = 3
            i = 1
            while i < len(combination) and index < len(d):
                if combination[i] == "+":
                    prev = prev + d[index]
                elif combination[i] == "*":
                    prev = prev * d[index]
                else:
                    prev = int(str(prev) + str(d[index]))
                index+=1
                i+=1
            if prev == d[0]:
                res += prev
                break
    return res           

def main():
    given_data = []
    while True:
        line = input()
        if line:
            t1 = line.split(":")
            t2 = t1[1].split(" ")
            sub = [int(c) for c in t1[:1] + t2[1:]]
            given_data.append(sub)
        else:
            break
    res = calibration_result(given_data)
    return res

print(main())