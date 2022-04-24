import re
import sys

han_regex = re.compile(r'[\u3006\u3007\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002ebef\U00030000-\U0003134f]')

def is_han(c):
    return bool(han_regex.fullmatch(c))

n1 = sys.argv[1]
n2 = sys.argv[2]

with open(n1, encoding='utf-8') as f1, open(n2, encoding='utf-8') as f2:
    s1 = f1.read()
    s2 = f2.read()

assert len(s1) == len(s2)

total = 0
correct = 0

for c1, c2 in zip(s1, s2):
    is_han_c1 = is_han(c1)
    is_han_c2 = is_han(c2)
    assert is_han_c1 == is_han_c2
    if is_han_c1:
        total += 1
        if c1 == c2:
            correct += 1

print(f'Accuracy: {correct / total * 100:.6f}%')
