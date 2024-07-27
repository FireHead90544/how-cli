from how.core.config import Config
from how.core.providers import LLM_PROVIDERS

llm_config = Config().values

LLM = LLM_PROVIDERS.get(llm_config.get("provider"))['provider'](
    model = LLM_PROVIDERS.get(llm_config.get("provider"))['model'],
    api_key = llm_config.get("api_key")
)