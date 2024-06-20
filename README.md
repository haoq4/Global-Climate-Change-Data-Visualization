# Global Climate Change Data Visualization

This application provides a comprehensive visualization of global climate change data. The goal is to make climate change trends accessible and understandable to a non-technical audience by offering interactive visualizations of global temperature changes and precipitation patterns.

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Source](#data-source)

## Background

Climate change is a critical issue affecting the entire globe. Understanding local weather patterns is essential for various stakeholders, including policymakers, researchers, and the general public. This application leverages weather data collected by NOAA to provide insights into local climate trends.

## Features

- **Monthly Average Wind Speed:** A line chart showing the average wind speed for each month.
- **Monthly Distribution of Precipitation Days:** A bar chart showing the number of days with significant rainfall.
- **Temperature Distribution Heatmap:** A heatmap showing the average maximum and minimum temperatures for each month.
- **Interactive Selection:** Users can select different locations and years to view the respective visualizations.

## Installation

To install and run this project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/haoq4/Global-Climate-Change-Data-Visualization.git
   cd Global-Climate-Change-Data-Visualization

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate (cmd) .\venv\Scripts\Activate (PowerShell)

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt

## Usage

To run the application locally, use the following command:
   ```sh
   streamlit run app.py
   ```

Open your web browser and go to http://localhost:8501 to view the application.

## Data Source
The data used in this application is sourced from the National Oceanic and Atmospheric Administration (NOAA).