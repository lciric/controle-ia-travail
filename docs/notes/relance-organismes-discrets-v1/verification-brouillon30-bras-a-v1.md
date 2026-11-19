# Vérification du brouillon 30 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 29. Je juge ; je ne corrige rien.
- **Texte vérifié** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon30.md` (`0b51d1dde38a…`). Note : `9730ffe906b9…`. Compagnons vérifiés.
- **Pièce lue en plus** : `verification-corrections-code-v8-bras-a-v1.md` (`e8786ca7…`), parties 2 et 3.
- **Méthode** : comparaison des brouillons 29 et 30, phrase par phrase, par programme. Lecture des blocs touchés et de leur contexte : conventions, lignes 190 à 194 ; 6.9, lignes 739 et 759 ; 8.4, lignes 1013 et 1014 ; 13.1, ligne 1320.
- **Non ouverts** : aucun code ; les deux pièces de demandes en version 5, dont je n'ai pris que l'empreinte.

## Verdict : **engageable après corrections**

- **Aucune règle de jugement ne change.** Par programme, sont identiques au brouillon 29 :
  - la section 12, les sections 7.1 à 7.8 et la section 10 ;
  - les sections de l'hypothèse au seuil, 6.1 à 6.8, 9 et 11.
- Les fiches 9 à 12 parties à Lazar restent mot pour mot dans le texte.
- Tous les points demandés sont tenus (partie 1).
- Il reste **un défaut à corriger** : deux phrases du texte disent deux choses différentes d'une révocation qui entre pendant une panne (C-1).
- Il reste aussi **un mineur** sur les faux constats malsains (M-1).

## 1. Les points demandés

| point | état | endroit |
|---|---|---|
| ma vérification du brouillon 29, C-1 : gardes de `piece_source` et des dossiers sans cas sain ni artefact | **tenu** | 8.4, ligne 1013. Cas sains : clé nulle, donc `piece_source` non lu ; clé inscrite et empreinte égale ; dossier des arrêts conforme ; dossier de livraison avec sa configuration. Artefacts : autre module, `piece_source` mal formé ou sans la clé, dossier sans configuration ou rang avec un zéro devant, dossier des arrêts mal placé. |
| M-1 : ordre de la garde de `piece_source` ; `piece_source` mal formé | **tenu** | 6.9, ligne 759 : « cette garde joue avant toute garde de la liste fermée » ; mal formé ou sans la clé, la provenance n'est pas établie. |
| M-2 : pleine précision des bornes et des aires | **tenu** | 6.9, ligne 739 ; 13.1, ligne 1320 ; demande 32 de la pièce du développeur. Ce reste une demande, non une garde, et la réserve 4 de la note le dit. L'épreuve de forme le vérifie avant toute dépense. |
| M-3 : empreinte du programme dans le constat | **tenu** | Huitième champ du constat ; cinquième entrée de `pieces_attendues`. Le programme d'analyse confronte les deux. Artefact : « un constat qui porte l'empreinte d'un autre programme ». |
| vérification du code v8, C-1 : révocation reconnue au type | **tenu** | Conventions, ligne 194 : reconnaissance par le sens. 8.4, ligne 1014 : les trois artefacts de l'essai d'attaque du code (« revocation » sans accent, type « décision », simple mention), plus le cas sain de l'identifiant voisin. |
| code v8, M-1 : valeur ajustée contraire à l'état | **tenu** | 6.9, ligne 739 : valeur ajustée rapportée exacte ; tout nombre à virgule affiché porte « arrondie » ; l'état fait foi. |
| code v8, M-2 : ligne qui retire la configuration | **tenu** | Seule la ligne d'inscription inscrit. Toute autre ligne neuve qui cite l'empreinte rend le constat malsain. Artefact en 8.4. |
| code v8, M-3 : trace d'un constat malsain | **tenu autrement** | La vérification du code proposait un fichier scellé à nom daté. Le texte écrit la trace sur la sortie du programme, sous la forme à huit champs, versée au manifeste scellé. C'est conforme à R6 et R12, et rien n'est perdu. Cas sain en 8.4. |
| code v8, M-4 : moment du constat | **tenu en partie** | Le constat et la lecture partent dans une même exécution. L'acte de reprise et les constats de l'étape (m) portent l'empreinte du constat. Le rejeu et l'étape (n) relèvent de la lecture déjà partie. Mais voir C-1. |

## 2. Règles de jugement

**La révocation reconnue par son sens, avec ses faux constats malsains voulus : ce n'est pas une règle de jugement.**
- Le constat malsain arrête le **lancement**, avant toute lecture. Ni état, ni seuil, ni issue de 7.5 ou du point 21 n'est touché.
- Le remède : une ligne de GO neuve, donc un nouveau mot de Lazar, et une configuration neuve. C'est la règle « aucune livraison sans un mot de Lazar ».
- Le choix est prudent et assumé : un faux constat malsain coûte une ligne au registre, une révocation manquée ferait lire sous un accord retiré.
- Il est plus strict que la proposition de la vérification du code, qui levait un faux malsain par une lecture humaine. Le texte refuse qu'un programme ou un agent juge le sens d'une ligne, ce qui est cohérent avec la précision sur la révocation (brouillon 26).
- Coût pratique : voir M-1.

**« L'état fait foi » contre la valeur ajustée : ce n'est pas une règle de jugement, et la phrase ne peut pas se contredire.**
- En calcul exact, la valeur ajustée de Holm est au plus 0,05 si et seulement si l'hypothèse est rejetée par la procédure pas à pas.
- Vérifié par programme sur 100 000 familles de quinze valeurs : **aucun désaccord** entre l'état et la valeur ajustée exacte.
- Le désaccord relevé par la vérification du code ne venait que de la valeur à virgule affichée. Elle porte désormais « arrondie ».

**« Constat et lecture dans une même exécution » : c'est une règle de procédure, non une règle de jugement.**
- La lecture porte l'empreinte de son constat, ce qui la lie à lui.
- L'écart de temps se lit au manifeste. Le texte n'invente pas de durée maximale.
- Le programme d'analyse ne vérifie pas la « même exécution », et la réserve 3 de la note le dit.
- Reste une tension sur le rejeu : C-1.

## 3. Défaut à corriger

**C-1. Une révocation entrée pendant une panne : deux phrases du texte disent deux choses différentes.**
- **Endroits** :
  - conventions, ligne 194 : « Un rejeu après une panne, et l'étape (n), relèvent de la lecture déjà partie : ils se font sous le même constat, et une révocation entrée entre-temps est une révocation entrée après la lecture (6.9) » ;
  - 6.9, « Panne pendant une lecture » (brouillon 26) : « Une lecture qu'une panne interrompt avant tout résultat écrit … **n'est pas une lecture** » ;
  - conventions, constat de lancement : « si une révocation est entrée, la lecture ne part pas ».
- **Pourquoi** :
  - Pour une panne survenue **avant tout résultat écrit**, rien n'a été lu. Le brouillon 26 dit que ce n'est pas une lecture.
  - Le brouillon 30 traite pourtant une révocation entrée pendant cette panne comme entrée « après la lecture ». Le rejeu part alors sous un accord que Lazar a retiré, alors que rien n'était encore lu.
  - Pour l'étape (n), après le fichier scellé de l'étape (m), la phrase du brouillon 30 est juste : une lecture a eu lieu.
  - Ce n'est pas une règle de jugement. Lazar reste maître de ce que vaut la lecture, par la précision du brouillon 26 sur la révocation. Mais le texte se contredit.
- **Ce qui le réglerait** : borner la phrase au seul cas où un résultat est déjà écrit.
  - **Rejeu d'une lecture interrompue avant tout résultat** : la session rejoue d'abord le programme du constat, à titre de contrôle. S'il est malsain, le rejeu ne part pas. S'il est sain, le rejeu part sous le constat d'origine, dont l'empreinte est dans l'acte de reprise. La sortie du contrôle est versée au manifeste.
  - **Étape (n) après le fichier scellé de l'étape (m)** : elle relève de la lecture déjà partie, comme écrit.
  - **Garde en 8.4** : cas sain, rejeu après un contrôle sain. Artefact, rejeu après un contrôle qui voit une révocation.

## 4. Mineur

**M-1. Les faux constats malsains peuvent venir de la tenue même du registre.**
- Une ligne de la session principale ou de Lazar peut nommer la ligne de GO d'une reprise pour une autre raison qu'une révocation. Par exemple, une ligne de calcul « sous GO-… », ou une ligne qui remplace un point d'une autre.
- Si elle entre après l'état figé, le constat devient malsain. Si elle entre dans l'état figé après la ligne de GO, elle ferme cette ligne.
- Chaque fois, il faut un nouveau mot de Lazar.
- Une consigne de tenue, sans changer la règle, éviterait la plupart de ces coûts : entre la ligne de GO d'une reprise et la fin de la lecture, aucune ligne du registre ne la nomme, sauf pour la révoquer. La ligne d'inscription de la configuration ne nomme que l'empreinte de celle-ci.
- À joindre à la demande 29 de la pièce du lecteur habilité, ou au prochain brouillon.

## 5. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 à 29 intacts | compagnons vérifiés (`b076e3f9…` à `4446b21e…`) |
| brouillon 30 et note | `0b51d1dd…`, `9730ffe9…` : compagnons vérifiés |
| section 12 ; 7.1 à 7.8 ; section 10 | **identiques au brouillon 29** ; fiches 9 à 12 mot pour mot dans le texte |
| hypothèse au seuil ; 6.1 à 6.8 ; sections 9 et 11 | identiques au brouillon 29 |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 29 : 1 189 sur 1 189 retrouvées |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | huit lignes (1307, 1308, 1310, 1311, 1313, 1318, 1319, 1320), toutes en 13.1 |
| table d'en-tête, lignes neuves ou changées | empreintes égales : brouillon 29 ; sa note ; ma vérification ; vérification du code de la version 8 et son complément 1 ; les deux pièces de demandes en version 5 (`fc3f3c13…`, `7c7c8c4c…`, avec leurs compagnons). Les deux versions 4 sont gardées et dites « non sorties ». **Aucune empreinte de fichier cloisonné prise.** |

**À la session qui orchestre.** Les deux pièces de demandes en version 5 doivent passer leur relecture de cloisonnement avant de sortir (réserve 5 de la note). Je ne les ai pas lues.

## 6. Fichiers ouverts

- Le brouillon 30 : par différence ; les lignes citées en tête.
- Les brouillons 20 et 29, par programme.
- La note du brouillon 30.
- `verification-corrections-code-v8-bras-a-v1.md` : parties 2 et 3, et la table des titres.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Pour leur seule empreinte : les deux pièces de demandes en version 5, le complément 1 et la note du brouillon 29.
- Rien d'autre :
  - aucun code ;
  - aucun interne de moniteur ;
  - aucune clé ;
  - aucun appel de modèle ni appel réseau ;
  - aucun sous-agent.
- Un seul fichier écrit, celui-ci, scellé ; rien committé.
