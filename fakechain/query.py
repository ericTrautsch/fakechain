import requests
import os 
import json

from abc import ABC, abstractmethod

class Query(ABC):
    @abstractmethod
    def __init__(self, api_url='https://api.openai.com/v1/chat/completions',api_key=None):
        pass
        
    @abstractmethod
    def query_api(self, input_context):
        pass


class OpenAIAPIQuery(Query):
    def __init__(self, api_url='https://api.openai.com/v1/chat/completions', api_key='not_a_key'):
        self.api_url = api_url
        self.api_key = api_key

    def query_api(self, input_context):
        headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}"
                  }
        data = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": f"{input_context}"}],
                "temperature": 0.7
               }

        return requests.post(self.api_url, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    openai_query = OpenAIAPIQuery(api_url='https://api.openai.com/v1/chat/completions', api_key=os.getenv('OPENAI_API_KEY'))
    print(openai_query.query_api('Hi, my name is Eric, what is the color of the sky?').text)

