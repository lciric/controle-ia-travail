# Rapport — quatre fichiers candidats du manifeste du rejeu du juge — v1

- **Contre-lecteur, modèle O.** Le mandat est `criteres-v7/mandat-contre-lecteur-candidats-manifeste-rejeu-v1.md` (`0d4374f8…`, égal à son compagnon). Processeur seul, aucune dépense, aucun appel de modèle. Rien n'est écrit dans le dépôt, rien n'est scellé.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/candidats-manifeste-rejeu-v1/`. Chaque fichier a son compagnon.

## Fichiers rendus

| fichier | sha256 |
|---|---|
| `manifeste-rejeu-v1.json` | `a81d30d35c3dad56405e536b901218982b16e2b5f6f82b77b2d84581974d49dd` |
| `configuration-a-masque-v1.json` | `8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4` |
| `configuration-b-lecteur-v1.json` | `b44371d235292623e2c51fdd31a68bbabae5402774d5e99860b5a6b90ebdaa6a` |
| `sortie-valider-manifeste-v1.txt` | `5c47b93fe3ef8444d163b04f922c078a647f8897ef59d88c4ac26ad79c548ef5` |
| `brouillon-piece-scellement-manifeste-rejeu-v1.md` | `9499d832a042b46fac148c6cf13f4be5d2a5bd5122d71699ca816f71f571cd63` |
| `programmes/ecrire_candidats_v1.py` | `6e648318d8f2e0d224d66314d77020a75bbf5a47788531362fd4af1ff0acd2d9` |

## Programme et commandes

- **`ecrire_candidats_v1.py`**, écrit avec l'outil d'écriture de fichiers.
  - Il vérifie d'abord cinq empreintes : l'assemblage v2 `2f5640da…`, le masque v1 `07ed8725…`, le lecteur v2 `de99117b…`, les critères v7 `6af793a2…` et l'extraction X6 `f5c7cc1c…`.
  - Il charge les trois programmes par leur chemin, sans rien écrire dans le dépôt (`-B`).
  - De l'extraction, il ne lit que `extraction.identifiants_par_classe.a_corriger`.
  - Il construit les trois JSON, puis appelle `verifier_numpy`, `valider_manifeste` (après avoir contrôlé que les clés égalent `CLES_MANIFESTE`) et les deux `valider_configuration`, ceux du masque et du lecteur.
  - Il n'écrit qu'en mode exclusif, et pose le compagnon de chaque fichier.
- **Lancement** : `python3 -B …/programmes/ecrire_candidats_v1.py DOSSIER_JUGE DOSSIER_SOURCES DOSSIER`, sortie et erreurs redirigées vers `sortie-valider-manifeste-v1.txt`.
- **Sur `main`**, après `fetch`, par `git show` redirigé vers `sources/` : les critères v7 (`6af793a2…`), la note v7 (`bbd71b7c…`), la garde (`635e9160…`), l'extraction X6 (`f5c7cc1c…`), `go.md` et `decisions.md` (lignes GO-2026-11-20-10, R-4097, R-4102 et R-4128). Toutes les empreintes sont égales à celles du mandat.

## Sortie de `valider_manifeste`, entière

```
empreintes des entrées : conformes (5)
valider_manifeste : passé, aucun refus ; clés : 16 ; égales à CLES_MANIFESTE
masque.valider_configuration : passé ; lecteur.valider_configuration : passé ; champs de B inclus dans A
manifeste-rejeu-v1.json a81d30d35c3dad56405e536b901218982b16e2b5f6f82b77b2d84581974d49dd
configuration-a-masque-v1.json 8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4
configuration-b-lecteur-v1.json b44371d235292623e2c51fdd31a68bbabae5402774d5e99860b5a6b90ebdaa6a
identifiants X6 (a_corriger) : f640bf1e40418 ; f9a7c8311d714
```

## Écarts

1. **Les noms des champs de `contenu`** sont pris dans la consigne du proposeur v2 : `course-v2/consigne-proposeur-auto-conception-v2.md`, `a7c34a7a…`, l. 43-44 et 50-61, dix champs. Ce chemin est donné par la configuration de la course v9, mais il n'est pas dans la liste « ce qui fait foi » du mandat. Le rapport v7, § 5, renvoie bien à « la consigne des proposeurs ».
   - Je n'ai pas vu les clés réelles de `contenu` dans le code de l'orchestrateur.
   - Si elles diffèrent, le masque refuse sans rien écrire (`extraire_contenus`). Il n'y a pas de repli silencieux, mais la règle d'arrêt joue alors.
2. **`formules` = `["non vérifié"]` seulement.** La consigne impose aussi « prédit » devant une valeur attendue. Je ne l'ai pas mis : le retirer effacerait si une valeur est prédite ou connue, ce qui est du contenu et non une formule de style. C'est un choix de ma main, que la mère confirme ou change.
3. **`intertitres` = `[]`** : la consigne du proposeur n'en impose aucun.
4. **Noms des familles** : `famille-opus-fable`, `famille-argon`, `famille-astra` et `famille-carbon`. Ils sont neutres et libres (C3) ; aucun nom de fournisseur n'est employé.
5. **« La réserve de ton § 4 »** : je ne sais pas laquelle la mère vise. Je le dis en tête du brouillon et je nomme les deux réserves possibles, qui portent toutes deux sur `lignee_reconnue` et sont toutes deux levées par la garde v2.
6. **Les identifiants X6** sont recopiés de la sortie du programme dans le brouillon, qui est un fichier `.md` et non un JSON. J'ai vérifié l'égalité par recherche exacte sur les deux fichiers.

**Aucun refus** de permission, de classifieur ni de garde. Aucune carte, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`, aucune commande de liste, une commande simple par appel, aucun code en ligne.

*contre-lecteur, modèle O*
