import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
a = HTTPBasicAuth('93857094983055b7', 'c1b26c7dfdb521cb')
r = requests.get(url='http://tsdashboard.analyticservice.net/employees-list', auth=a)

#或者直接(只加载requests模块就行)
# r = requests.get(url=('http://xxx.xxx.xxx'), auth=('user', 'password'))
json_data = json.loads(r.text)
for i in range(0,len(json_data['response'])):
    try :
        json_data['response'][i]['departments_id']=json_data['response'][i]['departments'][0]['wechat_id']
    except KeyError:
        json_data['response'][i]['departments_id'] = 0
    try :
        json_data['response'][i]['departments_name']=json_data['response'][i]['departments'][0]['name']
    except KeyError:
        json_data['response'][i]['departments_name'] = 0

# print(json_data['response'][0])
# print(type(json_data['response'][0]))
# print(type(json_data['response']))
# print(len(json_data['response']))
dic = {}
# print(json_data['response'][0]['departments'])
# print(type(json_data['response'][0]['departments']))
# 需要的几个字段
key_list = ['id', 'name', 'code', 'mobile', 'email', 'departments', 'job_status', 'position', 'departments_name']

df_list = []

for i in range(0, len(json_data['response'])):
    df = {}
    try:
        df['id'] = json_data['response'][i]['id']
    except KeyError:
        df['id'] = 0
    try:
        df['name'] = json_data['response'][i]['name']
    except KeyError:
        df['name'] = 0
    try:
        df['code'] = json_data['response'][i]['code']
    except KeyError:
        df['code'] = 0
    try:
        df['mobile'] = json_data['response'][i]['mobile']
    except KeyError:
        df['mobile'] = 0
    try:
        df['email'] = json_data['response'][i]['email']
    except KeyError:
        df['email'] = 0
    try:
        df['job_status'] = json_data['response'][i]['job_status']
    except KeyError:
        df['job_status'] = 0
    try:
        df['departments_id'] = json_data['response'][i]['departments_id']
    except KeyError:
        df['departments_id'] = 0
    try:
        df['position'] = json_data['response'][i]['position']
    except KeyError:
        df['position'] = 0
    try:
        df['departments_name'] = json_data['response'][i]['departments_name']
    except KeyError:
        df['departments_name'] = 0

    df_list.append(df)
data = pd.DataFrame()
for i in range(0, len(df_list)):
    if len(df_list[i]['code']) > 4:
        continue
    data_df = pd.DataFrame(df_list[i], index=[0])
    data = data.append(data_df)
#data = data[data['job_status'] == 0]
data = data.rename(columns={'code': 'employe_code', 'email': 'email', 'id': 'employe_id',
                            'job_status': 'job_status', 'mobile': 'phone_number', 'name': 'employe_name',
                            'departments_id': 'dep_id', 'position': 'employe_type', 'departments_name': 'dep_name'})
data_gm = data[ (data['employe_name']!='杨明华_miller') & (data['dep_id'] == 44) | (data['dep_id'] == 91) ]
data_gm['employe_type'] ='GM'
data_gm['employe_type_id'] = 1
data_gm=data_gm[data_gm['employe_name'] != '杨明华_miller']
data_pe =  data[(data['dep_name'].str.contains(r'Deliver_*')|(data['employe_name']=='王振_Alexander')) &  (data['employe_type'] == 'PE')]
data_pe['employe_type'] ='PE'
data_pe['employe_type_id'] =2
data_sales =  data[(data['dep_name'].str.contains(r'Sales*')) |(data['employe_name']=='顾怡潇_Pauline') |(data['employe_name']=='史朔_Shuo') ]
data_sales['employe_type'] ='Sales'
data_sales['employe_type_id'] =3
data_finance = data[(data['employe_name']=='张俐舒_Gigi') |(data['employe_name']=='杨明华_miller')
 |(data['employe_name']=='刘彦_Lily') |(data['employe_name']=='杨丽韫_Vicky')
 |(data['employe_name']=='金奕_Lucy') |(data['employe_name']=='郭晶_Jessie')
 |(data['employe_name']=='张佳佳_JiaJia') |(data['employe_name']=='张嘉桐_Annie')|(data['employe_name']=='李曦_Xi')|(data['employe_name']=='俞愈_Rain')]
data_finance['employe_type'] ='Finance'
data_finance['employe_type_id'] =4


print(data_sales[data_sales['employe_name'] == '史朔_Shuo'])
