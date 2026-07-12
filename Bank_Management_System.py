from abc import ABC,abstractmethod
class Account(ABC):
    _AccountBalance = 1000
    def __init__(self,AccountHolder : str,AccountNumber : int):
        self.AccountHolder = AccountHolder
        self._AccountNumber = AccountNumber
        self._with_draw_history = []
        self._deposit_history = []

    def AccountDetails(self):
        print("Account Holder : ",self.AccountHolder)
        print("Account number : ",self._AccountNumber)
        print("Current Balance($) : ",self._AccountBalance)

    def Deposit(self,credit_money : int):
        if(credit_money <= 0):
            print("Deposit cancelled!")
            return
        self._AccountBalance = self._AccountBalance + credit_money
        self._deposit_history.append(("You deposited "+str(credit_money)+"$ in your account!"))
        print(f"Amount of {credit_money}$ credited successfully!")
        print(f"Your current balance is : {self._AccountBalance}$")
        print("")

    @abstractmethod
    def WithDraw(self,debit_money : int):
        pass

    def CheckBalance(self):
        print(f"Dear user your current balance is : {self._AccountBalance}$")
        print("")

    def TransferMoney(self,target_account,amount):
        if(self._AccountBalance < amount):
            print(f"Due to out of balance you cannot transfer money of {amount}$.")
            self.CheckBalance()
            return
        self._AccountBalance = self._AccountBalance - amount
        target_account._AccountBalance = target_account._AccountBalance + amount
        print(f"Amount of {amount}$ tranfered successfully to the destination account")
        self.CheckBalance()
        target_account._deposit_history.append(f"Amount of {amount}$ credited from {self._AccountNumber}")
        self._with_draw_history.append(f"Amount of {amount}$ debit from your account to {target_account._AccountNumber}")

    def AccountHistory(self):
        if (len(self._deposit_history) == 0 and len(self._with_draw_history) == 0):
            print("No transactions found!")
            print("")
            return
        for i in self._deposit_history:
            print(i)
        for i in self._with_draw_history:
            print(i)
        print("")

class SavingsAccount(Account):
    def __init__(self,Accountolder : str,AccountNumber: int):
        self.interest = 4.0 #interest rate in percent (4 percent)
        self._with_draw_count = 0
        super().__init__(Accountolder,AccountNumber)

    def WithDraw(self,debit_money : int):
        if(self._with_draw_count >= 3):
            print("You have reached maximum withdraws please try again on next month!")
            return
        if(self._AccountBalance - debit_money < 1000):
            print("You cannot with draw because the minimum balance should be 1000!")
            super().CheckBalance()
            return
        self._with_draw_count = self._with_draw_count + 1
        super().WithDraw(debit_money)

    def calculate_interest(self,time_period : int):
        interest = (self._AccountBalance * float(time_period) * self.interest) / float(100)
        print(f"You have earned an interset amount of {self.interest}!")
        self._AccountBalance = self._AccountBalance + interest
        super().CheckBalance()

class GeneralAccount(Account):
    def __init__(self,AccountHolder : str,Accountnumber : int):
        super().__init__(AccountHolder,Accountnumber)

    def WithDraw(self,debit_amount : int):
        if(self._AccountBalance - debit_amount < -2000):
            print(f"With drawn cancelled due to overdraft!")
            super().CheckBalance()
            return
        self._AccountBalance = self._AccountBalance - debit_amount
        print(f"With draw of {debit_amount} has completed!")
        super().CheckBalance()

class LoanAccount(Account):
    def __init__(self,AccountHolder : str,AccountNumber : int):
        super().__init__(AccountHolder,AccountNumber)
        self._interest_rate = 10 #10%
        self._AccountBalance = 0
        self.emi = 0

    def TakeLoan(self,loan_amount : int,timeperiod : int):
        print(f"Loan of {loan_amount}$ approved successfully for {timeperiod} years!")
        self.CalculateEmi(loan_amount,timeperiod)
        self._AccountBalance = -1 * ((loan_amount * timeperiod * self._interest_rate) / 100 + loan_amount)
        print("")

    def CalculateEmi(self,loan_amount : int,timeperiod : int):
        #time period in years
        interset_money = (loan_amount * timeperiod * self._interest_rate) / 100
        emi = (loan_amount + interset_money) / (12 * timeperiod)
        self.emi = emi
        print(f"Your EMI is {emi}$")

    def PayEmi(self):
        print(f"Emi for this month has paid successfully!")
        self._AccountBalance = self._AccountBalance + self.emi
        self._deposit_history.append(f"Emi of {self.emi}$ paid successfully!")
        super().CheckBalance()

    def LoanStatus(self):
        if(self._AccountBalance == 0):
            print("Loan cleared successfully")
            print("")
            return
        print(f"Loan in Pending")
        super().CheckBalance()

    def WithDraw(self,debit_amount):
        print("You cannot with draw amount from this account since it is loan account!")
        print("")
        self._with_draw_history.append(f"With draw of {debit_amount}$ cancelled due to loan account!")

savings_account = SavingsAccount("Teja",95959595959595959)

general_account = GeneralAccount("Rajesh",95959595959590909)
general_account.TransferMoney(savings_account,900)

savings_account.AccountHistory()
general_account.AccountHistory()

savings_account.CheckBalance()
general_account.CheckBalance()