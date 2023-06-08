import page as pg
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.charts import Map
from pyecharts import options as opts


class Profit(pg.Page):
    def __init__(self, name, m_name, year):
        # Invoke the function from the father class
        super().__init__(name)
        # m_name -> page name
        self.m_name = m_name
        # Read data from CSV file
        self.dp = pd.read_csv('profit.csv', index_col=0)
        self.year = year
        # Convert province names from English to Chinese
        self.province_cn2en = {
            "Beijing": "北京市",
            "Tianjin": "天津市",
            "Hebei": "河北省",
            "Shanxi": "山西省",
            "Neimenggu": "内蒙古自治区",
            "Liaoning": "辽宁省",
            "Jilin": "吉林省",
            "Heilongjiang": "黑龙江省",
            "Shanghai": "上海市",
            "Jiangsu": "江苏省",
            "Zhejiang": "浙江省",
            "Anhui": "安徽省",
            "Fujian": "福建省",
            "Jiangxi": "江西省",
            "Shandong": "山东省",
            "Henan": "河南省",
            "Hubei": "湖北省",
            "Hunan": "湖南省",
            "Guangdong": "广东省",
            "Hongkong": "香港特别行政区",
            "Sichuan": "四川省"
        }

        self.city_dict = {
            "Luan": "六安市",
            "Anqing": "安庆市",
            "Hefei": "合肥市",
            "Huangshan": "黄山市",
            "Wuhu": "芜湖市",
            "Xuancheng": "宣城市",
            "Chuzhou": "滁州市"
        }

    def show_content(self):
        # Display title
        st.markdown(f"<h1 style='text-align: center; color: white;'>Welcome to Page {self.m_name}</h1>",
                    unsafe_allow_html=True)

        # Add empty space for formatting
        st.write("")
        st.write("")
        st.write("")

        # Display general overview
        self.yield_overview()

        # Add empty space for formatting
        st.write("")
        st.write("")
        st.write("")

        # Display the chart
        col21, col22 = st.columns([3, 1])
        with col21:
            self.yield_chart()

        with col22:
            self.compare_yield()

        # Add empty space for formatting
        st.write("")
        st.write("")
        st.markdown(f"<h2 style='text-align: center; color: white;'>$ Map of other regions $</h2>",
                    unsafe_allow_html=True)

        # Use CSS style to set the border as dashed lines
        st.markdown("<hr style='border-top: 2px dashed #B0C4DE; width: 100%;'>", unsafe_allow_html=True)

        col31, col32 = st.columns([3, 2])
        with col31:
            self.yield_nation_map_total()
        with col32:
            self.yield_anhui_map_total()

        col41, col42 = st.columns([3, 2])
        with col41:
            self.yield_nation_map_by_year()
        with col42:
            self.yield_anhui_map_year()

    def yield_overview(self):
        col11, col12, col13, col14 = st.columns(4)

        # Select the last row from the data
        last_row = self.dp.iloc[-1]
        # Select the data in the last two columns
        last_month = last_row[10]
        this_month = last_row[11]
        # Calculate the month-on-month profit rate and format the result as a percentage with two decimal digits
        result1 = (this_month - last_month) / last_month
        result1_percent = result1 * 100
        result1_str = "{:.2f}%".format(result1_percent)

        # Select the second-to-last row from the data
        last_second_row = self.dp.iloc[-2]
        # Select the data in the last column from the second-to-last row
        compared_month = last_second_row[11]
        result2 = (this_month - compared_month) / compared_month
        result2_percent = result2 * 100
        result2_str = "{:.2f}%".format(result2_percent)

        # Calculate the year-on-year profit rate and format the result as a percentage with two decimal digits
        this_year = last_row.sum()
        last_year = last_second_row.sum()
        result3 = (this_year - last_year) / last_year
        result3_percent = result3 * 100
        result3_str = "{:.2f}%".format(result3_percent)

        # Calculate the total profit and round the result to two decimal digits
        total_data = self.dp.sum().sum()
        total_data_rounded = round(total_data, 2)

        # Display the results using Streamlit metrics and Markdown syntax
        with col11:
            st.metric("Present Month / Last Month", f"${this_month}", f"{result1_str}")
        with col12:
            st.metric("Present Month Yo-y", f"${this_month}", f"{result2_str}")
        with col13:
            st.metric("Present Year / Last Year", f"${this_year}", f"{result3_str}")
        with col14:
            # Set HTML tags to change the text color to white
            st.markdown("<p style='color:white;'>Total Profit</p>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='font-size: 36px; color:orange'>${total_data_rounded}</h3>", unsafe_allow_html=True)

    def yield_chart(self):
        # Fill in missing values with 0
        self.dp.fillna(0, inplace=True)

        # Group data by year
        grouped = self.dp.groupby(self.dp.index)

        # Create line chart
        fig1, ax = plt.subplots(figsize=(10, 6))
        for i, (year, group) in enumerate(grouped):
            # Plot data for each year, with heavy line weight, markers, and color coding
            ax.plot(self.dp.columns, group.values[0], label=year, linewidth=3,
                    color=self.colors[i % len(self.colors)], marker='o', markeredgecolor='white', markersize=6)

        # Set chart title and axis labels, with font color and size adjustments
        font = {'color': 'white', 'size': 16}
        ax.set_title('Profit line chart 2020-2022', fontdict=font)
        ax.set_xlabel('Month', fontdict=font)
        ax.set_ylabel('Profit', fontdict=font)

        # Set chart background to be transparent and adjust font color and size
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color='orange', linestyle='dashed', alpha=0.5)
        ax.set_facecolor('none')

        # Set legend font and color
        legend = ax.legend(fontsize=10, loc='best')
        for text in legend.get_texts():
            text.set_color('white')
            text.set_fontsize(9)
            frame = legend.get_frame()
            frame.set_alpha(0.0)  # Set legend background to be transparent

        # Adjust axis tick font and color
        for tick in ax.get_xticklabels():
            tick.set_color('white')
            tick.set_fontsize(9)
        for tick in ax.get_yticklabels():
            tick.set_color('white')
            tick.set_fontsize(9)

        # Set chart background to be transparent
        fig1.patch.set_facecolor('#1e1e1e')
        fig1.patch.set_alpha(0.0)

        # Display chart
        st.pyplot(fig1)

    def compare_yield(self):
        # Pie chart
        # Get data for desired years
        year2020_data = self.dp.loc[2020, :]
        year2021_data = self.dp.loc[2021, :]
        year2022_data = self.dp.loc[2022, :]

        # Create pie chart
        fig2, ax = plt.subplots(figsize=(3, 3))

        # Set values and labels for pie chart
        values = [year2020_data.sum(), year2021_data.sum(), year2022_data.sum()]
        labels = ['2020', '2021', '2022']

        # Set font color and size for pie chart labels
        text_props = {'color': 'white', 'fontsize': 10}

        # Set chart title, with font size and color adjustments
        font = {'color': 'white', 'size': 16}
        ax.set_title('Annual earnings', fontdict=font)

        # Create pie chart with labels and percentages, with font, color, and weight adjustments
        wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%', colors=self.colors,
                                          textprops=text_props)
        plt.setp(autotexts, size=10, color='white', weight="bold")

        # Set chart background to be transparent
        fig2.patch.set_alpha(0.0)

        # Display chart
        st.pyplot(fig2)

    # Add the map of total company revenue in other provinces
    def yield_nation_map_total(self):
        # Load data
        data = pd.read_excel('China_profit.xlsx')

        # Fill missing values with 0
        data.fillna(0, inplace=True)

        # Replace province names in Chinese with English equivalents
        data['address'] = data['address'].replace(self.province_cn2en)

        # Use pyecharts to create China map
        map_chart = (
            Map()
            .add("Profit by province in total", [list(z) for z in zip(data['address'], data['total_profit'])],
                 "china", pos_left=150)
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=max(data["total_profit"]),
                                                  min_=min(data["total_profit"]),
                                                  range_color=["#B0C4DE", "#4169E1", "#FA8072"],
                                                  # Set color text style
                                                  textstyle_opts=opts.TextStyleOpts(
                                                      color="white",
                                                      font_size=12,
                                                  )),
                legend_opts=opts.LegendOpts(is_show=True),
                toolbox_opts=opts.ToolboxOpts(pos_left="0%"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .render("map2.html")
        )

        # Set main and sub-titles for map
        st.markdown(f"<h3 style='text-align: center; color: white;'>Profit by province in total</h3>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: white;'>Source: Courtesy of the branch</p>",
                    unsafe_allow_html=True)

        # Display map and image on Streamlit
        st.components.v1.html(open("map2.html", "r", encoding="utf-8").read(), height=600)

    # Add map of company revenue by province for a given year
    def yield_nation_map_by_year(self):
        # Load data
        data = pd.read_excel('China_profit.xlsx')

        # Fill missing values with 0
        data.fillna(0, inplace=True)

        # Replace province names in Chinese with English equivalents
        data['address'] = data['address'].replace(self.province_cn2en)

        # Use pyecharts to create China map
        map_chart = (
            Map()
            .add(f"Profit by province in {self.year}",
                 [list(z) for z in zip(data['address'], data[f'{self.year}_profit'])], "china", pos_left=150)
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=max(data[f"{self.year}_profit"]),
                                                  min_=min(data[f"{self.year}_profit"]),
                                                  range_color=["#B0C4DE", "#4169E1", "#FA8072"],
                                                  # Set color text style
                                                  textstyle_opts=opts.TextStyleOpts(
                                                      color="white",
                                                      font_size=12,
                                                  )),
                legend_opts=opts.LegendOpts(is_show=True),
                toolbox_opts=opts.ToolboxOpts(pos_left="0%"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .render("map1.html")
        )

        # Set main and sub-titles for map
        st.markdown(f"<h3 style='text-align: center; color: white;'>Profit by province in {self.year}</h3>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: white;'>Source: Courtesy of the branch</p>",
                    unsafe_allow_html=True)

        # Display map and image on Streamlit
        st.components.v1.html(open("map1.html", "r", encoding="utf-8").read(), height=600)

    # Add Anhui Province Branch Total Revenue Map
    def yield_anhui_map_total(self):
        # Load data
        data = pd.read_excel('Anhui_profit.xlsx')

        # Fill missing values with 0
        data.fillna(0, inplace=True)

        # Replace city names in Chinese with English equivalents
        data['address'] = data['address'].replace(self.city_dict)

        # Use pyecharts to create Anhui map
        map_chart = (
            Map()
            .add("Profit by city in total", [list(z) for z in zip(data['address'], data['total_profit'])], "安徽",
                 pos_left=100)
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=max(data[f"total_profit"]),
                                                  min_=min(data[f"total_profit"]),
                                                  range_color=["#B0C4DE", "#4169E1"],
                                                  # Set color text style
                                                  textstyle_opts=opts.TextStyleOpts(
                                                      color="white",
                                                      font_size=12,
                                                  )),
                legend_opts=opts.LegendOpts(is_show=True),
                toolbox_opts=opts.ToolboxOpts(pos_left="0%"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .render("map4.html")
        )

        # Set main and sub-titles for map
        st.markdown(f"<h3 style='text-align: center; color: white;'>Profit by city in total</h3>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: white;'>Source: Courtesy of the branch</p>",
                    unsafe_allow_html=True)

        # Display map and image on Streamlit
        st.components.v1.html(open("map4.html", "r", encoding="utf-8").read(), height=600)

    # Add Anhui Province Branch Annual Revenue Map
    def yield_anhui_map_year(self):
        # Load data
        data = pd.read_excel('Anhui_profit.xlsx')

        # Fill missing values with 0
        data.fillna(0, inplace=True)

        # Replace city names in Chinese with English equivalents
        data['address'] = data['address'].replace(self.city_dict)

        # Use pyecharts to create Anhui map
        map_chart = (
            Map()
            .add(f"Profit by city in {self.year}",
                 [list(z) for z in zip(data['address'], data[f'{self.year}_profit'])], "安徽", pos_left=150)
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=max(data[f"{self.year}_profit"]),
                                                  min_=min(data[f"{self.year}_profit"]),
                                                  range_color=["#B0C4DE", "#4169E1"],
                                                  # Set color text style
                                                  textstyle_opts=opts.TextStyleOpts(
                                                      color="white",
                                                      font_size=12,
                                                  )),
                legend_opts=opts.LegendOpts(is_show=True),
                toolbox_opts=opts.ToolboxOpts(pos_left="0%"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .render("map3.html")
        )

        # Set main and sub-titles for map
        st.markdown(f"<h3 style='text-align: center; color: white;'>Profit by city in {self.year}</h3>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: white;'>Source: Courtesy of the branch</p>",
                    unsafe_allow_html=True)

        # Display map and image on Streamlit
        st.components.v1.html(open("map3.html", "r", encoding="utf-8").read(), height=600)
