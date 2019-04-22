import json
import os

from common.jsonn import JsonSerializable
from common.logger import logger


class Config(JsonSerializable):
    def __init__(self, **entries):
        self.access_key = ''
        self.access_passwd = ''
        self.domain = ''
        self.rr = ''
        if entries:
            self.__dict__.update(entries)

    @classmethod
    def load(cls) -> 'Config':
        path = 'config.json'
        if not os.path.exists(path):
            return Config()
        with open(path, 'r') as f:
            dic = json.load(f)
            return Config(**dic)

    def save(self):
        path = 'config.json'
        with open(path, 'w') as f:
            f.write(self.dumps())


if __name__ == '__main__':
    config = Config.load()
    logger.debug(config.dumps())
    config.save()
