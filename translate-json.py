import json
import deepl
from collections import OrderedDict
from deep_translator import DeeplTranslator
from deep_translator import GoogleTranslator

auth_key = "9d5616c8-1c80-11f8-ab78-b98188f57c23:fx"  # info@antropoloops
translator = deepl.Translator(auth_key)



file = open('/Users/antropoloops/Desktop/antropoloops/Box Sync/00 jsons/sesion-dance2022.json')
albumJson = json.load(file)
songs = list(albumJson.keys())
# print(songs)
for song in songs:
    if albumJson[song]['comentario']:
        comment = albumJson[song]['comentario']
        # print(comment)
        comment_es = translator.translate_text(comment, target_lang='ES')
        # comment_es = DeeplTranslator(api_key="9d5616c8-1c80-11f8-ab78-b98188f57c23:fx", source="auto", target="es", use_free_api=True).translate(
        #     comment)
        print(comment_es)
        albumJson[song]['comentario'] = comment_es.text

print(albumJson)

with open('/Users/antropoloops/Desktop/antropoloops/Box Sync/00 jsons/sesion-dance2022-ES.json', 'w') as fp:
    json.dump(albumJson, fp, sort_keys=True, indent=4, ensure_ascii=False)