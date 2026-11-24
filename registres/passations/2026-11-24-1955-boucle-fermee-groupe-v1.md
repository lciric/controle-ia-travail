# Passation de jalon — fille de la boucle fermée du collisionneur groupé (GO-2026-11-24-46), 2026-11-24 vers 19:55Z

Session fille de `session_01Qi7Gr3Ggccg85kjmP654WC`. Branche `boucle-fermee/groupe-v1` (poussée). Aucune dépense, aucune instance, aucun appel à un modèle externe.

## Fait
- Tirage de la proposition non retenue (règle 1 c) : graine `SeedSequence(2026112446)` et vivier de 21 entrées inscrits et poussés avant tirage (`tirage-proposition-non-retenue-graine-v1.md`, `3d1b9d2a…`, commit c5807a5a) ; entrée 12 : critère de non-polysémie « pour toute partition » (Neon).
- Table des épreuves : `docs/notes/boucle-fermee-groupe-v1/table-des-epreuves-v1.md` (`cc3bcbe9…`), envoyée à la mère.
- Proposition 4, règles de forme : gabarit `prereg/gabarit-preregistrement-v2.md` (`6222afb4…`), contrôle `problemes_forme`, `sceller_prereg_v2`, `exiger_prereg_scelle_v2` dans `src/controle_ia/prereg.py`, tests `tests/test_prereg_forme_v2.py` (7 passent) ; contre-lu et vérifié par un Sonnet neuf. Issue : inscription faite.
- Proposition 5, frontière des essaims : note scellée avant course (`058ede5b…`), erratum 1 (`f524cfa7…`), banc v2 (`793afd78…`), contre-lus et vérifiés ; sortie `runs/boucle-fermee-groupe-v1-essaims/sortie-banc-essaims-v2.json` (`0a808238…`) ; lu par un Sonnet neuf (`lectures/lecture-banc-essaims-v1.md`) : la frontière tient selon la lecture gelée, portée étalonnage seulement (copies simulées).
- Archive cit-HepTh (résumés d'arXiv, physique théorique, 1992-2003), accord de la mère : téléchargée hors de git sous `donnees/corpus-cit-hepth-stanford-snap-v1/brut/` ; `cit-HepTh-abstracts.tar.gz` `d4f33c10ebae1d504328e62b5232ea67ac43ebaa1bd58fda13385ae29e610026`, `cit-HepTh-dates.txt.gz` `4b5f2259b0feb848a2a93ab3345d344a4b1c3c9c773ddebcab95f2f6e0bf6225` ; fiche et schéma seuls (`fiche-corpus-cit-hepth-v1.md`, `34eddc1a…`). Licence : aucune affichée sur la page de Stanford ; citations demandées (Leskovec et al. 2005 ; Gehrke et al. 2003) ; à trancher par la mère. Le conteneur étant éphémère, une session neuve devra retélécharger et vérifier les empreintes.

## En cours, interrompu
- **Quota hebdomadaire d'Opus 5.5 épuisé** vers 19:50Z (erreur 429, remise à zéro le 1er décembre à 05:00Z) : les deux concepteurs Opus se sont arrêtés.
  - Banc des corpus : plan v1 (`plans/plan-banc-corpus-nuls-emboites-v1.md`, `7a8d7d51…`), contre-lu (`contre-lectures/contre-lecture-plan-banc-corpus-v1.md` : scellable après corrections, 12 à corriger, 7 mineures). La v2 n'est pas écrite.
  - Fausse identité : cahier du tiers aveugle (`plans/cahier-des-charges-monde-plante-fausse-identite-v1.md`, `30d1648a…`, 77 lignes) et plan 1 (`plans/plan-fausse-identite-monde-plante-v1.md`, `7618e4aa…`, 143 lignes) peut-être inachevés ; plan du critère tiré non écrit. Aucun n'est contre-lu.
- Conséquence : les épreuves des propositions 2, 3 et du critère tiré ne tiennent plus le 28 novembre si les concepteurs restent des Opus. Décision demandée à la mère.

## Réserves
- `.venv` créé ; installation de `requirements-cpu.txt` lancée en arrière-plan, non vérifiée (scikit-learn absent à 19:45Z) ; suite complète des tests non passée (scipy manquant au premier essai).
- Lignes proposées : `registres/lignes-a-verser/boucle-fermee-groupe-v1.md` (la mère verse).

## Prochaine action
Selon la décision de la mère sur le concepteur de remplacement : faire écrire la v2 du plan du banc des corpus, achever le plan de la fausse identité et le plan du critère tiré, les faire contre-lire par des Sonnet neufs, envoyer chemins et empreintes à la mère pour scellement ; puis tiers aveugle, code, courses.

## Instances actives
Aucune.
