def read_fileandhandle_file():
    file_name = "Test file.txt"     
    try:
        with open("Test file.txt",'r') as file:
            print("Reading content of file: ")
            for line in file:
                line1 = line.strip()
                print(line1)
    except FileNotFoundError:
        print("Error: The File",file_name,"is not Found")
read_fileandhandle_file()