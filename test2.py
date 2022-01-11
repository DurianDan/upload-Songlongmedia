import json 
from glob import glob
listfile = glob("/home/duriandan/learning/personal project/upload Songlongmedia/json_description/*")
for i in range(len(listfile)) :
    file = listfile[i]
    with open(file,"r") as jsonfile:
        data = json.load(jsonfile)
        for i in data:
            print(data[i])
            print("__________________________________")
        print("""
        
        
        
        """)
        nextfile = str(input("next?(y/n):"))
        nextfile2 = str(input("for real?(y/n):"))
        print("________________")
        if nextfile=="y" and nextfile2=="y":
            continue
        else:
            break
