class Bank:
    balance=5000
    def login(self,pin):
        if pin==1111:
            return True
        else:
            return False
    def credit(self,amt):
        self.balance+=amt
    def debit(self,amt):
        self.balance-=amt
    def display(self):
        print("Saldo anda adalah "+str(self.balance))
obj = Bank()
flag=False
for i in range(1,4):
       if obj.login(int(input("Masukan Pin anda : "))):
           flag=True
           break
if flag:
  while True:
     o=input("""
             1. Informasi Saldo
             2. Tambah Saldo
             3. Tarik Saldo
             0. Keluar""") 
     if o=='2':
      obj.credit(int(input("enter amount for credit")))
      print("After credit total amount is ")
      obj.display()
     elif o=='3':
      amt=int(input("enter amount for debit"))
      if amt<obj.balance:
       obj.debit(amt)
       print("After debit total amount is ")
      else:
       print("insufficient balance")
      obj.display()
     elif o=='1':
      print("Total balance is ")
      obj.display()
     elif o=='0':
       exit(0)
else:
        print("Your pin code attempt has been completed")