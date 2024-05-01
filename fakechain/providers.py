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
    def __init__(self, api_url):
        self.api_url = api_url

    def query_api(self, input_context):
        data = {
            "model": "mistral:instruct",
            "messages": input_context
        }



        try:
            response = requests.post(f'{self.api_url}/api/chat', json=data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            messages = response.text.split('\n')
            result = ""
            for msg in messages:
                if msg.strip():  # Skip empty lines
                    msg_data = json.loads(msg)
                    if 'message' in msg_data:
                        result += msg_data['message']['content']
            return result.strip()

        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
if __name__ == '__main__':
    openai_query = OpenAIProvider(api_url='https://api.openai.com/v1/chat/completions', api_key=os.getenv('OPENAI_API_KEY'))
    print(openai_query.query_api('Hi, my name is Eric, what is the color of the sky?').text)

