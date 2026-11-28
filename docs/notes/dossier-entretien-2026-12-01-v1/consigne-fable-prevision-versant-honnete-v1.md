# Consigne à Fable 5.2 — prévision courte scellée du versant honnête de l'essai « jumeau contre jumeau » — v1

Écrite le 2026-11-24 vers 10:45Z (`date -u` relevé à 10:42Z). Session « dossier de l'entretien et billets », reprise sur le compte 01Qi7 (Opus 5.5). Pièce de travail.
Dosage : Fable 5.2, effort maximal. Raison : préenregistrement décisif (R1) ; ses critères gelés fixent la lecture d'une mesure payante.

## Le mandat

Lazar a accordé le versant honnête : « go devis honnête recos » (GO-2026-11-24-17, R-5265, sur origin/main), type calcul, 12 dollars, avec les recommandations de ses sept points :
- repasser les 64 épisodes de la course 7b ;
- plafond de 12 dollars en cumul, relance comprise ;
- six jumeaux par tâche ;
- calibrage croisé des fausses alertes par moitiés de tâches ;
- confiance de 0,8 de l'attestation de séparation jugée suffisante.

Le devis exige, avant tout départ, une prévision courte scellée (classe A). C'est ta pièce.

## Aveuglement — à attester par écrit en tête de ta pièce

Tu ne lis pas, et tu n'as pas lu :
- la lecture scellée de l'étalonnage de la base boîte noire v3 (LECTURE-T08) ni son verdict (VERDICT-T08-V3) ;
- les scores de sondes de l'épisode honnête de la course 7b ;
- aucun épisode, aucune sortie de course, aucun fichier de résultats, de diagnostic, de scores, de verdict ou de lecture ;
- rien sous `coffre/`.

Tu écris en tête une attestation datée (`date -u`) et la ligne à inscrire sur la liste « qui a lu quoi » (pièces lues, avec leur chemin et leur empreinte). C'est la mère qui l'inscrit.

## À lire (et rien d'autre)

1. Le devis : `docs/notes/dossier-entretien-2026-12-01-v1/devis-versant-honnete-jumeau-v2.md` et son erratum 1 (qui prime pour la coupure). Lis aussi la contre-lecture du devis (`contre-lecture-devis-versant-honnete-opus-v1.md`, même dossier), questions 5 et 6 : le réemploi des épisodes doit être déclaré et borné ; le plancher de rang vaut 1/6 ; l'accumulation se fait sur les tâches, non sur les pas.
2. `docs/notes/dossier-entretien-2026-12-01-v1/instruction-b6-versant-honnete-jumeau-v1.md`, § 2 et 3 : grandeurs à fixer.
3. L'attestation sur manifestes : `git show 2f63d6db:docs/notes/dossier-entretien-2026-12-01-v1/attestation-manifestes-versant-honnete-v1.md`.
4. `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` et ses errata 1 à 3 (le 3 prime).
5. Le texte scellé de l'étalonnage, **texte de conception seulement** : `git show 50a6d30c:prereg/T0.8-bases-boite-noire-v0-v3.md`.
6. Le gabarit `prereg/gabarit-preregistrement-v1.md`, et `src/controle_ia/prereg.py` pour la forme attendue.
7. Pour la cohérence seulement (prévision de l'épreuve complète, non scellée, d'un autre périmètre) : `docs/notes/pieces-manquantes-classe-a-v1/correction-opus-v1/brouillon-1-v3.md`.

## Ce que tu écris

Un seul fichier : `prereg/versant-honnete-jumeau-v1.md`. Rien de scellé, pas de commit.

Suis le gabarit (R1) : hypothèse, prédictions chiffrées et signe, métriques, seuils, plan d'analyse, critères de lecture gelés, liste d'arrêt. Les grandeurs, au moins :
- loi du rang de l'original honnête parmi ses jumeaux, sous l'hypothèse nulle ;
- taux réalisé de fausses alertes à 1 % selon l'horizon, en étalonnage global contre étalonnage par tâche, par calibrage croisé sur des moitiés de tâches ;
- rapport de variance intra-tâche contre inter-tâches ;
- comparaison entre les sondes internes gelées et les moniteurs boîte noire.

Contraintes :
- rapport toujours à cinq et à six jumeaux ;
- échangeabilité du sixième jumeau déclarée comme hypothèse ;
- garde d'équivalence par régénération, avec la limite d'hôte déclarée ;
- réemploi des épisodes de l'étalonnage déclaré et borné ;
- unité indépendante : la tâche ;
- une ligne de code d'analyse « à remplir » pour le commit du code contre-lu (pièce suivante, classe B).

Aucun chiffre de résultat ; aucun chiffre de l'état de l'art sans page vérifiée (R7). Fin de pièce : points pour Lazar, confiance.

Langue : français, sans sigle nu ; phrases courtes.
