class GoCard():

    # this function will get called once object of GoCard is created
    def __init__(self):
        self.bal = input('Creating Account. Input initial balance: ')

    def receive_command(self):
        while True:

            # try and except block to handle exception
            try:
                s = input('? ')
                # It will split the input using space as separator
                # and create a list of string eg.  r 3.50 become ['r','3.50']
                s = s.split(' ')
                # Now handle different input cases
                if len(s) == 2 and s[0] == 'r':
                    self.bal = float(self.bal) - float(s[1])
                elif len(s) == 2 and s[0] == 't':
                    self.bal = float(self.bal) + float(s[1])
                elif len(s) == 1 and s[0] == 'b':
                    # "%.2f" : used here to print upto two decimal places
                    print('Balance =', '$' + str("%.2f" % self.bal))
                elif len(s) == 1 and s[0] == 'q':
                    break
                else:
                    print('Bad command.')
            except:
                print('Syntax error.')


#####################################
obj = GoCard()  # create object
obj.receive_command()  # call receive_command()
######################################
obj = GoCard()
obj.receive_command()