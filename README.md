# how-cli
An AI-based CLI assistant to help you with command line & shell.


## Demo 
Would be adding install instructions and better demo soon, until then check this out.
### Setup
![image](https://github.com/user-attachments/assets/87d3ba64-ecb7-43c6-9863-a62c39396ac5)

### Inferences
![image](https://github.com/user-attachments/assets/7af58310-183a-429b-aa66-e6abe36713fb)
![image](https://github.com/user-attachments/assets/20062ac2-1057-4139-9f60-990bd41605da)


## Installation
**1. Using `pip`**
  - Ensure python is installed on your system. (Tested against Python 3.11+)
  - Install the package using pip.
  ```bash
  pip install -U how-cli
  ```
**2. Manual Installation**
  - Clone the repository & cd into it
  ```bash
  git clone https://github.com/FireHead90544/how-cli && cd how-cli
  ```
  - Ensure you're in a virtual environment.
  - Install the application.
  ```bash
  pip install -e .
  ```


## Usage
```console
$ how [OPTIONS] COMMAND [ARGS]...
```

**Options**:
* `-v, --version`: Shows the version of the application
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:
* `setup`: Sets up the configuration required to run...
* `to`: Sends the task to the LLM for analysis.


## `how setup`
Sets up the configuration required to run the application.
Set the LLM Provider & the corresponding API Key.

**Usage**:
```console
$ how setup [OPTIONS]
```

**Options**:
* `--interactive / --no-interactive`: Whether to use interactive mode for setting up configuration?  [default: interactive]
* `--provider TEXT`: The LLM Provider, needs to be passed explicitly if using --no-interactive mode.
* `--api-key TEXT`: The API Key for the LLM provider, needs to be passed explicitly if using --no-interactive mode.
* `--help`: Show this message and exit.


## `how to`
Sends the task to the LLM for analysis.
Returns the commands to be executed in order to achieve that.

**Usage**:
```console
$ how to [OPTIONS] TASK
```

**Arguments**:
* `TASK`: The command line task to perform.  [required]

**Options**:
* `--help`: Show this message and exit.


## Providers
`how-cli` uses ChatModels as they support chat messages as opposed to TextModels and below model providers and their corresponding models are available to use. If you could test the models that are marked as ❌, please create an issue or pull request along with the test results.

| Provider | Model | Package | Tested |
|:--------:|:-----:|:-------:|:------:|
| GoogleGenAI   | `gemini-1.5-flash` | `langchain-google-genai` | ✅ |
| GoogleVertexAI | `gemini-1.5-flash` | `langchain-google-vertexai` | ❌ |
| GroqMistralAI | `mixtral-8x7b-32768` | `langchain-groq` | ✅ |
| GroqLLaMa | `llama3-70b-8192` | `langchain-groq` | ✅ |
| OpenAI | `gpt-4o` | `langchain-openai` | ❌ |
| Anthropic | `claude-3-5-sonnet-20240620` | `langchain-anthropic` | ❌ |