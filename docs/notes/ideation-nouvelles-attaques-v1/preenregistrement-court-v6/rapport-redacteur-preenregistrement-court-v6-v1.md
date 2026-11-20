# Rapport du rédacteur — préenregistrement court v6 de la course « nouvelles attaques » — v1

- Rédacteur neuf, modèle F. Je n'ai écrit aucune version du préenregistrement court, du devis, ni leurs contre-lectures. Écrit le 2026-11-20. Pièce de travail (classe C).
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v5/mandat-redacteur-preenregistrement-court-v6-v1.md` (`9409a47aa450979601f7ea0994a902b3666f06930216b3cc79ae188cb23a6c7b`, égale au compagnon), sur GO-2026-11-20-33.
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. **Aucun refus de permission, de classifieur ni de garde.**

## 1. Pièces lues, empreintes égales au compagnon et à l'attendu

| pièce | empreinte |
|---|---|
| préenregistrement court v5 (la cible) | `b2bb980af931fef450cdcb3aee59c0134e8fc0fbf6cce62415bc99c70dcf6993` |
| vérification des corrections de la v5 et du devis v4, lue en entier | `508ebfde94a0192976bcd32722c9178cbdff6dfc6691fb5d8ad1f40aa7fa42fb` |
| jeu de corrections C1 à C3 du contre-lecteur | `5a02055af07113cb0ee1f7ae98f2349ebf3c1df7dafd6f8220cfe0f33c4915b7` |
| outil de remplacement à texte exact `scripts/remplacer_texte_exact_v1.py`, lu | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| validateur `valider_prereg_v4_v1.py` (dossier v4), lu d'abord | `63a1c0bcf0375fd4bbd661aa390f763ec2f325f942728c85c567d4224e87fde7` |

## 2. Ce qui est écrit

Dossier D = `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-preenregistrement-court-v6/`. Chaque fichier a son compagnon `.sha256`.

- D/`preenregistrement-court-course-nouvelles-attaques-v6.md` : `7e240c8c9b059171e06b416d5cf8b14c6822978f84219ad2d9770a32f90f11c5`.
- D/`preenregistrement-court-course-nouvelles-attaques-v6.md.journal-remplacements-v1.json` (journal de l'outil).
- D/`remplacements-preenregistrement-court-v5-v6-v1.json` (le jeu passé à l'outil, écrit avec l'outil d'écriture de fichiers).
- D/`differentiel-preenregistrement-court-v5-v6-v1.diff` (`diff -u` v5 → v6).
- D/`sortie-validateur-preenregistrement-court-v6-v1.txt`.
- D/`ancres-v1.txt` (les huit textes anciens, un par ligne ; aide de travail).
- ce rapport.

## 3. Les huit remplacements

Chaque texte ancien compté par `grep -c -F -e` sur la v5 avant l'appel : 1, huit fois. Sortie de l'outil : « FAIT : 8 remplacement(s) », cible `b2bb980a…`, sortie `7e240c8c…`.

1. **C1** (tableau des pièces, ligne du devis à six espèces) : « Ancien » et « Neuf » mot pour mot de la vérification, § 5, pris au jeu du contre-lecteur.
2. **C2** (même tableau, « même réserve » retirée) : de même.
3. **C3** (contre-lecture 4 : chemin avec `contre-lecture-v1/`, empreinte `539c4854…`) : de même.
4. **C4** (contre-lecture 4, blanc de la mère) : « Traitement : (à écrire par la mère). » remplacé par le texte de la mère, mot pour mot du mandat, point 2.
5. **Tenue, titre** : « v5 » devient « v6 ».
6. **Tenue, statut** : « les corrections portées par la v5 restent à vérifier par le même contre-lecteur. » devient « les corrections portées par la v5 sont vérifiées par le même contre-lecteur (verdict « À corriger », C1 à C3, section « Contre-lecture ») ; la v6 porte C1 à C3 et le traitement écrit par la mère (C4), et reste à vérifier par le même contre-lecteur. »
7. **Tenue, statut** : « tant que la v5 ne l'est pas » devient « tant que la v6 ne l'est pas ».
8. **Tenue, phrase de version** : une ligne « Version : la v6 remplace la v5 … » ajoutée après la phrase de version de la v5, avant la ligne « Commit du code d'analyse ». Elle cite la v5, la vérification, C1 à C4, le mandat, chacun par chemin et empreinte.

## 4. Contrôles après l'outil

- `grep -c -F -e "(à écrire par la mère)"` sur la v6 : **0**.
- `grep -c -F -e "(empreinte du rapport)"` sur la v6 : **0**.
- Validateur du dépôt sur la v6, par son chemin d'origine (son entrée n'est pas figée, aucune copie n'a été nécessaire) : les huit sections exigées présentes, aucune absente, « problemes : aucun ».
- Le jeu de C1 à C3 du contre-lecteur, joué seul, rend `367a85b7…` (vérification, § 5) ; la v6 porte en plus C4 et la tenue, son empreinte est donc autre : c'est attendu.

## 5. Réserves et écarts

1. **La ligne de date n'est pas changée.** Le mandat borne la tenue au titre, au statut et à la phrase de version ; la v4 et la v5 ajoutaient un relevé de `date -u` à la ligne de date. Je ne l'ai pas fait, et la phrase de version de la v6 le dit. Si la mère veut ce relevé, c'est un remplacement de plus.
2. **Une phrase ajoutée à la phrase de version, au-delà du strict gabarit de la v5** : « Par C1, « devis v3 » dans ce texte, hors la citation de GO-2026-11-20-34, renvoie au devis v4 (…) ; la phrase de version de la v5 qui dit ces renvois non récrits vaut pour la v5 seule. » Sans elle, la phrase de version de la v5, gardée telle quelle, dirait de la v6 une chose devenue fausse (C1 récrit le chemin et l'empreinte de la ligne du tableau). Elle ne tranche rien.
3. **Le statut dit le verdict de la vérification** (« À corriger », C1 à C3). C'est un fait de la pièce `508ebfde…`, non une décision.
4. Le texte de C4 a été écrit par la mère ; je l'ai porté mot pour mot, sans le juger.
5. Le validateur ne voit pas les blancs (vérification, § 4.1) : son « aucun » ne vaut pas « complet ». Les deux `grep -c` à 0 portent ce contrôle.
6. Aucun chiffre n'est recalculé : aucun total, seuil, arrêt ni décision n'est touché.
7. Reste, hors de mon mandat : la vérification de la v6 par le même contre-lecteur (par `cmp` ou rejeu du jeu), le scellement par la mère, le devis v4 à Lazar.

— rédacteur neuf, modèle F
