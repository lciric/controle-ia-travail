# Notes de rédaction — complément de validation du rejeu à graine — v1

- Auteur : sous-agent de rédaction (Opus 5.5). Rédigé le 2026-11-02 entre 18:54 et 19:10 UTC (`date -u`).
- Fichiers écrits (neufs) dans ce dossier : `R1-addendum-relance-v2-complement-validation-v1-brouillon1.md`,
  `R1-graine-config-complement-v1.json`, ces notes. Aucun fichier existant modifié, aucun `.sha256`, aucun commit, aucun
  réseau, rien lu sous `donnees/`, rien lu de l'analyse de R1-R2.
- Lu : addendum v2 (en entier, `9d17d640…`, empreinte refaite et égale), configuration v1 (`0f300925…`, canonique
  `f91716bf…` recalculée et égale), `resolution_graine_v1.py` (`cdc22b5a…`, lignes 1-190, 655-907, 1013-1062,
  1060-1239, 1250-1269, 1390-1836), `resolution_graine_lot_v1.py` (`5a9982b2…`, par recherche, lignes 830-846, 966-978,
  1180-1205), `r1_resolution_graine_instance_v1.sh` (`da07025f…`, en entier), l'amorce au commit `c2a8b6e1` (en-tête et
  corps, par `git show`), `harnais/validation_reelle.py` et `manifeste.py` au commit `c2a8b6e1` (citations et JSON
  canonique, par `git show`), le verdict (`64fab1a5…`, en entier), le journal de l'instance du 2 novembre (lignes hors
  progression : heures de mise en place, d'essais et des étapes), la ligne 72 de `registres/go.md`.

## Ce que j'ai vérifié dans le code (commit `c2a8b6e1`)

1. Compte exact de la validation : `exiger_compte_validation` l. 1156-1160, appelée l. 1531-1532 sur
   `episodes_de_l_etape` (l. 1396-1401 : tous les épisodes à identifiants connus, ordre du classement). Ne rejouer que
   93 épisodes exigerait du code neuf.
2. Garde R3 du cœur : `executions_anterieures` l. 1192-1211 filtre sur la commande **et** l'empreinte canonique de la
   configuration (l. 1204) **et** le même arbre gelé (l. 1209) ; une configuration aux durées changées
   (`8d18c7ee…` ≠ `f91716bf…`) la satisfait sans changer le code. Le texte neuf n'entre pas dans cette garde ; il entre
   dans `exiger_config_citee` (l. 1163-1166), l'entropie (l. 1723-1726) et `exiger_code_cite`
   (`validation_reelle.py` l. 214-228 : arbre gelé au lancement égal à celui du commit cité, regex
   ``Commit du code d'analyse : `<40 hex>` ``). Garde R3 du lot : l. 968-978 (commande et configuration) : satisfaite
   de même.
3. Gardes de durée : `exiger_reglages_execution` l. 1103-1105 (0 < `duree_max_episode_s` ≤ `duree_max_s`) ;
   `exiger_config` l. 1084-1085 ; lot l. 845-846 ; script l. 165-171 : 7 200 ≤ 86 400 passe partout.
4. Somme des délais du script (l. 172, 178-187) avec les quatre durées : 40 + 2 × 1 450 + 5 + 1 450 + 15 + 5 =
   **4 415 min** ; `PLAFOND_MIN` de l'amorce doit valoir au moins cela (sinon arrêt avant l'installation, code 2). Si
   l'on garde les budgets du lot de la v2 (900 / 3 600), la somme tombe à 3 035 min.
5. Garde R12 « table v3 déjà présente » : script l. 150-151 (le chemin `TABLE_V3`, par défaut
   `prereg/R1-table-tokenisation-v3.json`). L'étape validation du module n'écrit **aucune** table (sorties
   l. 1544-1545, 1628-1640, 1699 ; table seulement par `--etape table`, l. 1812-1822). Mais le script **n'a pas de mode
   « validation seule »** : il enchaîne toujours validation → résolution → cibles → (lot) → table (l. 457-499). Code
   inchangé, il faut donc passer `TABLE_V3` vers un nom absent (choisi :
   `prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json` ; `prereg/` existe, donc l'écriture l. 1785-1795 ne
   manque pas de dossier parent), et la résolution des 7 est rejouée (≈ 13 min) : le brouillon en fait une épreuve de
   répétabilité, et la table produite un sous-produit jamais cité comme référence.
6. Citations exigées du texte, simulées sur le brouillon avec les commandes mêmes du script et des modules :
   « Tests attendus » 1 fois → `71` ; « Chemin de la configuration … » 1 fois → `prereg/R1-graine-config-complement-v1.json` ;
   les deux libellés de l'empreinte canonique 1 fois chacun, égaux à `8d18c7ee…` ; commit `c2a8b6e1297a…` trouvé par la
   regex ; entropie trouvée. Toute retouche du brouillon doit garder ces six lignes uniques (le script compte les
   occurrences).
7. Arbre gelé : `git diff --quiet 0e2a8871 c2a8b6e1 -- <chemins gelés>` rend 0 (dépôt local, sans `fetch`) : citer
   `c2a8b6e1` ou `0e2a8871` revient au même pour `exiger_code_cite`.
8. Libellés du verdict : comptes par épisode de l'essai direct seul (l. 716-717, 726-727 ; jamais mis à jour l. 761-765
   ni 774-781 ; compteur neuf par rejeu l. 750) ; échéance d'épisode = la plus proche des deux (l. 662-667) ; horloge
   d'étape partie l. 1734, avant le modèle (l. 1523) ; contrôle croisé contre la table v2 seulement (l. 1254-1264,
   l. 1613-1615).
9. Mêmes épisodes aux mêmes rangs : la liste dépend seulement des pièces scellées et de la table v2 (l. 1396-1401) ;
   les rangs 0 à 56 sont les 57 tentés du 2 novembre, rejoués d'abord.
10. Les essais lancés par le script (liste `CIBLES`) ne lisent ni la configuration ni la table v3 sur disque (recherche
    dans les quatre fichiers d'essais au commit `c2a8b6e1` : constantes de nom et `tmp_path` seulement) : 71 attendus
    restent valables.

## Configuration : différences clé par clé avec `R1-graine-config-v1.json`

- `duree_max_s` : 2 400 → 86 400 (une clé changée suffit à la garde R3 ; celle-ci pour la demande de Lazar)
- `duree_max_episode_s` : 600 → 7 200
- `duree_max_lot_s` : 3 600 → 86 400 (non exigé ; cohérence)
- `duree_max_episode_lot_s` : 900 → 7 200 (non exigé ; cohérence)
- les 38 autres clés : identiques (vérifié par comparaison des objets JSON). 42 clés. Format du fichier identique à la
  v1 (`indent=1`, clés triées ; la v1 se relit octet pour octet sous ce format). Empreinte canonique
  `8d18c7ee9ce7bc6f2b176d2e5c67422708c8fc6c99f5b09e40b25d1e166663e8`. Toute modification de la configuration change
  cette empreinte : la recopier alors dans les deux lignes du texte.

## Ce qui reste à confirmer par la session qui lance (session-depot)

1. **Le script ne sait pas lancer la validation seule** : accepter la chaîne entière (choix du brouillon), ou décider
   autrement (code neuf : hors de la consigne « code inchangé »).
2. Sur le `main` réel (mon `origin/main` local date de 09:01 UTC) : arbre gelé du commit de scellement égal à celui de
   `c2a8b6e1` ; table du sous-produit absente ; aucun manifeste illisible dans `runs/` (garde R3 l. 1199-1203) ; table v3
   `ead8a668…` et sorties du 2 novembre versées ou non sur `main` (sans effet sur les gardes avec `TABLE_V3` changé).
3. La commande de création exacte du 2 novembre (offre, image, disque, forme de l'amorce en mode « args ») : je ne l'ai
   pas trouvée ; le brouillon dit « reprise mot pour mot » plus `BRANCHE`, `PREREG`, `TABLE_V3`, `PLAFOND_MIN`. Vérifier
   que ces variables passées par `--env` atteignent bien le script (l'amorce les hérite par `env`, sans les nommer ; son
   en-tête les décrit comme « pour l'essai local » : écart déclaré C6).
4. **Coût** : mon estimation (≈ 3 à 14 USD, central ≈ 6 USD) est au-dessus de « ≈ 3 USD » (demande) et de « ≈ 4 USD »
   (ligne du GO). Le surcoût des 54 est ≈ 13 min (≈ 0,3 USD), non ≈ 1 h ; l'incertitude vient des épisodes difficiles
   désormais menés jusqu'à 136 combinaisons. La garde de dépense (alerte à 10 USD, arrêt par PID à 14 USD sans
   extension) est à confirmer, avec le moyen d'atteindre le PID sur l'instance, et les dépenses déjà imputées à
   `GO-2026-11-02-26`.
5. **Écart dans le registre** : la ligne 72 de `registres/go.md` dit « 87 épisodes non tentés » ; le verdict scellé en
   compte 90 non tentés et 3 coupés (93 manqués). À corriger par la session (je n'ai rien modifié).
6. **Risque de résultat non concluant par une borne de travail** : `combinaisons_max` = 136 n'est pas un budget de temps,
   mais la frontière écrite en permet 272 ; P-C2 donne ≈ 0,7 à « méthode non transposée » (une manquée suffit). Lazar a
   dit (ligne du GO) ne vouloir « pas de résultats non concluants par défaut de conception, de plafond ». Le brouillon
   garde 136 (consigne « seules les durées changent ») ; passer à 272 changerait deux clés (`combinaisons_max` et
   `combinaisons_max_validation`, égales exigées l. 1108-1110) et le coût (jusqu'à ≈ 2,5 h par épisode difficile au pire
   taux observé, au-delà de la garde de 7 200 s). À trancher avant le scellement.
7. Garde de 7 200 s par épisode : marge de 1,6 fois sur le pire taux observé (33 s par combinaison × 136 ≈ 75 min).
   Suffisante au taux observé, non prouvée au-delà.
8. Concordance de conv-audit : annoncée par la ligne du GO ; le brouillon l'exige avant le lancement.
9. Essai local des gardes (`ARRET_AVANT_CALCUL=1`) : il pousse la branche (l. 190) ; ne le faire que contre un dépôt nu
   local ou sous une autre branche.

## Dix lignes pour le contre-lecteur

1. Vérifier que `lire_validation` (l. 854-886) et `declarer` sont bien inchangés et que la règle citée à « Seuil » les
   recopie exactement.
2. Vérifier la différence de configuration (quatre clés) et recalculer l'empreinte canonique `8d18c7ee…`.
3. Vérifier que la garde R3 du cœur (l. 1192-1225) et du lot (l. 968-978) passe avec une autre empreinte de
   configuration et rien d'autre.
4. Vérifier la somme des délais (4 415 min) contre le script (l. 172-187) et l'amorce (`PLAFOND_MIN`).
5. Vérifier que le script enchaîne toujours la résolution et la table, et que `TABLE_V3` vers un nom absent est le seul
   moyen, code inchangé, de passer la garde R12 si la table v3 est sur `main`.
6. Juger la lecture de la résolution rejouée et de la table du sous-produit « en répétabilité seulement » : est-elle
   gelée sans échappatoire (que lit-on si elles diffèrent) ?
7. Juger les prédictions P-C1 à P-C5 : sont-elles chiffrées, signées, et honnêtes au regard des 57 épisodes du
   2 novembre (en particulier P-C2 ≈ 0,3 pour « graines validées ») ?
8. Juger la ligne « méthode non transposée, cause méthode » : n'exige-t-elle rien de plus que la v2 (aucun nœud) et
   est-ce acceptable avec la consigne de Lazar sur les résultats non concluants ?
9. Juger la garde de dépense (10 USD, 14 USD, TERM par PID puis arrêt par identifiant) contre « aucun budget de temps qui
   coupe » et contre le plafond de 15 USD du GO.
10. Vérifier les corrections de libellé (contrôle croisé, comptes par épisode, cause « budget de l'épisode », horloge)
    contre les lignes de code citées et contre le verdict (réserves 3 et 6, § 6 point 2).

## À retenir (pour la mémoire de la session, pas pour l'utilisateur)

- Mesures du 2 novembre utiles aux devis : mise en place 33 min (dont essais 25 min 47 s, contre 12 à 13 min annoncés
  par la v2) ; résolution des 7 en 13 min 24 s ; source : journal de l'instance
  (`traces/r1-graine-20261102-181212-iXsM/journal.txt` de la copie de réception).
