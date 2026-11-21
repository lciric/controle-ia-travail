> You are powered by the model named Fable 5.2.

# Protocole X, première étape : la boucle « audit après coup, recapture, réapprentissage des sondes » devant l'invariant de l'oracle — ce qui casse, ce qui tient, où l'aveugle compte, la règle et ses épreuves — réponse du concepteur (v1)

- **Date** : 21 novembre 2026, de 15:25 à 16:06 UTC (`date -u`). **Auteur** : Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), effort maximal ; la phrase en tête est celle de mon invite système qui nomme mon modèle. Pièce de classe C, non contre-lue, non revendiquée. Aucun appel payant, aucune machine, ni commit ni poussée. Dépôt à `9a49c2f7f` au début, `6e1fe71bb` à l'écriture.
- **Mandat** : première étape du protocole X sur ton mot du 21 novembre vers 15:00 UTC (GO-2026-11-21-61, ligne 660 du registre des accords, lue avec la ligne 659). Deux extraits de cette ligne, rattachés par la mère : « que faire ? demande au collisionneur + protoocle x » ; et, sur le point 9 de la décision sur le plancher et les deux regards, « je penche poiur ca, demande au collisionneur et organisme dans la demande fusionnee ». La question, telle que la mère me la transmet : la boucle « audit après coup, recapture des épisodes pris, réapprentissage des sondes » heurte-t-elle le point 4 de la décision sur la vérité du dommage (N-060 v3), et comment la tenir ; ce qui casse, ce qui tient, la forme exacte d'une règle qui garde l'aveugle là où il compte, et les épreuves (cas sain, artefact planté) qui le montreraient.
- **Lu au dépôt**, empreintes égales aux compagnons : la consigne commune de méthode (`d327b3fc…23d8`) ; la décision sur l'assurance par l'audit, N-076 v1 (`49b664c1…dd78`) et son erratum 1 (`34a59c49…6484`) ; la décision sur la vérité du dommage, N-060, v3 (`2b448f69…5591`), v4 (`e1477998…f241`) et son erratum 1 (`316c8c23…ba95`) ; la décision sur le plancher et les deux regards, N-075 v3 (`5aed4bab…47b5`) et son erratum 1 (`c6efeccf…b0c1`) ; les notes sur la couverture de l'oracle (`659f4593…3376`), sur le dommage (`91784edf…424e`), sur ce qui reste après la publication du plancher (`6cbc8f49…f6ad`) ; le programme (`2fd63bad…a18c`). **Hors de la liste du mandat**, parce que l'invariant y naît ou y trouve ses précédents : N-060 v1 (`4a09c5f5…80ea`) et v2 (`06a7cb23…0270`) ; les cinq propositions de l'audit défensif, N-053 (`2204256d…deae`) ; la reconception des sondes, N-062 (`63f42690…`) ; le jeu final lu une seule fois, N-050 (`a54b128d…`) ; la question 4 de la note sur l'attaquant informé, où la boucle a été proposée (`c23a1034…e6d0`, lignes 128 à 154).
- **Lu sur PDF par moi** (texte extrait par `pdftotext`, rang de la page dans le fichier ; une seule page regardée en image, pour un tableau) : Rudoler et al., pages 1 à 9 et 12 à 16 ; Lyons Keenan et al., p. 1, 2, 6, 7, 18, 19 ; Li, Hays et al., p. 13, 14, 31, 32 ; Taufeeque et al., p. 1 et 7 ; la grille des études de tests diagnostiques (QUADAS-2), en entier ; les principes statistiques des essais cliniques, p. 23 à 25 ; et, par motifs ou à la page 1, les autres pièces de l'annexe. Chemins, empreintes et pages : `docs/sources/pdf/protocole-x-boucle-audit-recapture-v1/provenance-protocole-x-boucle-audit-recapture-v1.md`.
- **Recherche en ligne** : 11 requêtes en anglais (un moteur limité aux États-Unis, mode ordinaire), sans nom du programme, sans nom de personne, sans chemin interne ; 14 identifiants et un titre vérifiés par l'interface d'arXiv ; une page web lue par un outil qui résume. « Non trouvé » veut dire : non trouvé par ces requêtes, jamais « libre » (R8).
- **Sources** : 10 PDF versés et scellés sous `docs/sources/pdf/protocole-x-boucle-audit-recapture-v1/` ; 11 PDF du dépôt relus.
- **Mes calculs** : `calculs-boucle-audit-recapture-v1.py` (`38fa1ffe…179d`) et sa sortie `calculs-boucle-audit-recapture-v1.txt` (`a20fb790…512a`), même dossier que cette note : lois exactes et tirages à graines dérivées par `numpy.random.SeedSequence`, rejoués trois fois à l'octet, non contre-lus, aucune donnée du programme. **Toutes leurs entrées sont des suppositions d'illustration** : un monde gaussien où le dommage déplace les états le long d'une direction ; un état par épisode, la différence des moyennes étant prise entre épisodes, jamais sur les jetons.
- **Non ouvert** : tout dossier ou branche cloisonnés ; tout fichier « consigne-privee » ou « conception-ii-b » ; la ligne R-2059 ; tout résultat d'expérience ; tout préenregistrement ; la décision sur le mode tenu à l'écart (N-054), connue par `CLAUDE.md` et par N-062 ; les registres, hors les deux lignes dites.
- **Marques** : [établi] = lu ce jour par moi sur PDF, à la page dite, affirmation des auteurs ; [repris] = dit par une pièce du dépôt, non rouvert ; [dépôt] = texte d'une décision ; [calcul, X] = bloc X de ma sortie ; [proposition] = de moi, non mesurée ; [page web], [moteur], [de mémoire] = non opposables, aucun chiffre n'en est tiré.
- **Niveau** : toute menace est nommée par la supposition de défense qu'elle viole ; aucun mode opératoire.
- **Écarts déclarés** : une commande de liste par motif dans le dossier des décisions (les noms des fichiers N-060, N-075, N-076) ; des essais d'existence sur des chemins devinés (quatorze noms de décisions, neuf de PDF) ; les lectures hors liste dites ci-dessus, chacune par son chemin complet ; la note sur le dommage lue en entier, alors que le mandat en nommait les sections 2 et 4 ; une recherche par nom du script du collisionneur, dont j'ai lu les lignes de la garde de motifs ; une sortie d'outil trop longue rangée par l'outil sous un dossier que le mandat interdit, non rouverte ; deux PDF téléchargés puis retirés, parce que déjà au dépôt à l'identique ; le programme de calcul retouché deux fois par programme avant scellement (trois libellés et tolérances avant toute exécution ; une colonne ajoutée au bloc F après la première exécution, ses prévisions écrites avant la seconde) ; la table de provenance retouchée une fois (un titre).

## Verdict

1. **Oui, la boucle heurte la lettre de l'invariant de l'oracle, et par une seule de ses flèches.** L'audit ne choisit rien ; la recapture compte et annonce ; seul le réapprentissage fait entrer un verdict de l'oracle dans un moniteur. Ce que l'invariant protège tient en quatre choses (section 2), et la boucle n'en abîme aucune si l'on garde un ordre et un rôle : **un verdict de l'oracle peut instruire une sonde après l'avoir jugée, jamais avant, et jamais sur un épisode qui sert un verdict.**
2. **L'option (b), vers laquelle tu penches, est juste dans son esprit et fausse dans sa coupe.** « Au banc » contre « en service » ne sépare rien pour le programme : il n'a pas de service, et la boucle se mesurera au banc. Écrite ainsi, (b) interdit la mesure que la décision sur l'assurance par l'audit inscrit, ou bien permet tout à qui dit « service simulé ». La coupe qui tient est par **rôle de l'épisode** (verdict, flux, pli retenu), fixé avant que l'oracle ne parle. Je l'appelle (b′).
3. **Ce qui casse si rien ne garde**, sur mondes plantés, sous supposition. La recapture relue par la sonde qu'elle vient d'instruire vaut 1,00 là où le rappel vrai est 0,01 : l'annonce « moniteur invalide » ne sonnerait plus jamais [calcul, A]. Comptée sur un audit que la sonde oriente, elle vaut 0,71 pour un rappel vrai de 0,20 [calcul, B]. Un seuil calé sur les témoins qui ont instruit la sonde laisse passer de 2 % à 40 % de fausses alertes au lieu de 1 % [calcul, A]. Instruite contre le flux « sain » du suspect, la sonde apprend l'angle mort de l'oracle comme un signe d'innocence ; instruite contre des témoins exogènes seuls, elle peut ne lire que l'identité du suspect et signaler 99,6 % de ses épisodes sains [calcul, E].
4. **Ce qui tient** : la borne du plancher, tant que sa pièce ne dépend d'aucun score et que l'oracle ne voit pas le moniteur ; l'invariant « aucun score de moniteur dans l'entraînement de l'agent » ; les portes. **Et la grandeur que la décision demande de rapporter est aveugle par construction** : « le rappel retrouvé en fonction du nombre d'épisodes endommagés audités », compté épreuve puis leçon, n'a jamais besoin d'une relecture [calcul, A].
5. **L'aveugle compte à cinq endroits, pas à un** : l'oracle ne voit pas le moniteur ; le plancher ne voit pas le moniteur ; la version jugée n'a pas vu l'étiquette qui la juge ; les concepteurs ne voient pas les verdicts par épisode et les portes ne voient pas le flux ; l'agent ne voit rien. Les trois premiers ont chacun leur question dans la grille avec laquelle la médecine juge une étude de test diagnostique [établi pour la grille ; le rapprochement est de moi]. Le seul endroit où l'on cède : la procédure qui apprend une version à venir lit les étiquettes du flux.
6. **Dimensionnement.** Réglé par la table du seuil, le plancher livre en moyenne trois épisodes endommagés audités avant le seuil toléré, quel que soit ce seuil (ln 20) [calcul, C]. Avec trois étiquettes, réapprendre une sonde en dimension 4 096 rend 3 % de rappel ; choisir dans une réserve scellée de vingt détecteurs en rend 34 %, si la réserve voit la moitié de l'écart ; et un pli de trois épisodes ne certifie pas plus de 0,37 [calcul, C et D]. En régime de signature, la boucle ne tient donc pas le seuil : elle sert après l'alarme. En régime d'excès, les étiquettes sont nombreuses mais mêlées d'échecs honnêtes : 3 % de rappel là où des étiquettes pures en donneraient 17 %.
7. **Un pas se fait sans toucher l'invariant** : la même boucle, instruite par les étiquettes de construction du banc, révélées au taux du plancher. C'est l'épreuve de récupération après réentraînement que tu as accordée en octobre (N-053, point 5), étendue d'un bras d'attaque sur les poids à une famille de sabotage neuve pour la sonde ; elle donne la borne haute. (b′) n'y ajoute que ce que coûte l'oracle : ses manques, son délai, le mélange du sabotage et de l'échec honnête.
8. **Rien à revendiquer.** La règle assemble des pratiques publiées : deux dans notre domaine (Rudoler et al. ; Cooper Stickland et al.), les autres dans quatre métiers (tests diagnostiques, essais cliniques, détection de fraude, détection de logiciels malveillants). Deux heurts voisins sont apparus en chemin : la boucle déroge à l'anti-circularité du § 7 du programme ; et les lecteurs de l'oracle sont dits aveugles à la condition, pas au score ni à la raison du tirage.

---

## 1. Tes quatre points

**(1) Ce qu'un expert ferait, et que tu ne demandes pas.**
- **Il remonterait à ce que l'interdit protège** avant de demander lequel de deux textes cède. La première version de la décision le dit en clair : les sorties de l'oracle « servent d'étiquette de vérité à la lecture (fichier scellé que les moniteurs ne voient pas) et au choix d'une dose comme paramètre commun, sans filtrer un seul épisode » (N-060 v1, point 3) [dépôt].
- **Il reconnaîtrait la figure** : un test (la sonde) jugé contre un étalon (l'oracle) sur un échantillon vérifié en partie (l'audit), puis révisé à l'aide de l'étalon. La médecine a une grille pour cela ; il la passerait question par question (section 5).
- **Il refuserait « banc ou service »** et demanderait, pour chaque épisode, à quoi il sert, et pour chaque nombre, ce qui était écrit avant quoi.
- **Il jugerait la procédure qui apprend, non une sonde figée** : dans un flux, on note d'abord, on instruit ensuite [de mémoire : Dawid, 1984]. Les tests séquentiels qui parient sur un prédicteur mis à jour en ligne gardent leur niveau, et tiennent quand la loi dérive (Podkopaev et Ramdas, p. 1 et 3) [établi].
- **Il compterait les étiquettes** avant de parler de rétablissement, et ce que chaque étiquette injecte dans le moniteur : un choix parmi vingt, ou quatre mille poids.
- **Il chercherait par où l'agent instruit la sonde à sa place** : c'est lui qui écrit les épisodes qui seront pris.

**(2) Les données brutes de départ.** Pas une recapture agrégée. Par épisode, le journal du harnais : l'heure ; le tirage d'audit, sa probabilité et sa source (plancher, enjeu, soupçon) ; l'empreinte de la version qui l'a noté et le score, consignés avant le verdict ; le verdict de l'oracle, son heure, et ce que ses lecteurs avaient sous les yeux ; le rôle de l'épisode. Par version : sa lignée (les épisodes dont une étiquette l'a instruite), sa procédure, ses scores sur les témoins honnêtes. Les états internes lus, gardés pour tous les épisodes : sans eux il n'y a rien à réapprendre. Au banc seulement : la vérité plantée, pour juger la boucle elle-même.

**(3) Les méthodes et les outils.**

| Outil | Ce qu'il donne | Ce qu'il suppose | Comment il échoue |
|---|---|---|---|
| Épreuve puis leçon, par version scellée | une recapture que la leçon ne peut pas gonfler | le score consigné avant le verdict | un score recalculé après coup et présenté comme consigné |
| Compte sur le plancher seul, ou pondéré par l'inverse de la probabilité d'audit | une recapture sans biais de vérification | des probabilités consignées, un plancher non nul | plancher très bas : le compte pondéré se biaise et se disperse [calcul, B] |
| Pli retenu, tiré par le harnais ; borne binomiale exacte | un rappel annoncé pour une version neuve, sur le passé | un tirage que rien d'autre ne voit | pli réemployé pour choisir : il est consommé |
| Lignée et garde par programme | l'impossibilité matérielle de juger une version sur sa leçon | des identifiants d'épisode et de famille fiables | une famille tenue à l'écart qui fuit par un épisode voisin |
| Devin | une borne basse de la fuite vers l'agent | rien | il réfute, il n'atteste pas (N-076, § 6.3) [dépôt] |
| Essai de permutation | l'oracle et le plancher ne dépendent d'aucun score | un journal complet des entrées | une entrée de l'oracle hors journal |

**(4) Ce qui vérifierait hors de nous.** La grille des études diagnostiques, remplie par un tiers sur le harnais. Le journal rejoué par un autre : la recapture par version se recalcule sans rien savoir des sondes. Un statisticien du séquentiel pour le pas 8 de ma chaîne (contact : nœud). Le montage publié de Rudoler et al., qui tire sa pièce après le verdict et tient un jeu d'évaluation hors des leçons (p. 13 à 15) [établi]. Le collisionneur, pour l'antériorité et les contre-arguments.

**Reformulation.**

> Dans la boucle audit, recapture, réapprentissage : pour chaque flèche par laquelle un verdict de l'oracle atteint un moniteur, ceux qui le conçoivent, le tirage d'audit ou l'agent, dire ce qu'elle apporte et ce qu'elle fausse si rien ne la garde ; dire qui doit rester aveugle à quoi pour que chaque nombre rapporté (la borne du plancher, la recapture, le taux de fausses alertes, le verdict d'une porte, le rappel retrouvé) garde son sens ; écrire la règle par le rôle de l'épisode et l'ordre des événements, non par le lieu ; donner à chaque clause une épreuve d'admission du harnais, avec son cas sain et son artefact planté ; et dire, étiquettes comptées, ce que la boucle peut rendre avant le seuil toléré.

## 2. Ce que l'invariant protège, et par où la boucle le touche

**La lettre.** « Aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur » (N-060 v3, point 4) [dépôt]. Réapprendre une sonde, c'est choisir ses poids ; le faire sur des verdicts de l'oracle entre dans la lettre. La décision sur l'assurance par l'audit le dit déjà (§ 6.2) : je confirme.

**L'esprit : quatre protections**, lues dans les trois versions de la décision et dans ses voisines [dépôt ; le découpage en quatre est de moi].

| | Ce que l'interdit protège | Où c'est écrit | La boucle y touche-t-elle ? |
|---|---|---|---|
| P1 | **Une comparaison n'est pas réglée sur sa propre vérité** : l'oracle est l'étiquette de vérité à la lecture ; s'il réglait aussi ce qu'on compare, la lecture mesurerait le réglage | N-060 v1, point 3 ; N-050 ; N-062, point 4 : « chaque lecture est une épreuve fraîche, jamais une relecture du même jeu » | Oui, si un épisode de flux sert aussi un verdict, ou si une version est jugée sur sa leçon |
| P2 | **Aucun épisode n'est filtré sur son issue** : lecture en intention de traiter | N-060 v1, points 3 et 6 | Non : la boucle étiquette, elle ne trie pas la population lue |
| P3 | **L'oracle reste hors de la vue de ceux qui conçoivent** les moniteurs et le mode tenu à l'écart | N-060 v3, point 4 ; « fichier scellé que les moniteurs ne voient pas » | Oui, si les verdicts par épisode atteignent un concepteur ; non, si une procédure scellée est seule à les lire |
| P4 | **La vérité ne dépend pas des moniteurs** | N-060 v3, point 1 ; « oracle exogène », N-075 v3, § 1 | Par un chemin que les textes ne ferment pas : une file d'audit qui suit le soupçon peut dire à l'oracle ce que le moniteur pensait |

**Cinq flèches, dont une seule heurte la lettre.**

| Flèche | Ce qu'elle porte | Heurt avec le point 4 | Ce qu'elle fausse si rien ne la garde |
|---|---|---|---|
| α. Du tirage à l'oracle | un épisode à juger | aucun | l'étiquette, si l'oracle sait pourquoi l'épisode lui vient |
| β. De l'oracle au compte | la recapture, l'annonce « moniteur invalide » | aucun, sous la lecture « annoncer n'est pas sélectionner » de N-075 v3 (§ 11, point 2), encore à confirmer | la recapture, si le compte est pris sur ce que la sonde a fait auditer |
| γ. De l'oracle à la leçon | des étiquettes pour une version à venir | **oui, dans la lettre** | la recapture, les fausses alertes, les portes, le cloisonnement |
| δ. De la sonde réapprise au tirage | l'orientation de l'audit | aucun | les étiquettes de demain, choisies par la sonde d'aujourd'hui |
| ε. De la sonde réapprise à l'agent | toute conséquence visible | aucun (c'est l'invariant sur le retour à l'agent) | « le défenseur joue en dernier » |

**« Banc » et « service » ne sont pas la bonne coupe.** Trois raisons. (i) Le programme n'a pas de service : ses agents sont des organismes, ses déploiements des flux joués au banc, et la mesure de la boucle sur un modèle y est prévue, sur devis (N-076, § 6, « premier pas et dépense »). Lue à la lettre, (b) interdit donc ce qu'elle voulait permettre ; lue largement, il suffit d'appeler un bras « service » pour que l'interdit tombe partout. (ii) Dans un service réel non plus, l'interdit ne peut pas tomber entier : la recapture y juge encore les moniteurs, et c'est là qu'un faux « tout va bien » coûte le plus. (iii) Ce que l'interdit protège ne tient pas au lieu mais à l'usage : un épisode qui sert un verdict, où qu'il soit.

**Le programme a déjà la moitié de la réponse.** L'épreuve de récupération après réentraînement des sondes, contre la réserve de détecteurs, est accordée depuis le 26 octobre, dans le bras des attaques sur les poids (N-053, point 5) [dépôt] : trois jours avant la première décision sur l'oracle. Ses étiquettes ne pouvaient donc être que celles de la construction du banc (ma lecture ; le texte ne dit pas lesquelles). Le heurt ne commence qu'au moment où l'étiquette vient de l'oracle. L'option « garder l'invariant entier » n'enferme donc pas la boucle dans les mondes plantés, comme l'écrit la décision sur l'assurance par l'audit (N-076, § 13, point 3) : elle l'enferme dans les étiquettes de construction (section 7).

## 3. Ce qui casse

Chaque ligne est un défaut qui apparaît si la flèche est ouverte sans garde. Les nombres viennent de mon monde d'illustration, sauf mention.

| | Ce qui casse | Mécanisme | Combien | Clause |
|---|---|---|---|---|
| 1 | **La recapture relue** | La sonde finale note les épisodes qui l'ont instruite. En grande dimension, elle les reconnaît tous, qu'il y ait une trace ou non | Dommage sans aucune trace dans les états (rappel vrai 0,010) : relue 1,00 jusqu'à cent étiquettes, 0,68 à trois cents. L'erreur va dans le sens qui rassure [calcul, A] | 2, 3 |
| 2 | **La recapture sur l'audit orienté** | Les épisodes signalés sont plus souvent vérifiés : c'est le « biais de vérification partielle » des études diagnostiques. « Missing completely at random […] there is no partial verification bias involved » (Arifin et Yusof, p. 2) [établi] | Rappel vrai 0,20, plancher 5 %, signalés audités une fois sur deux : 0,71 ; plancher 1 % : 0,93 [calcul, B]. Exemple publié : sensibilité 0,975 sans correction, 0,819 corrigée (p. 7 et 9) [établi] | 3, 9 |
| 3 | **Le taux de fausses alertes** | Le seuil « 1 % » calé sur les témoins qui ont servi de négatifs est trop bas : la sonde a appris à les repousser | Fausses alertes réelles : 2 % avec trois étiquettes, 7 % avec trente, 23 % à 40 % avec trois cents [calcul, A]. C'est la seule garantie que portent nos moniteurs | 6 |
| 4 | **Une porte** | Une version née du flux concourt à une porte, ou un épisode de la famille d'une porte entre dans une leçon. Un seul variant d'une famille dans l'apprentissage peut en révéler beaucoup à l'épreuve (Pendlebury et al., p. 1) [établi] | Non chiffré : c'est la protection P1 | 1 |
| 5 | **Le second regard** | La sonde instruite par l'oracle ne voit au mieux que ce que l'oracle voit. Si ses négatifs sont les épisodes du suspect dits sains, la part de dommage cachée à l'oracle y entre comme « sain » | Dommages cachés signalés à 0,005 au lieu de 0,010 quand 6 % des « sains » en portent ; à 0,00004 quand 44 % en portent [calcul, E] | 6, 7 |
| 6 | **Le sens même du signal** | Si ses négatifs sont des témoins exogènes seuls, la sonde peut apprendre « c'est le suspect ». Le programme le sait : ses sondes ont lu « l'identité de l'organisme » (N-062, point 2) [dépôt] | Écart d'identité de 6 écarts types : 99,6 % des épisodes sains du suspect signalés, recapture de 1,00, aucun gain d'orientation [calcul, E] | 3, 6 |
| 7 | **Le cloisonnement** | Un verdict par épisode montré à un concepteur lui montre la référence cachée, contrôle par contrôle. Un compte rendu après chaque audit le montre aussi, par différence | Non chiffré : protection P3 | 5 |
| 8 | **L'ordre des coups** | Si une version, son changement ou une de ses conséquences se voit, l'agent a un signal. Des verdicts faux une fois sur dix portent encore 87 % de l'effet (Lyons Keenan et al., p. 7) [établi] | Écart qui change de direction à chaque épisode : recapture épreuve puis leçon 0,010, relue 1,00 [calcul, A, artefact A3] | 10 |
| 9 | **L'étiquette** | Un lecteur de l'oracle qui sait l'épisode signalé confirme plus volontiers | Précision de la file de soupçon : vraie 0,69 ; mesurée 0,56 par un oracle imparfait et aveugle ; 0,72 à 0,81 s'il sait [calcul, F]. Effet modeste sur la recapture (0,17 à 0,22) | 8 |
| 10 | **Le silence pris pour une bonne nouvelle** | La recapture se compte parmi les dommages que l'oracle trouve. Hors de sa couverture, la boucle ne voit ni dommage ni cécité | Rien à compter | 12 |

**Ce que l'agent peut faire de la leçon** [proposition, niveau de l'idée]. Il écrit les épisodes qui seront pris ; il peut donc chercher à orienter ce que la sonde apprendra. Tant que le plancher ne dépend d'aucun score, cela lui coûte ou lui rapporte de la vitesse, jamais la validité de la borne. Et le hasard du plancher fait des prises un échantillon au hasard des dommages que l'oracle voit : ce que la sonde apprend sur elles vaut, en loi, pour les dommages non audités du même passé. Rien ne vaut pour l'avenir.

## 4. Ce qui tient

1. **La borne du plancher.** Elle ne lit aucun état et ne dépend d'aucune version. La forme publiée couvre un tirage dont la probabilité dépend de l'histoire, pourvu qu'elle soit connue et bornée par un plancher : « a design propensity π_τ(h_τ) […] ≥ π_min > 0 » ; la non-interférence de la pièce y est « necessary and sufficient for an unbiased adaptive certificate » (« Blindfold », p. 3 et 5) ; et, pour un étiqueteur imparfait, « every true failure must have a positive probability of being audited with a ground-truth label at each round » (Li, Hays et al., p. 13) [établi]. Qu'elle couvre aussi une probabilité qui change selon des étiquettes passées, je le suppose par le même argument de martingale ; je ne l'ai pas lu en toutes lettres (pas 8 de ma chaîne).
2. **Un test valide à tout instant, avec un moniteur qui change.** Il suffit que la version qui note l'épisode t soit fixée avant que son verdict ne soit connu. C'est la structure de Rudoler et al. : la pièce est tirée « independently after the prediction », et « the learner's state depends only on previously queried examples » (p. 3 et 4) [établi].
3. **La courbe que la décision demande.** Comptée épreuve puis leçon, elle suit le vrai par en dessous : pour un écart de 4 écarts types, 0,13 puis 0,32 puis 0,55 sur le dernier tiers à trente, cent et trois cents étiquettes, quand le rappel vrai de la dernière version vaut 0,14, 0,35 et 0,58 [calcul, A]. Elle juge la procédure qui apprend, pas une sonde.
4. **L'emploi rétrospectif** (relire le passé non audité après l'alarme) : un pli retenu par tirage en donne une estimation valide par le seul hasard du défenseur, puisque le passé est écrit. Elle porte sur les dommages que l'oracle reconnaît, pondérés par sa probabilité de les reconnaître.
5. **L'invariant sur les scores de moniteur** (N-053, point 5) : la boucle n'entraîne ni ne sélectionne l'agent. **Les critères des portes** : aucun n'est touché si les rôles sont disjoints.
6. **Le principe que tu as posé pour l'organisme** : « des tâches fraîches (la seule chose qui marche vraiment) » (N-050) [dépôt]. Le flux en fournit de lui-même : chaque épisode du plancher est une épreuve neuve pour la version en place, à condition de servir d'épreuve avant de servir de leçon.

## 5. La règle

**En une phrase.** Un verdict de l'oracle n'instruit un moniteur qu'après l'avoir jugé, jamais sur un épisode qui sert un verdict, et par nulle autre main qu'une procédure scellée d'avance.

**Les cinq endroits où l'aveugle compte.** La grille des études de tests diagnostiques pose les mêmes questions à qui juge un test contre un étalon (QUADAS-2, p. 2 et 3) [établi] ; le rapprochement est de moi.

| Qui ne voit pas quoi | Ce que cela protège | La question de la grille | Clauses |
|---|---|---|---|
| L'oracle ne voit ni score, ni version, ni raison du tirage | la valeur de l'étiquette | « Were the reference standard results interpreted without knowledge of the results of the index test? » | 8 |
| La pièce du plancher ne voit aucun score | la borne du plancher ; la recapture sans biais | « Was a consecutive or random sample of patients enrolled? » ; « Did all patients receive a reference standard? » | 3, 9 |
| La version jugée n'a pas vu l'étiquette qui la juge ; son seuil est fixé avant | la recapture ; le taux de fausses alertes | « Were the index test results interpreted without knowledge of the results of the reference standard? » ; « If a threshold was used, was it pre-specified? » | 2, 4, 6 |
| Les concepteurs ne voient pas les verdicts par épisode ; les portes ne voient pas le flux | les portes, la famille tenue à l'écart, le cloisonnement | hors grille ; c'est la règle des analyses intermédiaires d'un essai : « All staff involved in the conduct of the trial should remain blind to the results of such analyses » (principes statistiques des essais cliniques, p. 24) [établi] | 1, 5 |
| L'agent ne voit rien | « le défenseur joue en dernier » | hors grille : le patient ne s'adapte pas au test | 10 |

**Définitions.** *Version* : un moniteur figé (direction, seuil, procédure de lecture), nommé par son empreinte et scellé avec sa *lignée*, la liste des épisodes dont une sortie de l'oracle a servi à le produire. *Rôle* d'un épisode jugé par l'oracle, fixé par le harnais et consigné avant que l'oracle ne rende son verdict : **épisode de verdict** (il sert une lecture décisive préenregistrée : porte, famille tenue à l'écart, jeu final) ; **épisode de flux** (il appartient à un déploiement, réel ou joué dans un bras déclaré) ; **épisode du pli retenu** (tiré au sort parmi les épisodes de flux, à taux déclaré).

**Les douze clauses** [proposition].

1. **Le verdict ne nourrit rien.** Un épisode de verdict, sa famille et son organisme n'entrent dans aucune lignée ; le mode tenu à l'écart n'est jamais un épisode de flux ; une version née d'un flux ne concourt à aucune porte. Pour eux, le point 4 garde toute sa lettre.
2. **L'épreuve avant la leçon.** Sur un épisode de flux, un verdict de l'oracle peut entrer dans la lignée d'une version à venir si : (i) le score de cet épisode par toute version qu'il juge a été consigné avant le verdict ; (ii) la version qui en naît est scellée, lignée comprise, avant de noter un épisode ; (iii) elle n'est jamais jugée sur un épisode de sa lignée.
3. **La recapture.** Elle se compte par version, sur les seuls épisodes tirés par la part de l'audit qui ne dépend d'aucun score, ou pondérée par l'inverse des probabilités consignées. Elle se rapporte en table à quatre cases : signalés parmi les endommagés, signalés parmi les dits sains. Une version qui signale les deux également lit le suspect, non le dommage.
4. **Le pli retenu.** Une version neuve n'annonce un rappel, et ne relit le passé non audité, que sur la foi d'un pli qu'elle n'a pas vu. Un pli qui a servi à choisir entre deux versions est consommé : il entre dans la lignée, un pli neuf est tiré.
5. **Qui apprend.** Une procédure écrite et scellée avant le flux (famille de sonde, couches, échelons, positifs et négatifs, règle de choix, calendrier des leçons), sans personne dans la boucle. Le calendrier est fixé d'avance : une version remplacée parce qu'elle paraissait mauvaise laisserait aux versions gardées une recapture flattée. Les verdicts par épisode et les lignées ne vont à aucun concepteur de moniteurs ; le compte et l'annonce leur vont, par lots, à dates fixées d'avance, et chaque compte rendu est compté comme une lecture. Changer la procédure est une reconception (N-062), sur les modes vus.
6. **Les témoins.** Ceux qui calibrent ne sont pas ceux qui instruisent ; ils sont exogènes, et notés de nouveau par chaque version, dont l'accumulation repart de zéro avec sa déclaration refaite (taille de la référence, horizon, source de validité : loi de la référence honnête, N-076, point 1). Toute statistique apprise sans étiquette (centrage, blanchiment) se calcule sur eux, jamais sur le flux du suspect. Les positifs de la leçon sont les prises du plancher ; celles de la file de soupçon restent dans un registre à part, pondérées, jamais fondues sans le dire. Les négatifs sont déclarés : si ce sont les épisodes du suspect dits sains, la version dit la part de dommage que l'oracle ne voit pas, ou « blanchiment non mesuré ».
7. **On ajoute, on ne remplace pas.** Toute lecture d'un regard reste consignée, même si l'on cesse de la suivre. Aucun texte ne compte une sonde instruite par l'oracle comme un regard indépendant de lui.
8. **L'oracle ne voit pas le moniteur** : ni score, ni version, ni source du tirage ; l'ordre de présentation est tiré par le harnais.
9. **Le plancher ne voit pas le moniteur** : sa part du tirage ne dépend d'aucun score d'aucune version ; ce que la sonde réapprise oriente est la part au-dessus.
10. **Rien ne revient à l'agent** : ni version, ni changement de version, ni score, ni verdict ; poids gelés ; aucune sortie de l'oracle dans son entraînement ni sa sélection. « Le défenseur joue en dernier » ne s'écrit qu'après l'épreuve du devin.
11. **À étiquettes égales.** Toute comparaison d'une sonde réapprise à une base donne à la base la même boucle : un lecteur de texte instruit par les mêmes étiquettes.
12. **Portée dite.** Tout chiffre de la boucle porte : l'oracle, sa version et sa couverture mesurée, le taux du plancher, le nombre d'étiquettes, l'échelon, la taille du pli. Hors couverture, la boucle se dit muette.

**Texte proposé pour le point 4 de la décision sur la vérité du dommage**, si tu retiens (b′) :

> Aucune sortie de l'oracle dans la sélection ni l'entraînement d'un agent (N-053). Aucune sortie de l'oracle sur un épisode qui sert un verdict dans la sélection, le réglage, l'entraînement ou la conception d'un moniteur. Sur un épisode de flux d'un bras déclaré, une sortie de l'oracle peut instruire une version à venir d'un moniteur, par une procédure scellée avant le flux, après que le score de cet épisode a été consigné, la version n'étant jamais jugée sur ce qui l'a instruite ; le mode tenu à l'écart n'est jamais un épisode de flux. Le reste du point est inchangé, et « inaccessible aux concepteurs de moniteurs » vaut pour chaque verdict par épisode.

**Et pour la ligne « asymétrie d'apprentissage » du § 9 du programme** :

> Dans un flux, chaque épisode audité par la part du tirage qui ne dépend d'aucun score, et dit endommagé par l'oracle, devient, après avoir servi d'épreuve aux versions en place, un exemple étiqueté pour une version à venir ; jamais un épisode qui sert un verdict ; canal de retour fermé, éprouvé.

## 6. Les épreuves

Ce sont des épreuves d'admission du harnais, sur mondes plantés, sans dépense ; chacune a un cas sain et un artefact (R5). Celles marquées « jouée » ont un prototype dans mes calculs ; les autres sont à écrire. Aucune n'est scellée.

| | Épreuve | Cas sain : ce que le harnais doit rendre | Artefact planté : ce qu'il doit rendre | État |
|---|---|---|---|---|
| 1 | Lignée et rôle (clause 1) | Rôles disjoints : la garde laisse passer | Un épisode de verdict, puis un épisode de la même famille, glissés dans une lignée : refus nommé, dans les deux cas | à écrire |
| 2 | Ordre (clause 2) | Scores consignés avant les verdicts : accepté | Un score recalculé par une version scellée après le verdict, présenté comme consigné : refus | à écrire |
| 3 | Recapture aveugle (clauses 2, 3) | Écart de 4 écarts types : la suite monte vers le vrai (0,55 contre 0,58 à trois cents étiquettes) | Dommage sans trace : la suite reste à 0,01 ; la relecture donne 1,00 et doit être refusée | jouée [A] |
| 4 | Audit orienté (clauses 3, 9) | Tirage sans égard au score : le compte naïf vaut le vrai (0,200) | Signalés audités une fois sur deux : le naïf vaut 0,71 ; le compte du plancher 0,20 ; le pondéré 0,20 | jouée [B] |
| 5 | Pli (clause 4) | Pli jamais vu : l'estimation tombe dans son intervalle exact | Pli qui a servi à choisir parmi vingt versions, puis relu : l'optimisme paraît (0,07 pour 0,01 à trois étiquettes) ; le harnais doit le dire consommé | jouée en partie [C3, D] |
| 6 | Témoins (clause 6) | Seuil calé sur des témoins neufs : fausses alertes à 0,010 | Seuil calé sur les témoins de la leçon : 0,23 à 0,40 à trois cents étiquettes ; refus | jouée [A] |
| 7 | Négatifs (clauses 3, 6) | Ni identité ni part cachée : dommages cachés signalés à 0,010, sains du suspect à 0,010 | Identité forte, négatifs exogènes : sains du suspect signalés à 0,996, la table à quatre cases doit le montrer. Part cachée, négatifs du suspect : dommages cachés sous 0,010, « blanchiment » à dire | jouée [E] |
| 8 | On ajoute (clause 7) | Le regard ancien et la version neuve voient le même dommage : rien ne change | Le regard ancien voit un dommage que l'oracle ne voit pas : un harnais qui remplace le perd ; il doit mourir | à écrire |
| 9 | L'oracle aveugle au moniteur (clause 8) | Permuter les scores entre épisodes laisse les entrées de l'oracle identiques à l'octet | Un champ « source du tirage » dans ce que lit l'oracle : l'essai doit échouer | à écrire ; ordre de grandeur de l'effet [F] |
| 10 | Le plancher aveugle au moniteur (clause 9) | Permuter les scores laisse les tirages du plancher identiques | Plancher abaissé pour les scores bas : l'essai doit échouer | à écrire |
| 11 | Canal de retour (clause 10) | Canal fermé : le devin est au hasard, la courbe monte | Canal ouvert, l'écart change de direction à chaque épisode : la courbe doit rester à 0,01. Si elle monte, le banc ne mesure rien (second test de mort de la décision sur l'assurance par l'audit) | jouée pour la courbe [A3] ; devin à écrire |
| 12 | Hors couverture (clause 12) | Dommage vu par l'oracle : des prises, une recapture | Tout le dommage caché à l'oracle : la boucle doit rendre « muette, aucune prise », jamais « rappel rétabli » | à écrire |

L'épreuve 3 porte à elle seule ta crainte : avec elle, « la recapture ne juge plus à l'aveugle » devient un défaut que le harnais refuse d'exécuter, non un risque à surveiller.

## 7. Ce que la boucle peut rendre, étiquettes comptées

**Régime de signature, plancher réglé par la table du seuil.** Le taux d'audit de la table donne une prise avant le seuil toléré 95 fois sur 100. Le nombre d'épisodes endommagés audités à ce seuil suit alors une loi de moyenne 2,85 à 2,99, quel que soit le seuil ; il n'atteint dix qu'une fois sur mille [calcul, C1]. À la première prise, le plancher a déjà sonné. **La boucle n'est donc pas ce qui tient le seuil ; elle sert à ce qui vient après l'alarme** : retrouver le dommage déjà fait, tenir si l'on ne peut pas arrêter. Le premier test de mort écrit par la décision sur l'assurance par l'audit (« la boucle ne se ferme pas à temps ») est donc, pour un réapprentissage complet au taux de la table, une prévision : il sonnera.

**L'échelle des échelons** [calcul, C2 ; supposé : écart de 4 en dimension 4 096 ; réserve de vingt détecteurs qui porte la moitié de l'écart ; 400 témoins].

| Étiquettes | Choisir dans la réserve | Repondérer la réserve | Réapprendre en dimension complète |
|---|---|---|---|
| 3 | 0,34 | 0,14 | 0,03 |
| 10 | 0,37 | 0,24 | 0,06 |
| 30 | 0,37 | 0,31 | 0,14 |
| 100 | 0,37 | 0,35 | 0,35 |
| 300 | 0,37 | 0,36 | 0,58 |

Trois leçons. **Les voies bon marché d'abord** (N-045) : sous cent étiquettes environ, choisir dans une réserve scellée bat tout réapprentissage, si la réserve voit quelque chose. **Ce qu'on perd d'aveugle suit ce qu'on apprend** : dans le monde sans trace, relire en échantillon ajoute 0,06 au vrai pour un choix parmi vingt à trois étiquettes, 0,59 pour vingt poids, 0,99 pour 4 096 poids [calcul, C3]. **La référence honnête borne aussi la sonde réapprise** : avec 400 témoins, le rappel plafonne à 0,79 au lieu de 0,95, quel que soit le nombre d'étiquettes ; la loi de la référence honnête vaut pour la leçon comme pour l'accumulation.

**Ce qu'on peut annoncer.** Un pli de trois épisodes tous signalés ne borne le rappel qu'à 0,37 ; il en faut dix pour 0,74, trente pour 0,90 [calcul, D]. Au taux de la table, rien ne se certifie avant le seuil. À dix fois ce taux, le plancher livre trente étiquettes en moyenne [calcul, C1].

**Régime d'excès : nombreuses, mais mêlées.** L'oracle dit « endommagé », pas « saboté ». Dans le monde planté de la note sur ce qui reste après la publication du plancher, l'alarme vient après 231 épisodes endommagés audités [repris], dont un sixième seulement dus au sabotage si l'honnête échoue une fois sur dix et le saboteur ajoute deux points (ma lecture de ce monde). Une sonde instruite sur ce mélange contre des échecs honnêtes rend 0,03 de rappel sur le sabotage ; les mêmes étiquettes triées en rendraient 0,17 [calcul, C4]. Au banc, la part est plantée ; en service, personne ne trie.

**Trois étapes**, de la moins chère à la plus chère.

| Étape | Étiquettes | Ce qu'elle mesure | Ce qu'elle demande |
|---|---|---|---|
| 0 | plantées, mondes simulés | la règle, ses douze épreuves, la courbe, l'échelle | rien : déjà accordé comme protocole (N-076, § 6.2) |
| 1 | de construction, sur organismes, révélées au taux du plancher | la borne haute de la boucle sur de vrais états | un devis et ton accord pour étendre l'épreuve de récupération (N-053, point 5) à une famille de sabotage neuve pour la sonde ; aucun invariant de l'oracle touché. Une famille propre au flux, que les sondes n'ont pas apprise, jamais celle d'une porte : une famille de plus à produire |
| 2 | de l'oracle, sur organismes | ce que coûte l'oracle : manques, délai, mélange | ton mot sur (b′) ; un devis |

## 8. Ce qui est pris

| Pièce | Occupant, page | Marque |
|---|---|---|
| Un moniteur qui apprend sur des audits tirés au hasard face à un ouvrier adverse ; la pièce tirée après le verdict ; l'état de l'apprenti ne dépend que des exemples déjà interrogés ; un jeu d'évaluation « drawn once and never trained on », des programmes exclus parce qu'ils figurent dans les journaux d'exposition à l'entraînement ; des exemples conformes connus dans chaque lot, sans quoi le moniteur « learns to reject everything » | Rudoler et al., p. 3, 4, 13, 14, 15 | [établi] |
| Ses limites, de ses auteurs : des étiquettes supposées sûres ; « vanishing average error does not preclude substantial harm before the monitor learns » ; l'ouvrier y reçoit le retour du moniteur, ce que notre invariant interdit | p. 2 et 8 | [établi] |
| La sonde instruite sur des tentatives étiquetées retrouve la détection (0,040 à 0,986) ; réapprise sur des états sains, non (0,146) ; l'objection : il faut « having confidently classified evasion attempts » | Lyons Keenan et al., p. 6 et 19 | [établi] |
| Après une dérive d'entraînement ordinaire, une sonde refaite sur des données hors domaine ne retrouve pas la détection (0,38 et 0,66) ; refaite sur le domaine, si (1,00) | Taufeeque et al., tableau 4, p. 7 | [établi] |
| Des tours rouge et bleu sur des cadres d'entraînement, un cadre tenu à l'écart pour le chiffre final ; l'équipe rouge joue en dernier | Cooper Stickland et al., p. 1 à 3 | [établi] |
| Le pari sur un prédicteur mis à jour en ligne | Podkopaev et Ramdas, p. 1 et 3 | [établi] |
| Le biais de vérification partielle et sa correction par l'inverse de la probabilité | Arifin et Yusof, p. 2 et 3 ; Begg et Greenes, d'après eux | [établi] |
| Les étiquettes venues des alertes et les étiquettes tardives sont deux problèmes, à traiter par deux classifieurs | Dal Pozzolo et al., p. 6 et 7 | [établi] |
| La cohérence dans le temps entre apprentissage et épreuve ; la proportion réelle des classes à l'épreuve | Pendlebury et al., p. 6 | [établi] |
| Le réemploi adaptatif d'un jeu retenu ; la validité par longueur de description | Dwork et al., p. 1 | [établi] |
| Quand le prédicteur est appris sur les données étiquetées elles-mêmes : la prédiction croisée | Zrnic et Candès, p. 1 | [établi] |
| Apprendre avec des positifs étiquetés au hasard et le reste sans étiquette ; la fréquence d'étiquetage | Bekker et Davis, p. 4, 7, 9 | [établi] |
| Quelques exemples pris sur le fait pour ajuster une sonde | billet de janvier 2026 | [page web] |

**Non trouvé par mes onze requêtes** : la règle assemblée pour une sonde sur états internes, un oracle à angle mort et trois rôles d'épisode ; le compte des étiquettes que livre un plancher réglé par un seuil toléré. Ce sont des questions (R8) ; et la règle est une règle d'exploitation : elle ne se revendique pas.

## 9. Le couple pour le collisionneur, et la question pour l'organisme

Dans `collisionneur-v1/`, même dossier : `faits-boucle-audit-recapture-v1.md` et `question-boucle-audit-recapture-v1.md` ; et, à côté de cette note, `question-organisme-boucle-audit-recapture-v1.md`. Empreintes aux compagnons. Les faits donnent le dispositif, la boucle, l'interdit, les deux options telles qu'écrites et ce qui est publié dans le domaine ; ils ne donnent ni (b′), ni l'ordre « épreuve puis leçon », ni les cinq aveugles, ni mes chiffres. **Ils ne disent pas vers quelle option tu penches** : un modèle qui le saurait irait dans ton sens. La mère l'ajoute si tu préfères. La garde de motifs du collisionneur rend une liste vide sur les trois fichiers ; je l'ai vue rouge sur un texte témoin avant de la croire verte.

---

## Relevé de méthode

**Chaîne de raisonnement.**
1. L'interdit : « aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur » (N-060 v3, point 4, `2b448f69…`) ; son origine : « étiquette de vérité à la lecture (fichier scellé que les moniteurs ne voient pas) […] sans filtrer un seul épisode » (N-060 v1, point 3, `4a09c5f5…`).
2. La boucle réapprend la sonde sur les épisodes que l'audit trouve endommagés (N-076, § 6.2, `49b664c1…` ; note sur l'attaquant informé, `c23a1034…`, l. 151).
3. Réapprendre est choisir des poids ; sur des verdicts de l'oracle, c'est le heurt de lettre (pas 1 et 2 ; N-075 v3, § 11, point 9, `5aed4bab…`).
4. Supposé, c'est une lecture de ton intention : tu veux pouvoir mesurer la boucle sur des organismes ; or le programme ne joue ses flux qu'au banc (N-076, § 6, « premier pas et dépense »). La coupe « banc ou service » ne sert donc pas cette intention.
5. Relue par la sonde qu'elle a instruite, la recapture vaut 1,00 quand le rappel vrai vaut 0,010 [calcul, A ; formule approchée Φ((Δ² + d/n)/√(Δ² + d/n + d/m) − z), retrouvée à 0,002 près par les tirages].
6. Épreuve puis leçon, et pli retenu, rendent le niveau des fausses alertes dans ce monde et suivent le vrai dans l'autre [calcul, A].
7. Le compte sur un audit orienté est biaisé : r·p₁/(r·p₁ + (1 − r)·p₀) [calcul, B] ; publié pour les tests diagnostiques (Arifin et Yusof, p. 2, 7, 9).
8. Supposé : la validité du plancher s'étend à une probabilité d'audit qui change selon des étiquettes passées, pourvu qu'elle soit connue au tirage et bornée par un plancher. Appui : « Blindfold », p. 3 et 5, règle adaptative à propension connue ; Li, Hays et al., p. 13. Preuves non lues.
9. Un seuil calé sur les témoins de la leçon sous-estime les fausses alertes [calcul, A].
10. Les négatifs décident de ce que la sonde apprend : l'identité du suspect, ou l'angle mort de l'oracle [calcul, E ; lois à étiquettes sans limite]. Supposé : les ordres de grandeur de l'écart d'identité et de la part cachée.
11. Sous la table du seuil (N-076, § 7), le nombre d'étiquettes au seuil est une binomiale de moyenne K·(1 − 0,05^(1/K)), qui tend vers ln 20 [calcul, C1].
12. Le rappel après ajustement dépend du nombre d'étiquettes et de la dimension de ce qu'on ajuste [calcul, C2 et C3]. Supposé : une réserve qui porte la moitié de l'écart ; un écart de 4 ; la dimension 4 096.
13. Des étiquettes mêlées d'échecs honnêtes diluent la leçon [calcul, C4]. Supposé : la part d'un sixième, lue dans un monde d'illustration d'une note sœur (`6cbc8f49…`, § 7).
14. Des pas 5 à 10 : la règle en douze clauses. C'est une proposition, non un résultat.
15. Supposé : aucun texte scellé du dépôt n'écrit déjà un audit suivi d'un réapprentissage ; je n'ai ouvert aucun préenregistrement.
16. « Rien à revendiquer » : Rudoler et al. et les pièces de la section 8, par onze requêtes et mes lectures.

**Objets de contrôle.**
- *La recapture comme preuve que la sonde s'est rétablie.* Objet où c'est faux, un dommage sans trace : prévu, épreuve puis leçon et pli au niveau des fausses alertes, relecture proche de 1 ; rendu 0,010, 0,010 et 1,000 ; la relecture « réussit » là où la conclusion est fausse : morte. Objet où c'est vrai, un écart de 4 et trois cents étiquettes : prévu, vrai près de 0,58 ; rendu 0,581, pli 0,504, fin de suite 0,545 [calcul, A].
- *Le compte sur l'audit.* Sain, tirage sans égard au score : prévu le vrai, rendu 0,200. Artefact, audit orienté : prévu 0,714, rendu 0,714 [calcul, B].
- *Le seuil.* Prévu 0,24 et 0,06 de fausses alertes réelles à trois cents et trente étiquettes ; rendu 0,230 et 0,066 [calcul, A].
- *Le canal de retour.* Artefact, un écart qui change de direction à chaque épisode : prévu, suite au niveau des fausses alertes ; rendu 0,010 [calcul, A3].
- *Les étiquettes au seuil.* Prévu, une moyenne entre 2,8 et 3,0 et une probabilité nulle de 0,05 par construction ; rendu [calcul, C1].
- *L'échelle.* Prévu, croisement vers 103 étiquettes ; rendu 109. Les formules approchées contre des tirages : écarts de 0,011 au plus sur les cases vérifiées [calcul, C2].
- *Les négatifs.* Prévu 0,0049 et moins de 0,0001 pour les dommages cachés, plus de 0,99 pour l'identité ; rendus 0,0049, 0,00004, 0,996. Sain : 0,010 [calcul, E].
- *L'oracle informé.* Sain, oracle parfait et aveugle : prévu le rappel et la précision vrais, rendus 0,200 et 0,690 [calcul, F].
- *Ma recherche en ligne.* Objet vrai : une pièce que je savais au dépôt (Rudoler et al.) est revenue en tête d'une requête. Objet faux : une pièce que Rudoler et al. citent (Kumar et Singh, 2026) n'est pas revenue : « non trouvé » ne dit donc rien de l'existence.
- *La garde de motifs.* Rouge sur un texte témoin portant un chemin, un identifiant d'accord et un identifiant de registre ; verte sur les trois fichiers.
- Prévisions écrites dans le code avant l'exécution ; rien de scellé avant. Ce sont des contrôles d'arguments, non de mesures.

**Premier pas non justifié.** Le pas 4 est une lecture de ton intention : seul ton mot le justifie. Parmi les pas de fond, le pas 8 : il faudrait la preuve du théorème sur les règles adaptatives de « Blindfold » (son annexe D), ou une re-dérivation par un agent qui ne reçoit que l'énoncé. Viennent ensuite le pas 10 (une mesure sur organismes de l'écart d'identité et de la part cachée) et le pas 12 (ce qu'une réserve voit d'une attaque neuve).

**Mode d'échec affecté.** Sans objet : pièce d'auteur, non de relecteur.

**Dérivation de l'énoncé seul.** Sans objet : pièce d'auteur, non d'agent de re-dérivation.

**Trouvaille de côté.**
- **L'anti-circularité du § 7 du programme** (« une sonde n'est jamais entraînée et évaluée sur les mêmes organismes ») est contredite par la boucle comme par la ligne « asymétrie d'apprentissage » du § 9 du même programme. Le rôle des épisodes la répare aussi : entière pour les verdicts, levée par déclaration pour un flux (décision D-4).
- **Les lecteurs de l'oracle sont dits « aveugles à la condition »** (N-060 v3, point 1), pas au score ni à la raison du tirage. Depuis que l'audit peut suivre le soupçon (N-076, § 6.1), ce n'est plus la même chose.
- **Le plancher fait des prises un tirage au hasard parmi les dommages vus** : la probabilité d'étiquetage d'un positif est connue par construction (le taux du plancher fois la probabilité de reconnaissance). C'est l'hypothèse sous laquelle on apprend avec des positifs seuls et le reste sans étiquette (Bekker et Davis, p. 7 et 9). Non poursuivi.
- Une équipe laisse l'équipe rouge produire les épisodes qui calibrent le seuil, pour voir (Cooper Stickland et al., p. 11) : un appui externe à « témoins exogènes ». Non poursuivi.
- La note sur ce qui reste après la publication du plancher propose de relire le passé après l'alarme : le pli retenu en est la mesure honnête (clause 4).

**Évaluateur et conseil.** Ce qui juge cette note : toi, la mère, puis le collisionneur ; aucun juge admis sur témoins. Par où elle serait bien jugée sans le mériter : douze clauses et cinq aveugles se lisent comme de la rigueur, et l'accord avec une grille médicale est « trop beau » (R4) : le rapprochement est de moi, et la grille ne connaît pas d'adversaire. Mes mondes sont gaussiens, à une direction ; de vrais états ne le sont pas. Presque toutes mes citations viennent de la première page ou de lignes trouvées par motifs. Conseil à qui reprendra : donner à un relecteur hostile le mode « garantie qui suppose ce qu'elle prouve », visé sur le pas 8 et sur la clause 2 (le score est-il vraiment consigné avant le verdict ; une normalisation partagée refait-elle entrer les étiquettes) ; et le mode « fuite de la vérité », visé sur la clause 5 (un compte rendu trop souvent livre les verdicts par différence ; une lignée lisible les livre tous).

---

## Ce que je n'ai pas fait

- **Aucune mesure.** Tous mes chiffres supposent leurs entrées ; rien n'est contre-lu.
- **Lectures partielles.** Rudoler et al. : pages 10, 11 et 17 à 24 non lues, figures non regardées. « Blindfold » : lignes trouvées par motifs, preuves non lues. Les autres pièces : page 1 ou motifs (table de provenance).
- **Recherche bornée** : un moteur, l'anglais, onze requêtes ; ni index de citations, ni actes de conférences.
- **Sources de mémoire**, sans pièce : l'évaluation « préquentielle » ; l'analyse circulaire ; la variance de la validation croisée.
- **Non ouverts** : tout préenregistrement ; les textes du bras A ; la décision sur le mode tenu à l'écart ; les notes sur l'adjudant, la pince, la science de la détection et les asymétries, connues par les deux décisions lues ; le reste de la note sur l'attaquant informé. Je ne sais pas si un harnais d'audit existe en code.
- **Le collisionneur n'est pas lancé** ; c'est à la mère, après sa relecture de cloisonnement.
- **Routine de reprise** : non faite, elle revient à la mère. Rien n'est commité.

## Annexe : travaux cités

Table complète, pages lues et empreintes : `docs/sources/pdf/protocole-x-boucle-audit-recapture-v1/provenance-protocole-x-boucle-audit-recapture-v1.md`.

- **Versés ce jour** : Podkopaev, Ramdas, « Sequential Predictive Two-Sample and Independence Testing », arXiv 2305.00143v2 ; Dwork et al., « Generalization in Adaptive Data Analysis and Holdout Reuse », 1506.02629v2 ; Ensign et al., « Runaway Feedback Loops in Predictive Policing », 1706.09847v3 (versé, non cité dans le texte) ; Kossen et al., « Active Testing: Sample-Efficient Model Evaluation », 2103.05331v2 (versé, non cité dans le texte) ; Pendlebury et al., « TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time », 1807.07838v4 ; Bekker, Davis, « Learning from positive and unlabeled data: a survey », 1811.04820v3 ; Arifin, Yusof, « Correcting for partial verification bias in diagnostic accuracy studies: A tutorial using R », 2509.12217v1 ; Zrnic, Candès, « Cross-Prediction-Powered Inference », 2309.16598v3 ; la grille QUADAS-2, copie de la page de l'université de Bristol ; Dal Pozzolo et al., « Credit Card Fraud Detection: a Realistic Modeling and a Novel Learning Strategy », copie d'auteur.
- **Déjà au dépôt, relus ce jour** : Rudoler et al., « Improving scalable oversight with co-trained monitors », 2609.36049v1 ; Lyons Keenan, Leckie, Erfani, « LLMs Learn to Evade Latent Monitors from Prior Feedback Alone », 2609.36490v1 ; Zhu, Zuo, Sun, « Blindfold », 2610.37055v1 ; Li, Hays, Ramdas, Raghavan, « Controlling the Probability of Unknown Unknowns in Pre-Deployment Testing of AI Systems », 2611.15835v1 ; Taufeeque, Heimersheim, Gleave, Cundy, « The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes », 2602.15515v2 ; Cooper Stickland et al., « Async Control: Stress-testing Asynchronous Control Measures for LLM Agents », 2512.13526v1 ; Conférence internationale d'harmonisation, « Statistical Principles for Clinical Trials (E9) », 1998 ; par motifs seulement, et non cités dans le texte : Gupta et Jenner (2506.14261v4), Wehner et Fritz (2510.21531v1), Westphal et al. (2606.09411), Bailey et al. (2412.09565v2).
- **Page web, moteur, mémoire** (non opposables) : Marcellino, « Testing few-shot coup probes », billet du 19 janvier 2026 ; Dawid (1984) ; Begg et Greenes (1983), d'après Arifin et Yusof ; Kumar et Singh (2026), d'après Rudoler et al., p. 9.

---

## Décisions pour toi

**D-1. Le point 9 de la décision sur le plancher et les deux regards : retenir (b′), l'option (b) écrite par rôle d'épisode et par ordre.** Enjeu : un invariant de l'oracle change de lettre, et la boucle que tu as inscrite devient mesurable sur des organismes. (a) Restreindre la ligne du programme et garder l'invariant entier : avantage, rien ne change ; inconvénient, la boucle ne se mesure qu'avec des étiquettes de construction, jamais avec celles de l'oracle. (b) Telle qu'écrite, « au banc » contre « en service » : avantage, une phrase ; inconvénient, la coupe ne sépare rien pour un programme sans service, et rien n'y garde la recapture. (b′) Le texte de la section 5 et ses douze clauses : avantage, l'interdit garde toute sa lettre là où un verdict se joue, et la recapture reste aveugle par construction ; inconvénient, un harnais à lignées et à rôles, et un texte de plus à contre-lire. Recommandation : (b′). Confiance 0,7. Modification d'un invariant : nœud, pas de défaut ; d'ici là, la lecture de N-076 s'applique (aucune sonde du programme n'est réapprise sur des verdicts de l'oracle).

**D-2. Écrire la règle et ses douze épreuves comme pièces à part.** Enjeu : sans elles, tout texte qui écrit la recapture bute sur le heurt. (a) La règle écrite par le concepteur et contre-lue par un autre modèle ; les douze épreuves écrites comme instruments, sur mondes plantés, sans dépense, en commençant par la troisième, la quatrième et la sixième : avantage, la crainte « la recapture ne juge plus à l'aveugle » devient un refus du harnais ; inconvénient, du travail sur un chantier actif. (b) Attendre le collisionneur. Recommandation : (a). Confiance 0,75. Défaut sous 48 heures : (a), pour l'écriture seule ; la règle n'entre en vigueur que par ton mot sur D-1.

**D-3. Jouer d'abord la boucle avec les étiquettes de construction, au taux du plancher.** Enjeu : une dépense, et la première mesure de la boucle sur de vrais états. (a) Instruire le devis de l'étape 1 de la section 7, sur une famille de sabotage propre au flux, comme extension déclarée de l'épreuve de récupération après réentraînement : avantage, aucun invariant de l'oracle touché, et la borne haute est connue avant de décider de l'étape 2 ; inconvénient, un bras de plus. (b) Passer directement aux étiquettes de l'oracle après D-1. (c) Rester aux mondes plantés. Recommandation : (a). Confiance 0,65. Dépense : nœud, pas de défaut.

**D-4. Fermer les deux heurts voisins.** Enjeu : deux textes du programme. (a) Écrire que l'anti-circularité du § 7 vaut entière pour tout épisode de verdict et se lève, par déclaration, dans un bras de flux ; et ajouter au point 1 de la décision sur la vérité du dommage que les lecteurs sont aveugles au score, à la version et à la raison du tirage : avantage, deux contradictions de moins avant d'écrire la recapture ; inconvénient, deux retouches de textes qui font foi. (b) Les laisser écrits ici. Recommandation : (a). Confiance 0,7. Modification du programme et d'une décision : nœud, pas de défaut.

**D-5. Rapporter la boucle par l'échelle des échelons, et dire le compte des étiquettes.** Enjeu : la façon de dire ce que la boucle rend. (a) Dans tout texte à venir qui écrit la boucle : le nombre d'étiquettes que le plancher livre au seuil toléré ; les échelons joués du moins cher au plus cher ; la table à quatre cases au lieu de la recapture seule ; « hors couverture : muette » : avantage, aucune promesse de rétablissement sans son budget d'étiquettes ; inconvénient, des phrases plus longues. (b) Garder « le rappel retrouvé en fonction du nombre d'épisodes endommagés audités » sans plus. Recommandation : (a). Confiance 0,75. Défaut sous 48 heures : (a), sans toucher un texte scellé.

**D-6. Aucune phrase sur la boucle hors du dépôt avant la lecture en entier de quatre voisins**, et cinq citations de plus là où la boucle est présentée : Rudoler et al. (lu ici pour quatorze pages sur vingt-quatre), Taufeeque et al., Cooper Stickland et al., Podkopaev et Ramdas ; et la grille des études diagnostiques, citée comme source de la forme. (a) Lecture par un agent neuf d'un autre modèle, avec verdict d'antériorité sur la règle et sur le compte des étiquettes ; (b) s'en tenir à cette note, tout y restant question. Recommandation : (a). Confiance 0,8. Défaut sous 48 heures : (a).
