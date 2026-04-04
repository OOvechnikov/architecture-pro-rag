# Задание 3. Создание векторного индекса базы знаний

## Используемая эмбеддинг-модель

Для построения векторного индекса использована модель bge-base-en, так как она демонстрирует высокое качество семантического поиска и оптимальна для Retrieval-Augmented Generation.

| Параметр          | Значение                                |
| ----------------- | --------------------------------------- |
| Название модели   | BAAI / bge-base-en                      |
| Размер эмбеддинга | 768                                     |
| Язык              | English                                 |
| Ссылка            | https://huggingface.co/BAAI/bge-base-en |

## База знаний

Была использована база знаний по звездным войнам, преобразованная в соответствии с словарем терминов.

## Создание индекса

База знаний была преобразована в векторный индекс с использованием `FAISS`. Документы были разбиты на чанки, для которых с помощью модели `bge-base-en` были сгенерированы эмбеддинги размерности 768. Индекс поддерживает семантический поиск по пользовательским запросам и используется в дальнейшем RAG-пайплайне.

1. Перейти в директорию [Task3](./) и установить все зависимости из файла [requirements.txt](./requirements.txt)
```
cd Task3
pip install -r requirements.txt
```

2. Создать индекс
```
 python.exe .\build_index.py
```

- количество чанков в индексе - 7088
- время генерации векторов - 552

## Пример запроса к индексу

Для запроса к индексу используется скрипт [search.py](./search.py)

Пример:
```
python3 Task3/search.py 
Введите запрос: What is directive omega?      

Результаты поиска:

Score: 0.8573
Source: ..\Task2\knowledge_base_final\events\directive_omega.md
Text: # Directive Omega

Directive OmegaHistorical informationCreator(s)Null AdeptDate created32 BBYFirst employed19 BBY,Battle of Ringo Vinda(prematurely)19 BBY, following theduel in Malrex's officeOrganizational informationPurposeSecret protocolto execute themembersof theOrder of Axiomfortreasonagainst ...
--------------------------------------------------------------------------------
Score: 0.8453
Source: ..\Task2\knowledge_base_final\events\directive_omega.md
Text: Directive Omega, also known asClone Protocol 66,Protocol 66, or simply "the Order," was one of the top-secretcontingency ordersthat identified allAxiom Adeptastraitorsto theUnified Stellar Accordand, therefore, subject tosummary executionby theGrand Army of the Accord. The order was programmed into ...
--------------------------------------------------------------------------------
Score: 0.8400
Source: ..\Task2\knowledge_base_final\events\directive_omega.md
Text: While Directive Omega only explicitly targeted the Axiom Adept by claimingevery member of the Orderhad committed treason,the clones targeted non-Axiom Adept targets just as easily.Indeed, sectionCodicil Nineof Directive Omega made keeping Obsidian Path artifacts illegal.Despite having left the Order...
--------------------------------------------------------------------------------
Score: 0.8313
Source: ..\Task2\knowledge_base_final\events\directive_omega.md
Text: The backstory of Directive Omega was provided in a four-episode arc inThe Lost Missionsof the television seriesStar Wars: The Replication Conflicts.An Directive Omega flashback scene appeared in thefirst,fifth,andsixth episodesof theStar Wars: Obren Kaitelevisions series.WriterJoby Haroldwanted the ...
--------------------------------------------------------------------------------
Score: 0.8307
Source: ..\Task2\knowledge_base_final\events\directive_omega.md
Text: . The CVarekcellor issued Directive Omega to various cloneofficersacrossthe galaxy, which caused the Clones' inhibitor chips to activate and then brainwash them into viewing the Axiom Adept as traitors to the Accord and subsequently executing them, while Arkan—now the Null Lord Xarn Velgor—wassentto...
--------------------------------------------------------------------------------
```

