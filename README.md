# 🎯 ColorTracker

**Nájde v obraze z kamery objekt zadanej farby a povie, v ktorom kvadrante obrazovky sa nachádza.**

![Rok](https://img.shields.io/badge/rok-2017-blue) ![Python](https://img.shields.io/badge/Python-2.7-yellow) ![OpenCV](https://img.shields.io/badge/OpenCV-2.4-green) ![Stav](https://img.shields.io/badge/stav-archív-lightgrey)

> **Rok realizácie:** 2017 · **Tagy:** `opencv` `python` `color-tracking` `hsv` `object-tracking` `webcam` `computer-vision`

## O projekte

ColorTracker sleduje farebný objekt pred kamerou. Obraz sa rozdelí na štyri kvadranty a skript vypíše, kde sa objekt práve nachádza: **vľavo hore, vpravo hore, vľavo dole, vpravo dole**. Ide o základný stavebný kameň pre ovládanie robota, kamery na motorčeku alebo hry pohybom farebného predmetu.

## Ako to funguje

1. Snímka sa prevedie z BGR do farebného priestoru **HSV**, ktorý je odolnejší voči zmenám osvetlenia.
2. `cv2.inRange` vytvorí masku pixelov v zadanom rozsahu (`[10, 90, 10]` až `[254, 200, 100]`).
3. Odčítanie pozadia (MOG) ponechá len pohybujúce sa časti masky.
4. Kontúry väčšie ako 20 × 20 px dostanú rámik a stred.
5. Podľa stredu sa vypíše kvadrant. Okná `frame` a `mask` ukazujú výsledok aj masku.

## Spustenie

Vyžaduje **Python 2.7 a OpenCV 2.4**.

```bash
python hladajfarbu.py
```

`ESC` ukončí program. Zmena farby = úprava hodnôt `lower_red` a `upper_red` v HSV.

## Poznámky

- Rozlíšenie 640 × 480 je zadané pevne.
- Premenné sú pomenované „red“, ale rozsah je široký a zachytáva viac odtieňov, preto ho treba pre konkrétny predmet doladiť.

## Autor

**Vratislav Režo** ([@VRDragon](https://github.com/VRDragon))
