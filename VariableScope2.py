# from python docs

def do_local():
    spam = "local spam"
    spamL[0] = spam

def do_global():
    global spam
    spam = "global spam"
    spamL[0] = spam

spam = "test spam"           # int, float, string  are IMMUTABLE
spamL = ["test spam list"]   # lists, dict, objects are MUTABLE
print("starts as test spam")
do_local()
print("After local  assign string NOT changed:", spam)
print("After local  assign   list IS changed", spamL[0])

do_global()
print("After global assign string IS changed:", spam)
print("After global assign   list IS changed", spamL[0])