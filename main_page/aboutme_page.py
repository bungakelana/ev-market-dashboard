import streamlit as st

def show():

    # ================= CSS =================
    st.markdown("""
    <style>
    .stApp{
        background: linear-gradient(to right, #0f172a, #1e293b);
        color: white;
    }
    .card { 
        background: rgba(255,255,255,0.25); 
        backdrop-filter: blur(12px); 
        -webkit-backdrop-filter: blur(12px); 
        border: 1px solid rgba(255,255,255,0.3); 
        border-radius: 24px; 
        padding: 28px; m
        argin-bottom: 25px; }
        
        /* LABEL */ label { 
        font-size: 18px !important; 
        font-weight: 600 !important; 
        color: #06212E !important; }
        
        /* HERO CARD */ 
        .hero-card{ 
        background: rgba(255,255,255,0.06); 
        padding: 35px; 
        border-radius: 25px; 
        backdrop-filter: blur(10px); 
        border: 1px solid rgba(255,255,255,0.1); 
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        
        /* TITLE */ 
        .big-name{ font-size: 48px; 
        font-weight: 800; 
        color: white; 
        margin-bottom: 5px; }
        
        /* SUBTITLE */ 
        .job-title{ font-size: 20px; 
        color: #cbd5e1; 
        margin-bottom: 20px; }
        
        /* ABOUT */ 
        .about{ font-size: 16px;
        color: #e2e8f0;
        line-height: 1.8; }
        
        .skill-card:hover{
        transform: translateY(-10px) scale(1.02);
        transition: 0.4s ease;
        box-shadow: 0 10px 35px rgba(59,130,246,0.4);}
        
        .big-name{
        font-size: 56px;
        font-weight: 800;
        background: linear-gradient(90deg,#38bdf8,#818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;}
    
    </style>
    """, unsafe_allow_html=True)

    # ================= CONTACT =================
    def show_contact():
        st.success("📧 Email: rebungakelana@gmail.com")
        st.success("💼 LinkedIn: linkedin.com/in/refitri-bunga-kelana")

    # ================= HERO =================
    st.markdown("<br>", unsafe_allow_html=True)
   
    
    col1, col2 = st.columns([1,2], gap="large")
    with col1:
        st.image("./picture/1_back_car.jpeg", width=320)

    with col2:
        st.markdown("""
        <div class="hero-card">
        <div class="big-name">
        Refitri Bunga Kelana
        </div>

        <div class="job-title">
        Data Scientist
        </div>

        <div class="about">
        Data Analyst specializing in business intelligence, machine learning, and RAG. 
        Experienced in developing predictive models, and data-driven solutions to optimize performance and support strategic growth.
        </div>

        </div>
    
        """, unsafe_allow_html=True)
        
    # ================= CONTACT =================
    st.markdown("<br>", unsafe_allow_html=True)
    
    
    st.markdown("## Contact")
    show_contact()
    
    st.markdown("""<style>
    /* CONTACT LINKS */
    .stAlert a {
        color: #38bdf8 !important;
        font-weight: 600 !important;
        text-decoration: none !important;
    }
    .stAlert a:hover {
        text-decoration: underline !important;
    }
        /* LABEL */ label {
    color: white !important;
    font-weight: 600 !important;}
    
        /* INPUT TEXT */
        input {
            background: rgba(255,255,255,0.1) !important;
            color: white !important;
            font-size: 18px !important;
            font-weight: 600 !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            padding: 12px 18px !important;
        }
        /* PLACEHOLDER */
        input::placeholder {
            color: rgba(255,255,255,0.7) !important;
            -webkit-text-fill-color: rgba(255,255,255,0.7)
        } !important;
        }</style>    
    """, unsafe_allow_html=True)
    
    # ================= EXPERIENCE =================
    st.markdown("""
    <div class="section-title">💼 Experience</div>
    """, unsafe_allow_html=True)

    exp1, exp2 = st.columns([1,1], gap="large")

    with exp1:
        st.markdown("""
        <div class="skill-card">
        <h4>🚗 Customer Relation Officer</h4>
        <p><b>Astra Daihatsu</b> | 2026 - Present</p>

        <hr>

        <h4>📊 Data Analyst Freelance</h4>
        <p><b>Astra Daihatsu</b> | 2026 - Present</p>
        </div>
        """, unsafe_allow_html=True)

    with exp2:
        st.markdown("""
        <div class="skill-card">
        <h4>🏢 Head Retail</h4>
        <p><b>PT. Setia Kawan Kramika</b> | 2019 - 2025</p>

        <hr>

        <h4>💳 Credit Analyst Intern</h4>
        <p><b>Bank Riau Kepri</b> | 2016 - 2017</p>
        </div>
        """, unsafe_allow_html=True)

    # ================= EDUCATION =================
    st.markdown("""
    <div class="section-title">🎓 Education</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="skill-card">
    <h4>🎓 Bachelor's in Computer Science</h4>
    <p>Muhammadiyah University of Riau</p>
    </div>
    """, unsafe_allow_html=True)

    # ================= SKILLS =================
    st.markdown("""
    <div class="section-title">⚡ Skills</div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="skill-card">
        <h3>🐍 Programming</h3>

        Python <br>
        SQL <br>
        LLMs (ChatGPT) <br>
        RAG
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="skill-card">
        <h3>🤖 Machine Learning</h3>

        XGBoost <br>
        Random Forest <br>
        NLP <br>
        Forecasting
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="skill-card">
        <h3>📊 Visualization</h3>

        Plotly <br>
        Power BI <br>
        Seaborn <br>
        Looker Studio
        </div>
        """, unsafe_allow_html=True)

    # ================= PROJECTS =================
    st.markdown("""
    <div class="section-title">🚀 Projects</div>
    """, unsafe_allow_html=True)

    project1, project2 = st.columns(2)

    with project1:
        st.markdown("""
        <div class="skill-card">
        <h4>🚗 EV Customer Satisfaction Prediction</h4>

        Built an XGBoost model to predict customer satisfaction
        based on EV specifications.
        </div>
        """, unsafe_allow_html=True)

    with project2:
        st.markdown("""
        <div class="skill-card">
        <h4>📈 Sales Analysis Dashboard</h4>

        Developed an interactive dashboard using Streamlit
        to visualize KPIs and sales trends.
        </div>
        """, unsafe_allow_html=True)