#!/usr/bin/env python3
""" Generate kotlin+jetpack compose code from a given text prompt. """

#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
from dotenv import load_dotenv
from openai import AzureOpenAI


load_dotenv()  # take environment variables from .env.

def generate_code(dialog_desc: str, variation: int=0) -> str:
    """ Generate kotlin+jetpack compose code for a specified dialog_description. """
    # Create an instance of the AzureOpenAI class.

    client = AzureOpenAI(
    azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_KEY"),
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION")
    )

    message_text = [
        {
            "role":"system", 
            "content":os.environ.get("SYSTEM_PROMPT")
        },
        {
            "role":"user",
            "content": 
                f"Create a Kotlin program using jetpack-compose to implement a {dialog_desc}."
        }
    ]

    completion = client.chat.completions.create(
        model="fhtw-csam-cs-walliscb-gpt-4-0613-deploy",
        messages = message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    completion_text = completion.choices[0].message.content

    # Extract the kotlin code from the completion_text.
    completion_text = completion_text.split("```")[1]
    # Remove the first line of the kotlin code.
    completion_text = completion_text.split("\n", 1)[1]

    # Save to a kotline source file.
    output_dir = os.environ.get("OUTPUT_DIR")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if variation > 0:
        filename = output_dir + f"{dialog_desc}_{variation}.kt".replace(" ","_")
    else:
        filename = output_dir + f"{dialog_desc}.kt".replace(" ","_")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(completion_text)

    return completion_text


if __name__ == "__main__":
    generate_code("login dialog")
