y=input("Has your startup started generating revenue: ").lower()
cm=float(input("Enter the cost required to make the product: "))
cs=float(input("Enter the cost at which the product is sold: "))
pr=cs-cm
pm=(pr/cs)*100
if y=="yes" or y=="y":
    print("For your evaluation determination answer the following situational question?")
    x=input("If you get an investor who wants to invest in you, you will ask for how much revenue and how much ownership(in %) will you provide him respectively: ").split()
    ev=int(x[0])/(int(x[1])/100)
    if pm<50:
        print("Hence, your startup is valued at a",ev,"$ evaluation")
    elif pm<75:
        print("Hence your startup is valued at a",ev+(0.2*ev),"$ evaluation")
    else:
        print("Hence your startup is valued at a",ev+(0.4*ev),"$ evaluation")
elif y=="no" or y=="n":
    a=input("Is your business a Perfect Competition(P.C.) Or Monopoly? ").lower()
    if a=="perfect competition" or a=="p.c." or a=="pc":
        s=input("Enter your expected sales in a month: ")
        y=int(s)*12
        print("Hence your sales/valuation for this year is",y-(0.25*y),"$")
    elif a=="monopoly" or a=="m":
        s=input("Enter your expected sales in a month: ")
        y=int(s)*12
        print("Hence your sales/valuation for this year is",y+(0.15*y),"$")
    else:
        print("Error!\nInvalid Input")