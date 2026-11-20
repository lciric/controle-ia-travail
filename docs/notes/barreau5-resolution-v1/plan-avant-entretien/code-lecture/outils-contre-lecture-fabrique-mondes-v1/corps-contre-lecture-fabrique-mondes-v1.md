# Contre-lecture de la fabrique des mondes et du juge de l'épreuve à vérité plantée (barreau 5) — v1

**Verdict : « conforme après ces corrections ».** La construction des mondes V0 à V12 et les règles du juge suivent le point 11. Mais le raccord au programme de lecture est faux en six endroits : tels qu'ils sont, **tous les mondes seraient refusés par la garde d'ouverture**, et le juge ne le verrait ni pour V0 ni pour V7. Seize couples corrigent la fabrique, trois le juge ; ils sont vérifiés sur une copie. Réserve : aucun monde n'est passé par la vraie garde, que je n'ai pas le droit de jouer (section 9).

- **Auteur** : contre-lecteur neuf, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). **Modèle** : Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que les deux développeurs (Claude Opus 5.5).
- **Date** : 20 novembre 2026 (horloge du conteneur).
- **Mandat** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/mandat-contre-lecteur-fabrique-mondes-v1.md`, sha256 `3c2ef07e479dd91642cfc9f8012db74e62e39e4bd3c047ef373e0e69f2e0e745`, vérifiée avant lecture.
- **Statut** : pièce d'instrument (classe B). Sortie scellée, non commise. La vérification des corrections me revient.

## 1. Ce que j'ai lu, et ce que je n'ai pas lu

Lu, chaque empreinte vérifiée avant lecture (toutes égales à celles du mandat) :
- le texte scellé (`bdff244f…d935`) : « Métrique », « Seuil », « Plan d'analyse » en entier, le point 11 avec sa table, « Critères de lecture gelés », « Ce que dira chaque issue au jury », « Liste d'arrêt » (lignes 151 à 261 et 302 à 361, repérées par les seuls titres). Ni « Ce que le rédacteur savait avant d'écrire », ni « La question » ;
- l'addendum 1 scellé (`2afa2186…99e4`), en entier ;
- le mandat du développeur (`d8977676…61e4`) et son rapport (`421bc554…d196`), en entier ;
- la fabrique (`f41377ae…c692`), le juge (`37e136b0…5e1c`), les essais (`6ffe12e0…4802`), en entier ; l'outil de mutations du développeur ;
- le programme de lecture `lecture_v1.py` (`d877d2de…c0df`), en entier, et le schéma de son résultat (`2c2cf90f…1114`) ;
- de la seconde programmation (`29c71ef9…5af7`), le comparateur seulement (lignes 496 à 778) ;
- deux modules que le programme de lecture appelle et sans lesquels les points 3 (b) et 3 (c) ne se tranchent pas : `barreau5_familles/engagement_v1.py` en entier (lignes du registre propre, table des étiquettes) et `manifeste.py`, lignes 1 à 80 (graines) ; et la définition de `CHEMINS_GELES` dans `harnais/validation_reelle.py` (lignes 71 à 73), pour le point 6.

Non lu : rien de `diag/` ; aucun score réel, aucune activation, aucune transcription ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'apprentissage des sondes sur la tâche ni de P3-bis ; rien de la branche de la formation ; aucun fichier « consigne-privee » ou « conception-ii-b » ; rien sous `archives-reponses-modeles/`. Aucun réseau, aucune dépense, aucun commit, aucun fichier existant modifié. Aucun code passé en ligne à l'interpréteur.

**À déclarer.** (1) Une de mes commandes de liste (le dossier `prereg/`, noms et tailles seulement) a rendu une sortie trop longue ; l'outil l'a rangée de lui-même dans un fichier sous `/root/.claude/`. Je n'ai pas ouvert ce fichier. (2) Aucun outil, aucun classifieur, aucune garde ne m'a rien refusé.

**Je n'ai pas joué l'épreuve.** Le programme de lecture n'est ni importé ni joué par mes outils. Les règles de sa garde que je confronte aux mondes sont recopiées de ma lecture dans `verifier_couples_v1.py` ; seuls `engagement_v1` et `manifeste` sont importés.

## 2. Constats

| n° | gravité | constat | preuve dans le programme | couples |
|---|---|---|---|---|
| B-1 | bloquant | **Forme des lignes du registre.** La fabrique écrit « - <date> `<nom>` : <contenu> ». Le registre propre se lit « \| CLÉ \| instant \| contenu \| référence \| » ; une ligne qui ne commence pas par « \| » est sautée. Aucune ligne n'est lue : refus « SCELLEMENT-B5F absente ou illisible », pour tous les mondes. La ligne `ENGAGEMENT-B5F` s'écrit « sha256 <64> », non « table sha256 <64> ». | `engagement_v1`, l. 42 à 44, 130 à 145, 184 ; `lecture_v1`, l. 453 à 456, 472 | F-6, F-7 |
| B-2 | bloquant | **Instants.** « 2026-11-21T08:00Z » n'est pas lu : le format est « AAAA-MM-JJTHH:MM:SSZ », secondes comprises. | `engagement_v1`, l. 44, 52 à 56 | F-2, F-5, F-11 |
| B-3 | bloquant, **hors de portée d'un paramètre** | **Lignes exigées et ordre des dates.** La garde exige dix lignes, non six : `SCELLEMENT-B5F` (qui cite le texte scellé et son empreinte), `CODE-FORMATION-B5F` (commit, entropie), `GO-FORMATION-B5F`, `SORTIES-FORMATION-B5F` manquent. Et elle exige l'épreuve et l'accord de lecture **avant** les scores ; la fabrique impose l'ordre inverse (scores avant l'épreuve), par un contrôle de ses paramètres qui interdit de le corriger sans toucher au code. | `lecture_v1`, l. 454 à 488 ; fabrique, l. 135 à 137, 191 à 197 | F-2, F-8, F-10, F-11, F-16 |
| B-4 | bloquant, **hors de portée d'un paramètre** | **Table des étiquettes.** (i) Le programme exige un seul sel de 64 signes hexadécimaux et des noms opaques qui se redérivent de ce sel (ordre des HMAC-SHA256) ; la fabrique tire un sel de 32 signes par ligne et des noms au hasard : refus « plusieurs sels ». (ii) L'empreinte engagée est celle de la forme canonique, **clés triées** ; la fabrique engage celle d'un fichier à clés non triées : refus « empreinte de la table différente de l'engagement » pour tout monde sain. (iii) Au deuxième cas de V7, la table reçue échange deux membres : elle serait refusée pour des noms qui ne se dérivent pas du sel, non pour l'engagement. | `engagement_v1`, l. 45, 68 à 104 ; `lecture_v1`, l. 526 à 532 ; fabrique, l. 618 à 626, 1031, 1076 à 1082 | F-1, F-2, F-12, F-13, F-15 |
| B-5 | bloquant | **Pli gelé.** Le programme recalcule le pli depuis les tâches du bilan et l'entropie de `CODE-FORMATION-B5F`, et refuse tout autre pli (« plis ≠ partition gelée »). Le défaut « pairs et impairs » est refusé. | `lecture_v1`, l. 670, 684, 740 à 748, 1364 | F-2, F-3, F-8, F-9, F-11 |
| B-6 | bloquant | **Nom du membre.** Le programme écrit `sur_saboteur` (tiret bas) ; le défaut de la fabrique est `sur-saboteur` : table « hors du plan », séries `A<k>-sur-saboteur` « hors du plan ». | `lecture_v1`, l. 106, 136, 530, 694 | F-4 |
| M-1 | majeur | **V7, premier cas.** La table est posée dans l'arbre sous `etiquettes.json`, nom que la liste blanche refuse avant que la garde des étiquettes ne la voie. Le refus sort, mais la garde que vise le point 8 de la liste d'arrêt n'est pas éprouvée. Sous un nom admis (`scores/etiquettes-pli0.json`), seule elle peut refuser. | `lecture_v1`, l. 141, 368, 404 à 428 | F-14 |
| M-2 | majeur | **Le juge ne confronte pas le motif d'un refus de V7.** Tout refus compte. Avec la fabrique telle qu'elle est, les six mondes refusés de V7 le seraient pour le registre illisible, et la règle « refus dans les quatre premiers cas » passerait. Montré sur un programme de ma fabrication : juge d'origine « passée », juge corrigé « manquée ». | juge, l. 309 à 310 | J-1 |
| M-3 | majeur | **V0 n'a que des règles « au plus ».** Un programme qui refuse les 2 000 mondes V0, ou qui n'y lit rien des sondes, passe les trois règles de V0 sans avoir rien lu (R5). Montré de même : juge d'origine « passée », juge corrigé « manquée ». | juge, l. 204 à 206, 374 à 378 | J-2 |
| m-1 | mineur | **Borne de la phrase E.** La phrase écrit la borne à trois chiffres significatifs ; le juge exige l'égalité à 10⁻⁹ près. Un traducteur qui lit la phrase ne peut pas la satisfaire. Descriptif seulement. | `lecture_v1`, l. 1128, 1220 ; juge, l. 446 | J-3 |
| m-2 | mineur | **Deux lettres de V0 sans essai** : « bruits indépendants d'un membre à l'autre » au niveau des jetons, et « de même loi pour les trois membres ». La fabrique les tient (lecture du code) ; aucun essai ne tuerait leur perte (mutations c1 et c2, section 7). | — | essais à ajouter |
| m-3 | mineur | **Clés du registre.** Une clé en « -B5F » inconnue du programme arrête la lecture. `lignes_supplementaires` ne peut donc porter que `GO-RELANCE-FORMATION-B5F` (qui change la copie attendue en `<k>-x1`), `LECTURE-B5F` ou `VERDICT-B5F` (qui font refuser). À dire dans l'en-tête de la fabrique. | `engagement_v1`, l. 38 à 40, 140 | texte |
| m-4 | mineur | **En-tête de la fabrique.** Sa liste des « lacunes de l'interface » et la section 8 du rapport du développeur sont tranchées par cette contre-lecture ; l'en-tête est à récrire avec les couples (erratum du développeur). | — | texte |

Le développeur ne pouvait voir aucun des six bloquants : le mandat lui fermait le programme. Sa garde factice, écrite depuis la même interface, partage ses lectures ; ses 138 essais et ses 50 mutations ne les touchent pas. C'est la raison d'être de cette contre-lecture, non un défaut de son travail.

## 3. Point 1 — Les mondes et le juge

**Unité et bruit.** Chaque contraste planté vaut μ + u ξ, avec u² + v = 1, v étant la variance que les bruits d'action et de jeton de deux membres laissent dans la différence de leurs statistiques (640 actions) : la différence d'une famille à l'autre a un écart type de 1. Les écarts sont plantés au niveau des scores par jeton (décalage du membre, bruit par action et bruit par jeton, tirés série par série) ; les déplacements moyens sont plantés à part, sur des coordonnées disjointes, et le programme en tire lui-même produits, facteurs et mises à l'échelle. J'ai refait à la main, sur le code du programme (`Pli.scores`, `Notation.statistique`, `epreuves`), le calcul de chaque monde.

| monde | planté comme le veut le point 11 ? | remarque |
|---|---|---|
| V0 | oui | trois membres de même loi, indépendants ; bruit par jeton normal, le maximum change de jeton ; coûts rangés ; les facteurs de E2a et de E2b sortent des déplacements, dans les bornes |
| V1 | oui | sur-saboteur à 6, saboteur à 3 ; q = r = 1/ρ, ρ de 0,85 à 1,2 : l'écart à poussée égale reste près de 6 |
| V2 | oui | trace de −(4 + u ξ) sur les deux membres édités ; q = r = 1 exactement : E2a = E2b = E3 ; séparation apprise à 1. Un passage à tort de E3 (0,5 % par monde) y donne « sabotage » : attendu 2,4 sur 500, la règle « 10 au plus » tient |
| V3 | oui | le sur-saboteur porte λ fois ce qu'il partage ; q = r = 1/λ ; l'écart égalisé est nul, au bruit propre de chaque membre près |
| V4 | oui | sur-saboteur à −3 ; le saboteur à −1,5 est un choix de la fabrique, que le texte ne fixe pas |
| V5 | oui | écarts nuls, séparation apprise à 8 ; tous les \|d_k\| sous 4 |
| V6 | oui | mêmes niveaux de coût pour les trois membres |
| V7 | oui après F-12 à F-15 | voir section 4 |
| V8 | oui | force sur ĝ seule ; r = λ_j / (λ_j + e3) annule E2b ; q reste près de 1, E2a garde environ 5 |
| V9 | oui | force sur la part de la famille seule ; le saboteur n'a rien sur ĝ ; q = λ_j / (λ_j + e3), r = 1 |
| V10 | oui | deux produits de E2a nuls ou négatifs (exactement nuls : coordonnées disjointes), un √q hors bornes, deux poussées non positives, un √r hors bornes ; E2a à sept familles, E2b à neuf |
| V11 | oui | sur-saboteur à 6, saboteur égal au jumeau |
| V12 | oui, avec un choix déclaré | la trace commune est multipliée par la force chez le sur-saboteur : c'est ce qui fait « disparaître » l'écart à poussée égale, que le texte exige ; le signe de la trace est partagé en deux moitiés (−4 : la réunion que vise « Seuil » ; +4 : la lettre). Les deux moitiés tiennent sous la même règle. Je le tiens pour juste ; c'est un choix que le texte ne fait pas, à connaître de la mère |

Bruit propre à chaque membre dans V3, V8, V9 et V12 : oui, et dans tous les mondes à régime fixe (un tirage par série, par action et par jeton ; essai du développeur sur V3, V9 et V12).

**Le juge.** Il applique la colonne « règle gelée » ligne pour ligne : nombres de mondes (2 000 ; 500 ; 200), bornes « au plus » (20, 20, 20 ; 10 ; 0 pour V4) et « au moins » (480 ; 490 pour V6), motifs exacts de V8, V9 et V11, motif « force non écartée » de V3 (partie non vide de {E2a, E2b}) et de V12 (qui nomme E2a ou E2b), les trois règles « dans tous les mondes » de V10, les trois de V7. Sa table du seuil est celle du texte (10 : 3 ; 9 : 1 ; 8 : 0 ; à 95 %, 7 : 2 ; 6 : aucune). Ses deux lectures déclarées (« au moins » au niveau de la vérité, « au plus » à tout niveau) sont celles de l'addendum. Trois défauts : M-2, M-3 et m-1 ci-dessus.

## 4. Point 2 — Les arbres, champ par champ

Hors des six bloquants, chaque fichier est celui que lit le programme. J'ai suivi `exiger_arbre`, `exiger_arbre_sans_etiquettes`, `charger_arbre`, `Pli`, `lire`, `manipulation`, `charger_entrees`, `exiger_copie_lue` et `exiger_alignement`, champ par champ :
- `inventaire.json` : format, `run_id`, lignes à trois clés, tout fichier de l'arbre sauf lui ; aucun compagnon ; tous les noms dans la liste blanche ;
- `bilan-relecture.json` : format, tâches, plis, sondes (les trois qui ne se coupent pas y sont) ;
- `scores/<sonde>-pli<k>.json` : format, sonde, pli, couche (7, 15, 23), tâches du pli, statut, séries à la seule clé « actions », noms de séries admis ;
- `jetons/<sonde>-pli<k>/<série>.json` : les cinq clés exactes, pour `decisive` et `comparaison`, pour toute série sauf les séries propres ; même nombre de jetons par action ; score d'action égal au maximum, au bit près (l'écriture JSON d'un flottant se relit à l'identique) ;
- `produits.json` (déplacements seuls : le programme recalcule), `intensites.json`, `textes-honnetes.jsonl` ;
- `couts.json`, `formation-resume.json` : formats, « copie » égale au nom de la famille (aucune ligne de relance), membres présents seulement ;
- aucun fichier de l'arbre ne porte une clé « famille » : la garde des lignes de formation ne se déclenche pas à tort.

**Un monde sain passe-t-il ses gardes ?** Tel quel, non (B-1 à B-6). Après les couples, oui selon les règles recopiées : le monde sain, les deux familles incomplètes et les sept familles sont acceptés (`resultats-verification-couples-v1.json`). Non éprouvé sur la vraie garde.

**Chaque monde de V7 produit-il le refus attendu, et lui seul ?** Après les couples :

| cas | artefact | refus du programme (fragment que le juge corrigé exige) |
|---|---|---|
| 1 | table sous `scores/etiquettes-pli0.json`, inventoriée | « table des étiquettes présente dans l'arbre de lecture » |
| 2, deux mondes | table reçue cohérente, sous un autre sel ; ouverture à l'empreinte engagée, ou à celle de la table reçue | « empreinte de la table différente de l'engagement » (la comparaison à l'engagement passe avant celle de l'ouverture) |
| 3 | `SCORES-B5F` daté après `OUVERTURE-B5F` | « OUVERTURE-B5F n'est pas postérieure à SCORES-B5F » |
| 4, deux mondes | une action ôtée d'une série de la sonde décisive ; un fichier de scores par jeton absent | « score manquant » |
| 5, deux mondes | famille sans sur-saboteur ; famille sans saboteur | lus : familles présentes 9 partout ; ou M1, E1, E2a à 9 et M3, E3, E2b à 10 ; motif écrit par le programme |
| 6 | sept familles | lu : toutes les épreuves à sept familles, niveau de 95 %, seuil 2 |

## 5. Point 3 — Les quatre points ouverts

**(a) La forme du résultat.** Un traducteur est nécessaire. Le programme écrit `resultat-lecture-b5f.json` dans le dossier de sortie ; sur un refus, il n'écrit rien, sort au code 2 et écrit « REFUS : <motif> » sur la sortie d'erreur. Je l'ai écrit : `outils-contre-lecture-fabrique-mondes-v1/traducteur_resultat_vers_rendu_v1.py` (essais sur des résultats fabriqués : passés ; jamais joué sur un résultat du programme). Il ne recalcule rien. Correspondance :

| champ du rendu | champ du résultat |
|---|---|
| `refus`, `motif_refus` | code de sortie 2, aucun fichier de résultat, dernière ligne de la sortie d'erreur après « REFUS : ». Tout autre code que 0 ou 2 est une panne : aucun rendu, le juge compte un rendu manquant |
| `issue` | `g_issue.code` |
| `niveau` | `g_issue.niveau` : « 99 », « 95 », null → 99, 95, null |
| `motifs_D` | `g_issue.motifs` : « force non écartée (E2a) », « (E2b) », « (E2a, E2b) » → E2a, E2b ; « saboteur non établi » → E1 |
| `mention_saboteur_sans_sur` | issue N et `g_issue.motifs` porte « saboteur au-dessus de son jumeau sans que le sur-saboteur le soit » |
| `epreuves.<e>` | `b_manipulation.<e>` pour M1 et M3 ; `d_epreuves.<e>` pour E3, E2a, E2b, E1 (absentes si `d_epreuves` est null) : `decision` ← `separe`, `contraire` ; `K` ; `niveau` ; `w` ; `W_moins` ; `W_plus` |
| `familles_E2a.<f>`, `familles_E2b.<f>` | pour chaque famille de `d_epreuves.E3.familles` : `presente` ← présence dans `d_epreuves.E2a.familles` (ou `E2b`) ; `motif`, `c_un` ← les phrases de `d_epreuves.familles.<f>.motifs` ; `c_sur` ← `d_epreuves.familles.<f>.E2b.facteur` |
| `familles_absentes.<f>` | la phrase « jumeau ou sur-saboteur absent : … (point 17) » de `d_epreuves.familles.<f>.motifs` |
| `manipulation.<f>` | [`b_manipulation.details.<f>.taches_communes`, `.taches_retenues`] |
| `phrase_E` | `borne` ← le nombre de `g_issue.phrases.issue` après « plus petite que » ; `delta_app` ← `c_separation_apprise.delta_app` |

Couples : J-3 (précision de la borne), J-1 (le motif du refus est lu).

**(b) Les lignes du registre fabriqué.** Dix lignes, chacune « | CLÉ | AAAA-MM-JJTHH:MM:SSZ | contenu | référence | » (la référence est libre ; ni « | » ni saut de ligne) :

| clé | contenu exact |
|---|---|
| `SCELLEMENT-B5F` | `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md ; sha256 bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935 ; membres-apprentissage 3 ; piece famille` (« 2 » ou « 3 » ; « famille » ou « instance ») |
| `CODE-FORMATION-B5F` | `commit <40> ; entropie <entier de ]0 ; 2^128[>` |
| `GO-FORMATION-B5F` | `GO-AAAA-MM-JJ-NN` |
| `SORTIES-FORMATION-B5F` | libre |
| `ENGAGEMENT-B5F` | `sha256 <64>`, empreinte de la forme canonique de la table |
| `CODE-LECTURE-B5F` | `commit <40> ; lecture sha256 <empreinte du fichier du programme joué>` |
| `EPREUVE-B5F` | `passee ; lecture sha256 <la même> ; rapport sha256 <64>` |
| `GO-LECTURE-B5F` | `GO-AAAA-MM-JJ-NN` |
| `SCORES-B5F` | `commit <40> ; inventaire sha256 <sha256 de arbre/inventaire.json>` |
| `OUVERTURE-B5F` | `table sha256 <64>` |

Ordre strict des instants : scellement et code de formation avant l'accord de formation ; accord de formation avant les sorties ; sorties avant l'engagement ; code de lecture avant l'épreuve ; engagement, épreuve, accord de lecture et code de lecture avant les scores ; scores avant l'ouverture. Ni `LECTURE-B5F` ni `VERDICT-B5F`. Couples : F-2, F-5 à F-8, F-10, F-11, F-16.

**(c) Les identifiants de tâches et le pli gelé.** Les identifiants sont libres (lettres, chiffres, « . », « _ », « - ») : le programme ne lit pas le fichier des tâches, il prend celles du bilan. `t00` à `t63` conviennent. Le pli, lui, n'est pas libre : c'est la permutation des identifiants triés tirée de la clé `b5f/lecture/plis` sous l'entropie de la ligne `CODE-FORMATION-B5F` du registre fabriqué ; première moitié, pli 0 ; chaque pli trié. La même entropie sert aux tirages de la séparation apprise. Couples : F-2, F-3, F-8, F-9, F-11. La fabrique refuse désormais un pli qui n'est pas celui-là.

**(d) La raison technique écrite d'un membre manquant.** Le programme ne l'exige pas et ne la lit nulle part. Un membre manque quand il n'est pas dans la table des étiquettes ; il doit alors manquer aussi aux séries de scores (le programme exige que les séries opaques égalent les noms de la table). Le programme écrit lui-même le motif : « jumeau ou sur-saboteur absent : famille absente de toutes les épreuves (point 17) », ou « saboteur absent : famille absente de E1 et de E2a (point 17) ». **La fabrique n'a rien à écrire** pour les deux mondes du cinquième cas, qui sont déjà plantés ainsi. Aucun couple. La raison « écrite avant toute lecture » du point 17 est une obligation de la chaîne réelle, hors du programme : à tenir par la mère au registre.

## 6. Point 4 — Vérités et graines

- **Vérités à part** : oui. Un seul fichier pour les 7 269 mondes ; le dossier d'un monde n'en porte rien (son identifiant dit son groupe, mais le programme ne lit pas `monde.json`). Le juge refuse un fichier de vérités dont l'empreinte n'est pas celle qu'on lui dit engagée.
- **Empreinte engagée avant tout passage** : c'est une procédure, que le code ne peut pas imposer. Les vérités portent l'empreinte de la fabrique, les paramètres, l'entropie et la version de numpy. **Où l'inscrire** : pas au registre propre sous une clé neuve en « -B5F », que le programme refuserait à l'ouverture réelle (« clé inconnue ») ; dans un fichier scellé et commis avant le premier passage, ou dans une ligne du registre qui ne commence pas par « | ».
- **Graines (R9)** : `numpy.random.SeedSequence(entropie, spawn_key=(c, flux))`, c tiré de la clé écrite `b5f/epreuve/<monde>` par la règle du dépôt, flux de 0 à 3. Conforme à R9 et à la clé du point 14 ; le second terme de la clé de dérivation est un ajout déclaré.
- **Une remarque pour la mère.** Le point 14 range `b5f/epreuve/<monde>` parmi les clés de l'entropie tirée à l'inscription de `CODE-FORMATION-B5F` ; le point 11 ne parle d'« entropie neuve » que pour un passage rejoué. Si le premier passage se joue sous une autre entropie que celle de la formation, c'est à écrire comme un choix.

## 7. Point 5 — Mutations

Huit mutations de mon choix, absentes de la liste du développeur, jouées contre ses essais par son montage (témoins : sans mutation, 137 essais passent ; import cassé, échec). Prédictions écrites avant le passage : huit justes sur huit. **Trois tuées sur huit.**

| n° | module | ce que la mutation casse | sort |
|---|---|---|---|
| c1 | fabrique | V0 : bruit par jeton commun à tous les membres | **survit** |
| c2 | fabrique | V0 : le sur-saboteur n'a plus la loi des deux autres | **survit** |
| c3 | fabrique | E2a : un produit nul n'est plus « non positif » | tuée (`test_verites_engagees`) |
| c4 | fabrique | V7, premier cas : table dans l'arbre, hors de l'inventaire | **survit** |
| c5 | fabrique | V9 : le saboteur porte une part sur ĝ | tuée (`test_ecart_qui_disparait_a_poussee_egale`) |
| c6 | juge | V10 : issue D ou C exigée à 95 % au lieu de 99 % | **survit** |
| c7 | juge | V3 : une issue D sans motif compte | **survit** |
| c8 | juge | V0 : la règle « contraire » compte les « séparé » | tuée (`test_juge_bornes_au_plus`) |

Les cinq survivantes demandent cinq essais, à écrire avec les couples : (c1) dans V0, la différence de deux membres, jeton par jeton, a la variance de deux bruits indépendants ; (c2) dans V0, les trois membres ont le même écart type de statistique d'une famille à l'autre ; (c4) la table du premier cas est dans l'inventaire ; (c6) dans V10, une issue D rendue à 95 % manque la règle du nœud 6, à 99 % la passe ; (c7) dans V3, une issue D sans motif ne compte pas. Résultats : `resultats-mutations-contre-lecture-v1.json`.

## 8. Les essais du développeur à reprendre avec les couples

Joués contre la copie corrigée, ses essais donnent : @@ESSAIS@@

Ces échecs sont attendus : ils portent sur les défauts mêmes que les couples changent (sel de 32 signes, « table sha256 », six lignes, garde factice). À reprendre par le développeur : la garde factice (dix lignes, engagement « sha256 », empreinte canonique), `test_arbre_conforme`, `test_v7_quatre_refus`, `test_v7_deuxieme_cas_deux_variantes`, `test_options_de_l_agent_de_l_epreuve` (sa ligne supplémentaire `SCELLEMENT-B5F` est maintenant une des dix), `test_parametres_et_ecrasement`, le programme « qui rend la vérité » (ses refus doivent porter le motif du programme), et deux essais d'égalité avec `engagement_v1` et `manifeste` pour les trois règles recopiées (`noms_opaques`, `_octets_table`, `partition_gelee`). Les mutations f09 à f11, f30 et j10 de son passage visent des textes que les couples changent : à récrire.

## 9. Point 6 — Ce qui menace le gel

1. **La fabrique, le juge et leurs essais sont dans l'arbre gelé.** L'arbre gelé est tout le dépôt hors `prereg`, `brouillons`, `registres`, `docs`, `diag`, `runs`, `donnees`, `livrables`, `papiers`, `traces` et `CLAUDE.md` : `src/` et `tests/` y sont. Après le commit de `CODE-LECTURE-B5F`, tout changement de la fabrique, du juge ou de leurs essais, et tout fichier non suivi sous `src/`, fait refuser l'ouverture réelle (« code joué différent de celui de CODE-LECTURE-B5F »). La clé ne se réinscrit pas (une clé en double arrête). **Les dix-neuf couples et la reprise des essais doivent donc être commis avant ce commit.** Le traducteur reste sous `docs/`, hors de l'arbre gelé.
2. **Aucun monde n'a passé la vraie garde.** Mes couples sont vérifiés contre des règles recopiées. Si un septième défaut de raccord m'a échappé, il ne se verra qu'après le gel, quand il sera trop tard pour toucher à la fabrique sans regeler. **Recommandation, à trancher par la mère** : avant le gel, un essai de raccord — un monde sain et les six refus de V7, sous une entropie qui ne servira pas à l'épreuve, par un agent qui ne tient aucun des trois rôles, en ne regardant que « accepté » ou le motif du refus. Ce n'est pas l'épreuve du point 11.
3. **Ce qui dépend du gel est un paramètre, non du code**, à condition de le régler : `empreinte_lecture` doit être l'empreinte du fichier gelé (sinon tout monde est refusé au point 10 de la liste d'arrêt). Le fichier des paramètres vit hors de `src/`.
4. **Trois règles recopiées, des phrases reconnues.** La fabrique recopie le pli gelé, les noms opaques et la forme canonique de la table ; le juge corrigé reconnaît quatre fragments de refus ; le traducteur reconnaît neuf phrases du programme. Tout changement du programme avant le gel qui touche l'un d'eux les désaligne. En particulier, la question laissée à la mère par le schéma du résultat (section 3 : refus sans résultat, ou issue NI écrite pour une garde) : si elle est tranchée pour « NI écrite », le traducteur et la règle des refus de V7 sont à reprendre.
5. **Rien d'autre ne dépend d'un état qui change** : ni le registre réel, ni les tâches réelles, ni l'entropie réelle, ni `diag/`. La commande `monde` du programme, sans `--racine`, ne lit pas git. La version de numpy est écrite dans les vérités : même environnement à l'engagement et au passage.
6. **Hors de mon mandat, vu en passant** : le point 11 prévoit qu'une règle manquée se corrige par un erratum du programme, puis que l'épreuve se rejoue. Or le registre n'admet qu'une ligne `CODE-LECTURE-B5F` et qu'une ligne `EPREUVE-B5F`. Ce chemin est à écrire avant d'en avoir besoin.

## 10. Ce qui va à la mère

1. Faire appliquer les dix-neuf couples et reprendre les essais (développeur), puis me rendre la main pour la vérification des corrections.
2. Trancher l'essai de raccord avant le gel (section 9, point 2). Recommandation : le faire. Confiance : 0,8.
3. Dire où s'engage l'empreinte des vérités (section 6).
4. Dire sous quelle entropie se joue le premier passage (section 6).
5. Savoir que V12 est partagé en deux signes (section 3), et que le saboteur de V4 est à −1,5.

## 11. Mes fichiers

Dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/outils-contre-lecture-fabrique-mondes-v1/`, chacun scellé par son compagnon :
- `couples_corrections_v1.py` : les dix-neuf couples (données) ;
- `verifier_couples_v1.py` et `resultats-verification-couples-v1.json` : chaque « avant » trouvé une fois ; copie corrigée ; dix mondes confrontés aux règles recopiées de la garde (état d'origine : aucun conforme ; copie corrigée : dix sur dix) ; juge d'origine et juge corrigé sur cinq programmes de ma fabrication ; essais du développeur sur la copie ;
- `mutations_contre_lecture_v1.py` et `resultats-mutations-contre-lecture-v1.json` ;
- `traducteur_resultat_vers_rendu_v1.py` ;
- `assembler_rapport_v1.py` et `corps-contre-lecture-fabrique-mondes-v1.md` : le corps de ce texte, auquel l'outil ajoute l'annexe.

Temporaires sous `/dev/shm/b5f-contre-lecture-fabrique-v1`, effacés à la fin par ce chemin.
