# Rapport des passes — conception v3 de la course « seuil et moniteurs », option (b) — v1

- Signé : rédacteur de la conception de la course seuil et moniteurs, modèle F. 2026-11-21 ; relevé de `date -u` : 07:26:18Z. Python 3.13.18.
- Statut : pièce de travail (classe C). Aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt, aucun commit, aucun lancement. Aucun refus de permission, de classifieur ni de garde.
- La v2 n'est pas touchée : sa table `empreintes-dossier-v2.txt` (`e66591ad315d6b585dbececac3c89ad91477219679d1325f58bfeb895bd96362`) reste vraie.

## 0. Verdict

1. **Passe 1 faite, égale à l'essai du contre-lecteur** : les quatre jeux portés tels quels, vingt-sept remplacements, les quatre sorties aux empreintes de son essai.
2. **Passe 2 faite** : seize remplacements pour les décisions de la mère de 07:24Z.
3. **Passe 3 faite** : onze remplacements de tenue.
4. **Noms de modèles et de fournisseurs qui restent dans les quatre pièces v3, dans le programme et dans sa sortie : 0.**
5. **Aucun total, aucun plafond, aucune ligne du devis ne change** : 20,77 / 97,41 / 114,48 USD ; ligne de calcul à demander 114,48.
6. La v3 n'est pas contre-lue : il lui faut le contrôle de son différentiel.

## 1. Pièces vérifiées avant d'agir

| pièce | empreinte, égale à son compagnon |
|---|---|
| contre-lecture de la v2, lue en entier : `docs/notes/ideation-seuil-moniteurs-v1/conception-v2/contre-lecture-v1/contre-lecture-conception-seuil-moniteurs-v2-v1.md` | `662f751006d7f23c887ea5fb4088bc93dd32521f77362b77f51ee13c099b44bf` |
| `corrections-v2-ordre-v1.json` | `b8cd6d1755f08a92f7c9353d63e63c3770b6b29ef1de3cd0dc3fc42979d006a6` |
| `corrections-v2-preenregistrement-v1.json` | `5d664d89ae30a17e14ac6ec3991ecd3a10b0eded4d588080455ff49721a7b830` |
| `corrections-v2-devis-v1.json` | `84e164618dac54919a60fa110885a25b91033310787f5c68e239e48c019214c8` |
| `corrections-v2-rapport-v1.json` | `27a4b757f1118baa8227d4faac16dfb3043f22c16572554153caf41bc0d7826d` |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` (recalculée ; compagnon non ouvert) |
| note du moniteur de dissonance, sur `origin/main` au commit `93e692b03433e87c16e09e47ab4e0d8f0eead648` | `403fe3e2827540569e45c82866eea98d91d977fad74d5c518f852c806e82fae2` |

## 2. Passe 1 — les quatre jeux tels quels

Chaque ancre comptée avant l'appel par `outils/compter_ancres_v1.py` (lecture seule, écrit pour cela) : **vingt-sept ancres, toutes à une occurrence** (14, 3, 4, 6).

| pièce v2 | remplacements | sortie de la passe 1 | empreinte de l'essai du contre-lecteur | égales |
|---|---|---|---|---|
| ordre | 14 | `917868dbb811e95ace1cee55e96f94e56b7444fa6171684f22600a6c488390b1` | `917868db…` | oui |
| préenregistrement court | 3 | `ee0bea7118efdf8dac4579d898b293613cf9a91b7a128236cf09c1abd86ae571` | `ee0bea71…` | oui |
| devis | 4 | `b984983c61c31178069cf9f4c2124426b4ffb8e031509deaa6c391ee49ce6be1` | `b984983c…` | oui |
| rapport | 6 | `3f9c4a676b54f19bef3b0d1346c2c2ff7c536b9e20df412f691acfe7b2776936` | `3f9c4a67…` | oui |

**Écart à la lettre, déclaré.** La consigne demandait `cmp` contre les fichiers de l'essai. Je n'ai pas leurs noms, et mon mandat m'interdit toute commande de liste. J'ai comparé l'empreinte SHA-256 de chaque sortie à celle que la contre-lecture donne pour son essai (§ 8) : les quatre sont égales. Si la mère veut le `cmp`, il lui suffit de me donner les quatre chemins.

## 3. Passe 2 — décisions de la mère (07:24Z)

Jeux à moi, dans `passe-2/` ; l'outil refuse toute ancre qui n'est pas à une occurrence, et les quatre appels ont rendu « FAIT ».

| décision | où elle est portée | remplacements |
|---|---|---|
| plus aucun nom de modèle : la mention de l'espèce retirée devient « le relais de l'espèce retirée est absent » | ordre v3, § 4, « Qui » | 1 |
| plus aucun nom de fournisseur : les deux parenthèses de la table des clés et « les relais … » deviennent « deuxième relais », « troisième relais » | devis v3, § 6 | 3 — **ajout de ma main**, au-delà de la lettre de la mère, pour que le compte soit nul |
| « clés désignées Minuit, Luc et Rigaud » | déjà fait par le jeu (devis § 6, rapport § 6) ; **vérifié : il n'en reste aucune autre forme** | 0 |
| D-M7 : trois points de GO-2026-11-21-15 — moniteur de dissonance, budget d'audit réparti selon la valeur, aiguillage en lecture rétrospective par texte à part | ordre v3, § 5, point 1 ; préenregistrement v3, « Hypothèse », point 3 ; rapport v3, D-M7 | 3 |
| D-M9 : l'affectation des lignées est la seule qui tient ; la clause de D-M4 tombe sous (b) | ordre v3, § 7, changement 1 (le jeu portait le raisonnement ; la passe 2 dit que la mère le retient) ; préenregistrement v3, « Ce qui reste », point 5 ; rapport v3, D-M9 | 3 |
| plafond de sortie des traducteurs fixé avec la lignée retenue, provision de réflexion comprise, au complément de valeurs | ordre v3, § 4 ; devis v3, § 4 (ligne de la table et alinéa) ; préenregistrement v3, « Ce qui reste », point 5 ; rapport v3, D-M9 | 2 de plus (devis) |
| la course est accordée avec le premier test de mort de la note du moniteur de dissonance ; chaque dépense garde son devis et sa ligne ; le monde à K actions du jumeau honnête est « sur devis à part » | ordre v3, § 7, changement 3 (deux remplacements) ; devis v3, § 7, point 5 ; préenregistrement v3, « Ce qui reste », point 7 | 4 |
| fait faux du § 2.1 | déjà corrigé par le jeu. **Vérifié par moi** au commit `93e692b0…` : `git cat-file -e` trouve sur `origin/main` le fichier `course2_v68.py` du paquet et les lanceurs 9 et 10 | 0 |
| programme v3 qui arrondit vers le haut | **non écrit** (facultatif). 75,77 et 114,07 sont écrits à la main au devis v3, § 3, dits comme tels par le jeu ; l'en-tête du devis v3 le redit | 0 |

Total de la passe 2 : 5 (ordre) + 6 (devis) + 3 (préenregistrement) + 2 (rapport) = **16**.

**Une lecture de ma main, à confirmer.** La mère dit que D-M7 « porte les trois points » : dissonance, budget d'audit, aiguillage. J'en ai tiré que le seuil certifié avec sa bande de seuils et le seuil unique sur score normalisé, que la v2 mettait aussi dans la liste, **passent par le tirage**. C'est écrit dans l'ordre v3, § 5, comme « lecture du rédacteur ». Si la mère voulait les garder nommés, la liste compte cinq entrées et une ligne est à changer.

**Sur la note du moniteur de dissonance.** Je n'en ai lu que les titres et les lignes qui portent ses tests de mort. Elle prévoit, sur devis à part, un monde par substitution sur MATH500 pour son test de mort n° 1 ; elle dit elle-même n'avoir lu aucun prix. Rien d'elle n'entre dans le devis de cette course.

## 4. Passe 3 — tenue

Titre en « v3 » ; ligne de version (« la v3 remplace la v2 (…) après la contre-lecture `662f7510…`, jeux portés tels quels », avec l'empreinte de la sortie de la passe 1 et le relevé de `date -u`) ; statut ; au préenregistrement, la section « Contre-lecture » dit celle de la v2 faite et celle de la v3 à faire. 3 + 3 + 3 + 2 = **11** remplacements.

**Un choix de tenue, dit.** Dans le corps des textes, les renvois « ordre de course v2 », « devis v2 », « rapport v2 » sont nombreux et répétés : l'outil refuse une ancre qui figure plus d'une fois. Je ne les ai pas réécrits un par un ; la ligne de version de chaque pièce porte la règle de lecture « v2 se lit v3 », comme le devis v6 de la course « nouvelles attaques » le faisait pour ses propres renvois. Le calcul reste le programme v2 et sa sortie, inchangés.

## 5. Le compte des noms

`grep -c -i` sur une liste de dix-huit noms de modèles et de fournisseurs, pièce par pièce :

| pièce | lignes trouvées |
|---|---|
| `ordre-course-seuil-et-moniteurs-v3.md` | 0 |
| `devis-course-seuil-et-moniteurs-v3.md` | 0 |
| `preenregistrement-court-course-seuil-et-moniteurs-v3.md` | 0 |
| `rapport-redacteur-conception-seuil-et-moniteurs-v3.md` | 0 |
| `calcul_devis_course_seuil_et_moniteurs_v2.py` | 0 |
| `calcul-devis-course-seuil-et-moniteurs-v2.json` | 0 |

**Ce qui en porte encore, par nature, et qui n'est pas une pièce à servir** : les quatre différentiels (leurs lignes retirées citent la v2) ; mon jeu `passe-2-ordre-v1.json` (son ancre) ; les journaux de remplacements de l'outil, s'ils recopient les ancres. La v1 et la v2, non touchées, en portent aussi. Les désignations de clés au registre (Minuit, Luc, Rigaud) restent : ce ne sont pas des noms de modèles.

## 6. Ce que je n'ai pas fait

- Aucune relecture en entier des quatre pièces v3 après les passes : j'ai vérifié les ancres, les empreintes, le compte des noms et la taille des différentiels (19, 13, 10 et 10 lignes ajoutées).
- Aucun `cmp` contre les fichiers de l'essai (§ 2).
- Aucun programme v3.
- La table d'empreintes v3 est à côté : `empreintes-dossier-v3.txt`.
