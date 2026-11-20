# Rapport du rédacteur — préenregistrement court v5 et devis v4 de la course « nouvelles attaques » — v1

- Rédacteur neuf, modèle F. Je n'ai écrit aucune version du préenregistrement court, du devis, ni leurs contre-lectures. Pièce de travail (classe C), sur GO-2026-11-20-33. Écrit le 2026-11-20 ; relevé de `date -u` : 10:30:08Z, après la lecture des pièces, avant l'écriture.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/mandat-redacteur-preenregistrement-court-v5-devis-v4-v1.md` (`2a813c54c06ff5a53198623ee5429da6c4f10426fda3ee641f070f0bc1ba8cf4`, égal à son compagnon).
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement du relais, du véhicule ni de la sonde, aucune écriture dans le dépôt, aucun commit. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

Les deux textes neufs sont écrits par l'outil contre-lu : le préenregistrement court v5 (9 remplacements) et le devis v4 (8 remplacements). Ils portent les neuf corrections de lettre de la contre-lecture (K1 à K9), le texte de la contre-lecture 4 et la tenue ; rien d'autre. Aucun total, seuil, arrêt ni décision ne change. Le validateur du dépôt ne rend aucun problème sur la v5. Restent à faire : la vérification des corrections par le même contre-lecteur, puis l'empreinte et le traitement de la contre-lecture 4, à écrire par la mère.

## 1. Pièces vérifiées (empreinte égale au compagnon, puis recalculée)

Dossier V = `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/`.

| pièce | empreinte |
|---|---|
| V/`preenregistrement-court-course-nouvelles-attaques-v4.md` | `2dabdadf9ac126ee8d931dfde3e3507a3183b50b8f584d0f817e7ebf8adf2b10` |
| V/`devis-course-nouvelles-attaques-v3.md` | `bf7b4ba3ede3ba73c8ee4e1a3548b6b0d52975df717b98ca4af44a6c503c142a` |
| V/`contre-lecture-v1/contre-lecture-preenregistrement-court-v4-devis-v3-v1.md` | `539c4854ad36e5d9b615c43bb2f7b7359c27661abc6f2a0abc6195812c1e150f` |
| V/`contre-lecture-v1/corrections-preenregistrement-court-v4-v1.json` | `14b429fe624abca8e4ee468a677b79dab4cd9200822551574aa93323de58b3bb` |
| V/`contre-lecture-v1/corrections-devis-v3-v1.json` | `11977cde4b4889011f15569c8291dccf9d5948a8440df3f2bf8e95c691e53c92` |
| `scripts/remplacer_texte_exact_v1.py` (recalculée, pas de compagnon vérifié) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

## 2. Ce qui est écrit

Dossier D = `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-preenregistrement-court-v5/`. Chaque fichier a son compagnon `.sha256` à côté.

| fichier | empreinte |
|---|---|
| D/`preenregistrement-court-course-nouvelles-attaques-v5.md` | `b2bb980af931fef450cdcb3aee59c0134e8fc0fbf6cce62415bc99c70dcf6993` |
| D/`devis-course-nouvelles-attaques-v4.md` | `620de3692d3454f08d32832ca471551bb9a8439f80122b716b13474d9a6d363e` |
| D/`remplacements-preenregistrement-court-v4-v5-v1.json` ; D/`remplacements-devis-v3-v4-v1.json` | au compagnon |
| les deux journaux de l'outil (`….journal-remplacements-v1.json`) | au compagnon |
| D/`differentiel-preenregistrement-court-v4-v5-v1.diff` ; D/`differentiel-devis-v3-v4-v1.diff` | au compagnon |
| D/`sortie-validateur-preenregistrement-court-v5-v1.txt` | au compagnon |

## 3. Les remplacements

Chaque ancre a été comptée une fois dans sa cible par `grep -c -F -e` avant l'appel (17 comptes, tous égaux à 1). Sorties de l'outil : « FAIT : 9 remplacement(s) » pour le préenregistrement, « FAIT : 8 remplacement(s) » pour le devis ; aucun avertissement.

**Préenregistrement v4 → v5 (9).**
- Quatre de tenue : le titre (« v4 » devient « v5 ») ; la ligne de date (un relevé « Version 5 » ajouté) ; le statut ; une phrase de version neuve, ajoutée après celle de la v4.
- K1 à K4 : « Ancien » et « Neuf » mot pour mot de la contre-lecture, § 8, comparés un par un au jeu JSON du contre-lecteur (égaux).
- La contre-lecture 4 : le texte du § 8 mot pour mot, à la place de la ligne « À REMPLIR ». Les mentions « (empreinte du rapport) » et « (à écrire par la mère) » y sont laissées telles quelles.

**Devis v3 → v4 (8).**
- Trois de tenue : le titre (« v3 » devient « v4 ») ; le statut ; une phrase de version neuve, qui remplace aussi « La v3 n'est pas contre-lue. » par « La v3 est contre-lue (ligne suivante). »
- K5 à K9 : mot pour mot, comparés de même.

Ce qui reste à Lazar n'est pas tranché : le plafond (570 ou 450 USD) reste écrit en deux options au § 9 du devis ; le plafond de la sonde de l'espèce 6 reste à 0,01 USD avec la réserve de K9 (« une ligne neuve se demande »).

## 4. Le validateur

`valider_prereg_v4_v1.py`, lu d'abord (il n'écrit rien, il n'appelle que `controle_ia.prereg.problemes` et `sections`), lancé par son chemin depuis la racine du dépôt, `PYTHONPATH=src`, sur la v5. Sortie :

```
sections exigees presentes : ['Hypothèse', 'Prédiction chiffrée et signe attendu', 'Métrique', 'Seuil', "Plan d'analyse", 'Critères de lecture gelés', "Liste d'arrêt", 'Contre-lecture']
sections exigees absentes : []
problemes : aucun
```

Le problème « section vide ou à remplir : Contre-lecture » de la v4 a disparu, parce que le marqueur « À REMPLIR » est remplacé.

## 5. Réserves

1. **Le validateur dit « aucun » alors que la contre-lecture 4 n'est pas finie.** L'empreinte du rapport et le traitement sont encore des mentions entre parenthèses, que le validateur ne reconnaît pas. La v5 n'est pas scellable tant que la mère ne les a pas écrites (par une version neuve ou par la voie qu'elle choisit, R12).
2. **Le chemin du rapport dans le texte de la contre-lecture 4** est celui que le contre-lecteur a écrit (`…/preenregistrement-court-v4/contre-lecture-preenregistrement-court-v4-devis-v3-v1.md`). La pièce que j'ai lue est au sous-dossier `contre-lecture-v1/`. Je n'ai pas corrigé : le texte est porté mot pour mot. À la mère de verser la pièce à ce chemin ou de corriger le chemin.
3. **Renvois croisés non récrits.** La v5 dit encore « devis v3 » (table des documents avec son chemin et son empreinte, section « Seuil », point 11 de « Ce qui reste à écrire »), et le devis v4 dit encore « préenregistrement court v4 » (§ 4, § 9, et le « Neuf » de K9 lui-même). Le mandat borne l'écriture aux corrections et à la tenue ; je l'ai seulement dit dans les deux phrases de version et dans le statut de la v5 (« le devis neuf […] le devis v4, qui remplace le devis v3 »). Si la mère veut des renvois récrits, c'est un jeu de remplacements de plus, à faire contre-lire.
4. **Le statut de la v5 parle du « devis neuf »** là où la v4 disait « devis v3 » : c'est le mot de GO-2026-11-20-33 tel que la contre-lecture le cite, et le seul endroit où j'ai touché à un renvoi. À vérifier par le contre-lecteur.
5. **La recommandation de 0,05 USD pour la sonde de l'espèce 6** (contre-lecture, § 5) n'est dans aucun des deux textes : K9 ne la porte pas. Elle se porte à Lazar avec le devis, par la mère.
6. **Le calcul du devis n'est pas rejoué** : aucune correction ne touche un chiffre calculé ; les chiffres neufs de K5 à K9 (124,10 ; 12,04 ; 36,50 ; 77,37 ; 10 562 ; 0,473 ; 0,0211) sont ceux du contre-lecteur, que je n'ai pas refaits.
7. Ce que la contre-lecture renvoie à la mère reste entier (§ 6 de la contre-lecture, points 7, 10, 12 et 13) : la manière de relire le solde de Rigaud, l'ordre de course v3 qui dit encore cinq espèces, R-4179.

## 6. Écarts

1. Sept remplacements de tenue en tout (quatre et trois), là où le mandat nomme « titre, statut, phrase de version » : la ligne de date de la v5 reçoit en plus un relevé d'heure, et la phrase « La v3 n'est pas contre-lue. » du devis, devenue fausse, est corrigée dans le même remplacement que la phrase de version.
2. La phrase de version de la v5 et celle du devis v4 citent l'empreinte du rapport de contre-lecture (`539c4854…`), vérifiée contre son compagnon. La section « Contre-lecture », elle, laisse l'empreinte à la mère, comme la pièce le dit.
3. Les différentiels sont écrits par `diff -u`, dont le code de sortie 1 (fichiers différents) est l'issue normale.
4. Aucun autre écart.

— rédacteur neuf, modèle F
