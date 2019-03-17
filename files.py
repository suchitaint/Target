import json
import os


dict={}
try:
    list=[]
    for roots, dirs, files in  os.walk(os.getcwd()):
        for file in files:
            dict1={}
            filename=os.path.join(roots,file)
            size=os.stat(filename).st_size
            dict1[filename]=size
            dict1=json.dumps(dict1)
            list.append(dict1)

    dict["files"]=list
except Exception as ex:
    dict["error"]="No such file or directory"
    print(ex)
json_data = json.dumps(dict, sort_keys=True, indent=4)
print(json_data)