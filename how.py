from typer import Typer

app = Typer()

@app.command()
def to(task: str):
    print(f"Send {task} to LLM. Test Finished.")

if __name__ == "__main__":
    app()