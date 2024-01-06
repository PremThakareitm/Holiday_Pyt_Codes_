max_line=3
max_bet=1000
min_bet=10

def depo():
    while True:
        a=input("Enter the Amount:Rs.")
        if a.isdigit():
            a=int(a)
            if a>0 :
                print("Valid Amount :)")
                break
            else :
                print("Invalid Amount:Rs")
        else :
            print("Try again.")
        return depo()
        
def get_lines():
    while True:
        b=input("Enter the number of lines to bet on(1-"+str(max_line)+")?")
        if b.isdigit():
            b=int(b)
            if 1<=b<=3 :
                break
            else :
                print("Invalid Number")
        else :
            print("Try again.")
        return get_lines()

def get_bet():
    while True:
        c=input("What would you like to bet?")
        if c.isdigit():
            c=int(c)
            if min_bet<=c<=max_bet :
                break
            else :
                print(f"Amount between {min_bet} and {max_bet}")
        else :
            print("Try again.")
        return get_bet()

def main():
    balance = depo()
    lines = get_lines()
    while True:
        bet_amt= get_bet()
        total_bet= bet_amt * balance
        if total_bet> balance :
            print(f"Your Current Balance: {balance}")
        else :
            break
    print(f"Your betting {bet_amt} on {lines} lines. Total bet is equal to:{total_bet}")
    return get_bet()


main()