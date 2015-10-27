#To replace all the underscores with spaces 
f1 = open('/Users/harishannavajjala/Desktop/pos.txt','r+') 
f2 = open('/Users/harishannavajjala/Desktop/neg.txt','r+')
old1 = f1.read() # read everything in the file    
old1 = old1.replace("_", " ")
old2 = f2.read() # read everything in the file    
old2 = old2.replace("_", " ")

f1.seek(0) 
f1.write(old1) 
f2.seek(0) 
f2.write(old2)

#This belongs to HARISH ANNAVAJJALA

