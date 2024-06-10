def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(f"\n{append_content}")

def read_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        content = file.read()
    return contentwrite_file("logfile", "Log 1: 5 bananas added")
    append_file("logfile", "Log 2: 3 bananas subtracted")
    
    print(read_file("logfile"))