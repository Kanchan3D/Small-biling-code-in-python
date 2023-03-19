print(" best price billing")
tp=0
n=int(input("specify total number of item"))
for i in range(0,n):
    print("\t\t enter price for item", i)
    p=int(input("enter price"))
    tp=tp+p
print("\t\t\t total bill amount is ",tp)