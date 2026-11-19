# Relecture de l'erratum — préenregistrement de l'épreuve sur l'héritage, palier 0b, version 3 — v1

- Auteur : le même contre-lecteur, modèle O. Pièce de travail (classe C). Relecture limitée à l'erratum.
- Date : 2026-11-19, de 22:02Z à 22:08Z environ (`date -u`). Travail sur processeur seul, sans appel de modèle ni dépense. Seul accès réseau : `git fetch` de la branche et de `main`. Rien n'a été écrit dans le dépôt. **Aucun refus d'outil.**

## Verdict

**Scellable tel quel.** Les quatre corrections de ma vérification (`9d18eab3…`, § 6) sont appliquées à la lettre. Le différentiel ne touche rien d'autre que la tenue déclarée du texte. Les trois écarts du rédacteur sont acceptés.

## Empreintes et différentiel

- **Empreintes, toutes égales aux attendues :**
  - version 3 : `a4535a67…` ;
  - différentiel v2 → v3 : `42253287…` ;
  - rapport du rédacteur v3 : `d61d0107…` ;
  - outil de remplacement : `438a2a0c…` ;
  - version 2 : `0a80a1ad…` ;
  - mandat v3 : `084207ec…`.
- **Compagnons `.sha256`** : tous égaux. Le commit `3c3cd4af` est un ancêtre de la branche.
- **Ligne `GO-2026-11-19-81`** : présente sur `main`. Au commit `d4449d32` cité, `go.md` a l'empreinte citée (`78efe878…`). Elle accorde bien, pour le palier 0b v2, A (a), le seuil, et B (a), l'engagement seul aux paliers payants.
- **Différentiel** : celui que j'ai refait de la v2 à la v3 est identique à l'octet au différentiel versé. J'ai comparé mot à mot chaque bloc changé : 15 lignes changées et 2 blocs ajoutés.
- **Validateur du gabarit** : même remarque qu'en v2, attendue (la section « Contre-lecture » sans ses deux empreintes).
- **Aucune chaîne interdite, aucun identifiant de modèle.**

## Les quatre corrections

| n° | appliquée à la lettre | où |
|---|---|---|
| 1 — engagement seul aux paliers payants | oui ; « ligne `GO-…` à inscrire » est remplacée par `GO-2026-11-19-81`, ce qui est juste puisque la ligne est inscrite | B4, point (iv), dans mes mots exacts ; réserve 16 ; valeurs gelées, ligne « ce que l'expérimentateur reçoit » |
| 2 — seuil « beaucoup plus de sources » | oui ; chiffres de S9 inchangés | réserve 14 ; valeurs gelées |
| 3 — paires de lois distinctes | oui, mot pour mot | B7, ligne du lecteur ; « Le repli du point 7 » |
| 4 — écart-type entre jumelles des proposeurs sans réglage | oui, la phrase est reprise à l'octet | B7, « Réglage par programme » |
| forme — « sur 72 cases » | oui | C1, colonne de raison |

## Ce qui a changé d'autre

Hors des quatre corrections, seules deux zones ont changé, toutes deux de tenue du texte :

- **l'en-tête** : titre « v3 (erratum) », phrase de version, heures, mandat v3 et ligne `GO-2026-11-19-81`, vérification citée ;
- **la section « Contre-lecture »** : vérification inscrite, relecture de l'erratum à faire, fichiers à donner.

L'annexe E reçoit une section neuve, « Erratum de la version 3 ». Rien d'autre ne bouge : ni les hypothèses, ni les pronostics, ni les métriques, ni les seuils, ni les critères, ni les gardes, ni la liste d'arrêt, ni les annexes A à D.

## Les trois écarts du rédacteur

1. **Place de la phrase de la correction 4** : acceptée. Ma consigne, prise à la lettre, coupait une phrase en deux. La phrase est placée après « … celle du contraste de la tenue pour τ. » et avant « Une cible est atteignable… ». C'est la bonne place, dans le paragraphe de l'étalonnage.
2. **Phrase de plus sur les usages de l'écart-type** (M9, M8, M14) : acceptée. Elle reprend les trois usages que ma vérification nommait, sans rien ajouter au dessin.
3. **Titre de l'annexe E laissé tel quel** : accepté. La section neuve a son propre titre explicite, et réécrire le titre n'apporterait rien.

## Point de forme, sans effet, non exigé

Réserve 14 : « une proposition du rédacteur, … écrite avant tout tirage et motivé » se lirait mieux avec « motivée ». C'est l'accord laissé de l'ancien « choix ». À corriger seulement si une version suivante vient pour une autre raison.
