from django.shortcuts import render
from datetime import datetime
import pandas as pd
import numpy as np
from django.http import StreamingHttpResponse
import csv


class Day:
  def __init__(self,id,title,display,percentage):
    self.id = id
    self.title = title
    self.display = display
    self.percentage = percentage

def view1(request):
  reports = pd.read_csv('status/report.csv') # reeading the report file with pandas
  reports['timestamp']= pd.to_datetime(reports.timestamp) # parsing the timestamps to datetime
  
  # grouping of individual days from the timestamps could be improved in a better way.
  # still finding means to do that.

  day1 = reports[reports.timestamp.dt.day==1]
  day2 = reports[reports.timestamp.dt.day==2]
  day3 = reports[reports.timestamp.dt.day==3]
  day4 = reports[reports.timestamp.dt.day==4]
  day5 = reports[reports.timestamp.dt.day==5]
  day6 = reports[reports.timestamp.dt.day==6]
  day7 = reports[reports.timestamp.dt.day==7]
  day8 = reports[reports.timestamp.dt.day==8]
  day9 = reports[reports.timestamp.dt.day==9]
  day10 = reports[reports.timestamp.dt.day==10]
  day11 = reports[reports.timestamp.dt.day==11]
  day12 = reports[reports.timestamp.dt.day==12]
  day13 = reports[reports.timestamp.dt.day==13]


# function to calculate the most popular device base of id occurences.
  def most_popular(day): 
    return day.groupby('type')['id'].value_counts().to_frame().sort_values('id',ascending=False).head(10)
  
  # had to hard code this section because i was finding it hard implementing the range method. still 
  # working on the range method
  day_1 = Day(
    id = 1,
    title = 'Day 1',
    display = most_popular(day1).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
    percentage ='N/A'

  )
  
  day_2 = Day(
  id = 2,
  title = 'Day 2',
  display = most_popular(day2).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage ='N/A'

)

  day_3 = Day(
  id = 3,
  title = 'Day 3',
  display = most_popular(day3).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage ='N/A'

)

  day_4 = Day(
  id = 4,
  title = 'Day 4',
  display = most_popular(day4).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage ='N/A'

)

  day_5 = Day(
  id = 5,
  title = 'Day 5',
  display = most_popular(day5).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage ='N/A'

)

  day_6 = Day(
  id = 6,
  title = 'Day 6',
  display = most_popular(day6).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage ='N/A'

)



  day_7 = Day(
  id = 7,
  title = 'Day 7',
  display = most_popular(day7).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage ='N/A'

)



  day_8 = Day(

  id = 8,
  title = 'Day 8',
  display = most_popular(day8).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage = ((day8.id.value_counts() - day1.id.value_counts())/ day1.id.value_counts() * 100).fillna(0).to_frame().to_html() 

)



  day_9 = Day(
  id = 9,
  title = 'Day 9',
  display = most_popular(day9).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage =((day9.id.value_counts() - day2.id.value_counts())/ day2.id.value_counts() * 100).fillna(0).to_frame().to_html() 

)

  day_10 = Day(
  id = 10,
  title = 'Day 10',
  display = most_popular(day10).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage =((day10.id.value_counts() - day3.id.value_counts())/ day3.id.value_counts() * 100).fillna(0).to_frame().to_html() 

)

  day_11 = Day(
  id = 11,
  title = 'Day 11',
  display = most_popular(day11).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage = ((day11.id.value_counts() - day4.id.value_counts())/ day4.id.value_counts() * 100).fillna(0).to_frame().to_html()

)



  day_12 = Day(
  id = 12,
  title = 'Day 12',
  display = most_popular(day12).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage = ((day12.id.value_counts() - day5.id.value_counts())/ day5.id.value_counts() * 100).fillna(0).to_frame().to_html()

)



  day_13 = Day(
  id = 13,
  title = 'Day 13',
  display = most_popular(day13).rename(columns={'id': 'id_counts'} ).reset_index().to_html(),
  percentage = ((day13.id.value_counts() - day6.id.value_counts())/ day6.id.value_counts() * 100).fillna(0).to_frame().to_html()

)


  

  context = {'days': [day_1,day_2,day_3,day_4,day_5,day_6,day_7,day_8,day_9,day_10,day_11,day_12
  ,day_13], 'current_date':datetime.now()}
  return render(request, "view1.html",context)


# ====================View2 Begins here =======================


def view2(request):
  reports = pd.read_csv('status/report.csv') # reeading the report file with pandas
  reports['timestamp']= pd.to_datetime(reports.timestamp) # parsing the timestamps to datetime
  available_types = reports[reports.type == 'gateway']
  available_types = available_types.groupby([reports.timestamp.dt.day,'type'])['id'].count().to_frame().to_html()

  context = {
    'type': available_types
  }

  return render(request,"view2.html",context)




def gateway(request):
  reports = pd.read_csv('status/report.csv') # reading the report file with pandas
  reports['timestamp']= pd.to_datetime(reports.timestamp) # parsing the timestamps to datetime
  available_types = reports[reports.type == 'gateway'] #group the device by type
  available_types = available_types.groupby([reports.timestamp.dt.day,'type'])['id'].count().to_frame()
  available_types = available_types.rename(columns={'id':'total_devices'} ).head(30).to_html()

  context = {
    'type': available_types
  }

  return render(request,"gateway.html",context)





def sensor(request):
  reports = pd.read_csv('status/report.csv') # reading the report file with pandas
  reports['timestamp']= pd.to_datetime(reports.timestamp) # parsing the timestamps to datetime
  available_types = reports[reports.type == 'sensor'] #group the device by type
  available_types = available_types.groupby([reports.timestamp.dt.day,'type'])['id'].count().to_frame()
  available_types = available_types.rename(columns={'id':'total_devices'} ).head(30).to_html()

  context = {
    'type': available_types
  }

  return render(request,"sensor.html",context)