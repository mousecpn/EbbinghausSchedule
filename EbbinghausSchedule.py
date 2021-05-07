# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:36:29 2019

@author: ASUS
"""
import pandas as pd
import openpyxl
def EbbinghausSchedule(init_date,num_list,first_num):
    # half day is a period
    periods = num_list*2+13
    schedule_list = []
    daytime = []
    for i in range(periods):
        day_sche = []
        schedule_list.append(day_sche)
        if i%2 == 0:
            daytime.append('AM')
        else:
            daytime.append('PM')
    for i in range(num_list):
        index = i+first_num
        # first day morning
        schedule_list[2*i].append(str(index))
        # first dat afternoon
        schedule_list[2*i+1].append(str(index))
        # one more day later
        schedule_list[2*i+3].append(str(index))
        # two more days later
        schedule_list[2*i+7].append(str(index))
        # four more days later
        schedule_list[2*i+14].append(str(index))
    
    init_time = init_date+' 09:00:00'
    time = pd.date_range(init_time, periods=periods,freq='12H')
    time = pd.DataFrame(time,columns=['Date'])
    daytime = pd.DataFrame(daytime,columns=['Daytime'])
    
    schedule = []
    for i in range(periods):
        schedule.append(','.join(schedule_list[i]))
    task = pd.DataFrame(schedule,columns=['Task'])
    task = pd.concat([time,task],axis=1)
    task = pd.concat([task,daytime],axis=1)
    return task

if __name__ == "__main__":
    sche = EbbinghausSchedule('2019-04-07',50,1)
    filePath = r'out.xlsx'
#    writer = pd.ExcelWriter('out.xlsx')
    sche.to_excel(filePath, encoding='utf-8', index=False, header=False)


        
        