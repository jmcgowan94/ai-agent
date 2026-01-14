import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Confirm it found API Key
    if api_key is None:
        raise RuntimeError("Cannot find API key.")
    
    # Create parser
    parser = argparse.ArgumentParser(description="ChatBot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Create contents list
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Create and Gen AI client and query Gemini
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages
    )
    # Confirm we received a response from the API
    if response.usage_metadata is None:
        raise RuntimeError("API request failed.")
    
    # Print response, as well as token usage metadata
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)

# Run main
if __name__ == "__main__":
    main()
