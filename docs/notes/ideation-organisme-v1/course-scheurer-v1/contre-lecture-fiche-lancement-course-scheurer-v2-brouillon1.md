# Contre-lecture de la fiche de lancement Scheurer v2, variante « sans Claude » (brouillon 1) — v1

Contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni le kit ni la fiche. 3 novembre 2026, 14:59 UTC (`date -u`).
Cadre de la lecture :
- aucun appel payant, aucune clé, aucun fichier existant modifié ;
- arbre partiel neuf `wt-cl-scheurer2`, au commit `19cce595` ;
- registres lus sur `main` (`83233a4e`) par `git show` ;
- de la sortie du premier run, seul le rapport `rapport-course-scheurer-v1.md` a été lu ;
- seul fichier écrit : ce rapport, non scellé et non commité.

Objet : `docs/notes/ideation-organisme-v1/course-scheurer-v1/fiche-lancement-course-scheurer-v2-brouillon1.md`,
sha256 `67fa274dfb086c152bba856e5b19d121477dffd15814b1a65bb73abba2efeb9f`. Compagnon vérifié : OK. Les numéros de ligne
renvoient à ce brouillon.

## Verdict

**Bloquant en l'état, pour une raison de règle et non de technique.**

Le kit v2 est techniquement conforme. Mais la fiche justifie la variante par la R-486 en lui donnant un sens qu'elle n'a pas
(l. 19-20). Or la R-486 décrit exactement ce cas.
- **Ce que dit la R-486** : session-depot y refuse de « faire passer par l'organisme une demande refusée par Opus et Fable »,
  même avec l'accord de Lazar, au nom de la consigne gelée « ne contourne jamais un refus d'un filtre de sûreté » (R-468 (5)).
- **Ce que fait cette variante** : Opus a refusé la question au tour du collisionneur, Fable l'a refusée à la course v1, et la
  variante retire toute la famille Claude pour servir la même question et les mêmes pièces à d'autres modèles.

La fiche ne peut pas être scellée tant que ce point n'est pas écrit honnêtement et tranché (CLS2-01). Le reste se corrige dans
le texte.

Ce que j'en pense sur le fond, à titre d'appui pour la décision et non comme verdict :
- La question (proposer comment mesurer une tendance d'échelle de comportements désalignés) est une question de méthode pour la
  sûreté.
- Les règles d'intégrité servies interdisent tout mode d'emploi.
- Elle diffère donc de la question « programme TAIF » de la R-486, qui portait sur des « contournements ».
- Mais deux refus de la famille Claude, sur ce texte, ne sont pas lus (R-468 (3)) : on ne sait pas ce qui les a déclenchés.
- Cette distinction doit être écrite et décidée, pas supposée.

## Points demandés

### 1. Le changement minimal du noyau v2

- **Le diff `7997da49..19cce595` n'ajoute que des fichiers** (34 fichiers, 4 911 lignes ajoutées, aucune retirée). Rien de la v1
  n'est modifié (R12).
- **Les cinq configurations v1 gardent leurs empreintes**, identiques à la table de la fiche v1 scellée : `364f2c91…`,
  `e6e739d7…`, `46d5025f…`, `02a36104…`, `916aff70…`.
- **Pièces, garde lexicale et paramètres du bisociateur de `sans-claude`** : identiques à `sans-opus`, metteur mis à part
  (comparaison faite).
- **Contrôles de la v2** :
  - Le relais 8806 et le contrôle de Claude ne jouent que si la configuration emploie Claude.
  - Les fournisseurs exigés sont ceux des rôles.
  - Un jeu de rôles est défini par variante.
- **Mutations neuves** : elles visent le changement exact et sont probantes.
  - M11 (relais Claude démarré sans Claude) fait échouer un essai.
  - M12 (Claude toujours exigé) en fait échouer trois.
  - M10 (marge réduite) reste détectée.
  - La copie intacte passe ses 64 essais (`resultat-mutations-scheurer-v2.txt`, `ebfdafaf…`).

### 2. Les rôles

- **Répartition** : Astra tient aiguilleur, premier juge, premier lecteur et metteur ; Argon tient second juge et second
  lecteur ; Kimi n'est que proposeur. C'est vérifié dans la configuration.
- **L'écart est déclaré** (l. 44-48) : deux lignées seulement, et Astra est aussi proposeur.
- **Mais l'auto-évaluation n'est pas rapportée à part.** La fiche dit seulement que « les sorties des deux juges sont rapportées
  à part ». Voir CLS2-02.
- **Astra est aussi l'aiguilleur, seul.** Le filtre « niveau méthode » est donc tenu par l'un des auteurs, sur la question que
  deux modèles Claude ont refusée (CLS2-01).

### 3. Relais Argon et S17

- **Relais Argon** : 20,7 USD au-dessus de la règle des 10 USD. L'écart est déclaré, avec son calcul : 1,2 × 17,1951 arrondi au
  dixième supérieur (l. 49-52). Il est cohérent avec le devis (pire cas d'Argon 17,20 USD).
- **S17** : 130 > 1,2 × 107,86 = 129,43 (calcul). C'est le plus petit entier au-dessus. L'arrêt d'étape vaut 117.
- **Relais, chacun au-dessus de son pire cas** : Astra 107,3 ≥ 89,88 ; Argon 20,7 ≥ 17,20 ; Kimi 2 ≥ 0,79. La somme fait 130.
- **Marge d'appels** : Astra (201 − 98) / 4 = 25 ; Argon (133 − 64) / 3 = 23. La borne de 23 annoncée est exacte.
- **Plafonds de session** : chacun au-dessus du pire cas d'un appel de son rôle.
- **Vérification `lancer_course_scheurer_v2.py verifier`** sur `sans-claude` :
  - **code 2** sur le vrai registre (« GO-2026-11-03-15 absent »), comme attendu ;
  - **code 0** sur une **copie** du registre où j'ai ajouté une ligne **factice** GO-2026-11-03-15 à 130 USD, jamais inscrite ;
  - sous GO-10, à 237 USD, la même configuration est refusée en code 2 (A15 : montant différent du S17).

### 4. La répétition corrigée

- **La déclaration est honnête** : elle figure à la l. 100 et en tête du résultat de la répétition. Le premier passage a échoué
  à l'essai 2 (« GEMINI_API_KEY_2 absente ») ; la cause était le script d'essai, pas le kit.
- **La seconde répétition est complète** et a été rejouée en entier :
  - essai 0 : refus sans autorité factice ;
  - essai 1 : course `sans-claude` au bout, code 0, aucun appel vers l'interface Anthropic ;
  - essai 2 : `kill -TERM`, code 130 ;
  - essai 3 : contrôle en échec, code 3 ;
  - essai 4 : plafond de session trop bas, code 2, aucun appel.
- **Réserve** : le résultat du premier passage n'est pas gardé dans le kit, et la fiche ne donne pas son chemin. Ce n'est pas
  exigé ; c'est mineur.

### 5. Le premier run

- **Il est cité** (l. 15-19) : branche `donnees/course-scheurer-v1-run`, `04ab7367`. Le suivant part d'un dossier de run neuf
  (l. 104-111 : `run-…-sans-claude`, hors du clone).
- **Il manque deux choses** :
  - l'empreinte du rapport (`6b2da5f5…`, R-1160) ;
  - sa réserve : la cause « refus de Fable » est **non vérifiée au journal de proposition** (rapport, « Comptes et cause
    probable »).
- Voir CLS2-03.

## Vérifié conforme (grille habituelle)

- **Table v2** : 61 lignes, toutes OK par `sha256sum -c`. `table_pieces_gelees_scheurer_v2.py --verifier` donne « conforme :
  61 pièces gelées ». Tous les compagnons du kit sont OK.
- **Empreintes citées, toutes exactes** :
  - `ff8e5dd2…` (configuration) ;
  - `167f87d3…` (devis v2) ;
  - `1cfea948…` (course à blanc v2) ;
  - `ebfdafaf…` (mutations v2) ;
  - `79170b2b…` (répétition v2) ;
  - `9391a28d…` (lanceur shell v2) ;
  - `fb5af70b…` (script de table v2).
- **Marqueurs** : le seul est `<<EMPREINTE_RAPPORT>>`, à la l. 10.

## Constats

### CLS2-01 — bloquant — la R-486 est citée à contresens ; la variante est le cas même qu'elle refuse

- **Où** : l. 19-20 (« Un refus ne se rejoue pas au même modèle (R-486) : la variante neuve n'emploie aucun modèle Claude ») et
  l. 24-25. Registre : R-468 (5), R-486, R-487, R-1160.
- **Le constat** :
  - La R-486 ne dit pas « pas au même modèle ». Elle dit : ne pas faire passer par l'organisme une demande refusée par Opus et
    Fable, même sur l'accord de Lazar, au nom de la consigne gelée.
  - Les circonstances sont réunies ici : refus d'Opus (tour), refus probable de Fable (course v1), même question, mêmes pièces,
    autres modèles.
  - Ce qui distingue ce cas de la R-486 (la question est une question de méthode, aucun contenu opérationnel n'est demandé)
    n'est écrit nulle part. Or c'est le seul argument qui pourrait permettre la course.
  - Dans cette variante, le filtre « niveau méthode » (l'aiguilleur) n'est plus tenu que par Astra, qui est aussi proposeur.
- **Correction** :
  - Récrire le § 1 en citant la R-486 et la R-468 (5) avec leur sens exact.
  - Y écrire, comme décision de session-depot et non comme évidence, pourquoi ce cas en diffère. Par exemple : la question ne
    demande que des mesures ; les règles d'intégrité interdisent le mode d'emploi ; le refus vise probablement les sources
    citées (portes dérobées, injections), non le fond. Ou bien conclure qu'il n'en diffère pas, et ne pas lancer.
  - Faire porter le mot de Lazar attendu pour GO-15 sur ce point précis : « les deux modèles Claude ont refusé ; course sans
    Claude ». La R-486 note que l'accord de Lazar ne suffit pas à lui seul : la décision revient aussi à session-depot, au
    regard de sa consigne gelée.
  - Garder dans le rapport la mention « course sans aucun modèle Claude » (l. 89), et ajouter : « après deux refus de la famille
    Claude ».

### CLS2-02 — mineur — l'auto-évaluation d'Astra n'est pas rapportée à part

- **Où** : l. 44-46.
- **Le constat** : Astra juge, lit et aiguille ses propres fiches.
- **Correction** : écrire que le rapport donne à part les notes de `juge-astra` sur les fiches d'Astra et sur celles des autres
  espèces, ainsi que les classes de l'aiguilleur par espèce. La clé de provenance le permet.

### CLS2-03 — mineur — le premier run est cité sans l'empreinte ni la réserve de son rapport

- **Où** : l. 15-19.
- **Correction** :
  - Ajouter l'empreinte du rapport `6b2da5f5…` (R-1160).
  - Écrire « refus de Fable : lecture probable, non vérifiée au journal de proposition (rapport) ».

### CLS2-04 — mineur — Argon en juge, jamais éprouvé, sous 4 000 jetons de sortie

- **Où** : l. 53-54, l. 101-102.
- **Le constat** : le risque est déclaré. Mais Argon tient la moitié des juges et des lecteurs, et toute troncature compte comme
  un échec (trois échecs consécutifs ou C13 : arrêt sans fiche).
- **Correction** : aucune dans le code. Dire au § 7 que ce rôle est le point de rupture le plus probable de la variante après
  CLS2-01.
