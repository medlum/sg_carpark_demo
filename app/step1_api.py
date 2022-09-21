import requests, datetime, time, json
import streamlit as st

#---------- shopping mall carpark data from lta api ------------#
## require api key from LTA ##
## require specific header as as api parameters ##

url = "http://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2"
#headers = {"AccountKey": "",
#           "accept": "application/json"}
headers = {"AccountKey": st.secrets["LTA_APIKEY"],
           "accept": "application/json"}
response = requests.request(method="get", url=url, headers=headers)
lta_data = response.json()
#print(json.dumps(lta_data, indent=4))


#---------------- hdb carpark data from data.gov.sg api ----------------#
## require current date and time as part of query parameter ##
## hence need to set up system time using datetime module ##

##------ set up system current date and time first ------##

# set to system current datetime and remove microseconds
now_dt = datetime.datetime.today().replace(microsecond=0)
# convert string to include "T" as part of the required format of query parameter
now_str = str(now_dt)
now_T = now_str.replace(' ', 'T')
# add 8 hours server due to timezone difference in streamlit using timedelta class
now_modifed = str(now_dt + datetime.timedelta(hours=8))

##------ connect to data.gov.sg api url ------##
## does not require api key ##

endpoint = "https://api.data.gov.sg/v1/transport/carpark-availability"
# query parameter
query_params = {'date_time': now_T}
# get data and convert to json
data = requests.get(endpoint, params=query_params).json()
#print(json.dumps(data, indent=4))
