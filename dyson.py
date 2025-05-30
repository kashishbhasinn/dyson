import streamlit as st

# Dyson color palette and styling
st.set_page_config(
    page_title="Kashish Bhasin - Resume",
    page_icon="⚙️",
    layout="wide"
)

# Custom CSS with Dyson colors
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #003d82 0%, #0052cc 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .section-header {
        background: linear-gradient(90deg, #ff6b35 0%, #ff8c42 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1.5rem 0 1rem 0;
        font-weight: bold;
    }
    .experience-card {
        background: #f8f9fa;
        border-left: 4px solid #003d82;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .project-card {
        background: #fff5f2;
        border-left: 4px solid #ff6b35;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .skill-tag {
        background: #e3f2fd;
        color: #003d82;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: 500;
    }
    .achievement-item {
        background: #fff8e1;
        border-left: 3px solid #ff8c42;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 5px 5px 0;
    }
    .contact-info {
        background: #f0f4ff;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .metric-highlight {
        color: #003d82;
        font-weight: bold;
    }
    .sidebar-card {
        background: #f8f9fa;
        border: 2px solid #003d82;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .sidebar-metric {
        background: linear-gradient(45deg, #003d82, #0052cc);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .quick-fact {
        background: #fff5f2;
        border-left: 3px solid #ff6b35;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 0 5px 5px 0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="main-header">
    <h1>KASHISH BHASIN</h1>
    <p style="font-size: 1.2rem; margin-top: 1rem;">Product Strategist & AI/ML Engineer</p>
</div>
""", unsafe_allow_html=True)

# Contact Information
st.markdown("""
<div class="contact-info">
    <p><strong>📧</strong> kashishbhasinn@gmail.com | <strong>📱</strong> (+91) 9811149303</p>
    <p><strong>💼</strong> linkedin.com/in/kashish-bhasin | <strong>💻</strong> github.com/kashishbhasinn</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #003d82, #0052cc); color: white; border-radius: 10px; margin-bottom: 2rem;">
        <h2>📊 Quick Stats</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    st.markdown("""
    <div class="sidebar-metric">
        <h3>9.29</h3>
        <p>CGPA</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sidebar-metric">
        <h3>6+</h3>
        <p>Internships</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sidebar-metric">
        <h3>10+</h3>
        <p>Tech Projects</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Why Dyson Section
    st.markdown("""
    <div class="sidebar-card">
        <h4 style="color: #003d82; text-align: center;">🎯 Why Dyson?</h4>
        <div class="quick-fact">
            <strong>Innovation Focus:</strong> Passionate about solving real-world consumer problems
        </div>
        <div class="quick-fact">
            <strong>Tech + Business:</strong> Perfect blend of AI/ML expertise and market research skills
        </div>
        <div class="quick-fact">
            <strong>Proven Results:</strong> 65% sales growth impact at Dr. Oetker
        </div>
        <div class="quick-fact">
            <strong>Team Leadership:</strong> Led 10+ cross-functional specialists
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Facts
    st.markdown("""
    <div class="sidebar-card">
        <h4 style="color: #003d82; text-align: center;">⚡ Quick Facts</h4>
        <div class="quick-fact">
            🎓 Top 2,000 AWS AI/ML scholarship recipients worldwide
        </div>
        <div class="quick-fact">
            🌍 International exposure through PASCH program (50/100+ nations)
        </div>
        <div class="quick-fact">
            💼 PwC Data Analytics certified (92% average score)
        </div>
        <div class="quick-fact">
            🏆 Treasurer role: 200+ attendee growth achieved
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills Summary
    st.markdown("""
    <div class="sidebar-card">
        <h4 style="color: #003d82; text-align: center;">🛠️ Core Skills</h4>
        <div class="quick-fact">
            <strong>Product:</strong> Roadmapping, PRDs, User Research
        </div>
        <div class="quick-fact">
            <strong>Marketing:</strong> Google Analytics, Meta Ads, A/B Testing
        </div>
        <div class="quick-fact">
            <strong>Tech:</strong> Python, AI/ML, Data Analysis
        </div>
        <div class="quick-fact">
            <strong>Business:</strong> Market Analysis, Strategy, KPI Tracking
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Download Section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h4 style="color: #003d82;">📄 Resume Actions</h4>
        <p style="font-size: 0.9rem; color: #666;">
            Contact me for the latest PDF version or connect on LinkedIn!
        </p>
    </div>
    """, unsafe_allow_html=True)

# Summary Section
st.markdown('<div class="section-header"><h2>PROFESSIONAL SUMMARY</h2></div>', unsafe_allow_html=True)
st.markdown("""
Product strategist and Computer Science undergrad passionate about leveraging technology to solve real-world consumer problems. 
Experienced in market research, customer behavior analysis, and leading cross-functional product teams to deliver innovative solutions. 
Combines deep technical expertise in AI/ML with business strategy skills to drive product growth, optimize market positioning, 
and deliver data-backed insights that support strategic objectives.
""")

# Education Section
st.markdown('<div class="section-header"><h2>EDUCATION</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("**Manipal University Jaipur**")
    st.markdown("BTech in Computer Science Engineering - Artificial Intelligence and Machine Learning")
with col2:
    st.markdown("**CGPA: 9.29**")

st.markdown("**Lotus Valley International School, Noida**")
st.markdown("Class 12: 93.8% | Class 10: 94.6%")

# Skills Section
st.markdown('<div class="section-header"><h2>SKILLS</h2></div>', unsafe_allow_html=True)

# Product & Business Skills
st.markdown("**Product & Business:**")
product_skills = ["Product Roadmapping", "Agile Scrum", "Jira", "Notion", "Feature Prioritization", 
                 "Competitive Analysis", "User Research", "KPI Tracking", "Market Segmentation", "Business Model Analysis"]
skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in product_skills])
st.markdown(skills_html, unsafe_allow_html=True)

# Marketing & Business Skills
st.markdown("**Marketing & Business Skills:**")
marketing_skills = ["Google Analytics", "Meta Ads Manager", "Social Media Strategy", "Brand Positioning", 
                   "Customer Journey Mapping", "SWOT Analysis", "Survey Design", "Sentiment Analysis", "A/B Testing"]
marketing_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in marketing_skills])
st.markdown(marketing_html, unsafe_allow_html=True)

# Technical Skills
st.markdown("**Technical:**")
tech_skills = ["Python", "NumPy", "Pandas", "Scikit-learn", "SQL", "Tableau", "Excel", 
              "LangChain", "HuggingFace", "Selenium", "BeautifulSoup"]
tech_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in tech_skills])
st.markdown(tech_html, unsafe_allow_html=True)

# Experience Section
st.markdown('<div class="section-header"><h2>PROFESSIONAL EXPERIENCE</h2></div>', unsafe_allow_html=True)

# IIM Bangalore
st.markdown("""
<div class="experience-card">
    <h3>Indian Institute of Management Bangalore</h3>
    <p><em>Data & Research Intern</em> | Remote | January 2024 - October 2024</p>
    <ul>
        <li>Built a Python-based web scraping tool with <span class="metric-highlight">92% accuracy</span>, automating extraction for <span class="metric-highlight">7-9 Cr beneficiary records</span></li>
        <li>Implemented an Agile project management process that <span class="metric-highlight">reduced manual data handling time by 50%</span></li>
        <li>Delivered weekly analytical reports, using data insights to <span class="metric-highlight">improve strategic alignment by 30%</span></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Dr. Oetker
st.markdown("""
<div class="experience-card">
    <h3>Dr. Oetker India Pvt. Ltd.</h3>
    <p><em>Product Intern</em> | New Delhi | July 2022</p>
    <ul>
        <li>Conducted market analysis of customer preferences, optimizing product positioning and driving <span class="metric-highlight">65% of total sales growth</span></li>
        <li>Designed 10 product logos using Canva & Adobe Illustrator, increasing <span class="metric-highlight">market viewership by 20%</span></li>
        <li>Planned brand analytics dashboards in Excel & Tableau, driving <span class="metric-highlight">5.7% YoY growth</span></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Arogo AI
st.markdown("""
<div class="experience-card">
    <h3>Arogo AI, IIT Kharagpur</h3>
    <p><em>Product & Marketing Strategist Intern</em> | Remote | February 2025 - May 2025</p>
    <ul>
        <li>Led a cross-functional team of <span class="metric-highlight">10+ specialists</span> in developing an AI-driven mental health platform</li>
        <li>Authored PRDs for a CV pipeline for <span class="metric-highlight">300K+ patients</span>, automating medical image analysis</li>
        <li>Managed product roadmap and sprint planning using Agile methodologies, delivering <span class="metric-highlight">5+ features</span></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# DRDO
st.markdown("""
<div class="experience-card">
    <h3>DRDO Defense Young Scientist Laboratory</h3>
    <p><em>AI Research Intern</em> | Bangalore | June 2024 - July 2024</p>
    <ul>
        <li>Developed a RAG system improving document retrieval efficiency by <span class="metric-highlight">70%</span></li>
        <li>Optimized search workflows reducing manual search time by <span class="metric-highlight">50%</span></li>
        <li>Conducted comparative analysis of <span class="metric-highlight">15+ vector databases</span></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="section-header"><h2>PRODUCT & TECH PROJECTS</h2></div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-card">
    <h4>AI-Powered Resume Analysis System</h4>
    <p>Conducted user research with <span class="metric-highlight">50+ job seekers</span> to identify pain points in resume optimization. 
    Developed an AI system achieving <span class="metric-highlight">65% accuracy improvement</span> through user feedback.</p>
    <p><strong>Tools:</strong> Python, Streamlit, Google Gemini API, PyPDF2</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="project-card">
    <h4>AI Kitchen Assistant</h4>
    <p>Developed an AI-powered smart cooking assistant with <span class="metric-highlight">35% improved meal planning efficiency</span> 
    and <span class="metric-highlight">40% increased engagement</span> through voice commands.</p>
    <p><strong>Tools:</strong> Python, Streamlit, Google Gemini API, Hugging Face Transformers</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="project-card">
    <h4>Case Study on Manus AI</h4>
    <p>Conducted comprehensive case study focusing on innovations in memory architecture, tool orchestration, and goal management.</p>
    <p><strong>Tools:</strong> Streamlit, Python, Agentic AI frameworks</p>
</div>
""", unsafe_allow_html=True)

# Achievements Section
st.markdown('<div class="section-header"><h2>KEY ACHIEVEMENTS</h2></div>', unsafe_allow_html=True)

achievements = [
    "**Data Analytics & AI Launchpad Trainee, PwC:** Completed 4 specialized microcertifications achieving 92% average score",
    "**Treasurer, AI ML Community:** Spearheaded budget optimization resulting in 200-attendee increase in event participation",
    "**AWS Udacity AI/ML Scholarship:** Selected as one of top 2,000 students worldwide for exclusive 4-month AI Programming course",
    "**PASCH Youth Course:** Among top 50 students from 100+ nations for fully funded scholarship in Hamburg"
]

for achievement in achievements:
    st.markdown(f'<div class="achievement-item">{achievement}</div>', unsafe_allow_html=True)

# Call to Action Section
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h2 style="color: #003d82; margin-bottom: 1rem;">Ready to Innovate with Dyson?</h2>
    <p style="color: #666; font-size: 1.1rem; margin-bottom: 2rem;">
        Let's create revolutionary consumer technology solutions together
    </p>
</div>
""", unsafe_allow_html=True)

# Hire Me CTA Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 HIRE ME FOR DYSON INTERNSHIP", 
                 key="hire_me",
                 help="Click to celebrate!",
                 type="primary"):
        st.balloons()
        st.success("🎉 Thank you for considering my application! I'm excited to contribute to Dyson's mission of solving problems others ignore.")
        st.markdown("""
        <div style="text-align: center; margin-top: 1rem; padding: 1rem; background: #e8f5e8; border-radius: 8px;">
            <p><strong>Next Steps:</strong></p>
            <p>📧 Email: kashishbhasinn@gmail.com</p>
            <p>📱 Phone: (+91) 9811149303</p>
            <p>💼 LinkedIn: linkedin.com/in/kashish-bhasin</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem; margin-top: 2rem;">
    <p style="font-style: italic;">"Engineering solutions that make a difference in people's lives"</p>
</div>
""", unsafe_allow_html=True)
