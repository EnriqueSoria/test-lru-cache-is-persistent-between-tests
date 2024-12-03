from functools import lru_cache


SETTINGS = {"DATABASE_NAME": "default"}


@lru_cache
def get_setting(key):
    return SETTINGS[key]
