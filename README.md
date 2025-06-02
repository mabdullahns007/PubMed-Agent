# PubMed Research Agent 🧬

An intelligent biomedical research assistant powered by Google's ADK Agents framework and Gemini 2.0 Flash, designed to make scientific literature search and analysis more efficient and accessible.

## 🚀 Overview

The PubMed Research Agent is an AI-powered tool that helps healthcare professionals, researchers, and students quickly find, analyze, and understand biomedical research from PubMed's extensive database of 35+ million citations. Instead of spending hours manually searching through papers, users can get evidence-based answers with proper citations in seconds.

## ✨ Features

- **🔍 Intelligent Query Processing**: Automatically breaks down complex medical questions into key search terms
- **📚 Comprehensive PubMed Search**: Searches through millions of biomedical papers and clinical trials
- **📊 Comparative Analysis**: Performs head-to-head comparisons between treatments and interventions
- **📖 Smart Summarization**: Analyzes and summarizes research findings in an accessible format
- **📝 Proper Citations**: Provides accurate citations for all referenced sources
- **🔬 Evidence-Based Focus**: Prioritizes recent, high-quality evidence and meta-analyses

## 🛠️ Technology Stack

- **Google ADK Agents**: Core agent framework
- **Gemini 2.0 Flash**: Advanced language model for analysis and reasoning
- **LangChain**: Tool integration and orchestration
- **PubMed API**: Access to biomedical literature database

## 📋 Prerequisites

Before running the PubMed Agent, ensure you have:

- Python 3.8 or higher
- Google ADK account and API access
- Required Python packages (see Installation)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/mabdullahns007/PubMed-Agent.git
cd PubMed-Agent
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
pip install xmltodict
```

3. Set up your GOOGLE API KEY
```bash
$env:GOOGLE_API_KEY="YOUR API KEY"
```
4. Run
```bash
adk web
```
![Capture](https://github.com/user-attachments/assets/2010b467-1876-4da2-bd39-8d334c5788c0)


## 💡 Use Cases

### For Healthcare Professionals
- Quick evidence-based treatment comparisons
- Latest clinical guidelines and recommendations
- Safety profiles and side effects research

### For Researchers
- Literature reviews and meta-analysis preparation
- Finding gaps in current research
- Staying updated with recent publications

### For Students
- Understanding complex medical concepts
- Finding credible sources for assignments
- Learning about disease mechanisms and treatments

## 🔍 How It Works

1. **Query Analysis**: The agent processes your question and identifies key medical terms
2. **PubMed Search**: Performs targeted searches using optimized queries
3. **Result Processing**: Analyzes retrieved papers for relevance and quality
4. **Evidence Synthesis**: Summarizes findings and identifies key insights
5. **Citation Generation**: Provides proper academic citations for all sources

## 📊 Configuration

The agent can be customized with different parameters:

```python
pubmed_query_runner = PubmedQueryRun(
    max_results=20,    # Maximum papers to retrieve
    top_k_results=10   # Top results to analyze in detail
)
```


## 🙏 Acknowledgments

- Google ADK team for the powerful agents framework
- LangChain community for excellent tool integrations
- PubMed/NCBI for providing access to biomedical literature
- The open-source community for inspiration and support

## ⚠️ Disclaimer

This tool is designed to assist with research and information gathering. Always consult qualified healthcare professionals for medical advice. The agent's responses should not be considered as medical recommendations or replace professional medical consultation.

---

⭐ **If you find this project helpful, please consider giving it a star!** ⭐
