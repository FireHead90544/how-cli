from how.core.prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES
from how.core.parser import PARSER
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

example_template = ChatPromptTemplate.from_messages([
    ("human", "How to {task}?"),
    ("ai", "{output}")
])

few_shot_examples_template = FewShotChatMessagePromptTemplate(
    example_prompt=example_template,
    examples=FEW_SHOT_EXAMPLES
)

PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT + "\n{format_instructions}"),
    few_shot_examples_template,
    ("human", "How to {task}?")
]).partial(format_instructions=PARSER.get_format_instructions())