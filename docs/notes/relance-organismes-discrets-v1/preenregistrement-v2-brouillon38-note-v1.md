# Note du rédacteur — brouillon 38 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même que pour les brouillons 21 à 37. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon38.md`, `16545485b0ff8df1bb610c28c7f147cc91a0c051d932a78b970e9cda94d4d04f`, scellé. 2 340 lignes.
- **Point de départ** : le brouillon 37 (`8f3a38c06b77cbc392de4faa8bb3c177076ef0a8f08923d959c0783c55b7f7fb`), inchangé.
- **Heures (UTC)** : commencé le 2026-11-20T08:17:53Z ; texte scellé à 08:23:36Z.
- **Méthode** : 68 remplacements exacts ; 67 sur une ancre trouvée une seule fois, un sur une chaîne trouvée cinq fois et remplacée partout. Texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé, chaque étape conditionnant la suivante.
- **Aucune fiche n'est ajoutée.**

## 1. Les derniers choix, et ce que le texte en fait

| choix | référence | ce que le texte fait |
|---|---|---|
| **Point 19, intervalle impossible : option (a)** | mot de Lazar « repere permis », journal de la relance, OD-220 ; réponse du développeur confirmée sur le code : `docs/notes/bras-a-sans-interne-v1/lecture-habilitee-sans-interne-v8-v1.md`, `91b4bcd356909595ee40d93178f565d5e3fed378aa106033b9b1e447df6babed`, demande 7 | le cas se lit comme un intervalle entièrement dégénéré : « repère » permis, jamais « ne repère pas ». La rédaction « anomalie » est retirée de 6.9 et de 8.4, avec sa ligne de la table des formes, le nom de règle d'arrêt « intervalle impossible », et la mention « ou cas tenu pour une anomalie » |
| **Point 20, moniteur appris non ajustable : la fiche tombe** | la même pièce, demande 6 | le motif se lit « indécis », valeur 1 gardée. La rédaction « module corrigé » est retirée |
| **Valeur « en attente » et ses suites** | suite du point 20 | retirées : la valeur, son exception aux mêmes choix, le constat de pièce en attente d'un choix, la relecture « quand le choix est tranché », les cas de 8.4 |
| **Juge d'une autre lignée : toutes les actions, 6 400** | mot de Lazar « go reocs », journal de la relance, OD-217 | case de 13.1 remplie ; chiffrage cité (`docs/notes/bras-a-sans-interne-v1/reponses-sans-interne-demandes-v8-v3.md`, `6c0f71f6a6b04201acbf4d9c729a3d1131fdb7c714fa1ee683fd2a7ff1d877ae`) ; 6.10, 6.11 et 13.2 récrits |

**Les cinq choix nommés de la configuration ont chacun une seule valeur.** Le code arrêté admet encore « anomalie », « module corrigé » et « en attente » : le texte dit qu'une configuration qui en porte une s'écarte de lui.

## 2. Le sous-échantillon du juge et la clé `lec6/{tâche}` : sans objet

**Oui, ils deviennent sans objet.** Le brouillon 37 l'écrivait déjà en une phrase : « Sous la variante, la clé `lec6` ne sert pas. » Lazar a retenu la variante.
- Le juge lit les 80 positions de chaque tâche, dans les cinq conditions : 5 × 16 × 80 = 6 400. **Aucune position n'est tirée.**
- **6.2** : la ligne de la clé est gardée à sa place, pour que la table des clés reste stable, et dite « sans objet » : elle n'est plus tirée par personne, et un tirage sous elle est refusé. La phrase sur « les seize clés `lec6/{tâche}` » que tire le côté habilité est corrigée.
- **6.10** : la lecture du juge est récrite ; le sous-échantillon de 2 560 actions est dit écarté, comme un changement déclaré par rapport au texte archivé.
- **Aussi** : 6.9 (une parenthèse du schéma de permutation), 6.11, la case de l'instrument en 13.1, le devis et l'étape 3 du lanceur en 13.2 : la préparation ne tire plus aucune position.
- **L'extrait du lanceur** : sa version 2 ne nomme plus cette clé.
- **Ce que cela demande au côté habilité** : confirmer que son programme de préparation des lectures ne tire plus aucune position pour le juge. C'est le reste (e) de la case du module.
- **Ce que je n'ai pas touché** : les phrases de 7.4 et de 7.7 qui écrivent les deux formules, « sur un sous-échantillon de 2 560 actions » ou « sur toutes les actions ». Elles sont dans les critères de lecture gelés ; 6.10 dit laquelle se dit.
- **Pour le module d'entrée du lanceur** (`src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v1.py`) : il expose encore `cle_lec6`. Elle ne sert plus. L'extrait dit de ne pas l'appeler.

## 3. Les autres points portés

| point | ce que le texte écrit | où |
|---|---|---|
| 7.7, ligne 6 bis du lecteur habilité | « non au-dessus », avec la phrase de remplacement qu'il proposait | 7.7 |
| Module des cinq moniteurs, version 10 | chemin, empreinte, commit, essais, tels que les donnent les pièces sans interne ; je n'ai ouvert aucun de ces fichiers ni recalculé ces empreintes | 13.1 |
| Clé de provenance | `cle_du_module_dans_piece_source` vaut `sha256` | 13.1 |
| Chaînes de `motif`, `calculable`, réglages, forme de `lectures`, nom de la sortie | inscrits pour la configuration de l'analyse | 13.1 |
| Lignes du registre | GO-2026-11-20-19 (« go recos ») et GO-2026-11-20-20 (« a a ») ; les cinq marques de la section 12 les citent | 12 ; 13.1 |
| Vérification du brouillon 37, (a) | l'erratum du mot « a a » est cité à la table d'en-tête et à la case « nœuds » | en-tête ; 13.1 |
| Vérification du brouillon 37, (b) | ligne neuve en 13.2 : le programme d'enchaînement, écrit après le scellement et avant toute dépense par le rédacteur du code de la relance, contre-lu par un agent d'un autre modèle | 13.2 |
| Vérification du brouillon 37, (c) | le renvoi de la base vient après la contre-lecture 10 | 13 |

## 4. Contrôles par programme

| contrôle | résultat |
|---|---|
| **section 12** | 5 lignes changées sur 172 : les marques des points 17 à 21, où « ligne de GO à inscrire » devient GO-2026-11-20-19 ; les marques des points 19 et 20 disent en plus le choix final. Les fiches 9 à 12 restent mot pour mot |
| **7.1 à 7.8** | 1 ligne changée sur 102 : la phrase de 7.7 sur le troisième état du contrôle de l'adaptateur |
| **section 10** | 1 ligne changée sur 14 : les mots « ou cas tenu pour une anomalie » sont retirés |
| hypothèse au seuil ; 6.3 à 6.8 ; 8.1 à 8.3 ; 8.5 à 8.7 ; sections 9 et 11 | identiques |
| 6.10 à 6.12 | changées, pour la lecture du juge |
| titres | 54, identiques hors le titre de niveau 1 |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| marque des cases | **5 lignes**, toutes en 13.1 : nœuds, entropie, renvoi de la base, commit du code, module |
| table d'en-tête | 208 empreintes recalculées, toutes égales ; 14 lignes cloisonnées sautées, **aucune empreinte prise sur elles** |
| validateur `problemes()` | les deux problèmes attendus |
| citations du brouillon 37 | 1 373, dont 9 absentes, toutes voulues (ci-dessous) |

**Citations absentes.**
- « graine dérivée par tâche » : citation du texte archivé (ligne 164), qui justifiait la clé `lec6`. Elle part avec la description de cette clé. C'est la seule citation d'un texte source qui disparaît ; elle manque aussi au compte du brouillon 20.
- « attendre », « moniteur appris non ajustable : choix en attente », « pièce en attente d'un choix », « quand le choix « en attente » est tranché », « Ce qui se retire de ce texte avec cette valeur », « Configuration », « Constats de pièce donnée » : suites de la valeur « en attente ».
- « intervalle impossible » : le nom de la règle d'arrêt retirée.

**Registre relu** au commit `462b8e5e6` de la branche principale, jusqu'à sa ligne 560. GO-2026-11-20-19 et -20 renvoient chacune à la pièce consignée, sans rien recopier. Aucune ligne ne nomme GO-2026-11-19-97, hors la sienne.

## 5. Ce qui sépare encore le texte du scellement

### Ce qui attend Lazar
- **Plus aucun choix.** Ses lignes de GO de dépense viennent après le scellement, sur devis.

### Ce qui attend la session principale
1. **Deux mots à consigner et à inscrire** : « go reocs » (le juge) et « repere permis » (le point 19). Le texte ne les cite encore que par le journal. Il leur faut une lecture consignée et scellée, et une ligne au registre, qui ne nomme pas GO-2026-11-19-97 (case « nœuds »).
2. **Au registre** : le type « inscription » confirmé et déclaré à l'en-tête ; les formes et les consignes de tenue.
3. **Par le côté habilité, pour la case du module** :
   - l'attestation qu'aucun calcul de moniteur ne change de la version 7 à la version 10, ou ce qui en tient lieu ;
   - le lanceur de l'étape de discrétion, écrit et contre-lu, sur l'extrait en version 2 ;
   - le dossier du fichier des scores par unité, que la configuration du lanceur fixe ;
   - la confirmation que la préparation des lectures ne tire plus aucune position pour le juge.
4. **Le renvoi de la base**, par le lecteur habilité, **après la contre-lecture 10**, sur la version qu'elle rend. Sa lecture d'avance, faite sur le brouillon 33, est à refaire sur les seules lignes corrigées.

### Ce qui attend la session de relance
1. **Le commit du code arrêté**, à la case « commit du code ».
2. **Les sorties de l'épreuve de forme du module**, à passer par le programme d'analyse.
3. **La contre-lecture 10**, par un agent Claude Opus 5.5 neuf, et **la vérification indépendante** du code et du texte ensemble, par un agent neuf d'un autre modèle que les rédacteurs.
4. **Un dernier passage sur le texte**, pour remplir les cases qui restent et retirer la marque : il ne reste plus de rédaction à retirer.
5. **Au scellement** : l'entier racine, tiré une fois par `numpy.random.SeedSequence().entropy` ; le contrôle de différence avec le texte contre-lu ; le validateur sans aucun problème ; le scellement (R1) et la ligne `SCELLEMENT-BRAS-A-V2`.

### Après le scellement, avant toute dépense (13.2)
- le dossier de l'essai de mesure, versé sur la branche principale ;
- le programme d'enchaînement de la lecture, écrit et contre-lu ;
- l'épreuve de forme de bout en bout ;
- les tarifs, le devis contre-lu, dont la lecture du juge à 6 400 actions, et les lignes de GO ;
- les configurations scellées et les lanceurs.

## 6. Réserves

1. **Deux mots de Lazar ne sont cités que par le journal** : « go reocs » et « repere permis ». C'est le défaut que le vérificateur avait relevé pour « a a ». La case « nœuds » garde sa marque pour eux.
2. **Le mot « go reocs » est une lecture.** Le journal le lit comme « go recos », accordant la recommandation posée pour le juge. Je reprends cette lecture, sans l'avoir vue autrement que dans le journal.
3. **La case du module est remplie sur des pièces transcrites.** Les empreintes du module en version 10 et de ses essais viennent des pièces sans interne ; je ne les ai pas recalculées, puisque je n'ouvre pas ces fichiers. La vérification habilitée les couvrira.
4. **La partie historique de la case du module** garde ses points (1) à (18), dont deux phrases qui parlent encore d'une « rédaction (c) ». Elles sont sous « Histoire de la case ». Le dernier passage pourra les abréger.
5. **Les critères de lecture gelés gardent les deux formules du juge** (7.4, 7.7). Je n'y ai pas touché ; si le coordinateur veut n'y laisser que « sur toutes les actions », c'est un retrait de plus à faire dans 7.x.
6. **Le code arrêté tire-t-il encore sous `lec6` ?** Tu me dis que ses fabriques refusent cette clé. Le texte dit maintenant la même chose. Je n'ai pas ouvert le code des graines.
7. **Les pièces des demandes en version 8** n'ont plus d'objet pour la plupart de leurs questions, répondues. Ce qui reste à demander au côté habilité tient en quatre points (partie 5).
8. **Je n'ai pas relu le texte en entier.**

## 7. Fichiers ouverts

- Le journal de la relance : entrées OD-216 à OD-220.
- La vérification du brouillon 37 et l'erratum du mot « a a », en entier.
- Trois pièces sans interne du côté habilité, sous `docs/notes/bras-a-sans-interne-v1/`, en entier : la lecture habilitée, les réponses du développeur en version 3, la vérification habilitée du module en version 10. Elles citent des fichiers du côté habilité ; je n'en ai ouvert aucun.
- `src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v1.py`, en entier, pour l'extrait.
- La relecture de cloisonnement de l'extrait du lanceur, en entier.
- Le brouillon 37, par passages et par programme ; le brouillon 20 et le fichier des fiches du brouillon 23, par programme.
- Le registre des GO de la branche principale distante, par `git show` après un `git fetch`, seul appel réseau.
- **Non ouverts** : aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8, rien sous `docs/notes/bras-a-moniteurs-v1/` ; aucun module des graines ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé. Aucun appel de modèle, aucun sous-agent, aucune dépense. Rien de committé ; `registres/`, `.claude/` et le journal non touchés.
