from utils import get_setting


def test_get_database_name():
    global SETTINGS

    assert get_setting("DATABASE_NAME") == "default"


def test_get_modified_database_name_after_modifying_it():
    from utils import SETTINGS

    SETTINGS["DATABASE_NAME"] = "modified"

    assert get_setting("DATABASE_NAME") == "modified"
