#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Desk Organizer Mac - Módulo de Organização da pasta Downloads (~/Downloads).
Desenvolvido por: Daniel Júnior Barbosa da Silva (DL MIDIA) & Antigravity AI
"""

from __future__ import annotations

import os
import shutil
import unicodedata

DOWNLOADS = os.path.expanduser("~/Downloads")

DOWNLOAD_CATEGORIES = {
    "Instaladores e Compactados": [
        ".dmg", ".pkg", ".zip", ".rar", ".7z", ".tar.gz", ".tar", ".gz", ".iso", ".apk"
    ],
    "Documentos e PDFs": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".txt", ".rtf", ".pages", ".numbers", ".key"
    ],
    "Imagens e Fotos": [
        ".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff", ".ico", ".heic", ".raw"
    ],
    "Vídeos e Mídias": [
        ".mp4", ".mov", ".m4v", ".avi", ".mkv", ".webm", ".mp3", ".wav", ".m4a", ".flac"
    ],
    "Design e Vetores": [
        ".psd", ".psb", ".ai", ".svg", ".eps", ".cdr", ".indd", ".fig"
    ],
    "Códigos e Scripts": [
        ".py", ".js", ".ts", ".html", ".css", ".json", ".sql", ".sh", ".php", ".xml"
    ],
}

IGNORED_ITEMS = {
    ".DS_Store",
    ".localized",
} | set(DOWNLOAD_CATEGORIES.keys())


def norm(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def safe_move(src: str, dest_dir: str, item_name: str) -> str:
    os.makedirs(dest_dir, exist_ok=True)
    target = os.path.join(dest_dir, item_name)
    if not os.path.exists(target):
        shutil.move(src, target)
        return target

    base, ext = os.path.splitext(item_name)
    if base.lower().endswith(".tar"):
        base, ext2 = os.path.splitext(base)
        ext = ext2 + ext

    counter = 1
    while True:
        candidate = os.path.join(dest_dir, f"{base} ({counter}){ext}")
        if not os.path.exists(candidate):
            shutil.move(src, candidate)
            return candidate
        counter += 1


def classify_file(n_name: str) -> str | None:
    lower_name = n_name.lower()

    # Ignorar downloads parciais em andamento
    if lower_name.endswith((".crdownload", ".download", ".part", ".tmp")):
        return None

    for category, extensions in DOWNLOAD_CATEGORIES.items():
        if any(lower_name.endswith(ext) for ext in extensions):
            return category

    return "Documentos e PDFs"


def organize_downloads() -> int:
    if not os.path.exists(DOWNLOADS):
        return 0

    moved_count = 0

    for item in os.listdir(DOWNLOADS):
        n_item = norm(item)
        if item.startswith(".") or n_item in IGNORED_ITEMS:
            continue

        src_path = os.path.join(DOWNLOADS, item)

        # Não mexe em subpastas já criadas pelo usuário
        if os.path.isdir(src_path):
            continue

        dest_category = classify_file(n_item)
        if dest_category:
            dest_dir = os.path.join(DOWNLOADS, dest_category)
            safe_move(src_path, dest_dir, item)
            moved_count += 1

    return moved_count


if __name__ == "__main__":
    count = organize_downloads()
    if count == 0:
        print("Sua pasta Downloads já está limpa e organizada! ✨")
    elif count == 1:
        print("1 arquivo foi organizado na pasta Downloads! ✅")
    else:
        print(f"{count} arquivos foram organizados na pasta Downloads! ✅")
