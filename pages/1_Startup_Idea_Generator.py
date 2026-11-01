"""
1_Startup_Idea_Generator.py - Interactive Generator Workspace
Client: National Incubation Center
Developer: Aima Khan
Technology: Python, Streamlit, Groq API (llama-3.3-70b-versatile)
"""

import os
from datetime import datetime
from typing import Optional, Tuple
import streamlit as st
from groq import Groq, AuthenticationError, APIConnectionError, RateLimitError, APIStatusError

from utils.prompts import build_startup_prompt, SYSTEM_ROLE_PROMPT

# Configurable Groq Models
DEFAULT_GROQ_MODEL = "openai/gpt-oss-120b"
FALLBACK_GROQ_MODEL = "llama-3.1-8b-instant"

# 1. Page Configuration
st.set_page_config(
    page_title="Startup Generator | National Incubation Center",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. National Incubation Center Theme CSS
CUSTOM_CSS = """
<style>
:root {
    --forest-green: #2F4834;
    --warm-champagne: #E6D9A8;
    --deep-burgundy: #470A11;
    --warm-off-white: #F8F6F0;
    --charcoal: #242424;
    --white: #FFFFFF;
}

.stApp {
    background-color: var(--warm-off-white);
    color: var(--charcoal);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    color: var(--forest-green) !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

div.stButton > button, div.stDownloadButton > button {
    background-color: var(--deep-burgundy) !important;
    color: var(--white) !important;
    border: 1px solid var(--deep-burgundy) !important;
    border-radius: 8px !important;
    padding: 0.65rem 1.75rem !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    box-shadow: 0 2px 8px rgba(71, 10, 17, 0.25) !important;
    transition: all 0.25s ease-in-out !important;
}

div.stButton > button:hover, div.stDownloadButton > button:hover {
    background-color: #5d101a !important;
    border-color: #5d101a !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(71, 10, 17, 0.35) !important;
    color: var(--warm-champagne) !important;
}

div[data-testid="stForm"] {
    background-color: var(--white);
    padding: 2rem;
    border-radius: 14px;
    border: 1px solid #e1e6de;
    box-shadow: 0 4px 20px rgba(47, 72, 52, 0.08);
}

.plan-container {
    background-color: var(--white);
    border-radius: 14px;
    padding: 2.5rem;
    border: 1px solid #dce2d8;
    box-shadow: 0 6px 25px rgba(47, 72, 52, 0.08);
    margin-top: 2rem;
    line-height: 1.7;
}

.app-footer {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem 1rem;
    margin-top: 3.5rem;
    border-top: 1px solid #dbe2d8;
    color: var(--forest-green);
    font-size: 0.95rem;
    font-weight: 600;
    letter-spacing: 0.02em;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def get_groq_api_key() -> Optional[str]:
    """Retrieves Groq API key securely from Streamlit secrets or environment."""
    try:
        if "GROQ_API_KEY" in st.secrets and st.secrets["GROQ_API_KEY"]:
            key = st.secrets["GROQ_API_KEY"].strip()
            if key and not key.startswith("gsk_your_") and key != "your_actual_groq_api_key":
                return key
    except Exception:
        pass

    env_key = os.environ.get("GROQ_API_KEY", "").strip()
    if env_key and not env_key.startswith("gsk_your_") and env_key != "your_actual_groq_api_key":
        return env_key

    return None


def generate_startup_plan(
    user_prompt: str,
    model: str = DEFAULT_GROQ_MODEL,
    temperature: float = 0.7,
    max_tokens: int = 5000,
) -> Tuple[bool, str]:
    """Executes a chat completion call to the Groq API."""
    api_key = get_groq_api_key()

    if not api_key:
        error_msg = (
            "**Groq API Key Not Found or Not Configured.**\n\n"
            "To generate live startup plans with AI, please configure your Groq API key:\n\n"
            "1. **Local Development:** Create `.streamlit/secrets.toml` in your project folder with:\n"
            "   ```toml\n"
            '   GROQ_API_KEY = "gsk_your_actual_groq_api_key"\n'
            "   ```\n"
            "2. **Streamlit Cloud Deployment:** Add `GROQ_API_KEY` under your App Settings > Secrets.\n"
            "3. **Get Free Key:** Create an account at [console.groq.com](https://console.groq.com/keys) to generate your key."
        )
        return False, error_msg

    try:
        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_ROLE_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        if chat_completion.choices and len(chat_completion.choices) > 0:
            result_text = chat_completion.choices[0].message.content
            if result_text:
                return True, result_text
            return False, "The Groq API returned an empty response. Please try submitting again."
        return False, "No completion choices were returned by the AI model."

    except AuthenticationError:
        return False, (
            "**Authentication Error:** The provided Groq API key is invalid or expired. "
            "Please check `.streamlit/secrets.toml` and ensure your key starts with `gsk_`."
        )
    except RateLimitError:
        return False, (
            "**Rate Limit Reached:** Groq API rate limit reached for your current tier. "
            "Please wait a few moments before trying again, or switch to a lighter model."
        )
    except APIConnectionError:
        return False, (
            "**Connection Error:** Could not connect to Groq API servers. "
            "Please check your internet connection and verify that `api.groq.com` is accessible."
        )
    except APIStatusError as e:
        return False, f"**Groq API Error (Status {e.status_code}):** {e.message}"
    except Exception as e:
        return False, f"**Unexpected Error:** An error occurred while generating your plan: {str(e)}"


# 3. Sidebar Controls & Info
with st.sidebar:
    st.markdown("### 🏛️ NIC Innovation Hub")
    st.markdown("Crafting incubator-ready startup concepts tailored for Pakistani and global markets.")
    
    st.divider()
    st.markdown("#### ⚙️ Engine Settings")
    
    selected_model = st.selectbox(
        "Groq Model",
        options=[DEFAULT_GROQ_MODEL, FALLBACK_GROQ_MODEL],
        index=0,
        help="llama-3.3-70b-versatile offers state-of-the-art strategic reasoning for comprehensive business plans.",
    )
    
    api_key_status = get_groq_api_key()
    if api_key_status:
        st.success("🟢 Groq API Key: Configured")
    else:
        st.warning("🟡 Groq API Key: Missing / Default")
        with st.expander("🔑 How to set your key"):
            st.markdown(
                "Create a `.streamlit/secrets.toml` file in the project folder:\n"
                "```toml\n"
                'GROQ_API_KEY = "gsk_your_key_here"\n'
                "```\n"
                "Or configure it in Streamlit Cloud Secrets."
            )
    
    st.divider()
    if st.button("⬅️ Back to Landing Page", use_container_width=True):
        st.switch_page("Home.py")
        
    st.markdown("---")
    st.caption("📌 **Assignment:** Generative AI for NIC\n\n👩‍💻 **Author:** Aima Khan")

# 4. Header Section
st.markdown("## Build Your Startup From Scratch")
st.markdown(
    "Describe the problem you want to solve and let AI help you turn it into an actionable business plan."
)
st.markdown("<hr style='border-color: #dbe2d8;'>", unsafe_allow_html=True)

# 5. Interactive Form Component
with st.form("startup_generator_form"):
    st.markdown("#### 1️⃣ Problem Identification *(Required)*")
    problem_statement = st.text_area(
        "Problem Statement",
        placeholder=(
            "Describe a real-world problem, inefficiency, or pain point you have observed...\n"
            "Example: Small neighbourhood grocery stores (Kiryanas) in Pakistan face cash-flow shortages "
            "and cannot access traditional bank credit because they lack digital transaction records."
        ),
        height=140,
        help="Be as specific as possible. Mention who faces the issue and how they currently struggle.",
    )

    st.markdown("#### 2️⃣ Industry & Venture Architecture")
    col_ind1, col_ind2 = st.columns(2)
    
    with col_ind1:
        # FIELD B: INDUSTRY AND THEMES (13 exact options)
        industry_options = [
            "Artificial Intelligence",
            "Healthcare",
            "Education",
            "Agriculture",
            "FinTech",
            "E-commerce",
            "ClimateTech",
            "SaaS",
            "Logistics",
            "Cybersecurity",
            "Retail",
            "Smart Cities",
            "Social Impact",
        ]
        selected_industries = st.multiselect(
            "Industry and Themes",
            options=industry_options,
            default=["FinTech", "Retail"],
            help="Select one or more sectors relevant to your startup idea.",
        )
        
        # FIELD C: TARGET AUDIENCE
        target_audience = st.text_input(
            "Target Audience (Optional)",
            placeholder="e.g. Small retailers, university students, hospitals, or local businesses",
            help="Specify the primary customers or users you plan to serve first.",
        )

        # FIELD D: LOCATION (Default: Pakistan)
        location = st.text_input(
            "Location / Market",
            value="Pakistan",
            help="The geographic market where the startup will initially launch and validate.",
        )

    with col_ind2:
        # FIELD E: AVAILABLE BUDGET
        budget_options = [
            "Under PKR 100,000",
            "PKR 100,000-500,000",
            "PKR 500,000-1,000,000",
            "PKR 1,000,000-5,000,000",
            "More than PKR 5,000,000",
            "Not decided yet",
        ]
        selected_budget = st.selectbox(
            "Available Budget",
            options=budget_options,
            index=1,
            help="Helps the AI propose a realistic, bootstrap-friendly MVP and tech stack.",
        )

        # FIELD F: STARTUP TYPE
        startup_type_options = [
            "SaaS",
            "Mobile App",
            "Web Platform",
            "AI Product",
            "Marketplace",
            "Service Business",
            "Hardware/IoT",
            "Open to Suggestions",
        ]
        selected_type = st.selectbox(
            "Startup Type",
            options=startup_type_options,
            index=2,
            help="The structural delivery medium of your proposed solution.",
        )

        # FIELD G: FOUNDER EXPERIENCE
        experience_options = [
            "Beginner",
            "Intermediate",
            "Experienced",
        ]
        selected_experience = st.selectbox(
            "Founder Experience",
            options=experience_options,
            index=0,
            help="Tailors the roadmap and technical complexity to your background.",
        )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Primary Submission Button in Deep Burgundy
    submit_button = st.form_submit_button(
        "Generate My Startup Plan ➔",
        use_container_width=True,
    )

# 6. Form Submission & Generation Logic
if submit_button:
    if not problem_statement.strip():
        st.error("⚠️ **Validation Error:** Please provide a Problem Statement before generating a plan. Real-world validation starts with a clear problem definition!")
    elif len(problem_statement.strip()) < 15:
        st.warning("⚠️ **Input Too Brief:** Please describe your problem in at least a sentence so the AI has sufficient context to analyze.")
    else:
        master_prompt = build_startup_prompt(
            problem_statement=problem_statement,
            industries=selected_industries,
            target_audience=target_audience,
            location=location,
            budget=selected_budget,
            startup_type=selected_type,
            founder_experience=selected_experience,
        )

        with st.spinner("🔍 Analyzing your startup opportunity and generating your 21-section incubation plan..."):
            success, result = generate_startup_plan(
                user_prompt=master_prompt,
                model=selected_model,
                temperature=0.7,
                max_tokens=6000,
            )

        if success:
            st.session_state["generated_plan"] = result
            st.session_state["plan_meta"] = {
                "problem": problem_statement[:60] + "...",
                "location": location,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            st.success("🎉 **Success!** Your initial startup business plan has been generated.")
        else:
            st.error(result)

# 7. Render Plan Output & Download Options from Session State
if "generated_plan" in st.session_state and st.session_state["generated_plan"]:
    st.markdown("<br><hr style='border-color: #dbe2d8;'><br>", unsafe_allow_html=True)
    
    meta = st.session_state.get("plan_meta", {})
    col_out_hdr, col_dl = st.columns([3, 1])
    
    with col_out_hdr:
        st.markdown("### 📋 Generated Startup Business Plan")
        if meta:
            st.caption(f"Generated on {meta.get('timestamp')} for market: **{meta.get('location')}**")
            
    with col_dl:
        clean_timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"startup_plan_{clean_timestamp}.md"
        st.download_button(
            label="📥 Download Plan (.md)",
            data=st.session_state["generated_plan"],
            file_name=filename,
            mime="text/markdown",
            use_container_width=True,
            help="Download the complete business plan in Markdown format for offline editing or sharing.",
        )

    st.markdown('<div class="plan-container">', unsafe_allow_html=True)
    st.markdown(st.session_state["generated_plan"])
    st.markdown('</div>', unsafe_allow_html=True)

# 8. Mandatory Developer Credit Footer
st.markdown(
    """
    <div class="app-footer">
        Developed by Aima Khan | Generative AI Project
        <div style="font-size: 0.8rem; color: #667568; margin-top: 0.3rem; font-weight: 400;">
            National Incubation Center • Empowering Next-Generation Pakistani Founders
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
