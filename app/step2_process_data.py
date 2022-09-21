from step1_api import data, lta_data
from cp_dict import cp_dict

#----------------- process shopping malls carpark data -----------------#

malls = []
for item in lta_data["value"]:
    if item["Area"] != "":
        malls.append([item["Development"], float(item["Location"].split(" ")[
                     0]), float(item["Location"].split(" ")[1]), item["AvailableLots"]])

# append the names of the shopping malls to a variable, mall_names.
# the variable will be used for streamlit multiselect function later.
mall_names = [mall[0] for mall in malls]

#---------------- process hdb carpark data -----------------#

# api data contains carpark codes, total and available lots
cp_code = [] 
total_lots = []
avail_lots = []

# data variable is from api_call
for item in data["items"]:
    for detail in item["carpark_data"]:
        # extract carpark_code, total lots and available lots
        cp_code.append(detail['carpark_number'])
        total_lots.append(detail["carpark_info"][0]["total_lots"])
        avail_lots.append(detail["carpark_info"][0]["lots_available"])

# removed first element as it is not useful
total_lots = total_lots[1:]
avail_lots = avail_lots[1:]

#---------------- refine the hdb carpark after extraction -----------------#

# hdb carpark codes alone is not useful, it is more useful to know the carpark address
# a dictionary that contains the details like the carpark address are available, so lets
# make use of this dictionary to match carpark codes with its details.

complete_list = []

for index in range(len(cp_code) - 1):
    if cp_code[index] in cp_dict:
        complete_list.append([index,
                              cp_code[index], # carpark code
                              cp_dict[cp_code[index]][0], # street name
                              cp_dict[cp_code[index]][1], # carpark block number
                              float(cp_dict[cp_code[index]][2]), # longtitude
                              float(cp_dict[cp_code[index]][3]), # latitude
                              total_lots[index],  
                              avail_lots[index]])


# append "street name" (index 2) from complete list to a variable, "location"
# the variable will be used for streamlit multiselect function later.
# location variable is convert to "set" data structure and back as a list again. 
# "set" keeps the unique street name.

location = sorted(list(set([address[2] for address in complete_list])))

#print(complete_list[1])
#print(complete_list[1][4])
#
print(malls)
#print(malls[0][1])
