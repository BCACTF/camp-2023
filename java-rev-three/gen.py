
flag = "camp{y0U_offic1ALLY_Be4t_jAVa_REV_!!}"
encryptString = "qxwfrKpXJeAChMnLCHbERWO2zc701ZPxURtFi"

guess = ""

length = len(flag)

nums = []

avgs = []

for i in range(length):
    num1, num2 = ord(flag[i]), ord(encryptString[i])
    nums.append(num1-num2)

print(nums)