flag = "bcactf{Y0u_4Re_4_X0R_Ch4mp1On_!!}"

inp = input()

outBits = ""

for index in range(len(inp)):
    flagIndex = index%len(flag)

    flagBits = format(ord(flag[index]), '08b')
    inputBits = format(ord(inp[index]), '08b')

    for bitIndex in range(8):
        result = int(flagBits[bitIndex]) ^ int(flagBits[bitIndex])
        outBits += str(result)

out = ""

for i in range(0, len(outBits), 8):
    value = int(outBits[i:i+8], 2)

    out+=f"{value:x}"

print(out)
