# use an external Python so that the Python code and Stata Code are not combined
from urllib3.util import Retry
from requests import Session
from requests.adapters import HTTPAdapter

import pandas as pd
import sys

from dotenv import dotenv_values

# Load environment variables from .env file
conf = dotenv_values()
API_KEY = conf["API_KEY"]


def get_logic_mill_data(out_file):


    # Establish session for robust connection
    s = Session()
    retries = Retry(total=5, backoff_factor=0.1,
                    status_forcelist=[500, 501, 502, 503, 504, 524])
    s.mount('https://', HTTPAdapter(max_retries=retries))

    # API settings
    URL = 'https://api.logic-mill.net/api/v1/graphql/'
    headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer '+ API_KEY,
    }

    # Build GraphQL query
    query="""
    query embedDocumentAndSimilaritySearch($data: [EncodeDocumentPart], $indices: [String], $amount: Int, $model: String!) {
    encodeDocumentAndSimilaritySearch(
        data: $data
        indices: $indices
        amount: $amount
        model: $model
    ) {
        id
        score
        index
        document {
        title
        url
        PatspecterEmbedding
        }
    }
    }
    """

    # Build variables
    variables = {
    "model": "patspecter",
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
        "patents",
        "publications"
    ]
    }

    # Send request
    r = s.post(URL, headers=headers, json={'query': query , 'variables': variables})

    # Handle response
    if r.status_code != 200:
        print(f"Error executing\n{query}\non {URL}")
    else:
        response = r.json()
        df = pd.json_normalize(response['data']['encodeDocumentAndSimilaritySearch'])

        # rename columns with '.'
        df.columns = [c.replace(".", "_") for c in df.columns]

        # Convert PatspecterEmbedding array to separate columns more efficiently
        # Create a dictionary of embedding columns all at once
        embedding_cols = {}
        for i in range(len(df.document_PatspecterEmbedding.iloc[0])):
            embedding_cols[f'embedding_{i}'] = df.document_PatspecterEmbedding.apply(lambda x: x[i])

        # Create a new dataframe with all embeddings and join with original data
        embedding_df = pd.DataFrame(embedding_cols)
        df = pd.concat([df.drop('document_PatspecterEmbedding', axis=1), embedding_df], axis=1)

        # Save to Stata format
        df.to_stata(out_file, version=118, write_index=False)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python external.py out_stata_file.dta")
        sys.exit(1)

    output_file = sys.argv[1]

    get_logic_mill_data(output_file)
