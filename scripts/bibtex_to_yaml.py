#!/usr/bin/env python3
"""Print publication YAML for a BibTeX file.

The site build does not run this script. Review the YAML and merge the records
you want into data/publications.yaml. Fields that BibTeX does not contain are
left blank.
"""

import sys
from pathlib import Path

import yaml


def parse_entries(text):
    entries = []
    i = 0
    while True:
        at = text.find("@", i)
        if at < 0:
            break
        brace = text.find("{", at)
        if brace < 0:
            break
        kind = text[at + 1 : brace].strip().lower()
        if kind in {"comment", "string", "preamble"}:
            i = brace + 1
            continue
        key_end = text.find(",", brace)
        key = text[brace + 1 : key_end].strip()
        fields, i = parse_fields(text, key_end + 1)
        entries.append((kind, key, fields))
    return entries


def parse_fields(text, start):
    fields = {}
    i = start
    while i < len(text):
        while i < len(text) and text[i] in " \t\r\n,":
            i += 1
        if i >= len(text) or text[i] == "}":
            return fields, i + 1
        name_end = text.find("=", i)
        name = text[i:name_end].strip().lower()
        i = name_end + 1
        while i < len(text) and text[i].isspace():
            i += 1
        value, i = parse_value(text, i)
        fields[name] = value
    return fields, i


def parse_value(text, i):
    if text[i] == "{":
        depth = 0
        start = i + 1
        while i < len(text):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    return clean(text[start:i]), i + 1
            i += 1
    if text[i] == '"':
        i += 1
        start = i
        while i < len(text) and text[i] != '"':
            i += 1
        return clean(text[start:i]), i + 1
    start = i
    while i < len(text) and text[i] not in ",}":
        i += 1
    return clean(text[start:i]), i


def clean(value):
    return " ".join(value.replace("\n", " ").split())


TYPE_MAP = {
    "article": "journal",
    "inproceedings": "conference",
    "conference": "conference",
    "incollection": "chapter",
    "inbook": "chapter",
    "misc": "preprint",
    "unpublished": "preprint",
}


def to_record(kind, key, fields):
    doi = fields.get("doi", "")
    if doi and not doi.startswith("http"):
        doi = "https://doi.org/" + doi
    venue = fields.get("journal") or fields.get("booktitle") or fields.get("howpublished") or ""
    year = fields.get("year") or ""
    try:
        year = int(year)
    except ValueError:
        year = year
    return {
        "id": key,
        "title": fields.get("title", ""),
        "authors": fields.get("author", ""),
        "year": year,
        "venue": venue,
        "detail": "",
        "type": TYPE_MAP.get(kind, "other"),
        "topics": [],
        "doi": doi,
        "url": fields.get("url", ""),
        "pdf": "",
        "code": "",
        "dataset": "",
        "featured": False,
        "open_access": False,
        "bibtex": "",
    }


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 scripts/bibtex_to_yaml.py papers.bib")
    text = Path(sys.argv[1]).read_text()
    records = [to_record(kind, key, fields) for kind, key, fields in parse_entries(text)]
    sys.stdout.write(
        "# Review this YAML before merging it into data/publications.yaml.\n"
        + yaml.safe_dump(records, allow_unicode=True, sort_keys=False, width=100)
    )


if __name__ == "__main__":
    main()
