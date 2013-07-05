def save_tmp_file(str_, path):
    with open(path, 'w') as f:
        f.write(str_)


def load_tmp_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return content
