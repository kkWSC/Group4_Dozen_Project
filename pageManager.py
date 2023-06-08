import string
import streamlit as st
import income as ic
import expenditure as ex
import profit as pf
import page as pg


class PageManager:
    def __init__(self, name: string) -> None:
        """
        Create an PageManager object with the given hotel name.
        """
        self.name = name
        self.page1 = pg.Page(self.name)

    def set_name(self, name):
        """
        Set the hotel name.
        """
        self.name = name

    def start_page(self):
        """
        Show the start page and receive the hotel name from the user.
        """
        start_page1 = st.empty()
        start_intro = st.empty()
        start_page2 = st.empty()
        start_page3 = st.empty()

        start_page1.markdown("<h1 style='text-align: center; color: white;'>" 
                             "Welcome to Hotel Financial Analysis Visualization System!</h1>", unsafe_allow_html=True)
        start_intro.markdown("<p style='text-align: center; color: #C0C0C0;'>" 
                             "This website is designed to help hotel businesses analyze their financial situation</p>",
                             unsafe_allow_html=True)
        start_page2.markdown("<h3 style='text-align: center; color: white;'>Please enter your hotel name:</h3>",
                             unsafe_allow_html=True)
        hotel_name = start_page3.text_input("", key="hotel_name")

        if hotel_name:
            start_page1.empty()
            start_intro.empty()
            start_page2.empty()
            start_page3.empty()
            return hotel_name

    def show_home(self):
        """
        Show the main page of the visualization system.
        """
        home1 = st.empty()
        # divide the page using line
        st.markdown("<hr style='border-top: 2px solid white; width: 100%;'>", unsafe_allow_html=True)
        home1.markdown(f"<h1 style='text-align: center; color: white;'>" 
                       f"Welcome to {self.name} Hotel Data Visualization Systems!</h1>", unsafe_allow_html=True)

        # menu page
        with st.sidebar:
            st.markdown(f"<h1 style='font-size: 36px; color : #393980'>{self.name} Hotel</h1>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='font-size: 18px'>Menu Bar</h1>", unsafe_allow_html=True)
            st.markdown("<hr style='border-top: 2px solid #B0C4DE; width: 100%;'>", unsafe_allow_html=True)
            select_page = st.radio('Please select the page:', ['Revenue', 'Expenditure', 'Profit'])
            st.write("")
            year = st.selectbox('please select the year:', ['2022', '2021', '2020'])
            st.write("")

            if select_page == "Revenue":
                element = st.radio('Please select the attribute:', ['Room_Revenue', 'Catering_Revenue',
                                                               'Meetings_And_Events', 'Entertainment', 'Other_Revenue'])
                self.page1 = ic.Income(self.name, "REVENUE", year, element)

            if select_page == "Expenditure":
                element = st.radio('Please select the attribute:',
                                   ['Hotel_Maintenance', 'Labor', 'Water_And_Electricity',
                                    'Material_Procurement', 'Marketing_And_Publicity'])
                self.page1 = ex.Expenditure(self.name, "EXPENDITURE", year, element)

            if select_page == "Profit":
                self.page1 = pf.Profit(self.name, "PROFIT", year)

            st.markdown("<hr style='border-top: 2px solid #B0C4DE; width: 100%;'>", unsafe_allow_html=True)

            if st.button("flushed"):
                st.write("The page has been refreshed")

            st.markdown("**[# HELP #](https://cn.bing.com/)**", unsafe_allow_html=True)

        # Show the selected page
        self.page1.show_page()
