import streamlit as st
import base64
from folium.features import DivIcon
from step1_api import now_modifed

def head():
    """
    Function is used to create headers, caption, description of the app
    and display current date and time.
    - st.markdown for header
    - st.caption for caption
    - st.write for description and current date and time
    """
    st.markdown("""
        <h2 style='text-align: center; margin-bottom: -35px;'>
        SG Car Park App \U0001F17F
        </h2>""", unsafe_allow_html=True)

    st.caption("""
        <p style='text-align: center'>
        by <a href='https://github.com/medlum'>medlum</a>
        </p>""", unsafe_allow_html=True)

    st.write("""
        <p style="font-size:25px";'text-align: center'>
        Find out how many parking lots are available!
        </p>""", unsafe_allow_html=True)

    st.write(f"<p style='text-align: left; color:GreenYellow'> Current Date Time: {now_modifed}</p>", unsafe_allow_html=True)


@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    """
    Function use base64 to encode and decode wallpaper.
    It calls for another custome function: get_base64
    """
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>.stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;} </style> """ % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)


def mall_DivIcon(mall_selected, lots_avail):
    """
    Create a HTML icon to display available shopping mall 
    carparks.
    """
    icon = DivIcon(
        icon_size=(180, 180),
        icon_anchor=(100, 35),
        html=f'<p style="font-size: 10pt; color : DarkSlateGray; text-align: center"> <strong> {mall_selected} <br> <br> <br> Available: {lots_avail}</strong></p>'
    )
    return icon


map_text = """
 <p style='text-align: left; color:AliceBlue';'>
 Map displays the number of parkings lots available in the select carparks.</p>
"""

update_text = f"<p style='text-align: left; color:Grey'> Data is updated on one minute interval</p>"
