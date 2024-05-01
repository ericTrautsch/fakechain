from fakechain.providers import OpenAIProvider
from fakechain.query import execute_query, BasicQuery

sky_color = BasicQuery('What color is the sky???')
provider = OpenAIProvider()
print(execute_query(provider, sky_color))
