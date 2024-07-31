import yaml

data = {
    "samle": "M110",
    "Gene": ["APOE", "BRAF", "TRET"],
}

with open("result.yaml", "w") as fw:
    yaml.dump(data, fw)
