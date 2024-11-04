import os
from dotenv import load_dotenv
from example.example import ExampleShell

def main():
    # Load environment variables from .env_run
    # load_dotenv(dotenv_path='.env_run')

    configs = {
        "run_primary_shell": os.getenv('run_primary_shell') == 'True',
        "replicate_api_token": os.getenv('replicate_api_token'),
    }

    if configs.get('run_primary_shell'):
        # Pass the configs dictionary to ExampleShell
        ExampleShell(configs=configs)

    else:
        print("RUN_PRIMARY_SHELL is set to False. Skipping the example shell execution.")

if __name__ == "__main__":
    main()
