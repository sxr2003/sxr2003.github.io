import serial
import time
import os
import json
def pa():
    ser = serial.Serial('/dev/ttyAMA0',9600)
    i=0
    while i<7 :
        ser.write(b'SC0%d'%i)
        i+=1
    i=0    
    while i<7 :
        ser.write(b'SO0%d'%i)
        os.system("cd /var/www/html/text/photo&&libcamera-jpeg -o %d.jpg -n"%i)
        ser.write(b'SC0%d'%i)
        i+=1
        time.sleep(1)
        print(i)
    
    
    f=open ("/var/www/html/outcome.txt","w+")
    f.write("")
    f.close()
    
    
    f=open ("/var/www/html/state.txt","w+")
    f.write("ok")
    f.close()


    os.system("sudo chmod 777 kaishi.txt")
    f=open ("/var/www/html/kaishi.txt","w+")
    f.write("")
    f.close
    
    os.system("cd /var/www/html/text&&python /var/www/html/text/pre_mul.py")
    

    with open("/var/www/html/state.txt","w+") as fo:
        fo.write('')
  
    
def denglu ():
    
    file = open("/var/www/html/huiyuan.json", 'r', encoding='utf-8')
    papers = []
    for line in file.readlines():
        dic = json.loads(line)
        papers.append(dic)

    file.close()
    f=open("/var/www/html/user.json","r")

    data=json.load(f)

    i=len(papers)-1
    while i >= 0 :
        if data["user"]==papers[i]["user"]:
            if data["pass"]==papers[i]["pass"]:
                with open('/var/www/html/mode.txt','w+') as fo:
                    fo.write("1")
                return 1
                break
            else :
                with open('/var/www/html/mode.txt','w+') as fo:
                    fo.write("2")
                    return 0
        i-=1
               
    if i<0:
        f.seek(0,0)
        a=f.read()
        with open('/var/www/html/mode.txt','w+') as fo:
            fo.write('3')
        
        with open('/var/www/html/huiyuan.json','a') as fo:
            fo.write("\n"+a)
        return 1
        

        
        
    
    
    
    
    
    
def main ():
    
    os.system("sudo chmod 777 kaishi.txt")
    f=open ("/var/www/html/kaishi.txt","w+")
    f.write("")
    f.close
    os.system("sudo chmod 777 state.txt")
    f=open ("/var/www/html/state.txt","w+")
    f.write("")
    f.close
    os.system("sudo chmod 777 /var/www/html/mode.txt")
    with open('/var/www/html/mode.txt','a') as fo:
            fo.write("")
    
    l=0
    while 1 :
        with open('/var/www/html/user.json','r') as fo:
            mode=fo.read()
        if mode !="":
            l=denglu()
            os.system("sudo chmod 777 /var/www/html/outcome.txt")
            with open('user.txt','w+') as fo:
                fo.write("")
            time.sleep(2)
            with open('/var/www/html/mode.txt','w+') as fo:
                fo.write("")
        os.system("sudo chmod 777 /var/www/html/kaishi.txt")
        f=open ("/var/www/html/state.txt","w+")
        f.write("")
        f.close()
        f=open ("/var/www/html/kaishi.txt","r+")
        
        TF=f.read()
        
        if TF!=""and l==1:
            f.close()
            pa()
            l=0

            

main()    