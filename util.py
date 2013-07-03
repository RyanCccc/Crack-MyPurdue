def save_tmp_file(str_, path):
    with open(path, 'w') as f:
        f.write(str_)
        f.close()
