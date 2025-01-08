This project is a Python-based application designed to allow users to upload CSV files, perform basic data analysis, and generate graphical visualizations. The application is user-friendly and provides clear and understandable results.

## Features

- **CSV File Upload**: Users can upload CSV files from their local system. The application validates the file format and handles errors if the file is not a CSV.
- **Data Analysis**: Utilizes the Pandas library to perform data analysis, including:
  - Viewing the first and last rows of the dataset.
  - Displaying descriptive statistics (mean, median, mode, standard deviation, etc.) for each numeric column.
  - Counting unique values in categorical columns.
  - Allowing users to filter data based on specific criteria (e.g., filtering by a specific column or range of values).
- **Data Visualization**: Uses Matplotlib and Seaborn to create graphical visualizations, including:
  - Bar charts for comparing categories.
  - Histograms to show the distribution of numeric data.
  - Scatter plots to explore relationships between two variables.
  - Line charts to show trends over time (if applicable).
- **User Interface**: Built with Streamlit to provide an intuitive interface for users to interact with the application. Includes buttons to load files, perform analysis, and generate visualizations. Displays analysis results and visualizations within the application window.

## Technologies Used

- **Python 3.x**
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static, interactive, and animated visualizations.
- **Seaborn**: For making statistical graphics.
- **Streamlit**: For building the user interface.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application with the following command:
   ```bash
   streamlit run main.py
   ```
2. Follow the instructions in the interface to upload a CSV file, perform data analysis, and generate visualizations.

## Examples

You can use any properly formatted CSV file to test the application. The application will guide you through the process of analyzing and visualizing your data.

## Future Enhancements (Optional)

- Allow users to save generated visualizations as images (e.g., PNG or JPEG).
- Implement the option to export analysis results to a new CSV file.
- Add a help system or tutorial within the application to guide users in using the features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
