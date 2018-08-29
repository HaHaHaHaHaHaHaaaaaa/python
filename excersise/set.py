

param = { 'apple', 'juice'}
for k in param:
    print(k)

param.remove('juice')

print(param)
a='juice' in param
b='apple' in param
if a:
    print("juice in param")
elif b:
    print("apple in param")

