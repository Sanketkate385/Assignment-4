file_name = "Sample.txt"

def WritingData():
    with open(file_name, 'w') as file:
        Data = input("Enter text to write in file: ")
        file.write(Data)
        print("Data Successfully written in the file", file_name)

def AppendingData():
    with open(file_name, 'a') as file1:
        Data = input("Enter the Additional Data in the file: ")
        file1.write(Data)
        print("Additional Data successfully Added in the file", file_name)

def ReadingData():    
    with open(file_name, 'r') as file2:
        for line in file2:
            line1 = line.strip()
            print(line1)

while True:
    print("1 - Writing the Data\n2 - Appending the Data\n3 - Reading the Data\n4 - Exiting the program")
    num = int(input("Enter the Choice: "))
    if num == 1:
        WritingData()
    elif num == 2:
        AppendingData()
    elif num == 3:
        print("Reading of the Data present in the file: ")
        ReadingData()
    elif num == 4:
        print("Closing the program")
        break
    else:
        print("Invalid Choice")