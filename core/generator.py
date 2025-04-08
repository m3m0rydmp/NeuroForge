import random
import string
from core import storage
from threading import Thread

def substitute_characters(word):
    sub_map = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7'],
        'l': ['1']
    }
    results = ['']
    for char in word:
        new_results = []
        subs = sub_map.get(char.lower(), []) + [char]
        for res in results:
            for sub in subs:
                new_results.append(res + sub)
        results = new_results
    return results

def apply_dictionary_attack(keyword):
    return substitute_characters(keyword)

def apply_hybrid_rule_based(keyword):
    results = []
    for i in range(100, 1000):
        results.append(f"{i}{keyword}")
    return results

def apply_bruce_schneir(keyword):
    return [''.join(random.choice([c.upper(), c.lower(), random.choice('!@#$%123')]) for c in keyword)]

def apply_pao_method(keyword):
    if len(storage.keywords) < 3:
        return []
    person, action, obj = storage.keywords[:3]
    pao = person[:3].capitalize() + action[:3].capitalize() + obj[:3].capitalize()
    return [pao, pao.replace('i', '1').replace('o', '0').replace('a', '@')]

def generate(length, count):
    result = []

    def worker():
        while len(result) < count:
            technique = random.choice(['dict', 'hybrid', 'bruce', 'pao'])
            word = random.choice(storage.keywords) if storage.keywords else ''.join(random.choices(string.ascii_letters, k=6))

            if technique == 'dict':
                variations = apply_dictionary_attack(word)
            elif technique == 'hybrid':
                variations = apply_hybrid_rule_based(word)
            elif technique == 'bruce':
                variations = apply_bruce_schneir(word)
            elif technique == 'pao':
                variations = apply_pao_method(word)
            else:
                variations = [word]

            if not variations:
                continue

            pwd = random.choice(variations)
            pwd = pwd[:length]
            result.append(pwd)

    threads = [Thread(target=worker) for _ in range(4)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    storage.passwords.extend(result)
    return result