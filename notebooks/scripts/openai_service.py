# Run marked code lines with Shift+Enter to run as jupyter notebook.
# Therefore not the whole script is getting executed and variables are saved in a session.

import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# TODO
# upload file via UI
# question regarding file
# limit tokens: response length (system)

class OpenAIService:
    def __init__(self):
        _ = load_dotenv(find_dotenv())  # read local .env file
        self.client = OpenAI(
            organization=os.getenv("OPENAI_ORG_ID"), api_key=os.getenv("OPENAI_API_KEY")
        )

    def upload_file(self, path):
        return self.client.files.create(file=open(path, "rb"), purpose="assistants")

    def get_assistant(
        self,
        name,
        instruction,
        file_ids=[],
        tools=[{"type": "code_interpreter"}],
        model="gpt-3.5-turbo-1106",
    ):
        return self.client.beta.assistants.create(
            name=name,
            instructions=instruction,
            tools=tools,
            model=model,
            file_ids=file_ids,
        )

    def get_thread(self):
        return self.client.beta.threads.create()

    def run_assistant(self, assistant, thread, role, content):
        self.client.beta.threads.messages.create(
            thread_id=thread.id, role=role, content=content
        )
        self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )
        return self.client.beta.threads.messages.list(thread_id=thread.id)

    def get_completion(self, prompt, model="gpt-3.5-turbo-1106"):
        response = self.client.chat.completions.create(
            model=model,  # gpt-4-1106-preview: possible but expensive
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant designed to output JSON.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,  # [0,2] high values are more random and less deterministic
            # stream=True, # enable to get a ChatGPT-like experiance
        )
        print(response.usage)
        return response.choices[0].message.content

