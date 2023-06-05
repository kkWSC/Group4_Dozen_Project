import streamlit as st


class Page:
    def __init__(self, name):
        """
        A Page object with a hotel name and a color pattern.
        """
        self.name = name
        self.colors = ['#4169E1', '#00BFEF', '#6A5ACD', '#00DF8A', '#DF9500']

    def show_tail(self):
        """
        Show the footer with links and credits information.
        """
        # Vertical divider
        st.markdown(
            """ <style> .st-border-right { border-right: 2px solid #ced4da; 
            padding-right: 15px; margin-right: 15px; } </style> """,
            unsafe_allow_html=True)

        # Divide the page using line
        st.markdown("<hr style='border-top: 2px solid white; width: 100%;'>", unsafe_allow_html=True)

        # Add footer information to four columns
        col1, col2, col3, col4 = st.columns([3, 3, 1, 2])

        col1.markdown(
            "<div style='text-align: center' class='st-border-right'<strong>" 
            "<a href='https://cn.bing.com/search?q=%E9%85%92%E5%BA%97'>About Us</a></strong></div>",
            unsafe_allow_html=True)

        col2.markdown(
            "<p style='text-alin: center; color: #C0C0C0' class='st-border-right'>" 
            "<em>© Copyright 2023 KK Group Dozen ©</em></p>",
            unsafe_allow_html=True)

        col3.markdown(
            "<div style='text-align: right' <strong><a href='https://wx.mail.qq.com/'>Contact us:</a></strong></div>",
            unsafe_allow_html=True)

        col4.markdown("<p style='color: #C0C0C0'>1234567890.qq.com</p>", unsafe_allow_html=True)
        st.write("")

        st.markdown("<p style='text-align: center; color: gray;'>Dozen Limited Liability Company</p>",
                    unsafe_allow_html=True)

    def show_content(self):
        """
        The child class will override this method to show specific content.
        """
        pass

    def show_page(self):
        """
        Show the content of the page with the footer information
        """
        self.show_content()
        self.show_tail()
