print("\t\tWelcome to Global Green Energy\n\n")
fixed_fee = 120.62
transact_fee = 1.32
account_number = int(input("Enter your account number: "))
month = int(input("Enter your month 1 to 12: "))
input_choice = str(input("Choose your electricity scheme\n1. EFIR\n2. EFLR\n").upper())
elect_consumption = int(input("Please enter your monthly consumption: "))
elec_bill = 0
gas_consumption = 0
gas_bill = 0
total_bill_exl_tax = 0
total_bill_incl_tax = 0
tax = 0
match input_choice:
   case "EFIR":
        if elect_consumption <= 1000:
            elec_bill = elect_consumption*0.01*8.36
        else:
            elec_bill = 1000*0.01 * 8.36+((elect_consumption-1000)*0.01*9.41)
   case "EFLR":
        elec_bill  = elect_consumption*9.11*0.01
   case _:
       print("Electricity scheme not valid")




input_choice1 = str(input("\nChoose your gas scheme\n1. GFIR\n2. GFLR\n").upper())
gas_consumption = int(input("Please enter your monthly consumption: "))
match input_choice1:
    case "GFIR":

        if gas_consumption <= 950:
            gas_bill = gas_consumption*0.01*4.56
        else:
            gas_bill = 950*4.56*0.01+((gas_consumption-950)*0.01*5.89)

    case "GFLR":
        gas_bill = gas_consumption * 3.93 * 0.01
    case _:
       print("Gas scheme not valid")

total_bill_exl_tax = elec_bill + gas_bill + fixed_fee + transact_fee
print("\nChoose your province\n1. AB, BC, MB, NT, NU, QC, SK, YT\n2. NB, NF, NL, NS, PE\n3. Ontario")

input_choice2 = int(input("\nEnter the number associated with your province (1, 2 or 3): "))

match input_choice2:
    case 1:
        tax = (5 / 100) * total_bill_exl_tax
    case 2:
        tax = (13 / 100) * total_bill_exl_tax
    case 3:
        tax = (15 / 100) * total_bill_exl_tax
    case _:
        print("Enter a valid option")

total_bill_incl_tax = tax+total_bill_exl_tax

print("\t\t\tBILL\n\nElectricity\t\t\t:\t\t${0}\n\nGas\t\t\t\t\t:\t\t${1}\n\nGGE Montly fee\t\t:\t\t${2}\n\nGas fixed fee\t\t:"
      "\t\t${3}\n\nTax\t\t\t\t\t:\t\t${4}\n\nTotal\t\t\t\t:\t\t${5}".format(round(elec_bill, 2),round(gas_bill,2),
      fixed_fee, transact_fee, round(tax,2), round(total_bill_incl_tax, 2)))


