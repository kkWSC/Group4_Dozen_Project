import page as pg
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# create a subclass -- Expenditure, inherit from Page class
class Expenditure(pg.Page):

    def __init__(self, name, m_name, year):
        """
        Constructor function to initialize variables and load data from csv files.
        """
        super().__init__(name)  # invoke constructor function of father class
        self.m_name = m_name  # page name
        self.year = year  # year of expenditure data
        self.de = pd.read_csv(f'{self.year}_expend.csv')  # read csv file and store as a pandas dataframe

    def show_content(self):
        """
        A function to show the content of this page.
        """
        # Set page title
        st.markdown(f"<h1 style='text-align: center; color: white;'>Welcome to Page {self.m_name}</h1>",
                    unsafe_allow_html=True)

        # Add white space
        st.write("")
        st.write("")
        st.write("")

        # Plot charts
        col21, col22 = st.columns([1, 1])
        with col21:
            self.total_outlay()
        with col22:
            self.classify_outlay()

        # Add white space
        st.write("")

        # Show detailed outlay
        self.outlay_detail()

    def total_outlay(self):
        """
        A function to calculate total expenditure for each month and plot a bar chart of total expenditure.
        """
        # Calculate total expenditure for each month by summing up the expenditure items
        self.de['Total_Outlay'] = self.de.apply(
            lambda row: row['Hotel_Maintenance'] + row['Labor'] + row['Water_And_Electricity'] +
                        row['Material_Procurement'] + row['Marketing_And_Publicity'], axis=1)

        # Group monthly total expenditures by month and plot a bar chart
        total_outlay_by_month = self.de.groupby('Month')['Total_Outlay'].sum()
        fig1, ax = plt.subplots()
        total_outlay_by_month.plot(kind='bar', ax=ax, color='#6A5ACD')

        # Set chart title and axis labels and adjust font style, color and size
        font = {'color': 'white', 'size': 16}
        ax.set_title('Total Expenditure', fontdict=font)
        ax.set_xlabel('Month', fontdict=font)
        ax.set_ylabel('Expenditure', fontdict=font)

        # Change the rotation of x-axis ticks from vertical to horizontal
        plt.xticks(rotation=0)

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

        # Set transparent background for chart
        fig1.patch.set_alpha(0.0)

        # Show the bar chart
        st.pyplot(fig1)

    def classify_outlay(self):
        """
        A function to calculate and plot the proportion of each expenditure item by category
        using a donut chart.
        """
        # Create a dataframe containing the sum of each expenditure item
        outlay_by_category = pd.DataFrame({
            'Category': ['Hotel Maintenance', 'Labor', 'Water And Electricity', 'Material Procurement',
                         'Marketing And Publicity'],
            'Outlay': [self.de['Hotel_Maintenance'].sum(), self.de['Labor'].sum(),
                       self.de['Water_And_Electricity'].sum(),
                       self.de['Material_Procurement'].sum(), self.de['Marketing_And_Publicity'].sum()]
        })

        # Create a donut chart of the proportion of each expenditure item
        fig2, ax = plt.subplots(figsize=(4, 4))
        wedges, texts, autotexts = ax.pie(outlay_by_category['Outlay'], labels=outlay_by_category['Category'],
                                          autopct='%1.1f%%', pctdistance=0.85,
                                          wedgeprops=dict(width=0.4, edgecolor='#00008B', linewidth=1),
                                          colors=self.colors)

        # Set chart title and adjust font style, size and color
        font = {'color': 'white', 'size': 16}
        ax.set_title('Expenditure by Category', fontdict=font)

        # Adjust the appearance of text labels
        plt.setp(autotexts, size=9, weight="bold", color="white")
        plt.setp(texts, size=10, color="white")

        # Set transparent background for chart
        fig2.patch.set_alpha(0.0)

        # Show the donut chart
        st.pyplot(fig2)

    def outlay_detail(self):
        """
        A function to plot a bar chart of detailed expenditure by month for each expenditure item.
        """
        # Calculate detailed expenditure by month for each expenditure item
        hotel_maintenance_by_month = self.de.groupby('Month')['Hotel_Maintenance'].sum()
        labor_by_month = self.de.groupby('Month')['Labor'].sum()
        water_and_electricity_by_month = self.de.groupby('Month')['Water_And_Electricity'].sum()
        material_procurement_by_month = self.de.groupby('Month')['Material_Procurement'].sum()
        marketing_and_publicity_by_month = self.de.groupby('Month')['Marketing_And_Publicity'].sum()

        # Plot a bar chart and customize its style
        x = range(1, len(self.de['Month'].unique()) + 1)
        height = 0.16
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar(x, hotel_maintenance_by_month, height, label='Hotel Maintenance', color=self.colors[0])
        ax.bar([i + height for i in x], labor_by_month, height, label='Labor',
               color=self.colors[1])
        ax.bar([i + height * 2 for i in x], water_and_electricity_by_month, height, label='Water And Electricity',
               color=self.colors[2])
        ax.bar([i + height * 3 for i in x], material_procurement_by_month, height, label='Material Procurement',
               color=self.colors[3])
        ax.bar([i + height * 4 for i in x], marketing_and_publicity_by_month, height, label='Marketing And Publicity',
               color=self.colors[4])

        # Show the legend and customize its style and location
        legend = ax.legend(fontsize=12, loc='upper left')
        for text in legend.get_texts():
            text.set_color('white')
        frame = legend.get_frame()
        frame.set_facecolor('gray')
        frame.set_edgecolor('gray')
        frame.set_alpha(0.2)

        # Set axis labels and adjust font style, color and size
        font = {'color': 'white', 'size': 16}
        ax.set_xlabel('Month', fontdict=font)
        ax.set_ylabel('Expenditure', fontdict=font)
        ax.set_xticks([i + height * 2 for i in x])
        ax.set_xticklabels(self.de['Month'].unique(), fontdict=font)
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

        # Setting title for the chart and adjust font style
        ax.set_title(f'Breakdown of Expenditure in {self.year}', fontdict=font)

        # Set the chart background transparency
        fig.patch.set_alpha(0.0)

        # Display the chart figure
        st.pyplot(fig)
