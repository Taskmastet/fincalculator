#!/usr/bin/env python3
"""Сборка single-file index.html: вшивает шрифты (base64) в исходник.
Запуск: python3 build.py
"""
import pathlib

src = pathlib.Path("index.src.html").read_text()
fonts = pathlib.Path("assets/fonts/inline-fonts.css").read_text()
out = src.replace("/*__FONTS__*/", fonts)
pathlib.Path("index.html").write_text(out)
print(f"built index.html: {len(out)} bytes (fonts {len(fonts)})")
