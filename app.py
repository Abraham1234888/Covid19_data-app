
# Deployment: Run with 'streamlit run app.py' in your terminal
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   


# Load data
df = pd.read_csv('covid_metadata.csv', parse_dates=['publication_date'])

st.title("COVID-19 Data Explorer")

st.header("COVID-19 Data Metadata Preview")
st.write(df.head())

# Year range filter
year_range = st.slider("Select Publication Year Range", 2019, 2022, (2020, 2021))
filtered_df = df[(df['publication_date'].dt.year >= year_range[0]) & 
                 (df['publication_date'].dt.year <= year_range[1])]
st.write(f"Showing papers from {year_range[0]} to {year_range[1]}")
st.write(filtered_df)

# Visualizations
st.header("Visualizations")
# Example: Bar chart of papers by publication year
if 'publication_date' in df.columns:
    df['publication_year'] = df['publication_date'].dt.year
    year_counts = df['publication_year'].value_counts().sort_index()
    fig1, ax1 = plt.subplots(figsize=(10,6))
    sns.barplot(x=year_counts.index, y=year_counts.values, palette='viridis', ax=ax1)
    ax1.set_xlabel('Publication Year')
    ax1.set_ylabel('Number of Papers')
    ax1.set_title('Number of COVID-19 Papers by Publication Year')
    plt.xticks(rotation=45)
    st.pyplot(fig1)
# Example: Top journals publishing COVID-19 research
if 'journal' in df.columns:
    top_journals = df['journal'].value_counts().head(10)
    fig2, ax2 = plt.subplots(figsize=(10,6))
    sns.barplot(y=top_journals.index, x=top_journals.values, palette='magma', ax=ax2)
    ax2.set_xlabel('Number of Papers')
    ax2.set_ylabel('Journal')
    ax2.set_title('Top 10 Journals Publishing COVID-19 Research')
    st.pyplot(fig2)
# Example: Distribution of papers by source type
if 'source' in df.columns:
    source_counts = df['source'].value_counts()
    fig3, ax3 = plt.subplots(figsize=(10,6))
    sns.barplot(x=source_counts.index, y=source_counts.values, palette='Set2', ax=ax3)
    ax3.set_xlabel('Source Type')
    ax3.set_ylabel('Number of Papers')
    ax3.set_title('Distribution of COVID-19 Papers by Source Type')
    plt.xticks(rotation=45)
    st.pyplot(fig3)

st.sidebar.header("Filters")

# Create brief report on findings
st.header("Summary Report")
st.write("""
This dashboard provides an overview of COVID-19 related research papers. Key insights include:
- Trends in publication volume over time
- Leading journals publishing COVID-19 research
- Distribution of research by source type
""")


