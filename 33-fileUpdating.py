
with open("33-newfile3.txt","a",encoding="utf-8") as file: # in apend mode the cursor goes to the end  
    file.write("\nGazanfer Gonul")

with open("33-newfile3.txt","r+",encoding="utf-8") as file:
    content = file.read()
    content = "Efe Mert" + content
    file.seek(0)
    file.write(content)
    print(content)


with open("33-newfile3.txt","r+",encoding="utf-8") as file:   
    list=file.readlines()
    list.insert(1,"Michael Dvine") # we just add new name  into the list
    file.seek(0)                    # to add list into the file, we throw the cursor top of the file
    file.writelines(list)           # write the list into the file

