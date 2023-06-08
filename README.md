<<<<<<< HEAD
=======
# Group4_Dozen_Project
Group4_Dozen_Project, this is a simple visualization system.
>>>>>>> a455c9c1be8fb00bedcaec8e851811de8940ab3f
# Hotel Financial Analysis Visualization System

The system is designed specifically for hotel managers and relevant stakeholders so that they can track the financial condition of the hotel and make appropriate business decisions.We will show the data visualization of the financial statements of a hotel in the past three years.This system  describes a data visualization website that displays financial reports to stakeholders.The financial report includes the hotel's monthly expenditure, revenue, profit and other relevant data for the past three years.Pie charts, bar charts, line charts, map and other types of charts are used to display data to help hotel managers analyze the financial situation of the hotel and make appropriate business decisions.


## Install

1.  Download and decompress the project compression package: " Group4_Project. The zip " and put into the C root directory.
2. Open the command line and go to the C disk root directory.
3. Enter the following command to install the library function:
	pip install  streamlit
	pip install  pandas
	pip install  matplotlib
	pip install pyecharts

# # Program run preparation

 Find the following file in the project root folder and open it for editing:
	"20xx_expend.csv "  Enter the corresponding 12 months of hotels in the table.
	"20xx_income.csv "  Enter the corresponding five categories revenue data for 12 months in the table.
	"Anhui_profit.xlsx"   Enter the profit data of hotels in various cities in Anhui province in the table.
	"China_profit.xslx"   Enter profit data for hotels in Chinese provinces in the table.
	"profit.csv "          Enters the profit data of each monthly hotel for 3 years.

## The program is run steps

1.  Start the command-line program and enter: " streamlit run main.py "
2.  The computer's default browser will automatically open the web page for access.

 
## system function

1.	 Go to the website and enter the hotel name.
 

2.	 For the web page, the left column provides three choices of Revenue / Expenditure / Profit.
	 If you click the first Revenue in the left column and select the year you want to query from the drop-down menu below, the right page will show the income statistics of the current year. The bar chart shows the total income of each of the 12 months of the year, and the pie chart shows the proportion of the five categories of income sources.	
 
After the decline, a more detailed bar chart of classified income statistics is displayed.
These five categories are, respectively:
	Room revenue
	Catering revenue
	Meetings and events
	Entertainment
	Other revenue

 

	 If you click the second Expenditure in the left column and select the year you want to query from the drop-down menu below, the right page will show the expenditure statistics of the current year. The bar chart shows the total expenditure of the 12 months of the year, and the pie chart shows the proportion of the five categories of expenditure. 

After the decline, a more detailed bar chart of classified income statistics is displayed.
These five categories are, respectively:
	Hotel Maintenance
	Labor
	Water and electricity
	Material procurement
	 Marketing and publicity
 

	 Click the third Profit in the left column, and the four figures you see are respectively "profit of the month", "monthly year-on-year growth", "total profit of this year" and "three-year total profit". The green percentage below is the corresponding percentage of year-over-year growth.
    The line chart below shows the profit changes in the last three years and 12 months. The pie chart on the right is the proportion of profit for three years.

 











 After the slide page, the page shows a map of the total revenue of other regions.
 
 When the mouse is moved to the corresponding map area, the profit data of the corresponding province or city is displayed.
  

 There is a data filter bar in the lower left corner of the map. When we drag the limit slider of the upper and lower limit, the provinces or cities with profit are displayed in the map, and the provinces or cities with profit not in the range will not be displayed (automatically hidden).

  
After the page continues to slide, the page shows a revenue map for the current year.
 


3.	The button at the bottom of the left bar, "flushed", can click to refresh the entire page.(Especially suitable to refresh web data after updating the database)
 


## Project code structure simple examination:
	Main -> pm1(pageManager) -> page1(page) -> [ revenue :: expenditure :: profit ]

