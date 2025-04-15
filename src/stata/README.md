# Run Python from within Stata

## Prerequisites

- Make sure you have the Python libraries installed: pandas, python-dotenv, requests
- Make sure the API key is set in the .env file
- Don't use a virtual environment: Stata will crash right away
- Tested with Python 3.10 and Stata 17

## Usage

- Open the logic_mill.do file from within Stata
- Set the correct path to Python
- Set the project directory
- Copy the API key into the .env file
- Run the do-file

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