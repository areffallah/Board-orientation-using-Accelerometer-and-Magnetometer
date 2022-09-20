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
        f = open('mag-readings_raw04.txt','a') 
        f.write(msg)
        f.close
        data = strParse(msg)
        print("Data: " + str(data))
        if(data != None):
            #print("data incoming")
            x = np.append(x,data[0])
            y = np.append(y,data[1])
            z = np.append(z,data[2])
        else: 
          print("no data incoming, check connection")

        # Define calibration parameters
        A = np.array(   [[1.194856, 0.042336, -0.004724],
                [0.0423360, 1.207232, 0.014726],
                [-0.004724, 0.014726, 1.244256]])
        b = np.array([4.245550, 14.722385, 8.095951])
        calibData = np.zeros((1, 3), dtype='float')
        currMeas = [data[0], data[1], data[2]]
        calibData = A @ (currMeas - b)
        print("CalibData: " + str(calibData))
        


    print("Data successfully acquired, size: "+str(len(x)))
    np.savetxt("Magdata_x4.csv",x, delimiter=",")
    np.savetxt("Magdata_y4.csv",y, delimiter=",")
    np.savetxt("Magdata_z4.csv",z, delimiter=",")