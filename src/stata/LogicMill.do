// Combined version of Python integrated in DO file
// start with a Python block to get the data from the API

python:

# note make sure the libraries are installed in Python
import requests
import json
import pandas as pd
API_KEY = <FILL YOUR API KEY HERE>'


URL = 'https://api.logic-mill.net/api/v1/graphql/'

# NOTE: We need to escape the dollar signs in the string by using \$

query="""query (\$id:String!, \$index:String!, \$amount:Int) {
  SimilaritySearch(index:\$index, id:\$id, amount:\$amount) {
 	  id
    score
    document {
      documentParts {
        title
      }
    }
	id
    score
    index
  }
}"""



variables = {
  "index":"semanticscholar_cos",
  "id":"123fa2d18fab2ae1752451405f0eac5e273f2695",
  "amount": 25
}

headers = {
    'content-type': 'application/json',
    'Authorization': f"Bearer {API_KEY}",
}

print(variables)


r = requests.post(URL, headers=headers, json={'query': query , 'variables': variables})

if r.status_code == 200:
	print(r.text)
 	results = r.json()['data']['SimilaritySearch']
	print(results)

	similar_docs = pd.DataFrame(results)
	keys = similar_docs["document"][0]["documentParts"].keys()

	for k in keys:
		similar_docs[k] = similar_docs["document"].apply(lambda x: x["documentParts"][k])

	# remove document
	del similar_docs["document"]

  # save the data to a stata file
	similar_docs.to_stata('similar_docs.dta', version=118, write_index=False)
end

// Load the file in Stata
use similar_docs.dta, clear

list
