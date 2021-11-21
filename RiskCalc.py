e = 4200 #default equity
r = .02 #default risk

#calculation functions
def movecalc(c,p,e,r):
    dr = r*e
    pm = move[c]
    n = dr/(pm*p)
    return n

def maxrisk(c,e,r):
    dr = r*e
    pm = move[c]
    p = dr/pm
    return p

def profcalc(c,n,pr):
    pm = move[c]
    p = pr/(pm*n)
    return p
    
def setrisk(c,d):
	pm = move[c]
	p = d/pm
	return p

#future contract point value in dollars
move = {'6A':100000,'6B':62500,'6C':100000,'6E':125000,'6M':500000,'6N':100000,'6J':12500000,'6S':125000,'RB':42000,'CL':1000,'NG':10000,'ZL':600,'ZC':50,'ZS':50,'ZM':100,'ZO':50,'KE':50,'ZW':50,'YM':5,'NQ':20,'RTY':50,'ES':50,'ZB':1000,'ZN':1000,'ZF':250,'ZT':500,'LC':400,'HE':400,'GC':100,'HG':25000,'PL':50,'SI':5000, 'PA':100}

choice = int(input("Enter 1 to calcualte contracts for risk, enter 2 to calculate max risk per contract, enter 3 to calculate number of points for goal, enter 4 to calculte dollar risk move."))
while choice == 1 or choice == 2 or choice ==3 or choice == 4:
    if choice == 1:
        contract = input("Enter contract symbol: ").upper()
        if contract not in list(move.keys()):
            print("Invalid contract")
        else:
            points = float(input("Enter points risk: "))
            equity = float(input("Enter equity: ") or e)
            risk = float(input("Enter risk: ") or r)
            print("Contracts: ",movecalc(contract,points,equity,risk))
            choice = int(input("Enter 1 to calcualte contracts for risk, enter 2 to calculate max risk per contract, enter 3 to calculate number of points for goal, enter 4 to calculte dollar risk move, any other key to quit"))
    elif choice == 2:
        contract = input("Enter contract symbol: ").upper()
        if contract not in list(move.keys()):
            print("Invalid contract")
        else:
            equity = float(input("Enter equity: ") or e)
            risk = float(input("Enter risk: ") or r)
            print("Maxrisk: ",maxrisk(contract,equity,risk))
            choice = int(input("Enter 1 to calcualte contracts for risk, enter 2 to calculate max risk per contract, enter 3 to calculate number of points for goal, enter 4 to calculte dollar risk move, any other key to quit"))
    elif choice == 3:
        contract = input("Enter contract symbol: ").upper()
        if contract not in list(move.keys()):
            print("Invalid contract")
        else:
            num = float(input("Enter number of contracts: "))
            goal = float(input("Enter profit goal: "))
            print("Points: ",profcalc(contract,num,goal))
            choice = int(input("Enter 1 to calcualte contracts for risk, enter 2 to calculate max risk per contract, enter 3 to calculate number of points for goal, enter 4 to calculte dollar risk move, any other key to quit"))
    else:
        contract = input("Enter contract symbol: ").upper()
        if contract not in list(move.keys()):
            print("Invalid contract")
        else:
            risk = float(input("Enter dollar risk: ") or 200)
            print("Maxrisk: ",setrisk(contract,risk))
            choice = int(input("Enter 1 to calcualte contracts for risk, enter 2 to calculate max risk per contract, enter 3 to calculate number of points for goal, enter 4 to calculte dollar risk move, any other key to quit"))
