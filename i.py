f1=open("first.txt","r")
if f1:
    print("File is read successfully")
    f1=open("second.txt","w")as f:
        content=f1.read()
        print(content)
        for word in content.split():
           if word[0] in 'a','e','i','o','u':
              f.write(word)
   