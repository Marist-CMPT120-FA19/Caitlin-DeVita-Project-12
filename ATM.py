#Caitlin De Vita
#caitlin.devita1@marist.edu
#ATM assignment

class Account: 

    def __init__(self, ID, PIN, checking, savings):
        self.ID = ID
        self.PIN = PIN
        self.checking = checking
        self.savings = savings

    def getID(self):
        return self.ID

    def getPIN(self):
        return self.PIN
    
    def getSavings(self):
        return self.savings

    def getChecking(self):
        return self.checking

    def withdraw(self,amount,type):
        if (type==1):

          if (self.savings<amount):
              return False
          else: 
              self.savings -= amount
        elif (type==2):
            if (self.checking<amount):
                return False
            else:
                self.checking -= amount
        return True

    def deposit(self,amount,type):
        if (type==1):
            self.savings += amount
        elif(type==2):
            self.checking += amount

def main():
    account = []
    n=0

    with open("account.txt") as file: 
        for line in file: 
            li = line.split(' ') 
            account.append(Account(li[0],li[1],float(li[2]),float(li[3].replace('\n',''))))
            n += 1 

    userId = input("Enter ID: ")
    userPin = input("Enter PIN: ")
    i=0

    while i<n:
        if(account[i].getID()==userid):
            if(account[i].getPIN()==userpin):
                option = int(input('Enter 1 for withdraw, 2 for transfer, 3 for balance: '))
                if(option==1):
                    type = int(input('Select type 1: Savings or 2: checking: '))
                    amount = float(input("Enter amount: "))
                    if(account[i].withdraw(amount,type)):
                        if(type==1):
                            print(amount,'withdrawn. Closing balance is ',account[i].getSavings())
                        else:
                            print(amount,'withdrwan. Closing balance is ',account[i].getChecking())
                    else:
                        print('Funds in your account are insufficent')
                elif(option==2):
                    option = int(input('Enter 1: Within account transfer, or enter 2: Transfer from/to other account: '))
                    if(option==1): 
                        fromto = int(input('Enter 1. transfer from savings to checking 2. transfer from checking to savings: '))
                        amount = float(input('Enter amount: '))
                        if(fromto==1):
                            account[i].withdraw(amount,1)
                            account[i].deposit(amount,2)
                            print('Transfer from savings to checking complete.')
                        else:
                            account[i].withdraw(amount,2)
                            account[i].deposit(amount,1)
                            print('Transfer from checking to savings complete.')
                    else: 
                        accoundID = input('Enter account ID to transfer money: ')
                        j=0
                        while j<n:
                            if(account[j].getID()==accID):
                                break
                            j += 1
                        if(j<n):
                            type = int(input('Select type 1. Savings 2.checking: '))
                            amount = float(input("enter amount: "))
                            account[i].withdraw(amount,type)
                            account[j].deposit(amount,type)
                            print('Transfer to:',account[j].getID(), 'successful.')
                            if(type==1):
                                print(amount,'transferred, your savings balance is: ',account[i].getSavings())
                            else:
                                print(amount,'transferred, your checking balance is: ',account[i].getChecking())
                        else:
                            print('Invalid ID. Transfer of funds failed.')
                else:
                    type = int(input('Select type 1. Savings 2.checking: '))
                    if(type==1):
                        print('Savings balance:',account[i].getSavings())
                    else:
                        print('Checking balance:',account[i].getChecking())
                break
        i += 1

    if (i==n): 
        print('invalid login')
    else: 
        file = open('account.txt','w')
        j=0
        while j<n:
            file.write(account[j].getID()+' '+account[j].getPIN()+' '+str(account[j].getChecking())+' '+str(account[j].getSavings())+' ')
            j += 1
    file.close() 
    print('Thank you.')

                             

main()
