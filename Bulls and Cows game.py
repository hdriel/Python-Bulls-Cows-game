import random
import math

# Hadriel Benjo

msg_sum   = "Sum of all digit  : "
msg_mul   = "Mul of all digit  : "
msg_even  = "The  even digits  : "
msg_big   = "The big(>5) digits: "
msg_asc   = "Is ascending(<<<)?: "
msg_prime = "The prime digits  : "


        
def game():
    digits = 3 # here you can change to any amount of  digit you want to guess
    num = random.randint((int)(math.pow(10, digits-1)), (int)(math.pow(10, digits)-1))# random 100-999
    points = 100
    Feild = 10 # here you can change to any amount of chances to guessing
    print(num, "welcome to guess game! \nYou have " ,Feild, " changes to guess my random num of 3 digit.\nIn every try I give you a tip for helping the calculate the number.\n")

    def printGameOver(num):
        print('\n\n')
        print("\t########################################")
        print('\t#### Game over! The number was: {0:3} ####'.format(num))
        print("\t########################################\n\n")
    
    def getMessage():    
        m = random.randint(1, 6) # random 1-6
        if   m == 1: return msg_sum 
        elif m == 2: return msg_mul 
        elif m == 3: return msg_even 
        elif m == 4: return msg_big 
        elif m == 5: return msg_asc 
        elif m == 6: return msg_prime
        
    def getFunction(msg):
        def sumList(numbers):  
            total = 0
            lst_digits = [int(i) for i in str(numbers)]
            for x in lst_digits:
                total += x  
            return total

        def multiply(numbers):  
            total = 1
            lst_digits = [int(i) for i in str(numbers)]
            for x in lst_digits:
                total = total * x  
            return total

        def eventStr(numbers):  
            res = ""
            lst_digits = [int(i) for i in str(numbers)]
            for x in lst_digits:
                if x%2 == 0: res = res + "X"
                else       : res = res + "-"
            print(res)

        def bigStr(numbers):  
            res = ""
            lst_digits = [int(i) for i in str(numbers)]
            for x in lst_digits:
                if x > 5 : res = res + "X"
                else     : res = res + "-"
            print(res)

        def ascStr(numbers):
            res = "AAA"
            lst_digits = [int(i) for i in str(numbers)]
            return sorted(lst_digits) == lst_digits

        
        def primeStr(numbers):  
            res = ""
            lst_digits = [int(i) for i in str(numbers)]
            for x in lst_digits:
                if x == 2 or x == 3 or x == 5 or x == 7 or x == 9:
                    res = res + "X"
                else     : res = res + "-"
            print(res)

        if   msg == msg_sum  : return lambda d: sumList(d)
        elif msg == msg_mul  : return lambda d: multiply(d)
        elif msg == msg_even : return lambda d: eventStr(d)
        elif msg == msg_big  : return lambda d: bigStr(d)
        elif msg == msg_asc  : return lambda d: ascStr(d)
        elif msg == msg_prime: return lambda d: primeStr(d) 

    def printTip():
        msg = getMessage()
        f = getFunction(msg)
        printF1(msg, f)
        printF2(msg, f)
        
    def printF1(msg, f):
        if msg == msg_sum   or msg == msg_mul  or msg == msg_asc :
            print("\n\tTip: ", msg, f(num)) 
    def printF2(msg, f):
        if msg == msg_even  or msg == msg_big  or msg == msg_prime  :            
            print("\n\tTip: ", msg, end = " ")
            f(num)
            
    # the game loop
    tryUser = 1
    while(points>0):
        
        if points - Feild <= 0:
            print('\n!!!!! Be careful - This is your last attempt !!!!!')
            
        printTip()
        guess = input('{0:2}) Enter num of 3-digits[or \'Enter\' to finish]: '.format(tryUser))
        tryUser = tryUser +1
        
        while(not ((guess.isnumeric() and len(guess) == digits) or guess == "")):
            guess = input('\n### Invalid Input!\n\n{0:2}) Enter num of 3-digits [or \'Enter\' to finish]: '.format(tryUser-1))
            
        if(guess == ""):
            ans = ""
            print('\n')
            while not(ans == "Y" or ans == "y" or ans == "N" or ans == "n"):
                ans = input('### Do you want to finish and exit the game? [Y|N] : ')
            if ans == 'Y' or ans == 'y':
                printGameOver(num)
                return True;
            else: print('return to continue the game...')
            
        else:
            guess = int(guess)
            
        if(guess == num):
            print('\n\n')
            print('\t****************************************')
            print('\t**** Yes correct! you win {0:2} points ****'.format(points))
            print('\t****************************************\n\n')
            return;

        points = points - Feild
        
    if(points <= 0):
        printGameOver(num) 



if __name__ == "__main__":
    repeat = True
    while(repeat):
        if (not game()):
            ans = ""
            print('\n')
            while not(ans == "Y" or ans == "y" or ans == "N" or ans == "n"):
                ans = input('### Do you want to play again? [Y|N] : ')
            if ans == 'Y' or ans == 'y':
                print('=====================================================')
                print('Restart the game again...')
                print('\n\n\n\n')
                repeat = True
            else:
                repeat = False
        else: repeat = False
    print('Good-bay')
    


    
