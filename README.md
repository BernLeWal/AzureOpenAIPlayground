# Code-Generator

A gpt-based code generator to create source-code fragments using kotlin & jetpack compose for pre-defined scenarios

## Pre-Requisites

* You need a Azure OpenAI Key and Access to the [Azure OpenAI Studio](https://oai.azure.com/portal)

## Installation

* Create a [.env](.env) file in the project root. See [.env.sample](.env.sample)
    * Important: set the AZURE_OPENAI_KEY environment variable

* Install Python (>3.10), create virtual environment (venv) and activate it

* Install the necessary python libraries
```
pip install -r requirements.txt
```
  or install the libraries manually:
```
pip install python-dotenv
pip install openai
pip install tqdm

pip freeze > requirements.txt
```

## Usage

Run ```python generate.py```
