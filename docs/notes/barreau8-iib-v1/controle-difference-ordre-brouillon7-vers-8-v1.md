# Contrôle de la différence entre les brouillons 7 et 8 de l'ordre du saboteur à budget (barreau 8) — v1

**Verdict : conforme.** Aucun couple obligatoire. Un point facultatif est signalé au § 5.

- Contrôleur : agent neuf (Sonnet 5.5), n'ayant ni écrit ni lu ni la conception, ni la consigne privée, ni les brouillons avant ce contrôle. Exclu de tout rôle côté sondes du barreau 8 pour avoir lu l'ordre.
- Lu : les cinq pièces du mandat, les lignes `R-3520` à `R-3524` du registre des décisions, les lignes `R-3310`, `R-3312`, `R-3485`, `R-3497`, `R-3509`, `R-3518` (début de ligne, pour les sources du § 8 ; voir « Lectures hors mandat »).

## 1. Empreintes (fichier par fichier)

| fichier | empreinte | attendue |
|---|---|---|
| ordre-exploratoire-ii-b-v1-brouillon7.md | `1ed0e736ed15f24e66a918815820ea73452a341c97004f6b21113eca22dd9766` | `1ed0e736…` : conforme |
| ordre-exploratoire-ii-b-v1-brouillon8.md | `eb83e9444df3bdfa822ef3bf76efe4039b450a7a8458fe4c91ba20f73d4eb76e` | `eb83e944…` : conforme |
| appliquer-brouillon8-ii-b-v1.py | `1384074fd891f5a7dbe79083238374d6de12cb68d54e300e8e8af2bd0a9ff1ed` | `1384074f…` : conforme |
| differences-brouillon7-vers-8-v1.md | `f25707217b887ce104c816446a93b6e2b7173c07d21f33ece33bc24808b208cc` | `f2570721…` : conforme |
| sortie-compter-marqueurs-ii-b-v3.txt | `2c0ef9a7720567e3af6e4cb71b12e4f48da82ea281dd5dcb9caf871372f5190c` | `2c0ef9a7…` : conforme |

Les notes citées par le brouillon 8 : `chemin-critique-saboteurs-discrets-entretien-v1.md` = `398215789b8a…` et `verification-ordre-et-devis-iib-brouillon6-v1.md` = `bd7941ecec09…`, empreintes recalculées, identiques à celles écrites dans l'ordre (contenu de la première non ouvert).

## 2. Rejeu du script

Copie du brouillon 7, du script, du programme de compte et du registre des décisions dans un dossier temporaire du contrôleur (`.../scratchpad/rejeu/`, même arborescence), script lancé là (`python3 -I -B`), sans écrasement, code de sortie 0 : « couples appliqués : 12 ; hunks : 8 ». Les trois fichiers produits (brouillon 8, sortie du compte, note des différences) sont **identiques à l'octet** (`cmp`) à ceux du dépôt. Rejeu fait sur le registre actuel : l'extrait de R-3521 y est donc toujours porté une seule fois.

## 3. Chaque changement rattaché à l'un des cinq commandés

Différence recalculée de mon côté (difflib, par ligne) : 10 régions modifiées, toutes rattachées, aucune autre.

1. **En-tête** : titre (l. 1), ligne de statut (l. 7), section neuve « Ce que le brouillon 8 change » (insérée après l. 38, 9 lignes).
2. **Couple du § 13** : l. 293 (devenue 302). Le « avant » est présent dans le brouillon 7 ; l'« après » est identique mot pour mot au couple de R-3523.
3. **Extrait de 7b et branche « sans objet »** : § 1 ligne « Préalable » (l. 85 -> 94) ; § 4 étape 1, point 2 (l. 138 -> 147) ; § 4 étape 4 (l. 142 -> 151, extrait rempli, phrase « Fait : la ligne neuve de constat est R-3521 » ajoutée).
4. **Exclus du § 8** : l. 245 -> 254, liste complétée, chaque ajout avec sa source.
5. **Compte des marqueurs** : § 11, ligne du tableau du marqueur de 7b (l. 269 -> 278, « rempli ») et phrase des comptes (l. 282 -> 291) ; la ligne du § 13 est le seul autre texte du § 11 touché : aucun.

Aucun changement hors de ces régions. Le texte inchangé restant, notamment le rappel historique de l'étape 1 (« attendre 7b ; si elle n'est pas créée le 25… »), garde la décision de Lazar telle qu'écrite et y ajoute « sans objet » : cohérent.

## 4. Extrait de 7b (point 3)

Programme à moi, lecture seule du registre : la ligne R-3521 est la **seule** ligne de `registres/decisions.md` qui porte `7b créée, instance 60218139 à 2026-11-11T14:19:58Z` (une occurrence ; aucune autre ligne ; aucun autre fichier de `registres/`). L'extrait que l'extraction par motif y trouve est identique, caractère pour caractère, à celui écrit dans le brouillon 8, qui le porte **exactement deux fois** (§ 1, l. 94 ; § 4 étape 4, l. 151), nulle part ailleurs. Le marqueur `<<LIGNE_REGISTRE_CREATION_7B>>` est absent du brouillon 8.

## 5. Les 13 marqueurs et le § 11 (points 4 et 5)

- Recompte indépendant du brouillon 8 : 31 occurrences, **13 distincts** : conception (chemin, empreinte) ; configuration (chemin, empreinte) ; commit de lancement ; empreintes du code ; dernière ligne des essais au processeur ; entropie ; exécutante ; lecteur ; longueurs de la consigne ; mot de Lazar de création ; version de l'outil de location. Identique à la sortie `sortie-compter-marqueurs-ii-b-v3.txt` et à la liste de R-3524.
- Tableau du § 11, recompté ligne par ligne : 36 noms ; sur les 30 : **16 remplis, 12 en attente, 2 hors de ce texte** ; plus 6 propres : 5 remplis, 1 en attente (commit de lancement). 12 + 1 = 13 : égal au compte du programme. Les noms « en attente » du tableau sont exactement les 12 de la sortie moins le commit de lancement. La phrase du § 11 (« 13 marqueurs distincts… = les 12 en attente des 30 + le propre en attente ») est juste. Les valeurs anciennes (14, 14, 2 ; 15, 13, 2) sont rappelées comme historique, justement.
- Reste noté, sans couple : la phrase finale du § 11 « Vérification au scellement : `grep -o '<<…>>'` vide » concerne le texte scellé final, pas ce brouillon ; elle est héritée du brouillon 7.

## 6. Écarts déclarés par le rédacteur : faut-il un couple ?

- **Suite de la ligne de statut décrivant encore le rédacteur du brouillon 6** : non. Ce texte est introduit par « Le brouillon 6 a été fabriqué… » et décrit bien le brouillon 6 (historique, y compris « vers 22:55 »). Seule imprécision : un « Il applique les couples de la contre-lecture du brouillon 5 » où « Il » renvoie au rédacteur du brouillon 6, ce qu'une lecture attentive comprend. Pas de couple.
- **Heure « vers 23:30 »** : le fichier du brouillon 8 date de 23:24:35Z (R-3524 : 23:25:37Z). L'heure écrite est donc postérieure de six minutes à la fabrication, au lieu de 23:22-23:24. Écart véniel d'un brouillon scellé comme brouillon, déjà déclaré dans R-3524, sans effet sur ce que le texte ordonne. **Pas de couple obligatoire.** Facultatif, si un brouillon 9 est fabriqué pour une autre raison : « vers 23:30 » -> « vers 23:24 ».

## 7. Autres observations (sans couple)

- Source de l'exclusion « le rédacteur du brouillon 8 (mandat de la session mère, `R-3523`, suite) » : R-3523 annonce seulement la suite (brouillon 8) ; c'est R-3524 qui nomme le rédacteur. La source est faible mais la personne est bien exclue ; à corriger à la prochaine version en « `R-3524` ».
- Sources de la liste du § 8 vérifiées : R-3312 (auteur du code du bras A exclu), R-3518 (vérificateur exclu), R-3310 (explorateur exclu), R-3520 (planificateur exclu), R-3485 et R-3497 (contrôles courts) existent et portent ce qui est cité ; les deux entrées citant la note du chemin critique (§ 7 point 2) n'ont pas pu être vérifiées (note non ouverte).
- L'ordre garde deux fois les mots « test de transfert » entre guillemets (liste du § 8 et section « Ce que le brouillon 8 change »), nommant l'agent exclu : voulu.

## 8. Refus rencontrés

Aucun.

## 9. Lectures hors mandat

Le motif de recherche sur `R-352[0-4]` dans `registres/decisions.md` a aussi affiché, en entier, les lignes R-3528, R-3529 et R-3533 (qui citent R-352x) ; sans lien avec la tâche ; rien n'en est repris ici sauf la ligne R-3533, qui dit que ce contrôle a été lancé. Début de lignes R-3310, R-3312, R-3485, R-3497, R-3509, R-3518 lu (700 premiers caractères et un extrait autour du mot « exclu »). Aucun fichier interdit ni dossier interdit ouvert.
