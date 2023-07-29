import json
import os
from pathlib import Path

path = Path(__file__).parent / "datapack/data/blazeandcave/advancements/"

translateFile = input("Введи название файла с переводом (Пример: ru_ru.json): ") or "ru_ru.json"

with open(translateFile, encoding="utf-8") as f:
    lines = f.readlines()
    lines = [line for line in lines if not line.strip().startswith('#')]
    translateData = json.loads("".join(lines))

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(".json"):
            toTranslate = json.load(open(os.path.join(root, name), encoding="utf-8"))
            try:
                toTranslate['display']['title']['translate'] = translateData[toTranslate['display']['title']['translate']]
                toTranslate['display']['description']['translate'] = translateData[toTranslate['display']['description']['translate']]
                with open(os.path.join(root, name), 'w', encoding="utf-8") as f:
                    json.dump(toTranslate, f, ensure_ascii=False, sort_keys=True, indent=2)
            except Exception as e:
                if 'display' not in str(e):
                    print("(" + name + "): ", e)
