# Python Streamlit App

A multi-page Streamlit application with interactive features, data analysis capabilities, and visualization tools.

## Features

- **Home Page**: Interactive widgets and basic statistics
- **Data Analysis**: CSV file upload and analysis with visualizations
- **Interactive Charts**: Dynamic chart generation with customizable parameters
- **About Page**: Information about the app and technologies used

## Technologies Used

- Python 3.x
- Streamlit - Web app framework
- Pandas - Data manipulation and analysis
- NumPy - Numerical computing
- Matplotlib - Plotting library
- Seaborn - Statistical data visualization

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To start the Streamlit application:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## App Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Usage

1. **Home Page**: 
   - Enter your name and select preferences
   - View real-time generated statistics and charts

2. **Data Analysis**: 
   - Upload your own CSV file for analysis
   - View data preview and statistical summary
   - Generate histograms for numeric columns

3. **Interactive Charts**: 
   - Choose from different chart types
   - Adjust the number of data points
   - View dynamically generated visualizations

## Customization

You can easily extend this app by:
- Adding new pages to the sidebar navigation
- Implementing additional chart types
- Adding more data analysis features
- Integrating with external APIs
- Adding user authentication

## Contributing

Feel free to fork this project and submit pull requests for any improvements!
