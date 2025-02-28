import streamlit as st
import os
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Researches | My Portfolio",
    page_icon="📚",
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
    .paper-title {
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
    /* Citation box styling */
    .citation-box {
        background-color: #1E1E1E;
        border-left: 3px solid #4d9fff;
        padding: 10px 15px;
        font-family: monospace;
        font-size: 0.9em;
        margin: 10px 0;
        white-space: pre-wrap;
        word-wrap: break-word;
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
    /* Paper metrics styling */
    .metrics-container {
        display: flex;
        flex-wrap: wrap;
        margin-bottom: 15px;
    }
    .metric-item {
        background-color: #1E1E1E;
        border-radius: 5px;
        padding: 8px 12px;
        margin-right: 10px;
        margin-bottom: 10px;
        font-size: 0.9em;
    }
    .metric-label {
        font-weight: bold;
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to display a PDF viewer
def display_pdf(pdf_path=None, pdf_url=None):
    """
    Display a PDF viewer for research papers
    
    Parameters:
    -----------
    pdf_path : str, optional
        Path to a local PDF file
    pdf_url : str, optional
        URL to a PDF file
    """
    if pdf_path and os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()
        st.download_button(
            label="Download PDF",
            data=pdf_data,
            file_name=os.path.basename(pdf_path),
            mime="application/pdf"
        )
        
        # Display PDF in an iframe
        st.markdown(f"""
        <iframe
            src="data:application/pdf;base64,{pdf_data.encode('base64').decode()}"
            width="100%"
            height="500"
            style="border: none;"
        ></iframe>
        """, unsafe_allow_html=True)
        return True
    
    elif pdf_url:
        st.markdown(f"[View Full Paper]({pdf_url})")
        
        # Try to embed the PDF if it's directly accessible
        try:
            st.markdown(f"""
            <iframe
                src="{pdf_url}"
                width="100%"
                height="500"
                style="border: none;"
            ></iframe>
            """, unsafe_allow_html=True)
            return True
        except Exception:
            st.info("PDF preview not available. Please use the link above to view the paper.")
            return False
    
    return False

# Function to display paper citation
def display_citation(citation_text):
    """Display a formatted citation box"""
    st.markdown(f"""
    <div class="citation-box">
    {citation_text}
    </div>
    """, unsafe_allow_html=True)

# Function to display paper metrics
def display_metrics(metrics):
    """
    Display metrics for a research paper
    
    Parameters:
    -----------
    metrics : dict
        Dictionary of metrics like {"Citations": 42, "Impact Factor": 3.8}
    """
    if not metrics:
        return
    
    metric_html = '<div class="metrics-container">'
    for label, value in metrics.items():
        metric_html += f"""
        <div class="metric-item">
            <span class="metric-label">{label}:</span>
            <span>{value}</span>
        </div>
        """
    metric_html += '</div>'
    
    st.markdown(metric_html, unsafe_allow_html=True)

# Function to display a single research paper
def display_paper(
    title,
    authors,
    publication,
    year,
    abstract,
    tags,
    highlights=None,
    methodologies=None,
    pdf_url=None,
    image_path=None,
    metrics=None,
    citation=None,
    links=None
):
    """
    Display a single research paper with customizable content
    
    Parameters:
    -----------
    title : str
        The title of the paper
    authors : list
        List of authors
    publication : str
        Journal or conference name
    year : int
        Publication year
    abstract : str
        Paper abstract
    tags : list
        List of research areas/keywords
    highlights : list, optional
        List of key findings or contributions
    methodologies : list, optional
        List of methodologies used
    pdf_url : str, optional
        URL to the PDF of the paper
    image_path : str, optional
        Path to a relevant figure from the paper
    metrics : dict, optional
        Dictionary of metrics like {"Citations": 42, "Impact Factor": 3.8}
    citation : str, optional
        Formatted citation for the paper
    links : dict, optional
        Dictionary of link labels and URLs
    """
    st.markdown('<div class="paper-container">', unsafe_allow_html=True)
    st.markdown(f'<h2 class="paper-title">{title}</h2>', unsafe_allow_html=True)
    
    # Author information
    st.markdown(f"**Authors:** {', '.join(authors)}")
    st.markdown(f"**Published in:** {publication}, {year}")
    
    # Display metrics if provided
    if metrics:
        display_metrics(metrics)
    
    # Display tags
    tags_html = " ".join([f'<span class="tag">{tag}</span>' for tag in tags])
    st.markdown(tags_html, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Abstract")
        st.markdown(abstract)
        
        if highlights:
            st.markdown("### Key Findings")
            for point in highlights:
                st.markdown(f"- {point}")
        
        if methodologies:
            st.markdown("### Methodologies")
            for method in methodologies:
                st.markdown(f"- {method}")
        
        if citation:
            st.markdown("### Citation")
            display_citation(citation)
    
    with col2:
        # Paper PDF or image
        pdf_displayed = display_pdf(pdf_url=pdf_url)
        
        # Fallback to image if PDF not displayed
        if not pdf_displayed and image_path and os.path.exists(image_path):
            st.image(Image.open(image_path))
            st.caption("Figure from the paper")
        
        # Paper links
        if links and len(links) > 0:
            st.markdown("### Links")
            for label, url in links.items():
                # Choose icon based on common link types
                icon = "🔗"  # Default icon
                if "doi" in label.lower():
                    icon = "🔍"
                elif "code" in label.lower() or "github" in url.lower():
                    icon = "💻"
                elif "dataset" in label.lower():
                    icon = "📊"
                elif "video" in label.lower() or "presentation" in label.lower():
                    icon = "🎬"
                
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
        if projects:
            st.switch_page("pages/projects.py")

        papers = st.sidebar.button("Researches", key="researches", use_container_width=True)
        
    
    st.title("Researches")
    
    # Example Paper 1
    display_paper(
        title="A convolutional neural network-VGG16 method for corrosion inhibition of 304SS in sulfuric acid solution by timoho leaf extract",
        authors=[
            "Femiana Gapsari",
            "Fitri Utaminingrum",
            "Chin Wei Lai",
            "Khairul Anam",
            "Abdul M. Sulaiman",
            "Muhamad F. Haidar",
            "Tobias S. Julian",
            "Eno E. Ebenso"
        ],
        publication="Journal of Materials Research and Technology",
        year=2024,
        abstract="""
            A corrosion inhibition test, coupled with a quantification of in-situ H2 evolution, can be used to evaluate an organic inhibitor such as Timoho leaf extract (TLE). 
            TLE is a biodegradable and effective corrosion inhibitor because of its potential to protect 304SS against sulfuric acid. 
            TLE corrosion inhibitor was studied through systematic electrochemical experiments and morphological characterization, with a concentration range of 0–6g L−1. 
            Convolutional Neural Network (CNN)-VGG16 was one of the machine learning approaches used to classify and predict physical changes in hydrogen gas bubbles. 
            Constituents of the TLE and 304SS surfaces were analyzed by FT-IR and UV–Vis tests. 
            The results suggested that 3 g L−1 TLE inhibitor was able to reduce the corrosion rate by 99.37 %. 
            The TLE's inhibition mechanism on 304SS was mixed adsorption and mixed type inhibitor that followed the Isothermal Freundlich Equation. 
            The prediction model by CNN-VGG16 for corrosion tests at varied inhibitor doses was 96% accurate. 
            SEM tests revealed that TLE constituent adsorption on the 304SS surface had a smooth surface morphology with few degraded spots.
        """,
        tags=["Computer Vision", "Deep Learning"],
        methodologies=[
            "VGG16",
        ],
        pdf_url=r"https://pdf.sciencedirectassets.com/286905/1-s2.0-S2238785424X00034/1-s2.0-S2238785424006859/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLWVhc3QtMSJIMEYCIQCl8yOfy32iHnYBFZeF4GWdGR5qWIKHwR3HftwKDwEZJAIhANhWKWC8vpw%2BEIlIYIuo5WUH2zMis9PNoivqhU2uCHDzKrwFCIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBRoMMDU5MDAzNTQ2ODY1Igw6e6Pxpg%2Bx0ieFPOEqkAW4YlbhvjnIXyI6veaM2kgqEX1R5b%2Ff1crFdCr6p9Qt%2FgOBPGXuk1xXAuQq3o1s1EuRS1ID4cfKBNJn5LKseD2habLttbuOpOI3RtiLhLLVsqQLX2AanFeprl2aP2Y8eBxd2UxjNlCWtBC1nhFeEOAgSgSk2yh7tPOfmVJ4x%2BHTvyid02yAkVmIZbM52o1YoBVnOd%2FXW3SJFmly%2BgMgTjU8oPT%2BsYdia5jXDVMkc8JhF7wVI11P8XsC4BrX9%2FYDADTItEZZqcLU%2FzAptp8ax%2BFONv4t%2BOaacjU2x900%2FVHZ0y3qpeTZBHdt1G5wLkmogN2aDQKyvgc%2BLkZexoiTA%2F4LbUMyxXiEurui9ktup6rz8oyAX9a8NguHMlLRKhXmaEixBZUHUt2P8xaPA2yq2cRt7szwaRvpIyeva0WkXvHVKUPLcvPO96uZ0%2F%2FTPcojkMJJBYyQmWDbEwqNJuNS6dmHq903Qp%2Bs241s5CyWLkqSojwo8H%2BlhcqzWrkSwDe0f2NeR7S16ERg9A3n6mUhiy4LECOL2n9q%2B%2FstJKVX%2Fbbly%2FqhsRSGHn9SKLzyCMdxSCUWpRCNrY%2B%2BVrreKaMm6toAsesOTO3Am6sxNV7vyLjv5ZaHUyKk7jHyY1ILwLKtv9IPT23lCoOTPKZ2TgJnC%2F%2BtOu3ubZBe%2BRCvuvGN6ETv%2Bm87fioAAz29ewBS7YDtmkUfm1IVISv3QELLqtI4lBXkk2TbjJa4jmMYJwXTMHWCdJ9%2FCDsRLeYB7try7BAJ5LQDwtatpi6Jtmy0vItlkWSPvIXPiTcCJ31PIGsBLrYL%2Fg6wUMdfiiGkPQPGKMfFwyejCYT3%2FIo1JCDwmJ4XIbKNJaS3q5D8TVsqrsrxoSVNWTD9qIS%2BBjqwAeWRDrXErGsnv8xkKhOmNCji13tgu3BpTnfkkx3E2JCb%2Bkd8LPvCVyQiiVADTjzEkcWXJ3rAWf%2BKtsW%2F%2BL04Knw7D2NtvdVrHaXj658Ogh1PvkY9YhKKyf2tiFi1u9az3v6Z3JfmYK1LwdhzF0%2B%2F%2FhV%2B9pPSZxG0lBa%2BuxJP1dLV6swdvHJhhS9bblVCoI2YMj7thbFv7k9aavImieVxPcdfccjJd%2FsHDG%2BW2lnCLlsa&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250228T025832Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYSY6Q5MKP%2F20250228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d3fa230b44855cdb814718c4cded8b667e8c49a55aebdc5ce68f5876a93898f3&hash=ebad16193efe4a1225ee5c01d6a6b9e95644b2064c6f852a5b036b8fae22f3e4&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2238785424006859&tid=spdf-32295588-865e-4485-ba1a-1093b41db3cd&sid=dd3ff4699862464d68491108b05e171e448egxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0f075b515d065654555d&rr=918d274808d8df8b&cc=id",
        links={
            "DOI": "https://doi.org/10.1016/j.jmrt.2024.03.156",
        }
    )
    

if __name__ == "__main__":
    main()