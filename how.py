import typer
from typing_extensions import Annotated
from rich.prompt import Prompt

app = typer.Typer()


@app.command()
def to(
    task: Annotated[str, typer.Argument(help="The command line task to perform.")]
):
    """
    Sends the task to the LLM for analysis.
    Returns the commands to be executed in order to achieve that.
    """
    print(f"Send {task} to LLM. Test Finished.")


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
    LLM_PROVIDERS = ["Gemini"]

    if not interactive:
        if not provider or not api_key:
            typer.secho(
                "Please set the --provider and --api-key", fg="red", bold=True
            )
            raise typer.Abort()
    else:
        provider = Prompt.ask("Select the LLM Provider", choices=LLM_PROVIDERS)
        api_key = Prompt.ask(f"Enter {provider} API Key", password=True)

        typer.confirm("Do you want to save the configuration?", abort=True)

    # Save the configration
    print(api_key, provider)


if __name__ == "__main__":
    app()
