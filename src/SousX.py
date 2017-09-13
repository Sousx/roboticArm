# SousX
# Arm Initialization and Food Item Movement Script
# 08/30/2017
 
# Initialization and connection of the Arm

import pyuarm
import time
timePause = 1
time.sleep(timePause)
print("pyuarm and time imported") 
arm = pyuarm.get_uarm()
print("pyuarm initialized") 
print("initial position set")  
#time.sleep(3)
#arm.set_position(50, 150, 150)
#time.sleep(5)

# Arm is set in position at storing module
# Pump is activated to retrieve food item
storage1 = [-124.5, 145, 155]
storage2 = [-134, 258, 156]

# Function for retrieving food from selected storage module
def getFood(storage, arm):
    arm.set_position(storage[0], storage[1], storage[2])
    time.sleep(timePause)
    while arm.get_tip_sensor() == False:
        storage[2] = storage[2] - 10
        arm.set_position(storage[0], storage[1], storage[2])
        time.sleep(0.1)
    print("food item retrieved")
 

getFood(storage2, arm)    
print('Current Position: ' + ', '.join(str(coordinate) for coordinate in arm.get_position())) # Get Current position
time.sleep(timePause)
arm.set_pump(True)
time.sleep(3)
print("pump turned on")
arm.set_position(storage2[0], storage1[1], 290, 100)
time.sleep(timePause) 

# Arm moves food item to cutting module
# Pump gripper is deactivated to release food item into module
# Pump is turned off
arm.set_position(207.5, 128.6, 250, 100)
time.sleep(timePause)
# if arm.get_tip_sensor():
    # print ("1")
#arm.set_position(207.5, 128.6, 130, 100)
#time.sleep(timePause)
print("cutting module position set") 
print('Current Position: ' + ', '.join(str(coordinate) for coordinate in arm.get_position())) # Get Current position
time.sleep(timePause)
arm.set_pump(False)
time.sleep(timePause)
print("pump turned off")

# Arm disconnects and program exits
print('Current Position: ' + ', '.join(str(coordinate) for coordinate in arm.get_position())) # Get Current positiony
time.sleep(timePause)
#arm.set_position(207.5, 128.6, 250, 100)
#time.sleep(timePause)
arm.disconnect()
time.sleep(timePause)
print("arm disconnected")
exit()
