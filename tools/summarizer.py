from langchain.tools import Tool
from PyPDF2 import PdfReader
from openai import OpenAI
import os

def summarize_pdf_tool(path: str) -> str:
    try:
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"

        if len(text.strip()) == 0:
            return "The PDF appears to be empty or could not be parsed."

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize the following PDF text."},
                {"role": "user", "content": text[:12000]}  # Token limit
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Summarization Error: {e}"

summarize_pdf = Tool(
    name="summarizer_tool",
    func=summarize_pdf_tool,
    description="Use this tool when a user asks to summarize a PDF document. Input should be the path to the PDF file."
)
