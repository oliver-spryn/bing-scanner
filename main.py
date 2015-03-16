from py_bing_search import PyBingSearch
b = PyBingSearch("fEOz4KDSWOC5T11W3LZrQ6Db2shWlc5agjbkl5HMNTQ=")
result_list, next_uri = b.search("Python Software Foundation", limit=50, format='json')

print(results_list[0].description)
