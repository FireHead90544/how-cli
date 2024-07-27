import typer
from typing_extensions import Annotated
from rich.prompt import Prompt
from how.core.config import Config
from how.formatting import display_result
from how import __version__

app = typer.Typer(
    name="how",
    help="An AI-based CLI assistant to help you with command line & shell.",
)
config = Config()

def get_version(value: bool):
    """
    Callback to get the version of the application.
    """
    if value:
        typer.echo(f"v{__version__}")
        raise typer.Exit()

@app.callback()
def show_version(
    version: bool = typer.Option(False, "--version", "-v", help="Shows the version of the application", callback=get_version)
):
    """
    Shows the version of the application.
    """
    pass


@app.command()
def to(
    task: Annotated[str, typer.Argument(help="The command line task to perform.")]
):
    """
    Sends the task to the LLM for analysis.
    Returns the commands to be executed in order to achieve that.
    """
    if not config.is_ready():
        typer.secho("Please setup the configuration first using `how setup`", fg="red", bold=True)
        raise typer.Abort()

    from how.infer import get_result
    result = get_result(task)
    display_result(task, result)


@app.command()
def setup(
    interactive: Annotated[bool, typer.Option(help="Whether to use interactive mode for setting up configuration?")] = True,
    provider: Annotated[str, typer.Option(help="The LLM Provider, needs to be passed explicitly if using --no-interactive mode.")] = "",
    api_key: Annotated[str, typer.Option(help="The API Key for the LLM provider, needs to be passed explicitly if using --no-interactive mode.")] = ""
):
    """
    Sets up the configuration required to run the application.
    Set the LLM Provider & the corresponding API Key.
    """
    from how.core.providers import LLM_PROVIDERS
    
    if not interactive:
        if not provider or not api_key:
            typer.secho("Please set the --provider and --api-key", fg="red", bold=True)
            raise typer.Abort()
        if provider not in LLM_PROVIDERS.keys():
            typer.secho("LLM Provider not available yet. Please select from the available options.", fg="red", bold=True)
            raise typer.Abort()
    else:
        provider = Prompt.ask("Select the LLM Provider", choices=list(LLM_PROVIDERS.keys()))
        api_key = Prompt.ask(f"Enter {provider} API Key", password=True)

        typer.confirm("Do you want to save the configuration?", abort=True)

    # Test the API Key & Save the configuration only if it works
    try:
        llm = LLM_PROVIDERS.get(provider)["provider"](model=LLM_PROVIDERS.get(provider)['model'], api_key=api_key)
        llm.invoke("Hi!")
    except:
        typer.secho("Invalid API Key for the given provider. Please try again.", fg="red", bold=True)
        raise typer.Abort()

    config.setup(provider, api_key)
