def partOne(file):
    sum = 0
    for line in file:
        first = 0
        second = 0
        for (i, digit) in enumerate(line.strip()):
            if int(digit)>first and i+1 < len(line.strip()):
                first = int(digit)
                second = 0
            elif int(digit)>second:
                second = int(digit)
        # print(str(first)+str(second))
        sum += int(str(first)+str(second))
    return sum
            

def partTwo(file):
    sum = 0
    for line in file:
        nums =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for (i, digit) in enumerate(line.strip()):
            for (j, num) in enumerate(nums):
                if int(digit)>num and i+12-j<=len(line.strip()):
                    nums[j] = int(digit)
                    nums = [cur if k<=j else 0 for k, cur in enumerate(nums)]
                    break
        # print(int("".join([str(num) for num in nums])))
        sum += int("".join([str(num) for num in nums]))
    return sum
