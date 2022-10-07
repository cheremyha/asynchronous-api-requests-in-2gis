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


def get_connections_limit(file_name: str) -> int:
    """
    This function read connections limit from file and return it
    :param file_name: String with name of config file
    :return: Number with connections limit.
    """
    config = configparser.ConfigParser()
    config.sections()
    config.read(file_name)
    connections_limit_ = config['Simple Values']['connections_limit']

    # Convert from string to integer.
    connections_limit = int(connections_limit_)
    return connections_limit
