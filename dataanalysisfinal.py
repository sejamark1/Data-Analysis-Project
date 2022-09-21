import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl
import pickle

#Setting up some screen parameters to make things easier to read
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



# Data_Allocation.xlsx

#filename: str = r'FULL PATH OF YOUR DATA FILE'
filename: str = r'LFB_data_section5.xls'

data = pd.read_excel(filename)
# print(data.head(4))

#Assigned Borogouhs
bourough1 = "Havering".lower()
bourough2 = "Barking and Dagenham".lower()
bourough3 = "Greenwich".lower()
bourough4 = "Bexley".lower()



#c)	Considering the data for Property Category: Non-Residential incidents in your boroughs and year
    #(i)	What was the average response time for the first engine?
    #(ii)	What was the standard deviation?


propertyCategory = data["PropertyCategory"]
calData = data["CalYear"]
hourOfCall = data["HourOfCall"]
borogugh = data["IncGeo_BoroughName"]

incidentGroup  = data["IncidentGroup"]
stopCodeDescription = data["StopCodeDescription"]
responseTime = data["FirstPumpArriving_AttendanceTime"]
ps = 0

ps1 = 0

def q1():
    incident = 0
    fire = 0
    pfire = 0
    sfire = 0
    falseAlarm = 0
    afa = 0
    gindent = 0
    mindent  = 0
    specialService = 0
    for i in range(len(propertyCategory)):
        if(propertyCategory[i] == "Non Residential" and str(calData[i]) == "2019" and (borogugh[i].lower() == bourough1 or borogugh[i].lower() == bourough2
                                                                                       or borogugh[i].lower() == bourough3 or borogugh[i].lower() == bourough4 )):
            incident += 1
            if(incidentGroup[i] == "Fire"):
                fire += 1
                if(stopCodeDescription[i] == "Primary Fire"):
                    pfire +=1
                elif(stopCodeDescription[i] == "Secondary Fire"):
                    sfire +=1
            elif (incidentGroup[i] == "False Alarm"):
                falseAlarm += 1
                if(stopCodeDescription[i] == "AFA"):
                    afa+=1
                elif(stopCodeDescription[i] == "False alarm - Good intent"):
                    gindent +=1
                elif(stopCodeDescription[i] == "False alarm - Malicious"):
                    mindent +=1
            elif (incidentGroup[i] == "Special Service"):
                specialService += 1

    return ("Total Incident:" + str(incident) + "\n"+
          "Fire: " + str(fire) +" : "+ str((fire/incident) * 100) + "\n"+
          "\tPrimary Fire: " + str(pfire) + " : " + str((pfire/fire) * 100) + "\n" +
          "\tSecondary Fire: " + str(sfire) + " : " + str((sfire/fire) * 100) + "\n" +
          "False Alarm: " + str(falseAlarm) +" : "+ str((falseAlarm/incident) * 100) +"\n"+
          "\tAFA: " + str(afa) + " : " + str((afa / falseAlarm) * 100) + "\n" +
          "\tFalse Alarm Good Indent: " + str(gindent) + " : " + str((gindent / falseAlarm) * 100) + "\n" +
          "\tFalse Alarm Malicoius: " + str(mindent) + " : " + str((mindent / falseAlarm) * 100) + "\n" +
          "Special Service: " + str(specialService) +" : "+ str((specialService/incident) * 100)
          )










def qb():
    hourofCallAr = [0] * 24
    totalHours = 0
    for i in range(len(propertyCategory)):
        if(propertyCategory[i] == "Non Residential" and str(calData[i]) == "2019" and (borogugh[i].lower() == bourough1 or borogugh[i].lower() == bourough2
                                                                                       or borogugh[i].lower() == bourough3 or borogugh[i].lower() == bourough4 )):
            hourofCallAr[hourOfCall[i]] += 1

    for  i in hourofCallAr:
        totalHours += i
    print(totalHours/24)
    return hourofCallAr


def qc1():
    responseCountiwthNull = 0
    responseCount = 0
    totalResponseTime = 0
    for i in range(len(propertyCategory)):
        if(propertyCategory[i] == "Non Residential" and str(calData[i]) == "2019" and (borogugh[i].lower() == bourough1 or borogugh[i].lower() == bourough2
                                                                                       or borogugh[i].lower() == bourough3 or borogugh[i].lower() == bourough4 )):
            responseCountiwthNull += 1
            if(str(responseTime[i]) == "nan"):
                responseCount += 1
            if(str(responseTime[i]) != "nan"):
                totalResponseTime+= float(responseTime[i])

    responseCount = responseCountiwthNull - responseCount # Gives responsecount without nan.
    avg = totalResponseTime/responseCount

    #C (ii)
    ravg = 0
    for i in range(len(propertyCategory)):
        if(propertyCategory[i] == "Non Residential" and str(calData[i]) == "2019" and (borogugh[i].lower() == bourough1 or borogugh[i].lower() == bourough2
                                                                                       or borogugh[i].lower() == bourough3 or borogugh[i].lower() == bourough4 )):
            if(str(responseTime[i]).strip() != "nan"):
                ravg += ((responseTime[i]) -avg) ** 2


    ravg = ravg/responseCount
    ravg = math.sqrt(ravg)
    print("Standrad Deviation: " + str(ravg))

    return ("Average with NULL included: {} \nAverage without NULL: {}\n".format((totalResponseTime/responseCountiwthNull), (totalResponseTime/responseCount)))





# print(qc1())


