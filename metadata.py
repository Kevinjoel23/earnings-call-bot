from langchain.llms import OpenAI 
from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate
from secret_key import openai_api_key

llm = OpenAI(temperature=0.5, openai_api_key=openai_api_key)
prompt_template_metadata = PromptTemplate(
    input_variables=['transcript'],
    template= """
    Following is the transcript of an earnings call report:
    {transcript}
    Generate a structured output for the given transcript using the GPT-3.5 API. 
    Please format the ouput as in markdown:

    Company name: [Company Name] \n\n
    Quarter: [Quarter] \n\n
    Conference Call date: [Conference Call Date] \n\n
    Number of pages in transcript: [Number of Pages] \n\n
    Management info: [Create a table in Markdown with columns for Name and Designation. Include only employees who have a designation in the company.]
    """
    )

def transcript_metadata(text):
    chain = LLMChain(llm=llm, prompt=prompt_template_metadata)
    response = chain.run(text)
    return response 
