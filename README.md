# 🛡️ Apertus Trust-VC: Sovereign Due Diligence

## The Problem
European Venture Capital (VC) firms, banks, and financial institutions handle highly confidential startup pitch decks and financial reports daily. Due to strict data sovereignty laws (GDPR) and corporate security policies, they **cannot** send these sensitive documents to US-based servers like OpenAI or Google for AI analysis.

## The Solution
**Apertus Trust-VC** is a sovereign, secure Due Diligence Agent designed to run entirely on **Apertus** (Switzerland’s open LLM). It allows VC analysts to upload confidential financial PDFs and instantly extract:
1. Financial Risks & Liabilities
2. Core Business Strengths
3. Critical Red Flags
All while ensuring zero data leakage outside of European/Swiss borders.

## Hackathon Architecture Note
*Due to the CSCS endpoint capacity being reached on Oct 6th, and pending HuggingFace credits during the final hours of the hackathon, this live prototype is temporarily proxied via an alternative open-weight model API. However, the architecture (built with LangChain) is fully designed to plug seamlessly into **Apertus 8B/70B** via HuggingFace Endpoints by simply swapping the LLM initialization line.*

## Tech Stack
- **Frontend:** Streamlit
- **Agent Logic:** LangChain
- **Document Parsing:** pypdf
- **Target LLM:** Apertus 8B/70B (Currently running in Proxy Mode)
