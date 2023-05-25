import yaml

from account.service.config import Config
from account.service.service import AccountService


def main():
    with open("config.yml") as config_file:
        config = Config.parse_obj(yaml.safe_load(config_file))

    service = AccountService(config)
    service.run()


if __name__ == "__main__":
    main()
