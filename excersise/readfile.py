fo = open('前端面试题.docx', 'r', encoding='gbk', errors='ignore')

print(fo.name)

line = fo.read()
print("docx contnet %s" % line)
fo.close()
