import uuid



def testfun(a, b):
    return a * b + a + b


a = testfun(2, 3)

print(a,uuid.uuid4())
