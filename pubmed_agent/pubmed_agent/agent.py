from google.adk.agents import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from google.genai import types

def pubmed_search_tool(query: str) -> dict:
    """
    Performs a PubMed search for the given query and returns citations.
    Ensure that the environment for PubmedQueryRun is correctly set up.
    """
    try:
        pubmed_query_runner = PubmedQueryRun(
            max_results=20,
            top_k_results=10
        )
        result = pubmed_query_runner.run(query)
        # Ensure the result is JSON-serializable
        return {"status": "success", "result": result}
    except Exception as e:
        print(f"Error during PubMed query: {e}")
        return {"status": "error", "result": f"An error occurred while querying PubMed: {str(e)}"}

# Create the root agent
root_agent = Agent(
    name="pubmed_research_agent",
    model="gemini-2.0-flash",
    description="An AI agent that helps users find and understand biomedical research from PubMed.",
    instruction="""I am a biomedical research assistant that helps find and analyze scientific literature from PubMed.
    
    When you ask a question:
    1. I will break down your query into key medical terms
    2. Search PubMed for relevant papers and clinical trials
    3. Analyze and summarize the findings
    4. Provide citations for the sources
    
    For comparative questions (like comparing treatments):
    - I will search for each treatment separately
    - Look for head-to-head trials and meta-analyses
    - Compare safety and efficacy data
    - Focus on recent evidence when specified
    
    I will provide clear, evidence-based answers with proper citations.""",
    tools=[pubmed_search_tool]  # Using only the PubMed search tool
) 