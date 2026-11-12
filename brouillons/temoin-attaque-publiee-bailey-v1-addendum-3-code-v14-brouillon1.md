# Addendum 3 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — code v14 : message d'erreur d'une exécution morte avant tout tour ; nouvelle série après la seconde chute du pilote — brouillon 1

12 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. **Brouillon : non contre-lu (R2), non scellé.** Le préenregistrement et ses
addenda 1 et 2 restent tels quels (R12) ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. Cet
addendum ne contient aucun résultat : aucune note de sonde ni de juge n'existe (zéro tour complet), aucune n'a été lue.

## 1. Pourquoi
Run du 12 novembre (conduite v6, code v13 au commit `4988f3f4`, instance 60370363) : mise en place (huit gardes) et
contrôle du juge tenus ; **pilote et reprise du pilote sortis en code 1 en ≈ 71 s, sans journal, configuration effective
« non décidée »** ; issue de la liste d'arrêt : « seconde chute du pilote : pas de run principal, pas de verdict ;
nœud » (note `registres/passations/2026-11-12-1545-temoin-bailey-pilote-seconde-chute-noeud.md`, `21f0fc4d…`). Le
message d'erreur n'est pas sorti de l'instance (liste fermée, texte l. 316-319) : cause non établie. Décision de Lazar
sur ce nœud : « go (a) » (`registres/passations/2026-11-12-1720-decision-lazar-bailey-option-a-v14.md`, `df3833a9…`).

## 2. Écarts actés par cet addendum
1. **Liste « Ce qui sort de l'instance » (texte l. 316-319 ; lecture 12) : s'y ajoute un seul fichier**,
   `erreur-demarrage-v1.txt`, écrit par l'instance **seulement** si l'enfant sort avec un code non nul, sans garde de
   démarrage décidée (la configuration effective n'a jamais été imprimée, donc `train_harmful.py` n'a commencé aucun
   tour) et avec zéro tour complet. Contenu : les 60 dernières lignes de la sortie d'erreur de l'enfant, chacune tronquée
   à 300 caractères ; toute ligne qui contient un nombre décimal, `tensor(` ou une suite de plus de 12 chiffres est
   remplacée par « [ligne retirée : valeurs numériques] » ; 20 000 octets au plus. Dans ce cas, aucune note, aucun texte
   produit par le modèle sous attaque, aucun suffixe ni aucune sonde n'existe encore. Le fichier est empreinté,
   transféré et scellé comme les autres ; il ne sert qu'au diagnostic borné de la liste d'arrêt (« nom de la garde,
   message d'erreur, durées, mémoire »).
2. **Nouvelle série.** La seconde chute du pilote est due à un défaut d'infrastructure survenu avant tout tour et avant
   toute donnée. Une **nouvelle série** est permise, une seule : pilote, au plus une reprise, puis la règle et le run
   principal selon le texte, inchangés. Mêmes graines (pilote 1394228342, run principal 1865327867), même B (75 USD),
   même D (cumulé depuis la première instance du poste : 1,976 USD au 12 novembre, 15:33Z). Les exécutions de la série
   du 12 novembre sont rapportées comme interrompues ; elles n'ont produit aucune note. Une nouvelle seconde chute du
   pilote : pas de run principal, pas de verdict ; nœud.
3. **Paramètres de lancement** (hors du texte, déclarés) : disque demandé 110 Go (valeur par défaut du code : 200 Go ;
   le devis chiffre 1 à 2 Go de sondes et suffixes) ; offres filtrées à 128,9 Go de mémoire allouée au moins ; la garde
   de mémoire vive du texte (128 × 10⁹ octets, à la mise en place) est inchangée et a passé le 12 novembre.

## 3. Commit et code
**Commit du code : `4821ad7ef562748be092ec00ae6665795ae1a886`.** Seuls changent :

| Rôle | Module | SHA-256 |
|---|---|---|
| Lanceur local | `lanceur_v14.py` | `02e9816a64160cea5a38f2c4cb10612d94f9ee6a8712c6da59684528f32fc101` |
| Lanceur côté instance | `instance_v13.py` | `62686ac11dbba382b97cd16c94f5280570f783d9329f8dcb3a7fc78776d20032` |

Manifeste neuf (R12) : `runs/temoin-bailey-v1-20261111/manifeste-local-v4.json`, écrit par
`lanceur_v14.manifeste_depuis_versions_figees` avec ce `commit_code` (l'archive envoyée sur l'instance est tirée de ce
commit ; le manifeste v3 citait `4988f3f4`, qui ne contient pas `instance_v13`) ; versions figées et graines inchangées.
Les autres modules sont ceux de l'addendum 2, inchangés (`lecture_v8`, `execution_v3`, `journaliseur_v3`,
`conventions_v3`, `analyse_v3`). `instance_v13` corrige en outre un **défaut de la v12** trouvé par l'essai v14 : dans
`executer`, une liste locale nommée `signal` masquait le module `signal` ; tout arrêt de l'enfant par son PID (garde de
démarrage tombée, dépense, échéance) levait `UnboundLocalError` au lieu d'arrêter. Renommée `signaux`.

**Essais (R5)** : `tests/test_temoin_bailey_condition6_v14.py` (`6f4809a5…`) : les 139 essais v13 rejoués sur les modules
v14, plus 8 essais du message d'erreur (cas sain : mort à l'import ; artefacts : configuration imprimée puis mort,
configuration fausse, sortie sans erreur ; filtre ; écriture qui ne lève pas ; transfert du seul nom nouveau ; modules et
archive). Réserve : l'essai `test_v13_P2_processus_reels_veilleur_arrete_autre_pid_jamais_signale` est instable, déjà
dans le fichier v13 sur un code inchangé (2 échecs sur 5 en isolé ; 5 sur 5 en v14).

**Contre-lecture du code (R2)** : `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v14-bailey-v1.md`
(à venir).

## 4. Ce qui ne change pas
Hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines, B, critères de lecture gelés, liste
d'arrêt (hors l'écart 2 ci-dessus), lectures 1 à 38 actées, risques déclarés de l'addendum 2.

## 5. Point ouvert pour Lazar (à trancher avant le scellement)
Le « go (a) » prévoyait un **essai à blanc sur une petite carte** avant de relouer une A100. La conduite exige à la mise
en place 128 × 10⁹ octets de mémoire vive (garde du texte) : les hôtes des petites cartes en ont rarement autant, et un
essai à blanc hors conduite serait un code de plus à écrire et relire. La première exécution v14 sur A100 joue le même
rôle : si le pilote meurt encore, le message sort ; coût observé d'une telle tentative : ≈ 0,44 USD.
Proposition : remplacer l'essai à blanc par la première exécution v14 sur A100.
