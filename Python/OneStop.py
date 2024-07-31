# Description: A program for One Stop Insurance Company to enter and calculate 
# new insurance information for it's customers
# Author: Melanie Adams
# Date(s): July 24 2024 - July 30 2024


# Define required libraries.
from datetime import datetime
import time

# Define program constants.
# from const.dat
constf = open('const.dat', 'r')
constants = constf.readlines()
polNum = constants[0].strip()
basePrem = constants[1]
basePrem = float(basePrem)
discountRate = constants[2]
discountRate = float(discountRate)
extraLiabilityFee = constants[3]
extraLiabilityFee = float(extraLiabilityFee)
glassFee = constants[4]
glassFee = float(glassFee)
loanerCarFee = constants[5]
loanerCarFee = float(loanerCarFee)
HSTrate = constants[6]
HSTrate = float(HSTrate)
monthProcessingFee = constants[7]
monthProcessingFee = float(monthProcessingFee)
constf.close()

# from claims.dat        
claims = [] 

with open('claims.dat', 'r') as file:
    lines = file.readlines()
    for line in lines:
        claims_info = line.split(',')
        claims.append(claims_info)
# REMEMBER for next time: global variables are usually all caps

# Define the loading bar function
def loading_bar(duration, length=50):
    for i in range(length + 1):
        # Calculate the percentage of completion
        percent = (i / length) * 100
        # Create the bar string
        bar = '#' * i + '-' * (length - i)
        # Print the loading bar on the same line
        print(f'\r[{bar}] {percent:.2f}%', end='', flush=True)
        # Sleep for a fraction of the duration
        time.sleep(duration / length)


# Main report processing starts here.
while True:
 #function variables
  provinces = ['NL', 'NS', 'NB', 'PE', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']

#user inputs
  fName = input('Please enter customer first name: ').title()
  lName = input('Please enter customer last name: ').title()
  fullName =  fName + " " + lName
  custAdd = input("Please enter the customer's street address: ").title()
  custCity = input("Please enter the customer's city: ").title()

  while True:
    custProv = input("Please enter the customer's province (##): ").upper()
    if custProv not in provinces:
      print("Province not valid. Please re-enter as 2 letter province code.")
    else:
       break
    
  custPC = input("Please enter customer's postal code (X#X #X#): ").upper()
  custPhone = input("Please enter customer's phone number (### ### ####): ")
  numCarsIns = input("Please enter the number of cars: ").strip()
  numCarsIns = int(numCarsIns)
  extraLiability = input("Extra liability for up to $1 000 000? (Y/N): ").strip().upper()[0]
  optGlassCov = input("Glass coverage (Y/N): ").strip().upper()[0]
  optLoanerCar = input("Loaner car (Y/N): ").strip().upper()[0]

  while True:
    paymentType = input("Please select option for payment type (full (F), monthly (M), down payment (D)): ").strip().upper()[0]
    if paymentType not in ['F', 'M', 'D']:
      print("Not a valid option. Please choose from full (F), monthly (M), down payment (D).")  
    else:
      break    

# calculations
  if paymentType == 'D':
    downValue = input("Please enter the down payment amount: ")
    downValueAMT = float(downValue)
  else:
    downValueAMT = 0

  if numCarsIns == 1:
    insPrem = basePrem
  else:
    insPrem = basePrem + (basePrem * (1 - discountRate)) * (numCarsIns - 1)   

# optional coverage
  if extraLiability == 'Y':
    extraLiabilityAmount = extraLiabilityFee * numCarsIns
  else: 
    extraLiabilityAmount = 0
  if optGlassCov == 'Y':
    optGlassCovAmt = glassFee * numCarsIns
  else:
    optGlassCovAmt = 0
  if optLoanerCar == 'Y':
    optLoanerCarAmt = loanerCarFee * numCarsIns
  else:
    optLoanerCarAmt = 0

  totalExtraCost = extraLiabilityAmount + optLoanerCarAmt + optGlassCovAmt
  subtotal = insPrem + totalExtraCost
  HSTAmt = HSTrate * subtotal
  total = subtotal + HSTAmt
  totalAMT = float(total)
  monthPay = total / 8

  if paymentType == 'D':
    monthPayAMT = (totalAMT + monthProcessingFee - downValueAMT) / 8
  elif paymentType == 'M':
    monthPayAMT = (totalAMT + monthProcessingFee) / 8 
  else:
    monthPayAMT = totalAMT           

  curDate = datetime.now()
  invDate = curDate.strftime('%Y-%m-%d')
  
  if curDate.month == 12:
        next_month = 1
        next_year = curDate.year + 1
  else:
        next_month = curDate.month + 1
        next_year = curDate.year
    
  monthPayDate = datetime(next_year, next_month, 1)     
  
# Display values
  cityProvPCDSP = custCity + ", " + custProv + " " + custPC
  numCarsInsDSP = numCarsIns
  paymentTypeDSP = paymentType
  insPremDSP = f"${insPrem:,.2f}" 
  downValueDSP = f"${downValueAMT:,.2f}"
  extraLiabilityAmountDSP = f"${extraLiabilityAmount:,.2f}" 
  optGlassCovAmtDSP = f"${optGlassCovAmt:,.2f}" 
  optLoanerCarAmtDSP = f"${optLoanerCarAmt:,.2f}" 
  totalExtraCostDSP = f"${totalExtraCost:,.2f}" 
  subtotalDSP = f"${subtotal:,.2f}" 
  HSTAmtDSP = f"${HSTAmt:,.2f}" 
  totalAMTDSP = f"${totalAMT:,.2f}"
  monthPayDSP = f"${monthPay:,.2f}"
  monthProcessingFeeDSP = f"${monthProcessingFee:,.2f}"
  monthPayAMTDSP = f"${monthPayAMT:,.2f}" 
  monthPayDateDSP = monthPayDate.strftime('%Y-%m-%d')

# Generate report headings.
  print()
  print(f"-" * 100)
  print(f" " * 35 + "ONE STOP INSURANCE AGENCY" + " " * 35)
  print(f"-" * 100)
  print()
  print()
  print(f" " * 39 + "[ CUSTOMER INFO ]" + " " * 39)
  print()
  print(f"Policy #: {polNum:<73} Date: {invDate}")
  print()
  print()
  print(f"{fullName:<75} {custAdd:>24}")
  print(f"{custPhone:<75} {cityProvPCDSP:>24}")
  print()
  print()
  print(f" " * 34 + "[ POLICY COVERAGE DETAILS ]" + " " * 34)
  print()
  print(f"   # of" + " " * 20 + "Extra" + " " * 25 + "Glass" + " " * 25 + "Loaner Car")
  print(f"   Cars" + " " * 20 + "Liability" + " " * 21 + "Coverage" + " " * 22 + "Coverage") 
  print()
  print(f"-" * 100)
  print()
  print(f"     {numCarsInsDSP}" + " " * 25 + f"{extraLiability}" + " " * 29 + f"{optGlassCov}" + " " * 29 + f"{optLoanerCar}")
  print()
  print(f"-" * 100)
  print()
  print()
  print(f" " * 38 + "[ PAYMENT DETAILS ]" + " " * 34)
  print()
  print(f" Premiums for {numCarsInsDSP} cars:" + " " * 69 + f"{insPremDSP:>9s}")
  print(f" Extra coverages: " + " " * 72 + f"{totalExtraCostDSP:>9s}")
  print()
  print(f"-" * 25 + " " * 64 + "-" * 11)
  print()
  print(f" Subtotal: " + " " * 79 +  f"{subtotalDSP:>9s}")
  print(f" HST: " + " " * 84 +  f"{HSTAmtDSP:>9s}")  
  print()
  print(f"-" * 25 + " " * 64 + "-" * 11)
  print()
  print(f" Total insurance amount:" + " " * 66 +  f"{totalAMTDSP:>9s}")  
  print()
  print(f" Payment option:" + " " * 82 +  f"{paymentTypeDSP}")
  print(f" Down payment:" + " " * 75 +  f"-{downValueDSP:>8s}")
  print()
  print(f"-" * 25 + " " * 64 + "-" * 11)
  print()
  print(f" Total owing:" + " " * 77 +  f"{totalAMTDSP:>9s}")
  print(f" Processing fee (if monthly):" + " " * 61 +  f"{monthProcessingFeeDSP:>9s}")
  print()
  print()
  print(f" " * 27 + f"First payment of {monthPayAMTDSP} due on {monthPayDateDSP}")
  print()
  print(f"-" * 100)
  print()
  print()
  print(f" " * 39 + "[ PREVIOUS CLAIMS ]" + " " * 34)  
  print()
  print()
  print(f" Claim #" + " " * 35 + "Claim Date" + " " * 39 + "Amount")
  print()
  print(f"-" * 100)
  print()
  for item in claims:
    print(f" {item[0]}" + " " * 37 + f"{item[1]}" + " " * 37 + f"{item[2]}")
  print()
  print(f"-" * 100)
  print()
  print(f" " * 27 + f"Thank you for choosing One Stop Insurance!")
  print()
  
# Initialize counters and accumulators.

# Open the data file.
  d = open("data.dat","a+")
  # writing data to file
  d.write("{}, ".format(polNum))
  d.write("{}, ".format(invDate))
  d.write("{}\n".format(total))
# Close the file.
  d.close()

# Update counters and accumulators.

  # (#) is the number of seconds for the loading time
  loading_bar(5)
# Print a new line after the loading is complete
  print('\nPolicy has been saved.')

  polNum = int(polNum)
  polNum += 1

# open, read, make list, close
  constf = open('const.dat', 'r')
  constants = constf.readlines()
  constf.close()

  polNum = str(polNum)
  constants[0] = polNum + "\n"

# writing data to file
# open, write, close
  constf = open('const.dat', 'w')
  constf.writelines(constants)
  constf.close()

  while True:
    continuePolicy = input("Would you like to process another policy (Y/N)? ").upper()
    if continuePolicy == 'N':
      exit()
    else: 
      break  

if __name__ == "__main__":
    main()
