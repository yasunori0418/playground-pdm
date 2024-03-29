from loguru import logger
from functools import wraps
import sys
import os
import tomllib
import pprint


def log():
    def log_wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            logger.remove()
            log_format: str = (
                "<level>{level}</level> | <cyan>{extra[func]}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
            )
            func_name = func.__name__
            custom_logger = logger.bind(func=func.__name__)
            custom_logger.add(sys.stdout, format=log_format)
            custom_logger.debug("start")
            custom_logger.info(f"function name: {func_name}")
            with custom_logger.catch(
                level="CRITICAL", message="exception test message"
            ):
                result = func(*args, **kwargs)
            custom_logger.debug("end")
            return result

        return wrap

    return log_wrapper


@log()
def test_deco():
    print("デコレーターテスト")


@log()
def toml_load():
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, "config.toml"), "rb") as file:
        toml_data = tomllib.load(file)
    pprint.pprint(toml_data)


if __name__ == "__main__":
    test_deco()
    toml_load()
