import streamlit as st
import pandas as pd
import plotly.express as px

def app():

    # Load data from the uploaded CSV file
    file_path = '/mnt/data/campaign_data.csv'
    data = pd.read_csv(file_path)

    # Display the data table in Streamlit
    st.title('Campaign Data Visualization')
    st.write('### Data Overview')
    st.write(data)

    # Select columns for visualization
    st.write('### Select Data for Visualization')
    columns = data.columns
    x_axis = st.selectbox('Select X-axis column', columns)
    y_axis = st.selectbox('Select Y-axis column', columns)

    # Line chart
    st.write('### Line Chart')
    line_fig = px.line(data, x=x_axis, y=y_axis, title=f'Line Chart of {y_axis} vs {x_axis}')
    st.plotly_chart(line_fig)

    # Bar chart
    st.write('### Bar Chart')
    bar_fig = px.bar(data, x=x_axis, y=y_axis, title=f'Bar Chart of {y_axis} vs {x_axis}')
    st.plotly_chart(bar_fig)

    # Scatter plot
    st.write('### Scatter Plot')
    scatter_fig = px.scatter(data, x=x_axis, y=y_axis, title=f'Scatter Plot of {y_axis} vs {x_axis}')
    st.plotly_chart(scatter_fig)

    # Histogram
    st.write('### Histogram')
    hist_column = st.selectbox('Select column for Histogram', columns)
    hist_fig = px.histogram(data, x=hist_column, title=f'Histogram of {hist_column}')
    st.plotly_chart(hist_fig)

    # Pie Chart (if categorical data is available)
    st.write('### Pie Chart')
    pie_column = st.selectbox('Select column for Pie Chart', columns)
    pie_fig = px.pie(data, names=pie_column, title=f'Pie Chart of {pie_column}')
    st.plotly_chart(pie_fig)

    # Display summary statistics
    st.write('### Summary Statistics')
    st.write(data.describe())

if __name__ == "__main__":
    app()
