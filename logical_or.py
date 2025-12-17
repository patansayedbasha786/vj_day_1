ex=False
sp=False
print("exam:",ex)
print("sports:",sp)
dohni={"ex":True,"sp":True}
ex=dohni["ex"]
sp=dohni["sp"]
print(ex)
print(sp)
res=ex or sp
print(res)

#2
ex=False
sp=False
print("exam:",ex)
print("sports:",sp)
siraj={"ex":False,"sp":True}
ex=siraj["ex"]
sp=siraj["sp"]
print(ex)
print(sp)
res=ex or sp
print(res)

#3
ex=False
sp=False
print("exam:",ex)
print("sports:",sp)
s_pr={"ex":True,"sp":False}
ex=s_pr["ex"]
sp=s_pr["sp"]
print(ex)
print(sp)
res=ex or sp
print(res)

#4
ex=False
sp=False
print("exam:",ex)
print("sports:",sp)
s1={"ex":False,"sp":False}
ex=s1["ex"]
sp=s1["sp"]
print(ex)
print(sp)
res=ex or sp
print(res)

