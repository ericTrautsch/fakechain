from fakechain.providers import OpenAIProvider
from fakechain.query import execute_basic_chain, BasicQuery

stat_question_query = BasicQuery('Write a question to give 10 numbers and ask for the mean and median of the data')
provider = OpenAIProvider()
print(execute_basic_chain(provider, stat_question_query, BasicQuery))
