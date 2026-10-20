import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("API_KEY")
deployment_name = os.getenv("MODEL_DEPLOYMENT_NAME")

# Create the client object
client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

def create_Asnwer(input_text):
    # Make a request using the client
    message = client.responses.create(
        model=deployment_name,
        input=input_text,
    )
    # Print the results
    print(message.output_text)
    return message.output_text
