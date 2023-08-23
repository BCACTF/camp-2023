flag = "camp{y0U_offic1ALLY_Be4t_jAVa_REV_!!}"

guess = ""

length = len(flag)

nums = []

for i in range(length):
    num1, num2 = ord(flag[i])+128, ord(flag[length-i-1])
    nums.append(num1-num2)

print(nums)
