import json
import os
from pathlib import Path

path = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent

translateFile = input("Введи название файла с переводом (Пример: ru_ru.json): ")
translateData = json.load(open(translateFile, encoding="utf-8"))

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(".json"):
            try:
                with open(os.path.join(root, name), 'r', encoding="utf-8") as f:
                    toTranslate = json.load(f)
                toTranslate['display']['title']['translate'] = translateData[toTranslate['display']['title']['translate']]
                toTranslate['display']['description']['translate'] = translateData[toTranslate['display']['description']['translate']]
                with open(os.path.join(root, name), 'w', encoding="utf-8") as f:
                    json.dump(toTranslate, f, ensure_ascii=False, sort_keys=True, indent=2)
            except Exception as e:
                if 'display' not in str(e):
                    print("(" + name + "): ", e)
