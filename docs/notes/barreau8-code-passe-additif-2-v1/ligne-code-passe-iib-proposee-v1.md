# Ligne `CODE-PASSE-IIB` proposée — v1

Proposée par le développeur du côté des moniteurs le 2026-11-24 ; **la session mère l'inscrit** au registre propre `registres/sondes-iib-v1.md`, à l'heure de l'inscription (`date -u`), après la fusion de cette branche sur `main`.

```
| CODE-PASSE-IIB | <heure de l'inscription, AAAA-MM-JJTHH:MM:SSZ> | registres/bordereau-code-passe-barreau8-v6.json | 74736c499d9bd7568d0ebe93b0eccd73746fe0ab1697fa26f2371ef816d6e8db |
```

- **Bordereau du code** : `registres/bordereau-code-passe-barreau8-v6.json`, empreinte `74736c499d9bd7568d0ebe93b0eccd73746fe0ab1697fa26f2371ef816d6e8db`, dix clés, écrit par `python -m controle_ia.barreau8_moniteurs.passe_recalcul_v6 bordereau-code` (même forme de lancement que la passe).
- **Commit porté par le bordereau** : `1f16e86e2ad1e3318be89566a8671a71f799bd4f` (branche `barreau8/code-passe-additif-2-v1`).
- **Module de la passe** : `controle_ia.barreau8_moniteurs.passe_recalcul_v6`, fichier `src/controle_ia/barreau8_moniteurs/passe_recalcul_v6.py`, empreinte `f3228b4b25a5140b3b8fa8c7ac994a727d61f9d986b0539f8ea5956eb5fba30a` (29 modules `controle_ia` au bordereau).
- **Pièces citées** : texte scellé `8e432cdc…` ; additif 1 `fc5b0610…` ; additif 2 `8e930aba…` ; table neuve des constantes `docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json`, `d576c16b61d7038d498eb1f60c523448922269142cf6f599d61a10cadb0dddc4` (« report ») ; rapport de conformité (vérification des corrections, Sonnet 5.5, « conforme ») `docs/notes/barreau8-code-passe-additif-2-v1/verification-corrections-passe-v6-comparaison-v3-sonnet-v1.md`, `8b81389e01b2e1c01bc47ddbb8f18cfd85343056900dd982083b6a6e8a31bc3b` ; notice `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v8.md`, `16798bd6ad770fa76072c19ef578dfdb5ea723056635d8b0bc4ddf99d9544433` ; devis `9a4a794c…` ; accord `GO-2026-11-24-13`.
- **Pièce de comparaison réécrite (M-4, cas « non attesté »)** : `docs/notes/barreau8-cote-moniteurs-sorties-v1/comparaison-interface-v6-v7-v2.json`, `0554c544b112cddffc3b7615e0bed4b249032b632d1849ad2ac144f797ec4b34` (8 blocs identiques, 14 changés, mêmes champs changés que la version 1 ; contrôle `controler` : « conforme »).
- **Essai à blanc de la garde P0** (2026-11-24T11:30:38Z) : sur une copie du registre propre portant cette ligne, la garde P0 de la passe est tenue sur le dépôt réel (trois textes scellés et intacts, bordereau, table « report », modules, rapport, notice, devis, une seule ligne de l'accord `GO-2026-11-24-13` citant le devis), et la spécification du code égale la table.
- **À faire avant la passe** : fusionner la branche sur `main` (le rapport de conformité, la notice, la table et le bordereau doivent être aux chemins cités) ; inscrire la ligne ; contrôle de la pièce d'attestation de l'ordre par la session mère (nœud NO-2, M-3) ; puis `verifier-entrees` et `essai-a-blanc` sur la machine (notice v8).
