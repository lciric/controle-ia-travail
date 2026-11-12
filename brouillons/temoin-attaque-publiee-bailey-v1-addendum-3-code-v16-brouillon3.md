# Addendum 3 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — code v16 : message d'erreur d'une exécution morte avant tout tour ; nouvelle série après la seconde chute du pilote — brouillon 3

12 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. **Brouillon 3 : corrections K-1 à K-8 de la contre-lecture appliquées ; non
scellé tant que Lazar n'a pas tranché le § 7.** Brouillons archivés tels quels (R12) : brouillon 1
(`brouillons/temoin-attaque-publiee-bailey-v1-addendum-3-code-v14-brouillon1.md`,
`614dc5d7669ccc598186a13df11937448752e9cc0fdf9ceba3c924cc108dc78a`) ; brouillon 2
(`brouillons/temoin-attaque-publiee-bailey-v1-addendum-3-code-v16-brouillon2.md`, `328405b7…`, contre-lu). Le
préenregistrement et ses addenda 1 et 2 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est
un nœud. Cet addendum ne contient aucun résultat : aucune note de sonde ni de juge n'existe (zéro tour complet) et aucune
n'a été lue.

## 1. Pourquoi
Run du 12 novembre (conduite v6, code v13 au commit `4988f3f4`, instance 60370363) : mise en place (huit gardes) et
contrôle du juge tenus ; **pilote et reprise du pilote sortis en code 1 en ≈ 71 s, sans journal, configuration effective
« non décidée »** ; issue de la liste d'arrêt : « seconde chute du pilote : pas de run principal, pas de verdict ; nœud »
(`registres/passations/2026-11-12-1545-temoin-bailey-pilote-seconde-chute-noeud.md`, `21f0fc4d…`). Le message d'erreur
n'est pas sorti de l'instance (liste fermée, texte l. 316-319) : cause non établie. Décision de Lazar sur ce nœud :
« go (a) » (`registres/passations/2026-11-12-1720-decision-lazar-bailey-option-a-v14.md`, `df3833a9…`), contre (b)
« arrêter le témoin ».

## 2. Écarts décidés par Lazar sur le nœud de la seconde chute du pilote (« go (a) », `df3833a9…`), actés par cet addendum
1. **Liste « Ce qui sort de l'instance » (texte l. 316-319 ; lecture 12, liste v11 `c1747537…`, complétée par ce point ;
   aucune autre lecture ne change) : s'y ajoute un seul fichier**, `erreur-demarrage-v1.txt`.
   - **Condition** (toutes requises) : code de retour non nul ; garde de démarrage non décidée ; zéro tour complet ;
     sortie standard reçue égale à un début exact de la configuration attendue ; aucun des trois arrêts d'`executer`
     décidé par l'instance (garde de démarrage, dépense, échéance) ; journal des notes (là où l'écrit le journaliseur,
     `dossier_journal` de `config-journal-v3.json`) absent ou vide ; dossiers des sondes et des suffixes (écart 9) absents,
     ou ne contenant que des sous-dossiers et des fichiers vides (tout lien symbolique, tube ou erreur de lecture les fait
     tenir pour non vides). Un enfant tué par un autre processus (chien de garde, noyau à court de mémoire) avant d'avoir
     fini d'imprimer la configuration laisse le message, sous la même condition. Dans tous ces cas, `train_harmful.py`
     n'a commencé aucun tour : aucune note, aucun texte produit par le modèle sous attaque, aucun suffixe ni aucune sonde
     n'existe.
   - **Contenu** : les 60 dernières lignes de la sortie d'erreur de l'enfant ; valeurs remplacées sur place (nombre
     décimal isolé, ou à exposant, non collé à un nom, un chemin ou une version : `<nombre>` ; suite de plus de 12
     chiffres : `<chiffres>` ; `hf_` suivi d'au moins 30 caractères alphanumériques : `<jeton>` ; suite alphanumérique de
     32 caractères ou plus, sans `_` ni `-` : `<suite>`) ; ligne qui contient `tensor(` remplacée par une marque ; 300
     caractères par ligne après le filtre ; 20 000 octets au plus. Le filtre ne retire ni les entiers, ni les mots, ni les
     nombres à virgule ou suivis d'un point : c'est une défense en profondeur ; **la garantie vient de la condition**.
   - Le fichier est empreinté, transféré et scellé comme les autres ; il ne sert qu'au diagnostic borné de la liste
     d'arrêt (« nom de la garde, message d'erreur, durées, mémoire »). La reprise (`lanceur_v16 reprendre`, même chemin
     absolu de `--sortie` : `runs/temoin-bailey-v1-20261111/sortie-conduite-v8`) transfère et scelle le fichier s'il
     existe ; elle ne l'écrit jamais (`reconstituer_etat` ne l'écrit pas).
2. **Portée (R-3, D-6).** Le message ne sort pas pour une mort après l'impression complète de la configuration, ni quand
   la garde de démarrage tombe, ni quand l'instance arrête l'enfant (dépense, échéance), même avant toute sortie. Dans ces
   cas, le diagnostic de la liste d'arrêt (texte l. 370) se borne au nom de la garde, aux durées et à la mémoire, sans
   message d'erreur. L'étendre serait un nouvel élargissement de la liste fermée : nœud, décision de Lazar.
3. **Écart à la lettre (R-4).** Le message peut contenir la ligne de Hydra des surcharges (graine, nombre de tours,
   chemins) et des morceaux de la configuration ; c'est un écart au texte l. 316-317 (« la configuration … n'en sort pas,
   seule son empreinte »), acté ici. Il ne contient aucune note : aucune n'existe dans ce cas.
4. **Nouvelle série (écart à R3 et à la ligne « Seconde chute du pilote … nœud », texte l. 69-71, 245, 366).** Décision de
   Lazar sur ce nœud : « go (a) », dont l'option comprenait « relouer une A100 », contre (b) « arrêter le témoin »
   (`df3833a9…`). La cause de la seconde chute n'est pas nommée : ce n'est pas la relance de la liste d'arrêt, c'est un
   écart. Ce qui le rend compatible avec l'objet de R3 : les exécutions du 12 novembre ont fini avec zéro tour complet ;
   aucune note de sonde ni de juge n'existe ; rien n'a été lu ; la reprise ne peut donc pas viser un signe. Une seule
   nouvelle série : pilote, au plus une reprise, puis la règle et le run principal selon le texte, inchangés. Mêmes
   graines (pilote 1394228342, run principal 1865327867 ; aucune sortie n'a été produite sous ces graines). B inchangé :
   75 USD, fixé à la création de la première instance du poste (60280913, 12 novembre, 00:03:20Z). D continue de cumuler
   depuis cette instance : 1,976 USD après quatre instances détruites (liste `ANTERIEURES` de
   `runs/temoin-bailey-v1-20261111/lancer-conduite-v8.py`, `a02f7b5b…`) ; l'essai à blanc, s'il a lieu, y entre. Les
   exécutions du 12 novembre sont rapportées comme interrompues. Une nouvelle seconde chute du pilote : pas de run
   principal, pas de verdict ; nœud ; aucune autre série sans nouvelle décision de Lazar et nouvel addendum.
5. **Paramètres de lancement** (hors du texte, déclarés ; source : note `21f0fc4d…`) : disque demandé 110 Go
   (`lancer-conduite-v8.py`, ligne `DISQUE_GO` ; valeur par défaut du code : 200 Go ; le devis chiffre 1 à 2 Go de sondes
   et suffixes) ; offres filtrées à 128,9 Go de mémoire allouée au moins (`poste-hetzner-v8.sh`) ; la garde de mémoire
   vive du texte (128 × 10⁹ octets, à la mise en place) est inchangée et a passé le 12 novembre ; pilotage par un poste
   Hetzner autonome (« go c » de Lazar, `registres/passations/2026-11-12-1250-poste-hetzner-temoin-bailey-plan.md`,
   `4f40c079…`). Le disque de 110 Go reste une des causes possibles de la seconde chute ; il est gardé ; si c'est la
   cause, le message le dira (« No space left on device »).

## 3. Commit et code
**Commit du code : `91238a735a2127a0879fb4533a6cde5baccb4efa`.** Seuls changent, par rapport à l'addendum 2 :

| Rôle | Module | SHA-256 |
|---|---|---|
| Lanceur local | `lanceur_v16.py` | `03df34aabc5146d4136d0ffe61a0df450362cb1c2a50c2030cd612f7cc57a6a0` |
| Lanceur côté instance | `instance_v15.py` | `39725c4c190f73262861ea1fee6f8e4360cca3712c271349b1b44eeff2fd100f` |

Les autres modules sont ceux de l'addendum 2, inchangés à ce commit (`lecture_v8`, `execution_v3`, `journaliseur_v3`,
`conventions_v3`, `analyse_v3`). Manifeste neuf (R12) : `runs/temoin-bailey-v1-20261111/manifeste-local-v4.json`
(`e15d456f…`), écrit par `lanceur_v16.manifeste_depuis_versions_figees` ; sa seule différence avec le manifeste v3
(`69143b99…`) est `commit_code` (l'archive envoyée sur l'instance est tirée de ce commit).

**Défaut corrigé (règle R4).** Dans `executer`, une liste locale nommée `signal` masquait le module `signal` depuis la
v7 : les trois arrêts internes d'une exécution (garde de démarrage tombée, dépense B − 2, échéance) levaient
`UnboundLocalError` et laissaient l'enfant vivre. Ce défaut est dans le code scellé par l'addendum 1 (`instance_v8`) et par
l'addendum 2 (`instance_v12`, commit `4988f3f4`) : pendant les exécutions du 12 novembre, ces trois arrêts n'étaient pas
opérants ; seuls le chien de garde et les veilleurs bornaient la dépense. Sans effet observé : l'enfant est mort de
lui-même. Les épreuves R5 de ces addenda ne couvraient pas ce chemin. Les relectures du code v7 à v12 ne l'ont pas vu ; la
relecture v13 ne relisait pas `instance_v12`. Trouvé par l'essai v14 ; corrigé (`signaux`) ; un essai vérifie qu'aucune
fonction de l'instance ne lie un nom local `signal`. Rapporté à Lazar avec cet addendum (R4).

**Essais (R5)** : `tests/test_temoin_bailey_condition6_v16.py` (`f5b71cad…`) : 161 passés (les 139 essais v13 rejoués,
les essais du message d'erreur v14 et v15, ceux de la relecture différentielle : filtre, enfant muet arrêté par la
dépense et par l'échéance, vacuité, lecture d'un dossier d'étape qui porte le fichier) ; `tests/test_temoin_bailey_
analyse_v3.py` (`8cca01f1…`, inchangé) : 36 passés. L'essai instable `test_v13_P2_…` est corrigé dans l'essai (attente
bornée ; cause établie : bénigne en production).

**Pièces de lancement** : `runs/temoin-bailey-v1-20261111/lancer-conduite-v8.py` (`a02f7b5b…`) ; poste
`poste-hetzner-v8.sh` et constructeur `construire-donnees-demarrage-v8.py` (empreintes à leurs compagnons ; v8 = v7 + la
garde K-6 (c) : le code `src/` de la tête de branche doit être identique à celui du commit `91238a73`, sinon rien ne
tourne).

## 4. Ce qui ne change pas
Hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines, B, critères de lecture gelés, liste
d'arrêt (hors les écarts du § 2), lectures 1 à 38 actées (la lecture 12 complétée par le § 2.1).

## 5. Risques déclarés
Ceux de l'addendum 2 (§ 4), tous gardés. En plus :
- (a) si la sortie standard porte, avant la mort, autre chose qu'un début de la configuration (impression d'une
  bibliothèque à l'import), le message ne sort pas ; on ne sait pas si c'était le cas le 12 novembre ;
- (b) un enfant bloqué avant l'impression n'a pas de délai (§ 7, point 2) ;
- (c) le poste exécute le lanceur local depuis la tête de la branche ; la garde du poste v8 exige que `src/` y soit
  identique au commit `91238a73`.

## 6. Conditions de lancement (état au scellement)
1 : rempli. 2 : `GO-2026-11-10-10` amendé par `GO-2026-11-11-01`, comme à l'addendum 2 ; échéance (2026-11-30) à
revérifier à la création contre création + (B − 2)/c heures, c relevé. 3, 4 : comme à l'addendum 2, inchangées. 5 : comme
à l'addendum 2 (addendum 2 de la règle du bras, `73c8de01…`) : la nouvelle série ne change pas ce que le verdict vaut pour
le témoin. 6 : remplie par cet addendum, une fois scellé **et déposé chez le tiers** ; il remplace, pour la condition 6,
le code de l'addendum 2. 7 : le mot direct de Lazar du 11 novembre portait sur la première série ; un mot direct pour
cette série est requis (§ 7, point 3). 8 : pilotage par le poste Hetzner autonome (« go c », `4f40c079…`) ; `DEPOT_URL`
du dépôt de travail. Aucune instance avant le scellement, le dépôt chez le tiers et le mot de la condition 7.

## 7. Décisions de Lazar (nœuds, sans défaut) — à trancher avant le scellement
1. **Essai à blanc.** Enjeu : sans essai à blanc, une nouvelle double chute consomme la seule série permise (nœud, avec le
   message). Avec un essai à blanc sur petite carte : la garde de mémoire vive (128 × 10⁹ octets) tomberait sur la
   plupart des hôtes ; l'adapter serait un écart et du code neuf. Options : (a) remplacer l'essai à blanc par la première
   exécution v16 sur A100 (≈ 0,44 USD par tentative ratée) ; (b) écrire et relire un essai à blanc hors conduite.
   Recommandation : (a), confiance moyenne.
2. **Délai de la garde de démarrage (R-10).** Une garde de démarrage jamais décidée n'a pas de délai : un enfant bloqué
   avant l'impression n'est arrêté que par la dépense B − 2, l'échéance ou le chien de garde. Options : (a) garder ainsi,
   avec une alerte de la session à Lazar si le pilote n'a pas fini 4 heures après son lancement ; (a′) alerte si la
   configuration effective n'est pas décidée 30 minutes après le lancement du pilote, quand le journal poussé par le
   poste le rend visible, sinon 4 heures ; (b) délai borné dans une version suivante, nouvel addendum. L'alerte ne
   déclenche aucun arrêt par la session sans mot de Lazar, sauf les arrêts de la liste d'arrêt (R10, par identifiant).
   Recommandation : (a′), confiance moyenne.
3. **Mot de lancement (condition 7).** Options : (a) mot exprès de Lazar pour cette série, après le scellement et le dépôt
   de cet addendum ; (b) tenir le « go (a) » pour ce mot. Recommandation : (a), confiance haute : le « go (a) » prévoyait
   un essai à blanc avant de relouer, et le point 1 le change.

## Contre-lecture
Rapport (R2) : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-3-code-v16-bailey-v1.md`
(`919e67d0…`), contre-lecteur neuf. Verdict sur le brouillon 2 : « scellable après corrections » (K-2 bloquant,
corrigeable par le texte ; K-1, K-3, K-4 à corriger ; K-5 à K-8 à préciser) ; code v16 conforme. Corrections reprises du
rapport, presque mot pour mot : K-1 (en-tête) ; K-2 (§ 2, titre et point 4) ; K-3 (§ 3) ; K-4 (§ 6) ; K-5 (§ 2.1) ; K-6
(§ 5 et poste v8) ; K-7 (§ 2.1, 2.5, 3, 4) ; K-8 (§ 7).
