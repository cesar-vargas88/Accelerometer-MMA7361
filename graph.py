import serial                         
import numpy
import matplotlib.pyplot as plt
from drawnow import *
 
g_X = []
g_Y = []
g_Z = []

arduinoData = serial.Serial('/dev/ttyACM0', 115200)     #Creating our serial object named arduinoData
plt.ion()                                               #Tell matplotlib you want interactive mode to plot live data

cnt = 0
 
def makeFig(): #Create a function that makes our desired plot
    plt.ylim(-40,40)                                #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Acceleration m/s^2')                #Set ylabels
    plt.plot(g_X)                                   #plot the temperature
    plt.plot(g_Y) 
    plt.plot(g_Z) 

while True:          

    while (arduinoData.inWaiting()==0):                 
        pass                                            

    arduinoString = arduinoData.readline()              #read the line of text from the serial port
    dataArray = arduinoString.split(',')                #Split it into an array called dataArray

    x = ( ( ( float(dataArray[0]) * 3.22265625 ) - 1650 ) * 0.00125 * 9.8 )
    y = ( ( ( float(dataArray[1]) * 3.22265625 ) - 1650 ) * 0.00125 * 9.8 ) 
    z = ( ( ( float(dataArray[2]) * 3.22265625 ) - 1650 ) * 0.00125 * 9.8 )

    g_X.append(x)  
    g_Y.append(y)   
    g_Z.append(z)  

    drawnow(makeFig) 

    #plt.pause(.000001)                                  #Pause Briefly. Important to keep drawnow from crashing

    cnt = cnt + 1

    if(cnt > 60):                                         #If you have 50 or more points, delete the first one from the array
        g_X.pop(0)                                      #This allows us to just see the last 50 data points
        g_Y.pop(0)
        g_Z.pop(0)

