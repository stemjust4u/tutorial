import os

def functionC3(input_txt):
    import_dir = os.path.relpath(__file__, start=os.curdir)
    comment = input_txt + import_dir + " functionC3"
    return comment

def file_name():
    return __name__

# The file will only be called __main__ when executed directly. 
# So code will only run when file is executed directly and will
# not run when imported
if __name__ == "__main__":
    print(functionC3("called "))
    print(file_name())