# 🚀 AI-Powered Startup Idea Generator

> **National Incubation Center (NIC) — Generative AI Innovation Studio**  
> **Assignment Project**  
> **Developer:** Aima Khan  
> **Status:** Completed & Tested Locally  

---

## 📌 Executive Summary & Context

The **AI-Powered Startup Idea Generator** is a specialized Generative AI web application designed for the **National Incubation Center (NIC)**. It bridges the gap between early-stage problem observation and rigorous venture incubation by converting everyday real-world pain points into comprehensive, 21-section startup business plans.

Powered by **Streamlit** and the **Groq API** (running high-speed inference on `llama-3.3-70b-versatile`), this application allows students, aspiring entrepreneurs, and early-stage founders to validate assumptions, assess market opportunities, structure Lean MVPs, and generate actionable 90-day execution roadmaps.

---

## 🎨 Brand Design & Aesthetic Philosophy

The application features an incubation-grade editorial aesthetic avoiding generic AI blue-and-purple gradients. It uses the NIC-inspired palette:

| Role | Color Name | Hex Code | Purpose |
| :--- | :--- | :--- | :--- |
| **Primary Brand** | Forest Green | `#2F4834` | Main brand identity, headers, card borders, and icons |
| **Accent / Highlight** | Warm Champagne | `#E6D9A8` | Highlights, badges, step indicators, and warmth |
| **Primary CTA** | Deep Burgundy | `#470A11` | Action buttons, submission triggers, and focus elements |
| **Base Surface** | Warm Off-White | `#F8F6F0` | Soft background surface reducing eye strain |
| **Text Primary** | Charcoal | `#242424` | Crisp, high-contrast, accessible typography |
| **Container Surface** | Pure White | `#FFFFFF` | Card bodies, form containers, and plan outputs |

---

## 📂 Exact Project Structure

```text
startup-idea-generator/
├── Home.py                             # Landing Page & Multipage Entry Point
├── pages/
│   └── 1_Startup_Idea_Generator.py     # Interactive Generation Workspace
├── utils/
│   ├── __init__.py                     # Package export (empty Python source file)
│   └── prompts.py                      # Master prompt engineering & 21-section template
├── .streamlit/
│   └── secrets.toml.example            # Template for local API key configuration
├── requirements.txt                    # Minimal, pinned dependencies
├── .gitignore                          # Protects keys, environments, and caches
└── README.md                           # Complete project documentation
```

---

## 🛠️ Technology Stack

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/) (v1.35+)
- **LLM Engine & Inference Provider:** [Groq Cloud](https://console.groq.com/) using official `groq` SDK
- **Language Models Supported:** 
  - `llama-3.3-70b-versatile` (Default, strategic reasoning)
  - `llama-3.1-8b-instant` (High-speed fallback)
- **Language:** Python 3.10+ / 3.12+

---

## 🚀 Running The Application

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Groq API Key
1. Get a free API key from [Groq Console](https://console.groq.com/keys).
2. Create `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
   ```

### 3. Launch App
```bash
streamlit run Home.py
```
Open your browser at `http://localhost:8501`.

---

## 👩‍💻 Credits & Academic Integrity

Developed by **Aima Khan** as part of the Generative AI venture studio assignment for the **National Incubation Center (NIC)**.
