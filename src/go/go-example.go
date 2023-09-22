package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

// GraphQLMutationResponse represents the structure of the GraphQL mutation response.
type GraphQLMutationResponse struct {
	Data   interface{} `json:"data"`
	Errors []struct {
		Message string `json:"message"`
	} `json:"errors"`
}

func main() {
	// Example usage:
	endpointURL := "https://api.logic-mill.net/api/v1/graphql/"
	apiKey := "YOUR API KEY HERE"
	mutation := `
query encodeDocument($data: EncodeObject) {
  encodeDocument(data: $data)
}

`

	jsonVariablesString := `
{
  "data": {
    "id": "ID",
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
}
`
	// parse jsonVariablesString into a map[string]interface{}
	variables := map[string]interface{}{}
	err := json.Unmarshal([]byte(jsonVariablesString), &variables)
	if err != nil {
		fmt.Println(err)
		return
	}

	requestBody := map[string]interface{}{
		"query":     mutation,
		"variables": variables,
	}

	// Convert the request body to JSON format
	jsonBody, err := json.Marshal(requestBody)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Create the HTTP request
	request, err := http.NewRequest("POST", endpointURL, bytes.NewBuffer(jsonBody))
	if err != nil {
		fmt.Println(err)
		return
	}

	// Set the request headers
	request.Header.Set("Content-Type", "application/json")
	request.Header.Set("Authorization", "Bearer "+ apiKey)

	// Send the request
	client := &http.Client{}
	response, err := client.Do(request)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer response.Body.Close()

	// Decode the response JSON
	var mutationResponse GraphQLMutationResponse
	err = json.NewDecoder(response.Body).Decode(&mutationResponse)
	if err != nil {
		fmt.Println(err)
		return
	}

	if len(mutationResponse.Errors) > 0 {
		fmt.Println("GraphQL errors:")
		for _, e := range mutationResponse.Errors {
			fmt.Println("- ", e.Message)
		}
	} else {
		fmt.Println("GraphQL response:", mutationResponse.Data)
	}
	return
}
