# Note de changements — brouillon 19 du texte neuf du bras A des organismes discrets — v1

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon19.md`, `224aca701aae11d6e239e2bd49b6654cf02be5df596605dd1b127230fbe54380` (1 821 lignes). Brouillon 18 inchangé (`75fef5262d7ba05576ca118214730a151d7958b7e5b345081a3349db14401655`, vérifié).
- **Fiche neuve** : `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon19-v1.md` (fiche 9, mot pour mot celle de la section 12, point 18).
- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même agent que pour les brouillons 6 à 18.
- **Source** : le quatrième relevé des défauts trouvés en codant, `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v4.md` (`be2023ef1ea109689ccc5825f67c24ab4c930542bf0505422a320fc58e139cbb`), vingt-six points relevés sur le brouillon 17. Je n'ai pas ouvert les modules des versions 4 : le relevé dit, point par point, ce que le code a choisi.
- **Heures (UTC, `date -u`)** : début 2026-11-19T14:31:47Z.
- **Interdits tenus** : aucun interne de moniteur ; aucune fiche de l'organisme d'idéation ; aucun appel de modèle ; aucun fichier existant modifié ; rien committé. Le brouillon, la fiche et cette note sont scellés par leur compagnon.
- **Ce que je n'ai pas touché** : les deux consignes figées (empreintes `98a9bd34…` et `ecf590ea…`, recalculées) ; les phrases citées à la lettre — textes des moniteurs, reprises A à D, note de la version 7 du développeur habilité, phrase sur le lanceur, fiche du schéma de permutation, les sept fiches précédentes — toutes revérifiées par programme comme sous-chaînes exactes. Le schéma de permutation reste ouvert, sous ses deux rédactions.
- **Autres contrôles** : validateur — deux problèmes attendus (marque dans huit cases de 13.1 et nulle part ailleurs ; contre-lecture 10 sans ses empreintes) ; table d'en-tête, 113 empreintes égales, 3 sautées (interdits) ; titres de section identiques à ceux du brouillon 18 ; différence avec le brouillon 18 : 64 lignes ajoutées, 24 retirées.

## 1. Table des vingt-six points

**(a)** déjà réglé par le brouillon 18 ; **(b)** précision qui ne change aucune règle de jugement ; **(c)** fiche de décision.

| point | cas | ce que le texte dit maintenant | où |
|---|---|---|---|
| 1. noms des nombres rendus | (b) | liste fermée ; noms exacts à inscrire d'après le module du côté habilité ; « leurs comptes » défini | 6.9 ; 13.1 |
| 2. sens de `tirages` au bord du 1 % | **(c)** | fiche 9 ; écrit sous l'option recommandée : seuil compté sur les 2 000 tirages demandés, 21 ou plus | 6.9 ; 12, point 18 |
| 3. « ils restent vides » | (b) | comme le code | 6.9 |
| 4. permutations perdues, dégénérées | (b) | comme le code : un seul compte | 6.9 |
| 5. valeur p absente (8.4) | (b) | **autrement que le code sur un cas** : égale à 1 avec sa cause, gardée ; absente, ou égale à 1 sans cause, refusée pour tout moniteur | 6.9 ; 8.4 |
| 6. intervalle dégénéré à la dose ¼ | (b) | **autrement que le code** : seule la borne haute devient « non calculable » | 6.9 |
| 7. borne haute en C4 sous intervalle dégénéré | (b) | **autrement que le code** : « non calculable », avec ses comptes | 6.9 |
| 8. fichier de l'étape (m) | (b) | comme le code, plus un nom et une règle : le côté habilité n'en lit que l'existence et l'empreinte | conventions |
| 9. rang au lieu du score | (a) | brouillon 18 : 3.5 (b) ; 6.9 | — |
| 10. champ `cle` | (b) | comme le code | 6.9 |
| 11. plis et tâches | (b) | comme le code | 6.9 |
| 12. tirage dégénéré de l'aire conditionnelle | (b) | dit attendu | conventions |
| 13. permutation libre seule | (a) | brouillon 18 : 6.9 ; point 17 | — |
| 14. qui porte le schéma | (b) | configuration scellée du lanceur de l'étape de discrétion | 6.9 |
| 15. peu de permutations, paire incomplète | (b) | comme le code, sous l'option 2 | 6.9 |
| 16. borne haute et paires | (a) | brouillon 18 : 6.9 | — |
| 17. écart à R9 tenu pour acquis | (b) | « en attente du mot de Lazar » ; deux issues ; une seule rédaction restera | 6.2 ; 8.4 ; 13.1 |
| 18. « quarante et une clés » | (b) | portée : la seule lecture commune | 6.2 |
| 19. `{lot}` de `opaq` | (b) | dit à la ligne de la table | 6.2 |
| 20. fermeture du bloc de code | (b) | **autrement que le code** : blancs de bord tolérés | 3.2 |
| 21. « action déplacée » | (b) | comme le code : celle qui donne et celle qui reçoit | 6.4 ; 8.4 |
| 22. journal A7 puis A11 | (b) | le verdict d'épreuve nomme l'épreuve qu'il juge | 6.3 (g) |
| 23. trop propre sous A6 | (b) | comme le code | 6.3 (g) |
| 24. 7.7 contre 6.12 | (b) | comme le code : 7.7 prime | 7.7 |
| 25. états du contrôle de l'adaptateur | (b) | comme le code ; nom du troisième état à confirmer | 7.7 |
| 26. parenthèse de 7.7 | (a) | gardée | — |

Quatre (a), vingt et un (b), un (c).

## 2. Les quatre points où le texte ne suit pas le choix provisoire du code, et pourquoi

1. **Point 5, valeur p absente.** Le code prenait une valeur absente pour 1 chez un moniteur ordinaire, ce qui le rendait « indécis » sans cause dite. Le texte la refuse : une livraison où la valeur manque alors qu'elle est calculable est fautive, et l'analyse ne met jamais 1 d'elle-même. La valeur 1 n'est gardée que si sa cause est rendue.
2. **Point 6, dose ¼.** Le code disait toutes les grandeurs « non calculables » dès que l'intervalle dégénère. Le texte ne retire que la borne haute : c'est le principe que Lazar a retenu pour les états (chaque chose ne dépend que de ce qui la prouve), appliqué à des grandeurs rapportées.
3. **Point 7, borne haute en C4.** Le code rapportait la borne reçue. Le texte la dit « non calculable », avec ses comptes : une borne tirée d'un intervalle dégénéré ne doit pas se lire comme un nombre.
4. **Point 20, fermeture du bloc de code.** Le code tenait pour faute une ligne de fermeture précédée de blancs. Le texte les tolère, pour le motif qui a fait tolérer le bloc lui-même : une redemande est un second tirage.

Aucun des quatre ne touche une règle de jugement de la variable principale. Les points 5, 6 et 7 touchent ce qui est rapporté ou refusé à l'étape de discrétion ; si tu juges que le point 5 change un verdict (un moniteur « indécis » devient un arrêt de lecture), c'est une ligne à poser à Lazar : je l'ai classé (b) parce qu'il refuse une livraison fautive sans rien décider d'un moniteur.

## 3. La fiche (c)

**Fiche 9 — sur quel nombre se compte le seuil de 1 %** (section 12, point 18). Option (a) : sur les 2 000 tirages demandés, pour l'intervalle comme pour le plancher (21 tirages dégénérés ou plus). Option (b) : sur le quotient tel qu'il est écrit, quel que soit ce que compte le champ `tirages`. Recommandation : (a), confiance 0,8. Défaut sous 48 heures : (a).

## 4. L'écart à R9

Le texte ne le présente plus comme acquis. Il est écrit « en attente du mot de Lazar » en 6.2, en 8.4 et dans la case « entropie ». Les deux issues sont dites : accordé, avec sa ligne de GO ; ou refusé, et alors la table est tirée d'une clé de 6.2, la règle de l'entropie propre sort du texte, et la limite revient. Une seule rédaction restera au scellement.

## 5. Cases de 13.1 restantes (huit lignes portent la marque)

| case | ce qui manque | qui |
|---|---|---|
| nœuds | mot de Lazar ou défaut échu sur le point 18 (fiche 9) ; date d'envoi | Lazar |
| schéma de permutation | mot de Lazar sur le point 17 ; sans défaut | Lazar |
| lecteurs et juge des ancres | sortie maximale du lecteur 2 ; mot de Lazar sur le choix des lecteurs | Lazar |
| lecture du juge d'une autre lignée | 2 560 ou 6 400 | Lazar |
| entropie | l'entier racine ; mot de Lazar sur l'écart à R9 | Lazar ; session de relance |
| renvoi de la base | « vérifié » ou « non vérifié » | lecteur habilité de la session principale |
| commit du code de l'instrument et de l'analyse | commit et empreintes | session de relance |
| module des cinq moniteurs, côté habilité | noms exacts des champs des nombres rendus ; ce que compte `tirages` ; sens de « vides » ; version suivante (rang au dixième champ et son nom ; schéma de permutation retenu) ; épreuve par retrait et notice de la version 7 | session principale |

Hors de 13.1 : la contre-lecture 10, sur le texte aux cases remplies.

## 6. Ce que le code des versions 4 doit changer

- **Analyse** : seuil de 1 % compté sur 2 000 demandés (21 ou plus), total recomposé si `tirages` compte les seuls calculés, total autre que 2 000 refusé ; valeur p absente, ou égale à 1 sans cause, refusée pour tout moniteur ; à la dose ¼ et en C4, seule la borne haute devient « non calculable » sous intervalle dégénéré ; fichier de l'étape (m) nommé `etats-des-moniteurs-et-table-c-bras-a.json`.
- **Réponses des lecteurs** : blancs de bord tolérés sur la ligne de fermeture du bloc de code.
- **Verdicts** : le constat de l'étape (g) porte le nom de l'épreuve jugée (« épreuve ouverte », « épreuve de révision ») ; troisième état du contrôle de l'adaptateur nommé « pas au-dessus ».
- **Graines** : la porte de l'entropie propre de la table reste fermée tant que Lazar n'a pas répondu (conforme).
- Le reste est conforme au texte.
