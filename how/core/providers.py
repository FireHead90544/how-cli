import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_vertexai import ChatVertexAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

os.environ["GRPC_VERBOSITY"] = "NONE"

LLM_PROVIDERS = {
    "GoogleGenAI": { "provider": ChatGoogleGenerativeAI, "model": "gemini-1.5-flash" },
    "GoogleVertexAI": { "provider": ChatVertexAI, "model": "gemini-1.5-flash" },
    "GroqMistralAI": { "provider": ChatGroq, "model": "mixtral-8x7b-32768" },
    "GroqLLaMa": { "provider": ChatGroq, "model": "llama3-70b-8192" },
    "OpenAI": { "provider": ChatOpenAI, "model": "gpt-4o" },
    "Anthropic": { "provider": ChatAnthropic, "model": "claude-3-5-sonnet-20240620" }
}
