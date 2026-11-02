# Addendum au préenregistrement de R1 — relance du rejeu des 2 400 actions de P3 après l'arrêt sur la garde CLC-03 — v1

- Auteur : sous-agent de préparation de la session « session-depot » (Opus 5.5), pour Lazar ; **brouillon 1**, non
  scellé, non contre-lu. **Lazar n'a pas décidé** : modifier une règle d'un préenregistrement scellé est un nœud de
  décision (CLAUDE.md, hiérarchie de décision : « écart à un préenregistrement scellé »).
- Date (UTC) : 2026-11-02 ≈ 03:10.
- Préenregistrement parent (scellé, non modifié) : `prereg/R1-R2-rejeu-p3-v1.md`
  (`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`), commit de scellement
  `567260c05687747f0c7a715fc9b15b4fc6297d65` (branche `prep/runs-r1-r2-r4-v1`), code cité `29bd8e2e…`.
- Chemin du préenregistrement parent : `prereg/R1-R2-rejeu-p3-v1.md`
- Commit du code d'analyse : `5b72e2e2a1f6d42a3fecbfc3001b86dbbf77154f`
- Documents qui font foi (chemin + empreinte) : le préenregistrement parent ci-dessus, qui garde tout ce que le présent
  addendum ne remplace pas ; rapport d'enquête `docs/notes/runs-r1-r2-r4-v1/enquete-arret-r1-v1.md`
  (`377101ecd9b33c76c34ce799f8b511d60b71b089699a7df3dc0e4705ccbb00c3`) ; arrêt de R1
  `diag/20261102-002114-r1-rejeu-reel/arret.json` (`c6671d2c9534463f82da90c21eba80f29a2bce04e898643b59a0caa4c9a9eb07`,
  branche `calcul/r1-r2-reel-v1`) ; message n° 339 de conv-audit (branche `canal/conv-audit-n04`,
  `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-11-02_n339.md`,
  `05179024bfe3332aa032ade5302f8f4b3373a618a2cb950f61f2ce0ea58d7794`) : exigences de leur analyse principale scellée
  (`8e267952…`) ; **GO-2026-11-01-13** (`registres/go.md`, plafond 25 USD, échéance 2026-11-02).
- Chemin de la configuration du rejeu : `prereg/R1-rejeu-config-v3.json`
- Configuration du rejeu (empreinte canonique) : `6f8a285d8c29b1706d923bf33921ba2e4e7b22eaa9865a75e50cedb9d02dd5b6`
- Chemin de la table de tokenisation : `prereg/R1-table-tokenisation-v1.json`
- Table de tokenisation (empreinte du fichier) : `5309326bc307d9849745a7b51f259661bf7bfb68b0508449d45903868e0cbd5c`
- Entropie : `36410133060804533274328900142752730279`
- Tests attendus : `299`

**Statut.** Cet addendum remplace **une seule règle** du préenregistrement parent, la garde CLC-03 (« un épisode
entièrement conforme en longueur à trajectoire différente arrête la course »), par les règles A et B ci-dessous, et
ajoute le seuil qui les borne. Tout le reste du parent vaut tel quel (section « Ce qui ne change pas »). Il porte sur
**R1 seule** ; R2 ne se relance pas. L'entropie est celle du parent (aucun choix libre) ; l'échantillon de fidélité est
retiré parmi les éligibles de la relance (épisodes à trajectoire identique), donc différent de celui qu'aurait tiré la
première course, qui s'est arrêtée avant ce tirage.

## Cause de l'arrêt (renvoi au rapport)

R1 (instance du 2 novembre 2026, ≈ 00:21 UTC) s'est arrêtée sur CLC-03 : « 21 épisodes entièrement conformes en
longueur à trajectoire différente » (`arret.json` ci-dessus). Cause établie par l'enquête (rapport cité, sections 1 et 2,
reproduction sans modèle identique à l'instance : 151 épisodes conformes en longueur, 129 identiques, 22 signalés ; 130
et 21 après la substitution du jeton de fin) : **la garde supposait qu'un épisode conforme en longueur a forcément les
identifiants de P3 ; c'est faux.** À température 1, l'agent de P3 a parfois échantillonné un **découpage non canonique**
d'un mot, de même longueur en jetons et qui se décode en le même texte (`Ġro` + `crap` au lieu de `Ġroc` + `rap`). Le
texte stocké ne le dit pas ; l'empreinte de trajectoire stockée par P3, qui couvre les identifiants, le voit. Ni le
gabarit, ni la date, ni la consigne, ni une version de bibliothèque (manifestes comparés, rapport section 2).

## Hypothèse

Inchangée (parent, section « Hypothèse » : H-R1 ; H-R2 est hors de cet addendum, voir « R2 »). **Hypothèse de travail
précisée** : la reconstruction d'un épisode est la tokenisation du texte seul plus le jeton de fin compté par P3
(parent), **corrigée par la table de tokenisation** quand la table redonne exactement l'empreinte de trajectoire de P3 ;
un épisode conforme en longueur que la table ne résout pas n'est pas en contexte exact et n'entre pas dans les actions
fidèles.

## Prédiction chiffrée et signe attendu

P-R1 à P-R4 : inchangées (parent). **P-R5 (instruments), ainsi modifiée** : contrôle de fidélité conforme ; contrôle
négatif discriminant (prédiction incertaine, inchangée) ; **trajectoires identiques à P3 : 144 épisodes sur 240**
(129 de la reconstruction de base, plus 15 corrigés par la table : 1 par le jeton de fin, 12 par une paire redécoupée,
2 par deux paires), mesurées sur processeur avant la carte (section « Plan d'analyse », étape 0) ; **épisodes non
conformes (règle B) : 7, au plus 10** ; **au moins 90 % des actions notées fidèles** (critère du parent et de l'analyse
de conv-audit, n° 339). Valeur attendue, calculée sur processeur sans aucun score (« notée » = `jetons_notes` > 0) :
les 2 400 actions sont notées ; **borne haute 2 166 / 2 400 = 90,25 %** (actions conformes en longueur, hors
des 70 actions des 7 épisodes non conformes, si toutes restent dans la tolérance) ; **borne basse 1 712 / 2 400 =
71,3 %** (seules les actions en contexte exact passent). Par condition, borne haute / contexte exact : honnête 538 / 441,
saboteur 546 / 427, témoin 522 / 358, mention 560 / 486 (`docs/notes/runs-r1-r2-r4-v1/comptes-table-relance-v1.json`).
**P-R5 ne tient que si au plus 6 des 454 actions conformes hors contexte exact sortent de la tolérance** : prédiction
**incertaine, plutôt contraire** (confiance ≈ 0,3 qu'elle tienne). La règle B retire 70 actions de la borne haute du
parent (« au plus 93 % », 2 236 / 2 400). Si P-R5 est contraire, la lecture suit le parent et l'analyse de conv-audit
(réserve d'instrument, voir « Critères de lecture gelés ») ; rien n'est relancé pour la faire tenir (R3). Masse {Yes, No} : sans objet (R2 ne se relance pas).

Note de compte : le rapport d'enquête annonce « 145 épisodes à trajectoire identique (au lieu de 130) » ; le bon compte
est **144** : les 130 de l'instance comprennent déjà l'épisode résolu par le jeton de fin, que la somme 130 + 15
comptait deux fois (129 + 1 + 12 + 2 = 144).

## Métrique

Inchangée (parent). Seule précision : les actions des épisodes non conformes de la règle B ont `fidele` = faux ; elles
sortent donc de toutes les lectures, pour tous les bras (« seules les actions notées par P3 et fidèles au rejeu
entrent », parent), comme l'exige l'analyse principale scellée de conv-audit (n° 339 : exclusion action par action, même
ensemble pour tous les bras).

## Seuil

Inchangés (parent), plus : **seuil de la règle B = 10 épisodes** (`seuil_non_conformes` de la configuration v3). Au plus
10 épisodes non conformes : la course continue et le verdict du run reste « conforme » ; au-delà : arrêt.

## Plan d'analyse

**Étape 0 — table de tokenisation (processeur, avant la carte, déjà faite ; règle A).** Pour chaque épisode conforme en
longueur dont l'empreinte de trajectoire diffère de celle de P3, une recherche **déterministe, sans choix libre**, arbitrée
par la seule égalité d'empreinte avec P3, dans un **ordre fixe**, premier succès retenu : (1) substitutions du jeton de fin
(une, puis deux ; même fonction que la v1) ; (2) une paire de jetons voisins des jetons notés d'une action, redécoupée en
deux jetons ordinaires du vocabulaire couvrant les mêmes octets (même longueur, même texte) ; (3) deux paires disjointes.
Ordre des candidats : pas, rang dans l'action, point de coupe croissants ; couples dans l'ordre de
`itertools.combinations`. Code : `src/controle_ia/runs_nuit/resolution_tokenisation_v1.py` ; commande :
`python -m controle_ia.runs_nuit.resolution_tokenisation_v1 --tokeniseur <tokeniseur de la révision 0e9e39f2…>
--config prereg/R1-rejeu-config-v2.json --sortie prereg/R1-table-tokenisation-v1.json` (≈ 30 min sur processeur).
Tokeniseur : fichiers publiés de la révision citée (`tokenizer.json` `79e3e522…`, `tokenizer_config.json` `177c7b61…`,
55 351 octets ; empreintes écrites dans la table). Résultat (table, `comptes`) : 22 épisodes signalés ; 1 résolu par le
jeton de fin, 12 par une paire, 2 par deux paires, **7 non résolus** — les mêmes résolutions que le rapport d'enquête,
épisode par épisode. Chaque correction est revérifiée, au moment du calcul, par la fonction que l'instance appliquera.

**Étape 1 — R1 relancée (instance).** Module `controle_ia.runs_nuit.rejeu_activations_v2` (nom nouveau ; la v1 citée par
le parent n'est pas modifiée et ses fonctions sont importées telles quelles). Reconstruction de base de tous les épisodes
sur processeur, comme la v1 ; puis :
- **Règle A** : la table (empreinte citée par la configuration, sceau vérifié) doit couvrir **exactement** les épisodes
  conformes en longueur à trajectoire différente, dans les deux sens ; chaque correction est appliquée avec ses gardes
  (jeton de fin parmi ceux du format ; paire canonique à sa place ; mêmes octets ; jetons ordinaires ; même longueur ;
  même texte au décodage) et **doit redonner exactement l'empreinte de trajectoire de P3** ; les bornes des champs sont
  recalculées sur les identifiants corrigés. Les épisodes corrigés deviennent « trajectoire identique » (éligibles à
  l'échantillon de fidélité, contexte exact). La recherche à la volée du jeton de fin de la v1 passe dans la table (même
  fonction, même ordre).
- **Règle B** : un épisode conforme en longueur que la table déclare non résolu est **classé non conforme** au lieu
  d'arrêter la course : `fidele` = faux pour toutes ses actions, `contexte_conforme` = faux, `trajectoire_identique` =
  faux ; `conforme_longueur` garde la mesure par action (vrai). **Arrêt si ces épisodes sont plus de 10.**
- Le contrôle négatif rejoue les épisodes corrigés **avec leurs identifiants corrigés** sous la consigne fausse (seule la
  consigne diffère du contexte exact) ; ses règles sont celles du parent.
- Tout le reste est le parent : échantillon de fidélité (5 par condition, clé « fidelite », parmi les notées à
  trajectoire identique), contrôle négatif (18 sur 20), règle de repli gelée, passe avant unique, couches 7, 15 et 23,
  agrégats, tolérance 0,02 × (1 + |score|).
- **Sorties : mêmes fichiers, mêmes tableaux, mêmes noms, mêmes formes et mêmes types que le parent** (exigence du
  n° 339 ; vérifiée par un test contre la v1) : `activations-p3-rejeu-v1.npz` (`moyenne` (2400, 3, 4096) float16),
  `activations-p3-rejeu-v1-maximum.npz` (`maximum`), `activations-p3-rejeu-v1-complement-hors-cout.npz`
  (`maximum_hors_cout`), sous `donnees/<run>/` d'un run neuf (aucun fichier n'est écrasé, R12) ; clés communes
  inchangées. Résultat du run `diag/<run>/rejeu-activations.json` : clés du parent inchangées, `verdict_fidelite` =
  « conforme » quand la course va au bout (au plus 10 épisodes non conformes) ; clé descriptive ajoutée `tokenisation`
  (empreinte de la table, corrections par méthode, épisodes et actions non conformes, seuil, part des notées fidèles et
  drapeau de P-R5). Un arrêt écrit `arret.json` avec « non conforme » (fidélité, contrôle négatif, ou plus de 10 non
  conformes) ou « echec » (toute autre cause, table falsifiée comprise).
- Script d'instance `scripts/r1_relance_instance_v2.sh` et amorce `scripts/amorce_instance_r1_relance_v2.sh` (noms
  nouveaux) : `ETAPES=rejeu` seule valeur admise ; branche de résultats `calcul/r1-relance-reel-v1` ; l'addendum, la
  configuration v3, la table et le parent doivent être présents et scellés au commit lancé, sinon arrêt avant
  l'installation ; suite ciblée de 18 fichiers (celle du parent plus `tests/test_runs_nuit_v2.py`) ; plafond de l'amorce
  100 minutes. Lancement : commande au chemin littéral `…/vastai create instance` précédée de
  `GO_ID=GO-2026-11-01-13` (garde de calcul éprouvée : `docs/notes/runs-r1-r2-r4-v1/essai-garde-calcul-relance-v1.txt`).

**R2.** **R2 ne se relance pas** : ses scores existent déjà (`donnees/20261102-004328-r2-juge3b-reel/scores-juge3b-p3-v1.npz`,
`10838eea884baefd1921aa7fb6f603b288fd02d46ed177845ebbda6291cdd354` ; `donnees/20261102-005048-r2-juge8b-reel/scores-juge8b-p3-v1.npz`,
`1ebbeff89fe7ff4a6da834651b0701b0cfde8cce9781ca6e2318224d872e8d4b` ; branche `calcul/r1-r2-reel-v1`). **Aucune lecture
de R2 n'a lieu avant que R1 relancée ait rendu son résultat** (ni étiquette, ni score, ni métrique ; aucun bras ne se
compare sans les fidèles de R1, qui fixent l'ensemble commun des actions) ; la lecture suit l'analyse scellée de
conv-audit, après la vérification de concordance par un lecteur neuf (parent, « Statut »).

**Coût et GO.** R1 seule, même gabarit d'instance que la première course (A100 SXM4 80 Go, ≤ 1,40 USD de l'heure) :
≈ 1 h, soit **≈ 1,0 à 1,4 USD** (tarifs relevés de 1,01 à 1,37 USD de l'heure ; rapport, section 3) ; au pire, plafond de
l'amorce 100 minutes × 1,40 USD ≈ 2,3 USD plus le disque. Dans **GO-2026-11-01-13** (plafond 25 USD ; dépenses déjà
engagées sous ce GO au registre des dépenses : R1-R2 ≈ 1,0 USD, R4 à relever). **Échéance du GO : 2026-11-02** ; la
garde de calcul refuse le lancement après ce jour : une relance plus tardive exige une ligne d'extension de Lazar dans
`registres/go.md`. **Repli** si la relance échoue (fidélité contraire, plus de 10 non conformes, table non applicable) :
relance de l'environnement (≈ 3 h, ≈ 3 à 4 USD), devis et préenregistrement neufs (parent, critères de lecture).

**Essais (processeur, sans dépense).** Table rejouée sur les vraies pièces de P3 par le chemin de l'instance jusqu'à la
carte (`docs/notes/runs-r1-r2-r4-v1/comptes_table_relance_v1.py`, sortie `comptes-table-relance-v1.json`) : 144
trajectoires identiques, 7 épisodes non conformes (70 actions), chaque correction redonnant l'empreinte de P3. Essai
jouet de bout en bout de l'amorce v2 (`docs/notes/runs-r1-r2-r4-v1/essai-jouet-relance-v1/`) : cas sain (une correction
par le jeton de fin, fidélité conforme, contrôle négatif 4 sur 4, sorties poussées, code 0) ; table falsifiée (arrêt,
« echec », rien d'écrit, code 1) ; `ETAPES` avec un juge refusée, addendum non scellé refusé (code 2, avant
l'installation). Suite ciblée de 18 fichiers au commit du code : 299 passés (291 du parent et 8 nouveaux).

## Ce qui ne change pas

Hypothèses H-R1 et H-R2 ; prédictions P-R1 à P-R4 ; métrique principale et secondaires, bras, plancher apparié, plis,
intervalles ; seuils (taux de fausse alarme, tolérance de fidélité, contrôle négatif 18 sur 20, règle de repli gelée) ;
critères de lecture gelés autres que la ligne remplacée ci-dessous ; liste d'arrêt du parent hors CLC-03 ; formats de
sortie (fichiers, tableaux, noms, formes, types) ; run source, pièces de P3 et leurs empreintes ; entropie ; couches.

## Critères de lecture gelés

Ceux du parent, à une ligne près. La ligne « Fidélité contraire, ou épisode conforme à trajectoire différente → rejeu non
validé » devient :

| Issue observée | Lecture |
|---|---|
| Fidélité contraire, **ou plus de 10 épisodes conformes en longueur non résolus par la table, ou table non applicable** (épisode signalé absent, épisode en trop, correction qui ne redonne pas l'empreinte de P3) | Rejeu non validé : rien n'est lu ; repli = relance de l'environnement (≈ 3 h, devis et préenregistrement neufs) |
| Au plus 10 épisodes non conformes (règle B) | Course normale ; leurs actions hors des fidèles ; nombre et liste rapportés par condition |
| Fidèles < 90 % des notées (P-R5) | Réserve d'instrument (P-R5 contraire), rapportée ; les critères du parent s'appliquent (moins de 80 % parmi saboteur ou honnête : non concluant, rejeu partiel) |

Toutes les autres lignes du parent valent telles quelles.

## Liste d'arrêt

Celle du parent, sauf l'arrêt « épisode entièrement conforme à trajectoire différente » (CLC-03), remplacé par :
- table de tokenisation absente, non scellée, ou d'empreinte ≠ citée par la configuration ; table calculée sur d'autres
  pièces (empreintes des textes, des scores ou des fiches ≠ celles de la configuration) ; version ou méthode inconnue ;
  épisode en double : arrêt avant la carte (« echec ») ;
- épisode signalé absent de la table, ou épisode de la table non signalé : arrêt (« echec ») ;
- correction de la table qui viole une garde ou ne redonne pas exactement l'empreinte de trajectoire de P3 : arrêt
  (« echec ») ;
- **plus de 10 épisodes non conformes** : arrêt (« non conforme ») ;
- préenregistrement parent absent, non scellé, ou d'empreinte ≠ `80c85a00…` : arrêt ; addendum qui ne cite pas la
  configuration, l'empreinte du parent, l'entropie ou le commit du code : arrêt ;
- `ETAPES` autre que `rejeu` : arrêt avant l'installation.
Dans tous ces cas : `arret.json` consigné, aucun fichier d'activations écrit ; arrêt de l'instance par son identifiant
(R10).

## Contre-lecture

À REMPLIR — sous-agent neuf (identifiant), empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de
chaque remarque. Fichiers à lui donner : le présent addendum ; le parent ; le rapport d'enquête ; le n° 339 ;
`prereg/R1-rejeu-config-v3.json` ; `prereg/R1-table-tokenisation-v1.json` ; `src/controle_ia/runs_nuit/rejeu_activations_v2.py`,
`resolution_tokenisation_v1.py` et `rejeu_activations_v1.py` ; `tests/test_runs_nuit_v2.py` ; les scripts v2 ; les sorties
d'essai citées. Puis vérification de concordance par un lecteur neuf de conv-audit avec leur analyse principale scellée.
