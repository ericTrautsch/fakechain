from fakechain.providers import OpenAIProvider
from fakechain.query import execute_query, BasicPaL

sky_color = BasicPaL('What is the average of [5,123,1234,33]?')
provider = OpenAIProvider()
print(execute_query(provider, sky_color))
