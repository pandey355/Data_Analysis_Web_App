# import required libraries
import streamlit as st
import pandas as pd
import seaborn as sns



# adding title and subheader
st.title("Data Analysis")
st.subheader("Analysing Data using Python & Streamlit")

# upload dataset

upload = st.file_uploader("Upload Your file in CSV format")
if upload is not None:
    data = pd.read_csv(upload)

# check the Head and Tail data
if upload is not None:
    if st.checkbox("Explore Dataset"):
        if st.button("Head Data"):
            st.write(data.head())
        if st.button("Tail Data"):
            st.write(data.tail())

# check the DataType of each column

if upload is not None:
    if st.checkbox("Datatype of each data columns"):
        if st.button("DataType Of Each Column"):
            st.write(data.dtypes)

# check the Shape of Dataset no of rows and columns

if upload is not None:
    data_shape = st.radio(
        "What Dimention your want to check?", ('Rows', 'Columns'))
    if data_shape == "Rows":
        st.text("number of rows")
        st.write(data.shape[0])
    elif data_shape == "Columns":
        st.text("number of rows")
        st.write(data.shape[1])

# check the null values in a data set

if upload is not None:
    test=data.isnull().values.any()
    if test:
        if st.checkbox("Null values in Dataset"): 
            st.write(data.isnull().sum())
            sns.heatmap(data.isnull())
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
           
    else:
        st.success("congratulation|| Dataset doesn't contains any null values")


# check duplicate values and remove the null values in a dataset
              
if upload is not None:
    test=data.duplicated().values.any()
    if test==True:
        st.warning("This Dataset contain's some duplicate values")
        dup=st.selectbox("Do you want to remove duplicate values",("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.success("Congratulation||")
            st.text("Duplicate values are removed")
            st.write(data)
        if dup=="No":
            st.warning("Duplicate values may reduce your model accuracy")
            st.write(data)
    
            
# get overall statics about dataset

if upload is not None:
    if st.checkbox("Statical View Of Dataset"):
            st.text("Summary of Data")
            k=data.describe(include="all")
            st.write(k)


# about section
if st.button("About App"):
    st.text("This app is Build with the help of Pandas , Seaborn , Streamlit")
    st.text("Thank's to Steamlit")
if st.checkbox("Developed By"):
    st.text("Akash Pandey")
