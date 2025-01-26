def create_user(user_id, config):
    f = open(f'{user_id}.txt', 'w+')
    for key in config:
        f.write(f'{key}={config[key]}\n')
    f.close()
