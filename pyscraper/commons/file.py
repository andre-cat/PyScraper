from io import TextIOWrapper

def print(path: str = '', name: str = 'file', type: str = '', text: str = '') -> None:
    if name == '' and type == '':
        name = 'file'
    elif type != '':
        type = '.' + type
    
    file: TextIOWrapper = open(f'{path}/{name}{type}', 'w', encoding='utf-8')
    file.write(text)
    file.close