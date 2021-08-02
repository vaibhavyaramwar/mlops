import os
import argparse
import yaml
import logging

def read_config(configpath):
    with open(configpath) as yml_file:
        config=yaml.safe_load(yml_file)
    return config


def main(configpath,datasource):
    config=read_config(configpath)
    print(config)

if __name__ == "__main__":
    default_config_path=os.path.join("..\config", "params.yml")
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()
    print(parsed_args)
    main(configpath=parsed_args.config, datasource=parsed_args.datasource)