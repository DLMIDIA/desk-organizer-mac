#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Desk Organizer Mac - Orquestrador Completo (Mesa + Downloads).
Executa a organização inteligente simultânea do Desktop e da pasta Downloads no macOS.
Desenvolvido por: Daniel Júnior Barbosa da Silva (DL MIDIA) & Antigravity AI
"""

from __future__ import annotations

import subprocess
import sys
import os

from organizar_mesa import main as run_mesa
from organizar_downloads import organize_downloads


def main():
    print("=====================================================")
    print("🧹 Desk Organizer Mac — DL MIDIA")
    print("Organizador Inteligente de Mesa & Downloads para Mac")
    print("=====================================================")

    # 1. Organizar Mesa
    print("\n[1/2] Analisando e organizando a Área de Trabalho (Desktop)...")
    run_mesa()

    # 2. Organizar Downloads
    print("\n[2/2] Analisando e organizando a pasta Downloads...")
    down_count = organize_downloads()
    if down_count == 0:
        print("Sua pasta Downloads já está limpa e organizada! ✨")
    else:
        print(f"{down_count} arquivos organizados em Downloads! ✅")

    print("\n✨ Processo finalizado com sucesso!")


if __name__ == "__main__":
    main()
