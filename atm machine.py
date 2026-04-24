class ATM:
   def _init_(self):
      self.pin=""
      self.balance=0
      self.menu()

   def menu(self):
       userinput= input("""
              hello how i can help you
               1.press 1 to create pin.
               2.press 2 to change pin.
               3.press 3 to check balance.
               4.press 4 to withdraw.
               5.anything else to exit.
""")
