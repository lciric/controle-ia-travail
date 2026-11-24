# Contre-lecture (classe B) — règles de forme du gabarit v2, code et tests

Contre-lecteur neuf (Claude Sonnet 5.5). Pièces lues : `prereg/gabarit-preregistrement-v2.md`, ajout en fin de `src/controle_ia/prereg.py` (lignes 78 à 129), `tests/test_prereg_forme_v2.py`.

## Verdict : tient avec corrections

Constats positifs vérifiés : `git diff origin/main -- prereg/gabarit-preregistrement-v1.md` est vide ; le diff de `prereg.py` ne contient que des ajouts (fonctions existantes intactes) ; les 15 tests de `test_prereg_forme_v2.py` et `test_prereg.py` passent ; les dix étiquettes sont fidèles à la liste (statistique et seuil uniques ; hypothèses complémentaires ; effectif par puissance avec « non exécutable » ; nul de la maximisation refaite ; comparateur de même capacité et budget ; unité indépendante et règle de trois ; extracteurs figés avant la coupure ; amputation placebo et réécriture hétérogène ; seuils sur générateurs disjoints ; lot d'étalonnage distinct). Le venv `.venv` n'existe pas dans ce conteneur : les tests ont tourné avec `PYTHONPATH=src` et le Python système.

## Remarques

1. **À corriger** — `prereg/gabarit-preregistrement-v2.md:5` : le gabarit dit « puis sceller avec `controle_ia.prereg.sceller_prereg` ». Cette fonction (v1) ne contrôle pas les règles de forme ; un texte v2 scellé ainsi passe sans contrôle. Correction : « sceller avec `sceller_prereg_v2` ».

2. **À corriger** — `prereg.py:106` : règle écrite sur plusieurs lignes. Une ligne `- **Effectif par analyse de puissance** :` suivie de la mise en œuvre à la ligne (ou sur lignes de continuation indentées) est jugée « vide ou à remplir » (essai 1) : faux positif sur un texte légitime ; inversement, une continuation contenant « À REMPLIR » n'est pas vue. Correction : capturer le corps jusqu'à la puce suivante (`(?=^\s*[-*]\s*\*\*|\Z)`, flags `M|S`) et appliquer les tests (marqueur, mots) sur le corps entier.

3. **À corriger** — `prereg.py:105-106` : étiquettes à variante typographique rapportées « absentes » sans distinction : `**Étiquette :**` (deux-points dans le gras), puce `*` ou `1.`, casse différente, apostrophe typographique `’` dans « Lot d'étalonnage distinct » (essais 2, 3, 5, 6, 12), forme décomposée NFD (essai 11, huit règles « absentes »). Pas de faux négatif dangereux (le refus est sûr) mais messages trompeurs. Correction : normaliser le corps (`unicodedata.normalize("NFC")`, `’`→`'`), tolérer `:` dans ou hors du gras et les puces `-`, `*`, `\d+.`, comparer sans casse ; au minimum, ajouter au message « étiquette exacte attendue : `- **…** : …` ».

4. **À corriger** — `prereg.py:112` : marqueur sensible à la casse. `à remplir plus tard svp` passe (essai 7). Correction : `MARQUEUR.lower() in valeur.lower()` (le contrôle v1 a la même limite, mais `sceller_prereg_v2` l'hérite ; à traiter ici seulement). Ajouter aussi `GABARIT` (`<<X>>`) et « TODO » est optionnel.

5. **À corriger** — `prereg.py:112-119` : seuil de trois mots trivial à contourner (`n/a n/a n/a`, `TODO TODO TODO`, `sans objet : n/a n/a n/a` passent : essais 9, 10). C'est une limite de principe d'un contrôle de forme ; elle doit être dite dans le docstring et dans le gabarit (« le contrôle vérifie la présence, jamais la qualité ; la contre-lecture R2 juge le fond »). Correction mineure possible : exiger au moins un mot de plus de trois lettres distinct, ou refuser les mots répétés.

6. **À corriger** — doublon : `prereg.py:107-110` signale le doublon mais ne valide que la première occurrence ; une seconde ligne vide ou « sans objet » est ignorée. Correction : valider toutes les occurrences (boucler sur `lignes`) ; le doublon reste signalé.

7. **Mineure** — `prereg.py:91` `SANS_OBJET` n'accepte que `sans objet :` ; `Sans objet — raison` ou `sans objet, raison` passent par la branche « mise en œuvre » (essai 8) et sont donc acceptés sans que la raison soit contrôlée comme telle ; `sans objet` seul est refusé avec le message « trop courte » (peu clair). Correction : accepter `[:—–-]` après « sans objet » et dire « sans objet sans raison » pour le cas nu.

8. **Mineure** — `prereg.py:103-104` : si la section « Règles de forme » apparaît deux fois, `sections()` ne garde que la dernière sans avertir ; un `### sous-titre` est correctement ignoré. Correction : compter les titres `## Règles de forme` et refuser plus d'un.

9. **Mineure** — `prereg.py` (`exiger_prereg_scelle`, inchangé, lignes 66-76) : avant un run, seul `problemes` (v1) est exigé ; un préenregistrement v2 scellé sans règles de forme (par `sceller_prereg`) passerait la garde de run. Hors périmètre du code livré, mais à inscrire : prévoir `exiger_prereg_scelle_v2` ou un drapeau `forme=True`, et le mentionner dans la passation.

10. **Mineure** — `prereg/gabarit-preregistrement-v2.md:44,48` : deux ajouts à la liste visée sans être signalés : « si zéro événement » (règle de trois) et « avant la vérité plantée » (extracteurs figés). Interprétations plausibles ; à confirmer ou retirer pour rester fidèle à la liste de Lazar. Le contrôle exige « non exécutable » nulle part : la déclaration d'avance de la règle 3 n'est pas vérifiée par programme, seulement demandée dans le texte du gabarit ; à dire.

11. **Mineure** — tests (`tests/test_prereg_forme_v2.py`) : R5 satisfaite à gros grain (témoin vrai complet, témoin faux avec absence et marqueur, sans objet avec/sans raison, doublon, section absente, gabarit vierge, v1), mais non couverts : règle multiligne (remarque 2), variantes typographiques (3), casse du marqueur (4), contenu bidon (5), seconde occurrence vide (6), le refus de `sceller_prereg_v2` par défaut de la v1 seule (section manquante hors forme). Ajouter un cas par remarque corrigée ; l'assertion `not (tmp_path / "p.md.sha256").exists()` est bonne (aucun scellement partiel). Le test `test_gabarit_v2_vierge_refuse_et_v1_inchange` ne vérifie pas l'empreinte de la v1 : l'invariant « v1 inchangée » repose sur git ; ajouter si voulu une assertion sur `sha256sums` ou `git diff`.

## Bilan
Bloquante : 0. À corriger : 6 (1 à 6). Mineure : 5 (7 à 11).
