# Stub for chat gpt commands
import os
import openai


class ChatGipity:

    def __init__():
        token = os.environ["OPENAI_API"]
        if token is None:
            raise Exception(
                "Failed to get OpenAI API key from the enviroment variables!\r\nDid you remember to set it with export OPENAI_API=<your api key here> ?"
            )

        openai.my_api_key = token

    def getResponse(question: str) -> str:

        messages = {"role": "user", "content": question}
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        reply = chat.choices[0].message.content
        return reply
