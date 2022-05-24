class InsufficientFundsException(Exception):
    def __init__(self,arg):
        self.msg = arg
        
amount  = int(input("Enter Amount:"))
try:
    if amount > 500:
        print("Go to Movie")
    else:
        raise InsufficientFundsException("Go to PG")
except InsufficientFundsException as msg:
    print(msg)