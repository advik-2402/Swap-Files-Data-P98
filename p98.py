def swapFileData():
    file1 = input("Enter 1st file: ")
    file2 = input("Enter 2nd file: ")

    text1 = open(file1, 'r+')
    data_a = text1.read()

    text2 = open(file2, 'r+')
    data_b = text2.read()

    write1 = open(file1, 'w+')
    write1.write(data_b)

    write2 = open(file2, 'w+')
    write2.write(data_a)

swapFileData()