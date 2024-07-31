from utils import read_config

config = read_config("config.yaml")
samtools = config["TOOL"]["SAMTOOLS"]
ref_grch38 = config["DATA"]["REFERENCE"]["GRCH38"]

print(samtools)
print(ref_grch38)
