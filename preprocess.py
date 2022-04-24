import json
import re

han_regex = re.compile(r'[\u3006\u3007\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002ebef\U00030000-\U0003134f]')

def has_han(s):
    return bool(han_regex.search(s))

with open('ChatExport.json', encoding='utf-8') as f:
    o = json.load(f)

with open('answer.txt', 'w', encoding='utf-8') as f:
    for message in o['messages']:
        if message['text'] and isinstance(message['text'], str):
            for line in message['text'].split('\n'):
                for sentence in re.split(r'(?<=[。！？])', line):
                    if has_han(sentence):
                        print(sentence, file=f)
