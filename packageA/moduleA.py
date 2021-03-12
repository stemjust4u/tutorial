import os

def functionA(input_txt):
    import_dir = os.path.relpath(os.path.abspath(__file__), start=os.curdir)
    comment = input_txt + import_dir + " functionA"
    return comment

def file_name():
    return __name__

# The file will only be called __main__ when executed directly. 
# So code will only run inside this "if" when the file is executed 
# directly and will not run when imported. So it is part module, 
# part script.
if __name__ == "__main__":
    print(functionA("called "))
    print(file_name())