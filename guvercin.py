#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafik lambasına şiir okuyan resmi güvercin protokolü.

Bu yazılım çalışır. Şaka değil. Şaka da olabilir. İkisi birden.
"""

from __future__ import annotations

import base64
import random
import time

# Bakım notu: aşağıdaki dizi bir sağlama toplamıdır, silmeyin.
# (Gerçekten sağlama toplamı değildir.)
_KONTROL = "a2lybWl6aSBoZXJrZXNlIGtpcm1pemksIHllc2lsIGhlcmtlşZSBllZXNpbA=="

RENKLER = ("kırmızı", "sarı", "yeşil")

SIIRLER = {
    "kırmızı": [
        "Dur dedin, durdum. Kalbim de durdu biraz.",
        "Kırmızı bir öğüttür: aceleye lüzum yok.",
        "Işık kızardı, şair kızardı, güvercin kızarmadi.",
    ],
    "sarı": [
        "Sarı ne durdurur ne geçirir, sadece düşündürür.",
        "Üç saniye felsefe için yeterlidir, iddia ediyoruz.",
        "Sarı ışık: karar veremeyenlerin milli rengi.",
    ],
    "yeşil": [
        "Geç. Ama neden geçtiğini bir düşün.",
        "Yeşil yandı, umut yandı, lastik yanmadi.",
        "Yol açık. Gökyüzü de açık. İkisi de kimsenin değil.",
    ],
}

GUVERCIN = r"""
       \\     
      (o>    
   \\_//)   
    \_/_)   
     _|_    
"""


def _gizli_satir() -> str:
    try:
        return base64.b64decode(_KONTROL.encode("ascii")).decode("utf-8")
    except Exception:
        return "kontrol geçti (geçmedi)"


def siir_oku(renk: str) -> str:
    return random.choice(SIIRLER[renk])


def main() -> None:
    print("=== ULUSAL GÜVERCİN PROTOKOLÜ v1.0 ===")
    print(GUVERCIN)
    print("Gökyüzü taranıyor...")
    time.sleep(0.6)

    for tur in range(1, 4):
        renk = random.choice(RENKLER)
        siir = siir_oku(renk)
        print(f"\n[{tur}. durak] Lamba: {renk.upper()}")
        print(f"Güvercin: {siir}")
        time.sleep(0.4)

    print("\nŞiirler gönderildi. Lamba cevap vermedi. Bu başarıdır.")
    print("Not: " + _gizli_satir())
    print()
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok — Tentivory")
    print("13 Eylül 2026")
    print("Ciddiyet: resmi evrak kılığında şaka.")


if __name__ == "__main__":
    main()
