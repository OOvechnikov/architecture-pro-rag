# Задание 6. Автоматическое ежедневное обновление базы знаний

## Скрипт обновления индекса

Скрипт обновления индекса [update_index.py](./update_index.py) работает в соответствии со следующим алгоритмом:
1. Проверяет директорию [docs](./docs/) на наличие новых документов, которые отсутствуют в метаданных индекса
2. Если обнаруживает новые документы, то дозаписывает их в индекс (изменение и удаление не реализовано в силу его трудоемкости при использовании `FAISS`)


## Настройка периодического запуска

Для настройки периодического запуска скрипта [update_index.py](./update_index.py) через cron был выполнен следующий набор команд:
```
cd Task6
pip install -r requirements.txt

py.exe .\scheduler.py
```

В результате скрипт запускается каждые 10 минут и сохраняет лог в [logs/index_update.log](./logs/index_update.log) в следующем формате:

```
2026-04-05 10:10:49,720 [INFO] Start time: 2026-04-05 10:10:49.720851
2026-04-05 10:10:49,768 [INFO] Use pytorch device_name: cpu
2026-04-05 10:10:49,768 [INFO] Load pretrained SentenceTransformer: BAAI/bge-base-en
2026-04-05 10:10:50,309 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/modules.json "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:50,340 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/modules.json "HTTP/1.1 200 OK"
2026-04-05 10:10:50,500 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/config_sentence_transformers.json "HTTP/1.1 307 Temporary Redirect"
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-04-05 10:10:50,501 [WARNING] Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
2026-04-05 10:10:50,530 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/config_sentence_transformers.json "HTTP/1.1 200 OK"
2026-04-05 10:10:50,685 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/config_sentence_transformers.json "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:50,716 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/config_sentence_transformers.json "HTTP/1.1 200 OK"
2026-04-05 10:10:50,877 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/README.md "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:50,904 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/README.md "HTTP/1.1 200 OK"
2026-04-05 10:10:51,069 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/modules.json "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:51,099 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/modules.json "HTTP/1.1 200 OK"
2026-04-05 10:10:51,264 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/sentence_bert_config.json "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:51,321 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/sentence_bert_config.json "HTTP/1.1 200 OK"
2026-04-05 10:10:51,508 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/adapter_config.json "HTTP/1.1 404 Not Found"
2026-04-05 10:10:51,873 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/config.json "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:51,969 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/config.json "HTTP/1.1 200 OK"

Loading weights:   0%|          | 0/199 [00:00<?, ?it/s]
Loading weights: 100%|##########| 199/199 [00:00<00:00, 6957.87it/s]
[1mBertModel LOAD REPORT[0m from: BAAI/bge-base-en
Key                     | Status     |  | 
------------------------+------------+--+-
embeddings.position_ids | UNEXPECTED |  | 

Notes:
- UNEXPECTED:	can be ignored when loading from different task/architecture; not ok if you expect identical arch.
2026-04-05 10:10:52,294 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/config.json "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:52,324 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/config.json "HTTP/1.1 200 OK"
2026-04-05 10:10:52,485 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/tokenizer_config.json "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:52,515 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/tokenizer_config.json "HTTP/1.1 200 OK"
2026-04-05 10:10:52,682 [INFO] HTTP Request: GET https://huggingface.co/api/models/BAAI/bge-base-en/tree/main/additional_chat_templates?recursive=false&expand=false "HTTP/1.1 404 Not Found"
2026-04-05 10:10:52,844 [INFO] HTTP Request: GET https://huggingface.co/api/models/BAAI/bge-base-en/tree/main?recursive=true&expand=false "HTTP/1.1 200 OK"
2026-04-05 10:10:53,102 [INFO] HTTP Request: HEAD https://huggingface.co/BAAI/bge-base-en/resolve/main/1_Pooling/config.json "HTTP/1.1 307 Temporary Redirect"
2026-04-05 10:10:53,133 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/BAAI/bge-base-en/b737bf5dcc6ee8bdc530531266b4804a5d77b5d8/1_Pooling%2Fconfig.json "HTTP/1.1 200 OK"
2026-04-05 10:10:53,298 [INFO] HTTP Request: GET https://huggingface.co/api/models/BAAI/bge-base-en "HTTP/1.1 200 OK"
2026-04-05 10:10:53,649 [INFO] Added 2 new chunks to index
2026-04-05 10:10:53,775 [INFO] Index stats: vectors=7091, file_size=20.77 MB
2026-04-05 10:10:53,781 [INFO] End time: 2026-04-05 10:10:53.781788
2026-04-05 10:10:53,782 [INFO] Total time: 4
```

## Архитектурная диаграмма

[Архитектурная диаграмма](./arch.puml)

<div align="center">

![Архитектурная диаграмма](./arch.png)

</div>