import streamlit as st
import os
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Projects | My Portfolio",
    page_icon="💼",
    layout="wide"
)

# Custom CSS
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
    p {
        color: white;
        line-height: 1.6;
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
    </style>
    """, unsafe_allow_html=True)

# Function to display video
def extract_youtube_id(url):
    """Extract the YouTube video ID from various YouTube URL formats"""
    if "youtube.com/shorts/" in url:
        return url.split("youtube.com/shorts/")[1].split("?")[0].split("/")[0]
    elif "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtube.com/embed/" in url:
        return url.split("embed/")[1].split("?")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def display_video(video_url=None, video_path=None):
    """
    Display a video either from a URL or local path
    
    Parameters:
    -----------
    video_url : str, optional
        URL to a YouTube or Vimeo video
    video_path : str, optional
        Path to a local video file
    """
    if video_path and os.path.exists(video_path):
        # For local videos, use Streamlit's built-in video support
        st.video(video_path)
        return True
    
    elif video_url:
        # Try to use Streamlit's built-in video function first
        try:
            st.video(video_url)
            return True
        except Exception:
            pass
        
        # If that failed, try our custom embedding approach
        if "youtube" in video_url.lower():
            video_id = extract_youtube_id(video_url)
            if video_id:
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                st.markdown(f"""
                <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
                    <iframe
                        src="{embed_url}"
                        frameborder="0"
                        allowfullscreen
                        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
                    ></iframe>
                </div>
                """, unsafe_allow_html=True)
                return True
        
        elif "vimeo" in video_url.lower():
            # Extract Vimeo ID
            video_id = video_url.split("/")[-1]
            embed_url = f"https://player.vimeo.com/video/{video_id}"
            st.markdown(f"""
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
                <iframe
                    src="{embed_url}"
                    frameborder="0"
                    allowfullscreen
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
                ></iframe>
            </div>
            """, unsafe_allow_html=True)
            return True
        
        # Fallback - provide a link to the video
        st.warning(f"Unable to embed video. You can view it directly at: {video_url}")
        st.markdown(f"[Open Video in New Tab]({video_url})")
        return True
    
    return False

# Function to display a single project
def display_project(
    title,
    tags,
    description,
    key_features,
    technologies,
    video_url=None,
    video_path=None,
    image_path=None,
    links=None
):
    """
    Display a single project with customizable content
    
    Parameters:
    -----------
    title : str
        The title of the project
    tags : list
        List of tags/skills associated with the project
    description : str
        Project description text
    key_features : list
        List of key features of the project
    technologies : list
        List of technologies used in the project
    video_url : str, optional
        URL to a YouTube or Vimeo video
    video_path : str, optional
        Path to a local video file
    image_path : str, optional
        Path to a local image file (fallback if no video)
    links : dict, optional
        Dictionary of link labels and URLs, e.g., {"GitHub Repository": "https://github.com/..."}
    """
    st.markdown('<div class="project-container">', unsafe_allow_html=True)
    st.markdown(f'<h2 class="project-title">{title}</h2>', unsafe_allow_html=True)
    
    # Display tags
    tags_html = " ".join([f'<span class="tag">{tag}</span>' for tag in tags])
    st.markdown(tags_html, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Description")
        st.markdown(description)
        
        st.markdown("### Key Features")
        for feature in key_features:
            st.markdown(f"- {feature}")
        
        st.markdown("### Technologies Used")
        for tech in technologies:
            st.markdown(f"- {tech}")
    
    with col2:
        # Project media (video or image)
        video_displayed = display_video(video_url, video_path)
        
        # Fallback to image if video not displayed
        if not video_displayed and image_path and os.path.exists(image_path):
            st.image(Image.open(image_path))
        elif not video_displayed:
            st.info("Add project image or video to showcase your work")
        
        # Project links
        if links and len(links) > 0:
            st.markdown("### Links")
            for label, url in links.items():
                # Choose icon based on common link types
                icon = "🔗"  # Default icon
                if "github" in url.lower():
                    icon = "🔗"
                elif "demo" in label.lower() or "live" in label.lower():
                    icon = "🌐"
                elif "case" in label.lower() or "study" in label.lower() or "doc" in label.lower():
                    icon = "📄"
                elif "result" in label.lower() or "analysis" in label.lower():
                    icon = "📊"
                
                st.markdown(f"[{icon} {label}]({url})")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.divider()

def main():
    local_css()
    
    with st.sidebar:
        st.title("Navigation")
        st.markdown('<div class="sidebar-nav">', unsafe_allow_html=True)
        
        st.sidebar.markdown("### Menu")
        home = st.sidebar.button("Home", key="home", use_container_width=True)
        if home:
            st.switch_page("main.py")
            
        projects = st.sidebar.button("Projects", key="projects", use_container_width=True)

        papers = st.sidebar.button("Researches", key="researches", use_container_width=True)
        if papers:
            st.switch_page("pages/research.py")
    
    st.title("My Projects")
    
    display_project(
        title="Skin Analysis AI",
        tags=["Computer Vision"],
        description="""
            A feature that uses DETR object detection model with a custom dataset to identify acne
            problems, InceptionV3 for wrinkle classification, mediapipe for facial landmark detection,
            and VGG16 for skin type classification. The same method for wrinkle detection is applied to
            detect dark circles under the eyes.
        """,
        key_features=[
            "Object Detection",
            "Landmark Detection",
            "Image Classification",
        ],
        technologies=[
            "Flask API",
            "Tensorflow",
            "Transformers"
        ],
        video_url="https://www.youtube.com/embed/sdrObaXCZVc",
    )
    
    # Example of using the template for Project 2
    display_project(
        title="Facial Ratio Measurement AI",
        tags=["Computer Vision"],
        description="""
            Using EfficientNetV2, the system can classify the shape of the face. It also calculates the width-
            to-length ratio of the face using Euclidean Distance to measure the distance between facial landmarks.
        """,
        key_features=[
            "Object Detection",
            "Landmark Detection",
            "Image Classification",
        ],
        technologies=[
            "Flask API",
            "Tensorflow",
            "Transformers"
        ],
        video_url="https://www.youtube.com/embed/qANcUrKSWHU",

    )
    
    # Example of using the template for Project 3
    display_project(
        title="Human Tracking System for Smart Wheelchair",
        tags=["Computer Vision", "Robotics"],
        description="""
            The system Leveraging YOLOv5 and byte track to create auto navigation by following human
            in front of the smart wheelchair captured by web camera. The system is embedded to Nvidia
            Jetson TX2.
        """,
        key_features=[
            "Object Detection",
            "Object Tracking",
        ],
        technologies=[
            "Nvidia Jetson",
            "Arduino",
            "Pytorch"
        ],
        video_url="https://youtu.be/F_w_tT8pDR4",
    )

    display_project(
        title="Room Name Recognition System",
        tags=["Computer Vision", "Robotics"],
        description="""
            The system contained object detection to detect the plate using YOLOv5 and read/recognize
            the plate character using EasyOCR, the object captured using web camera. The system is
            embedded to Nvidia Jetson TX2.
            """,
        key_features=[
            "Object Detection",
            "OCR",
        ],
        technologies=[
            "Nvidia Jetson",
            "Arduino",
            "Pytorch",
        ],
        video_url="https://youtu.be/HYcV47oXoCE",

    )

if __name__ == "__main__":
    main()