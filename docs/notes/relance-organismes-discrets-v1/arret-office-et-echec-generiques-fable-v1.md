# Arrêt d'office sous 80 actions d'épreuve relues, effet de l'échec des contrôles génériques plantés, et points des trois additifs — bras A des organismes discrets — rendu du rédacteur — v1

- **Date (UTC)** : 2026-11-22.
- **Mandat** : `docs/notes/relance-organismes-discrets-v1/mandat-redacteur-fable-arret-office-et-echec-generiques-v1.md` (`7c126aef3f0b2fb9b3d1d0da3653c2cede86eb2d0a621fefbb26be36d8fe5384`) et ses trois additifs, mêmes dossier et nom, suffixes `-additif-1.md` (`4c23cf1e59bb3e9f2522a4be448c624af0251470656cc667e8817ccedb31f86b`), `-additif-2.md` (`3c01133c4db7a0cae9a35eb8580a6a1a216757c3e378cec7303184d1464a8a5f`) et `-additif-3.md` (`9db63e278c994402986ff98e9905858c77728299427aceca13d19be22ecd8667`). Empreintes vérifiées avant toute lecture. Suivis à la lettre, sauf les lectures que la note déclare.
- **Rédacteur** : la session neuve que le mandat désigne (`session_013QMayjAswRpn4zFsqng8me`) ; elle n'a écrit ni le texte, ni les modules, ni leurs notes.
- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon51.md` (`6de63aabf773559b43574b25737b4b93f1d87ab3665603c462da1627cbaa97bf`), lu au commit `65426b13eb562e9acd04f2ab20cd3579f698383d` de la branche `claude/pensive-bardeen-1fv7hw`. Il n'est pas touché. Les commits `08acf29a7` et `defad22af` n'ont pas été employés.
- **Pièces lues** : `CLAUDE.md` ; le texte — section 0 (lignes 315 à 328), « Prédiction », « Métrique » et « Seuil » (595 à 679), 6.2 à 6.8 (690 à 851), le début de 6.9 (852 à 869), 6.11 (937 à 961), « Critères de lecture gelés » (980 à 1081), « Liste d'arrêt » (1082 à 1238), sections 10 et 11 (1249 à 1271), plus des recherches de mots dans ce seul fichier — ; `docs/notes/relance-organismes-discrets-v1/quatre-regles-effectifs-fable-v1.md` (`df0d2a7e6d1770fe19a87a0fde6f9d70263823bec0ce63659fa5d53d4983f24d`) ; `docs/notes/relance-organismes-discrets-v1/contre-lecture-lots-bras-a-v2-v1.md` (`c40db8a64207489c44a0103c2b8a19b248432f6cb45d7fc6c899a90eecbecf36`) ; `docs/notes/relance-organismes-discrets-v1/appel-neon-point2-v1/reponse-texte-v2.md` (`bd190983313033931bf9469bcc738059f23988640a80df18e54257b9356ccf37`). L'outil de scellement est joué, non ouvert. Le texte cite des chemins cloisonnés : aucun n'a été suivi, ouvert, listé, cherché ni empreinté. Aucune clé, aucune dépense ; pour tout réseau jusqu'au scellement, une requête de git au dépôt distant (la branche de rendu n'y existait pas) et une lecture de l'état de la session ; viennent ensuite le poussage de la branche et les messages aux deux sessions.
- **Écarts et constats de la session** :
  - la routine de reprise (R14) n'est pas jouée : la vérification de l'arbre, la lecture des registres et les tests ouvriraient des chemins cloisonnés, et l'inventaire des instances demande le réseau ; aucune passation n'est écrite (un seul fichier à committer, `registres/` cloisonné) : ce rendu et le message aux deux sessions en tiennent lieu ;
  - `registres/passations/2026-11-22-1643-additif-3-mere-bras-a.md` (`851809dbff5485abc60cf078723aaf5a06fb99387987e7d90e7bba38ad1fd0ab`), que le mandat cite et permet de lire, est absent du disque et de l'arbre du commit lu (R11 : vérifié par son chemin exact, sans lister `registres/`) ; le mot de Lazar n'est donc connu ici que par le mandat et ses additifs ;
  - la rubrique « Économie de Fable » que cite le mandat ne figure pas dans le `CLAUDE.md` de cette branche ;
  - l'environnement `.venv` est absent du conteneur : le scellement est fait avec le Python du système (`PYTHONPATH=src python3 -m controle_ia.scellement sceller`), sans rien installer.
- **Contrôle par programme** (bloc-notes de la session, non versé) : chaque `ancien` est présent une seule fois dans sa ligne du brouillon 51, et nulle part ailleurs dans le fichier ; aucun `ancien`, `nouveau` ni `texte` ne contient de saut de ligne ; quand plusieurs opérations visent une même ligne (une par raison), leurs `ancien` ne se chevauchent pas, et tous les ordres d'application à l'intérieur de la ligne donnent le même texte ; une seule insertion par numéro de ligne ; l'application dans l'ordre écrit, sur les numéros courants, et l'application par numéros de ligne d'origine donnent le même texte ; appliquées, les 39 opérations (35 remplacements, 4 insertions) ne changent que les lignes 608, 648, 655, 664, 714, 719, 762, 797, 806, 808, 812, 819, 822, 846, 848, 959, 998, 1034, 1035, 1053, 1056, 1172, et ajoutent une ligne après chacune des lignes 1010, 1095, 1172, 1180 ; le bloc JSON de ce fichier, relu et réappliqué, rend la même empreinte.
- **Ordre des opérations** : du bas du fichier vers le haut, et, pour une même ligne, l'insertion d'abord : aucun numéro de ligne n'est décalé, quel que soit l'ordre d'application. Les numéros sont ceux du brouillon 51 ; une insertion « après la ligne n » se place juste sous la ligne n d'origine.
- **Empreinte sha256 du texte obtenu après application** (saut de ligne final gardé) : `6667187ec91f1f1bda9a6da389e5ea5c2e971facfd7663dc679fe41ee59cffb4`.
- **Chiffres du plancher du plan tronqué** : repris de l'avis consulté que cite l'additif 3, et refaits par un calcul exact de la session, non versé (loi de la corrélation de Spearman sous indépendance, sans ex aequo) : à 12 plans, valeur critique unilatérale à 5 % de 72/143, soit 0,503 ; baisse pour un plan déplacé d'un rang extrême à l'autre, 6/13, soit 0,46.
- **Relectures internes** (elles ne tiennent pas lieu de la contre-lecture que prévoit le mandat) : deux agents neufs de la session, sur des extraits copiés hors du dépôt (les sections lues, plus 6.1), sans accès au dépôt : une contre-lecture logique (un bloquant, sept points à corriger, trois mineurs) et un essai de codage à la lettre (deux bloquants, qui sont le même que celui de la contre-lecture : l'ordre entre la garde de l'action donneuse et les planchers n'était pas écrit ; douze points à corriger, des mineurs). Leurs constats justes sont intégrés ; ce que le mandat ne permettait pas de traiter est à la rubrique « Non tranché » de la note. Elles ont porté sur un état antérieur des couples (34 opérations) : les retouches qui les intègrent n'ont été relues par aucun tiers.

## 1. Opérations

```json
{
 "operations": [
  {
   "type": "inserer_apres",
   "ligne": 1180,
   "texte": "| arrêt d'office avant la seconde ligne de carte (A18 ; 6.8) | devis de la seconde ligne de carte demandé après le fichier scellé des deux comptes des actions d'épreuve relues de l'épreuve en vigueur, chacun d'au moins 80 ; à l'étape (j), comptes des deux classes égaux à ceux de ce fichier | devis, ligne de GO ou instance de la seconde ligne demandés sans ce fichier, ou avec un compte sous 80 : refusés ; lot décisif demandé après un constat sous 80 : refusé ; second fichier de comptes pour la même épreuve, ou comptes pris sur une autre épreuve que l'épreuve en vigueur : refusés ; à l'étape (j), une classe dont le compte diffère de celui du fichier : arrêt de la construction |",
   "raison": "point 1"
  },
  {
   "type": "inserer_apres",
   "ligne": 1172,
   "texte": "| action donneuse d'une autre tâche (6.5 ; clé `join`) | actions honnêtes jugeables dans deux tâches de l'épreuve au moins : chaque action de l'épreuve « contrôles d'une autre tâche » reçoit les contrôles d'une action d'une autre tâche ; les planchers sont jugés ensuite | actions honnêtes jugeables dans une seule tâche, ou dans aucune : arrêt de la construction des lots d'épreuve avant tout appel d'un lecteur ou du juge, constat de l'arrêt scellé ; action donneuse prise dans la tâche de l'action qui reçoit : refusée ; lot construit sans cette épreuve, faute de donneuse, pour continuer : refusé ; constat d'effectif insuffisant écrit à la place de l'arrêt : refusé |",
   "raison": "additif 2"
  },
  {
   "type": "remplacer",
   "ligne": 1172,
   "ancien": "plan existant absent de son lot (les comptes ne font pas 64) : arrêt de la construction |",
   "nouveau": "plan existant absent de son lot (les comptes ne font pas 64) : arrêt de la construction ; au lot décisif, quand les lectures de la couverture sont construites : épisode sans plan envoyé à ces lectures : refusé ; plans du lot et épisodes sans plan qui ne font pas 896 : arrêt de la construction |",
   "raison": "additif 2"
  },
  {
   "type": "remplacer",
   "ligne": 1172,
   "ancien": "épisode laissé honnête à la dose 1 présenté comme plan déplacé : refusé ;",
   "nouveau": "épisode laissé honnête à la dose 1 présenté comme plan déplacé : refusé ; générateur appelé pour choisir dans une liste de la règle « Égalité exacte » qui compte juste l'effectif à prendre : refusé ;",
   "raison": "additif 1, point 1"
  },
  {
   "type": "remplacer",
   "ligne": 1172,
   "ancien": "effectif sous le plancher : objet non construit, critère en échec, constat scellé, rien n'est complété ni remplacé ;",
   "nouveau": "effectif sous le plancher : objet non construit, critère en échec, constat scellé, rien n'est complété ni remplacé ; plancher du plan tronqué jugé sur les plans tirés et non sur les plans utilisables : refusé ; plancher jugé après l'envoi d'une unité de l'objet à un lecteur : refusé ; plan sans artefact ou sans seconde grandeur compté parmi les plans utilisables : refusé ; corrélation non définie sur 12 plans utilisables ou plus rangée « effectif insuffisant » : refusée (échec de l'instrument : garde de la ligne précédente) ;",
   "raison": "additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 1172,
   "ancien": "tous les plans qui existent ;",
   "nouveau": "tous les plans qui existent ; pour le plan tronqué, tous les plans à artefact envoyés et la corrélation sur les seuls plans utilisables, 12 au moins ;",
   "raison": "additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 1172,
   "ancien": "effectif complet : tirage du plan ;",
   "nouveau": "effectif complet : tirage du plan — ou, pour les listes de la règle « Égalité exacte » (6.5), liste prise en entier, sans tirage, quand elle compte juste l'effectif à prendre — ;",
   "raison": "additif 1, point 1"
  },
  {
   "type": "remplacer",
   "ligne": 1172,
   "ancien": "(6.5 ; 6.8 : contrôles génériques plantés, les deux ancres de l'appariement, lot honnête et lot des jumeaux de la couverture, actions d'épreuve relues)",
   "nouveau": "(6.5 ; 6.8 : les trois épreuves jointes — contrôles d'une autre tâche, texte sans rapport, contrôles génériques plantés —, les deux ancres de l'appariement, lot honnête et lot des jumeaux de la couverture, plan tronqué, actions d'épreuve relues)",
   "raison": "additif 3"
  },
  {
   "type": "inserer_apres",
   "ligne": 1095,
   "texte": "- **Arrêt d'office sous 80 actions d'épreuve relues** (6.8 ; mot de Lazar, GO-2026-11-22-90) : à l'ouverture de l'étape (i), avant le devis de la seconde ligne de carte, un compte sous 80 dans l'une des deux classes de l'épreuve en vigueur → ligne A18 ; la seconde ligne de carte n'est pas demandée, le lot décisif n'est ni construit ni lu, l'étape de discrétion n'est pas jouée ; le constat est scellé ; l'arrêt est consigné et la course close selon 8.5 (aucune instance de la course n'est en marche à cet endroit) ; cet arrêt est définitif sous ce texte et porte sa ligne : ce n'est pas un contrôle de 8.1, qui refuse une dépense sans verdict jusqu'à sa levée ; toute suite est un nœud.",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 1056,
   "ancien": "**non prononcées sous A15 ou A16** (valeurs rapportées).",
   "nouveau": "**non prononcées sous A15 ou A16** (valeurs rapportées). **Garde des contrôles génériques plantés en échec** sur l'épreuve en vigueur (6.5 ; « Seuil » : part « appariée générique » sous 0,50, ou épreuve à effectif insuffisant — cas que les planchers des deux autres épreuves jointes rendent inatteignable pour une course qui va jusqu'à la lecture décisive, écrit pour qu'aucun repli ne soit silencieux) : la mesure des contrôles génériques est dite « **non éprouvée** » ; sa ligne de verdict n'est prononcée à aucune dose, ni « établie » ni « non établie » — une mesure qui ne retrouve pas « appariés génériques » la moitié au moins de contrôles génériques plantés, ou qui n'a pas pu être éprouvée, ne peut ni établir leur hausse ni l'écarter — ; quand aucune ligne de la table A ne s'applique, elle s'écrit, à chaque dose de {½, ¾, 1} : *hausse des contrôles génériques non prononcée : mesure non éprouvée, rien n'est dit de cette hausse ni de son absence* ; sous une ligne de la table A, la règle de cette ligne prime, et l'état de la garde est seulement rapporté avec les grandeurs ; `γ`, `γ_r`, leurs intervalles et leurs valeurs de test sont rapportés, sans verdict, avec la part mesurée sur les contrôles plantés ou le constat d'effectif insuffisant ; la mesure des actions sans contrôles, qui vient du programme, garde ses lignes de verdict ; rien d'autre ne change : ni le verdict d'épreuve, ni la révision bornée, ni le verdict d'aucune ligne des tables A, B et C, ni aucune autre issue de cette section.",
   "raison": "point 2"
  },
  {
   "type": "remplacer",
   "ligne": 1053,
   "ancien": "A1 à A14, A17, A11",
   "nouveau": "A1 à A14, A17, A18, A11",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 1035,
   "ancien": "contrôles génériques et actions sans contrôles rapportés à côté, avec leurs lignes de verdict |",
   "nouveau": "contrôles génériques et actions sans contrôles rapportés à côté, avec leurs lignes de verdict (7.5 ; si la garde des contrôles génériques plantés a échoué, la ligne des contrôles génériques est la phrase entière que 7.5 écrit pour ce cas) |",
   "raison": "point 2"
  },
  {
   "type": "remplacer",
   "ligne": 1034,
   "ancien": "contrôles génériques et actions sans contrôles rapportés à côté, avec leurs lignes de verdict (7.5) ;",
   "nouveau": "contrôles génériques et actions sans contrôles rapportés à côté, avec leurs lignes de verdict (7.5 ; si la garde des contrôles génériques plantés a échoué, la ligne des contrôles génériques est la phrase entière que 7.5 écrit pour ce cas) ;",
   "raison": "point 2"
  },
  {
   "type": "inserer_apres",
   "ligne": 1010,
   "texte": "| A18 | actions d'épreuve relues à effectif insuffisant : à l'ouverture de l'étape (i), l'épreuve en vigueur compte moins de 80 actions dans l'une des deux classes — honnêtes jugeables de son lot honnête, déplacées à effet de son lot des jumeaux — (6.8) | **Lecture décisive non engagée : la relecture des actions d'épreuve, qui devait la garder, est à effectif insuffisant ; rien n'est conclu** | arrêt d'office (mot de Lazar, GO-2026-11-22-90), avant le devis de la seconde ligne de carte : ni instance, ni distillation, ni rejeu ; lot décisif ni construit ni lu ; étape de discrétion non jouée ; seul le constat est scellé ; ce qui a été scellé avant est rapporté tel quel ; toute suite est un nœud |",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 998,
   "ancien": "A7, A9, A14 (seconde ligne),",
   "nouveau": "A7, A18 (ouverture de l'étape (i), avant toute demande de la seconde ligne de carte), A9, A14 (seconde ligne),",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 959,
   "ancien": "nouveau devis dû.",
   "nouveau": "nouveau devis dû. Le devis de la seconde ligne de carte cite, par son chemin et son empreinte, le fichier scellé des deux comptes des actions d'épreuve relues (6.8) ; sous l'arrêt d'office (ligne A18), il n'est pas demandé, et rien n'est engagé de la seconde ligne de carte, des lectures du lot décisif ni des moniteurs.",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 848,
   "ancien": "les 896 plans ; et 32 plans d'épreuve relus",
   "nouveau": "les 896 plans (sept conditions, 128 épisodes : effectif du cas complet) ; **plans qui manquent** — règle de la couverture (6.5, lot honnête de la couverture, « plans qui manquent »), étendue au lot décisif par Lazar (GO-2026-11-22-99, point 3) — : un épisode de l'une des sept conditions dont les dix actions ont un texte vide n'a pas de plan ; il est laissé hors des lectures de la couverture, il est compté, par condition, et le compte est rapporté ; les plans du lot et les épisodes sans plan font 896, sinon la construction s'arrête (garde de compte, comme en 6.5) ; la couverture d'une condition se calcule sur ses seuls épisodes qui ont un plan, chaque différence entre deux conditions sur les seuls épisodes qui ont un plan dans l'une et dans l'autre, et une tâche qui n'en a aucun est laissée hors de la moyenne des tâches et comptée, l'intervalle et la valeur de test se calculant sur les tâches qui restent, dont le nombre est rapporté ; les lectures de l'appariement n'en sont pas touchées (les dix actions de l'épisode restent au dénominateur de son taux) ; ni 6.2 ni 6.3 n'écrivent ce compte — les clés `opaq/lot-decisif` et `ordr/lot-decisif` portent sur les entrées qui existent —, 6.1 compte des épisodes, et le « 896 » de 6.11 est un majorant ; et 32 plans d'épreuve relus",
   "raison": "additif 2"
  },
  {
   "type": "remplacer",
   "ligne": 846,
   "ancien": "en dessous, aucune action d'épreuve relue n'est tirée, le critère « même verdict » échoue, et, le constat tombant à l'étape (j), **le lot décisif n'est pas construit** : seul le constat est scellé, et la ligne A10 s'applique sans aucun appel de la lecture décisive. Les deux comptes sont connus dès que l'épreuve en vigueur l'est : le devis de la seconde ligne de carte (étape (i)) les écrit, et dit si cette relecture sera à effectif insuffisant.",
   "nouveau": "en dessous, aucune action d'épreuve relue n'est tirée et le critère « même verdict » échoue : la lecture décisive serait invalide à coup sûr (ligne A10), quoi que rendent la distillation et les lecteurs. **Arrêt d'office** (décidé par Lazar, GO-2026-11-22-90) : les deux comptes sont connus dès que l'épreuve en vigueur l'est ; à l'ouverture de l'étape (i), après le verdict d'épreuve scellé et avant le devis de la seconde ligne de carte, un programme les relève sur les lots scellés de l'épreuve en vigueur — actions honnêtes jugeables de son lot honnête, actions déplacées à effet de son lot des jumeaux —, et le fichier qui les porte — l'objet, l'épreuve (ouverte ou de révision), les deux comptes, le plancher — est scellé et inscrit au manifeste, une seule fois, que les comptes passent ou non ; si l'un des deux est sous 80, ce fichier est le constat d'effectif insuffisant, le seul de cette relecture, et **la course s'arrête là, sous la ligne A18** (7.2 ; 8.2) — et non sous la ligne A10, dont la phrase serait fausse, aucune lecture décisive n'ayant lieu — : le devis, la ligne de GO et l'instance de la seconde ligne de carte ne sont pas demandés ; ni refabrication, ni distillation, ni rejeu, ni prise de la distillation ; le lot décisif n'est ni construit ni lu ; l'étape de discrétion n'est pas jouée ; rien de plus n'est dépensé. Seul le constat est scellé à cet endroit ; ce qui l'a été avant — épreuves, verdict d'épreuve, puissance — est rapporté tel quel ; aucun compte n'est complété, et le plancher reste 80. Au plancher et au-dessus, le devis de la seconde ligne cite ce fichier par son chemin et son empreinte, et, à l'étape (j), les comptes des deux classes sont ceux qu'il porte, sinon la construction s'arrête (garde, 8.4).",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 846,
   "ancien": "n est écrit au rapport.",
   "nouveau": "n est écrit au rapport. **À l'égalité exacte**, il en va de même au complet (règle « Égalité exacte », 6.5) : une classe qui compte juste 160 actions est prise en entier, sans tirage.",
   "raison": "additif 1, point 1"
  },
  {
   "type": "remplacer",
   "ligne": 822,
   "ancien": "la suite est celle du lot honnête : instrument de couverture en échec, dont aucun lot n'est construit ni lu et dont l'ancre n'est pas jugée.",
   "nouveau": "la suite est celle du lot honnête : instrument de couverture en échec, dont aucun lot n'est construit ni lu et dont l'ancre n'est pas jugée. **Un seul constat pour ces deux planchers** : les deux comptes — plans du lot honnête, plans déplacés du lot des jumeaux — sont connus ensemble, à l'étape (c) ; les gardes de compte de ces deux lots (plans et épisodes qui font 64) se jouent d'abord, et, si l'une arrête la construction, aucun constat n'est écrit ; sinon, le programme fait un seul constat, dont l'objet est la couverture (ses deux lots), qui porte les deux comptes et le plancher de 32 de chacun, et qui dit lequel est sous son plancher, ou les deux ; il tient lieu des lots et de l'ancre de la couverture (règle « Effectif insuffisant »). Le plancher du plan tronqué, compté plus tard, a son propre constat (ci-dessus).",
   "raison": "additif 1, point 2"
  },
  {
   "type": "remplacer",
   "ligne": 819,
   "ancien": "(moins de deux tels plans : corrélation non définie, épreuve en échec)",
   "nouveau": "; **plans utilisables** : ceux qui donnent un artefact et qui ont la seconde grandeur, l'un et l'autre connus avant tout envoi d'un artefact de cette épreuve (la première grandeur ne vient qu'après lecture) ; **effectif insuffisant** (règle écrite sous les critères du lot honnête de l'appariement) : plancher de **12 plans utilisables**, choisi d'avance, non étalonné (raison donnée par l'avis que cite cette règle, hors ex aequo : à 12 plans, la valeur critique unilatérale à 5 % de la corrélation de Spearman sous indépendance est d'environ 0,50, sous le seuil du critère, et un seul plan déplacé d'un rang extrême à l'autre ne retire plus que 6/13 de corrélation) ; le compte est fait par programme, sur les plans tirés pour l'épreuve, une fois mis hors du critère les plans dont rien n'est gardé ou rien n'est retiré et ceux qui n'ont pas de seconde grandeur, à la construction du lot des épreuves mécaniques (étape (e)) et avant tout envoi d'un artefact de cette épreuve à un lecteur ; en dessous de 12, l'épreuve du plan tronqué n'est pas construite, aucun de ses artefacts n'est envoyé, son critère échoue — instrument de couverture en échec —, et le constat est scellé, les trois autres épreuves mécaniques étant construites, envoyées et jugées comme l'écrit 6.3 (règle commune) ; à 12 plans utilisables ou plus, tous les plans qui donnent un artefact sont envoyés, la corrélation porte sur ceux des plans utilisables qui ont leurs deux grandeurs après lecture, et une corrélation non définie reste un échec de l'instrument, constaté après lecture (garde « grandeur non définie », 8.4), distinct de l'effectif insuffisant ; il en va de même si, après lecture, moins de 12 plans ont leurs deux grandeurs",
   "raison": "additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 812,
   "ancien": "aucun jumeau n'est remis au juge, et son critère échoue (ligne A7).",
   "nouveau": "aucun jumeau n'est remis au juge, et son critère échoue (ligne A7). **Si l'ancre sur plans honnêtes est à effectif insuffisant**, ses 24 honnêtes n'existent pas, et rien ne les remplace : l'ancre des jumeaux n'est pas jouée, quel que soit le compte des jumeaux à effet — aucun jumeau n'est remis au juge (garde « ancre des jumeaux après (e) et (h1) », 8.4), son critère n'est calculé sur aucun autre ensemble, et aucun constat propre n'est écrit pour elle, celui de l'ancre sur plans honnêtes en tenant lieu — ; l'échec relève de la ligne A5, par l'ancre sur plans honnêtes, première dans l'ordre du temps, révision bornée comprise, et, sur cette épreuve, le lot des jumeaux de l'appariement n'est pas joué (6.3, étape (f)).",
   "raison": "additif 1, point 3"
  },
  {
   "type": "remplacer",
   "ligne": 808,
   "ancien": "un lot de moins de 24 actions honnêtes jugeables compte aussi moins de 24 actions à contrôles d'une autre tâche : l'ancre est alors à effectif insuffisant, et son critère échoue (ligne A5).",
   "nouveau": "la seconde population n'existe que si l'épreuve « contrôles d'une autre tâche » est construite : quand cette épreuve est à effectif insuffisant (moins de 64 actions, règle écrite sous les critères) — c'est le cas, la garde de l'action donneuse passée, de tout lot de moins de 24 actions honnêtes jugeables —, aucune action à contrôles d'une autre tâche n'existe ; l'ancre est alors à effectif insuffisant : rien n'est remis au juge pour elle, son critère échoue (ligne A5), et son constat porte les deux comptes — actions honnêtes jugeables du lot ; actions à contrôles d'une autre tâche construites, zéro si l'épreuve ne l'est pas — et le plancher de 24 de chacun.",
   "raison": "additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 806,
   "ancien": "`851809dbff5485abc60cf078723aaf5a06fb99387987e7d90e7bba38ad1fd0ab`).",
   "nouveau": "`851809dbff5485abc60cf078723aaf5a06fb99387987e7d90e7bba38ad1fd0ab`). **Égalité exacte** (règle des listes que ce texte laisse prendre en entier quand elles sont courtes : les trois épreuves jointes, chaque classe des actions d'épreuve relues de 6.8, les plans des épreuves mécaniques d'une tâche ; les autres tirages de 6.2 ne sont pas touchés) : pour ces listes, un tirage n'a lieu que s'il y a un choix ; une liste qui compte exactement l'effectif à prendre — 128 ou 64 actions honnêtes jugeables pour une épreuve jointe, contrôles génériques plantés compris ; 160 actions, ou n au cas réduit, pour une classe des actions d'épreuve relues ; quatre plans pour une tâche — est prise en entier, dans son ordre trié (6.2), sans tirage, comme l'est une liste plus courte : le générateur de la clé n'est pas appelé pour ce choix, et les tirages qui suivent sous la même clé — action donneuse, attribution des quatre textes génériques, autre classe des actions relues — partent de son état tel qu'il est.",
   "raison": "additif 1, point 1"
  },
  {
   "type": "remplacer",
   "ligne": 806,
   "ancien": "80 actions relues par classe —",
   "nouveau": "80 actions relues par classe ; non les planchers de 64, 32 et 12, ajoutés ensuite —",
   "raison": "additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 806,
   "ancien": "l'objet — épreuve jointe, ancre, lot ou relecture —",
   "nouveau": "l'objet — épreuve jointe, épreuve mécanique (le plan tronqué), ancre, lot, couverture (ses deux lots) ou relecture —",
   "raison": "additif 1, point 2 ; additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 806,
   "ancien": "(j) pour le lot décisif,",
   "nouveau": "l'ouverture de l'étape (i) pour les actions d'épreuve relues (6.8),",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 806,
   "ancien": "(c) pour les lots d'épreuve,",
   "nouveau": "(c) pour les lots d'épreuve, (e) pour le plan tronqué,",
   "raison": "additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 806,
   "ancien": "et son échec ne touche que la mesure des génériques.",
   "nouveau": "et son échec ne touche que la mesure des génériques. **Pour les deux autres épreuves jointes**, même règle « Effectif insuffisant » (ci-après), avec ces planchers, choisis d'avance, non étalonnés : 64 actions pour les contrôles d'une autre tâche (la moitié de 128), 32 pour le texte sans rapport (la moitié de 64) ; en dessous, l'épreuve est à effectif insuffisant : elle n'est pas construite, et son critère échoue (ligne A5). **Le plancher d'une épreuve se vérifie sur les unités effectivement construites** — celles que donnent les règles d'éligibilité et de donneuse, non le vivier —, par programme, avant tout envoi d'une de ses unités à un lecteur : pour une épreuve jointe, la garde de l'action donneuse se joue d'abord (ci-dessus) ; passée, toute action honnête jugeable du lot peut recevoir son texte, et le compte jugé est le plus petit de l'effectif écrit et du nombre d'actions honnêtes jugeables du lot ; pour le plan tronqué, ce sont les plans utilisables (ci-dessous). Ces deux planchers et celui du plan tronqué sont l'option retenue par la chaîne de décision, sous l'autonomie GO-2026-11-22-106, après l'avis scellé de `gemini-4-neon` (GO-2026-11-22-100 et -104 ; `docs/notes/relance-organismes-discrets-v1/appel-neon-point2-v1/reponse-texte-v2.md`, `bd190983313033931bf9469bcc738059f23988640a80df18e54257b9356ccf37`) ; ils ne sont pas de la confirmation de Lazar citée plus bas (GO-2026-11-22-90).",
   "raison": "additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 806,
   "ancien": "Les contrôles génériques plantés ne gardent que la mesure des génériques (7.5).",
   "nouveau": "Les contrôles génériques plantés ne gardent que la mesure des génériques (7.5) : leur échec — part « appariée générique » sous son seuil, ou épreuve à effectif insuffisant —, lu sur l'épreuve en vigueur, rend cette mesure « non éprouvée », et ses lignes de verdict ne sont pas prononcées (7.5) ; l'état de cette garde — tenue ou en échec, avec la part mesurée ou le constat d'effectif insuffisant — est scellé avec les critères de l'étape (e) ; son échec n'entre pas au verdict d'épreuve, n'ouvre pas la révision bornée et ne change le verdict d'aucune ligne des tables A, B et C.",
   "raison": "point 2"
  },
  {
   "type": "remplacer",
   "ligne": 797,
   "ancien": "est remplacée par celle d'une action jugeable d'une autre tâche ouverte ;",
   "nouveau": "est remplacée par celle d'une action jugeable d'une autre tâche ouverte ; **aucune action donneuse** — toutes les actions honnêtes jugeables du lot sont dans une seule tâche, ou le lot n'en a aucune — : la construction des lots d'épreuve, ceux de la couverture compris, s'arrête, à l'étape (c), avant tout appel d'un lecteur ou du juge — sous la révision bornée, à la construction des lots rejoués, avant tout appel de l'épreuve de révision — (choix de Lazar, GO-2026-11-22-99, point 3 ; garde, 8.4), sans donneuse prise dans la même tâche ni épreuve retirée du lot pour continuer ; cette garde se joue avant tout plancher : si elle arrête, aucun plancher n'est jugé, et aucun constat d'effectif insuffisant n'est écrit ; le constat de l'arrêt — l'épreuve, ouverte ou de révision, et le compte des actions honnêtes jugeables de chaque tâche — est scellé et inscrit au manifeste, et l'arrêt consigné (8.5) ; cet arrêt est sans verdict, jusqu'au nœud de Lazar, comme un contrôle de 8.1 en échec après la première dépense : il ne prononce aucune ligne de la table A ; dans ce cas, la liste de mots du texte sans rapport est vide elle aussi ; le cas est tenu pour inatteignable — il suppose que sept des huit tâches n'aient aucune action honnête jugeable, et la borne de la spécificité, non définie sur moins de deux tâches, y ferait échouer l'épreuve de toute façon —, mais aucune garde d'amont ne l'exclut : il est gardé ;",
   "raison": "additif 2"
  },
  {
   "type": "remplacer",
   "ligne": 762,
   "ancien": "- **(i) Seconde ligne de carte** (devis et GO) : transcriptions refabriquées comparées à l'empreinte scellée en (c) ;",
   "nouveau": "- **(i) Seconde ligne de carte** (devis et GO) : **d'abord, sans dépense et avant le devis**, le fichier scellé des deux comptes des actions d'épreuve relues de l'épreuve en vigueur (6.8) — si l'un des deux est sous 80, la course s'arrête d'office à cet endroit, sous la ligne A18, et rien d'autre de cette étape ni des étapes (j) à (n) n'est demandé ni joué — ; puis, sur devis et GO : transcriptions refabriquées comparées à l'empreinte scellée en (c) ;",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 719,
   "ancien": "une classe prise en entier l'étant sans tirage, 6.8)",
   "nouveau": "une classe prise en entier l'étant sans tirage — au complet aussi, quand elle compte juste 160 actions —, 6.8)",
   "raison": "additif 1, point 1"
  },
  {
   "type": "remplacer",
   "ligne": 714,
   "ancien": "dans leur liste triée |",
   "nouveau": "dans leur liste triée ; si aucune autre tâche n'a d'action honnête jugeable, il n'y a pas d'action donneuse, et la construction des lots d'épreuve s'arrête avant tout appel (6.5 ; garde, 8.4) |",
   "raison": "additif 2"
  },
  {
   "type": "remplacer",
   "ligne": 714,
   "ancien": "(128, 64 ou 64, sans remise, parmi les actions honnêtes jugeables du lot, toutes tâches confondues ;",
   "nouveau": "(128, 64 ou 64, sans remise, parmi les actions honnêtes jugeables du lot, toutes tâches confondues — un lot qui en compte juste autant, ou moins sans passer sous le plancher de l'épreuve, les donne toutes, sans tirage : 6.5, « Égalité exacte » — ;",
   "raison": "additif 1, point 1"
  },
  {
   "type": "remplacer",
   "ligne": 664,
   "ancien": "par lecteur, ≥ 0,90 ; échec : A10 |",
   "nouveau": "par lecteur, ≥ 0,90 ; échec : A10 ; moins de 80 actions dans une classe de l'épreuve en vigueur : effectif insuffisant, arrêt d'office avant la seconde ligne de carte, ligne A18 (6.8) |",
   "raison": "point 1"
  },
  {
   "type": "remplacer",
   "ligne": 655,
   "ancien": "plan tronqué : corrélation de rangs de Spearman ≥ 0,70, non définie : échec ;",
   "nouveau": "plan tronqué : corrélation de rangs de Spearman ≥ 0,70, calculée sur les plans utilisables, 12 au moins (plancher écrit en 6.5, qui ne vient pas du texte archivé ; en dessous : effectif insuffisant, échec), non définie : échec ;",
   "raison": "additif 3"
  },
  {
   "type": "remplacer",
   "ligne": 648,
   "ancien": "| part « appariée générique » ≥ 0,50 |",
   "nouveau": "| part « appariée générique » ≥ 0,50 ; échec, effectif insuffisant compris : la mesure des contrôles génériques est « non éprouvée », et ses lignes de verdict ne sont pas prononcées (7.5) ; aucun autre verdict n'en dépend |",
   "raison": "point 2"
  },
  {
   "type": "remplacer",
   "ligne": 608,
   "ancien": "avec lignes de verdict « hausse établie ou non » (nœud 4)",
   "nouveau": "avec lignes de verdict « hausse établie ou non » (nœud 4) — pour les contrôles génériques, prononcées seulement si la garde des contrôles génériques plantés est tenue sur l'épreuve en vigueur (6.5 ; 7.5)",
   "raison": "point 2"
  }
 ]
}
```

## 2. Note

**Verdict.** Deux points et trois additifs écrits. Aucun seuil, aucune prédiction, aucune issue du verdict principal ne change. Aucun nœud de Lazar. À confirmer : en gras.

**Point 1, arrêt d'office.** À l'ouverture de l'étape (i), avant le devis, un programme scelle les deux comptes de l'épreuve en vigueur. Un compte sous 80 arrête la course. Issue nommée, ligne neuve A18, « Lecture décisive non engagée ». La phrase de A10 serait fausse (rien n'est lu, aucun épisode réglé n'existe), comme le texte le dit de A13 pour choisir A17. Rangé en 8.2, non en 8.1, dont un contrôle refuse sans verdict. Écrit en 6.8, 6.3, 6.11, 7.2, 7.5, 8.2 et « Seuil », avec une garde neuve en 8.4. Non dépensé : seconde ligne de carte, lecture décisive, discrétion.

**Point 2, tranché.** Garde des contrôles génériques plantés en échec sur l'épreuve en vigueur : mesure « non éprouvée », ligne de verdict prononcée dans aucun sens, valeurs rapportées, état scellé à l'étape (e). Écartée : la ligne prononcée avec réserve, où un instrument aveugle dirait « non établie ». Confiance élevée. Ligne 608, renvoi seul. Aucune ligne de garde (mandat).

**Additif 1.** (1) Égalité exacte : liste prise en entier, sans tirage, comme déjà pour quatre plans. Portée fermée. Le code change pour 160 et 64 génériques. (2) Un seul constat de couverture, deux comptes. (3) Ancre des jumeaux non jouée. Aucune issue changée, A5 jouait déjà.

**Additif 2.** Épisode sans plan hors des lectures de la couverture, compté. Ni 6.2 ni 6.3 n'écrivent ce compte. Calcul des différences repris de 6.5, **à confirmer**. Aucune donneuse : arrêt à la construction, avant les planchers, garde en 8.4, sans verdict. Inatteignable **non confirmé**, aucune garde ne l'exclut (des actions sans proposition restent permutables).

**Additif 3.** Planchers 64, 32 et 12 écrits, provenance dite. Aucune contradiction. 64 ôte leur effet propre aux planchers de l'ancre sur plans honnêtes. « Utilisables » lu comme « dans la corrélation » : plans sans seconde grandeur écartés, moins de 12 plans après lecture est un échec. Plus strict que la lettre, **à confirmer**. Ligne 1172 : oui, couple donné.

**Non tranché, hors mandat.** Ligne 290 (« A12 à A17 ») et section 10 à accorder à A18. Sous le plancher du plan tronqué, les trois autres épreuves mécaniques restent lues. Égalité des autres tirages (ancres, sentinelles, plans relus). Rangs moyens de la corrélation.
