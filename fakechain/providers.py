from abc import ABC, abstractmethod
import os
import requests
import json

class LLMProvider(ABC):
    @abstractmethod
    def query_api(self, input_context):
        pass

class OpenAIProvider(LLMProvider):
    def __init__(self, api_url='https://api.openai.com/v1/chat/completions', api_key=os.getenv('OPENAI_API_KEY')):
        self.api_url = api_url
        self.api_key = api_key

    def query_api(self, messages):
        headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}"
                  }
        data = {
                "model": "gpt-3.5-turbo",
                "messages": messages,
                "temperature": 0.7
               }

        return json.loads(requests.post(self.api_url, headers=headers, data=json.dumps(data)).content)['choices'][0]['message']['content']


class OllamaProvider(LLMProvider):
    # TODO: Implement for release.
    def __init__(self):
        pass

    def query_api(self, input_context):
        pass

if __name__ == '__main__':
    openai_query = OpenAIProvider(api_url='https://api.openai.com/v1/chat/completions', api_key=os.getenv('OPENAI_API_KEY'))
    print(openai_query.query_api('Hi, my name is Eric, what is the color of the sky?').text)

