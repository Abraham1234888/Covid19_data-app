import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   


#load data

df = pd.read_csv('metadata.csv', parse_dates=['publication_date'])

st.title("COVID-19 Data Explorer")

st.header("COVID-19 Data Metadata Preview")
st.write(metadata_df.head())

#year range filter
year_range = st.slider("Select Publication Year Range", 2019, 2022, (2020, 2021))
filtered_df = metadata_df[(metadata_df['publication_date'].dt.year >= year_range[0]) & 
                          (metadata_df['publication_date'].dt.year <= year_range[1])]
st.write(f"Showing papers from {year_range[0]} to {year_range[1]}")
st.write(filtered_df)
#visualizations
st.header("Visualizations")
# Example: Bar chart of papers by publication year
if 'publication_year' in metadata_df.columns:
    year_counts = metadata_df['publication_year'].value_counts().sort_index()
    plt.figure(figsize=(10,6))
    sns.barplot(x=year_counts.index, y=year_counts.values, palette='viridis')
    plt.xlabel('Publication Year')
    plt.ylabel('Number of Papers')
    plt.title('Number of COVID-19 Papers by Publication Year')
    plt.xticks(rotation=45)
    st.pyplot(plt)
# Example: Top journals publishing COVID-19 research
if 'journal' in metadata_df.columns:
    top_journals = metadata_df['journal'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(y=top_journals.index, x=top_journals.values, palette='magma')
    plt.xlabel('Number of Papers')
    plt.ylabel('Journal')
    plt.title('Top 10 Journals Publishing COVID-19 Research')
    st.pyplot(plt)

    # Example: Distribution of papers by source type
if 'source' in metadata_df.columns:
    source_counts = metadata_df['source'].value_counts()
    plt.figure(figsize=(10,6))
    sns.barplot(x=source_counts.index, y=source_counts.values, palette='Set2')
    plt.xlabel('Source Type')
    plt.ylabel('Number of Papers')
    plt.title('Distribution of COVID-19 Papers by Source Type')
    plt.xticks(rotation=45)
    st.pyplot(plt)

st.sidebar.header("Filters")

#create brief report on findings
st.header("Summary Report")
st.write("""
This dashboard provides an overview of COVID-19 related research papers. Key insights include:
- Trends in publication volume over time
- Leading journals publishing COVID-19 research
- Distribution of research by source type
""")


