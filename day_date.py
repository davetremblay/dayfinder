#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:43:31 2018

@author: DaveTremblay
"""

def day_date(date,month,year):
    """
    Original concept by mathematician John H Conway.
    
    Inputs: date (int), month (1 to 12), and year (int).
    
    Output: day of the week (str).
    """
    assert date > 0 and month > 0, "Input error."
    
    weekdays = {
            0:"Sunday",
            1:"Monday",
            2:"Tuesday",
            3:"Wednesday",
            4:"Thursday",
            5:"Friday",
            6:"Saturday"
            }
    weekdaysrev = {
            "Sunday":0,
            "Monday":1,
            "Tuesday":2,
            "Wednesday":3,
            "Thursday":4,
            "Friday":5,
            "Saturday":6,
            }
    monthdays = {
            1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
            }
    monthdaysleap = {
            1:31,
            2:29,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
            }
#    doomsdays = {
#            1:3,
#            2:28,
#            3:14,
#            4:4,
#            5:9,
#            6:6,
#            7:11,
#            8:8,
#            9:5,
#            10:10,
#            11:7,
#            12:12
#            }
#    doomsleap = {
#            1:4,
#            2:29,
#            3:14,
#            4:4,
#            5:9,
#            6:6,
#            7:11,
#            8:8,
#            9:5,
#            10:10,
#            11:7,
#            12:12
#            }
    months = {
            1:"January",
            2:"February",
            3:"March",
            4:"April",
            5:"May",
            6:"June",
            7:"July",
            8:"August",
            9:"September",
            10:"October",
            11:"November",
            12:"December"
            }
    
    #anchor day
    
    if year == 0:
        
        print ("Year 0 does not exist.")
    
    else:
        
        yeartr = year
                
        if year > 0 :
            
            yeartr = yeartr % 400
                                            
            minc1 = 0
            maxc1 = 99
            
            minc2 = 100
            maxc2 = 199
            
            minc3 = 200
            maxc3 = 299
            
            minc4 = 300
            maxc4 = 399
            
            if yeartr >= minc1 and yeartr <= maxc1:
                anchor = weekdays[2]
                
            elif yeartr >= minc2 and yeartr <= maxc2:
                anchor = weekdays[0]
            
            elif yeartr >= minc3 and yeartr <= maxc3:
                anchor = weekdays[5]
                
            elif yeartr >= minc4 and yeartr <= maxc4:
                anchor = weekdays[3]
                
            else:
                anchor = "Error."
                
        else:
                            
            yeartr = yeartr % -400
                                
            minc1 = 0
            maxc1 = -99
            
            minc2 = -100
            maxc2 = -199
            
            minc3 = -200
            maxc3 = -299
            
            minc4 = -300
            maxc4 = -399
            
            if yeartr <= minc1 and yeartr >= maxc1:
                anchor = weekdays[3]
                
            elif yeartr <= minc2 and yeartr >= maxc2:
                anchor = weekdays[5]
            
            elif yeartr <= minc3 and yeartr >= maxc3:
                anchor = weekdays[0]
                
            elif yeartr <= minc4 and yeartr >= maxc4:
                anchor = weekdays[2]
                
            else:
                anchor = "Error."    
                
        #doomsday per year
        yearstr = str(year)
                
        last2 = int(yearstr[int(len(yearstr))-2:int(len(yearstr))])
        
        step1 = last2 // 12
        
        step2 = abs(last2 - (step1 * 12))
        
        step3 = step2 // 4
        
        step4 = weekdaysrev[anchor]
        
        step5 = step1 + step2 + step3 + step4
        
        doomsdayyear = step5 % 7
            
        #what day of the week
        
        if year % 4 == 0:
            if year % 100 != 0:
                #leap
                julian = date
                monthcalc = month - 1
                while monthcalc > 0:
                    julian += monthdaysleap[monthcalc]
                    monthcalc -= 1
                if date > monthdaysleap[month]:
                    print ("Date error.")
                juliandoom = 4
    
            else:
                if year % 400 == 0:
                    #leap
                    julian = date
                    monthcalc = month - 1
                    while monthcalc > 0:
                        julian += monthdaysleap[monthcalc]
                        monthcalc -= 1    
                    if date > monthdaysleap[month]:
                        print ("Date error.")
                    juliandoom = 4
                
                else:
                    #not leap
                    julian = date
                    monthcalc = month - 1
                    while monthcalc > 0:
                        julian += monthdays[monthcalc]
                        monthcalc -= 1  
                    if date > monthdays[month]:
                        print ("Date error.")   
                    juliandoom = 3
                        
        else:
            #not leap
            julian = date
            monthcalc = month - 1
            while monthcalc > 0:
                julian += monthdays[monthcalc]
                monthcalc -= 1     
            if date > monthdays[month]:
                print ("Date error.") 
            juliandoom = 3
        
        #day difference
        day1 = julian % 7
        day2 = day1 - juliandoom
        day3 = day2 + doomsdayyear
        
        if day3 < 0:
            finalday = day3 + 7
        else:
            finalday = day3
                            
        print (date, months[month], year, "is a", weekdays[finalday])
        return finalday

date = int(input("Date: "))
month = int(input("Month (1-12): "))
year = int(input("Year: "))
day_date(date,month,year)