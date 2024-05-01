from fakechain.providers import OllamaProvider
from fakechain.query import execute_query, BasicPaL

sky_color = BasicPaL('What is the average of the numbers 1, 2, and 32')
provider = OllamaProvider('http://192.168.4.64:11434')
print(execute_query(provider, sky_color))
