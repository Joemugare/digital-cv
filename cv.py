import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import plotly.express as px
import pandas as pd
from streamlit_lottie import st_lottie
import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

matplotlib.use('Agg')  # Set Matplotlib backend to 'Agg' for Streamlit compatibility

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Portfolio", page_icon="📄", layout="wide")

# Define custom CSS styles for improved aesthetics
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .st-bm {
        background-color: #2a3e72;
        color: white;
    }
    .st-at {
        background-color: #f0f2f6;
        color: #2a3e72;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to load Lottie animation
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    # Header with Photo
    st.title("Joseph Mugare Portfolio")
    st.subheader("Data Analyst / Fullstack Developer")

    # Add Lottie animation from the provided URL
    animation_url = "https://lottie.host/e8dbe450-ca62-4516-8646-b646e8bef5a1/rTmqdL4mNv.json"
    animation_data = load_lottie_url(animation_url)
    if animation_data:
        st_lottie(animation_data, speed=1, height=300, key="lottie")

    # Contact Information
    st.header("Contact Information")
    st.markdown("📧 Email: joemugare@gmail.com")
    st.markdown("📞 Phone: +254720957180")
    st.markdown("🌐 LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/joseph-mugare/)")
    st.markdown("📂 GitHub: [GitHub Profile](https://github.com/joemugare)")
    st.markdown("📺 YouTube: [YouTube Channel](https://www.youtube.com/user/joemugare)")

    # Summary or Objective Section
    st.header("Summary")
    st.write("Experienced Data Analyst and Fullstack Developer with a passion for crafting innovative web applications. Proficient in Python, JavaScript, and adept in cloud computing technologies. Committed to delivering high-quality solutions that precisely align with business objectives.")

    # Education
    st.header("Education")
    st.markdown("**Bachelor In Information Technology, KCA University**")
    st.markdown("**January 2009 - December 2011**")

    # Additional Certifications
    st.header("Additional Certifications")
    st.markdown("1. CCNA, ZETECH")
    st.markdown("2. MySQL, EDX Stanford (Feb 2023 - July 2023)")
    st.markdown("3. Python Data Science, EDX Harvard (January 2023 - June 2023)")
    st.markdown("4. CS50's Introduction to Computer Science, Harvard University (March 2024)")
    st.markdown("5. MIT Computer Science and Programming Using Python, Massachusetts Institute of Technology (January 2024)")
    st.markdown("6. MIT Computational Thinking and Data Science, Massachusetts Institute of Technology (March 2024)")

    # Work Experience
    st.header("Work Experience")
    st.subheader("Data Analyst, Colgate-Palmolive, Nairobi")
    st.write("**January 2023 – Present**")
    st.write("- Conducted comprehensive data analysis to optimize supply chain operations, achieving a 12% reduction in operational costs.")
    st.write("- Designed and implemented interactive dashboards and automated reports for key stakeholders, enhancing decision-making efficiency.")
    st.write("- Developed ETL pipelines to streamline data extraction, transformation, and loading, reducing manual processing time by 30%.")
    st.write("- Collaborated with cross-functional teams to identify key performance indicators (KPIs) and establish data governance best practices.")

    st.subheader("Data Analyst, Biohazard Waste Solutions, Nairobi")
    st.write("**June 2020 – December 2022**")
    st.write("- Led a customer segmentation initiative that identified high-value customer segments, resulting in an 18% increase in customer retention.")
    st.write("- Created predictive models to anticipate service demand, enabling proactive resource allocation and cost optimization.")
    st.write("- Regularly presented detailed analytical reports to senior management, facilitating data-driven strategic decisions.")

    st.subheader("Network Administrator, Dimension Data, Nairobi")
    st.write("**July 2013 – December 2020**")
    st.write("- Ensured network integrity by implementing advanced cybersecurity protocols, mitigating risks of data breaches and unauthorized access.")

    st.subheader("NOC Support, Liquid Telecom, Nairobi")
    st.write("**February 2010 – April 2013**")
    st.write("- Monitored network performance using industry-standard tools such as SolarWinds, Nagios, and Wireshark.")
    st.write("- Diagnosed and resolved network issues promptly, minimizing downtime and ensuring service reliability.")
    st.write("- Documented network configurations and procedures, contributing to knowledge management and compliance.")

    # GitHub Contributions
    st.header("GitHub Contributions (Line Chart)")
    github_data = {
        "Year": [2019, 2020, 2021, 2022, 2023, 2024],
        "Contributions": [100, 350, 550, 600, 600, 800]
    }
    github_df = pd.DataFrame(github_data)
    fig_line = px.line(github_df, x="Year", y="Contributions", title="GitHub Contributions Over Time")
    st.plotly_chart(fig_line)

    # Skills
    st.header("Skills")
    animation_url1 = "https://lottie.host/81923711-4d08-4098-9c30-4df1491579ac/bDnigl2A7X.json"
    animation_data1 = load_lottie_url(animation_url1)
    if animation_data1:
        st_lottie(animation_data1, speed=1, height=300, key="lottie_animation_skills")

    st.write("- Programming Languages: Python, JavaScript")
    st.write("- Machine Learning: Scikit-learn, TensorFlow, Keras")
    st.write("- Cloud Computing: AWS")
    st.write("- Databases: MySQL, MongoDB")
    st.write("- Version Control: Git")

    # Projects
    st.header("Projects")
    animation_url2 = "https://lottie.host/c69a85a4-cc7e-472d-921b-851566ade1d4/EySROHiYry.json"
    animation_data2 = load_lottie_url(animation_url2)
    if animation_data2:
        st_lottie(animation_data2, speed=1, height=300, key="lottie_animation_projects")

    st.subheader("E-commerce Website")
    st.write("- Developed a full-stack e-commerce website using React and Node.js.")
    st.write("- Implemented payment processing, user authentication, and product recommendation system.")

    st.subheader("Portfolio Website")
    st.write("- Created a personal portfolio website using HTML, CSS, and JavaScript.")
    st.write("- Utilized responsive design principles for optimal viewing across devices.")
    st.write("- Implemented dynamic content loading and smooth transitions for improved user experience.")

    # Skills Proficiency Bar Chart
    st.header("Skills Proficiency")
    skills = ["Python", "JavaScript", "Data Analysis", "Machine Learning", "SQL", "HTML/CSS", "React.js", "Node.js"]
    proficiency = [90, 80, 85, 75, 90, 85, 80, 75]
    fig, ax = plt.subplots()
    ax.barh(skills, proficiency, color='skyblue')
    ax.set_xlabel('Proficiency (%)')
    ax.set_title('Skills Proficiency')
    st.pyplot(fig)

    # Downloadable PDF
    st.header("Downloadable PDF")
    def generate_pdf():
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 700, "Digital Resume")
        c.drawString(100, 680, "Joseph Mugare")
        c.drawString(100, 660, "Data Analyst / Fullstack Developer")
        c.showPage()
        c.save()
        buffer.seek(0)
        return buffer

    if st.button("Download PDF"):
        pdf_buffer = generate_pdf()
        st.download_button("Click here to download your resume", data=pdf_buffer, file_name="digital_resume.pdf", mime="application/pdf")

if __name__ == '__main__':
    main()
