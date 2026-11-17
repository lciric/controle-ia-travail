# Contre-lecture neuve (R2), lecture courte — plan de lecture de la recourse de B-7, v3 — v1

Même contre-lecteur que pour les lectures précédentes (n'a rien écrit des pièces). Diff `plan-de-lecture-recourse-b7-v2.md` contre `-v3.md` lu en entier. Aucun résultat de
`diag/20261117-015632-…`, de `diag/20261115-120622-…` ni de R-2915 ouvert ; rien exécuté ; aucun fichier existant modifié ; aucun commit. Seul ajout : ce fichier.
Pour vérifier un nom, j'ai relu le code du lanceur v5 (déjà lu à la lecture précédente : `grandeurs-par-pole-b-alpha-graine1{suffixe}-v1.json`, clé `grandeurs.n` du résultat de l'audit).

## Verdict

**Prêt à sceller** (une précision facultative, non bloquante, ci-dessous).

## Les deux majeures

1. **Écart (a) « dans le bruit » : corrigée.** Le maximum de (a), pris par cible (« ablate win », puis « ablate pos »), est comparé au maximum de (c) ; les écarts cellule par cellule sont
   rapportés sans la phrase. Plus de choix au lecteur.
2. **Audit de B-7 non tenu : corrigée.** § 4 : « aucune lecture de B-7 de la recourse » si la série au lot 64 est en chaîne en défaut, non jouée, ou « non reproduit par le haut » avec audit non tenu, non joué,
   ou déclenché par le lecteur sans avoir été joué ; la lecture de la troisième course reste en vigueur avec son écart de lot. Phrases permises : une série sans lecture rend la comparaison « non comparable » ;
   « non reproduit par le haut, confirmé à la graine 1 » compte comme un verdict. Les trois cas que j'avais cités (audit non tenu, lecteur déclenche seul, issue pour « diffère ») sont écrits.

## Les mineures 3 à 8

- **3. Noms de la graine 1 : corrigée.** `grandeurs-par-pole-b-alpha-graine1-v1.json` et `…-graine1-lot64-v1.json` (conformes au lanceur v5), résumés `causal_lens_seed1[-lot64]_…`, et
  `grandeurs.n`, `temoin_bien_apparie`, `pilotage_norme_non_nulle` lus dans le résultat de l'audit « trop beau ».
- **4. Ordre de calcul : corrigée.** Nouvelle étape 3 bis : constat des fichiers d'audit par liste, avant le calcul et sans lire `b-alpha-verdicts*.json` ; le motif (trop beau / B-7) ne se lit qu'à l'étape 5
  (`motifs_audit`) ; divergence avec `audits_requis` et `motifs_audit` rapportée.
- **5. B-4 et marque de précision : corrigée** (B-4 dans « trop beau » ; « précision de ce plan, déclarée »).
- **6. Déclaration : corrigée** : fichier `declaration-lecteur-recourse-b7-v1.md`, horodaté par `date -u`, scellé avant l'étape 1 ; repris dans les livrables.
- **7. « Tout négatif » : corrigée** : verdict de reproduction « proposé, non tranché ».
- **8. Renvoi d'empreinte : corrigée** : `verdict-recourse-b7-v1.md` cite l'empreinte du plan scellé, de sa contre-lecture et de la déclaration.

## Reste-t-il un choix laissé au lecteur après résultat ?

Non, sauf un point d'importance négligeable : si, pour la graine 1, le `n` du fichier de grandeurs et celui de la clé `grandeurs.n` du résultat de l'audit divergeaient, le plan ne désigne pas la source qui fait foi.
Le principe d'en-tête (« n'arbitre aucune ambiguïté : il la signale et donne le verdict sous chacune des lectures ») s'applique ; une ligne « divergence rapportée, (3) donné sous les deux » dans la v3 suffirait,
mais ne justifie pas une nouvelle version. Le lanceur écrit les deux depuis le même calcul : la divergence est improbable.

## Vérifié

- Le diff ne touche aucune règle de seuil, bande ou définition ; ce qui était fidèle en v2 l'est resté.
- Aucun défaut nouveau introduit : l'étape 3 bis ne contredit pas l'étape 4 (le calcul de (3) vient avant la lecture des verdicts et du code de la course) ; « aucune lecture » (au lieu de « aucun verdict ») est cohérent avec
  les formules « confirmé / non confirmé » et avec les phrases permises.
