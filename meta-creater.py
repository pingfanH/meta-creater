import os
import os.path
import random
meta_path = os.getcwd()

def randmata():
    rand=(random.random())
    rand2=(random.random())
    rand = ('ec79f249-c319a-4d43-8395-'+str(100 * rand - rand2))
    randmata=str({
        "uuid": rand,
        "assetType": "SCW"
    })
    randmata= randmata.replace("'",'"')
    print (randmata)
def randjsonmata():
    rand=(random.random())
    rand2=(random.random())
    rand = ('ec79f249-c319a-4d43-8395-'+str(100 * rand - rand2))
    randmata=str({"uuid":rand,"shortID":9716923057,"assetType":"AssetASMData"})
    randmata= randmata.replace("'",'"')
    print (randmata)

meta_path=(os.getcwd())
print (meta_path)
path=(meta_path)
files = os.listdir(path)
res=''
for file in files:
    file_path = os.path.join(path, file)
    os.path.isfile(file_path)
    print("creat:"+(file))
    if (".glb") in file:
        name=str(file)
        rand=(random.random())
        rand2=(random.random())
        rand = ('ec79f249-c319a-4d43-8395-'+str(100 * rand - rand2))
        rand= rand.replace("'",'')
        rand= rand.replace(".",'')
        randmata=str({
            "uuid": rand,
            "assetType": "SCW"
        })
        randmata= randmata.replace("'",'"')
        print (randmata)
        text=randmata
        print(text)
        
        # print(meta_path)
        file_path = os.path.join(meta_path, name+'.meta')
        file_test = open(file_path, 'w', encoding='utf-8')
        file_test.write(text)
    if (".json") in file:
            name=str(file)
            rand=(random.random())
            rand2=(random.random())
            short=(random.random())
            short=str(short)
            short= short.replace("'",'')
            short= short.replace(".",'')
            rand = ('ec79f249-c319a-4d43-8395-'+str(100 * rand - rand2))
            rand= rand.replace("'",'')
            rand= rand.replace(".",'')
            randjsonmata=str({"uuid":rand,"shortID":short,"assetType":"AssetASMData"})
            randjsonmata= randjsonmata.replace("'",'"')
            text=randjsonmata
            print(text)
            
            # print(meta_path)
            file_path = os.path.join(meta_path, name+'.meta')
            file_test = open(file_path, 'w', encoding='utf-8')
            file_test.write(text)



