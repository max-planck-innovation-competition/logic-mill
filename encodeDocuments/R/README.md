# encodeDocuments — R Example

This example demonstrates the [encodeDocuments](https://logic-mill.net/app/lm/encode-multiple-documents) API endpoint of [Logic Mill](https://logic-mill.net/), which generates embeddings for multiple user-supplied documents.

## Setup

1. Obtain an API key at <https://logic-mill.net/identity/api-token>.
2. Create a `.env` file in this directory:
   ```
   API_KEY=your_api_key_here
   ```
3. Install required R packages: `httr`, `jsonlite`, `ghql`.
4. Run with `Rscript example.R`.
