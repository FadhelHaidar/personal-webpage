import streamlit as st
from PIL import Image

# Configure the page
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🚀",
    layout="wide"
)

# Set dark theme for the entire app
st.markdown("""
<style>
    .reportview-container {
        background-color: #121212;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #1E1E1E;
        color: white;
    }
    body {
        color: white;
        background-color: #121212;
    }
    /* Responsive column fixes */
    .row-widget.stHorizontal {
        flex-wrap: wrap !important;
    }
    /* Make columns more responsive on smaller screens */
    @media (max-width: 768px) {
        div[data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            margin-bottom: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Custom CSS to improve the appearance
def local_css():
    st.markdown("""
    <style>
    .main {
        padding: 2rem;
        background-color: #121212;
        color: white;
    }
    h1, h2, h3 {
        margin-bottom: 1rem;
        color: white;
    }
    h1 {
        margin-top: 0;
        padding-top: 0;
    }
    p {
        color: white;
        line-height: 1.6;
    }
    .project-container {
        border: 1px solid #333;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 30px;
        background-color: #1E1E1E;
        color: white;
    }
    .project-title {
        color: white;
        margin-bottom: 15px;
    }
    .tag {
        display: inline-block;
        background-color: #333;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        margin-right: 5px;
        margin-bottom: 5px;
        font-size: 14px;
    }
    /* Fix for white elements */
    .stMarkdown, .stMarkdown p, .stMarkdown div {
        color: white;
        background-color: transparent;
    }
    /* Make sure containers don't have white backgrounds */
    div.element-container, div.row-widget, div.stButton, div.stText, div.Widget {
        background-color: transparent !important;
        border: none !important;
    }
    /* Fix for white info boxes */
    div.stAlert {
        background-color: #1E1E1E !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    /* Improve responsive design for the intro section */
    .intro-section {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
    }
    .intro-text {
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
    }
    /* Enhanced profile header styling with better responsiveness */
    .profile-header {
        display: flex;
        flex-direction: column;
        margin-bottom: 40px;
        padding-top: 20px;
    }
    .profile-name {
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.2;
        letter-spacing: -0.03em;
        color: #ffffff;
    }
    .profile-title {
        font-size: 1.8rem;
        font-weight: 500;
        margin: 0.5rem 0 1.5rem 0;
        color: #4d9fff;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    .profile-intro {
        font-size: 1.1rem;
        line-height: 1.7;
        margin-top: 1rem;
    }
    /* New styles for better alignment and responsiveness */
    .image-container {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        height: 100%;
        width: 100%;
    }
    .image-container img {
        max-width: 280px;
        width: 100%;
        height: auto;
    }
    /* Remove negative margin that was causing issues */
    .profile-header {
        margin-left: 0;
    }
    .text-container {
        width: 100%;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #1E1E1E;
    }
    .sidebar-nav {
        padding: 10px 0;
    }
    .sidebar-nav-item {
        padding: 10px 15px;
        border-radius: 5px;
        margin-bottom: 8px;
        transition: background-color 0.3s;
    }
    .sidebar-nav-item:hover {
        background-color: #333;
    }
    .sidebar-nav-item.active {
        background-color: #4d9fff;
    }
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .profile-title {
            font-size: 1.5rem;
        }
        .profile-intro {
            font-size: 1rem;
        }
        .image-container {
            margin-bottom: 1.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    local_css()
    
    # Create sidebar
    with st.sidebar:
        st.title("Navigation")
        st.markdown('<div class="sidebar-nav">', unsafe_allow_html=True)
        
        # Home link (current page)
        st.sidebar.markdown("### Menu")
        home = st.sidebar.button("Home", key="home", use_container_width=True)
        
        # Projects link
        projects = st.sidebar.button("Projects", key="projects", use_container_width=True)
        if projects:
            st.switch_page("pages/projects.py")
            
    # Main content - Using containers for better responsiveness
    st.markdown('<div class="intro-section">', unsafe_allow_html=True)
    
    # Create responsive columns with a container
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        # Profile picture with responsive container
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        profile_pic_path = "assets/photo.jpg"
        try:
            profile_img = Image.open(profile_pic_path)
            st.image(profile_img, use_container_width=True, output_format="JPEG", clamp=True)
        except Exception as e:
            st.error(f"Could not load image: {e}")
            st.write("Please ensure the image path is correct.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Text content with responsive container
        st.markdown('<div class="text-container">', unsafe_allow_html=True)
        st.markdown("""
        <div class="profile-header">
            <div class="profile-title">Welcome to my page! 🔥🔥🔥</div>
            <div class="profile-intro">
            Hi, my name is Fadhel! I'm a dedicated AI Engineer with over two years of experience in the field. 
            My passion lies in crafting innovative solutions with AI, and I'm always eager to expand my knowledge and skills.
            <br><br>
            In my free time, you can find me pushing the limits as a hardstuck Diamond 1 player in Valorant 😂.
            <br><br>
            I hold a degree in Computer Engineering from Brawijaya University. 
            Throughout my career, I've worked with various companies, delivering impactful solutions that drive meaningful change.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Skills section
    st.divider()
    # st.header("Tech Stacks")
    
    # # Categorized skills
    # skills_data = {
    #     "Programming Languages": ["Python", "SQL"],
    #     "Frameworks & Libraries": ["Fast API", "Flask API", "Pytorch", "TensorFlow"],
    #     "Tools & Technologies": ["Docker", "Git", "vLLM", "Open Vino", "TensorRT"],
    # }
    
    # for category, skills in skills_data.items():
    #     st.subheader(category)
        
    #     # Create bullet points for each skill
    #     bullet_points = "\n".join([f"- {skill}" for skill in skills])
    #     st.markdown(bullet_points)
    
    # # Experience section
    # st.divider()
    # st.header("Experience")
    
    # # Example experience items
    # experiences = [
    #     {
    #         "title": "Artificial Intelligence Engineer",
    #         "company": "PT United Tractors Tbk",
    #         "duration": "Jul 2024 - Present",
    #         "description": "Working on RAG systems, PDF extraction with multimodal approaches, and customer data mapping using embedding models.",
    #         "highlights": [
    #         "Developing RAG system to help the business consultant advancing the pitching process, the system will be able to retrieve multiple data sources from structured and unstructured data",
    #         "Developing PDF extractor system using multimodal to help lab team advancing the data storing system",
    #         "Developing data mapping using embedding model and semantic search to map customer data to streamline the customer search"
    #         ]
    #     },
    #     {
    #         "title": "Artificial Intelligence Engineer",
    #         "company": "PT Asa Ren Global Nusantara",
    #         "duration": "Mar 2024 - Jul 2024",
    #         "description": "Built RAG systems with Claude, OCR systems using multimodal LLMs, and biomedical data standardization.",
    #         "highlights": [
    #             "Developed patient analysis with RAG system, utilizing Claude sonnet model",
    #             "Developed an OCR system using multimodal LLM to extract multi variance electronic health record structure",
    #             "Developed biomedical data standardization system to map the biomedical terms into standardized format using embedding model and semantic search"
    #         ]
    #     },
    #     {
    #         "title": "Artificial Intelligence Engineer",
    #         "company": "PT Wide Technologies Indonesia",
    #         "duration": "Aug 2023 - Mar 2024",
    #         "description": "Developed computer vision solutions for face analysis, skin analysis, and eKYC processes.",
    #         "highlights": [
    #             "Developed a face analyzer that can classify face shape with 85% accuracy using Efficientnet and calculate facial features ratio, using Euclidean distance for glasses recommendation",
    #             "Built a skin analysis service for skin care recommendation on a telemedicine app, using InceptionV3, DETR, and vgg16 for various skin analyses",
    #             "Built an API service for eKYC process using MTCNN, ArcFace, and similarity measures, improving onboarding efficiency by 50%"
    #         ]
    #     },
    #     {
    #         "title": "Artificial Intelligence Engineer (Part-time)",
    #         "company": "GAIA Dental Studio",
    #         "duration": "May 2023 - Sep 2023",
    #         "description": "Created AI solutions for dental and ocular disease detection, and invoice extraction.",
    #         "highlights": [
    #             "Created a dental disease detection API using YOLOv8 and VGG16 models with 70% mAP and 89% precision",
    #             "Established ocular disease classification API services using VGG16 model with 89% precision",
    #             "Designed and implemented an invoice extraction system using YOLOv8, Google Vision, and GPT 3.5 with 92% mAP"
    #         ]
    #     },
    # ]
    
    # for exp in experiences:
    #     st.markdown('<div class="experience-item">', unsafe_allow_html=True)
    #     st.subheader(f"{exp['title']} | {exp['company']}")
    #     st.markdown(f"**{exp['duration']}**")
    #     st.markdown(exp['description'])
        
    #     st.markdown("**Key Achievements:**")
    #     for highlight in exp['highlights']:
    #         st.markdown(f"- {highlight}")
        
    #     st.divider()
    
    # Contact information
    st.header("Contact Me")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Contact Information")
        st.markdown("📧 fadhel1597l@gmail.com")
    
    with col2:
        st.markdown("### Social Links")
        st.markdown("""
        - [GitHub](https://github.com/fadhel1597)
        - [LinkedIn](https://linkedin.com/in/fadhel-haidar)
        """)

        
if __name__ == "__main__":
    main()