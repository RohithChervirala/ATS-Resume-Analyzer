import streamlit as st
from groq import Groq
import PyPDF2
import os
from dotenv import load_dotenv

# 1. Page Configuration (Must be the first command)
st.set_page_config(
    page_title="Smart ATS Analyzer",
    page_icon="👔",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.sidebar.error("❌ GROQ_API_KEY not found in .env file.")
    st.stop()
    
client = Groq(api_key=api_key)

# --- Functions ---
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def get_model_output(prompt):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content

# --- Custom CSS for styling ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4A90E2;
        text-align: center;
        font-weight: 700;
    }
    .sub-text {
        text-align: center;
        color: #888;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4A90E2;
        color: white;
        height: 3em;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Main Layout ---
st.markdown('<div class="main-header">🚀 Smart ATS Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Optimize your resume for Applicant Tracking Systems with AI precision</div>', unsafe_allow_html=True)

# Create two main columns
col1, col2 = st.columns([1, 2])

# --- Sidebar / Left Column (Controls) ---
with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("Upload your details below to get started.")
    
    uploaded_file = st.file_uploader("📂 Upload Resume (PDF)", type="pdf")
    
    analysis_option = st.selectbox(
        "🔍 Select Analysis Type",
        ["Full Analysis", "Skill Match", "ATS Score", "Missing Keywords", "Optimization Tips"]
    )
    
    analyze_btn = st.button("✨ Analyze Resume")
    
    st.markdown("---")
    st.markdown("### 🤖 Powered by")
    st.caption("Groq LLaMA 3.3 | Streamlit")

# --- Main Content Area ---
with col1:
    st.subheader("📝 Job Description")
    job_description = st.text_area("Paste the job description here...", height=400, placeholder="e.g., We are looking for a Senior Python Developer...")

with col2:
    st.subheader("📊 Analysis Results")
    
    if analyze_btn:
        if uploaded_file is not None and job_description:
            
            # Show a progress spinner
            with st.spinner("🤖 AI is analyzing your resume against the job description..."):
                try:
                    # 1. Extract Text
                    resume_text = extract_text_from_pdf(uploaded_file)
                    
                    # 2. Prepare Prompt
                    prompt = f"""
                    You are an expert ATS (Applicant Tracking System) Analyzer. 
                    Perform a comprehensive '{analysis_option}' on the following resume against the job description.
                    
                    RESUME TEXT:
                    {resume_text}
                    
                    JOB DESCRIPTION:
                    {job_description}
                    
                    OUTPUT GUIDELINES:
                    - Provide a professional, constructive tone.
                    - Use bullet points for readability.
                    - Highlight key missing skills specifically.
                    - Give a final 'Match Percentage' estimate (0-100%).
                    """
                    
                    # 3. Get AI Response
                    analysis_result = get_model_output(prompt)
                    
                    # 4. Display Result
                    st.success("Analysis Complete!")
                    st.markdown("### 📋 Detailed Report")
                    st.markdown(analysis_result)
                    
                    # 5. Download Button
                    st.download_button(
                        label="📥 Download Report as Text",
                        data=analysis_result,
                        file_name="resume_analysis.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            if not uploaded_file:
                st.warning("⚠️ Please upload a PDF resume.")
            if not job_description:
                st.warning("⚠️ Please paste a job description.")
    
    else:
        # Placeholder content when no analysis is running
        st.info("👈 Upload your resume and click 'Analyze Resume' to see insights here.")
        
        # Optional: Show resume preview if uploaded but not analyzed
        if uploaded_file:
            with st.expander("📄 View Extracted Resume Text"):
                st.text(extract_text_from_pdf(uploaded_file))