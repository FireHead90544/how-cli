import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GRPC_VERBOSITY"] = "NONE"

LLM_PROVIDERS = {
    "Gemini": { "provider": ChatGoogleGenerativeAI, "model": "gemini-1.5-flash" },
}
