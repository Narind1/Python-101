b=int(input("Enter your bill amount:"))
p=int(input("Enter the number of people you want to split the bill:"))
tip=b*8/100
gst=b*18/100
total=b+tip+gst
split=(total)/p
print("The payable amount perhead is:",split)