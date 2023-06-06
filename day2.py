bill = int(input("total amt of bill:"))
tip = int(input("enter the tip amt: "))
final= bill*(tip/100)
bill = bill+final
print(bill)
ppl = int(input("no. of ppl: "))
total=bill/ppl
print(total)