import re
import requests
import time
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = "https://starwars.fandom.com/api.php"

ENTITIES = {
    "characters": [
        "Darth_Vader", "Luke_Skywalker", "Leia_Skywalker_Organa_Solo", "Obi-Wan_Kenobi",
        "Darth_Sidious", "Yoda", "Anakin_Skywalker", "Han_Solo",
        "Boba_Fett", "Mace_Windu", "Padmé_Amidala_Naberrie"
    ],
    "planets": [
        "Tatooine", "Coruscant", "Naboo", "Endor",
        "Mustafar", "Hoth", "Dagobah", "Alderaan"
    ],
    "technology": [
        "Death_Star", "Lightsaber", "Hyperdrive",
        "Star_Destroyer", "X-wing_starfighter"
    ],
    "organizations": [
        "Jedi_Order", "Sith", "Galactic_Empire", "Rebel_Alliance"
    ],
    "events": [
        "Clone_Wars", "Order_66", "The_Force", "Galactic_Senate"
    ]
}

def clean_text(text: str) -> str:
    text = re.sub(r"\[\d+]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_article_text(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    content = soup.find("div", {"class": "mw-parser-output"})
    if not content:
        return ""

    paragraphs = content.find_all("p", recursive=False)
    texts = []
    for p in paragraphs:
        text = p.get_text(strip=True)
        if len(text) > 50:
            texts.append(clean_text(text))

    return "\n\n".join(texts)

def save_article(category: str, title: str, text: str):
    dir_path = Path("knowledge_base") / category
    dir_path.mkdir(parents=True, exist_ok=True)
    file_name = title.lower().replace(" ", "_") + ".md"
    file_path = dir_path / file_name

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# {title.replace('_', ' ')}\n\n")
        f.write(text)

    print(f"Saved: {file_path}")

def download_entity(category: str, entity: str):
    params = {
        "action": "parse",
        "page": entity.replace("_", " "),
        "format": "json",
        "prop": "text"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=15)
        response.raise_for_status()

        data = response.json()
        if "parse" in data and "text" in data["parse"]:
            html = data["parse"]["text"]["*"]
            article_text = extract_article_text(html)
            if article_text:
                save_article(category, entity, article_text)
            else:
                print(f"Empty article: {entity}")
        else:
            print(f"No content for {entity}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {entity}: {e}")

def main():
    for category, entities in ENTITIES.items():
        for entity in entities:
            download_entity(category, entity)
            time.sleep(1)  # пауза между запросами

if __name__ == "__main__":
    main()