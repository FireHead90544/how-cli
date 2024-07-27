import warnings
from how.core.chains import HOW_CLI_CHAIN
from how.core.parser import PARSER

def get_result(task: str) -> dict[str, str | list | float]:
    """Invokes the chain with the given task and returns the result.

    Args:
        task (str): The task to perform.

    Returns:
        dict: The result of the chain.
    """
    tries = 3
    parsed = {"status": "error", "commands": [], "confidence": 0.0}

    while tries > 0:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res = HOW_CLI_CHAIN.invoke({ "task": task })

        try:
            parsed = PARSER.invoke(res)
            break
        except Exception as e:
            tries -= 1

    return parsed