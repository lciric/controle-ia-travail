# Contrôle des corrections V1 à V8 du préenregistrement court « papier dopamine » (v3, brouillon)

- **Contrôleur** : le même contre-lecteur, modèle Opus 5.5 (`claude-opus-5-5`), sous-agent. Pièce de classe A, contrôle en une passe. Aucun appel payant, ni commit ni poussée.
- **Date (UTC)** : 20 novembre 2026, 15:21 (`date -u`).
- **Relus** (empreintes recalculées, égales à leurs compagnons) :
  - v3 : `preenregistrement-court-papier-dopamine-v3-brouillon.md`, `1925d18b6ccb3fafb697abc7f29090f4649cd2b634403609be3663e0c3845a7c` ;
  - différentiel : `differentiel-v2-v3-preenregistrement-court-papier-dopamine.diff`, `d827fbf786c95f8cfe555c4214a9be96e336487774aec7afa606b3aa4c0f14e3` ;
  - v2 (`9166040a…`) et mon rapport de vérification (`d22b426a…`), tous deux intacts.
- **Périmètre** : V1 à V8, et l'absence de tout autre changement de fond dans le différentiel.

## Verdict

**Conforme, à sceller une fois les points du directeur tranchés.**

## Contrôles

- **Le différentiel** : je l'ai recalculé entre la v2 et la v3 ; il est identique au fichier fourni, en-têtes de date mis à part.
- **V1 à V8** : chaque texte neuf est porté à la lettre, à la place prévue.
  - V1 : la phrase fautive sur h est remplacée. La suite du paragraphe (calcul des demi-largeurs, vérité plantée à 0,9) est gardée, comme prévu.
  - V2 et V3 : portées dans l'étape 1.
  - V4 : portée après la définition de « Battre ».
  - V5 : portée dans l'audit de symétrie.
  - V6 : ligne insérée juste après « P5 tenue (nul pour (i)) ».
  - V7 : ligne « P5 réfutée » remplacée.
  - V8 : citation de Lin et al. remplacée.
- **Hors de V1 à V8, rien que de la tenue de pièce** :
  - le titre passe en v3, et l'avertissement de tête est mis à jour (il nomme la v2 et les points du directeur, dont VO-14) ;
  - la date de la v3 et le rôle du contre-lecteur sont ajoutés ;
  - mon rapport de vérification entre dans les documents qui font foi ;
  - dans la table de traitement de la contre-lecture 1, la ligne 15 renvoie désormais à V4 ;
  - la section « Contre-lecture » reçoit une entrée « Contre-lecture 2 » avec ses deux empreintes et la table de V1 à V8, et la liste des points du directeur y gagne VO-14.

  Aucun énoncé, critère, seuil ni valeur ne change.
- **Validateur** : `problemes()` sur la v3 renvoie une liste vide.

## Avant le scellement

Le directeur doit trancher VO-6 (seuil de fausses alertes ; ma recommandation reste l'option A, confiance 0,65), VO-11, VO-12, VO-13, VO-14 (le PDF de Lin et al., ou la réserve gardée) et VO-16. Le texte scellé ne garde qu'une option à la section « Seuil ».
