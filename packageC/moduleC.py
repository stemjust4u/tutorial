import os

def functionC(input_txt):
    import_dir = os.path.relpath(os.path.abspath(__file__), start=os.curdir)
    comment = input_txt + import_dir + " functionC"
    return comment

def file_name():
    return __name__

# The file will only be called __main__ when executed directly. 
# So code will only run when file is executed directly and will
# not run when imported
if __name__ == "__main__":
    print(functionC("called "))
    print(file_name())