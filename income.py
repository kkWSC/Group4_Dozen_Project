import streamlit as st
import page as pg
import pandas as pd
import matplotlib.pyplot as plt


class Income(pg.Page):
    def __init__(self, name, m_name, year, elment):
        """
        Initializes the Income class object.
        Args:
        name (str): the name of the hotel.
        m_name (str): the name of the page.
        year (int): the year for which the income records need to be displayed.
        """
        super().__init__(name)  # invoke function from father class
        self.m_name = m_name
        self.year = year
        self.element = elment
        self.di = pd.read_csv(f'{self.year}_income.csv')  # read data from CSV file

        self.color_dict = {
            "Room_Revenue": 0,
            "Catering_Revenue": 1,
            "Meetings_And_Events": 2,
            "Entertainment": 3,
            "Other_Revenue": 4
        }

    def show_content(self):
        """
        Display the content of the income page.
        """
        st.markdown(f"<h1 style='text-align: center; color: white;'>Welcome to Page {self.m_name}</h1>",
                    unsafe_allow_html=True)

        # Add empty lines
        st.write("")
        st.write("")
        st.write("")

        # Display charts
        col21, col22 = st.columns([3, 2])
        with col21:
            self.total_revenue()

        with col22:
            self.classify_revenue()

        # Add empty line
        st.write("")

        # Display detailed histogram
        self.revenue_detail()

        self.revenue_detail_by_each()

    def total_revenue(self):
        """
        Generate a bar chart to display the total revenue by month.
        """
        # Add up all rows to get total income
        self.di['Total_Revenue'] = self.di.apply(
            lambda row: row['Room_Revenue'] + row['Catering_Revenue'] + row['Meetings_And_Events'] +
                        row['Entertainment'] + row['Other_Revenue'], axis=1)

        # Group the total income according to the month
        total_revenue_by_month = self.di.groupby('Month')['Total_Revenue'].sum()

        # Generate a bar chart
        fig1, ax = plt.subplots()
        total_revenue_by_month.plot(kind='bar', ax=ax, color='#6A5ACD')

        # Add title and axis labels, and adjust font color and size
        font = {'color': 'white', 'size': 16}
        ax.set_title(f'Total Revenue in {self.year}', fontdict=font)
        ax.set_xlabel('Month', fontdict=font)
        ax.set_ylabel('Revenue', fontdict=font)

        # Change the orientation of x-axis text from vertical to horizontal
        plt.xticks(rotation=0)

        # Set the background of the histogram to transparent and adjust font color and size
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color='orange', linestyle='dashed', alpha=0.5)
        ax.set_facecolor('none')
        for tick in ax.get_xticklabels():
            tick.set_color('white')
            tick.set_fontsize(10)
        for tick in ax.get_yticklabels():
            tick.set_color('white')
            tick.set_fontsize(10)

        # Set the chart background to transparent
        fig1.patch.set_alpha(0.0)

        # Display the chart
        st.pyplot(fig1)

    def classify_revenue(self):
        """
        Generate a donut chart to display the proportion of different types of revenue.
        """
        # Pie chart section
        # Create a DataFrame that contains the total revenue for each income category
        revenue_by_category = pd.DataFrame({
            'Category': ['Room Revenue', 'Catering Revenue', 'Meetings and Events', 'Entertainment', 'Other Revenue'],
            'Revenue': [self.di['Room_Revenue'].sum(), self.di['Catering_Revenue'].sum(),
                        self.di['Meetings_And_Events'].sum(),
                        self.di['Entertainment'].sum(), self.di['Other_Revenue'].sum()]
        })

        # Draw the donut chart
        fig2, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(revenue_by_category['Revenue'], labels=revenue_by_category['Category'],
                                          autopct='%1.1f%%', pctdistance=0.85,
                                          wedgeprops=dict(width=0.4, edgecolor='#00008B', linewidth=1),
                                          colors=self.colors)

        # Add title and adjust font color and size
        font = {'color': 'white', 'size': 16}
        ax.set_title('Revenue by Category', fontdict=font)

        # Adjust text appearance
        plt.setp(autotexts, size=9, weight="bold", color="white")
        plt.setp(texts, size=10, color="white")

        # Set the chart background to transparent
        fig2.patch.set_alpha(0.0)

        # Add empty lines
        st.write("")
        st.write("")

        # Display the chart
        st.pyplot(fig2)

    def revenue_detail(self):
        """
        Calculate the monthly revenue by category, plot a bar chart with custom style and show the chart.
        """

        # Calculate the monthly revenue by category
        room_revenue_by_month = self.di.groupby('Month')['Room_Revenue'].sum()
        catering_revenue_by_month = self.di.groupby('Month')['Catering_Revenue'].sum()
        meetings_and_events_by_month = self.di.groupby('Month')['Meetings_And_Events'].sum()
        entertainment_by_month = self.di.groupby('Month')['Entertainment'].sum()
        other_revenue_by_month = self.di.groupby('Month')['Other_Revenue'].sum()

        # Plot a bar chart with custom style
        x = range(1, len(self.di['Month'].unique()) + 1)
        height = 0.16
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x, room_revenue_by_month, height, label='Room Revenue', color=self.colors[0])
        ax.bar([i + height for i in x], catering_revenue_by_month, height, label='Catering Revenue',
               color=self.colors[1])
        ax.bar([i + height * 2 for i in x], meetings_and_events_by_month, height, label='Meetings and Events',
               color=self.colors[2])
        ax.bar([i + height * 3 for i in x], entertainment_by_month, height, label='Entertainment', color=self.colors[3])
        ax.bar([i + height * 4 for i in x], other_revenue_by_month, height, label='Other Revenue', color=self.colors[4])

        # Show legend and customize its style
        legend = ax.legend(fontsize=12)
        for text in legend.get_texts():
            text.set_color('white')
        frame = legend.get_frame()
        frame.set_facecolor('gray')
        frame.set_edgecolor('gray')
        frame.set_alpha(0.2)

        # Set X and Y axis labels and adjust their font style, color and size
        font = {'color': 'white', 'size': 16}
        ax.set_xlabel('Month', fontdict=font)
        ax.set_ylabel('Revenue', fontdict=font)
        ax.set_xticks([i + height * 2 for i in x])
        ax.set_xticklabels(self.di['Month'].unique(), fontdict=font)
        ax.tick_params(axis='both', labelcolor='white', labelsize=10)

        # Set transparent background for chart and adjust font color and size
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color='orange', linestyle='dashed', alpha=0.5)
        ax.set_facecolor('none')
        for tick in ax.get_xticklabels():
            tick.set_color('white')
            tick.set_fontsize(10)
        for tick in ax.get_yticklabels():
            tick.set_color('white')
            tick.set_fontsize(10)

        # Set chart title and adjust font style
        ax.set_title(f'Breakdown of Revenue in {self.year}', fontdict=font)

        # Set transparent background for chart
        fig.patch.set_alpha(0.0)

        # Show chart
        st.pyplot(fig)

    def revenue_detail_by_each(self):
        """
        Calculate the monthly revenue by category, plot a bar chart with custom style and show the chart.
        """
        col1, col2 = st.columns([3, 1])
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.markdown("<h4 style='text-align: right; color:#C0C0C0;'>New features are in development...</h4>",
                        unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: right; color:#C0C0C0;'>Please look forward to it</h4>",
                        unsafe_allow_html=True)

        with col1:
            # Calculate the monthly revenue by category
            show_by_month = self.di.groupby('Month')[f'{self.element}'].sum()

            i = self.color_dict[self.element]
            # Generate a bar chart
            fig1, ax = plt.subplots()
            show_by_month.plot(kind='bar', ax=ax, color=self.colors[i])

            # Add title and axis labels, and adjust font color and size
            font = {'color': 'white', 'size': 16}
            ax.set_title(f'{self.element} in {self.year}', fontdict=font)
            ax.set_xlabel('Month', fontdict=font)
            ax.set_ylabel('Revenue', fontdict=font)

            # Change the orientation of x-axis text from vertical to horizontal
            plt.xticks(rotation=0)

            # Set the background of the histogram to transparent and adjust font color and size
            ax.set_axisbelow(True)
            ax.yaxis.grid(True, color='orange', linestyle='dashed', alpha=0.5)
            ax.set_facecolor('none')
            for tick in ax.get_xticklabels():
                tick.set_color('white')
                tick.set_fontsize(10)
            for tick in ax.get_yticklabels():
                tick.set_color('white')
                tick.set_fontsize(10)

            # Set the chart background to transparent
            fig1.patch.set_alpha(0.0)

            # Display the chart
            st.pyplot(fig1)

