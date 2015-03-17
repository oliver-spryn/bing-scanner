import json
from ResultsModel import ResultsModel
import urllib
import urllib2

class Bing:
	def __init__(self, username, key):
	# Save the credentials provided by the user
		self.Key = key
		self.ResultsMax = 50
		self.UserName = username

	def remainingBalance(self, APIName = "Bing Search API"):
	# Fetch the data form the Bing API
		baseURL = "https://api.datamarket.azure.com/Services/My/Datasets?%24format=json"
		results = self.URLFetch(baseURL)

	# Parse the returned data for the remaining balance
		parser = json.JSONDecoder().decode(results)
		data = parser["d"]["results"]
		total = 0		

		for row in data:
			if row["Title"] == APIName:
				total = row["ResourceBalance"]
				break

		return total

	def search(self, query, page = 1):
	# Fetch the data form the Bing API
		query = urllib.quote("'{}'".format(query))
		baseURL = "https://api.datamarket.azure.com/Bing/Search/v1/Web?Query={}&%24format=json&%24skip={}&%24top={}".format(query, self.ResultsMax * (page - 1), self.ResultsMax)
		results = self.URLFetch(baseURL)

	# Parse the data into a Python model
		parser = json.JSONDecoder().decode(results)
		data = parser["d"]["results"]
		models = []

		for row in data:
			model = ResultsModel()
			model.Description = row["Description"]
			model.DisplayURL = row["DisplayUrl"]
			model.ID = row["ID"]
			model.Title = row["Title"]
			model.URL = row["Url"]

			models.append(model)

		return models

	def URLFetch(self, URL):
		passw = urllib2.HTTPPasswordMgrWithDefaultRealm()
		passw.add_password(None, URL, self.UserName, self.Key)
		handle = urllib2.HTTPBasicAuthHandler(passw)
		open = urllib2.build_opener(handle)
		urllib2.install_opener(open)
		results = urllib2.urlopen(URL).read()

		return results
