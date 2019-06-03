from common.log import logger
from config import Config
from dog import Dog

if __name__ == '__main__':
    # config
    config = Config.load()
    logger.debug(config.dumps())
    config.save()
    # dog
    dog = Dog()
    dog.run()
