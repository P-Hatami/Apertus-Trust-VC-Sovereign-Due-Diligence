import streamlit as st
from pypdf import PdfReader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

# TODO: Replace with HuggingFaceEndpoint and Apertus 8B when credits arrive
# Get a free API key from console.groq.com for immediate testing
os.environ["GROQ_API_KEY"] = "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"


def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# UI Configuration
st.set_page_config(page_title="Apertus Trust-VC", layout="wide")
st.title("🛡️ Apertus Trust-VC: Sovereign Due Diligence")
st.markdown(
    "Secure, localized financial document analysis for European Venture Capital firms ensuring strict data sovereignty.")

# File Upload Section
uploaded_file = st.file_uploader("Upload Pitch Deck or Financial Report (PDF)", type="pdf")

if uploaded_file is not None:
    st.info("File uploaded successfully. Extracting text...")
    document_text = extract_text_from_pdf(uploaded_file)

    # Limit text for initial testing
    short_text = document_text[:6000]

    st.write("✔️ Data ready for LLM analysis.")

    if st.button("Run Due Diligence Analysis"):
        with st.spinner("Processing document..."):
            llm = ChatGroq(model_name="openai/gpt-oss-120b", temperature=0.2)

            # Prompt Engineering
            prompt = PromptTemplate.from_template("""
            You are an expert Venture Capital analyst. Read the following excerpt from a startup's pitch deck or financial report.
            Based strictly on the provided text, extract and summarize the following in professional bullet points:
            1. Financial Risks & Liabilities
            2. Core Business Strengths
            3. Critical Red Flags (if any)

            Text to analyze:
            {text}
            """)

            # Execute Chain
            chain = prompt | llm
            response = chain.invoke({"text": short_text})

            # Display Output
            st.success("Analysis complete:")
            st.write(response.content)
