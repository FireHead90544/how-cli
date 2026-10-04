from unittest.mock import patch
from typer.testing import CliRunner
from how.how import app
from how.core.config import Config

runner = CliRunner()

def test_setup_non_interactive(tmp_path):
    with patch("how.how.config", Config(config_dir=tmp_path)):
        # Test missing provider flag
        result = runner.invoke(app, ["setup", "--no-interactive"])
        assert result.exit_code != 0
        assert "Please set the --provider" in result.stdout

        # Test missing api key for provider that needs it
        result = runner.invoke(app, ["setup", "--no-interactive", "--provider", "OpenAI"])
        assert result.exit_code != 0
        assert "Please provide --api-key for provider 'OpenAI'" in result.stdout

        # Test valid non-interactive setup (Ollama doesn't require API key)
        with patch("how.core.llm.get_llm") as mock_get_llm:
            # Mock get_llm to avoid actually calling the LLM
            mock_llm = mock_get_llm.return_value
            mock_llm.invoke.return_value = "Success"
            
            result = runner.invoke(app, [
                "setup", 
                "--no-interactive", 
                "--provider", "Ollama",
                "--endpoint", "http://localhost:11434"
            ])
            
            assert result.exit_code == 0
            assert "Configuration saved successfully" in result.stdout
