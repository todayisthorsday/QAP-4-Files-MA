# Description: A program for One Stop Insurance Company to enter and calculate 
# new insurance information for it's customers
# Author: Melanie Adams
# Date(s): July 24 2024


# Define required libraries.
from datetime import datetime
import time

# Define program constants.
constf = open('const.dat', 'r')
constants = constf.readlines()
polNum = constants[0]
polNum = int(polNum)
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
# REMEMBER for next time: global variables are usually all caps

# Main report processing starts here.
while True:
  #def main():
  #function variables
  provinces = ['NL', 'NS', 'NB', 'PE', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']

  #user inputs
  fname = input('Please enter customer first name: ').title()
  lname = input('Please enter customer last name: ').title()
  custadd = input("Please enter the customer's street address: ").title()
  custcity = input("Please enter the customer's city: ").title()

  while True:
    custprov = input("Please enter the customer's province (##): ").upper()
    if custprov not in provinces:
      print("Province not valid. Please re-enter as 2 letter province code.")
    else:
       break
    
  custPC = input("Please enter customer's postal code (X#X #X#):" ).upper()
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
    downValue = float(downValue)
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
  totalCost = insPrem + totalExtraCost
  HSTAmt = HSTrate * totalCost
  total = totalCost + HSTAmt

  if paymentType == 'D':
    monthPay = (total + monthProcessingFee - downValue) / 8
  else:
    monthPay = (total + monthProcessingFee) / 8
  if paymentType == 'M':
    payment = monthPay
  else:
    payment = total           

  curDate = datetime.now()
  invDate = curDate.strftime('%Y-%m-%d')
  
  if curDate.month == 12:
        next_month = 1
        next_year = curDate.year + 1
  else:
        next_month = curDate.month + 1
        next_year = curDate.year
    
  monthPayDate = datetime(next_year, next_month, 1)     
  monthPayDateDSP = monthPayDate.strftime('%Y-%m-%d')

# Generate report headings.
  print(insPrem)
  print(extraLiabilityAmount)
  print(optGlassCovAmt)
  print(optLoanerCarAmt)
  print(totalCost)
  print(HSTAmt)
  print(total)
  print(invDate)
  print(monthPayDate)


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
  #loading bar for "saving data"
  def loading_bar(duration, length=50):
    for i in range(length + 1):
        # Calculate the percentage of completion
        percent = (i / length) * 100
        # Create the bar string
        bar = '#' * i + '-' * (length - i)
        # Print the loading bar
        print(f'\r[{bar}] {percent:.2f}%', end='')
        # Sleep for a fraction of the duration
        time.sleep(duration / length)
    print('\nPolicy has been saved.')
  # number is the seconds of "loading time"
  loading_bar(5)

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
