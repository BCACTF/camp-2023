with open('funfile','rb') as f:
    data = f.read().split(b"\x89PNG")
    with open('solve.png','wb') as f2:
        f2.write(b"\x89PNG")
        f2.write(data[1])
        print('Done')