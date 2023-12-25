import json


def main():
    with open("tests.json", "r") as file:
        test_json = file.read()

    test = json.loads(test_json)

    with open("values.json", "r") as file:
        value_json = file.read()

    value = json.loads(value_json)

    for val in test["tests"]:
        for val2 in value["values"]:
            if val["id"] == val2["id"]:
                val["value"] = val2["value"]

    with open('report.json', 'w') as file:
        json.dump(test, file)


if __name__ == '__main__':
    main()
