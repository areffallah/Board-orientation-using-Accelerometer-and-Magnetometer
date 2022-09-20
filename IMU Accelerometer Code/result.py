import time
import numpy as np 
import serial
from matplotlib import pyplot as plt

#Creating a serial connection, using correct port and baud rate 
macIotBoard = serial.Serial('COM3', 9600)

record_t = 5 #Number of seconds to record for
start_t = time.time()
 
x = np.array([])
y = np.array([])
z = np.array([])

# Turn string array into float array
def strArrayToIntArr(strArr):
    for i in range(0, len(strArr)): 
        strArr[i] = float(strArr[i])
    return strArr

# Turn raw message from IOT board into float array
def strParse(message):
    mylist = message.split(',')
    data = strArrayToIntArr(mylist)
    return data

# Main loop that gathers data for pre defined amount of time 
if __name__ == "__main__":
    while (time.time()-start_t)<record_t:
        msg = macIotBoard.readline().decode()
        data = strParse(msg)
        print("Data: " + str(data))
        if(data != None):
            print("data incoming")
            x = np.append(x,data[0])
            y = np.append(y,data[1])
            z = np.append(z,data[2])
        else: 
          print("no data incoming, check connection")
            
    print("Data successfully acquired, size: "+str(len(x)))
    np.savetxt("data_x1.csv",x, delimiter=",")
    np.savetxt("data_y1.csv",y, delimiter=",")
    np.savetxt("data_z1.csv",z, delimiter=",")
