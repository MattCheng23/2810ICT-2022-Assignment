class GoCardTransportService:

    transactions = {'events': [], 'amounts': [], 'balance': []}
    balance = 0

    def __init__(self, balance):
        self.balance = balance
        self.transactions['events'].append('Intial balance')
        self.transactions['amounts'].append(' ')
        self.transactions['balance'].append(100 / 1.0)

    def ride(self, amount):
        if (self.balance >= amount):
            self.balance = self.balance - amount
            self.transactions['events'].append('Ride')
            self.transactions['amounts'].append(amount)
            self.transactions['balance'].append(self.balance)
        else:
            print('Bad command')

    def topup(self, amount):
        if (amount < 0):
            print("Bad command")
            return
        self.balance += amount
        self.transactions['events'].append('Top up')
        self.transactions['amounts'].append(amount)
        self.transactions['balance'].append(self.balance)

    def currentBalance(self):
        return self.balance

    def printStatemet(self):
        print("{:<15} {:<15} {:<15}".format('event', 'amount ($)', 'balance ($)'))
        for i in range(len(self.transactions['events'])):
            print("{:<15} {:<15} {:<15}".format(self.transactions["events"][i], self.transactions["amounts"][i],
                                                self.transactions["balance"][i]))
            print("{:<15} {:<15} {:<15}".format("Final balance", " ", self.balance))


intialBalance = int(input('Creating account. Input intial balance: '))
account = GoCardTransportService(intialBalance)
command = ""

while (command != 'q'):
    command = input('?')
    inputs = command.split(' ')
    length = len(inputs)
    if (inputs[0] == 'r' and length == 2 and inputs[1].replace('.', '',
                                                               1).isdigit()):
        account.ride(float(inputs[1]))
    elif (inputs[0] == 't' and length == 2 and inputs[1].replace('.', '',
                                                                 1).isdigit()):
        account.topup(float(inputs[1]))
    elif (inputs[0] == 'b' and length == 1):
        print("Balance = $" + str(account.currentBalance()))
    elif (inputs[0] == "q" and length == 1):
        break
    else:
        print('Bad command')

print('\n')
print('Statement:')
account.printStatemet()