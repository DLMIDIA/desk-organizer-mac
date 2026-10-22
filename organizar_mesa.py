#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script automático para organizar a Mesa (Desktop) do Mac em 7 categorias.
Executado pelo aplicativo 'Organizar Mesa.app'.
"""

from __future__ import annotations

import os
import shutil
import unicodedata

DESKTOP = os.path.expanduser("~/Desktop")

MAIN_FOLDERS = {
    "01 - Projetos & Sistemas",
    "02 - Orçamentos & Contratos",
    "03 - Fotos, Vídeos & Drone",
    "04 - Design & Artes",
    "05 - Documentos & PDFs",
    "06 - Capturas e Gravações de Tela",
    "07 - Backups & Arquivos",
}

SUBFOLDERS_TO_ENSURE = [
    "01 - Projetos & Sistemas",
    "01 - Projetos & Sistemas/Scripts Python (Tucunare)",
    "02 - Orçamentos & Contratos",
    "03 - Fotos, Vídeos & Drone",
    "03 - Fotos, Vídeos & Drone/Mídias Soltas",
    "04 - Design & Artes",
    "04 - Design & Artes/Editáveis (PSD, AI, SVG)",
    "04 - Design & Artes/Peças e Imagens",
    "05 - Documentos & PDFs",
    "06 - Capturas e Gravações de Tela",
    "06 - Capturas e Gravações de Tela/Capturas de Tela (Prints)",
    "06 - Capturas e Gravações de Tela/Gravações de Tela (Vídeos)",
    "07 - Backups & Arquivos",
]

IGNORED_ITEMS = {
    ".DS_Store",
    ".localized",
    "Organizar Mesa.app",
} | MAIN_FOLDERS


def norm(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def safe_move(src: str, dest_dir: str, item_name: str) -> str:
    os.makedirs(dest_dir, exist_ok=True)
    target = os.path.join(dest_dir, item_name)
    if not os.path.exists(target):
        shutil.move(src, target)
        return target

    base, ext = os.path.splitext(item_name)
    # Handle .tar.gz
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


def classify_directory(dir_path: str, n_name: str) -> str | None:
    lower_name = n_name.lower()

    # Pastas do Google Drive não sincronizadas
    if lower_name.startswith("google drive (not synced)"):
        return "07 - Backups & Arquivos"

    # Pastas de orçamento, proposta ou contrato
    if any(k in lower_name for k in ("orcamento", "orçamento", "proposta", "contrato", "minuta")):
        return "02 - Orçamentos & Contratos"

    # Inspecionar arquivos internos para classificar pastas novas automaticamente
    try:
        entries = [norm(e) for e in os.listdir(dir_path) if e not in (".DS_Store", ".localized")]
    except PermissionError:
        return None

    if not entries:
        # Remove automaticamente "pasta sem título" vazia
        if lower_name.startswith("pasta sem título") or lower_name.startswith("untitled folder"):
            try:
                shutil.rmtree(dir_path)
            except Exception:
                pass
        return None

    lower_entries = [e.lower() for e in entries]

    # Projeto de código / site
    if any(
        e in ("package.json", "index.html", "index.php", "tsconfig.json", "requirements.txt", ".git")
        or e.endswith((".py", ".js", ".ts", ".php", ".apk"))
        for e in lower_entries
    ):
        return "01 - Projetos & Sistemas"

    # Design
    if any(e.endswith((".psd", ".ai", ".svg", ".eps", ".fig")) for e in lower_entries):
        return "04 - Design & Artes"

    # Fotos, vídeos ou drone
    if any(
        e.endswith((".mp4", ".mov", ".arw", ".cr2", ".cr3", ".dng", ".kmz", ".gpkg"))
        or e.startswith(("dji_", "img_", "dsc"))
        for e in lower_entries
    ):
        return "03 - Fotos, Vídeos & Drone"

    # Documentos
    if any(e.endswith((".pdf", ".docx", ".doc", ".xlsx", ".pptx")) for e in lower_entries):
        return "05 - Documentos & PDFs"

    return None


def classify_file(n_name: str) -> str | None:
    lower_name = n_name.lower()

    # Ignorar downloads em andamento
    if lower_name.endswith((".crdownload", ".download", ".part", ".tmp")):
        return None

    # 1. Capturas de Tela
    if lower_name.startswith(("captura de tela", "screen shot", "screenshot", "fundo de captura de tela")):
        return "06 - Capturas e Gravações de Tela/Capturas de Tela (Prints)"

    # 2. Gravações de Tela
    if lower_name.startswith(("gravação de tela", "screen recording")):
        return "06 - Capturas e Gravações de Tela/Gravações de Tela (Vídeos)"

    # 3. Orçamentos, Propostas e Contratos avulsos
    if any(k in lower_name for k in ("orcamento", "orçamento", "proposta", "contrato", "minuta")):
        return "02 - Orçamentos & Contratos"

    # 4. Scripts e código
    if lower_name.endswith((".py", ".js", ".ts", ".sh", ".sql", ".php", ".html", ".css", ".json")):
        return "01 - Projetos & Sistemas/Scripts Python (Tucunare)"

    # 5. Backups, compactados e instaladores
    if lower_name.endswith((".tar.gz", ".tgz", ".zip", ".rar", ".7z", ".tar", ".gz", ".dmg", ".pkg", ".iso", ".ffs_gui", ".apk")):
        return "07 - Backups & Arquivos"

    # 6. Editáveis de Design
    if lower_name.endswith((".psd", ".psb", ".ai", ".svg", ".eps", ".cdr", ".indd", ".fig")):
        return "04 - Design & Artes/Editáveis (PSD, AI, SVG)"

    # 7. Vídeos, Áudios e Fotos brutas de Câmera/Drone
    if (
        lower_name.endswith((".mov", ".mp4", ".m4v", ".avi", ".mkv", ".mp3", ".wav", ".m4a", ".arw", ".cr2", ".cr3", ".nef", ".dng", ".heic"))
        or lower_name.startswith(("dji_", "img_", "dsc"))
    ):
        return "03 - Fotos, Vídeos & Drone/Mídias Soltas"

    # 8. Documentos, PDFs, Planilhas e Textos
    if lower_name.endswith((".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".txt", ".md", ".rtf", ".pages", ".numbers", ".key")):
        return "05 - Documentos & PDFs"

    # 9. Imagens e Peças Gráficas (.png, .jpg, .webp, etc.)
    if lower_name.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff", ".ico")):
        return "04 - Design & Artes/Peças e Imagens"

    # Outros arquivos avulsos vão para Documentos & PDFs
    return "05 - Documentos & PDFs"


def main():
    for folder in SUBFOLDERS_TO_ENSURE:
        os.makedirs(os.path.join(DESKTOP, folder), exist_ok=True)

    moved_count = 0

    for item in os.listdir(DESKTOP):
        n_item = norm(item)
        if item.startswith(".") or n_item in IGNORED_ITEMS or n_item.endswith(".app"):
            continue

        src_path = os.path.join(DESKTOP, item)
        dest_rel = None

        if os.path.isdir(src_path):
            dest_rel = classify_directory(src_path, n_item)
        elif os.path.isfile(src_path):
            dest_rel = classify_file(n_item)

        if dest_rel:
            dest_dir = os.path.join(DESKTOP, dest_rel)
            safe_move(src_path, dest_dir, item)
            moved_count += 1

    if moved_count == 0:
        print("Sua Mesa já está 100% organizada! ✨")
    elif moved_count == 1:
        print("1 item foi organizado na sua Mesa! ✅")
    else:
        print(f"{moved_count} itens foram organizados na sua Mesa! ✅")


if __name__ == "__main__":
    main()
