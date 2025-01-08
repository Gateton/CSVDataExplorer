import pandas as pd

    def load_data(file):
        try:
            df = pd.read_csv(file)
            return df
        except Exception as e:
            raise ValueError("Error loading CSV file: " + str(e))

    def analyze_data(df):
        analysis = {
            "First Rows": df.head(),
            "Last Rows": df.tail(),
            "Descriptive Statistics": df.describe(),
            "Unique Values": {col: df[col].nunique() for col in df.select_dtypes(include='object').columns}
        }
        return analysis
