def swapFileData():
    first = input("enter the first file: ")
    second = input("enter a second file: ")
    
    with open(first, 'r') as f:
        dataA = f.read()
    
    with open(second, 'r') as b:
        dataB = b.read()

    with open(first, 'w') as f:
        f.write(dataB)
    
    with open(second, 'w') as b:
        f.write(dataA)

swapFileData()