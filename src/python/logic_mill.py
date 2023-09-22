import requests
import json
import pandas as pd


def parse(document_data, data_dict, parent=""):
    """Parses a single dictionary record of the response
    data_dict is called by reference so it will be updated
    """

    if not isinstance(data_dict, dict):
        print("Input should be a dictionary")
        return

    # parse the keys of the dictionary
    keys = [str(k) for k in document_data.keys()]
    for k in keys:
        d = document_data[k]
        if isinstance(d, dict):
            # if the item is a dictionary, call function recursively
            if parent == "":
                next_parent = k
            else:
                next_parent = key = "_".join([parent, k])
            parse(document_data[k], data_dict, parent=next_parent)
        elif isinstance(d, str) or isinstance(d, int) or isinstance(d, float):
            if parent == "":
                key = k
            else:
                key = "_".join([parent, k])
            data_dict[key] = document_data[k]
        elif isinstance(d, list):
            # the list can containt differen types of data
            for i, v in enumerate(document_data[k]):
                data_dict[f"{k}_{i}"] = v
        elif d is None:
            data_dict[k] = None
        else:
            print(f"[parse] Unhandeled type: {type(d)}")


def convert_json_response(data, save=""):
    """
    Parses the response output. Normally use
    convert_json_response(r.json())

    Save: use filename to save the dataframe to
    """
    if data.get('data') is None:
        print("ERROR: Input data is empty")
        return pd.DataFrame()

    endpoint = list(data['data'].keys())[0]
    document_data = data['data'][endpoint]

    df = pd.DataFrame()
    if isinstance(document_data, list):
        for i, document in enumerate(document_data):
            data_dict = {}
            # todo no necesarrily a dictionary
            if isinstance(document, dict):
                parse(document, data_dict)
            elif isinstance(document, float):
                data_dict["values"] = document
            elif isinstance(document, list):
                for i2, doc2 in enumerate(document):
                    if isinstance(doc2, float):
                        data_dict[f"value_{i2}"] = doc2
                    else:
                        print(
                            f"convert_json_response>list>list {type(doc2)} not handled")
            else:
                print(
                    f"[convert_json_response > list] Unhandled data type: {type(document)}")
            tmp = pd.DataFrame([data_dict])
            df = pd.concat([df, tmp], axis=0)
    elif isinstance(document_data, dict):
        data_dict = {}
        parse(document_data, data_dict)
        df = pd.DataFrame([data_dict])
    else:
        print(
            f"[convert_json_response main loop] Unhandled type: {type(document_data)}")
    df = df.reset_index(drop=True)

    if save != "":
        df.to_csv(save, index=False)

    return df
