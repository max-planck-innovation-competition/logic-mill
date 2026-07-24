# Pairwise Document Similarity API
# Compute similarity between specific pairs of documents by ID.

library(httr)
library(jsonlite)
library(ghql)
library(dplyr)
library(ggplot2)
library(igraph)

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

# Similarity metric: cosine, l1, l2
SIMILARITY_METRIC <- "cosine"

# Define pairs of documents to compare
document_pairs <- list(
  list(sourceIndex = "patents", sourceId = "80544619", targetIndex = "patents", targetId = "43862061"),
  list(sourceIndex = "patents", sourceId = "29559527", targetIndex = "publications", targetId = "W2531412717"),
  list(sourceIndex = "patents", sourceId = "43820202", targetIndex = "patents", targetId = "61199404"),
  list(sourceIndex = "patents", sourceId = "61199404", targetIndex = "patents", targetId = "80544619")
)

# Build GraphQL query
query <- 'query retrieveDocumentAndSimilarityCalculation($data: [RetrievalSimilarityObject], $metric: similarityMetric, $model: String!) {
  retrieveDocumentAndSimilarityCalculation(
    data: $data
    similarityMetric: $metric
    model: $model
  ) {
    score
    sourceId
    sourceIndex
    targetId
    targetIndex
  }
}'

# Build variables for the query
variables <- list(
  data = document_pairs,
  metric = SIMILARITY_METRIC,
  model = "patspecter"
)

# Execute query
new <- Query$new()$query('link', query)
res <- conn$exec(new$link, variables = variables) %>%
    fromJSON(flatten = FALSE)

# Extract results
results <- res$data$retrieveDocumentAndSimilarityCalculation

# Create data frame
df <- data.frame(
  sourceId = results$sourceId,
  sourceIndex = results$sourceIndex,
  targetId = results$targetId,
  targetIndex = results$targetIndex,
  score = results$score
)

print(df)

# --- Network Graph with extended pairs ---

extended_pairs <- list(
  list(sourceIndex = "patents", sourceId = "80544619", targetIndex = "patents", targetId = "43862061"),
  list(sourceIndex = "patents", sourceId = "29559527", targetIndex = "publications", targetId = "W2531412717"),
  list(sourceIndex = "patents", sourceId = "43820202", targetIndex = "patents", targetId = "61199404"),
  list(sourceIndex = "patents", sourceId = "61199404", targetIndex = "patents", targetId = "80544619"),
  list(sourceIndex = "publications", sourceId = "W2167224711", targetIndex = "patents", targetId = "43862061"),
  list(sourceIndex = "publications", sourceId = "W2531412717", targetIndex = "patents", targetId = "80544619"),
  list(sourceIndex = "publications", sourceId = "W2364777665", targetIndex = "patents", targetId = "43862061"),
  list(sourceIndex = "publications", sourceId = "W2079788930", targetIndex = "patents", targetId = "43862061"),
  list(sourceIndex = "publications", sourceId = "W4392883972", targetIndex = "patents", targetId = "43820202"),
  list(sourceIndex = "patents", sourceId = "43862061", targetIndex = "patents", targetId = "29559527"),
  list(sourceIndex = "patents", sourceId = "71425071", targetIndex = "patents", targetId = "43820202"),
  list(sourceIndex = "patents", sourceId = "82025502", targetIndex = "patents", targetId = "43820202"),
  list(sourceIndex = "patents", sourceId = "73969714", targetIndex = "patents", targetId = "43820202"),
  list(sourceIndex = "patents", sourceId = "57146653", targetIndex = "patents", targetId = "43820202")
)

variables_ext <- list(
  data = extended_pairs,
  metric = SIMILARITY_METRIC,
  model = "patspecter"
)

res_ext <- conn$exec(new$link, variables = variables_ext) %>%
    fromJSON(flatten = FALSE)

results_ext <- res_ext$data$retrieveDocumentAndSimilarityCalculation

df_ext <- data.frame(
  sourceId = results_ext$sourceId,
  sourceIndex = results_ext$sourceIndex,
  targetId = results_ext$targetId,
  targetIndex = results_ext$targetIndex,
  score = results_ext$score
)

head(df_ext, 10)

# --- Network Graph Visualization ---

edges <- df_ext[, c("sourceId", "targetId", "score")]
colnames(edges) <- c("from", "to", "weight")

g <- graph_from_data_frame(edges, directed = FALSE)

# Assign node colors based on index type
node_colors <- sapply(V(g)$name, function(x) {
  if (grepl("^W", x)) return("#ff7f0e")  # Publications (OpenAlex IDs start with W)
  else return("#1f77b4")  # Patents
})

set.seed(40)
layout <- layout_with_fr(g, niter = 500)

plot(g,
     vertex.color = node_colors,
     vertex.size = 15,
     vertex.label.cex = 0.6,
     vertex.label.color = "black",
     edge.width = E(g)$weight * 3,
     edge.label = round(E(g)$weight, 2),
     edge.label.cex = 0.6,
     layout = layout,
     main = "Pairwise Document Similarity Graph (Undirected)")

legend("bottomleft",
       legend = c("Patents", "Publications"),
       fill = c("#1f77b4", "#ff7f0e"),
       border = NA,
       bty = "n")

# --- Summary Statistics ---

cat("Network Statistics:\n")
cat("  Number of nodes:", vcount(g), "\n")
cat("  Number of edges:", ecount(g), "\n")
cat("  Average similarity score:", round(mean(df_ext$score), 3), "\n")
cat("  Max similarity score:", round(max(df_ext$score), 3), "\n")
cat("  Min similarity score:", round(min(df_ext$score), 3), "\n")
