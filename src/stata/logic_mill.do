** Run python from within Stata
** Make sure you have the Python libraries installed: pandas, python-dotenv, requests
** Don't use a virtual environment: Stata will crash right away
** Make sure the API key is set in the .env file

clear

global my_project "FILL IN PROJECT DIR"
cd "$my_project"
python set exec "FILL IN PATH TO PYTHON"
global out_file = "similar_docs.dta"

python script "$my_project/external.py", args("$my_project/$out_file")

use "$my_project/$out_file", clear
browse
