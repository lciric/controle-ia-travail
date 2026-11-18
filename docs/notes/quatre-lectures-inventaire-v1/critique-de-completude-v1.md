# Critique de complétude des quatre lectures sans dépense de l'inventaire des courses anciennes — v1

- **Écrit** le 18 novembre 2026 vers 06:00 UTC (`date -u` : 2026-11-18T05:59:19Z au début de la rédaction) par un sous-agent critique neuf (Claude Opus 5.5), sur une consigne calculée par le script de la mère, sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures sans dépense de l'inventaire (R-3168, R-3170, point 1). Je n'ai écrit aucune des notes, contre-lectures ou relevés de ce dossier.
- **Inventaire de référence** : `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md`, sha256 `b49dc2462382206d7e90eb35cac831a292f286af817399f65286a46898fd5fd0` (recalculé), sections A, B (points 1 à 4) et E (nœuds 1 à 4).
- **Cadre tenu** : aucune dépense, aucun appel de modèle externe, aucune clé lue ni affichée, aucun commit, aucune poussée, aucun `git fetch`. Rien lu sous `diag/` ; aucune branche `calcul/` ni `donnees/` ouverte. Dans l'extrait de la mère (`/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/quatre-lectures/extrait/`), je n'ai lu que les noms des dossiers et, dans les huit dossiers des tours du collisionneur v9, le seul champ `modele_servi` des journaux. Aucune cellule, fiche ni passage exclu n'a été ouvert. Aucun contenu des deux familles exclues (conception d'organismes saboteurs discrets ; évasion des moniteurs et bras d'attaque) n'a été lu.
- **Statut** : ce que disent les modèles du collisionneur ou de l'organisme est un avis ; ce que disent les rédacteurs et contre-lecteurs est leur constat, rapporté avec son lieu. Ce qui suit est mon constat de complétude. Je ne juge pas le fond des idées.

## Ce que j'ai lu

Le dossier `docs/notes/quatre-lectures-inventaire-v1/` compte 29 fichiers `.md`, tous scellés. J'ai vérifié les 29 avec `python -m controle_ia.scellement verifier` : tous répondent OK. Au moment de ma lecture, tous les fichiers et leurs compagnons sont suivis par git et égaux à `HEAD` (commit `e95db1b5`).
- **Lu en entier** : les critères scellés du 2 novembre ; les contre-lectures du 26 octobre et du 2 novembre.
- **Lu en grande partie** : le relevé d'ensemble des mentors (en-tête, sources, compte, fils communs, manques, réserves, destination, limites).
- **Lu par sections** (en-tête, ce que la version 2 change, sources, « ce que j'ai lu », exclusions, verdict, réserves, limites, et recherches ciblées dans le corps) : les versions 2 des trois premières lectures, la contre-lecture d'Argon, les six relevés des mentors en version 2 et leurs six contre-lectures.
- Les versions 1 n'ont été lues que par leurs empreintes et par ce que les versions 2 en disent.

Au dépôt : l'inventaire ; `registres/decisions.md` (R-3168, R-3170, R-3175) ; `registres/depenses.md` (lignes 328-351 et recherche des six montants des mentors).

## Verdict

**Les quatre lectures couvrent les quatre produits du point B de l'inventaire. Aucune course ni aucune branche annoncée n'est oubliée.** Les 22 branches des mentors (dix courses, douze branches de tours) sont toutes citées, comme les deux tours du 26 octobre et les deux dossiers du 2 novembre. Chaque note des trois premières lectures et chacun des six relevés des mentors a eu une contre-lecture neuve, qui a rouvert les sources, rendu le verdict « à corriger » et écrit une version 2.

Restent **quinze manques**. Aucun n'invalide une note. Trois touchent la couverture du contenu :
- les critiques croisées du deuxième tour ne sont lues par personne au 2 novembre, ni dans les quatre tours des mentors ;
- l'avis d'Argon n'est connu que de seconde main ;
- le relevé d'ensemble des mentors, note en vigueur de la quatrième lecture, n'a pas de contre-lecture.

Les versions 2 n'ont été revues par personne. Deux sont conditionnelles (Kirchner, Scheurer).

## 1. Couverture, source par source (inventaire, section B, points 1 à 4)

| point de l'inventaire | annoncé par l'inventaire | lu | non lu |
|---|---|---|---|
| 1. Tours « explorateur de neurones » et « déjà propre » du 26 octobre | deux tours, neuf cellules chacun ; branches `donnees/collisionneur-neuron-explorer-v1` (`191a658`) et `donnees/collisionneur-already-clean-v1` (`08e6b31`) | les 18 cellules, moins 66 passages exclus (famille 2 : environ 14 % des octets du premier tour et 19 % du second, recalcul du contre-lecteur) ; questions, journaux, états | branche `outils/collisionneur-neuron-explorer-preparatifs-v1`, que l'inventaire cite au tableau A.1 (ligne 20) ; invites ; dépôt `neuron-explorer` et essai non relus |
| 2. Collisionneur à cinq espèces du 2 novembre (sélection ; bac à sable) | 15 + 15 cellules ; branche `donnees/collisionneur-v8-runs-v2` (`0e7b3e59`) ; avis d'Argon seul et de Kimi seul | les 10 réponses (troisième tour), moins quatre passages proches de la famille 2 ; les 10 conceptions **en partie** ; les trois lectures vérifiées d'espèce seule | **les 10 critiques croisées** (deuxième tour), par le rédacteur comme par le contre-lecteur ; les faits servis au-delà des titres ; les réponses brutes d'espèce seule (lues par leurs lectures vérifiées) |
| 3. Avis d'Argon sur la porte G0 | `docs/notes/argon-seul-v1/lecture-argon-questions-ouvertes-abc-v1.md` (`be2b3c4d…`) | les 15 entrées de la question B (porte G0) de cette lecture ; grille v7 et v8, brief, programme, décisions | question A en entier et une partie de C (famille 2, selon le classement de l'inventaire) ; **la question et les réponses brutes d'Argon** (branche `donnees/sauvegardes-restaurees-2026-10-31-v1`, non extraite) ; les contre-lectures 6 et 7 de la grille (hors de `main`) |
| 4. Courses de l'organisme et tours du collisionneur sur les questions des mentors | dix branches `donnees/course-*-run*` et douze `donnees/collisionneur-v9-*` | toutes les fiches lisibles (Heimersheim 46/46, Kirchner 30/33, Ibrahim 64/64, Scheurer 12/22, Colognese et Ward 31/31, Jang et Feng 26/29, d'après le relevé d'ensemble § 1.7) ; conceptions et réponses des quatre tours | **critiques croisées des quatre tours, lues par leurs titres seulement** (relevé d'ensemble § 3.3) ; **deux appels seuls d'Astra et d'Argon sur la question Heimersheim** (GO-2026-11-03-02, `registres/depenses.md` l. 332), hors de l'extrait ; verdicts des juges, classements, lectures d'étiquettes (par choix) ; trois premières courses sans fiche lisible (Kirchner, Scheurer, Colognese et Ward) |

Le dossier `organisme-re-search` est aussi dans l'extrait. Il ne relève d'aucun point de l'inventaire. Je ne l'ai pas lu et aucune note ne le cite.

## 2. Manques

### Couverture du contenu

1. **Collisionneur du 2 novembre : les dix critiques croisées ne sont lues par personne.**
   - Le rédacteur le déclare (`collisionneur-2-novembre-v2.md`, « Ce que j'ai lu, et pas lu »). Le contre-lecteur ne les a pas ouvertes non plus (`contre-lecture-collisionneur-2-novembre-v1.md`, « Sources rouvertes »).
   - Or les critères scellés de la lecture disent, au point 2, que « la conception (premier tour) et la critique croisée (deuxième tour) servent à repérer les changements de position et les objections reçues » (`criteres-lecture-collisionneur-2-novembre-v1.md`, `4f5604b5…`).
   - C'est un écart de la lecture à ses propres critères. Il n'est pas déclaré comme tel, et la contre-lecture ne le relève pas.
   - Un tiers des cellules (10 sur 30) n'a donc été lu par personne, et les conceptions ne l'ont été qu'en partie.
   - Effet : la réserve 3 de la note (« accords nés de la critique croisée ») ne peut être vérifiée sur les cellules qui les ont fait naître.
2. **Tours des mentors : critiques croisées lues par leurs titres seulement.**
   - Le relevé d'ensemble le dit (§ 3.3 et § 6). La contre-lecture Colognese et Ward (correction 8) montre que ces cellules portent plus que leurs rubriques, par exemple les « défauts transversaux » de B (l. 17-42).
   - Le vivier d'idées du point 4 est donc incomplet de ce côté. Les idées propres à une critique, que la réponse n'a pas reprises, manquent.
3. **Avis d'Argon : lecture de seconde main.**
   - Ni le rédacteur ni le contre-lecteur n'a ouvert la question ni les réponses d'Argon (`avis-argon-g0-v2.md`, l. 64 et 314). Toute phrase « d'Argon » est une phrase de la lecture de Fable du 31 octobre (`be2b3c4d…`). La note le dit.
   - Pour la reprendre dans la grille de G0, il faudrait extraire seul le dossier de la question B (porte G0) de `donnees/sauvegardes-restaurees-2026-10-31-v1`, sans la question A, qui relève de la famille 2.
4. **Question Heimersheim : deux appels seuls non lus.**
   - Il s'agit d'Astra et d'Argon, faits le 3 novembre de 08:24 à 08:30 UTC (GO-2026-11-03-02, `registres/depenses.md` l. 332). Le relevé d'ensemble (§ 3.1) et le relevé Heimersheim les signalent hors de l'extrait.
   - Ce sont des produits sur une question des mentors. Le point B.4 de l'inventaire ne les nomme pas.
5. **Explorateur de neurones : une branche nommée par l'inventaire n'a pas été extraite.**
   - Il s'agit de `outils/collisionneur-neuron-explorer-preparatifs-v1` (inventaire, tableau A.1, ligne 20). Valeur probablement faible (préparatifs), mais non établie.
6. **Fiches retirées par cloisonnement : parts à garder en vue.**
   - À Scheurer, 10 fiches sur 22 sont exclues (seconde course). À Kirchner, 3 sur 33 ; à Jang et Feng, 3 sur 29.
   - Au 26 octobre, 14 % et 19 % des octets sont exclus.
   - Le vivier est amputé par construction. Personne n'a vérifié le classement de ces pièces (voir manque 13).

### Contre-lectures et versions en vigueur

7. **Le relevé d'ensemble des mentors n'a aucune contre-lecture.** C'est pourtant la note en vigueur de la quatrième lecture (`mentors-releve-d-ensemble-v1.md`, `f7eaec6f…`). Son rédacteur n'a rouvert aucune source et recopie les provenances des six relevés (§ 6). J'ai fait quatre contrôles par sondage, sans valeur de contre-lecture :
   - les 93 lignes de la table se répartissent bien 22, 17, 16, 13, 17 et 8 (compté par programme) ;
   - les six empreintes des relevés lus égalent celles des versions 2 actuelles ;
   - les six montants dits absents du registre des dépenses (seconde course Ibrahim, deux courses Scheurer, deux courses Colognese et Ward, Jang et Feng) n'y figurent pas (recherche des montants dans `registres/depenses.md`, aucune occurrence). Leur somme vaut 41,82 USD ;
   - dans les huit dossiers de tours v9 de l'extrait, le champ `modele_servi` de l'espèce B vaut `claude-opus-5-5`. Le nommage « Opus = Opus 5.5 » du relevé est donc juste pour les tours des mentors, à la différence du 2 novembre, où B est Opus 4.6.
8. **Personne n'a revu les versions 2.**
   - Les neuf versions 2 du dossier (trois lectures et six relevés) sont écrites par le contre-lecteur qui a jugé la version 1. Aucun lecteur ne les a vérifiées ensuite.
   - Chacune déclare en tête ce qu'elle change. Mais un ajout du contre-lecteur, par exemple les six oublis ajoutés au 2 novembre, n'a été contre-lu par personne.
9. **Deux versions en vigueur sont conditionnelles** : celles de Kirchner et de Scheurer.
   - Les deux contre-lecteurs écrivent que leurs retraits de cloisonnement ne sont pas, au sens strict, des corrections de fait. Si la mère lit la règle à la lettre, elle peut écarter la version 2 et faire appliquer ces retraits par le rédacteur (`contre-lecture-mentors-kirchner-q2-v1.md`, l. 21 ; `contre-lecture-mentors-scheurer-v1.md`, l. 36).
   - Tant que la mère n'a pas tranché, la version 2 est la seule qui tient le cloisonnement. Je la donne pour en vigueur au LISEZMOI, sous cette réserve.
   - Même nature au 26 octobre : la réserve sur la ligne 314 de la conception de B (« déjà propre ») attend le choix de la mère, qui peut appuyer la leçon sur les deux autres sources.

### Gestes prévus par l'inventaire et non faits

10. **26 octobre : aucun critère de lecture scellé avant l'ouverture.**
    - L'option (a) du nœud 1 de l'inventaire, accordée par Lazar (R-3170), prévoyait « un lecteur neuf, critères scellés avant ouverture ». Aucun fichier de critères n'existe pour cette lecture, et la note n'en parle pas. La contre-lecture ne le relève pas.
    - Au 2 novembre, les critères existent, mais leur antériorité ne repose que sur les dates de modification (04:08 contre 04:17), comme le dit le contre-lecteur.
11. **Avis d'Argon : rien n'est encore repris dans la grille de lecture de G0.** Le nœud 4 de l'inventaire disait « reprendre l'avis d'Argon dans la grille », comme pièce non opposable. La note est une annexe, et ses dix-sept questions attendent la prochaine version de la grille. C'est un geste de la mère.
12. **Les suites ne sont pas faites.**
    - La fusion du 2 novembre n'est pas confrontée à la conception v4 ni au brouillon 3 du préenregistrement de la course à plusieurs générations (R-3051). Le rédacteur le dit (réserve 5 ; § 3).
    - Les dix questions du 26 octobre à la tranche de la lecture par lentille neuronale arrivent après son texte gelé. Celui-ci a été scellé à 04:22:35Z (R-3175), deux minutes après le scellement de la note. Rien n'indique qu'elles lui ont été transmises. Elles ne peuvent plus servir qu'à un addendum ou à la tranche suivante.

### Affirmations non vérifiées et cloisonnement

13. **Le classement des passages exclus n'est vérifié par personne.** Ni les 66 plages du 26 octobre, ni les quatre passages du 2 novembre, ni la question A d'Argon, ni les fiches exclues des mentors. Les contre-lecteurs n'en ont vérifié que la taille et l'absence de reprise. C'est voulu par le cloisonnement, mais l'exhaustivité des exclusions comme leur justesse restent des affirmations des rédacteurs.
14. **Incidents de cloisonnement déclarés, à porter au registre par la mère** :
    - 26 octobre : des passages de la famille 2 ont défilé à l'écran avant d'être classés (rédacteur, réserve d'honnêteté) ;
    - Jang et Feng : le compte des axes « sur les 29 fiches » suppose que le rédacteur a lu au moins un champ des trois fiches exclues au-delà de leur titre (`contre-lecture-mentors-jang-feng-v1.md`, correction 4) ;
    - Kirchner et Scheurer : refus de l'outil de sécurité, respectés.
    Aucune note n'a repris de contenu exclu, d'après les contre-lectures.
15. **Restent non vérifiables ici** :
    - le commit court `0e7b3e5`, absent de l'extrait ;
    - l'origine des chiffres de l'essai « déjà propre » (183 ou 200 neurones, « < 2 % » ou « 5 % », « −0,004 nats ») : non vérifiés (R7), à lire sur le PDF empreinté avant toute citation.
    Tous les rédacteurs et contre-lecteurs sont Claude Opus 5.5, de la même famille que les espèces A et B du collisionneur. La règle R2 est tenue (agents neufs), mais aucune lecture n'est d'une autre lignée. La note du 2 novembre le signale comme biais possible (réserve 6).

## 3. Écarts de l'inventaire relevés par les lectures (pour une version 2 de l'inventaire)

- Tableau A.1 : les deux tours du 26 octobre y sont rangés sous « v2.5 ». D'après leurs `LISEZMOI-v1.md`, l'outil était la v2.6 (contre-lecture du 26 octobre).
- Tableau A.1, ligne 20 : le renvoi « l. 199 » de `lecture-voisin-neuron-lens-v1.md` ne nomme pas l'explorateur. Il vise sans doute `docs/notes/weight-space-programming-v1/piece-3-lecture-factuelle.md` l. 199 (note du 26 octobre, § 6).
- Tableau A.6, ligne 74, colonne « coût (registre des dépenses) » : les montants donnés pour la seconde course Ibrahim (10,64), la seconde course Scheurer (5,24) et Jang et Feng (8,74) n'ont aucune ligne dans `registres/depenses.md`. Ils viennent des rapports et du registre des décisions (relevé d'ensemble § 3.4 ; recherche confirmée par moi).
- Point B.3 : « 18 inexactitudes signalées sur 76 », contre « 82 entrées » au tableau A.3, ligne 48. Les deux comptes ne concordent pas. La note d'Argon s'en tient aux 18 inexactitudes.
- La ligne 149 de l'inventaire relève de la section C, non de la section B (contre-lecture d'Argon, correction 4).

## 4. Limites

- Je n'ai pas lu chaque ligne des corps des notes (voir « Ce que j'ai lu ») : un manque interne à un corps de note, non signalé par sa section de couverture ou par sa contre-lecture, peut m'avoir échappé.
- Je n'ai rouvert aucune cellule ni aucune fiche. Ma critique porte sur la couverture déclarée par les notes et sur leur cohérence avec l'inventaire, pas sur l'exactitude de leurs résumés.
- Le compte des cellules de critique croisée des quatre tours des mentors n'est pas établi ici. Je ne l'ai pas recompté pour ne pas ouvrir les cellules.
- Mes quatre contrôles du relevé d'ensemble (manque 7) sont des sondages, pas une contre-lecture.
