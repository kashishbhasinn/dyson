import streamlit as st
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Kashish Bhasin - Dyson Summer Intern",
    page_icon="🌪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #6C63FF;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #6C63FF, #FF6B6B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .subtitle {
        font-size: 1.3rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .project-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #6C63FF;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        color: black;

    }
    
    .skill-badge {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.8rem;
        font-weight: bold;
    }
    
    .internship-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    
    .achievement-item {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 0.5rem 0;
    }
    
    .dyson-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
    }
    
    .hire-button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.3s;
    }
    
    .hire-button:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for progress tracking
if 'visited_sections' not in st.session_state:
    st.session_state.visited_sections = set()

# Sidebar Navigation
st.sidebar.markdown("## 🧭 Navigation")
sections = ["Introduction", "Internships", "Projects", "Skills", "Why Dyson", "Achievements", "Contact"]

selected_section = st.sidebar.selectbox("Choose a section:", sections)
st.session_state.visited_sections.add(selected_section)

# Progress tracking
progress = len(st.session_state.visited_sections) / len(sections)
st.sidebar.progress(progress)
st.sidebar.markdown(f"**Progress:** {int(progress * 100)}% complete")

# Visited sections indicator
st.sidebar.markdown("### ✅ Visited Sections")
for section in sections:
    if section in st.session_state.visited_sections:
        st.sidebar.markdown(f"✅ {section}")
    else:
        st.sidebar.markdown(f"⬜ {section}")

# Main content based on selected section
if selected_section == "Introduction":
    st.markdown('<h1 class="main-header">Hi, I\'m Kashish Bhasin! 👋</h1>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Product strategist and Computer Science undergrad passionate about leveraging technology to solve real-world consumer problems</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🎓 Education</h3>
            <p><strong>BTech CSE - AI/ML</strong><br>
            Manipal University Jaipur<br>
            CGPA: <strong>9.29</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>💼 Experience</h3>
            <p><strong>4+ Internships</strong><br>
            IIM Bangalore, DRDO, Dr. Oetker<br>
            Arogo AI (IIT Kharagpur)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🏆 Recognition</h3>
            <p><strong>Global Achiever</strong><br>
            Top 2,000 AWS Scholarship<br>
            Top 50 PASCH Global</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🚀 Fun Fact")
    st.info("I led a cross-functional team of 10+ specialists at IIT Kharagpur to develop an AI-driven mental health platform - combining my passion for technology with real-world impact!")

elif selected_section == "Internships":
    st.markdown("# 💼 Professional Experience")
    
    # Arogo AI
    st.markdown("""
    <div class="internship-card">
        <h3>🧠 Arogo AI, IIT Kharagpur</h3>
        <h4>Product & Marketing Strategist Intern | Feb 2025 - May 2025</h4>
        <ul>
            <li><strong>Led a cross-functional team of 10+ specialists</strong> (UI/UX designers, developers, LLM engineers) in developing an AI-driven mental health platform, streamlining the development workflow</li>
            <li><strong>Authored PRDs for a CV pipeline for 300K+ patients</strong>, automating medical image analysis using Swin-UNETR, Inception v3 and BLIP-2</li>
            <li><strong>Managed product roadmap and sprint planning</strong> using Agile methodologies, delivering 5+ features for the prescription management system</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # IIM Bangalore
    st.markdown("""
    <div class="internship-card">
        <h3>📊 Indian Institute of Management Bangalore</h3>
        <h4>Data & Research Intern | Jan 2024 - Oct 2024</h4>
        <ul>
            <li><strong>Built a Python-based web scraping tool with 92% accuracy</strong>, automating extraction for 7-9 Cr beneficiary records</li>
            <li><strong>Implemented an Agile project management process</strong> that reduced manual data handling time by 50%</li>
            <li><strong>Delivered weekly analytical reports</strong>, using data insights to improve strategic alignment by 30%</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Dr. Oetker
    st.markdown("""
    <div class="internship-card">
        <h3>🍕 Dr. Oetker India Pvt. Ltd.</h3>
        <h4>Product Intern | July 2022</h4>
        <ul>
            <li><strong>Conducted a market analysis of customer preferences</strong>, optimizing product positioning and driving 65% of its total sales growth</li>
            <li><strong>Designed 10 product logos</strong> using Canva & Adobe Illustrator, increasing market viewership 20%</li>
            <li><strong>Planned brand analytics dashboards</strong> in Excel & Tableau, driving 5.7% YoY growth</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # DRDO
    st.markdown("""
    <div class="internship-card">
        <h3>🛡️ DRDO Defense Young Scientist Laboratory</h3>
        <h4>AI Research Intern | June 2024 - July 2024</h4>
        <ul>
            <li><strong>Developed a RAG system for the DRDO procurement manual</strong>, improving the efficiency of document retrieval by 70%</li>
            <li><strong>Optimized search workflows</strong> using LangChain, ChromaDB, and HuggingFaceEmbeddings, to reduce manual search time by 50%</li>
            <li><strong>Conducted a comparative analysis of 15+ vector databases</strong>, collaborating with the LLM team to deploy large-scale AI models</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif selected_section == "Projects":
    st.markdown("# 🚀 Innovation Showcase")
    
    tab1, tab2, tab3 = st.tabs(["AI Resume Analyzer", "AI Kitchen Assistant", "Manus AI Case Study"])
    
    with tab1:
        st.markdown("""
        <div class="project-card">
            <h3>🎯 AI-Powered Resume Analysis System</h3>
            <p><strong>Impact:</strong> Helped 50+ job seekers optimize their resumes with 65% accuracy improvement through user feedback</p>
            <h4>What I Built:</h4>
            <ul>
                <li>Conducted user research with 50+ job seekers to identify pain points in resume optimization</li>
                <li>Developed an AI system that analyzes resumes, identifying missing keywords and suggesting improvements</li>
                <li>Improved accuracy to 65% through iterative user feedback integration</li>
            </ul>
            <p><strong>Tech Stack:</strong> Python, Streamlit, Google Gemini API, PyPDF2, python-dotenv</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="project-card">
            <h3>🍳 AI Kitchen Assistant</h3>
            <p><strong>Impact:</strong> 35% improved meal planning efficiency and 40% increased engagement through voice commands</p>
            <h4>Features:</h4>
            <ul>
                <li>Voice-enabled smart cooking assistant with natural language processing</li>
                <li>Intelligent meal planning with personalized recommendations</li>
                <li>Real-time cooking guidance and recipe optimization</li>
            </ul>
            <p><strong>Tech Stack:</strong> Python, Streamlit, Google Gemini API, Hugging Face Transformers, Google Speech Recognition API</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="project-card">
            <h3>🤖 Case Study on Manus AI: Advancing Autonomous Agent Capabilities</h3>
            <p><strong>Focus:</strong> Innovations in memory architecture, tool orchestration, and goal management</p>
            <h4>Research Areas:</h4>
            <ul>
                <li>Memory architecture optimization for autonomous agents</li>
                <li>Advanced tool orchestration mechanisms</li>
                <li>Goal management and decision-making frameworks</li>
            </ul>
            <p><strong>Tech Stack:</strong> Streamlit, Python, Agentic AI frameworks</p>
        </div>
        """, unsafe_allow_html=True)

elif selected_section == "Skills":
    st.markdown("# 🛠️ Technical Arsenal")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Product & Business")
        skills = ["Product Roadmapping", "Agile Scrum", "Jira", "Notion", "Feature Prioritization", 
                 "Competitive Analysis", "User Research", "KPI Tracking", "Market Segmentation", "Business Model Analysis"]
        for skill in skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("<br><br>### 📈 Marketing & Analytics", unsafe_allow_html=True)
        marketing_skills = ["Google Analytics", "Meta Ads Manager", "Social Media Strategy", "Brand Positioning", 
                           "Customer Journey Mapping", "SWOT Analysis", "Survey Design", "Sentiment Analysis", "A/B Testing"]
        for skill in marketing_skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 💻 Technical")
        tech_skills = ["Python (NumPy, Pandas, Scikit-learn)", "SQL", "Tableau", "Excel", 
                      "LangChain", "HuggingFace", "Selenium", "BeautifulSoup"]
        for skill in tech_skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("<br><br>### ☁️ Platforms", unsafe_allow_html=True)
        platform_skills = ["AWS", "Azure (basic)", "Streamlit", "ChromaDB", "GitHub", "Canva", "Adobe Illustrator"]
        for skill in platform_skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

elif selected_section == "Why Dyson":
    st.markdown("""
    <div class="dyson-section">
        <h1>🌪️ Why Dyson?</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Typewriter effect simulation
    dyson_text = """I'm inspired by Dyson's mission to solve problems others ignore. My passion for data, technology, and creative problem-solving aligns perfectly with Dyson's culture of innovation. I want to contribute to products that make a real impact, learn from world-class teams, and grow in a fast-paced, global environment."""
    
    placeholder = st.empty()
    displayed_text = ""
    
    if st.button("🎬 Play My Dyson Story"):
        for char in dyson_text:
            displayed_text += char
            placeholder.markdown(f"*{displayed_text}*")
            time.sleep(0.03)
    else:
        st.markdown(f"*{dyson_text}*")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎯 What I Bring
        - **Product Strategy** from managing roadmaps for 300K+ users
        - **Market Research** experience driving 65% sales growth
        - **Data Analytics** expertise with millions of records
        """)
    
    with col2:
        st.markdown("""
        ### 🔍 My Interest Areas
        - **Marketing Analytics** and consumer insights
        - **Product Research** and user behavior analysis
        - **Cross-functional leadership** and team collaboration
        """)
    
    with col3:
        st.markdown("""
        ### 🚀 Ready to Impact
        - **Fast learner** with global exposure (50 countries)
        - **Innovation mindset** from AI/ML background
        - **Results-driven** approach with proven metrics
        """)

elif selected_section == "Achievements":
    st.markdown("# 🏆 Achievements & Recognition")
    
    achievements = [
        {
            "title": "AWS Udacity AI/ML Scholarship - Python Nanodegree AI Programming",
            "description": "Selected as one of the top 2,000 students worldwide to attend an exclusive 4-month AI Programming course, gaining hands-on experience in advanced AI and ML concepts",
            "icon": "☁️"
        },
        {
            "title": "Data Analytics & AI Launchpad Trainee, PwC",
            "description": "Completed 4 specialized microcertifications in IT fundamentals, RDBMS (Oracle) and data engineering, achieving a 92% average score across all assessments",
            "icon": "📊"
        },
        {
            "title": "Treasurer, AI ML Community",
            "description": "Spearheaded budget optimization efforts, identifying cost inefficiencies and reallocating funds, resulting in a 200-attendee increase in event participation over six months",
            "icon": "💰"
        },
        {
            "title": "PASCH Youth Course (JuKu)",
            "description": "Among the top 50 students from over 100 nations to receive a fully funded 3-week youth scholarship in Hamburg by the Max Mueller Bhavan & Goethe Institute in June 2019, expanding my global network by 100+ international peers",
            "icon": "🌍"
        }
    ]
    
    for achievement in achievements:
        st.markdown(f"""
        <div class="achievement-item">
            <h3>{achievement['icon']} {achievement['title']}</h3>
            <p>{achievement['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Animated counters
    st.markdown("### 📈 Impact Numbers")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("CGPA", "9.29", "🎓")
    with col2:
        st.metric("Global Ranking", "Top 2,000", "🌟")
    with col3:
        st.metric("PwC Score", "92%", "📊")
    with col4:
        st.metric("Event Growth", "+200", "📈")

elif selected_section == "Contact":
    st.markdown("# 📞 Let's Connect!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📧 Contact Information
        
        **Email:** kashishbhasinn@gmail.com  
        **Phone:** (+91) 9811149303  
        **LinkedIn:** [linkedin.com/in/kashish-bhasin](https://linkedin.com/in/kashish-bhasin)  
        **GitHub:** [github.com/kashishbhasinn](https://github.com/kashishbhasinn)
        """)
        
        st.markdown("---")
        
        # The big hire button
        if st.button("🎉 HIRE ME FOR DYSON!", key="hire_button"):
            st.balloons()
            st.success("🎊 Thank you for considering my application! I'm excited about the opportunity to contribute to Dyson's innovative culture and make a real impact. Let's build the future together!")
            st.markdown("### 🚀 Next Steps:")
            st.write("1. 📧 I'll follow up via email within 24 hours")
            st.write("2. 📅 Ready for interviews at your convenience")
            st.write("3. 💼 Prepared to start contributing from day one!")
    
    with col2:
        st.markdown("""
        ### 🎯 Quick Stats
        
        **Experience:** 4+ Internships  
        **Education:** BTech CSE-AI/ML  
        **CGPA:** 9.29  
        **Global Recognition:** Top 2,000 AWS  
        **Leadership:** 10+ team members  
        **Impact:** 300K+ users affected
        """)
        
        st.markdown("### 🌟 Why Choose Me?")
        st.write("✅ Proven track record in product strategy")
        st.write("✅ Strong technical and business skills")
        st.write("✅ Experience with cross-functional teams")
        st.write("✅ Data-driven decision making")
        st.write("✅ Global perspective and adaptability")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🌪️ Built with passion for Dyson Summer Internship 2025 | Kashish Bhasin</p>
    <p>Combining innovation, technology, and real-world impact - just like Dyson!</p>
</div>
""", unsafe_allow_html=True)
