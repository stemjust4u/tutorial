import os

def functionA2(input_txt):
    import_dir = os.path.relpath(os.path.abspath(__file__), start=os.curdir)
    comment = input_txt + import_dir + " functionA2"
    return comment

# There is no code in this module to run stand alone. Is only useful for importing