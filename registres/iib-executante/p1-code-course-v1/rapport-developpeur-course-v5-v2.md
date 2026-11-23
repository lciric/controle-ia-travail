# Rapport du développeur — code de la course de l'organisme retenu, version 5 (P1) — v2

Date : 2026-11-22. Pièce d'instrument (classe B). Même développeur (Claude Opus 5.5), même cadre. Ce rapport complète la v1
(`rapport-developpeur-course-v5-v1.md`, intacte), qui reste valable pour les correctifs 0014 à 0017. Ces correctifs ne sont pas
changés : un contre-lecteur les lit déjà. Rien poussé, rien dépensé, aucune machine, aucun modèle téléchargé.

- Tête : **`2d0d3fa509b9df3f6927e4fdd64e46d0b4425be3`**, arbre **`93b4e384ebd6b20e05cfec5c00819b539aecfbb0`** ; correctif `0018-…patch` (`git format-patch --start-number 18 ae1c76aa1..HEAD`), à appliquer après 0014 à 0017.

## 1. Correctif 0018 — graines de la course sous un préfixe propre (section 14, suivie à la lettre ; R9)

- **Constat.** La configuration scellée de l'étalonnage (`config-iib-organisme-retenu-v5-etalonnage-v2.json`) porte `prefixe_graines = ""`, et la course reprenait ce même préfixe. La section 14 dit « la course dérive ses clés de la même entropie sous un préfixe propre ».
- **Aucune règle du texte n'est changée.** La correction ne touche que le préfixe des clés de la course. Les noms des clés, l'entropie, les seuils et l'étalonnage déjà joué restent tels quels, et la configuration de l'étalonnage reste intacte.
- **`designation_v5.py`, l. 97 à 123** :
  - `PREFIXE_DE_LA_COURSE = "course/"` ;
  - `prefixe_de_la_course(config)` rend le préfixe de l'étalonnage suivi de `course/`, et refuse un préfixe égal à celui de l'étalonnage ;
  - `configuration_de_course` écrit ce préfixe dans la configuration dérivée de la course. Les tours, les témoins, l'évaluation et le distillateur (qui lit `course["prefixe_graines"]`) tirent donc tous sous lui.
- **`lanceur_v5.py`** :
  - l. 426 : `phase_course` refuse une configuration de course dont le préfixe n'est pas le préfixe propre ;
  - l. 734 : le manifeste du run de course tire sous le préfixe propre.
- **Essais** (`tests/test_iib_distillation_bout_en_bout_v5.py`, +2) :
  - **cas sain** : toutes les clés de `manifeste-course-iib-v5.json` et de `distillation-iib-v5.json` commencent par le préfixe propre ; elles sont disjointes de celles de l'étalonnage ; l'entropie est la même ; la configuration de l'étalonnage reste intacte ; le préfixe vide de la configuration réelle donne `course/` ;
  - **artefacts** : le suffixe vide est refusé ; une configuration de course qui reprend le préfixe de l'étalonnage est refusée avant le premier tour.
- La liste figée v6 rend maintenant 290 essais (`ATTENDUS = 290` dans la répétition). La liste de la course rend 292 sur une machine qui a torch.

## 2. L'essai du moteur à torch du distillateur — joué

- **Environnement à part**, dans le bloc-notes (`…/scratchpad/venv-torch-cpu`) :
  - torch 2.14.1+cpu, depuis l'index CPU de PyTorch ;
  - transformers 5.18.0, tokenizers 0.23.2, safetensors 0.8.0, scipy 1.17.1, numpy 2.4.6, matplotlib 3.11.2, huggingface_hub 1.33.0, pytest 9.1.1, soit les versions de `requirements-gpu.txt`.
- **Aucun modèle téléchargé.** L'essai construit un petit Llama à poids aléatoires (`modele_v1.petit_llama`) ; il est joué avec `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`.
- **Ce qu'il fait** : il joue `MoteurTorch` en entier, sur processeur. Injection, simple précision, entraînement, sauvegarde en demi-précision puis recharge, contrôle d'identité à dose 0 et à dose 1, doses, empreintes. Il vérifie aussi la constante `IGNORE` et l'égalité des transcriptions avec le code de l'organisme (ii).
- **Résultat** : `tests/test_iib_distillation_torch_v5.py`, **2 réussis en 54 s**, au premier passage.
  - Réserve R4 : un essai écrit sans avoir pu être joué, qui passe du premier coup, ne prouve pas que le moteur soit juste sur carte. Restent non éprouvés : le modèle réel de 8 milliards de paramètres, la mémoire de la carte, la demi-précision sur CUDA, `MondeReel`, et `motifs_de_la_course` sur la consigne réelle.
- **Liste figée de la course rejouée entière dans cet environnement** (v6 plus l'essai du moteur) : **292 réussis en 11 min 30** (`sortie-essais-p1-v2.txt`, dernière ligne « 292 passed »).

## 3. Ce qui reste ouvert (mis à jour par rapport à la v1, § 4)

- Le point 1 de la v1 (moteur à torch jamais joué) est levé sur processeur. Il reste à le jouer sur carte : il est dans la liste de la course, donc il se joue aux premières minutes de la machine de la course.
- Le point 6 de la v1 (préfixe propre) est corrigé par 0018. Ce n'est plus un nœud.
- Restent, tels qu'écrits dans la v1 :
  - nœud C1 (une ou deux machines) ;
  - nœud C2 (ligne de GO de la course) ;
  - calendrier (dernière création le 26 novembre) ;
  - lecture « gardée » de la première action, à confirmer par la mère ;
  - le mode réel, non éprouvé ;
  - ce que l'ordre de la course devra porter : `TESTS_ATTENDUS=292` pour la liste de la course, et 290 pour la liste de l'étalonnage v6.

## 4. Livrables v2
- `0018-…patch` ;
- `rapport-developpeur-course-v5-v2.md` ;
- `sortie-essais-p1-v2.txt`, liste de la course, 292 attendus, torch compris.

Arbre final : `93b4e384ebd6b20e05cfec5c00819b539aecfbb0`.
