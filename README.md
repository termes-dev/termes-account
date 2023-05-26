# Termes Account Service

This is a part of [Termes Server](https://github.com/termes-dev/termes)

- Config example: [config_example.yml](config_example.yml)
- Dockerfile: [Dockerfile](Dockerfile)

Before running service first create config file (`config.yml`)

If you're running with Docker, mount `config.yml` to `/termes-account/config.yml`

Also, you can run this service without docker:
```bash
pip install --upgrade -r requirements.txt
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"
python3 -m account.service
```

### Dependencies:
- [ReNats](https://github.com/Respirens/renats) - communication over NATS
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) - ORM
- [Pydantic](https://github.com/pydantic/pydantic) - data validation
- [PyYAML](https://github.com/yaml/pyyaml) - configuration in YAML format