from fakechain.providers import OpenAIProvider
from fakechain.query import execute_basic_chain, BasicQuery

stat_question_query = BasicQuery('What is a good question to ask about statistics and data science?')
provider = OpenAIProvider()
print(execute_basic_chain(provider, stat_question_query, BasicQuery))
