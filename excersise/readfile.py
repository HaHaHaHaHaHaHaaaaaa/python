# fo = open('前端面试题.docx', 'r', encoding='gbk', errors='ignore')
#
# print(fo.name)
#
# line = fo.read()
# print("docx contnet %s" % line)
#
# fo.close()




# with open('123.txt','r') as fo:
#
#     # for line in fo.readlines():
#     #     print(line)
#     con=fo.read(100)
#     while len(con):
#         print(con)
#         con=fo.read(100)


# with open('123.txt','r') as file:
#     print(file.readline())
#     # print(file.seek(0))
#     print(file.readline())


fp=open("test.txt",'w')


with open('123.txt','r') as file:
    for line in file.readlines():
        fp.write(line)
