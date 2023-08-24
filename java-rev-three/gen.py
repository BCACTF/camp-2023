flag = "camp{y0U_offic1ALLY_Be4t_jAVa_REV_!!}"

guess = ""

length = len(flag)

nums = []

avgs = []

for i in range(length):
    num1, num2 = ord(flag[i])+128, ord(flag[length-i-1])
    nums.append(num1-num2)
    avgs.append((num1-128+num2)/2)

print(nums)
print(avgs)