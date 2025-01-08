import streamlit as st
    from data_analysis import load_data, analyze_data
    from visualization import plot_data

    def main():
        st.title("Data Analysis Application")
        uploaded_file = st.file_uploader("Upload CSV File", type="csv")
        
        if uploaded_file is not None:
            df = load_data(uploaded_file)
            st.write("Loaded Data:")
            st.write(df.head())
            
            if st.button("Analyze Data"):
                analysis_results = analyze_data(df)
                st.write(analysis_results)
            
            if st.button("Generate Visualizations"):
                plot_data(df)

    if __name__ == "__main__":
        main()
