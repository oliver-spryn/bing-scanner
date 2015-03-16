from py_bing_search import PyBingSearch
b = PyBingSearch("CHANGE ME")
result_list, next_uri = b.search("Python Software Foundation", limit=50, format='json')

print(results_list[0].description)
