import configparser


def get_secret_api_key(file_name: str) -> str:
    """
    This function read secret api key from file and return it
    :param file_name: String with name of config file
    :return: String with secret api key.
    """
    config = configparser.ConfigParser()
    config.sections()
    config.read(file_name)
    secret_api_key = config['Simple Values']['key']
    return secret_api_key
