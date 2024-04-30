import requests
import os 
import json

from abc import ABC, abstractmethod

def execute_query(provider, query):
    """Function to execute a query given a provider and a specified query"""
    return query.postprocess(provider.query_api(query.generate_query()))

def execute_basic_chain(provider, query_one, query_two_type=BasicQuery):
    """Function to execute a two queries, given a query, and a type of query for the followup"""
    response_one = execute_query(provider, query_one)
    return execute_query(provider, query_two_type(response_one))

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
        return self.input_text[{"role": "user", "content": str(input_text)}]
        
class BasicPaL(Query):
    def __init__(self, input_text)
        self.input_text = input_text

    def generate_query(self):
        return [ {'role': 'system', 'content': 'You are a helpful assistant that can write Python code that solves mathematical reasoning questions. Response with ONLY executable code, and ensure the correct answer is returned.'},
            {'role': 'user', 'content': self.input_text}]

    def postprocess(self, response):
        try:
            response.strip().split('\n')
            for line in lines:
                exec(line)
        except:
            return f"Result failed unsuccessfully. {response}"
        return f"No result. {response}"



