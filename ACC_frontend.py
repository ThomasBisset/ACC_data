from ACC_logging import *
from ACC_functions import *
from pathlib import Path
import datetime
import time
import pandas as pd


currentDateTime = datetime.datetime.now()
timestamp = currentDateTime.strftime("%Y_%m_%d_%H_%M_%S")
filename = timestamp + ".csv"
output = Path.cwd() / "logs" / filename                                                     # edit to suit, path / folder MUST exist!
data = []


print("Started")


try:
    while True:                                                                             # starts an infinite loop
        if read_graphics()["ACC_STATUS"] == 2:                                              # skips the checks if the script is started before any actual track time
            if read_graphics()["iSplit"] < 300:                                             # combined with the sleep() command later

                # Collect the data for the sector
                stageData = {

                    # Track, session info etc
                    "Track": read_static()["track"],
                    "Session": read_graphics()["ACC_SESSION_TYPE"],

                    # Conditions
                    "Time_Of_Day": read_graphics()["Clock"],                               # Time is in seconds from midnight
                    "Rain": read_graphics()["rainIntensity"],
                    "Air_Temperature": read_physics()["airTemp"],
                    "Track_Temperature": read_physics()["roadTemp"],
                    "Grip_Level": read_graphics()["trackGripStatus"],

                    # Car Info
                    "Car": read_static()["carModel"],
                    "Fuel": read_physics()["fuel"],
                    "Front_Brake_Compound": read_physics()["frontBrakeCompound"],
                    "Rear_Brake_Compound": read_physics()["rearBrakeCompound"],
                    "Brake_Bias": read_physics()["brakeBias"],
                    "TC": read_graphics()["TC"],
                    "TC_Cut": read_graphics()["TCCut"],
                    "ABS": read_graphics()["ABS"],
                    "Engine_Map": read_graphics()["EngineMap"],

                    # Tyre Info
                    "Tyres": read_graphics()["currentTyreSet"],
                    "Tyre_Temperature_Front_Left": read_physics()["tyreTemp"][0],
                    "Tyre_Temperature_Front_Right": read_physics()["tyreTemp"][1],
                    "Tyre_Temperature_Rear_Left": read_physics()["tyreTemp"][2],
                    "Tyre_Temperature_Rear_Right": read_physics()["tyreTemp"][3],
                    "Tyre_Pressure_Front_Left": read_physics()["wheelPressure"][0],
                    "Tyre_Pressure_Front_Right": read_physics()["wheelPressure"][1],
                    "Tyre_Pressure_Rear_Left": read_physics()["wheelPressure"][2],
                    "Tyre_Pressure_Rear_Right": read_physics()["wheelPressure"][3],

                    # Timing Data
                    "Lap": read_graphics()["completedLaps"],
                    "Last_Lap_Time": read_graphics()["iLastTime"],                          # time in milleseconds
                    "Sector": read_graphics()["currentSectorIndex"],
                    "Last_Sector_Time": read_graphics()["lastSectorTime"]                   # time in milleseconds

                }


                print("Appending Data |", millisecondsToTime(read_graphics()["iLastTime"]))
                data.append(stageData)


                # Wait (prevents info spamming)
                time.sleep(0.5)


except KeyboardInterrupt:
    print("Exiting")
    df = pd.DataFrame(data)
    print(df)
    df.to_csv(output)