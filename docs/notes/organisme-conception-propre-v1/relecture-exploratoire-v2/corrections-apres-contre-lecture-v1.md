# Corrections décidées après la contre-lecture (modèle C) — relecture exploratoire v2 — v1

Écrit par le préparateur (modèle A), le 14 novembre 2026, de 12:50 à 12:58 UTC environ (`date -u`), **avant** d'écrire le
générateur v2.1, de tirer le hasard v2.1 et de modifier l'outil ou le classement. Réponse à
`contre-lecture-modele-c-v1.md` (`18b28285…`, verdict « utilisable sous conditions », aucun bloquant). Toutes les
corrections font des **versions neuves** (R12) : `regle-v2-1.md`, générateur et contrôles v2.1, `temoins-hasard-v2-1.json`,
outil et classement **v3.2.1**, devis v2. La v3.2 n'a jamais servi (aucun dossier préparé) : la v3.2.1 garde ses noms de
fichiers écrits et son dossier (`lecture-g1-v3-2/`, `manifeste-relecture-v3-2.json`) ; seul le nom de version change dans le
manifeste, et l'envoi refuse un manifeste d'une autre version.

| Constat | Décision |
|---|---|
| **M1** « séparation de forme » non fondée (puissance faible, n = 8) | Issues renommées : « **séparation réelle (portée par R7)** » si p ≤ 0,05 ; « **séparation non établie sur R7 (n = 8)** » sinon ; « pas de séparation » si L5 v2 ne rejette pas. Table de puissance exacte déclarée d'avance (ci-dessous). Classement v3.2.1. |
| **M2** hasard reconnaissable (dispersion, phrases, fragments répétés, opérations répétées) | **Hasard v2.1**, corrigé sur le style seulement (règles ci-dessous) ; contrôles ajoutés, fixés ici avant tout tirage ; première sortie qui passe tous les contrôles retenue ; traits restants déclarés au § 9 de la règle v2.1 (objets tous numériques). |
| **M3** les publiées reprennent le vocabulaire du catalogue | Déclaré au § 9 : L1 mesure la reconnaissance d'un mécanisme dans des mots proches du catalogue, non dans une paraphrase lointaine. Témoins inchangés (éprouvés). |
| **M4** plafond = tout le reste | **Plafond proposé : 6,50 USD** (devis v2) : couvre la sortie triple de la première lecture ; la constante absolue de l'outil reste 11,65. Seuil du premier appel recalculé au devis v2. |
| **M5** statut des relecteurs de l'épreuve | Précisé : sous-agents lancés par le client de la session (même compte, même usage que tout sous-agent de la session), hors de toute ligne de GO et hors du fournisseur de la lecture ; à la mère de dire s'ils s'inscrivent. |
| **M6** exactitude circulaire pour les critères non porteurs | Règle v2.1, § 7 : exactitude **descriptive** ; pour les critères non porteurs, les valeurs attendues sont le consensus de deux relecteurs de modèle C : comparaison rapportée, jamais interprétée comme une erreur d'Astra. |
| **m1** sous-règle du tour 2 | Déclarée comme écart à l'engagement (§ 6) : écrite dans `temoins-lecteur-v2-epreuve-2.json` (champ `regle`, scellé avant le lancement des relecteurs du tour 2). |
| **m2** verdict non lisible ambigu | Classement v3.2.1 : « (non lue : classement non lisible) » après l'issue de séparation. |
| **m3** codage du signe « 0 » | Dit au § 5 de la règle v2.1 (chaîne sur le coût, sens attendu : baisse). |
| **m4** T2-V lu strictement | Déclaré au § 9 (deux appels par proposeur et par génération, e-BH et test de mort à mi-génération, antériorité supposée). |
| **m5** « réserve du lecteur » | Sans objet depuis R-2726 (la ligne GO-2026-11-13-06 et son reste sont la seule borne) ; à confirmer par la mère. |
| **m6** bancs sans trace | Versés (`…/resultat-mutations-*.json`, 30 sur 30 et 15 sur 15) ; rejoués sur les versions neuves. |
| **m7** dossier de relecture supprimé en entier | Limite de la v3.1 conservée ; condition d'emploi : toute seconde préparation est un nœud et déclare la dépense des relevés du dossier perdu. |

**Puissance du test de R7 seul** (exacte, loi hypergéométrique, 23 réelles contre 8 idées au hasard, unilatéral ; calculée
par programme) : la séparation est « réelle » si le nombre j d'idées au hasard à R7 retenu = 1 ne dépasse pas : j ≤ 0 pour
10 à 12 réelles à R7 = 1 ; j ≤ 1 pour 13 à 15 ; j ≤ 2 pour 16 et 17 ; j ≤ 3 pour 18 à 20 ; j ≤ 4 pour 21 ; j ≤ 5 pour 22 et 23.
(Valeurs : p(13, 1) = 0,038 ; p(12, 1) = 0,058 ; le contre-lecteur, par calcul à la main, donnait 0,058 pour 13 et 1.)

**Hasard v2.1 : changements, sur le style seulement** — (a) opérations tirées sans remise entre les huit (deux au plus en
double, une seconde permutation complétant la première) ; (b) ressources des justifications tirées sans remise ; (c) neuf
tournures d'arrondi sans fragment commun ; (d) gabarits qui commencent pareil réécrits ; (e) dispersion des longueurs : chaque
fiche reçoit un rang de longueur u tiré dans [0,05 ; 0,95], et la cible de chaque champ suit la répartition réelle à ce rang
(à ± 0,15 près) ; (f) moins de suites en « ; » (jointures par virgule là où la phrase le permet). Graines inchangées
(`SeedSequence(2026111411)`) ; aucune lecture d'un modèle ne guide un changement.

**Contrôles ajoutés au hasard v2.1** (avant tout tirage ; ceux de la v2 restent) : (1) aucune opération plus de deux fois ;
(2) écart interquartile des longueurs totales du hasard ≥ la moitié de celui des réelles ; (3) médiane des phrases par fiche
dans l'intervalle interquartile des réelles, médiane des mots par phrase aussi (mesures de `stats_forme_fiches_v1.py`) ;
(4) toute suite de quatre mots présente dans au moins trois idées au hasard (champs libres) figure aussi dans au moins un
témoin du lecteur (vocabulaire du domaine, non remplissage de gabarit).
