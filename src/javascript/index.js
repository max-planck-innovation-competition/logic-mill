const resultsContainer = document.querySelector('#results-container');

const url = 'https://api.logic-mill.net/api/v1/graphql/';
const API_KEY = 'YOUR API KEY';

const initialDocs = [
  {
    id: Math.random().toString(36).slice(-5),
    parts: [
      {
        key: 'title',
        value: 'Hello World',
      },
      {
        key: 'abstract',
        value:
          'Airbags are one of the most important safety gears in motor vehicles such as cars and SUVs. These are cushions built into a vehicle that are intended to inflate in case of a car accident in order to protect occupants from injuries by preventing them from striking the interior of vehicle during a crash.',
      },
    ],
  },
  {
    id: Math.random().toString(36).slice(-5),
    parts: [
      {
        key: 'title',
        value: 'Logic Mill',
      },
      {
        key: 'abstract',
        value: 'Whats up?',
      },
    ],
  },
  {
    id: Math.random().toString(36).slice(-5),
    parts: [
      {
        key: 'title',
        value: 'Cat Food is awesome',
      },
      {
        key: 'abstract',
        value: 'It tastes soo good!',
      },
    ],
  },
  {
    id: Math.random().toString(36).slice(-5),
    parts: [
      {
        key: 'title',
        value: 'Black Holes are cool',
      },
      {
        key: 'abstract',
        value: 'So far away from the galaxies!',
      },
    ],
  },
];

// let gql = `mutation embedDocumentsAndSimilarityCalculation($data: [LmDocumentMutationObject]){
//   embedDocumentsAndSimilarityCalculation(data: ${initialDocs},similarityMetric: cosine) {
//     similarities
//     xs {
//       id
//     }
//     ys {
//       id
//     }
//   }
// }
// `;

let gql = `query = """{
  Version
}"""
`;

const options = {
  method: 'post',
  headers: {
    'content-type': 'application/json',
    Authorization: `Bearer ${API_KEY}`,
  },
  body: JSON.stringify({
    query: gql,
  }),
};

function renderResults(r) {
  console.log(r);
  resultsContainer.innerHTML = 'Results: ';
  resultsContainer.innerHTML += r;
}

let response = fetch(url, options);

if (response.ok) {
  // if HTTP-status is 200-299
  // get the response body (the method explained below)
  let json = response.json();
  renderResults(json);
} else {
  msg = 'HTTP-Error: ' + response.status;
  resultsContainer.innerHTML = msg;
  console.log(msg);
}
// .then((res) => res.json())
// .then(renderResults);
