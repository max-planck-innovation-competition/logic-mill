# Document Similarity Search API
# Find similar documents to one already in the database.

library(httr)
library(jsonlite)
library(ghql)
library(dplyr)
library(ggplot2)
library(wordcloud)
library(tm)

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

# Build GraphQL query
query <- 'query SimilaritySearch($index: String!, $id: String!, $amount: Int, $indices: [String], $model: String!) {
  SimilaritySearch(
    index: $index
    id: $id
    amount: $amount
    indices: $indices
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
}'

# Build variables - search for documents similar to patent 91081326
variables <- fromJSON('{
  "model": "patspecter",
  "amount": 25,
  "id": "91081326",
  "index": "patents",
  "indices": [
    "patents",
    "publications"
  ]
}')

# Execute query
new <- Query$new()$query('link', query)
res <- conn$exec(new$link, variables = variables) %>%
    fromJSON(flatten = FALSE)

# Extract documents
documents <- res$data$SimilaritySearch

# Create summary data frame
df <- data.frame(
  id = documents$id,
  score = documents$score,
  index = documents$index,
  title = substr(documents$document$title, 1, 60)
)

head(df, 10)

# --- Word Cloud ---

# Combine all titles, weighted by their similarity score
titles <- documents$document$title
scores <- documents$score

# Build word frequency weighted by score
word_freq <- list()
for (i in seq_along(titles)) {
  words <- unlist(strsplit(tolower(titles[i]), "\\s+"))
  words <- gsub("[^a-z]", "", words)
  words <- words[nchar(words) > 2]

  stopwords_list <- c("the", "and", "for", "with", "from", "that", "this", "are",
                      "was", "were", "been", "being", "have", "has", "had", "its",
                      "which", "can", "may", "will", "would", "could", "should")
  words <- words[!words %in% stopwords_list]

  for (word in words) {
    if (is.null(word_freq[[word]])) {
      word_freq[[word]] <- scores[i]
    } else {
      word_freq[[word]] <- word_freq[[word]] + scores[i]
    }
  }
}

# Convert to data frame for wordcloud
freq_df <- data.frame(
  word = names(word_freq),
  freq = unlist(word_freq)
)

# Generate word cloud
if (nrow(freq_df) > 0) {
  wordcloud(words = freq_df$word,
            freq = freq_df$freq,
            min.freq = 0.1,
            max.words = 100,
            random.order = FALSE,
            colors = c("#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                       "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"),
            scale = c(3, 0.5))
  title("Word Cloud Weighted by Similarity Score")
}
