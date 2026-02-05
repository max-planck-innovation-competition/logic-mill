# Logic Mill R Examples

This directory contains R Markdown files for interacting with the [Logic Mill API](https://api.logic-mill.net/api/v1/graphql/). The examples demonstrate how to retrieve documents, encode documents, compute similarities, and perform clustering and visualization using the Logic Mill knowledge navigation system.

## Overview

The provided R Markdown files contain examples for each available API endpoint.

### API Endpoints

- **[Encode Document](encode_document.html)** - Convert a single document (title and abstract) into an embedding.
- **[Encode Multiple Documents](encode_multiple_documents.html)** - Batch encode several documents and compute similarities.
- **[Calculate Document Similarity](calculate_document_similarity.html)** - Directly compute a similarity matrix between multiple documents.
- **[Retrieve Documents by ID](retrieve_documents_by_id.html)** - Fetch metadata and embeddings for specific documents using their IDs.
- **[Own Document Similarity Search](own_document_similarity_search.html)** - Embed a user-supplied document and search for similar documents in the database.
- **[Document Similarity Search](document_similarity_search.html)** - Find the most similar documents in the database to a given document.
- **[Pairwise Document Similarity](pairwise_document_similarity.html)** - Compute similarity scores between specific pairs of documents.

## Setup

### 1. Install Dependencies

Install the required R packages:

```R
packages <- c("rmarkdown", "knitr", "httr", "jsonlite", "ghql", "dplyr", 
              "ggplot2", "wordcloud", "tm", "igraph", "gridExtra", "viridis")
install.packages(packages)
```

### 2. API Key Configuration

To use the Logic Mill API, you need an API key. You can obtain your API key from your [Logic Mill profile page](https://logic-mill.net/identity/api-token) after [logging in](https://logic-mill.net).

To securely use your API key, create a `.env` file in this directory with the following content:

```env
API_KEY=your-api-key-here
```

**Note:** Do not commit your `.env` file or API key to version control.

## Rendering the R Markdown Files

To generate HTML files from the R Markdown sources, use the provided shell script:

```bash
# Render all .Rmd files in the current directory
bash render_all.sh

# Or render files from a specific directory
bash render_all.sh /path/to/directory
```

The script will:
- Check for required packages and install missing ones
- Render each `.Rmd` file to HTML
- Skip files that are already up-to-date (HTML newer than source)
- Display progress and results