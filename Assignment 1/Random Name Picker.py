import random
f=open("name_list.txt","r")
print(random.choice(f.readlines()))
f.close()