def check_for_increase_or_decrease(report):
        increase_flag,decrease_flag = 1,1
        # check for increase of level
        for i in range(1,len(report)):
            if report[i-1] > report[i]:
                increase_flag = 0
                break
        # check for decrease of level
        for i in range(1,len(report)):
            if report[i-1] < report[i]:
                decrease_flag = 0
                break
        return increase_flag or decrease_flag
def is_safe(report):
        is_increase_or_decrease = check_for_increase_or_decrease(report)
        if is_increase_or_decrease:
            for index in range(1,len(report)):
                if abs(report[index]-report[index-1]) < 1 or abs(report[index]-report[index-1]) > 3:
                    return False
            return True
        return False
# for day2 part1
def numberOfSafeReports(reports):
    count_safe_reports = 0
    for r in reports:
        if is_safe(r):
            count_safe_reports+=1
    return count_safe_reports

# for day2 part2
def numberOfSafeReports2(reports):
    def can_single_report_become_safe(report):
        if (is_safe(report)):
            return True
        for i in range(len(report)):
            temp = []
            for j in range(len(report)):
                if i != j:
                    temp.append(report[j])
            if is_safe(temp):
                return True
        return False
    count_safe_reports = 0
    for r in reports:
        if can_single_report_become_safe(r):
            count_safe_reports+=1
    return count_safe_reports            
def main():
    lists = []
    while True:
        line = input()
        if line == "":
            break
        else:
            currList = list(map(int,line.split()))
            lists.append(currList)
    ans = numberOfSafeReports(lists)  # for day2 part1
    ans = numberOfSafeReports2(lists) # for day2 part2
    return ans

print(main())


'''
Tips for input:
- after writing down the input press enter for coming to "next line" and then again press enter to get the result.
'''