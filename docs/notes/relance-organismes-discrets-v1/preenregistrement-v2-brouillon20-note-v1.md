# Note de changements — brouillon 20 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Opus 5.5 (`claude-opus-5-5`), recopie seulement, pendant la limite d'usage de Claude Fable 5.2** (rédacteur des brouillons 6 à 19, arrêté jusqu'au 22 novembre). Je ne conçois rien. Toute précision qui demanderait un choix (règle de jugement, seuil, verdict, forme d'un calcul) n'est pas écrite dans le texte : elle est posée ici, dans la partie 3, « à trancher ».

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md`, `b076e3f942d6252883ab5008993cd0fb9d5ac9788171e3c52975b2b38229d697` (1 839 lignes). Le brouillon 19 n'est pas modifié (`224aca701aae11d6e239e2bd49b6654cf02be5df596605dd1b127230fbe54380`, vérifié avant lecture et après écriture).
- **Source** : les réponses du développeur habilité sur la version 8 du module des cinq moniteurs, recopiées à la lettre par la session de relance : `docs/notes/relance-organismes-discrets-v1/reponses-du-developpeur-habilite-noms-comptes-rang-v1.md`, `54c8afb3bcf77301e2ec8a494d890cbd699ba9069f1ea5032f52b92f79717107` (compagnon vérifié). Module cité : `autres_moniteurs_v8.py`, `61105129…`, commit `18f63f40`. **Je n'ai ouvert ni ce module ni les notes qu'il cite**, dont celle sur l'hypothèse de l'échange par paire (`95e656e7…`).
- **Ce que j'ai ouvert** : les consignes permanentes du dépôt ; le brouillon 19, par recherches ciblées et lecture des passages touchés (en-tête, conventions, 6.9, 8.4, section 12 points 17 et 18, 13.1, 13.2, fin de la section 14) ; sa note (`a939fcae…`) ; la fiche 9 (`955aa979…`) ; les réponses du développeur habilité ; le validateur `src/controle_ia/prereg.py`.
- **Interdits tenus** : aucun interne de moniteur ; rien sous `bases/`, `sondes/`, `t07*/`, rien de T0.8, rien de `scripts/mots_et_cout_*` ; ni `prereg/T0.6-organismes-v0-v1.md`, ni notices, contre-lectures du code ou vérifications des lots ; rien sous `src/controle_ia/organismes_discrets/bras_a_v2_habilite/` ; aucune fiche de l'organisme d'idéation ; aucune réponse de lecteur ; aucune variable de clé ; aucun appel réseau ni de modèle ; ni `.claude/` ni `registres/` touchés ; rien committé.
- **Heures (UTC, `date -u`)** : début 2026-11-19T14:42:36Z ; brouillon écrit à 14:47:27Z.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| titres de section (53) | les 52 titres de niveau 2 et 3 sont identiques à ceux du brouillon 19 ; seul le titre de niveau 1 change, « BROUILLON 19 » devient « BROUILLON 20 » |
| consignes figées (blocs de 3.2 et 3.3) | `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248` et `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816`, recalculées : égales |
| citations à la lettre du brouillon 19 | les 929 passages entre guillemets les plus extérieurs du brouillon 19 sont tous des sous-chaînes exactes du brouillon 20 ; les neuf lignes de la fiche du point 17, citée à la lettre sans guillemets, sont intactes |
| ancien nom de fichier, champ `score` | `scores-par-unite-moniteurs-bras-a.jsonl` et `` `score` `` ne restent qu'une fois chacun, dans la citation à la lettre du développeur habilité (version 7) en 6.9 |
| table d'en-tête | 118 lignes lues : 115 empreintes égales (dont les deux lignes neuves), 0 différente, 3 sautées (fichiers visés par les interdits : `registres/code-mots-et-cout-t06/…`, `prereg/T0.6-organismes-v0-v1.md`, `prereg/T0.8-base-A-mots-et-cout-v1.md`) ; une ligne à empreintes abrégées transmises (code de la base) non recalculée |
| validateur | aucun script de `scripts/` ne porte « valid » avec « prereg » ou « brouillon » (seul `validation_t04_instance.sh`, sans rapport) ; j'ai lancé `problemes()` de `src/controle_ia/prereg.py`, celui que le texte nomme validateur : deux problèmes, les mêmes qu'au brouillon 19, attendus — marque « À REMPLIR » dans huit cases de 13.1 et nulle part ailleurs ; contre-lecture 10 sans ses empreintes |
| différence avec le brouillon 19 | 15 blocs touchés, 27 remplacements exacts, chacun unique ; 18 lignes ajoutées (deux lignes de table, cinq lignes au point 17, onze pour 14.32) |

## 1. Ce qui change, section par section

| section | changement |
|---|---|
| titre | « BROUILLON 19 » devient « BROUILLON 20 » |
| statut (ligne 3) | statut neuf du brouillon 20 : recopie, rédigée par Claude Opus 5.5, ce qu'elle porte ; l'ancien statut devient « Au brouillon 19 » |
| auteur | phrase ajoutée : brouillon 20 recopié par Claude Opus 5.5, ce qui a été ouvert et ce qui ne l'a pas été |
| date ; commit lu | début du brouillon 20 ; commit `9345d01e` |
| note du rédacteur ; fiches | renvoi à cette note ; la fiche 9 a son enjeu complété au texte, son fichier ne l'est pas |
| table d'en-tête | deux lignes neuves : le brouillon 19 et les réponses du développeur habilité |
| conventions, « Numérotation stable » | « Au brouillon 20 : de même ; est neuf 14.32 » |
| 6.9 | sens des comptes (point 2) ; forme des comptes, à la lettre (point 3), avec une phrase qui dit que les écarts sont posés ici, non tranchés ; noms rendus en quatre listes fermées (point 1) ; « cause » lue comme `motif` rempli et `calculable` faux ; une phrase du nom nouveau après les deux citations sur la forme du fichier ; le dixième champ nommé `rang` et le fichier `rangs-par-unite-moniteurs-bras-a.jsonl` (point 4) |
| 8.4 | garde du cloisonnement : « dixième champ (`rang`) » ; garde de la famille de Holm : cause rendue par `motif` rempli et `calculable` faux |
| 12, point 17 | une puce d'information, à la lettre, avec les quatre puces de l'hypothèse de l'échange par paire ; le nœud reste ouvert, sans défaut |
| 12, point 18 | ajout à l'enjeu : le module compte comme l'option (a) ; l'option (b) divergerait de lui au bord. **La fiche n'est pas tranchée** |
| 13.1 | case « schéma de permutation » : renvoi à l'information du point 17 ; case du module : nom du fichier ; part « noms exacts », sens de `tirages`, forme des comptes, dixième champ remplis d'après la version 8 ; ce qui reste marqué est réécrit (partie 4) |
| 13.2 | ligne du lanceur de l'étape de discrétion : nom du fichier ; « État du lanceur » : non écrit, la session principale le fait écrire par le développeur habilité, contre-lu ensuite par Opus ; la phrase d'exigence du brouillon 18 est gardée à la lettre |
| 14.32 | neuf : table du traitement des réponses du développeur habilité |
| « Contre-lecture » | inchangée |

## 2. Endroits renommés

| endroit | avant | après |
|---|---|---|
| 6.9, phrase sur le nom du dixième champ | « le nom de ce champ dans la version qui l'écrira (`score` gardé, ou un nom qui dit le rang) est à inscrire en 13.1 » | le champ s'appelle `rang`, avec sa définition ; le fichier s'appelle `rangs-par-unite-moniteurs-bras-a.jsonl` |
| 6.9, après la citation de la session principale (« … étiquette, score ; … ») | — | phrase ajoutée : le dixième champ s'appelle `rang` depuis la version 8 |
| 6.9, après les deux citations du développeur habilité, version 7 (`scores-par-unite-moniteurs-bras-a.jsonl` ; `score`) | — | phrase ajoutée, « nom nouveau » : le fichier s'appelle `rangs-par-unite-moniteurs-bras-a.jsonl`, son dixième champ `rang` |
| 8.4, garde du cloisonnement | « dixième champ : rang dans le pli » | « dixième champ (`rang`) : rang dans le pli » |
| 13.1, case du module | `scores-par-unite-moniteurs-bras-a.jsonl` | `rangs-par-unite-moniteurs-bras-a.jsonl` (nom de la version 8 ; la forme de la version 7 reste citée sous son ancien nom en 6.9), « le dixième `rang` » |
| 13.2, ligne du lanceur de l'étape de discrétion, étape (6) | `scores-par-unite-moniteurs-bras-a.jsonl` | `rangs-par-unite-moniteurs-bras-a.jsonl`, « (champ `rang`) » |

**Non renommés, à dessein** : les deux citations à la lettre de 6.9 (elles gardent `scores-par-unite-moniteurs-bras-a.jsonl`, `score`) ; les tables de la section 14 qui décrivent des brouillons passés (14.30, 14.31 : « noms exacts à inscrire d'après le module », « rang au lieu du score ») ; le nom en clair « fichier des scores par unité », qui revient une quinzaine de fois (3.5 (b), 6.9, 8.4, 13.1, 13.2, conventions, section 14) et que le module garde lui-même dans la clé `scores_par_unite` : voir la partie 3, point 11.

## 3. Points « à trancher » (non réglés dans le texte)

1. **« Vides » contre la forme du module.** Le texte (6.9, point 3 du quatrième relevé) n'admet un couple de comptes vide que si l'aire n'est pas calculable pour une cause antérieure, sinon la livraison est refusée. Le module rend le couple des tirages `null` sous deux motifs qui ne sont pas des causes antérieures au sens du texte : « plus de 1 % de permutations perdues » et « intervalle impossible faute de deux tâches ». À la lettre du texte, ces livraisons seraient refusées.
2. **Citation de la version 7 contre la version 8.** La citation à la lettre (point 33 de la version 7) dit les quatre comptes « rendus aussi quand le moniteur n'est pas calculable à la dose parce que l'un des deux dépasse 1 % » ; la version 8 rend les tirages `null` quand ce sont les permutations qui dépassent 1 %. Laquelle fait foi ?
3. **Règle d'un moniteur dont seul l'intervalle dégénère** (choix de Lazar, GO-2026-11-19-70, option (b) de la fiche 16, écrite en 6.9). Le texte garde alors `valeur_p_haut` dans la famille de quinze, et le moniteur peut être « repère ». Le module, sous le motif « plus de 1 % de tirages dégénérés », rend `calculable` faux, les valeurs p nulles et `valeur_p_pour_la_famille` = 1 : le moniteur ne peut plus être « repère ». **Écart à une règle tranchée par Lazar** ; c'est le même écart que la note du brouillon 19 relevait sur le code (ses points 6 et 7), et la version 8 le porte encore, selon les réponses.
4. **Grandeurs rapportées sans verdict** (6.9 ; dose ¼ ; borne haute en C4). Le texte veut qu'un plancher au-delà de 1 % rende les seules valeurs p « non calculables », et un intervalle au-delà de 1 % la seule borne haute, l'aire restant rapportée. Le module rend aire, valeurs p et borne nulles dans tous les cas non calculables.
5. **« Cause » d'une valeur égale à 1.** J'ai écrit que la cause se lit comme `motif` rempli et `calculable` faux (6.9 ; 8.4). Reste un écart. Le texte ne nomme que deux causes qui gardent une valeur égale à 1 (aire non calculable ; plancher au-delà de 1 %). Le module en rend quatre : il met aussi `valeur_p_pour_la_famille` = 1, avec un motif, sous « plus de 1 % de tirages dégénérés » et « intervalle impossible faute de deux tâches ». La valeur p haute y est nulle, si bien que l'analyse ne peut pas voir qu'elle était calculable. Ces deux cas sont-ils une « cause » qui garde la valeur, ou une livraison à refuser ? La réponse dépend des points 3 et 6.
6. **Motif « intervalle impossible faute de deux tâches ».** Le texte n'écrit aucun état pour ce cas chez un moniteur du verdict.
7. **Motif « moniteur appris non ajustable ».** C'est une cause « avant les permutations » que le texte ne nomme pas (il dit : classe absente d'un pli, vocabulaire vide). Est-ce une « aire non calculable » au sens de 6.9 ?
8. **Correspondance entre les noms et la liste fermée du texte.** La liste du texte (aire, aires des deux plis, valeurs p basse, haute et pour la famille, aires au moins égales, borne haute, effectifs, comptes d'exclusion, quatre comptes, somme et maximum de l'agrégateur) ne se recouvre pas terme à terme avec les dix-huit clés. Le module ajoute `moniteur`, `dose`, `calculable`, `motif` et `quantile_borne_haute`. « Comptes d'exclusion » n'a pas de clé par moniteur et par dose : est-ce `exclues`, en sortie de la lecture commune ? La somme et le maximum de l'agrégateur sont en sortie de la lecture commune (`agregateur_somme_sans_etat`, `agregateur_maximum_sans_etat`), non par moniteur. Enfin, la règle « un champ de plus ou de moins arrête la lecture » ne dit pas à quelle liste elle s'applique : les dix-huit, les onze, les neuf, les cinq, ou toutes.
9. **Quotient de la règle de l'intervalle dégénéré.** En 6.9, la règle de la fiche 16 écrit `tirages_degeneres ÷ tirages`. `tirages` étant le nombre calculé, ce quotient a la forme de l'option (b) de la fiche 9, alors que le texte se dit écrit sous l'option (a). La phrase conditionnelle « si le champ `tirages` compte les seuls tirages calculés… » est aussi devenue sans objet. Les deux sont à reprendre après le mot de Lazar sur la fiche 9.
10. **Contrôle des réglages.** Le texte refuse un total différent de 2 000. Faut-il aussi contrôler `reglages.n_tirages`, `reglages.n_permutations`, et les valeurs de `reglages.permutation` et `reglages.unite_de_la_permutation` contre l'option que Lazar retiendra au point 17 ? Les réponses n'en donnent que les noms.
11. **Nom en clair du fichier.** « Fichier des scores par unité » devient-il « fichier des rangs par unité » ? Le module garde la clé `scores_par_unite`.
12. **Lecture de « nul ».** Le texte dit le champ « présent et nul » ; le module dit `null`, et zéro veut dire « compté, aucun ». Le texte entend-il `null` ? Je ne l'ai pas écrit.
13. **Case du module en 13.1.** Faut-il nommer la version 8 comme module qui fait foi, à la place de la version 7 qui reste inscrite comme « remplie » ? L'épreuve par retrait et sa notice, demandées « pour la version 7 », valent-elles pour la version 8 ? L'empreinte complète, le chemin et les essais de la version 8 manquent.
14. **Fichier de la fiche 9.** `decisions-bras-a-brouillon19-v1.md` se dit « mot pour mot » la fiche du texte. L'enjeu du point 18 est complété au brouillon 20 ; une version neuve du fichier de la fiche est à écrire avant tout envoi à Lazar. Je ne l'ai pas écrite : ce n'était pas demandé.
15. **Contre-lecture 10 et modèles.** La règle veut un contre-lecteur « d'un autre modèle que le rédacteur ». Le brouillon 20 est recopié par Opus 5.5, les brouillons 6 à 19 sont de Fable 5.2, et le lanceur sera contre-lu par Opus. Il faut dire quel modèle peut faire la contre-lecture 10. La liste des fichiers à lui donner ne porte pas encore les réponses du développeur habilité ni cette note.
16. **Hypothèse de l'échange par paire.** Je l'ai versée comme information seulement. Ce qu'elle fait à la fiche n'est pas écrit : en particulier, l'épisode honnête est commun aux quatre doses, et le rejeu au bit près n'est pas vérifié. Le nœud reste à Lazar, sans défaut.

## 4. Cases restantes de 13.1 (huit lignes portent la marque, comme au brouillon 19)

| case | ce qui manque | qui |
|---|---|---|
| nœuds | mot de Lazar, ou défaut échu, sur le point 18 (fiche 9) ; date d'envoi | Lazar |
| schéma de permutation | mot de Lazar sur le point 17 ; sans défaut (information de l'échange par paire versée) | Lazar |
| lecteurs et juge des ancres | sortie maximale du lecteur 2 ; mot de Lazar sur le choix des lecteurs | Lazar |
| lecture du juge d'une autre lignée | 2 560 ou 6 400 | Lazar |
| entropie | l'entier racine ; mot de Lazar sur l'écart à R9 | Lazar ; session de relance |
| renvoi de la base | « vérifié » ou « non vérifié » | lecteur habilité de la session principale |
| commit du code de l'instrument et de l'analyse | commit et empreintes | session de relance |
| module des cinq moniteurs, côté habilité | **remplis au brouillon 20** : noms exacts, sens de `tirages` et de `n_permutations`, forme des comptes, `rang` et nom du fichier ; **restent** : empreinte complète, chemin et essais de la version 8 ; mise d'accord de la forme des comptes avec 6.9 (partie 3, points 1 à 7) ; schéma retenu par Lazar ; lanceur de l'étape de discrétion, non écrit ; épreuve par retrait et notice | session principale |

Hors de 13.1 : la contre-lecture 10, sur le texte aux cases remplies (partie 3, point 15).

## 5. Ce que le code de la version 5 devra porter

**Ce qui découle de la recopie, sans choix :**
- Lire le fichier `rangs-par-unite-moniteurs-bras-a.jsonl`, dont le dixième champ s'appelle `rang` : rang moyen dans le pli, nombre à virgule, 1 pour la plus petite valeur, ex æquo à la moyenne de leurs rangs. Les neuf autres champs et leur ordre sont inchangés.
- Lire les nombres rendus sous les noms de la version 8 : dix-huit clés par moniteur et par dose ; onze en sortie de la lecture commune (`lectures` rangé par dose puis par moniteur) ; neuf dans `reglages` ; cinq dans `scores_par_unite`.
- Comptes : `null` veut dire « pas connu », jamais zéro ; zéro veut dire « compté, aucun ».
- Règle du 1 % : `tirages` est le nombre calculé et `tirages` + `tirages_degeneres` = `reglages.n_tirages`, le nombre demandé ; `n_permutations` est le nombre demandé. Le seuil est strictement au-dessus de 0,01 × les demandés, soit 21 sur 2 000. C'est l'option (a), celle du texte et du défaut ; la fiche 9 attend Lazar.
- Famille de Holm : prendre `valeur_p_pour_la_famille` ; une valeur égale à 1 avec `motif` rempli et `calculable` faux, pour les deux causes du texte, est gardée.
- Garde du cloisonnement : le dixième champ se lit sous le nom `rang`.

**Ce qui attend un arbitrage (partie 3) et ne doit pas être codé avant** : la réponse à un couple de tirages `null` sous les motifs « permutations perdues » et « intervalle impossible » (points 1, 2 et 6) ; la conduite quand le module rend `valeur_p_pour_la_famille` = 1 sous « plus de 1 % de tirages dégénérés », alors que le texte garde la valeur p haute (points 3 et 5) ; les grandeurs rapportées à la dose ¼ (point 4) ; la liste à laquelle s'applique « un champ de plus ou de moins arrête la lecture » (point 8) ; le contrôle des réglages (point 10).
