from io import TextIOWrapper

def print(path: str = '', name: str = 'file', type: str = 'txt', text: str = '') -> None:
    file: TextIOWrapper = open(f'{path}/{name}.{type}', 'w', encoding='utf-8')
    file.write(text)
    file.close