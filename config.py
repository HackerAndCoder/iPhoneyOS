import yaml

with open('config.yml') as f:
    config_file = yaml.safe_load(f.read())

def get_value(name):
    return config_file[name]

def set_value(name, value):
    config_file[name] = value
    with open('config.yml', 'w') as f:
        f.write(config_file)

def get_string(name):
    return str(get_value(name))

def get_int(name):
    return int(get_value(name))

def get_bool(name, default : bool = False):
    value = get_string(name).lower()
    if value == 'true':
        return True
    elif value == 'false':
        return False
    else:
        return default