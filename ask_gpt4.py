import os

from openai import OpenAI

os.environ["OPENAI_API_KEY"] = open("/Users/deven367/openai-key.txt").read().strip()

class AskGPT4:

    def __init__(self, question, logs):
        self.question = question
        self.logs = logs
        self.text = self.process_payload()



def send_message(message_log):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # The name of the OpenAI chatbot model to use
        messages=message_log,  # The conversation history up to this point, as a list of dictionaries
        max_tokens=3800,  # The maximum number of tokens (words or subwords) in the generated response
        stop=None,  # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,  # The "creativity" of the generated response (higher temperature = more creative)
    )

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content