import os


def gen_models():
    db_url = "mysql://root:123456@localhost:3306/db_auth?charset=utf8"
    current_path = os.getcwd()
    model_path = os.path.join(current_path, 'models','models.py')
    cmd = 'flask-sqlacodegen --flask {}'.format(db_url)
    try:
        output = os.popen(cmd)
        content = str(output.read())
        with open(model_path, 'w+',encoding='utf-8') as f:
            f.write(content)
        print('Generated database models successfully')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    gen_models()