"""
This code shows how to automatically parse the responses of Logic Mill into flattened dataframes. The code to do this
is in logic_mill.py

The queries are the default queries from the logic mill website.

TODO:
- encodeDocumentAndSimilarityCalculation, is not completely flattened
- not all variables and combinations are tested.

"""

# %% imports
import requests
import json
import pandas as pd
from pathlib import Path
import os

from logic_mill import convert_json_response

API_KEY = '<YOUR API KEY>'

OUT = Path("./out")
os.makedirs(OUT, exist_ok=True)

# %% encodeDocument - Encode Document

# build graphql query
query = """
query encodeDocument($data: EncodeObject) {
  encodeDocument(data: $data)
}
"""

# build variables
variables = {
    "data": {
        "id": "ID",
        "parts": [
            {
                "key": "title",
                "value": "Airbags"
            },
            {
                "key": "abstract",
                "value": "Airbags are one of the most important safety gears in motor vehicles such as cars and SUVs. These are cushions built into a vehicle that are intended to inflate in case of a car accident in order to protect occupants from injuries by preventing them from striking the interior of vehicle during a crash."
            }
        ]
    }
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(r.json(), OUT / "encodeDocument.csv")


# %% SimilaritySearch

query = """
query SimilaritySearch($index: String!, $id: String!, $amount: Int, $indices: [String]) {
  SimilaritySearch(index: $index, id: $id, amount: $amount, indices: $indices) {
    document {
      documentParts {
        title
      }
    }
    id
    score
    index
  }
}
"""

# build variables
variables = {
    "id": "20130226771",
    "index": "uspto_cos",
    "amount": 25,
    "indices": [
        "uspto_cos",
        "wipo_cos",
        "epo_cos"
    ]
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(r.json(), OUT / "SimilaritySearch.csv")


# %% encodeDocuments - Encode Multiple Documents

# build graphql query
query = """
query encodeDocuments($data: [EncodeObject]) {
  encodeDocuments(data: $data)
}
"""

# build variables
variables = {
    "data": [
        {
            "id": "trade_resolutions_pat",
            "parts": [
                {
                  "key": "title",
                  "value": "market driven implied trade resolutions_pat"
                },
                {
                    "key": "abstract",
                    "value": "An electronic trading system utilizes a Match Engine that receives orders, stores them internally, calculates tradable combinations and advertises the availability of real and implied orders in the form of market data. New tradable items defined as combinations of other tradable items may be included in the calculation of tradable combinations. The disclosed embodiments relate to detection of market conditions where identification of implied opportunities may, for example, subvert real orders resulting in undesirable effects. Under circumstances where such undesirable effects are likely to occur, identification of implied opportunities may be delayed thereby allowing market forces to attempt to resolve the aberrant market conditions and avoid the undesirable effects."
                }
            ]
        },
        {
            "id": "trading_systems_pat",
            "parts": [
                {
                  "key": "title",
                  "value": "dynamic peg orders in an electronic trading system "
                },
                {
                    "key": "abstract",
                    "value": "In order to protect a trading party from predatory trading strategies employed by some market participants, especially during certain periods when quotes for a particular security are experiencing rapid changes or transitions, embodiments of the present invention facilitate and support a new type of trading orders whose booking and execution behaviors are dynamically varied in response to environmental market conditions. Pursuant to predefined rules for the new type of trading orders, the orders may be allowed to trade at more aggressive price levels if the market is relatively stable, and the orders can only trade at less aggressive price levels when the market is unstable."
                }
            ]
        }
    ]
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(r.json(), OUT / "encodeDocuments.csv")

# %% Documents
# build graphql query
query = """
query Document($data: [DatabaseSearchDocument]) {
  Documents(data: $data) {
    id
    vector
  }
}
"""

# build variables
variables = {
    "data": [
        {
            "index": "semanticscholar_cos",
            "id": "7233050d4e325d7ff70693af5e6234c4d3274e02"
        },
        {
            "index": "semanticscholar_cos",
            "id": "c12615777e76852b0ff2e7495efb19a806a02221"
        },
        {
            "index": "wipo_cos",
            "id": "WO2020151634A1"
        }
    ]
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(r.json(), OUT / "Documents.csv")
# %% encodeDocumentAndSimilarityCalculation NOT COMPLETELY FLATTEND

# build graphql query
query = """
query encodeDocumentAndSimilarityCalculation($data: [EncodeObject]) {
  encodeDocumentAndSimilarityCalculation(data: $data, similarityMetric: cosine) {
    similarities
    xs {
      id
    }
    ys {
      id
    }
  }
}
"""

# build variables
variables = {
    "data": [
        {
            "id": "8rq4h",
            "parts": [
                {
                  "key": "title",
                  "value": "Hello World"
                },
                {
                    "key": "abstract",
                    "value": "Airbags are one of the most important safety gears in motor vehicles such as cars and SUVs. These are cushions built into a vehicle that are intended to inflate in case of a car accident in order to protect occupants from injuries by preventing them from striking the interior of vehicle during a crash."
                }
            ]
        },
        {
            "id": "la09s",
            "parts": [
                {
                  "key": "title",
                  "value": "Logic Mill"
                },
                {
                    "key": "abstract",
                    "value": "Whats up?"
                }
            ]
        },
        {
            "id": "x1tnp",
            "parts": [
                {
                  "key": "title",
                  "value": "Cat Food is awesome"
                },
                {
                    "key": "abstract",
                    "value": "It tastes soo good!"
                }
            ]
        },
        {
            "id": "95kfj",
            "parts": [
                {
                  "key": "title",
                  "value": "Black Holes are cool"
                },
                {
                    "key": "abstract",
                    "value": "So far away from the galaxies!"
                }
            ]
        }
    ],
    "metric": "cosine"
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(
    r.json(), OUT / "encodeDocumentAndSimilarityCalculation.csv")

# %% searchDocuments - Document Search

# build graphql query
query = """
query searchDocuments($index: String!, $keyword: String!) {
  searchDocuments(index: $index, keyword: $keyword) {
    id
    documentParts {
      title
    }
    metadata {
      createdAt
      aliases
    }
    vector
  }
}
"""

# build variables
variables = {
    "keyword": "EP19164094B1",
    "index": "epo_cos"
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(r.json(), OUT / "searchDocuments.csv")

# %% Document - Document Retrieval

# build graphql query
query = """
query Document($index: String!, $id: String!) {
  Document(index: $index, id: $id) {
    id
    documentParts {
      title
    }
    metadata {
      createdAt
      aliases
    }
    vector
  }
}
"""

# build variables
variables = {
    "id": "20130226771",
    "index": "uspto_cos"
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(r.json(), OUT / "Document.csv")

# %% embedDocumentAndSimilaritySearch (own document)


# build graphql query
query = """
query embedDocumentAndSimilaritySearch($data: [EncodeDocumentPart], $indices: [String], $amount: Int) {
  encodeDocumentAndSimilaritySearch(
    data: $data
    indices: $indices
    amount: $amount
  ) {
    document {
      documentParts {
        title
      }
    }
    id
    score
    index
  }
}
"""

# build variables
variables = {
    "data": [
        {
            "key": "title",
            "value": "Airbags"
        },
        {
            "key": "abstract",
            "value": "Airbags are one of the most important safety gears in motor vehicles such as cars and SUVs. These are cushions built into a vehicle that are intended to inflate in case of a car accident in order to protect occupants from injuries by preventing them from striking the interior of vehicle during a crash."
        }
    ],
    "amount": 25,
    "indices": [
        "uspto_cos",
        "wipo_cos",
        "epo_cos"
    ]
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(r.json(), OUT / "embedDocumentAndSimilaritySearch.csv")

# %% SimilaritySearch

# build graphql query
query = """
query SimilaritySearch($index: String!, $id: String!, $amount: Int, $indices: [String]) {
  SimilaritySearch(index: $index, id: $id, amount: $amount, indices: $indices) {
    document {
      documentParts {
        title
      }
    }
    id
    score
    index
  }
}
"""

# build variables
variables = {
    "id": "20130226771",
    "index": "uspto_cos",
    "amount": 25,
    "indices": [
        "uspto_cos",
        "wipo_cos",
        "epo_cos"
    ]
}

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY,
}

# api endpoint
url = 'https://api.logic-mill.net/api/v1/graphql/'

# send request
r = requests.post(url, headers=headers, json={
                  'query': query, 'variables': variables})


convert_json_response(r.json(), OUT / "SimilaritySearch.csv")
