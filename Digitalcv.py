import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from streamlit_lottie import st_lottie
import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from pathlib import Path

# Function to load Lottie animation
def load_lottie_animation(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        return None

def main():
    # --- PAGE SETTINGS ---
    st.set_page_config(page_title="Joseph Mugare Portfolio", page_icon=":wave:", layout="wide")

    # Add Lottie animation from the provided URL
    animation_url = "https://lottie.host/e8dbe450-ca62-4516-8646-b646e8bef5a1/rTmqdL4mNv.json"
    animation_data = load_lottie_animation(animation_url)
    
    # --- Contact Info and Lottie on Same Line ---
    col1, col2 = st.columns([2, 1])  # You can adjust the relative sizes of the columns here

    with col1:
        st.header("Contact Information")
        st.markdown("📧 Email: joemugare@gmail.com")
        st.markdown("📞 Phone: +254720957180")
        st.markdown("🌐 LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/joseph-mugare/)")
        st.markdown("📂 GitHub: [GitHub Profile](https://github.com/joemugare)")
        st.markdown("📺 YouTube: [YouTube Channel](https://www.youtube.com/user/joemugare)")

    with col2:
        if animation_data:
            st_lottie(animation_data, speed=1, height=300, key="lottie")  # Adjust height as needed

    # --- PATH SETTINGS ---
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    resume_file = current_dir / "assets" / "CV.pdf"
    profile_pic_path = current_dir / "assets" / "profile-pic.png"

    # --- GENERAL SETTINGS ---
    PAGE_TITLE = "Digital CV | Joseph Mugare"
    NAME = "Joseph Mugare"
    DESCRIPTION = """
    Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
    """
    EMAIL = "joemugare@email.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/joseph-mugare/",
        "GitHub": "https://github.com/joemugare",
        "YouTube": "https://www.youtube.com/user/joemugare"
    }

    # Load CSS, PDF & Profile Pic
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic_path)

    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write(
        """
        - ✔️ 13 years of experience in data analysis, business intelligence, and full-stack development, driving data-driven decision-making across diverse industries.
        - ✔️ Strong hands-on experience in Python (Pandas, NumPy, Scikit-learn) for data analysis, modeling, and machine learning.
        - ✔️ Proficient in advanced Excel techniques, including Power Query, macros (VBA), and dashboards.
        - ✔️ Solid understanding of statistical analysis, hypothesis testing, and predictive analytics, with real-world application in solving complex business problems.
        - ✔️ Extensive experience in designing and implementing ETL pipelines to streamline data processing workflows.
        - ✔️ Excellent interpersonal skills, capable of leading cross-functional teams and delivering presentations to non-technical stakeholders.
        - ✔️ Proven track record in developing and deploying end-to-end data solutions using cloud platforms such as AWS and Azure.
        """
    )

    # --- SKILLS ---
    st.write('\n')
    st.subheader("Skills")
    st.write(
        """
        - 👩‍💻 **Programming:** Python (Scikit-learn, Pandas, NumPy, TensorFlow, Flask, Streamlit), JavaScript (Node.js, React.js), SQL, VBA  
        - 📊 **Data Visualization:** Power BI, Tableau, Matplotlib, Seaborn, Plotly, Excel Dashboards  
        - 🧠 **Machine Learning:** Regression models, Classification models, Clustering, Time Series Analysis, NLP (Natural Language Processing)  
        - 📚 **Modeling:** Logistic regression, Linear regression, Decision trees, Random forests, XGBoost, K-Means Clustering  
        - 🗄️ **Databases:** PostgreSQL, MongoDB, MySQL, SQLite, AWS RDS, Azure SQL  
        - ☁️ **Cloud Computing:** AWS (S3, Lambda, EC2, RDS), Azure (Data Factory, SQL Database), Google Cloud Platform (BigQuery)  
        - 🛠️ **Tools & Technologies:** Jupyter Notebooks, Anaconda, Git, Docker, Airflow  
        - 🔍 **Data Engineering:** ETL pipelines, Data wrangling, API integration, Web scraping (BeautifulSoup, Scrapy)  
        - 📝 **Documentation & Reporting:** PowerPoint, Confluence, JIRA, Notion, MS Word, Google Docs  
        """
    )

    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    st.subheader("Data Analyst, Colgate-Palmolive, Nairobi")
    st.write("**January 2023 – Present**")
    st.write("- Conducted comprehensive data analysis to optimize supply chain operations, achieving a 12% reduction in operational costs.")
    st.write("- Designed and implemented interactive dashboards and automated reports for key stakeholders, enhancing decision-making efficiency.")
    st.write("- Developed ETL pipelines to streamline data extraction, transformation, and loading, reducing manual processing time by 30%.")

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

    # --- PROJECTS ---
    st.write('\n')
    st.subheader("Projects")
    st.write("---")

    st.subheader("E-commerce Website")
    st.write("- Developed a full-stack e-commerce website using React and Node.js.")
    st.write("- Implemented payment processing, user authentication, and product recommendation system.")

    st.subheader("Portfolio Website")
    st.write("- Created a personal portfolio website using HTML, CSS, and JavaScript.")
    st.write("- Utilized responsive design principles for optimal viewing across devices.")
    st.write("- Implemented dynamic content loading and smooth transitions for improved user experience.")

    # --- FOOTER ---
    st.write("---")
    st.write("© 2025 Joseph Mugare | All rights reserved.")

if __name__ == "__main__":
    main()
