# encodeDocumentAndSimilaritySearch — Stata Example

This example demonstrates the [encodeDocumentAndSimilaritySearch](https://logic-mill.net/app/lm/own-document-similarity-search) API endpoint of [Logic Mill](https://logic-mill.net/), which encodes user text and finds similar documents in one call. It runs Python from within Stata.

## Setup

1. Obtain an API key at <https://logic-mill.net/identity/api-token>.
2. Create a `.env` file in this directory:
   ```
   API_KEY=your_api_key_here
   ```
3. Install the Python libraries: `pandas`, `python-dotenv`, `requests` (outside a virtual environment — Stata will crash otherwise).
4. Tested with Python 3.10 and Stata 17.

## Usage

- Open `logic_mill.do` from within Stata.
- Set the correct path to Python.
- Set the project directory.
- Run the do-file.

## Notes

_ If you want to use the Logic Mill query directly in the do-file, you need to escape characters in the graphQL query, especially the `$` signs:

```python
query="""query (\$id:String!, \$index:String!, \$amount:Int) {
  SimilaritySearch(index:\$index, id:\$id, amount:\$amount) {
 	  id
    score
    document {
      documentParts {
        title
      }
    }
	id
    score
    index
  }
}"""

```