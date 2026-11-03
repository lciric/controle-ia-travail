# Protocole du rapport des idées sur la question 1 de Heimersheim — v1 (gelé avant toute sortie)

Session conv-audit (Claude), 3 novembre 2026, 07:35 UTC (`date -u`). Mots de Lazar (heure de Paris) : 08:11 « à la fin fais un rapport de toutes les idées du collisionneur (pas de consensus, on garde tout ce qui est ouvert et non réfuté) et des deux modèles seuls, et classe-les par ordre de priorité à traiter dans la réponse pour se démarquer des autres et rendre quelque chose d'original et absolument mémorable et impressionnant » ; 08:12 demande de version approfondie (rendue) ; 08:24 « je veux moisson et classement de ce qui sort de la course d'idéation et des deux modèles », puis « go » sur la version reformulée. « Collisionneur » est lu comme la course d'idéation de l'organisme lancée sur ce mot (le collisionneur v9 n'a pas de bisociateur ; vérifié : 0 occurrence dans `collisionneur_v9.py`).

Écrit et scellé **avant qu'aucune sortie n'existe** : aucune règle ci-dessous ne se change après lecture (R12 : une v2 éventuelle est un fichier neuf, avec sa raison).

## 1. Entrées (scellées par session-depot avant toute lecture)
- **Course** : toutes les fiches de toutes les passes de tous les proposeurs, y compris celles que l'aiguilleur a classées « à corriger » ; les fusions du bisociateur (tous bras). **Exclus** : les fiches du coffre (classées « trop concrètes » : comptées, jamais ouvertes, ni par les lecteurs ni par moi ; Lazar peut les lire lui-même) ; les sorties des juges de la course (au plafond au dernier tour : rapportées à part, jamais utilisées pour garder ou écarter une idée).
- **Appels seuls** : la partie 1 (idées) et la partie 2 (réponse) d'Astra et d'Argon, consigne `consigne-appel-seul-v1.md` (`8d6896a1…`).
- Version 1 du rapport dès que la course et Astra sont versées ; version 2 quand Argon l'est (après A1-v3).

## 2. Étape A — normalisation et dédoublonnage (lecteur neuf A)
- Chaque idée devient une **fiche normalisée** : énoncé (une phrase falsifiable), mécanisme, mesure qui la tuerait, prédiction et signe, échec le plus probable, rattachement à la pièce (neuve / prolonge le point n / déjà dans la pièce), coût. Ce qui manque reste vide et se dit, jamais complété par le lecteur.
- **Dédoublonnage par structure** : deux idées sont une seule si elles ont la même hypothèse et la même mesure qui tue, quels que soient les mots ; la fiche fusionnée garde la liste de toutes ses provenances.
- **Réfutée** seulement si une source citée (point de la pièce, ou source primaire ouverte et citée avec page ou section) contredit son énoncé central, ou si elle se contredit elle-même. **Jamais par accord ou désaccord des modèles, jamais par les notes des juges.** Tout le reste est **gardé**.
- Hors sujet (ne porte ni sur pourquoi la direction (c) échouerait, ni sur comment l'éprouver) : gardée en annexe, non classée.
- Sorties : `fiches-normalisees.json` (identifiants opaques, **aucune provenance**), `cle-provenances.json` (identifiant → provenances), `refutees.md` (chaque réfutation avec sa preuve). La clé ne va qu'à moi.

## 3. Étape B — deux témoins publiés déguisés (préparateur neuf B, qui ne classe rien)
- Deux idées **déjà publiées** (2024 à 2026), absentes de la pièce, directement liées à l'échec possible du pilotage contre la conscience d'évaluation ; existence, identifiant, date et affirmation exacte vérifiés en source primaire.
- Écrites au format des fiches normalisées, sans citer leur source ; clé scellée à part (identifiant, phrase du résumé, requêtes qui doivent les trouver), qui ne va qu'à moi.
- Mêlées aux fiches par une permutation tirée de `numpy.random.SeedSequence` (graine : entier des 16 premiers hexadécimaux du sha256 de `fiches-normalisees.json`), identifiants opaques réattribués ; clé de la permutation scellée.

## 4. Étape C — moisson de nouveauté (un ou deux moissonneurs neufs, aveugles à la provenance et aux témoins)
- Par fiche : au moins deux requêtes de mots différents sur arXiv et OpenAlex ; trois au moins, plus LessWrong et Alignment Forum (où une partie de ce champ publie, par exemple la réplication sur GLM-5), pour toute fiche qui sortirait « ouverte » (zone vierge séduisante vérifiée plus durement, R8).
- Classe : **déjà fait** (identifiant, phrase du résumé qui le montre) ; **voisin** (identifiant, ce qui diffère) ; **ouverte** (les requêtes exactes qui n'ont rien trouvé). Non opposable : métadonnées et résumés seulement ; une zone vierge est une question, jamais une affirmation.
- Une fiche contredite par un résumé trouvé passe en réfutée, avec la preuve.
- Plus de 30 fiches : deux moissonneurs, moitié chacun, par la même permutation.

## 5. Étape D — classement (classeur neuf D, aveugle à la provenance et aux témoins)
- **Porte** : seules les fiches gardées, dans le sujet, sont classées.
- **Trois critères gelés**, notés 0 à 3 avec ancres :
  - *Originalité vérifiée* — 0 : déjà fait ; 1 : voisin proche ; 2 : voisin lointain ; 3 : ouverte après moisson.
  - *Testable en jours sur Llama-3.1-8B-Instruct* — 0 : pas de mesure qui tue ; 1 : mesure floue ou d'un mois ; 2 : protocole clair d'une à deux semaines ; 3 : protocole clair de quelques jours sur une carte, avec seuil.
  - *Prolonge un outil du mentor* (plateaux d'activation et directions sensibles, exposant p et correction d'erreur par trait, décomposition de paramètres, activations synthétiques) — 0 : aucun lien ; 1 : cite l'outil ; 2 : l'utilise ; 3 : en fait une mesure neuve que ses papiers n'ont pas faite.
- Les douze premières par somme (égalités départagées par l'originalité) sont ordonnées par **comparaisons par paires dans les deux ordres** (66 paires × 2) sur la question gelée : « laquelle rendrait une réponse à cette question plus originale et plus mémorable pour ce mentor, sur ces trois critères ? » ; forces de Bradley-Terry calculées par un script (numpy, sans modèle) ; **cohérence** = part des paires dont les deux ordres concordent ; sous 0,8, réserve écrite.
- Risque devant ce mentor (affirmation qu'il pourrait contredire de ses propres papiers) : drapeau, pas une note ; chaque drapeau dit pourquoi.

## 6. Contrôle par les témoins (moi, après le classement)
- **Tenu** si chaque témoin est classé « déjà fait » (ou « voisin » avec le bon identifiant) à la moisson **et** n'est pas noté 3 en originalité.
- **Non tenu** : l'axe d'originalité est déclaré invalide dans le rapport ; une moisson neuve, plus stricte, est refaite par un moissonneur neuf sur toutes les fiches notées 3, et le rapport v1 porte les deux résultats.

## 7. Rapport pour Lazar (moi, après levée des clés)
- **Classées**, dans l'ordre : énoncé ; mesure qui la tue ; échec le plus probable ; moisson (identifiant ou requêtes) ; où elle entre dans la réponse (ses quatre parties : lisible n'est pas causal ; registre ; soustraire n'est pas retirer ; ce que je voudrais voir) ; ce qu'il a déjà pour l'appuyer (D36, R6, rang 3, validité de construit), avec chemin ; ce qu'il faudrait vérifier avant de l'écrire ; provenances.
- **À part** : les réfutées avec leur preuve ; les hors sujet ; le résultat des témoins ; la cohérence du classement ; les notes des juges de la course, rapportées avec leur réserve.
- **Règle du mentor, dite une fois en tête** : la réponse doit être écrite par lui (« 100% human-written ») et ne pas suivre de près un texte écrit par une machine ; le rapport donne des idées et leurs preuves, aucune phrase anglaise à recopier.
- Aucun chiffre sans chemin et empreinte (R6) ; aucun chiffre de la littérature sans source primaire (R7).
