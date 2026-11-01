"""
Home.py - Landing Page for AI-Powered Startup Idea Generator
Client: National Incubation Center
Developer: Aima Khan
Technology: Python, Streamlit, Groq API
"""

import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Startup Idea Generator | National Incubation Center",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. National Incubation Center Brand Palette & Styling
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

div.stButton > button {
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

div.stButton > button:hover {
    background-color: #5d101a !important;
    border-color: #5d101a !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(71, 10, 17, 0.35) !important;
    color: var(--warm-champagne) !important;
}

.hero-container {
    background: linear-gradient(135deg, var(--forest-green) 0%, #1e3022 100%);
    border-radius: 16px;
    padding: 3rem 2.5rem;
    color: var(--white);
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 30px rgba(47, 72, 52, 0.15);
    border: 1px solid rgba(230, 217, 168, 0.2);
}

.hero-badge {
    display: inline-block;
    background-color: rgba(230, 217, 168, 0.18);
    color: var(--warm-champagne);
    font-size: 0.85rem;
    font-weight: 600;
    padding: 0.35rem 0.85rem;
    border-radius: 20px;
    border: 1px solid rgba(230, 217, 168, 0.4);
    margin-bottom: 1rem;
    text-transform: uppercase;
}

.hero-title {
    font-size: 2.7rem;
    font-weight: 800;
    color: var(--white) !important;
    margin-bottom: 1rem;
    line-height: 1.15;
}

.hero-subtitle {
    font-size: 1.15rem;
    color: #e3ebdf !important;
    max-width: 800px;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.feature-card {
    background-color: var(--white);
    border-radius: 12px;
    padding: 1.75rem 1.5rem;
    height: 100%;
    border-top: 4px solid var(--forest-green);
    border-left: 1px solid #e8eae4;
    border-right: 1px solid #e8eae4;
    border-bottom: 1px solid #e8eae4;
    box-shadow: 0 4px 20px rgba(47, 72, 52, 0.08);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(47, 72, 52, 0.15);
    border-top-color: var(--deep-burgundy);
}

.feature-icon-wrapper {
    width: 48px;
    height: 48px;
    border-radius: 10px;
    background-color: #eaf0eb;
    color: var(--forest-green);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    margin-bottom: 1rem;
}

.feature-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--forest-green);
    margin-bottom: 0.5rem;
}

.feature-desc {
    color: #555555;
    font-size: 0.95rem;
    line-height: 1.5;
}

.step-card {
    background: var(--white);
    border: 1px solid #e3e6de;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    height: 100%;
}

.step-number {
    width: 36px;
    height: 36px;
    background-color: var(--warm-champagne);
    color: var(--forest-green);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 1rem;
    margin: 0 auto 0.75rem auto;
    border: 2px solid var(--forest-green);
}

.step-title {
    font-weight: 700;
    font-size: 1.1rem;
    color: var(--forest-green);
    margin-bottom: 0.4rem;
}

.step-desc {
    font-size: 0.9rem;
    color: #595959;
    line-height: 1.45;
}

.user-chip {
    display: inline-block;
    background-color: #eaf1eb;
    color: var(--forest-green);
    border: 1px solid #c9d8cc;
    border-radius: 20px;
    padding: 0.4rem 1rem;
    font-size: 0.92rem;
    font-weight: 600;
    margin: 0.3rem 0.3rem;
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

# 3. Sidebar Branding & Info
with st.sidebar:
    st.markdown("### 🏛️ NIC Innovation Hub")
    st.markdown(
        "Welcome to the **National Incubation Center** AI-Powered Startup Idea Generator. "
        "Empowering Pakistani founders with data-backed, market-tailored venture plans."
    )
    st.divider()
    st.markdown("#### ⚡ Quick Navigation")
    if st.button("🚀 Open Idea Generator", use_container_width=True, key="sidebar_nav_btn"):
        st.switch_page("pages/1_Startup_Idea_Generator.py")
    
    st.markdown("---")
    st.caption("📌 **Assignment:** Generative AI for NIC\n\n👩‍💻 **Author:** Aima Khan")

# 4. Hero Section
hero_html = """
<div class="hero-container">
    <div class="hero-badge">National Incubation Center • GenAI Venture Studio</div>
    <h1 class="hero-title">Turn Your Ideas Into Startups</h1>
    <p class="hero-subtitle">
        Transform real-world problems into actionable startup business plans with Generative AI. 
        Explore business opportunities, validate your ideas, and create a practical roadmap 
        for your entrepreneurial journey.
    </p>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# Call-to-action button
col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
with col_cta2:
    if st.button("Start Building Your Startup ➔", use_container_width=True, key="hero_cta_btn"):
        st.switch_page("pages/1_Startup_Idea_Generator.py")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Feature Cards Section
st.markdown("## 🌟 Key Capabilities")
st.markdown("Designed specifically to bridge the gap between an early idea and a pitch-ready incubation plan.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon-wrapper">🔍</div>
            <div class="feature-title">Discover Startup Opportunities</div>
            <div class="feature-desc">
                Turn real-world problems into potential business opportunities with targeted validation angles.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon-wrapper">📊</div>
            <div class="feature-title">AI-Powered Business Plans</div>
            <div class="feature-desc">
                Generate structured plans tailored to your market, budget, and target audience across 21 strategic sections.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon-wrapper">🎯</div>
            <div class="feature-title">90-Day Execution Roadmap</div>
            <div class="feature-desc">
                Get actionable milestones to help validate and develop your startup with realistic timelines and metrics.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br><hr style='border-color: #dbe2d8;'><br>", unsafe_allow_html=True)

# 6. How It Works Section
st.markdown("## 🧭 How It Works")
st.markdown("A seamless 3-step structured journey from problem discovery to comprehensive business architecture.")

step_col1, step_col2, step_col3 = st.columns(3)

with step_col1:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">1</div>
            <div class="step-title">Describe Your Problem</div>
            <div class="step-desc">
                Users enter a problem, opportunity, or startup theme they have observed in their daily life or industry.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with step_col2:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">2</div>
            <div class="step-title">Customize Your Idea</div>
            <div class="step-desc">
                Users select their industry, target audience, location, and budget to align constraints with execution reality.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with step_col3:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">3</div>
            <div class="step-title">Generate Your Plan</div>
            <div class="step-desc">
                The Groq API generates a tailored startup business plan ready for incubation review and investor pitching.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br><hr style='border-color: #dbe2d8;'><br>", unsafe_allow_html=True)

# 7. Who Can Use It Section
st.markdown("## 👥 Who Can Use It?")
st.markdown("Built for innovators at any point along their venture creation pathway:")

audience_chips = [
    "🎓 Students",
    "🚀 Aspiring Entrepreneurs",
    "💡 Early-Stage Founders",
    "🔬 Innovators & Researchers",
    "🏪 Small Business Owners",
]

chip_html = "".join([f'<span class="user-chip">{item}</span>' for item in audience_chips])
st.markdown(f'<div style="margin-top: 0.5rem; margin-bottom: 1.5rem;">{chip_html}</div>', unsafe_allow_html=True)

st.info(
    "💡 **Pro-Tip for NIC Applicants:** Prepare your real-world observations beforehand. "
    "The more specific your problem statement, the sharper and more realistic your business model will be."
)

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
