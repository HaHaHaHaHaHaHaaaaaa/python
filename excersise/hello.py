import uuid



def testfun(a, b):
    return a * b + a + b


a = testfun(2, 3)

# print(a,uuid.uuid4())


tuple1=(1,2,3,4,5)

# print(type (tuple1))


list1= ['Google', 'Taobao', 'Runoob', 'Baidu',"Baidu"]

tuple2=tuple(list1)

# print(tuple2)


param={'a','b','c','d'}

# print(param)


set_a=set('abcd')
print(set_a)