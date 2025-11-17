a=int(input("Enter the number of seconds :"))
sec=a%60
a=a-sec
min=a/60
hr=min//60
min=min%60
print("The given seconds amount to ",hr,"hours",min,"minutes",sec,"seconds")