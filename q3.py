s="Upes is a good uni . Upes has a great view"
s=s.replace("Upes","It")
s=list(s)
s[0:2]="Upes"
ap="".join(s)
print(ap)