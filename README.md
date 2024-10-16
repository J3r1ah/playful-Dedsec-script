# DedSec Recruitment Workflow

This repository contains a GitHub Actions workflow that simulates the DedSec recruitment process from the Watch Dogs game series.

## Workflow Description

The workflow is triggered on push or pull request to the main branch. It performs the following tasks:

1. Sets up a Python environment
2. Runs unit tests
3. Performs linting with flake8
4. Runs the DedSec recruitment script

## Script Features

- Evaluates potential recruits based on a skill score
- Provides welcome or rejection messages
- Displays DedSec's mission statement
- Requests a coded message from successful recruits
- Displays DedSec ASCII art

## Local Development

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m unittest discover tests`
4. Run the script: `python src/dedsec.py`

## Contributing

1. Fork this repository
2. Create a new branch for your feature
3. Make your changes and commit them
4. Push to your fork and submit a pull request

## Disclaimer

This project is for educational and entertainment purposes only. It does not actually recruit for any hacking group or endorse any illegal activities. The content is fictional and based on the Watch Dogs game.

## License

This project is open source and available under the MIT License.
