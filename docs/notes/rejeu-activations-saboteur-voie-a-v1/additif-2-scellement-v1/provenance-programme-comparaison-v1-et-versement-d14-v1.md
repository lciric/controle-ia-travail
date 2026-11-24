# Versement des quatre pièces de la condition D-14 et provenance du programme de comparaison de version 1 — note pour la session mère — v1

Note de travail (classe C) de la session fille `session_01Qi7Gr3DCGJkFuLgghCz7Mh`, écrite le 2026-11-24 vers 10:25Z, sur la demande de la session mère (message de 10:16Z). Rien n'est scellé.

## 1. Versement (fait sur la branche `prep/additif-2-scellement-v1`, partie de la branche principale à `c4550d8d`)

Copie à l'identique, avec les compagnons, le 2026-11-24 à 10:18:40Z (`date -u`) ; aucune cible n'existait ; les sources restent en place.

| source (dossier `docs/notes/rejeu-activations-saboteur-voie-a-v1/prealables-cote-expose-v7-brouillon/`) | cible | empreinte après versement |
|---|---|---|
| `interface-passe-cote-moniteurs-v7.md` | `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v7.md` | `b16779bc3ee843c698debf825680b9847739f4a150a9aa3c9460b76048c277b6` |
| `interface-passe-cote-moniteurs-v7-champs.json` | `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v7-champs.json` | `dc4d0a1decddbc6bf893a28b8e748620f3881b4fe29d6da964b3521e64588c30` |
| `comparaison-interface-v6-v7-v1.json` | `docs/notes/barreau8-cote-moniteurs-sorties-v1/comparaison-interface-v6-v7-v1.json` | `e744d82406e5887a963b0e251b56152e3bbf9805ac1b3117ea6631b74b72c7c2` |
| `constantes-reportees-additif-1-v1.json` | `docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-1-v1.json` | `f6e9c8d5830dc503e129bc7b0c631a65ec8b8b61b7d4e5ac6c330910f9882171` |

Sortie du contrôle `sha256sum -c`, dans chaque dossier cible :

```
interface-passe-cote-moniteurs-v7.md: OK
interface-passe-cote-moniteurs-v7-champs.json: OK
comparaison-interface-v6-v7-v1.json: OK
constantes-reportees-additif-1-v1.json: OK
```

## 2. Provenance du programme de comparaison de version 1 (`comparer_v6_v7_v1.py`, `51ce5970280065161078053688175bc4891fbf38b82283e2f6dc8aeeb60fe0cc`) : « non attesté »

L'additif 1 scellé pose quatre exigences : le programme est écrit par le développeur du côté des moniteurs ; à partir de l'additif 1 seul ; contre-lu par un autre modèle ; ses corrections vérifiées par le même contre-lecteur.

Ce que le dépôt dit, cherché le 2026-11-24 vers 10:20Z :

- **Auteur.** `registres/decisions.md`, ligne R-5239 (2026-11-24T05:39:25Z) : un sous-agent neuf du côté exposé (`97f22687`, exclu de tout rôle du côté des moniteurs) est habilité « pour rédiger D-14 (interface v7, fiche JSON, comparaison v6-v7, constantes reportées), D-13 et, si requis, le brouillon d'additif 2 ». Le programme et ses deux pièces entrent au dépôt par un seul commit, `46e9142c` (2026-11-24T06:28:23Z, passation intégrale de la mère d'alors), dans le dossier des préalables du côté exposé. Aucune ligne de registre ne nomme un développeur du côté des moniteurs pour ce programme. **Exigence 1 : non tenue, d'après R-5239.**
- **Source.** L'en-tête du programme cite l'additif 1 à son empreinte et dit ne lire que les deux notes, la fiche et leurs compagnons. Son auteur, lui, a lu davantage (les métadonnées de la course). **Exigence 2 : non établie.**
- **Contre-lecture.** Recherche du nom du programme et de son empreinte dans `registres/` et `docs/` : hors du dossier de l'additif 2, seul le brouillon 1 de l'additif 2 le cite. Aucun rapport de contre-lecture du programme, aucune vérification de corrections. La seule pièce jointe est la sortie de son propre auto-essai (douze essais réussis), qui n'est pas une contre-lecture. **Exigences 3 et 4 : non tenues.**
- Branches : aucune branche distante ne porte un nom de contre-lecture de ce programme ; les branches de la course n'ont pas été ouvertes.

**Conclusion à la lettre du brouillon 6 : « non attesté ».** La suite est celle de la règle M-4 : après le scellement, la version nouvelle du programme, écrite par le développeur du côté des moniteurs et contre-lue par un autre modèle, écrit la table neuve des constantes **et réécrit la pièce de comparaison** sous le nom `comparaison-interface-v6-v7-v2.json` ; cette pièce remplace `e744d824…` partout où l'additif 1 écrit « la pièce de comparaison » ; elle doit rendre les mêmes états de blocs (huit identiques, quatorze changés, aucun ajouté, aucun absent) et les mêmes champs changés ; sinon : nœud (ligne 21).

Ce que cela ne change pas : la pièce `e744d824…` reste versée comme pièce d'origine ; la table `f6e9c8d5…` reste la pièce qui constate le nœud ; le vérificateur des corrections a recalculé par son propre programme les quatorze blocs changés sur les deux notes, et la liste fermée de M-4 contre la fiche.

## 3. Ce que cette session n'a pas pu vérifier

Les cinq faits du champ AD2-3 que seule la session mère atteste (bornes (b2) et (b3) ; aucun score, texte d'épisode ni état lu ; source « qui a lu quoi » ; ce que Lazar avait vu ; lectures jouées ou non). Constats mécaniques de cette session, qui ne valent pas attestation : sur la branche principale à `c4550d8d`, le fichier de l'extrait des seuls états est absent de son chemin, et le registre propre ne porte que ses deux lignes de scellement (aucune ligne de code de la passe).
