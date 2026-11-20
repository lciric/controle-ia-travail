# Vérification des corrections C1 à C3 du code du palier 0b, version 3 — v1

Pièce de travail (classe C). Contre-lecteur, modèle S, le même que pour la contre-lecture du code v2 (`3778fb39…`). Rapport du développeur v3 vérifié par son compagnon (`5e3fa3e8…`, OK). Code v3 copié dans mon dossier (`v3/src`, `v3/tests`, `v3/outils-dev`) ; rien écrit dans le dépôt ; aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille ; aucun refus d'outil.

## Verdict

**Conforme.** C1 à C3 sont appliquées ; D4 et D7 sont traitées sans changer de résultat ; D5, D6, D8, D9 sont intactes ; 71 essais sur 71, fichier par fichier et en suite entière ; 50 défauts sur 50 vus ; 140 empreintes de sorties identiques entre v2 et v3.

## 1. C1, C2, C3 appliquées comme demandées

- **C1** (`tests/..._zz_aucune_graine_decisive.py`) : `GR.REFUS and` n'est plus exigé avant l'essai ; l'essai provoque lui-même une demande par couche décisive, refusée et consignée, sans entrée nouvelle au journal ni aux étiquettes. Chez moi : **passe seul** (0,09 s) et en suite entière. Le sens est renforcé, pas affaibli.
- **C2** (`registre.verifier_vue_etrangere_4b`, appelée dans `mecanique.jouer_source` avant de servir chaque vue, et avant le retrait des champs du repli). Les quatre cas d'arrêt, lus : (1) copie déposée dont la source est la source propre ; (2) une entrée servie dont la provenance est la source propre ; (3) une entrée qui n'est pas de (source étrangère, bras 2, origine « continuation ») ; (4) empreinte canonique de la vue servie différente de l'empreinte déposée (prise au moment où le bras 2 de la source étrangère a reçu la vue). **Le registre propre du bras 2 servi au 4b est bien arrêté** : par (1) si la copie porte son vrai numéro de source, par (2) si l'étiquette est falsifiée mais les entrées sont les siennes, par (4) si le contenu est altéré ; le cas de bout en bout (`jouer_jeu_diagnostic` déposant `premieres[k]`) est joué par le banc (« registre-propre-au-bras-4b », vu en 38,6 s) et par l'essai de la garde 27 (arrêt dès la première génération). Limite, sans gravité : la première génération sert une vue vide, que (2), (3) et (4) laissent passer ; seul (1) la distingue, et il suffit puisqu'il porte sur le numéro de source déposé. Une falsification qui recalculerait à la fois l'étiquette de source, les provenances et l'empreinte échappe au contrôle : c'est hors du modèle de menace d'une garde interne.
- **C3** (`statistique.Mondes(..., passage_requis)`) : `simuler` passe `"p_passage_vraie" in strates_requises(prop, dose, bras)`. Les tirages `rng.random((S, d))` restent faits dans tous les cas : le flux de graines du monde est inchangé. Strate non requise : passages à None ; les employer arrête (`jouer_bras`, message « non tirés »). Cohérent avec `strates_requises` (lecteur aux bras 3 ou 4a, dose non nulle). Essai neuf passé.

## 2. D4 à D9

- **D4** traitée (`analyse.table_des_criteres` arrête si les gardes ne sont pas exactement 1 à 27, ou si une autre que la 17 vaut None). Une table complète rend la même table qu'en v2 ; une table partielle ne s'écrit plus : aucun résultat changé. Note : le texte (C6) a toujours voulu « toutes tenues » ; cet arrêt est plus strict qu'avant sur une entrée incomplète seulement.
- **D7** traitée (`mondes.generer_jeu_avec_etrangeres` : compteurs cumulés par source, portés par la suite). Aucun tirage n'en dépend : le jeu du § 5 a les mêmes empreintes. Vérifié : l'objet `Compteurs` est « vrai » en Python, donc `compteurs or Compteurs()` de `generer_source` ne remplace pas celui qu'on passe.
- **D5, D6, D8, D9** laissées à l'erratum, avec les raisons du développeur : D5 (taille du cache, se mesure à l'essai de forme), D6 (lier l'autorisation à l'empreinte du texte qui sera scellé), D8 (règle de lecture), D9 (stratifier change des résultats). Aucune n'a été touchée ; les fichiers concernés (`rangs_signes`, `graines`, `etalonnage`, `audit`) sont ceux de la v2 d'après la liste des fichiers changés.

## 3. Essais, chez moi (`PYTHONPATH=src`, copie de l'organisme du dépôt)

Chaque fichier seul : `zz` 1 passé ; `gardes` 17 ; `outils` 15 ; `statistique` 10 ; `etapes` 5 ; `organisme` 5 ; `mecanique` **9** ; `mondes` 9. Total 71, 0 échoué. **Suite entière en un processus : 71 passés, 0 échoué (724 s).** Même compte que le développeur.

## 4. Banc des défauts `mutations_v2.py`

Rejoué chez moi, en entier, un processus, témoins joués d'abord. Résultat : **témoins au vert ; 50 défauts appliqués, 50 vus**, dont les 9 neufs (refus-non-consigne 0,3 s, registre-propre-au-bras-4b 38,6 s, copie-4b-de-la-source-propre-acceptee 42,3 s, entree-propre-au-4b-acceptee 42,0 s, empreinte-4b-non-verifiee 41,4 s, bras-4b-sans-controle 42,0 s, passage-exige-sans-besoin, table-des-gardes-incomplete, compteurs-du-jeu-perdus) et les 41 de la v1.

## 5. « Aucun résultat changé »

Outil à moi (`outils-cl/empreintes_v2_v3.py`, graines « essai », hors des essais du développeur) : empreintes SHA-256 de M1, D, I et des lois fausses tenues, couche statistique, 400 sources, bras 1 à 4b (2 et 3 à dose nulle), pour sept proposeurs et doses (lecteur pour l'héritage à 0,5 et 0,25, lecteur pour la tenue, sourd qui paie, copieur, suiveur à la lettre, généraliste à dose nulle) ; couche mécanique : le jeu à deux sources de la garde 27, registres (octets), mesures, entrées servies et reliquats des bras 1 à 3 et 4a, 4b. **140 lignes sur 140 identiques entre le code v2 et le code v3.** Les 57 empreintes du développeur ne sont pas rejouées une à une (son outil n'est pas au dossier) ; la mienne couvre les mêmes familles.

## 6. Défauts vus

Aucun nouveau. Remarque : le contrôle C2 ne regarde pas la longueur de la liste des vues déposée au-delà du test de complétude (4 vues) de `copie_scellee_4b` ; suffisant.

*Contre-lecteur, modèle S.*
