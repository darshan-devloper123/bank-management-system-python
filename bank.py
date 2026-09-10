class Account:
    def __init__(self,id, holder_name):
        self.id  = id
        self.holder_name = holder_name
        self._balance = 0                #Encapsulaion

    def Check_balanace(self):
        print(f"Balance:  {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit suceesfull.. Updated balance: {self._balance}")

    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw suceesfull.. Updated balance: {self._balance}")
        else:
            print("Balance is less than ask...")


class Savings_Account(Account):  #Inheritance
    def caluculate_intrest(self):
        INTREST_RATE = 0.04  #4%
        interest = self._balance * INTREST_RATE
        print(f"Interest: {interest}") 
    
class Current_Account(Account):
    def withdraw(self, amount):     #Polymorphisim
        OVERDRAFT_LIMIT = 1000
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"Withdraw ucessfull.. Updated Balance: {self._balance} ")
        else:
            print("ask is over limits..")

        
class Bank:
    def __init__(self, name ,city):
        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self, id, holder_name, type):
        if type =="savings":
            new_account = Savings_Account(id, holder_name)
        elif type=="current":
            new_account = Current_Account(id,holder_name)
        self.__accounts[id] = new_account
        print("Account creation sucessfull")
        return new_account
        

    def get_account(self,id):
        if id not in self.__accounts:
            print("account Not found..")
        else:
            account = self.__accounts[id]
            print(f"ID: {account.id}\nHolder Name:  {account.holder_name}")
            return account


dbk = Bank("Darshan Bank of karnataka", "Turuvekere")

s1 = dbk.create_account("1","Darshan", "savings")
c1 = dbk.create_account("2", "Virat", "current")


s1.deposit(1000)
c1.deposit(10)

s1.withdraw(2000)
c1.withdraw(20)

s1.caluculate_intrest()

