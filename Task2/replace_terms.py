import json
import re
from pathlib import Path
from shutil import copy2

KNOWLEDGE_BASE_DIR = Path("knowledge_base")
KNOWLEDGE_BASE_FINAL_DIR = Path("knowledge_base_final")
TERMS_MAP_PATH = Path("terms_map.json")


def load_terms_map():
    with open(TERMS_MAP_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_regex(term: str) -> re.Pattern:
    escaped = re.escape(term)

    pattern = rf"""
        (?:
            (?<![a-zA-Z])
            | (?<=[A-Z])
            | ^
        )
        {escaped}
        (?:
            (?![a-zA-Z])
            | (?=[A-Z])
            | $
        )
    """

    return re.compile(pattern, re.IGNORECASE | re.VERBOSE)


def replace_terms_in_text(text: str, terms_map: dict) -> str:
    sorted_terms = sorted(terms_map.items(), key=lambda x: len(x[0]), reverse=True)

    for original, replacement in sorted_terms:
        regex = build_regex(original)
        text = regex.sub(replacement, text)

    return text


def get_new_filename(file_path: Path, terms_map: dict) -> str:
    old_filename = file_path.stem
    old_filename_clean = old_filename.replace("_", " ").lower()
    sorted_terms = sorted(terms_map.items(), key=lambda x: len(x[0]), reverse=True)
    for original, replacement in sorted_terms:
        if original.lower() in old_filename_clean:
            return replacement.replace(" ", "_").lower()

    return old_filename

def process_file(file_path: Path, terms_map: dict):
    original_text = file_path.read_text(encoding="utf-8")
    replaced_text = replace_terms_in_text(original_text, terms_map)
    relative_path = file_path.relative_to(KNOWLEDGE_BASE_DIR)
    new_filename = get_new_filename(file_path, terms_map)
    target_dir = KNOWLEDGE_BASE_FINAL_DIR / relative_path.parent
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"{new_filename}.md"
    target_file.write_text(replaced_text, encoding="utf-8")

    print(f"Processed: {file_path} -> {target_file}")


def main():
    if not KNOWLEDGE_BASE_DIR.exists():
        print(f"Error: {KNOWLEDGE_BASE_DIR} does not exist")
        return

    terms_map = load_terms_map()

    KNOWLEDGE_BASE_FINAL_DIR.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    for file_path in KNOWLEDGE_BASE_DIR.rglob("*.md"):
        process_file(file_path, terms_map)
        processed_count += 1

    print(f"\nDone! Processed {processed_count} files to {KNOWLEDGE_BASE_FINAL_DIR}")

if __name__ == "__main__":
    main()