import time
import numpy as np 
import serial
from matplotlib import pyplot as plt

#Creating a serial connection, using correct port and baud rate 
macIotBoard = serial.Serial('COM3', 9600)

record_t = 10 #Number of seconds to record for
start_t = time.time()

# Acceleration 
x = np.array([])
y = np.array([])
z = np.array([])

#Magnetic field
Bx = np.array([])
By = np.array([])
Bz = np.array([])

# Defining magnetic field soft-iron, hard-iron correction  matrix

K = np.array(   [[1.194856, 0.042336, -0.004724],
        [0.0423360, 1.207232, 0.014726],
        [-0.004724, 0.014726, 1.244256]])
V = np.array([4.245550, 14.722385, 8.095951])

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
        #print("Data:",msg)
        data = strParse(msg)
        #print("Data: " + str(data))
        if(data != None):
            #print("data incoming")
            x = np.append(x,data[0])
            y = np.append(y,data[1])
            z = np.append(z,data[2])
            Bx = np.append(x,data[3])
            By = np.append(y,-data[4])
            Bz = -np.append(z,-data[5])
            Br =  np.zeros((1, 3), dtype='float')
            Br = K @ ([data[3], data[4], data[5]] - V)
            # All angles are in Radian
            roll = -np.arctan2(data[1],data[2])
            pitch = -np.arctan2(-data[0],(data[1]*np.sin(roll)+data[2]*np.cos(roll)))
            yaw = np.arctan2((Br[2]*np.sin(roll)-Br[1]*np.cos(roll)),(Br[0]*np.cos(pitch)+Br[1]*np.sin(pitch)*np.sin(roll)+Br[2]*np.sin(pitch)*np.cos(roll)))
            print("Roll:",roll*180/np.pi,"Pitch:",pitch*180/np.pi,"Yaw:",yaw*180/np.pi)
        else: 
          print("no data incoming, check connection")
            
    #print("Data successfully acquired, size: "+str(len(x)))
    #np.savetxt("data_x.csv",x, delimiter=",")
    #np.savetxt("data_y.csv",y, delimiter=",")
    #np.savetxt("data_z.csv",z, delimiter=",")
    #np.savetxt("Ort_x.csv",Tetta_x, delimiter=",")
    #np.savetxt("Ort_y.csv",Tetta_y, delimiter=",")

