"""
Prompt engineering module for the AI-Powered Startup Idea Generator.
Constructs structured, highly contextual master prompts for the Groq API.
Designed for the National Incubation Center assignment by Aima Khan.
"""

from typing import List, Optional

SYSTEM_ROLE_PROMPT = (
    "You are an experienced startup strategist, product manager, business consultant, "
    "financial planner, and incubation mentor. Your task is to help early-stage founders "
    "transform real-world problems into practical, innovative, and financially considered "
    "startup opportunities."
)


def build_startup_prompt(
    problem_statement: str,
    industries: List[str],
    target_audience: Optional[str] = None,
    location: str = "Pakistan",
    budget: str = "PKR 500,000-1,000,000",
    startup_type: str = "Web Platform",
    founder_experience: str = "Beginner",
) -> str:
    """
    Constructs a comprehensive, context-aware prompt tailored to early-stage founders.

    Parameters:
        problem_statement (str): Real-world problem or pain point identified by the user.
        industries (List[str]): List of selected industry sectors/themes.
        target_audience (str, optional): Target customer base or user demographics.
        location (str): Operational geography/market (e.g., Pakistan).
        budget (str): Available initial capital/budget tier.
        startup_type (str): Format of solution (e.g., SaaS, Mobile App, AI Product).
        founder_experience (str): Founder background (Beginner, Intermediate, Experienced).

    Returns:
        str: Fully formatted master prompt instructing the AI to generate a 21-section startup plan.
    """
    # Clean and format input data
    industries_str = ", ".join(industries) if industries else "General / Cross-Industry"
    audience_str = target_audience.strip() if target_audience and target_audience.strip() else "Identified prospective end-users"
    loc_str = location.strip() if location and location.strip() else "Pakistan"

    prompt = f"""You are advising an early-stage founder presenting to an incubation review committee at the National Incubation Center.

### FOUNDER CONTEXT & PARAMETERS:
- **Identified Problem Statement:** {problem_statement.strip()}
- **Target Industries / Themes:** {industries_str}
- **Primary Target Audience:** {audience_str}
- **Geographic Location / Target Market:** {loc_str}
- **Available Starting Budget:** {budget}
- **Proposed Startup Type:** {startup_type}
- **Founder Experience Level:** {founder_experience}

---

### INSTRUCTIONS & QUALITY GUIDELINES:
1. **Contextual Tailoring:** Deeply ground every recommendation in the founder's specific location ({loc_str}), budget tier ({budget}), and experience level ({founder_experience}).
2. **Pragmatic Feasibility:** Prioritize realistic execution over buzzwords. If the budget is limited, suggest lean tools, bootstrap strategies, and no-code/low-code or open-source tech stacks.
3. **No Fabricated Statistics:** Never invent fake citations or unverified market share numbers. State assumptions transparently.
4. **Illustrative Financials:** All financial figures must be clearly marked as illustrative estimates and calculations tailored to {loc_str}'s economic reality.
5. **No Profitability Guarantees:** Present honest break-even scenarios and acknowledge risks upfront.
6. **Incubation Focus:** Prepare the founder to pitch confidently to incubators like the National Incubation Center (NIC).

---

### REQUIRED 21-SECTION STARTUP BUSINESS PLAN:
Generate a complete, comprehensive, and well-structured business plan covering every single section listed below. Use clear Markdown headings (e.g. `### 1. Executive Summary`), bullet points, and tables.

### 1. Executive Summary
Provide a high-level summary of the venture, the market urgency, proposed value, and expected impact.

### 2. Startup Name and Tagline
Suggest 3 catchy, memorable names with rationale, an impactful tagline, and clear brand positioning tailored to {loc_str}.

### 3. Problem Statement
Deconstruct the problem: who suffers from it, current broken workarounds, economic/emotional costs, and why now is the time to solve it.

### 4. Proposed Solution
Explain the core product/service, how it directly solves the identified problem, and the primary benefit delivered to customers.

### 5. Product Description
Walk through the user journey, core workflow, and key customer touchpoints from discovery to recurring usage.

### 6. Target Market and Customer Personas
Define 2 detailed buyer personas (Demographics, Goals, Pain Points, Willingness to Pay) within {audience_str} in {loc_str}.

### 7. Market Opportunity
Analyze the addressable market potential (TAM, SAM, SOM) conceptually with clear underlying assumptions. Do not fabricate unverified statistics.

### 8. Competitor Analysis
Analyze direct and indirect alternatives currently used in {loc_str}. Highlight key differentiation axes. Label unverified or hypothetical data clearly.

### 9. Unique Value Proposition (UVP)
State a crisp, compelling UVP formula: "We help [Target Audience] achieve [Desired Outcome] without [Primary Pain Point]."

### 10. Business Model
Detail primary and secondary revenue streams (e.g., subscriptions, commission, freemium, licensing, pay-per-use).

### 11. Pricing Strategy
Propose initial pricing tiers appropriate for {loc_str}'s purchasing power and the target audience's budget elasticity.

### 12. Minimum Viable Product (MVP)
Define the smallest version of the product that can be tested in week 1-4. List strictly essential features vs. "nice-to-have" features to cut scope.

### 13. Core Features and Technology Stack
Recommend a realistic, modern, and cost-effective tech stack suitable for a {founder_experience} founder building a {startup_type} within {budget}.

### 14. Marketing and Customer Acquisition
Outline 4 low-cost, guerrilla marketing and digital acquisition tactics to acquire the first 100 paying customers in {loc_str}.

### 15. Financial Plan
Provide an illustrative 12-month financial breakdown (in {loc_str} currency if appropriate, e.g., PKR):
- Estimated Initial Setup Costs (within {budget})
- Estimated Monthly Operating Expenses (burn rate)
- Estimated Revenue Scenarios (Conservative, Moderate, Aggressive)

### 16. Break-Even Analysis
Explain the estimated break-even point in units or subscribers, detailing unit economics (CAC, LTV, Contribution Margin) and key assumptions.

### 17. 30-Day, 60-Day, and 90-Day Roadmap
Present actionable execution milestones in a clean Markdown table with columns:
| Phase | Duration | Key Milestones & Deliverables | Measurable KPIs |

### 18. Risks and Mitigation
Detail 4 primary risk categories (Market Risk, Technical/Operational Risk, Financial/Cash-flow Risk, Regulatory Risk) with proactive mitigation tactics.

### 19. Customer Validation Strategy
Design an experiment plan: 5 key interview questions to ask potential customers, target survey metrics, and measurable go/no-go criteria.

### 20. Funding and Incubation Opportunities
Recommend relevant early-stage incubation programs (such as National Incubation Center / NIC cohorts), grants, or angel networks applicable in {loc_str}. Outline realistic evaluation criteria.

### 21. Elevator Pitch
Provide a punchy, 60-second pitch script formatted for an incubation committee demo day.

---
Deliver a polished, professional, and directly actionable startup plan now.
"""
    return prompt
