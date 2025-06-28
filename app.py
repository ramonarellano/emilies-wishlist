import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(
    page_title="My Python App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("🚀 My Python Streamlit App")
st.write("Welcome to your new Streamlit application!")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Data Analysis", "Interactive Chart", "About"])

if page == "Home":
    st.header("Home Page")
    st.write("This is a sample Streamlit application with multiple features.")
    
    # Add some interactive widgets
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Interactive Widgets")
        name = st.text_input("What's your name?")
        age = st.slider("How old are you?", 0, 100, 25)
        favorite_color = st.selectbox("What's your favorite color?", 
                                    ["Red", "Blue", "Green", "Yellow", "Purple"])
        
        if st.button("Submit"):
            st.success(f"Hello {name}! You are {age} years old and your favorite color is {favorite_color}.")
    
    with col2:
        st.subheader("Quick Stats")
        # Generate some sample data
        data = np.random.randn(100)
        st.write(f"Sample mean: {np.mean(data):.2f}")
        st.write(f"Sample std: {np.std(data):.2f}")
        st.line_chart(data)

elif page == "Data Analysis":
    st.header("📊 Data Analysis")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        
        # Display data
        st.subheader("Data Preview")
        st.dataframe(df.head())
        
        st.subheader("Data Summary")
        st.write(df.describe())
        
        # Column selection for analysis
        if len(df.select_dtypes(include=[np.number]).columns) > 0:
            numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
            selected_column = st.selectbox("Select a column for visualization", numeric_columns)
            
            # Plot histogram
            fig, ax = plt.subplots()
            ax.hist(df[selected_column].dropna(), bins=20, edgecolor='black')
            ax.set_title(f'Distribution of {selected_column}')
            ax.set_xlabel(selected_column)
            ax.set_ylabel('Frequency')
            st.pyplot(fig)
    else:
        st.info("Please upload a CSV file to begin analysis.")
        
        # Show sample data
        st.subheader("Sample Data")
        sample_data = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
            'Age': [25, 30, 35, 28],
            'Score': [85, 92, 78, 96],
            'City': ['New York', 'London', 'Tokyo', 'Paris']
        })
        st.dataframe(sample_data)

elif page == "Interactive Chart":
    st.header("📈 Interactive Chart")
    
    # Generate sample data
    chart_type = st.selectbox("Select chart type", ["Line Chart", "Bar Chart", "Scatter Plot"])
    
    # Parameters
    num_points = st.slider("Number of data points", 10, 200, 50)
    
    # Generate data
    x = np.linspace(0, 10, num_points)
    y = np.sin(x) + np.random.normal(0, 0.1, num_points)
    
    df_chart = pd.DataFrame({'x': x, 'y': y})
    
    if chart_type == "Line Chart":
        st.line_chart(df_chart.set_index('x'))
    elif chart_type == "Bar Chart":
        # Create bins for bar chart
        bins = np.linspace(x.min(), x.max(), 20)
        hist, _ = np.histogram(y, bins=bins)
        df_bar = pd.DataFrame({'bins': bins[:-1], 'count': hist})
        st.bar_chart(df_bar.set_index('bins'))
    else:  # Scatter Plot
        st.scatter_chart(df_chart.set_index('x'))

else:  # About page
    st.header("ℹ️ About")
    st.write("""
    ## About This App
    
    This is a sample Streamlit application that demonstrates various features:
    
    - **Interactive widgets**: Text input, sliders, selectboxes, buttons
    - **Data visualization**: Charts and plots using matplotlib and built-in Streamlit charts
    - **File handling**: CSV file upload and analysis
    - **Multi-page navigation**: Using sidebar for page selection
    - **Layout**: Columns and responsive design
    
    ### Technologies Used
    - Python 3.x
    - Streamlit
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    
    ### Getting Started
    To run this app locally:
    ```bash
    pip install streamlit pandas numpy matplotlib seaborn
    streamlit run app.py
    ```
    """)
    
    st.subheader("Contact")
    st.write("Built with ❤️ using Streamlit")
