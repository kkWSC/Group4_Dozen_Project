import streamlit as st
import pageManager as pM


def start():
    """
    Main function for starting the visualization system.
    """
    # start-page: sign in page
    hotel_name = pm1.start_page()

    if hotel_name:
        pm1.set_name(hotel_name)
        # show home page
        pm1.show_home()

    # setting background pattern
    bg_image1 = """
    <style>
    [data-testid="stAppViewContainer"]{
        width: 100%;
        height: 100%;
        background-size: cover
        background-position: center center;
        background-repeat:repeat;
        background-image: url(./bg.png)
        }
    [data-testid="stHeader"]{
        background-color:rgba(0, 0, 0, 0)
        }
    </style>
    """
    st.markdown(bg_image1, unsafe_allow_html=True)

    # setting sidebar pattern
    bg_image2 = """
    <style>
    [data-testid="stSidebar"]{
        background-color:#96B4E1
        }
    </style>
    """
    st.markdown(bg_image2, unsafe_allow_html=True)

    # set the metric color to white
    bg_image3 = """
    <style>
    [data-testid="stMetricLabel"]{
        color: white
        }
    [data-testid="stMetricValue"]{
        color: white
        }
    </style>
    """
    st.markdown(bg_image3, unsafe_allow_html=True)


# Set the page config to widescreen mode.
st.set_page_config(layout="wide", page_title="Hotel Financial Analysis Visualization System",
                   page_icon=":currency_exchange:")

# Define a PageManager object pm1.
pm1 = pM.PageManager("Unknown")

if __name__ == '__main__':
    # Call the start() function to start the visualization system.
    start()
