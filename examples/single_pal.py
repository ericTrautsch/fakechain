from fakechain.providers import OpenAIProvider
from fakechain.query import execute_query, BasicPaL

sky_color = BasicPaL('Generate 15 samples from the multivariate normal distribution with mu=[0,2], sigma=[[1,0],[0,2]]')
provider = OpenAIProvider()
print(execute_query(provider, sky_color))
