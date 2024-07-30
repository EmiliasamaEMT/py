alien_0={
    'color':'green',
    'speed':'slow',
    'points':10
}
point_value=alien_0.get('points','NO')
print(point_value)
a1=["color","speed"]
for key1,value1 in alien_0.items():
    print(f"\nkey:{key1}")
    print(f"value:{value1}")
    print(f"the alien's {key1} is {value1}")
    if key1 in a1:
        print(f"good,{key1}:{value1}")
for name in alien_0:
    print(f"{name}")
print(alien_0.keys())
for name in sorted(alien_0.keys()):
    print(name)
    