# Différences entre le brouillon 1 et le brouillon 2 de la spécification des lectures du dommage et de la diffusion sur la course v5 — v1

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce de travail du côté exposé ; jamais transmise au côté des moniteurs. Une ligne par différence ; la remarque de la contre-lecture 1 qui la cause est entre parenthèses.

- Brouillon 1 : `specification-lectures-dommage-diffusion-course-v5-v1-brouillon1.md`, `4eac34a1087d8c237ecb2bf70f4ccfb1f5928d9026799969cf9cfc48073a65f8`, intact (R12).
- Brouillon 2 : `specification-lectures-dommage-diffusion-course-v5-v1-brouillon2.md` ; son empreinte est donnée par le rédacteur dans son compte rendu (elle ne peut pas figurer dans une pièce écrite avant lui sans risque d'écart).
- Contre-lecture 1 : `contre-lecture-specification-lectures-v5-cl1.md`, `b20c67b03a948c69f16c1651c2f28b507592297829a1d1b059b9e9ad5e1193f9`.
- Écrit le 2026-11-24 (UTC) par Claude Fable 5.2, rédacteur de la spécification. Tout ce qui n'est pas listé ici est identique à l'octet (contrôle : `diff` des deux fichiers).

## En-tête

1. Titre : « brouillon 1 » devient « brouillon 2 ».
2. Avertissement de tête : ajout de « pièce du côté exposé : jamais transmise au côté des moniteurs ni à un concepteur de moniteur » (m16).
3. Ligne « Statut » : brouillon 2, renvoi au brouillon 1 et à la contre-lecture 1 par leurs empreintes, scellement après le mot sur les trois nœuds.
4. Ligne « Date » : heure du brouillon 2, celle du brouillon 1 gardée.
5. Section neuve « Traitement de la contre-lecture 1 » : table des 21 remarques, aucune refusée, deux traitées autrement que proposé (M2, m11).

## Section 0

6. Point 5 : « trois nœuds ouverts, à trancher avant qu'une citation n'en dépende » devient « trois nœuds, à trancher avant le scellement ; texte écrit sous l'option recommandée » (M1, M2).

## Section 1

7. Phrase finale : les nœuds ne touchent pas aux invariants sous leurs options recommandées ; l'option (b) du nœud N-2 y toucherait, et le dit (M2).

## Section 2

8. Le registre propre du côté des moniteurs est lu par son chemin, pour ses seules lignes de scellement (m12).

## Section 3

9. Ouverture : la lecture stricte du JSON est celle du code neuf, qui relit en plus chaque fichier que les fonctions d'origine ouvrent (m8).
10. Contrôle neuf T0, joué en premier : les trois lignes de scellement du côté des moniteurs, leurs heures, leurs textes cités scellés, leurs empreintes attendues (m12).
11. Contrôle E3 : exception de nom de la clé `manifeste` (m2).
12. Contrôle E4 : égalité à `designation_v5.configuration_de_course(…)` au lieu de « égales, deux clés ôtées » ; `resultat.configuration_sha256` égal à `config_sha256` du manifeste du run (m3).
13. Contrôle E7 : types de l'entropie et règle de comparaison ; préfixe égal à `designation_v5.prefixe_de_la_course(…)` au lieu de « finit par `course/` » (m1, m3).
14. Section 3.1 : les lignes d'un épisode sont triées par pas par le code avant `exiger_sorties_oracle` (m7).
15. Section 3.2 : même tri pour les épisodes du maître (m7).
16. Section 3.2 : `regle_v5.accepter` reçoit les lignes triées (m7).

## Section 4

17. Point 3 : l'appel de décodage de la course est cité dans `regenere_v5.py`, ligne 84, celui de la première course restant cité comme le même (m10).
18. « Trois décisions liées » : renvoi à la section 16, « Tranché par la spécification » (m17).

## Section 5

19. Section 5.1, `MODULES_D_ORIGINE` : ajout de `designation_v5.py`, `harnais/run_harnais_factice.py`, `harnais/formats.py`, `scellement.py`, `gardes.py` ; le reste est tenu par le commit du manifeste et l'arbre propre (m9).
20. Section 5.1 : constante neuve `SCELLEMENTS_SONDES`, trois clés et trois empreintes attendues (m12).
21. Section 5.2 : fonction neuve `exiger_ordre_du_temps` (m12).
22. Section 5.3 : la clé `episodes` vaut `{"fiches": […]}` (m6).
23. Section 5.4 : le script de la lecture (1) reçoit `--registre-sondes` (m12).
24. Section 5.4 : le script de la lecture (2) reçoit `--registre-sondes` (m12).
25. Section 5.4 : le script d'audit « n'écrit rien », dit dès sa ligne (M4).
26. Section 5.4, ordre des opérations : la ligne de relecture de l'audit porte son issue (m13).

## Section 6

27. Section 6.1, point 1 : contrôle T0 en tête (m12).
28. Section 6.2 : clés neuves `cloisonnement` et `ordre_du_temps` (m16, m12).
29. Section 6.2, `exces_du_maitre` : clé neuve `exces_moyen_honnete_de_l_etalonnage` (M1).
30. Section 6.3, réécrite : quatre gardes du script d'audit ; échantillon lu dans la sortie scellée et retiré pour contrôle d'égalité ; rien n'est écrit sur disque ; ligne de consignation avec issue (`ISSUE=SANS-DEFAUT`, `ISSUE=DEFAUT`, `ISSUE=DEFAUT-AUTORISE` avec identifiant d'accord) (M4, m13).

## Section 7

31. Section 7.1, mode réel : dossier du jetoniseur à exactement quatre fichiers à empreinte de référence, `config.json` compris ; toute autre entrée arrête ; la phrase « tout autre fichier a son empreinte consignée, sans référence » disparaît (m11, m4).
32. Section 7.1 : puce neuve « taille du vocabulaire » (`vocab_size` de `config.json`, `len(tok)` exigé égal, `tok.vocab_size` écarté) (m4).
33. Section 7.1, fins d'action : citation de `modele_v5.charger_modele_reel`, lignes 59 et 60, au lieu de `modele_v1.charger_modele_reel` (m10).
34. Section 7.2, réécrite en deux alinéas : clés exactes des deux sortes de fichiers, clés de `ids` triées, réunion des tranches égale à l'ensemble, identifiant de 0 à V − 1, clé de l'action imprimée sur la sortie d'erreur et rien sur disque (m5, m4, m15).
35. Section 7.3, point 1 : « clé seule écrite » devient « clé seule imprimée sur la sortie d'erreur, rien sur disque » (m15).
36. Section 7.3, point 3 : même précision, et ces gardes jouent avant le manifeste (m15).
37. Section 7.3, point 4 : les fiches sont lues sous `sorties["episodes"]["fiches"]` (m6).
38. Section 7.4, point 1 : contrôle T0 (m12).
39. Section 7.4, point 2 : la garde de l'audit lit l'issue de la dernière ligne ; refus sur `DEFAUT`, sur une issue absente, ou sur `DEFAUT-AUTORISE` sans accord ; clé neuve `audit_de_la_lecture_1` (m13).
40. Section 7.5 : puce neuve `cloisonnement`, `ordre_du_temps`, `audit_de_la_lecture_1` (m16, m12, m13).
41. Section 7.5, base « premier coût contre les suivants » : le lecteur du coût est nommé, `cout_declare` de la ligne, lisible si `cout_lisible` (M3).
42. Section 7.5, `a_cote_de_chaque_taux` : score et critère « fixés par cette spécification à son scellement », au lieu de « à confirmer » (M2).
43. Section 7.5 : clé neuve `note_reperes` (m17).
44. Section 7.5, fichier des mots pondérés : reçoit `cloisonnement` (m16).
45. Section neuve 7.6 : sort de la base « premier coût contre les suivants » sous l'option (a) du nœud N-2, en cinq points, dont l'accompagnement sans condition vers Lazar (M2).

## Section 8

46. Garde de collision : étendue aux graines du manifeste du run (m14).

## Section 10

47. Section 10.1, table : la troisième ligne renvoie au « nœud N-3, option (a) » (M1).
48. Section 10.1 : *p* est la part citée `p_cite` (M1).
49. Section 10.2, réécrite : trois parts toujours calculées (`p_tous_les_episodes`, `p_episodes_acceptes`, `p_tous_les_episodes_moins_l_honnete`, l'honnête étant celui de l'étalonnage) ; part citée fixée avant toute lecture, `p_cite` et `option_citee` ; la clé `p_sur_les_episodes_acceptes` change de nom ; tout changement après la sortie est un écart (M1).

## Section 12

50. Liste fermée : ajout du registre propre du côté des moniteurs (lignes de scellement seules) et des trois textes cités (empreinte seulement) ; « les quatre fichiers » du jetoniseur (m12, m11).
51. « Jamais ouverts » : « tout registre du côté des moniteurs » devient « toute ligne autre que ses lignes de scellement » (m12).

## Section 13

52. Relance : les nœuds sont tranchés avant le scellement et ne se rouvrent pas sur une sortie écrite (M1, M2).

## Section 14

53. Ligne neuve « T0 » (m12).
54. Ligne « E0, E1 » : `aucune_activation` faux, `avertissement` altéré (m14).
55. Ligne « E4, E7 », réécrite : configuration rendue par `configuration_de_course`, `configuration_sha256`, entropie « 007 », entropie booléenne, préfixe (m3, m1, m14).
56. Ligne « E5 » : chemin cité absolu, chemin portant `..` (m14).
57. Ligne « E8 » : lignes d'un épisode dans le désordre, lues après tri (m7).
58. Ligne « graines » : nom déjà parmi les graines du manifeste du run (m14).
59. Ligne « liste fermée » : fragment `scores-moniteur` ; ligne du registre des moniteurs autre qu'un scellement (m14, m12).
60. Ligne « citations » : trois parts présentes, `p_cite` et `option_citee` (M1).
61. Ligne « garde de l'audit », réécrite : les trois issues, la dernière ligne décide (m13).
62. Ligne « jetoniseur » : cinquième fichier, sous-dossier, `config.json` altéré, `len(tok)` différent de `vocab_size` (m11, m4).
63. Ligne « identifiants » : clé de premier niveau en trop, clés non triées, clé en trop ou absente, piège de `tok.vocab_size` (m5, m4).
64. Ligne « base premier coût contre les suivants » : le score suit `cout_declare` de la ligne, non `cout_action(texte)` (M3).
65. Ligne neuve « script d'audit » : cas sain et sept artefacts (M4).
66. Ligne « écriture » : clé `cloisonnement` (m16).

## Section 15

67. Lignes neuves 8, 9 et 10 : épisodes sans ancre commune gardés dans la statistique qui décide ; garde d'ordre du temps ; issue de la ligne de l'audit (m17, m12, m13).

## Section 16

68. Réécrite. Règle commune : nœuds tranchés avant le scellement, texte sous l'option recommandée, texte de rechange écrit pour chaque autre option, aucune option sur résultat, aucune qui transmette un trait de l'organisme (M1, M2).
69. N-1 : phrases de sens (« *p* plus grand », « plus petit ») retirées ; option (c) précisée par l'honnête de l'étalonnage, l'honnête de l'évaluation écarté avec sa raison ; recommandation (a) sur la lettre seule, confiance 0,6 inchangée ; textes sous (a), (b), (c) (M1).
70. N-2 : option « trancher sur résultat » retirée ; option « un mot de plus dans l'extrait ou une pièce à part » retirée ; options neuves (b) règle par le seul mot « réussit » et (c) base non calculée ; le rédacteur recommande maintenant (a), confiance 0,7 (il ne recommandait pas) ; textes sous (a), (b), (c) ; score et critère fixés quelle que soit l'option (M2).
71. N-3 : trois options écrites, (a) recommandée, confiance 0,8 ; phrases de rechange de l'option (b) écrites ; tranché avant la lecture (1) (M1).
72. Sous-section neuve « Tranché par la spécification, à voir par Lazar » : sept choix (m17).

## Section 17

73. « Conduite de la relecture de l'audit » : ce qui reste hors de la spécification après l'ajout de la ligne d'issue (m13).
74. « Provenance des fichiers du jetoniseur » : dossier à quatre fichiers ; arrêt et nœud si le chargement ne tient pas ; la phrase sur `special_tokens_map.json` disparaît (m11).
75. « Toute interprétation » : « rien n'en sort » précisé « vers le côté des moniteurs » (cohérence avec la section 7.6).

## Section 18

76. Réécrite : points de la vérification des corrections ; liste des fichiers de la première contre-lecture gardée pour mémoire.

## Section 19

77. Alinéa neuf « Lus en plus pour le brouillon 2 », avec empreintes.
