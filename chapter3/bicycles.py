bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0])
a=3
print(bicycles)
message=f"My first bicycle was a {bicycles[a].title()}."
print(message)
bicycles[3]="yamaha"
print(message)
print(bicycles)
bicycles.append("honda")
a=-1
message=f"My first bicycle was a {bicycles[a].title()}."
print(bicycles)
print(message)
bicycles.insert(2,"suziki")
a=2
message=f"My first bicycle was a {bicycles[a].title()}."
del bicycles[4]
print(bicycles)
print(message)
pop=bicycles.pop()
print(pop)
print(bicycles)

too_expensive="trek"
bicycles.remove(too_expensive)
print(bicycles)