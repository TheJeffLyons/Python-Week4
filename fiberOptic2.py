print('Welcome to Lyons Fiber Optic')

companyName = input('What is your company name?')

fiberFeet = input('Fiber optic feet to be installed?')

totalCost = ""

if int(fiberFeet) < 100:
    totalCost = int(fiberFeet) * .87
elif int(fiberFeet) < 250:
    totalCost = int(fiberFeet) * .80
elif int(fiberFeet) < 500:
    totalCost = int(fiberFeet) * .70
elif int(fiberFeet) >= 500:
    totalCost = int(fiberFeet) * .50

print(f"{companyName.title()} owes ${totalCost}")