# Encode Document API
# Generate an embedding for a single user-supplied document.

library(httr)
library(jsonlite)
library(ghql)


# Load environment variables
readRenviron(".env")
API_KEY <- paste('Bearer', Sys.getenv("API_KEY"))

# API URL and headers
URL <- 'https://api.logic-mill.net/api/v1/graphql/'

# Set up GraphQL client
conn <- GraphqlClient$new(
  url = URL,
  headers = list(Authorization = API_KEY)
)

# Choose model to encode the document: patspecter, specter2 or paecter
DEFAULT_MODEL <- "patspecter"

# Build GraphQL query
query <- 'query encodeDocument($data: EncodeObject, $model: String!) {
  encodeDocument(data: $data, model: $model)
}'

# Build variables with document information
variables <- fromJSON('{
  "model": "patspecter",
  "data": {
    "id": "Air bags",
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
}')

# Execute query
new <- Query$new()$query('link', query)

res <- conn$exec(new$link, variables = variables) |>
    fromJSON(flatten = FALSE)

# Get the embedding
embedding <- res$data$encodeDocument

# Print first 10 dimensions of the embedding
cat("Encoded Document (first 10 dimensions):\n", embedding[1:10], "\n")
cat("Embedding length:", length(embedding), "\n")

# --- Encode another document ---

variables2 <- list(
  model = DEFAULT_MODEL,
  data = list(
    id = "ML_interpretability",
    parts = list(
      list(key = "title", value = "Towards A Rigorous Science of Interpretable Machine Learning"),
      list(key = "abstract", value = "As machine learning systems become ubiquitous, there has been a surge of interest in interpretable machine learning: systems that provide explanation for their outputs. These explanations are often used to qualitatively assess other criteria such as safety or non-discrimination. However, despite the interest in interpretability, there is very little consensus on what interpretable machine learning is and how it should be measured.")
    )
  )
)

# Execute query
res2 <- conn$exec(new$link, variables = variables2) |>
    fromJSON(flatten = FALSE)

# Print first 10 dimensions
cat("Encoded Document (first 10 dimensions):\n", res2$data$encodeDocument[1:10], "\n")
