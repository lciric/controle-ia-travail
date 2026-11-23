# Mandat — rédacteur Fable : brouillon 2 de l'additif et du devis de la voie (A) — v1

Pièce de travail (classe C), exécutante v5, le 2026-11-22, sur la demande de la mère. Rédacteur : Claude Fable 5.2. Suite du mandat `registres/iib-executante/mandat-fable-additif-ordre-course-et-devis-v1.md` (0ead00d9…), dont les § 2 et § 4 (contraintes et interdits) restent en vigueur.

## 1. Ce que tu rédiges
Le **brouillon 2** de `additif-ordre-course-voie-A` et de `devis-voie-A` (R12 : le brouillon 1 reste intact), qui porte **toutes** les corrections de la contre-lecture :
`registres/iib-executante/contre-lecture-voie-A-v1/contre-lecture-additif-et-devis-voie-A-v1-cl1.md` sur `origin/claude/iib-executante-v5`, sha256 922a3ecfc6ba7919b9b48dbd49ebbd24662ba7c6ae9f3fe6c5c4a94eae5a97df (verdict « scellable après corrections » ; corrections exactes et table des champs dedans), plus une note des différences, une ligne par correction. La voie (B) n'est pas à reprendre (gardée pour plus tard).

## 2. Décisions prises, à écrire
- **Ligne** : `GO_ID=GO-2026-11-22-75` (`registres/go.md` de `main`), 60 USD de dépense neuve hors les 16,22 USD déjà dépensés ; plafond 60, coupure 55 ; **configuration neuve** citant cette ligne (entropie tirée par la mère au scellement) ; la borne de 5 USD de dépense antérieure (code figé) est un écart déclaré ; aucune création à partir du 2026-11-27T00:00:00Z ; minuterie au plus tard 2026-11-30T22:00:00Z.
- **Essai de vitesse (option (b), mot de la mère)** : pas de machine de plus. La vitesse se mesure **en marche, sur le premier lot de l'étalonnage rejoué**, avec la **liste d'essais d'étalonnage v7**, qui porte l'essai de déterminisme sur carte (correctif 0022, en cours : chemin et empreinte donnés par l'exécutante). Récris la règle de décision (seuil, garde de rythme) sur ces marques.
- **Tirage** : variable `IIB_TIRAGE=carte` à l'étalonnage et à la course (non une clé de configuration) ; vérifier `-e IIB_TIRAGE=carte` dans la commande imprimée ; arrêt si le journal ou la marque de chargement dit autre chose ; la garde « même tirage » du correctif 0021 refuse une course qui tirerait autrement.
- **Code** : branche distante `prep/iib-tirage-carte-v1`, tête 6696aca1fc57df7e4d5d3a26b3f25dd05d0d4f58, arbre 725f3d5884c3617065aa913d04e9b3eee0e2afac (correctifs 0014 à 0021) ; plus 0022 à venir. Essais attendus : course 312 (liste v2, sur carte) ; étalonnage : nombre de la liste v7, à venir.
- **Machine** : une seule à la fois ; 61875617 doit avoir disparu de l'inventaire avant toute création (destruction par Lazar, console du loueur).
- **Recharge automatique du crédit activée** (GO-2026-11-22-73) : reformuler la règle « aucune création sans recharge » en « crédit relevé avant chaque création ».

## 3. Pièces de plus à lire
Sur `origin/claude/iib-executante-v5` : `registres/iib-executante/p1-code-course-v1/` (correctifs 0020, 0021, rapports v4 et v5, `contre-lecture-tirage-carte-0020-cl1.md`, `note-verification-0021-cl1.md`, `constat-lanceur-de-session-trois-points-v1.md`) ; registre `registres/go.md` de `main` (GO-2026-11-22-71, -73, -75).

## 4. Ce que tu rends, et où
Sur ta branche `claude/iib-executante-v5-fable-additif-c`, dossier `brouillons/ii-b-saboteur-budget-v5/additif-course-v1/` : `additif-ordre-course-voie-A-v1-brouillon2.md`, `devis-voie-A-v1-brouillon2.md`, `differences-voie-A-brouillon1-vers-2.md`, le programme de calcul v2 et sa sortie, chacun avec son compagnon `.sha256` ; puis un message à l'exécutante (session_01XJ6MgqUTEVCed6a2f6rWmC) et à la mère, chemins et empreintes.
