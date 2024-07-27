from how.core.schema import Result
from langchain_core.output_parsers import JsonOutputParser

PARSER = JsonOutputParser(pydantic_object=Result)