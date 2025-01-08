import matplotlib.pyplot as plt
    import seaborn as sns
    import streamlit as st

    def plot_data(df):
        st.write("Bar Chart:")
        st.bar_chart(df.select_dtypes(include='number').iloc[:, 0])

        st.write("Histogram:")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df.select_dtypes(include='number').iloc[:, 0], bins=20, color='skyblue', edgecolor='black')
        ax.set_title('Histogram')
        ax.set_xlabel('Values')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

        st.write("Scatter Plot:")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1], ax=ax)
        st.pyplot(fig)

        st.write("Line Chart:")
        st.line_chart(df.select_dtypes(include='number'))
