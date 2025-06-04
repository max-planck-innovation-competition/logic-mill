# Logic Mill Python Examples

This directory contains example Python scripts and Jupyter notebooks for interacting with the [Logic Mill API](https://api.logic-mill.net/api/v1/graphql/). The examples demonstrate how to retrieve documents, encode documents, compute similarities, and perform clustering and visualization using the Logic Mill knowledge navigation system.

## Overview

The provided notebooks contain examples for each available API endpoint.

- **Basic API Usage**: How to connect to the API, retrieve document metadata, and get embeddings.
- **Retrieve Documents by ID**: Fetch metadata and embeddings for specific documents using their IDs.
- **Encode Document**: Convert a single document (title and abstract) into an embedding.
- **Encode Multiple Documents**: Batch encode several documents and compute similarities.
- **Calculate Document Similarity**: Directly compute a similarity matrix between multiple documents.
- **Document Similarity Search**: Find the most similar documents in the database to a given document.
- **Own Document Similarity Search**: Embed a user-supplied document and search for similar documents in the database.
- **Pairwise Document Similarity**: Compute similarity scores between specific pairs of documents.

## Setup

### 1. Install Dependencies

Install the required Python packages using pip:

```sh
pip install -r requirements.txt
```

### 2. API Key Configuration
To use the Logic Mill API, you need an API key. You can obtain your API key from your [Logic Mill profile page](https://logic-mill.net/identity/api-token) after [logging in](https://logic-mill.net).

To securely use you API key, create a `.env` file in this directory (`logic-mill/src/python/`) with the following content:
```env
API_KEY=your-api-key-here
```

**Note:** Do not commit your `.env` file or API key to version control.

## Additional Resources
- [Logic Mill Website](https://logic-mill.net)
- [API Documentation & Explorer](https://logic-mill.net/app/lm/explorer/)
- [Main Repository](https://github.com/max-planck-innovation-competition/logic-mill)
- Email: [team@logic-mill.net](mailto:team@logic-mill.net)