clear

global my_project "FILL YOUR PROJECT PATH"
global token = "YOUR API KEY"
global api_key = "Bearer $token"
global out_file = "similar_docs.dta"

python script "$my_project/external.py", args("$my_project/$out_file" "$api_key")

use "$my_project/$out_file", clear
browse
