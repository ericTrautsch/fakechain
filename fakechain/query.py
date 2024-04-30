import requests
import os 
import json

from abc import ABC, abstractmethod

class Query(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def generate_query(self):
        pass

    def postprocess(self, response):
        return response


class BasicQuery(Query):
    def __init__(self, input_text):
        self.input_text = input_text

    def generate_query(self):
        return [{"role": "user", "content": str(self.input_text)}]
        
class BasicPaL(Query):
    def __init__(self, input_text):
        self.input_text = input_text

    def generate_query(self):
        return [ {'role': 'system', 'content': 'You are a helpful assistant that can write Python code that solves mathematical reasoning questions. Respond with ONLY executable code, and ensure the correct answer is printed to the command line inferface using the print() function.'},
            {'role': 'user', 'content': self.input_text}]

    def postprocess(self, response):
        response = response.strip('```')
        response = response.replace('python', '')
        print(f'Intermediate Code:\n{response}\n\n')
        try:
            lines = response.strip().split('\n')
            for line in lines:
                exec(line)
        except Exception as e:
            print(f'error: {e}')
            return f"Result failed unsuccessfully. {response}"
        return f"Successful."


def execute_query(provider, query):
    """Function to execute a query given a provider and a specified query"""
    return query.postprocess(provider.query_api(query.generate_query()))

def execute_basic_chain(provider, query_one, query_two_type=BasicQuery):
    """Function to execute a two queries, given a query, and a type of query for the followup"""
    response_one = execute_query(provider, query_one)
    print(f'intermediate: {response_one}')
    return execute_query(provider, query_two_type(response_one))


