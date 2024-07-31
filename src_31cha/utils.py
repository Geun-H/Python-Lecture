import yaml


def read_config(config_filepath: str):
    with open(config_filepath) as handle:
        config = yaml.safe_load(handle)
        return config
