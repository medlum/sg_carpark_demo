import streamlit as st
import folium
from utils import *
from streamlit_folium import folium_static
from step2_process_data import location, mall_names, malls, complete_list

####------- configure the webpage in streamlit app -------####

# setup webpage in streamlit 
st.set_page_config(
    page_title='Carpark Availability',
    page_icon=':shark:',
    layout="wide",
    menu_items={"About": "Data is updated on one minute interval"})

# create a wallpaper in the app
set_bg("assets/wallpaper.jpg") 

# create headers and information for the app
head() 

####------- user to select hdb carpark ---------####

st.header("HDB Carpark")

# use of multiselect widget for user to select the hdb carparks by street name.
# note: there could have more than one carpark in the same street.
with st.expander("HDB"):
    filter_hdb = st.multiselect("You may select more than one", location)
    
####------- user to select shopping mall carpark ---------####
st.header("Shopping Malls Carpark")

# use of multiselect widget for user to select the sooping mall carparks by mall name.
with st.expander("Shopping Mall"):
    filter_malls = st.multiselect("You may select more than one", mall_names)

####------- setup folium base map ---------####
m = folium.Map(location=[1.3521, 103.8198],
               min_zoom=11,
               max_zoom=18,
               zoom_start=12,
               max_bounds=True,
               tiles="CartoDB positron",
               name="Light Map")

####------- display the selected carparks using the metric widget ---------####

## shopping malls ##
if len(filter_malls) != 0:
    for index in range(len(malls)):
        # malls[index][0] refers to the mall's name
        if malls[index][0] not in filter_malls:
            pass
        else:
            mall_selected = malls[index][0] # malls name
            lots_avail = malls[index][3] # lots available
            mall_lat = malls[index][1] # longtitide 
            mall_long = malls[index][2] # latitude
            
            # create a metric to display data
            st.metric(label=mall_selected, value=lots_avail) 
            # create a custom icon
            mall_icon = folium.CustomIcon(icon_image='assets/mall_icon.png', icon_size=(30, 30))
            # put a marker to the map
            folium.Marker(location=[mall_lat, mall_long], icon=mall_icon).add_to(m)
            folium.Marker(location=[mall_lat, mall_long], icon=mall_DivIcon(mall_selected, lots_avail)).add_to(m)

## hdb carparks ##
if len(filter_hdb) != 0:

    for index in range(len(complete_list)):
        if complete_list[index][2] not in filter_hdb:
            pass
        else:         
            avail = complete_list[index][7] # available lots
            total = complete_list[index][6] # total lots
            hdb_selected = complete_list[index][3] # hdb block
            hdb_long = complete_list[index][4] # longtitude
            hdb_lat = complete_list[index][5] # latitude

            # create a metric to display data
            st.metric(label=hdb_selected, value=avail)
            # create a custom icon
            hdb_icon = folium.CustomIcon(icon_image='assets/carpark_logo.jpg', icon_size=(20, 20))
            # put a marker to the map
            folium.Marker(location=[hdb_long, hdb_lat], tooltip=folium.Tooltip(f"{hdb_selected} <br> Total {total} <br> Available {avail}"),
                          icon=hdb_icon).add_to(m)


####------- display folium map ---------####

with st.expander("View Map"):

    st.write(map_text, unsafe_allow_html=True) # map text is from utils 
    folium_static(m, width=250, height=500)

st.write(update_text, unsafe_allow_html=True) # update_text is from utils
