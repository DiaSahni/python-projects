# data.py
import pandas as pd

def load_courses():
    # Code to load course data from a CSV file, database, or API
    data = pd.read_csv("courses.csv")
    return data

# ui.py
import streamlit as st
from data import load_courses
from logic import (  # Optional: import logic functions if applicable
    get_course_details,
    process_quiz_answer,
    # ...
)

def display_sidebar():
    # Define navigation options in the sidebar
    st.sidebar.title("MedMastery Navigation")
    selected_page = st.sidebar.selectbox("Select a Page", ["Courses", "Assessments", "Forum"])
    return selected_page

def display_courses(courses):
    # Show courses with filtering and expanders
    categories = list(set(courses["category"]))
    selected_category = st.selectbox("Filter by Category", categories + ["All"])
    filtered_courses = courses if selected_category == "All" else courses[courses["category"] == selected_category]

    for category in set(filtered_courses["category"]):
        with st.expander(category):
            for course in filtered_courses[filtered_courses["category"] == category].itertuples():
                st.write(f"{course.title} ({course.difficulty})")
                if st.button(f"View Details"):
                    display_course_details(course.Index)  # Pass course ID

def display_course_details(course_id):
    # Fetch detailed information about a specific course
    course_details = get_course_details(course_id)
    st.subheader(course_details["title"])
    st.write(course_details["description"])
    # ... (display additional details)

# app.py
import streamlit as st

# Load data
courses = load_courses()

# Display UI elements
selected_page = display_sidebar()

if selected_page == "Courses":
    display_courses(courses.copy())  # Avoid modifying original DataFrame
elif selected_page == "Assessments":
    # Implement quiz or survey logic
elif selected_page == "Forum":
    # Display forum functionality (optional)
