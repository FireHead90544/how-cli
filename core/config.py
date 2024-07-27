import json
from pathlib import Path

class Config:
    """
    Manages the configuration of the application.
    Config file is stored in the user's home directory.
    """
    def __init__(self):
        self.config_dir = Path.home() / ".how"
        self.config_file = self.config_dir / "config.json"
        self.__init_config()

    def __init_config(self):
        """
        Initialize the configuration directory & file if they don't exist.
        """
        if not self.config_dir.exists():
            self.config_dir.mkdir()
        
        if not self.config_file.exists():
            with open(self.config_file, "w") as f:
                json.dump({"provider": "", "api_key": ""}, f, indent=4)

    def setup(self, provider: str, api_key: str):
        """
        Set the LLM Provider & the corresponding API Key.
        """
        with open(self.config_file, "w") as f:
            json.dump({"provider": provider, "api_key": api_key}, f, indent=4)

    @property
    def values(self):
        """
        Get the configuration values.
        """
        with open(self.config_file) as f:
            return json.load(f)
        
    def is_ready(self):
        """
        Check if the configuration file is ready to use.
        """
        try:
            assert self.values.get("provider")
            assert self.values.get("api_key")
        except:
            return False

        return True