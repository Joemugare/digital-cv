import streamlit as st

def main():
    # Page Configuration
    st.set_page_config(page_title="Digital Resume", page_icon="📄")

    # Header with Photo
    st.image("C:/Users/Qunta/Desktop/PYTHON CODES/Streamlit Projects/CV/images/profile-pic.png", use_column_width=True)
    st.title("John Doe's Digital Resume")
    st.subheader("Software Engineer")

    # Contact Information
    st.write("📧 Email: john@example.com")
    st.write("📞 Phone: +123-456-7890")
    st.write("🌐 LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/johndoe/)")
    st.write("📁 GitHub: [GitHub Profile](https://github.com/johndoe)")

    # Education
    st.header("Education")
    st.subheader("Bachelor of Science in Computer Science")
    st.write("University of Computer Science")
    st.write("Graduated: May 2020")

    # Work Experience
    st.header("Work Experience")
    st.subheader("Software Engineer at ABC Tech")
    st.write("Jan 2023 - Present")
    st.write("Developed and maintained web applications.")
    st.write("Collaborated with cross-functional teams to deliver projects.")

    # Skills
    st.header("Skills")
    st.write("Programming Languages: Python, JavaScript")
    st.write("Web Development: HTML, CSS, React")
    st.write("Databases: MySQL, MongoDB")
    st.write("Version Control: Git")

    # Projects
    st.header("Projects")
    st.subheader("E-commerce Website")
    st.write("Developed a full-stack e-commerce website using React and Node.js.")
    st.subheader("Portfolio Website")
    st.write("Created a personal portfolio website using HTML, CSS, and JavaScript")

if __name__ == '__main__':
    main()
