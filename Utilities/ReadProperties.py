import configparser  # To read .ini configuration files
import os  # To interact with the operating system

config = configparser.RawConfigParser()  # Allows to load and read values from .ini files
# Getting the absolute path of the config.ini file
# os.path.dirname(__file__) gives the directory of the current file
# os.path.join is used to combine directory path with the config file path
# os.path.abspath gives the full path
config_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "/Users/jaypatel/PycharmProjects/NEAP/Configuration/config.ini"))
config.read(config_path)  # Reading the configuration file from given path


class ReadConfig:
    @staticmethod  # Calling the method without creating an object of the class
    def getApplicationUrl():
        url = config.get('common info', 'baseURL')  # Getting the value of 'baseURL' from the 'common info' section
        return url  # Returning the URL value
