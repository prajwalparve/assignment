import time
import json
import sys
import os
from pathlib import Path


def save_changes(data, filename='test.json'):
     #import json
     with open(filename,'w') as f:
        json.dump(data, f, indent=4)


def create(key="",value="",path="",timetolive=0):
    #import json
    m_path = path
    my_file = Path(path+"test.json")
    if not my_file:
        with open(path+'test.json', 'w+') as json_file:
            json_file.write('{}')
    else:
        with open('test.json', 'r') as json_file:
            dct = json.load(json_file)
        
    if key in dct:
        print("error: key exists")
    else:
        if(key.isalpha()):
            if sys.getsizeof(dct)<(1024*1020*1024+400) and sys.getsizeof(value)<=(16*1024*1024+400): #constraints for file size less than 1GB and Jasonobject value less than 16KB adding 400 beacause dict size is 400
                if timetolive==0:
                    l=[value,timetolive]
                else:
                    l=[value,time.time()+timetolive]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dct[key]=l
                    save_changes(dct,path+"test.json")
            else:
                print("error: Memory exceeded!! ")
        else:
            print("error: Invalid key_name!!")


def read(key,m_path=""):
    #import json
    with open(m_path+'test.json', 'r') as json_file:
        d = json.load(json_file)
    if key not in d:
        print("error: key does not exist in database.")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #checking time expiry
                stri=str(key)+":"+str(b[0]) #return JasonObject
                return stri
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri



def delete(key,m_path=""):
    #import json
    with open(m_path+'test.json', 'r') as json_file:
        d = json.load(json_file)
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                save_changes(d,m_path+"test.json")
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del d[key]
            save_changes(d,m_path+"test.json")
            print("key is successfully deleted")



