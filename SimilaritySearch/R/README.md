# SimilaritySearch — R Example

This example demonstrates the [SimilaritySearch](https://logic-mill.net/app/lm/database-document-similarity-search) API endpoint of [Logic Mill](https://logic-mill.net/), which finds similar documents to one already in the database.

## Setup

1. Obtain an API key at <https://logic-mill.net/identity/api-token>.
2. Create a `.env` file in this directory:
   ```
   API_KEY=your_api_key_here
   ```
3. Install required R packages: `httr`, `jsonlite`, `ghql`.
4. Run with `Rscript example.R`.
