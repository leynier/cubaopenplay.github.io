from hashlib import sha1
from json import dump
from os import makedirs


apps = {
    'apps': [
        'club.postdata.covid19cuba',
        'com.codestrange.www.cuba_weather',
        'com.cubanopensource.todo',
    ]
}


def main():
    result = {}
    makedirs('api', exist_ok=True)
    with open(f'api/apps.json', mode='w', encoding='utf-8') as file:
        dump(apps, file, ensure_ascii=False)
    with open('api/apps.json', encoding='utf-8') as file:
        text = file.read()
        cache = sha1(text.encode())
        result['hash'] = cache.hexdigest()
    with open(f'api/apps_hash.json', mode='w', encoding='utf-8') as file:
        dump(result, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
