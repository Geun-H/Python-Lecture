import yaml

with open("config.yaml") as handle:
    config = yaml.safe_load(handle)

print(config["TOOL"]["SAMTOOLS"])
print(config["DATA"]["REFERENCE"]["GRCH38"])
