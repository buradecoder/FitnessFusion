import streamlit as st

def app():

    
    st.subheader(":violet[Meet the Team]")

    About = [
        {"name": "Anshul Bura", "enroll_number": "03218002721", "course": "B.Tech Computer Science Engineering", "academic_year": "4th Year"},
    ]

    # Display team members
    for member in About:
        st.write(f"*Name:* {member['name']}")
        st.write(f"*Enrollment Number:* {member['enroll_number']}")
        st.write(f"*Course:* {member['course']}")
        st.write(f"*Academic Year:* {member['academic_year']}")
        st.write("---")