![LM Logo](img/lm-logo.png)

# Logic Mill - A Knowledge Navigation System

Logic Mill is a scalable and openly accessible software system that identifies semantically similar documents within either one domain-specific corpus or multi-domain corpora. It uses advanced Natural Language Processing (NLP) techniques to generate numerical representations of documents. Currently, it leverages a large pre-trained language model to generate these document representations. The system focuses on scientific publications and patent documents and contains more than 200 million documents. It is easily accessible via a simple Application Programming Interface (API) or via a web interface. Moreover, it is continuously being updated and can be extended to text corpora from other domains. We see this system as a general-purpose tool for future research applications in the social sciences and other domains.


This repository contains public documentation, and code examples for the use of the API. This is also the place to post issues and feature requests.


# Waiting list

> Logic Mill is still in beta and we are still finishing things for public access.
> 
You can sign up for the Logic Mill waiting list: https://logic-mill.net/waiting-list.
Signing up for the waiting list does not automatically give you access to the system. 

# API key
In order to use the Logic Mill endpoint you need an API key. Check your profile (top right) once you are logged in and copy the key into your code.

# Examples

In the /src directory you will find examples on how to use the Logic Mill API in several languages. We have examples in:

- [Go](src/go/)
- [Javascript](src/javascript/)
- [Python](src/python/)
  - `basic-api-usage.ipynb`: basic Python examples
  - `automatic_parsing.py`: automatically flattens the response to dataframe. This code has not been thoroughly tested yet.
- [R](src/R/)
- [Stata](src/stata/) (using Python)
  - `LogicMill.do`: `.do` file where the python is integrated
  - `external.do`: `.do` file with external python files (`external.py` and `logic_mill.py`). Also has automated flatening of the json response. Not completely tested.


# Bug reports and feature requests

If you found an error in our API or if you have a request for an improvement of our system, please let us know! You can add those as an issue in this Github repository:

[Create a request](https://github.com/max-planck-innovation-competition/logic-mill/issues/new/choose)

# URLs
- [Website](https://logic-mill.net/)
- [API endpoint](<https://api.logic-mill.net/api/v1/graphql/>)
- [API documentation](https://logic-mill.net/app/lm/explorer)


# Paper

If you use the Logic Mill system, please cite our paper: <https://doi.org/10.48550/arXiv.2301.00200>:

```
@misc{erhardt2022logic,
      title={Logic Mill -- A Knowledge Navigation System},
      author={Sebastian Erhardt and Mainak Ghosh and Erik Buunk and Michael E. Rose and Dietmar Harhoff},
      year={2022},
      eprint={2301.00200},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```
<https://arxiv.org/abs/2301.00200>

<!-- # Terms of use
 -->


# Contact
- Email: <team@logic-mill.net>
- [Homepage of Max Planck Institute for Innovation and Competition](https://www.ip.mpg.de/en/)
- [Imprint ](<https://www.ip.mpg.de/en/imprint/>)


© 2023 Max Planck Institute for Innovation and Competition. All rights reserved.
