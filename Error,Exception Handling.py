#Error handling
#syntax error
'''for i in range(10):
    print(i)'''

#run_time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''

#logical error
'''a=20
b=40
print(a-b)'''


'''a=3
b=9
if a<b:
    print("less")

a=3
b=9
if a>b:
    print("less")'''
    
#EXCEPTION HANDLING:
#TRY : Instructions from which we are expecting the exceptions.
#EXCEPT : Exception is raised in try block it will be handle by this block.
#ELSE : Optional(non-exceptions)
#FINALLY : Always it will display

'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends......")'''


#File Handling
#write()
'''a=open("pooja.txt","w")
a.write("python")
a.close()


a=open("pooja.txt","w")
a.write("java")
a.close()'''

#append()
'''a=open("pooja.txt","a")
a.write("\tdsa")
a.close()

a=open("pooja.txt","w")
a.write(input("data"))
a.close()

a=open("pooja.txt","w")
b=input("enter the data")
a.write(b)
a.close()'''


#Readlines()
'''a=open("pooja.txt")
#print(a.read())#it will  display entire content
#print(a.readline())#it will display firtline
#print(a.read(10))#it will display no.of characters
#print(a.readlines())#it will display with \n'''

#Writelines() : It makes every object side by side.
'''names=["sai","chandu","ishu","aishu","sangu"]
a=open("priya.txt","w")
a.writelines("\n".join(names))
a.close()'''


'''a=open("mymodule.py")
print(a.read())'''

'''a=open("C:\\Users\\Lenovo\\OneDrive\\Documents\\codegnan\\compiler\\tasks.py")
print(a.read())'''





























        
        
    
