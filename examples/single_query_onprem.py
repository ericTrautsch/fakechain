from fakechain.providers import OllamaProvider
from fakechain.query import execute_query, BasicQuery

sky_color = BasicQuery('What color is the sky???')
provider = OllamaProvider('http://192.168.4.64:11434')
print(execute_query(provider, sky_color))
