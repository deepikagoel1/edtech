#import the libraries that are required
import streamlit as st
import datetime
import pandas as pd
import pickle
import numpy as np
from PIL import Image
import streamlit_theme as stt

#---------------------------------Page title------------------------------------------

st.set_page_config(page_title="Result Status Prediction Using Random Forest Classifier Model")

rf = pickle.load(open("random_forest.pickle", "rb"))

course = st.selectbox("Course", ("Artificial Intelligence", "Data Science", "Digital Marketing", "Embedded Systems", "Life Science", "Python", "Statistics"))

course_level = st.selectbox("Course Level", ("Beginner", "Intermediate", "Advanced"))

age_band = st.selectbox("Age Band Selection", ("0-35", "35-55", "55<="))

qual = st.selectorbox("User Qualification", ("Graduate", "Post Graduate"))

queries = st.selectorbox("Querries", ("Artificial Intelligence", "Botany", "Data Science", "Digital Marketing", "Ecology", "Electronics and Communication", "Genetics", "IOT","Machine learning", "Micro-Biology", "Microcontroller", "Microprocessor", "Probability", "Python", "Robotics", "Statistics", "VLSI", "Zoology"))

user_pr = st.selectorbox("User Profile", ("Professional", "Student"))

region = st.selectorbox("Region", (" Oxfordshire", "Norfolk", "Cheshire", "Buckingham", "London", "Surrey", "Hampshire", "Scotland", "Yorkshire Region", "Leicester", "Ireland", "Singapore", "Wales"))

mod = st.selectorbox("Module Used by User in Days", ("234", "240", "241", "261", "262", "268", "269"))


def run():
    pred_final_res = []

    if st.button("Check"):
        for j in range(6):
            
            