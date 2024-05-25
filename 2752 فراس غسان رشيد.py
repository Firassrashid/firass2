# فراس غسان رشيد 2752  

# Q1.A   :
#  طريقة1
l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,443,21,53]
d={k:v for (k,v) in zip (l1,l2)}
print(d)


# طريقة2
d2={}
for i in range (len(l1)):
    d2[l1[i]]=l2[i]
print(d)    

#Q1.B  :
n=int(input('inter the number'))
f=1
if n<0:
    print('there is no factorial for negative numbers')
elif n==0:
    print(1)
else :
    for i in range(1,n+1):
        f=f*i
    print('the factorial of ',n,' is ',f)  

#Q1.C    :

#طريقة 1 :
l3=['Network','Bio','Programming','Physics','Music']
l4=[i for i in l3 if i.startswith('B')]
print(l4)

#طريقة2  :
l5=[]
for i in l3:
    if i.startswith('B'):
        print(i)


#Q1.D    :

d3={n:n+1 for n in range(11)}
print(d3)


#Q2     :

B_number=input('inter the binary number : ')
D_number=int(B_number,2)
print('the decimal of ',B_number,'is: ',D_number)


#Q3       :

import json
questions = { }
scores = 0
number=1
f = open("D:\\جامعة 2\بايثون\questions.json",'r')
questions = json.load(f)
f.close()

print("python quiz programm")
name = input("Enter your full name: ")
print("Enter 't' for True or 'f' for False")

for Q in questions.keys():
    print("Question",number,": ", Q)
    ans = input("The answer is ")
    if ans == questions[Q]:
        scores = scores + 1
        print("Correct ")
    else:
        print ("Wrong")
    number = number + 1

result={name:scores}
m = open("score.txt",'w')
result = json.dump(result,m)
m.close()
           



#Q_4       :


class BankAccount:
    def __init__(self,account_number,account_holder,balance=0.0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount)    :
        if self.balance>=amount:
              self.balance-=amount
              return self.balance
            
           
        else :
             print("miuns chip")
        
    def get_balance(self):
         return self.balance

Account1 =BankAccount("2752","firass rashid")

Account1.deposit(1000)
print("the balance after added this deposit is : ",Account1.get_balance())

Account1.withdraw(500)
print("the balance after withdrawal is : ",Account1.get_balance())         


class SavingAccount(BankAccount):
     def __init__(self,account_number,account_holder,interest_rate):
          super().__init__(account_number,account_holder)
          self.interest_rate=interest_rate

     def apply_inter(self):
          inter_amount=self.balance*self.interest_rate
          self.deposit(inter_amount)     


     def print(self):
          print("the last balance is :",self.get_balance)
          print("interest rate is : ",self.interest_rate)


S_Account=SavingAccount("25468","ahmad",0.03)
S_Account.apply_inter()
S_Account.print()          



   


        