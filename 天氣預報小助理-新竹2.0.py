#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests

radar_url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-0154C4AF-D3C0-4CE4-92A8-F03D3555B0EF&format=JSON&locationName=&elementName=&sort=time'
radar = requests.get(radar_url)
radar_json = radar.json()

radar_record = radar_json['records']['location']


radar_city = radar_json['records']['location'][4]['locationName']
print(radar_city)
radar_element = radar_json['records']['location'][4]['weatherElement'][1]
#print(radar_element)

radar_pop = radar_element['time'][0]
print(radar_pop)

radar_pop_stt = radar_pop['startTime']
print(radar_pop_stt)

radar_pop_edt = radar_pop['endTime']
print(radar_pop_edt)

radar_pop_para = radar_pop['parameter']
print(radar_pop_para)

radar_pop_num = radar_pop_para['parameterName']
print((radar_pop_num) +" %")

pop_num = ((radar_pop_num) +" %")
print(pop_num)

# radar_img = radar_json['cwbopendata']['dataset']['resource']['uri']
# radat_time = radar_json['cwbopendata']['dataset']['time']['obsTime']   # 取得時間
# print(radar_img)

url = 'https://notify-api.line.me/api/notify'
token = 'tvsZBxbRF77CcO5USUcnmwX4aDvxYNwQLETzCMqj9re'
headers = {
    'Authorization': 'Bearer ' + token
}
data = {
    'message': '\n' + radar_city + '\n' + radar_pop_stt + '\n' + radar_pop_edt + '\n' + '今日降雨機率 ' + pop_num
    
}
data = requests.post(url, headers=headers, data=data)


# In[ ]:




