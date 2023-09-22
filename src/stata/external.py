# use an external Python so that the Python code and Stata Code are not combined

from sfi import Data
import pandas as pd
import json
import requests
import sys
from logic_mill import convert_json_response


def get_logic_mill_data(out_file):
    url = 'https://api.logic-mill.net/api/v1/graphql/'

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
                "value": "LoRA: Low-Rank Adaptation of Large Language Models"
            },
            {
                "key": "abstract",
                "value": "An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible. Using GPT-3 175B as an example -- deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks. Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times. LoRA performs on-par or better than fine-tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency. We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA. We release a package that facilitates the integration of LoRA with PyTorch models and provide our implementations and model checkpoints for RoBERTa, DeBERTa, and GPT-2 at"
            }
        ],
        "amount": "5",
        "indices": [
            "wipo_cos",
            "semanticscholar_cos"
        ]
    }

    headers = {
        'content-type': 'application/json',
        'Authorization': API_KEY,
    }

    r = requests.post(url, headers=headers, json={
        'query': query, 'variables': variables})

    if r.status_code == 200:
        # These lines are different form the Website
        similar_docs = convert_json_response(r.json())
        similar_docs.to_stata(out_file, version=118, write_index=False)


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 3:
        print("Usage: python external.py out_stata_file.dta API_KEY")
        sys.exit(1)

    output_file = sys.argv[1]
    API_KEY = sys.argv[2]

    get_logic_mill_data(output_file)
