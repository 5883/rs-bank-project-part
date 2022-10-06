# CRUD конфигурационными файлами
from configparser import ConfigParser
import os

prj_setting_ini = Project.Path + Project.Variables.setting_file_path

def create_config(path):
    """
    Создает файл конфигурации
    """
    config = ConfigParser()

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """
    Возвращает объект конфигурации
    """
    config = ConfigParser()
    if not os.path.exists(path):
        create_config(path)
        config = ConfigParser()
    config.read(path)
    return config


def get_setting(section, setting, path=prj_setting_ini):
    """
    Распечатать настройку
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )

    #    Log.Message(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Обновляет настройку
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    Удалить настройку
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)











