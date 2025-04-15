** Run python from within Stata
** Make sure you have the Python libraries installed: pandas, python-dotenv, requests
** Make sure the API key is set in the .env file

** If this doesn't work, you can run the python script separately:
** python external.py similar_docs.dta

clear

global my_project "FILL YOUR PROJECT PATH"

python set exec "FILL YOUR PATH TO PYTHON"
global out_file = "similar_docs.dta"

python script "$my_project/external.py", args("$my_project/$out_file")

use "$my_project/$out_file", clear
browse
