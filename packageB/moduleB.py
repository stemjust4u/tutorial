import os
from datetime import date 

def functionB(input_txt):
    """Simple function to output the path of the function"""
    import_dir = os.path.relpath(os.path.abspath(__file__), start=os.curdir)
    comment = input_txt + import_dir + " functionB"
    return comment

def file_name():
    """simple function to output the name of the module"""
    return __name__

#print(functionB.__doc__)
#help(functionB)

class BankAccount:
    """
    This is the help for the class
    """

    # DATA OR ATTRIBUTES
    # Can make these 'private' attributes with '_' to indicate they shouldn't be modified unless using a method
    def __init__(self, initial_amount=0): # self is used to refer to the specific instance of the object
        #creates INSTANCE variables
        self._deposits = []               # putting it inside __init__ makes it create a unique attribute for each instance
        self._balance = initial_amount    # data variable
        self.opendate = date(2021, 2, 15) # can nest classes inside each other

    # ACTIONS OR METHODS    
    def makeDeposit(self, amount):
        self._balance += amount
        self._deposits.append(amount)

    def makeWithdrawal(self, amount):
        self._balance -= amount

    def getBalance(self):
        return self._balance

    def getDeposits(self):
        #copied_list = self._deposits[:] # since list is mutable use a cpy in case somebody creates a cpy in the code and edits it
        return self._deposits              # change this to copied_list to prevent self._deposits from being changed outside our class

# The file will only be called __main__ when executed directly. 
# So code will only run when file is executed directly and will
# not run when imported
if __name__ == "__main__":
    checking = BankAccount(200) # INSTANTIATION. Python will run the __init__ method of BankAccount
    checking.makeDeposit(100)
    checking.makeDeposit(10)
    checking.makeWithdrawal(50)

    print(checking.getBalance())
    false_balance = checking.getBalance() # self._balance is a float and NOT mutable
    false_balance = 9999                  # this false assignment will not affect our self._balance
    print(checking.getBalance()) 

    print(checking.getDeposits())
    false_deposits = checking.getDeposits() # self._deposits is a list and is mutable
    false_deposits[0] = 9999          # If self._deposits is not copied it will get changed.
    print(checking.getDeposits())    # Uncomment the copied_list in getDeposits and run again. 
    
    #print(checking.opendate)
