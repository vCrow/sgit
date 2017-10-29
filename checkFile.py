import time
import threading

def saveTime():
    file = open('/shares/nCrow/MyCloud/File.txt','a')
    #file = open('.\\File.txt','a')
    file.write('Time=')
    file.write(time.asctime(time.localtime(time.time())))
    file.write('\n')
    file.close()
    t = threading.Timer(3600,saveTime)
    t.start()

if __name__ == "__main__":  
    saveTime() 