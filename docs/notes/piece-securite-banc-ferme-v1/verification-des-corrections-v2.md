# Vérification des corrections — pièce de sécurité du banc fermé, v3 — v2

- **Pièce vérifiée** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v3.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `96b79c798f786bc77d7374cb4bc794b289af80a1`. Empreinte recalculée : `d016d9d9e35c93af11d4ad304ffdf6ffbe3cec71a96bba1d0303626e024a4f9e`, égale au `.sha256`. Les versions précédentes sont intactes : v1 `a4d515fc…`, v2 `0064c4be…`, toutes deux recalculées.
- **Référence** : `verification-des-corrections-v1.md`, commit `a329fac5`, `5554992738da69831ec2c3691b650bee94ecea8e8c64fa840a6d7a2ed27a9b63`, qui demandait une v3 ne corrigeant que le point N1.
- **Vérificatrice** : la même contre-lectrice (Opus 5.5). **Date** : 21 novembre 2026, vers 18:30 UTC.

## Constat

La différence ligne à ligne entre la v2 et la v3 compte exactement deux lignes :
1. le titre, « v2 » devenu « v3 » ;
2. la ligne [R611] de la table des sources, dont l'empreinte est maintenant `ba86f8f89cbce31c86047f0dcc8ca420d965aec2516580e1618c778448fbf1e9`. C'est celle que j'ai recalculée sur `registres/decisions.md` au commit `d5635e17…`. La ligne [R888] renvoie à « même empreinte » et est donc juste elle aussi.

**N1 : corrigé.** Rien d'autre n'a changé, ce qui était la demande.

**Remarque, sans point** : la ligne « Version » de l'en-tête dit encore « v2 ». C'est la conséquence de la consigne « sans autre différence » ; le titre, le nom du fichier et l'empreinte désignent sans ambiguïté la v3. Ce n'est pas un point à corriger. Une v4 éventuelle le reprendra.

**Mot de Lazar rapporté hors registre** : l'auteur signale un mot qui trancherait le nœud 1. Il ne l'a pas trouvé sur `main` et ne l'a donc pas porté. C'est conforme : un mot rapporté n'entre dans une pièce scellée qu'une fois lisible au registre. Il appartiendra à une v4, contre-lue à son tour.

**Contenu d'attaque** : aucun. **Refus de classifieur** : aucun.

## Verdict final

**Accepté** : la pièce de sécurité du banc fermé, v3 (`d016d9d9…`). Au total, la contre-lecture et ses vérifications ont relevé deux points bloquants et huit mineurs (sept dans la contre-lecture, un neuf dans la v2) ; tous sont corrigés.

L'acceptation porte sur la pièce comme dossier de sécurité. Elle n'autorise aucune construction, aucune exécution ni aucune dépense, et elle ne tranche pas les trois nœuds renvoyés à Lazar (section 7 de la pièce).
