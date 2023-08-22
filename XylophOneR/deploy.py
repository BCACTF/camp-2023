def hexify(string):
    out = ""

    for i in string:
        out+=f"{ord(i):2x}"

    return out

flag = hexify("bcactf{Y0u_4Re_4_X0R_Ch4mp1On_!!}")

inp = hexify(input())

outBits = ""

for index in range(0, len(inp), 2):
    flagIndex = index%len(flag)

    flagBits = format(int(flag[flagIndex:flagIndex+2], 16), '08b')
    inputBits = format(int(inp[index:index+2], 16), '08b')

    for bitIndex in range(8):
        result = int(flagBits[bitIndex]) ^ int(inputBits[bitIndex])
        outBits += str(result)

out = ""

for i in range(0, len(outBits), 8):
    value = int(outBits[i:i+8], 2)
    out+=f"{value:02x}"

print(out)