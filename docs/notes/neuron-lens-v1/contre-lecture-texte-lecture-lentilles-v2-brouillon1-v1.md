# Contre-lecture du brouillon 1 de la version 2 du préenregistrement « lecture, par la lentille publique et par nos lentilles R et S, des directions des sondes apprises sur la tâche » — v1

- Heure (`date -u`) : commencée le 2026-11-19 vers 10:28Z, arrêtée sur un refus d'outil, reprise à 10:35Z sur le mot de la session
  mère, finie à l'heure du pied.
- Contre-lecteur : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, modèle Fable 5.2 (`claude-fable-5-2`),
  autre modèle que le rédacteur (Opus 5.5). Il n'a écrit ni la version 1, ni la version 2, ni le devis du réajustement, ni le critère
  d'identité, ni le texte gelé de la tranche, ni son verdict ; il ne sera ni développeur, ni opérateur, ni lecteur de ce texte.
- Pièce relue, classe A (préenregistrement) : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon1.md`, branche
  `claude/brave-galileo-jhp684`, commit `8a22361e7c6f854a9c5085e85f9dca47dd098f14` (daté 10:27:59Z), empreinte recalculée
  `d6c3a6eedac25d8e2965730ea266c1674ad7b48272a577e7878bf7351838f3ab`, 1 469 lignes. Les numéros de ligne ci-dessous sont les siens.
- Lu, empreintes recalculées : la version 1 scellée (`prereg/lecture-sondes-bbis-par-lentilles-v1.md`, branche principale,
  `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`, 813 lignes ; elle n'est pas dans l'arbre du commit `8a22361e`) ;
  le critère d'identité du réajustement, version 2 (`fc706d8e5bd0bb75942e17844a450ca82520972746e1b7233881817a8c3f679c`, commit
  `de836897`), entier ; sa contre-lecture (`9241903708eacef5244bf81b0b071131edab0023195d8a068dc7051cd57883ff`, l. 1-215) ; la
  vérification de ce critère (`docs/notes/neuron-lens-v1/verification-critere-identite-reajustement-v2-v1.md`,
  `8a6045bb3db81188e9c0889fbd69bafa57085c5336bff6db7dec7e24de1a4f94`, l. 1-40 et 164-205) ; l'erratum du devis
  (`c7915a23402515cdc2a4af61be74993cff32b69ff4b634868383ab1d14c8f6f9`) ; la note de place (`a6e91e25…`), entière ; du devis version 2
  (`49dcbc93…`), les paragraphes 4 à 6 ; de la vérification du devis (`3cc64c86…`), les l. 40-115 ; du texte gelé de la tranche
  (`f5d46860…`, un préenregistrement), les l. 74-88, 107-165, 236-250, 314-324, 440-452 ; de la copie versée du document de conception
  du code voisin (`docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/docs-design.md`,
  `88478b63fbed3dd8654a4da845c356ddc3f9ec0ffb5f7ba6d00b5f0b6b6a45e5`), les l. 20-60, 148-158, 174-186 ; le gabarit (`8cad4371…`) et le
  validateur (`3b2e3ee5…`) ; de `registres/go.md` (branche principale), les lignes GO-2026-11-19-16, -26, -28 et -33.
- Non lu : le verdict de la tranche de l'ajustement de nos lentilles (lecture refusée, voir la réserve) ; les deux pièces de la course de
  la tranche sous `diag/` (interdites par mon mandat) ; le code voisin lui-même (`transport.py`, `lenses.py`, `reads_at_firings.py` : aucune
  copie n'est versée au dépôt) ; le registre propre de la version 1 (lecture refusée au rédacteur ; non tentée) ; `docs/verdicts/`,
  `diag/`, `runs/`, `donnees/`, tout verdict, table ou résultat de l'apprentissage des sondes sur la tâche, tout résultat de la première
  passe, tout fichier « consigne-privee » ou « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/`.
- Vu sans ouvrir : les noms des dossiers de `/home/user/` (une commande de recherche les a listés) ; le nom d'un fichier de la course de
  la tranche dans une liste de chemins ; les quelques valeurs de la tranche que la vérification du devis cite dans sa réserve N-1. Aucune
  n'est reprise ici.
- Aucune dépense, aucune machine, aucun modèle chargé, aucun réseau hors `git fetch`, aucun commit, aucun fichier existant modifié.
  **Un refus d'outil**, texte exact en annexe A.

## Réserve en tête

**La table des valeurs de nos lentilles et les réserves (R-a) à (R-f) ne sont pas vérifiées contre le verdict de la tranche : lecture
refusée par le classifieur des permissions, texte exact en annexe ; vérification à faire par un lecteur que Lazar désignera.** Sont dans
le même cas les deux valeurs que le brouillon reprend de ce verdict comme repères (l. 811, garde du montage ; l. 987, déclencheur
d'audit) et l'attente A-5 (l. 418). La copie du verdict extraite dans mon bloc-notes a été supprimée sans avoir été lue.

Autre limite, de même nature : tout ce que le brouillon tire du code voisin (indice de couche de nos lentilles, orientation de la
matrice de notre S, forme des fichiers d'ajustement, `Accumulator.mean`) n'a pas pu être vérifié, faute de copie versée de ce code. Je
m'appuie, là où je le dis, sur son document de conception, qui est versé.

## Conclusion

**Pas avant : six corrections bloquantes (B1 à B6) — alignement sur le critère d'identité, déclaration d'exposition, entrées de
contre-lecture de la version 2, contradictions de la liste d'arrêt, règle de la reproduction, valeurs du verdict de la tranche non
vérifiées.** Le plan de mesure lui-même est solide : mêmes directions, mêmes nuls, mêmes niveaux que la version 1, aucune revendication,
aucun repli silencieux trouvé. Quatorze corrections non bloquantes suivent.

## Verdict par point

### 1. Règle du préenregistrement (R1) : tout est-il fixé pour la seconde passe ? — **presque ; quatre marges restent.**
Fixés sans ambiguïté : l'objet (descriptif, aucune hypothèse soumise à un seuil), les attentes A-5 à A-9 avec ce qui les réfute, les
métriques (lecture par notre R par la fonction de la version 1 ; lecture par notre S ; recouvrement des vingt premiers jetons et son p),
les niveaux de libellé (repris tels quels), les graines (mêmes clés, donc mêmes directions nulles pour toutes les lentilles), l'ordre des
lignes de registre, les phrases gelées, la liste d'arrêt. Marges après coup :
1. « le nom que lui donnera le critère scellé » (l. 310, 566) : une case ouverte, que le critère a fermée depuis (B1).
2. Au palier 2, rien ne dit quelles couches sont lues si la stabilité ne tient pas dans les deux ajustements, alors que le critère
   l'exige (B1-e).
3. Si la reproduction de la première passe diffère, la lentille publique porte deux libellés pour une même lecture, et le texte ne dit
   pas lequel entre dans « lecture commune » (B5).
4. Le code de la version 1 est « réemployé tel quel si son interface l'accepte, sinon version neuve » (l. 1239-1241) : dans le second
   cas, « même code » ne tient plus pour la reproduction (non bloquante n° 13).
Le validateur rend une liste vide, mais pour une raison qui ne vaut pas preuve (B3).

### 2. Exposition — **déclarée, mais à moitié : elle ne couvre que deux parties sur six (le rédacteur et l'auteur de la version 1 ; manquent Lazar, les deux sessions et les contre-lecteurs), et pas la décision elle-même.**
Ce que le texte peut avoir appris des résultats. Par son rédacteur : rien de la chaîne des sondes, s'il dit vrai, et rien ne le
contredit ; il a lu en entier le verdict de la tranche des lentilles, ce qu'il déclare, et ses attentes A-5 à A-7 et deux déclencheurs
d'audit en viennent, ce qui est légitime (ce sont des faits sur l'outil, pas sur les sondes). Par les autres : le texte ne le dit pas.
Ce qu'un lecteur sceptique conclurait :
1. **La décision d'ajouter la seconde passe est postérieure au verdict.** Le mot de Lazar (GO-2026-11-19-33) est de 10:05:29Z ; la clé
   `VERDICT-BBIS` est inscrite depuis 00:13:25Z (l. 53). Le texte raisonne sur la manière de lire, jamais sur le fait d'avoir choisi
   d'ajouter une lecture après avoir vu le verdict. Il ne peut pas l'exclure ; il doit le dire.
2. **Deux sessions sont appelées « la mère »** : la session des lentilles, qui a mandaté le rédacteur (l. 3), et la session principale,
   qui scelle, inscrit les lignes et relaie les corrections. La déclaration demandée (l. 262-264) n'en vise qu'une, sans dire laquelle.
3. **Le mandat du rédacteur est « non versé »** (l. 4) : un lecteur ne peut pas vérifier que les demandes ne portaient aucun choix fait
   au vu d'un résultat. La version 1 citait son mandat par chemin et empreinte.
4. **L'état de la première passe au scellement n'est pas écrit.** Le texte sera scellé après la première passe ; le rédacteur dit
   qu'aucune table n'existait « à la connaissance de la mère ; non vérifié » (l. 245-246). Il existe pourtant une ancre : le brouillon 1,
   avec son empreinte, est dans un commit daté de 10:27:59Z. Si la ligne `TABLES-LENTILLES-BBIS` est postérieure, les choix neufs
   (nuls partagés, recouvrement, k = 20, niveaux) sont datés d'avant toute table de la première passe.
5. **La retenue de la lecture humaine est une règle d'un texte non scellé** qui prétend lier avant son scellement, et sa sanction vise
   la mauvaise cible : elle « invalide » une lecture de la première passe conforme à la version 1 scellée, alors que ce qui serait
   exposé, c'est la seconde passe.
Les choix neufs ont-ils pu être faits au vu d'un résultat ? Rien ne l'indique : les nuls partagés prolongent l'appariement de la
version 1 (plan, point 9), le recouvrement reprend k = 20 et les niveaux de la concentration, la seconde passe découle de la décision de
Lazar. Mais c'est une affirmation, pas une démonstration, tant que les cinq points ci-dessus ne sont pas écrits. Texte à écrire : B2.

### 3. La condition « mention d'identité » — **non conforme au critère version 2 : le texte laisse lire nos lentilles comme si le verdict du 18 novembre les couvrait.**
Ce que dit le critère (`fc706d8e…`, § 3 à § 5) et ce qu'en fait le brouillon :

| palier du critère | ce que le critère autorise | ce que le brouillon écrit | écart |
|---|---|---|---|
| 1, « même lentille, octets identiques » | les mesures et le verdict du 18 novembre décrivent la lentille ; phrase permise fixée ; audit déclenché (résultat trop propre) | lue ; « même lentille que celle jugée par la tranche » (l. 565) | phrase à remplacer par la phrase permise ; l'audit du critère n'est pas exigé avant la lecture ; la reprise sur sauvegarde suit encore le devis |
| 2, « différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables » | identité **non établie** ; le verdict du 18 **ne se transporte pas** ; Lazar averti dans ces termes avant tout usage ; sans course rejouée, aucune mesure propre ; couche stable seulement si elle l'est dans les deux ajustements ; phrases permise et interdites fixées | « lentille équivalente, octets différents » (l. 309, 566) ; « le verdict de la tranche ne la couvre que par cette concordance » (l. 568, 952-953) ; verdict de la tranche et réserves recopiés comme ceux de « nos lentilles » (l. 954-958) ; « seule une concordance […] la rattache à V » (l. 1137) | le mot « équivalente » est interdit ; « couvre par concordance » et « rattache » transportent le verdict ; les réserves prêtent à la lentille lue des mesures faites sur une autre |
| au-delà, « différente » ; préalable manqué, « non comparable » ; anomalie ou contrôle d'audit manqué, mention suspendue ; « non réajustée » | aucune lecture sans nœud de Lazar | « différente » et absente : non lue (l. 569-573) | « non comparable » et mention suspendue manquent |
| dans tous les cas | texte de lecture neuf, contre-lu, qui recopie la mention **et l'écart mesuré** ; le billet dit le palier obtenu | la mention est recopiée de la fiche ; l'écart ne l'est pas | la fiche de rangement ne porte pas l'écart |

Cause : le rédacteur a travaillé sur le paragraphe 4 du devis, que l'erratum (`c7915a23…`) dit **remplacé** par le critère. Le nœud N12
en hérite (« presque vide à la tolérance proposée » vise l'ancienne tolérance). Corrections : B1.
À noter : la vérification du critère version 2 (`8a6045bb…`) conclut « pas avant : sept corrections », dont une (D5) réécrit la phrase
permise du palier 2 et rend obligatoires des chiffres de plus pour la lentille R. Le texte de lecture doit donc citer le critère **dans
sa version scellée** et ne peut pas être scellé avant lui.

### 4. Symétrie et replis (R4, R5) — **symétrie tenue pour les lectures, incomplète pour les comparaisons ; aucun repli silencieux trouvé ; huit essais manquent.**
- **Symétrie.** L'audit de la seconde passe a ses deux sens (« trop beau », « tout négatif », l. 985-993). Manquent quatre déclencheurs,
  tous du côté des comparaisons, qui sont l'objet neuf : reproduction de la première passe différente (aujourd'hui une réserve sans
  audit, alors que le même code et les mêmes graines sur un processeur devraient rendre les mêmes libellés) ; recouvrement nul entre les
  deux lentilles R pour plus de la moitié des directions de la couche 23 (le pendant du « 20 sur 20 pour plus de la moitié ») ;
  recouvrement des deux moitiés de notre R inférieur à celui entre les deux lentilles R pour plus de la moitié des directions (signe
  d'une matrice mal rangée) ; palier 1 obtenu sans audit du critère versé. Non bloquante n° 2.
- **Replis.** Tous ceux que j'ai trouvés sont écrits : première passe non calculée, remplacée et dit (l. 896-897) ; lentille non lue,
  motif en tête (l. 577-578) ; nuls refaits par direction pour trois lentilles, recouvrement des moitiés « non calculable » (l. 861-864) ;
  calibration du recouvrement hors borne, « non calculable » (l. 869-870) ; jamais un autre fichier, une autre révision, un fichier
  exporté ou une lentille d'un tiers (l. 1035). Un risque d'arrêt à tort : non bloquante n° 8.
- **Gardes, cas sain et artefact** (seconde passe ; les gardes reprises de la version 1 ont été contre-lues avec elle) :

| garde (liste d'arrêt, l.) | cas sain écrit | artefact écrit | état |
|---|---|---|---|
| ouverture d'une table avant le scellement ou l'abandon de la version 2 (1031) | non | oui, pour le code (l. 1262) | cas sain à ajouter (ouverture permise après la ligne) ; la part humaine est tenue par les rôles, c'est dit |
| lignes `SCELLEMENT-`, `GO-`, `CODE-LENTILLES-BBIS-V2` absentes (1032) | non | non | **essai manquant** (la version 1 a le sien pour ses propres lignes) |
| `RANGEMENT-NOS-LENTILLES-BBIS` absente ; fiche altérée, révision courte, deux empreintes différentes (1033) | implicite | oui (l. 1244-1245), sauf la ligne absente | essai « ligne absente » à ajouter ; contradiction sur « mention absente » (B4-b) |
| mention qui interdit la lecture (1034) | oui (l'autre lentille et la lentille publique restent lues) | oui (l. 1245-1246) | à refaire sur les mentions du critère ; « non comparable », mention suspendue, critère non scellé : essais manquants |
| fichier introuvable à la révision ; essai d'un octet refusé (1035) | implicite | refus oui ; fichier introuvable non | essai « introuvable » à ajouter |
| empreinte ou taille sur le flux différentes (1036) | oui (extraction égale au chargement entier) | oui (un octet changé ; empreinte du 18 novembre) | tenu |
| forme de l'archive (1037) | oui (ordre des enregistrements à la version installée) | oui : compressé, non contigu, classe hors liste ; non : archive illisible, décalage non nul | deux artefacts à ajouter |
| `meta`, comptes de documents, formes (1038) | oui (faux fichier) | oui (l. 1250) | tenu ; la `meta` de S attendue n'a pas été relevée (non bloquante n° 7) |
| matrices non finies, moitiés égales, R égale à l'identité ou à la lentille publique, S égale à R ou à sa transposée (1039) | implicite (bout en bout) | oui (l. 1251) | tenu ; le seuil s'appuie sur un repère du verdict de la tranche, non vérifié |
| fonction de lecture de notre R, de ses moitiés, de notre S (1040) | oui | oui (couche suivante ; transposée ; matrice de sortie à la place des plongements) | tenu pour R ; pour S, le « chemin indépendant » est écrit par le même développeur et partage l'hypothèse d'orientation (non bloquante n° 4) |
| `model.embed_tokens.weight` absent, d'une autre forme, d'un fichier d'une autre empreinte (1041) | non | non | **essai manquant** |
| empreinte de E-1 ou E-2 différente entre les deux passes (1042) | non | non | **essai manquant** |
| reproduction de la première passe (1043) | oui | oui (l. 1261) | tenu ; tables de la première passe d'une autre empreinte que leur ligne de registre : règle et essai manquants (B5) |
| clé d'écriture du dépôt de rangement dans la session (1044) | non | non | en partie codable (présence d'une variable d'environnement d'un autre nom) : à dire ou à essayer |
| espace et durée (1045) | implicite | oui (l. 1263) | tenu |
| garde du rapport à ε étendue à trois lentilles ; moitiés « non calculables » (plan, 6) | non | non | **essai manquant** |
| calibration du recouvrement, borne haute seule (plan, 6) | oui | oui (l. 1259-1260) | tenu ; l'argument de la borne haute est juste (annexe C) |
| indice de couche de nos lentilles (plan, 6) | oui | oui (l. 1255) | tenu, par convention pour le sens de l'indice |

### 5. Multiplicité — **aucune correction, ce qui se défend pour un texte descriptif ; mais la seconde passe double les occasions de phrase de « soupçon », et une phrase gelée se lira comme une revendication.**
- Comptes, au plus (quarante vecteurs, deux signes, quatre lentilles) : 320 lectures pour la concentration, 320 pour la part au-dessus
  du nul, 640 tests de famille, 80 recouvrements de la paire principale. Attendus par le seul hasard, par la règle du texte : au plus
  0,32 ; 0,32 ; 6,4 ; 0,08. La première passe seule avait au plus 3,2 familles « sur-représentées » par hasard. **Le seul libellé où le
  hasard pèse est la famille** : jusqu'à six phrases « la lecture ajoute un soupçon » peuvent sortir sans rien derrière.
- Les nuls partagés ne gonflent pas le nombre de tests ; ils corrèlent les p (entre directions d'une couche, et désormais entre
  lentilles pour une direction). La borne « attendu par hasard » reste juste **en espérance** ; la dispersion autour d'elle est plus
  large que pour des tests indépendants. Le texte dit la dépendance (l. 679-681) ; il ne dit pas cette conséquence.
- Le recouvrement ajoute une paire libellée (publique, notre R) et deux paires rapportées sans libellé (notre R et logits ; moitiés),
  plus des corrélations sans libellé : la séparation « libellé / rapporté » est nette dans « Seuil » (l. 709-718).
- **Ce qui porte une phrase** : concentration, part, familles, pôles, comparaison appariée, et les quatre libellés entre lentilles.
  **Ce qui reste en table** : corrélations, paire avec les logits, moitiés, témoin de couche, différence des deux recouvrements, jetons
  communs par pôle. Aucune revendication n'est annoncée, mais la phrase gelée « la lecture […] tient d'une lentille R à l'autre »
  (l. 971) sera lue dans le billet comme une revendication de robustesse.
- Asymétrie du libellé entre lentilles : « lecture commune » exige trois conditions, dont un recouvrement au-delà des deux nuls ;
  « lecture propre à une lentille » n'en exige que deux. Là où les deux lentilles lisent presque pareil toute direction (ce que le
  rédacteur attend à la couche profonde), les directions nulles se recouvrent déjà beaucoup, le p du recouvrement plafonne, et une
  direction lue de même par les deux tombe en « mixte, rapporté sans conclusion ». C'est prudent, pas faux ; il faut que le lecteur voie
  le plafond. Non bloquantes n° 5 et 6.

### 6. Les cinq nœuds ouverts pour le directeur — **N14 et N15 bien posés ; N11 incomplet ; N12 mal posé ; N13 sous-dit.**

| nœud | bien posé ? | recommandation | confiance |
|---|---|---|---|
| **N11**, texte exposé | incomplet : l'enjeu oublie que la décision d'ajouter la passe suit le verdict (point 2) ; l'option (b) est mal décrite : le lecteur de la seconde passe doit **déjà** n'avoir lu aucun verdict de l'apprentissage des sondes sur la tâche (« mêmes conditions que celui de la première », l. 1080, et l. 1061) ; (b) n'ajoute donc que « ni le billet », presque sans coût | **(b)**, avec la déclaration B2 | 0,7 |
| **N12**, lecture au palier 2 | mal posé : ancienne tolérance, mot « équivalente », « couvre par concordance ». À réécrire (B1-j) : au palier 2 l'identité n'est pas établie, le verdict du 18 novembre ne se transporte pas, et sans course rejouée la lentille lue n'a aucune mesure propre | **(b) réécrite** : lire au palier 2 sous la phrase permise du critère scellé, après une ligne de registre disant que Lazar a été averti dans les termes du critère, écart mesuré compris ; écarter l'ancienne option (c) ; défaut (a) juste | 0,55 |
| **N13**, notre S côté entrée | bien posé, enjeu sous-dit : la cible lue n'a aucune mesure de fidélité ; au palier 2, S n'a aucune ancre de position (critère, § 3) ; et le document de conception du voisin réserve l'usage de S côté entrée aux premières couches (jusqu'à la couche 8 d'un modèle de 36) | **(a)**, avec trois ajouts : la réserve du domaine d'usage, citée ; aux couches 15 et 23, la phrase de « soupçon » de S remplacée par « rapporté sans conclusion » ; la référence « plongements seuls » (non bloquante n° 4). Défaut (a) acceptable : GO-2026-11-19-33 nomme R et S | 0,55 |
| **N14**, calendrier du billet | bien posé ; l'option (c) est une décision de dépense, qui relève du devis et non de ce texte : le dire | **(a)** ; la phrase du billet dit aussi que le texte a été scellé après le verdict | 0,75 |
| **N15**, clé de lecture du dépôt de rangement | bien posé ; le devis (§ 5, point 3) suppose déjà que la clé gardée de la session relit ce dépôt | **(a)** si la clé gardée est une clé de lecture seule du compte de Lazar, ce que l'essai d'un octet confirme ; sinon **(b)** ; défaut juste | 0,6 |

### 7. La version 1 est-elle gardée mot pour mot ? — **oui pour le fond ; « 15 lignes prolongées » est inexact ; la première passe change par la procédure, pas par les mots.**
Contrôle par programme (annexe B) : 799 lignes égales, 0 supprimée, 15 touchées, 460 insérées. Des 15 lignes touchées :
- **10 sont prolongées** au sens strict (le début est intact, un ajout « v2 » suit) : lignes 182, 320, 351, 356, 358, 385, 476, 478,
  480 et 600 de la version 1 ;
- **5 sont réécrites** : le titre (l. 1) ; l. 147, « **n'entrent pas dans ce texte**. » devenu « **n'entrent pas dans la première
  passe** (v1) ; elles entrent dans la seconde (v2, ci-dessous). » ; l. 263, « (seule lentille ajustée lue par ce texte) » devenu
  « (seule lentille ajustée lue par la première passe ; lue aussi par la seconde) » ; l. 321-322, mêmes mots, gras retiré, étiquette
  « v1 (première passe), inchangé » ajoutée.
Aucune de ces réécritures ne change le sens de la première passe. Ce qui la change est ailleurs :
1. la **retenue de sa lecture humaine** (plan, point 1, l. 733-736), déclarée ;
2. la **ligne d'arrêt neuve** (l. 1031) qui invalide une lecture conforme à la version 1 (B2, B4-c) ;
3. « si la première passe n'a pas été calculée, la seconde la remplace » (l. 896-897), déclaré ;
4. une **contradiction** : la phrase « les lignes ci-dessus valent aussi pour la seconde passe » (l. 1026) reprend la première ligne de
   la liste (« `VERDICT-BBIS` déjà présente à son inscription : rien ne part », l. 999), alors que le plan inscrit le scellement de la
   version 2 « alors que `VERDICT-BBIS` est présente » (l. 737) (B4-a) ;
5. rien ne dit **lequel des deux textes gouverne la première passe** une fois la version 2 scellée (B4-c).

## Corrections bloquantes (texte avant et après)

### B1 — Aligner la condition d'identité sur le critère scellé
Règle d'ensemble : le texte cite le critère d'identité **dans sa version scellée** (chemin, empreinte), recopie ses mentions et ses
phrases permises mot pour mot, et n'est scellé qu'après lui. Les « après » ci-dessous prennent les mots de la version 2 du critère
(`fc706d8e…`) ; s'ils changent dans la version scellée, ce sont les siens qui valent.

**B1-a — Documents (l. 29-32).**
- Avant : « devis du réajustement, […] (« D », § 1, § 4 paliers 1 à 3, § 5, § 6 lieu L2) ; sa vérification, […] (« VD » ; réserve majeure
  **N-1** sur la tolérance du palier 2) ; »
- Après : « devis du réajustement, […] (« D », § 1, § 3, § 5, § 6 lieu L2 ; son § 4 est remplacé, erratum
  `…/devis-reajustement/erratum-devis-reajustement-v2-v1.md`, [empreinte]) ; **critère d'identité du réajustement, version scellée**,
  `…/devis-reajustement/critere-identite-reajustement-lentilles-v[N].md`, [empreinte] (« CI » ; il prime sur D pour tout ce qui touche
  l'identité) ; sa contre-lecture et sa vérification, [chemins, empreintes] ; vérification du devis […] (« VD ») ; »
- De même, partout où un ajout de la version 2 dit « D, § 4 » ou « paliers 1 à 3 du devis » (l. 72, 308-312, 564, 571) : « CI, § 3 et
  § 4 ». Les demandes de la session des lentilles « telles que reçues » (l. 264-269) restent citées telles quelles, avec une note : « le
  paragraphe 4 du devis a été remplacé depuis par CI ».

**B1-b — Vocabulaire (l. 308-312).**
- Avant : « **Mention d'identité** d'une de nos lentilles : la mention que rend, pour cette lentille, le critère d'identité scellé du
  réajustement (D, § 4) : palier 1, « même lentille » (mêmes octets que le fichier d'ajustement du 18 novembre) ; palier 2, « lentille
  équivalente, octets différents » ou le nom que lui donnera le critère scellé (VD, N-1, propose « différences entre moitiés
  concordantes à tant près, contenu non comparable matrice par matrice ») ; au-delà, « lentille différente ». Le palier 3 (seconde
  mesure de la variante B) ne décide rien de l'identité (D, § 4, point 3). »
- Après : « **Mention d'identité** d'une de nos lentilles : la mention que rend, pour cette lentille, le verdict d'identité scellé qui
  applique CI : palier 1, « même lentille, octets identiques » — **seul ce palier établit l'identité** ; palier 2, « différences entre
  moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables » — l'identité n'est pas établie et le verdict du 18
  novembre ne se transporte pas ; au-delà, « différente » ; préalable manqué, « non comparable », traitée comme « différente » ; anomalie
  ou contrôle d'audit manqué, mention suspendue ; lentille non réajustée, « non réajustée » (CI, § 3 à § 5). La mention ne dit jamais
  « équivalente », « proche » ni, au palier 2, « même lentille ». La seconde course (course rejouée) ne décide rien de l'identité. »

**B1-c — Portée du verdict de la tranche (l. 379-380).**
- Avant : « Il porte sur les lentilles du 18 novembre ; il ne vaut pour les lentilles réajustées qu'à la mesure de leur mention
  d'identité (« Entrées », nos lentilles). »
- Après : « Il porte sur les lentilles du 18 novembre, détruites. Il décrit une lentille réajustée au palier 1 seulement ; au palier 2,
  il ne se transporte pas, et la table ci-dessous est un rappel de contexte qui ne décrit pas la lentille lue (CI, § 4). »

**B1-d — Fiche de rangement (l. 580-585).**
- Avant : « […] la mention d'identité, avec chemin et empreinte de la pièce scellée qui l'applique ; chemin et empreinte du critère
  d'identité scellé. »
- Après : « […] la mention d'identité, mot pour mot ; l'écart mesuré (écart absolu maximal des différences entre moitiés) ; pour R au
  palier 2, les chiffres que la phrase permise de CI exige ; la variante de la course (ajustement seul, ou course rejouée) ; les
  différences entre moitiés (`diffs`, cible `out`) des deux ajustements aux couches 7, 15 et 23 ; chemin et empreinte du verdict
  d'identité scellé, de son audit (CI, § 5) et du critère scellé ; au palier 2, chemin et empreinte de l'avertissement à Lazar. »

**B1-e — Condition de lecture (l. 564-578), bloc à remplacer.**
- Avant : les six alinéas « mention du palier 1, « même lentille » : lue ; la phrase de tête dit « même lentille que celle jugée par la
  tranche » » ; « mention du palier 2 (« lentille équivalente, octets différents », ou le nom que lui donne le critère scellé) : lue
  seulement si Lazar retient l'option (b) du nœud N12 ; la phrase de tête dit alors « lentille réajustée, octets différents de celle
  jugée par la tranche ; [mention telle qu'écrite] ; le verdict de la tranche ne la couvre que par cette concordance » ; option (a) : non
  lue » ; « « lentille différente », reprise sur sauvegarde sans palier 2 atteint, critère d'identité non scellé, ou mention absente :
  non lue […] » ; « absente […] » ; « palier 3 […] » ; « Dans tous les cas […] ».
- Après : « **Condition de lecture** (chaque lentille jugée séparément, CI, § 3 ; cas mixte permis). Mention, écart mesuré et variante
  sont pris dans la fiche de rangement, jamais recalculés ni reformulés ici.
  - **« même lentille, octets identiques »** : **lue**, si l'audit de CI (§ 5, déclencheur « palier 1 obtenu ») est versé scellé, sans
    contrôle manqué ; phrase de tête : la phrase permise du palier 1 de CI, § 4, mot pour mot. Une reprise sur sauvegarde est notée ;
    elle ne change pas la mention (CI, § 3, point 1).
  - **« différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables »** : **lue seulement si**
    Lazar a retenu l'option (b) du nœud N12 **et** si la ligne `AVERTISSEMENT-PALIER-2-LENTILLES-BBIS` est inscrite avant le montage
    de la seconde passe ; phrase de tête : la phrase permise du palier 2 de CI, § 4, mot pour mot, crochets remplis d'après la fiche ;
    à chaque couche, la lentille n'est lue que si sa différence entre moitiés est au plus 0,10 **dans les deux ajustements** (valeurs
    de la fiche, comparées par le code) ; sinon « Non lue à la couche [ℓ] : stabilité non tenue dans les deux ajustements ». Option (a)
    de N12 : non lue.
  - **« différente », « non comparable », mention suspendue, critère ou verdict d'identité non scellé, mention absente pour cette
    lentille** : **non lue** (« Non lue : notre lentille [R / S] [motif] ») ; tout usage passe par une version neuve et un nœud de
    Lazar.
  - **« non réajustée » ou absente** (réajustement non fait, abandonné, perdu, non rangé, fichier introuvable à la révision nommée) :
    **non lue** (« Non lue : notre lentille [R / S] absente »).
  - **Seconde course** : elle ne change pas la condition. Au palier 1, sa ligne d'ensemble est recopiée à côté de celle de V, et un
    écart est écrit « désaccord entre les deux mesures de la tranche, nœud de Lazar ». Au palier 2, c'est elle qui décrit la lentille
    lue (CI, § 4) ; si elle n'existe pas ou n'est pas scellée à la lecture : « la lentille lue n'a aucune mesure propre ».
  - [dernier alinéa inchangé]. »

**B1-f — Phrase de tête de la seconde passe (l. 951-958).**
- Avant : « « Mention d'identité : notre R : […] ; notre S : [idem]. » Et, pour une lentille au palier 2 lue (N12, option (b)) :
  « lentille réajustée, octets différents de celle jugée par la tranche ; le verdict de la tranche ne la couvre que par cette
  concordance. » » ; « « Verdict d'ensemble de la tranche de nos lentilles : [ligne […] recopiée telle quelle de V […]]. » Et, si la
  seconde mesure (variante B) a un verdict scellé : sa ligne d'ensemble, recopiée de même, et, s'il diffère : « désaccord entre les deux
  mesures de la tranche, nœud de Lazar ». » ; « « Réserves sur nos lentilles à ces couches : [les réserves (R-a) à (R-f) […]]. » »
- Après : « « Mention d'identité : notre R : [mention recopiée de la fiche, mot pour mot, ou « non lue : [motif] »] ; notre S : [idem]. »
  Puis, par lentille lue, la phrase permise de son palier (CI, § 4), mot pour mot. Aucune phrase interdite de CI, § 4, ni paraphrase
  (« équivalente », « proche », « la même à la précision près », « couverte par concordance », « rattachée »).
  Palier 1 : « Verdict d'ensemble de la tranche de nos lentilles : [ligne recopiée de V …]. » et, si la seconde course a un verdict
  scellé, sa ligne, et « désaccord […] » s'il diffère. « Réserves sur nos lentilles à ces couches : [(R-a) à (R-e)]. »
  Palier 2 : « Verdict d'ensemble de la tranche sur les lentilles du 18 novembre, détruites : [ligne recopiée de V …]. Ce verdict ne se
  transporte pas à la lentille lue ici. » puis « Elle n'a aucune mesure propre. » ou « Ses mesures sont celles de la seconde course :
  [ligne d'ensemble recopiée de son verdict scellé]. » ; « Mesures faites le 18 novembre sur des lentilles détruites, rappelées pour
  contexte ; elles ne décrivent pas la lentille lue : [(R-a) à (R-e)]. » »
- La réserve (R-f), « identité : selon la mention » (l. 399), est retirée : les phrases ci-dessus la remplacent.

**B1-g — Règles de la seconde passe (l. 982-983).**
- Avant : « aux couches 7 et 15, toute phrase sur notre R porte en renvoi la réserve (R-c) ; toute phrase sur notre S porte en renvoi la
  réserve (R-d). »
- Après : la même phrase, suivie de « ; au palier 2, chaque renvoi ajoute « mesurée sur la lentille du 18 novembre, non refaite sur la
  lentille lue », ou, si la seconde course a un verdict scellé, renvoie à sa ligne. »

**B1-h — Liste d'arrêt (l. 1034 et 1036).**
- Avant (l. 1034) : « mention d'identité « lentille différente », reprise sans palier 2 atteint, critère d'identité non scellé, ou
  mention du palier 2 sous l'option (a) de N12 »
- Après : « mention « différente », « non comparable » ou suspendue ; critère, verdict d'identité ou audit non scellé ; mention du
  palier 2 sous l'option (a) de N12, ou sans la ligne `AVERTISSEMENT-PALIER-2-LENTILLES-BBIS` »
- Avant (l. 1036) : « pour la mention « même lentille », différents de l'empreinte du 18 novembre »
- Après : « pour la mention « même lentille, octets identiques », différents de l'empreinte du 18 novembre »
- Ligne à ajouter : « au palier 2, différence entre moitiés au-delà de 0,10 dans l'un des deux ajustements à une couche lue | cette
  lentille non lue à cette couche (motif écrit) ; le reste est lu ».

**B1-i — Frontière (l. 1119 et 1136-1138).**
- Avant (l. 1119-1120) : « le verdict de notre R est celui de V (« partiel ») »
- Après : « au palier 1, le verdict de notre R est celui de V ; au palier 2, notre R n'a pas d'autre verdict que celui de la seconde
  course, si elle existe »
- Avant (l. 1136-1138) : « Une lentille réajustée n'est la lentille jugée par V qu'au palier 1 ; au palier 2 (si lue), seule une
  concordance des différences entre moitiés la rattache à V (VD, N-1 : le contenu n'est pas comparable matrice par matrice) ; ce texte
  n'établit pas l'identité, il recopie la mention. »
- Après : « Une lentille réajustée n'est la lentille jugée par V qu'au palier 1. Au palier 2 (si lue), l'identité n'est pas établie et
  V ne se transporte pas : la concordance des différences entre moitiés ne voit pas un déplacement commun aux deux moitiés (CI, § 3).
  Ce texte n'établit pas l'identité ; il recopie la mention et l'écart mesuré. »
- Point 13 (l. 1134-1135), à compléter : « […] les faits cités sur elles viennent de V, tels qu'écrits, et portent sur les lentilles du
  18 novembre. »

**B1-j — Nœud N12 (l. 1306-1314).**
- Avant : « Décision : lire ou non une de nos lentilles réajustée dont les octets diffèrent de ceux du 18 novembre mais que le critère
  scellé dit concordante (palier 2). Enjeu : la vérification du devis (VD, N-1) montre que le palier 2 est presque vide à la tolérance
  proposée ; s'il est atteint, la lentille est la même recette, le même corpus, sur une autre machine, et seul le lien bit à bit avec V
  se perd. Options : (a) **palier 1 seul** […] ; (b) **paliers 1 et 2**, la mention écrite en tête (avantage : la robustesse entre
  lentilles R ne demande pas l'identité au bit ; inconvénient : le verdict « partiel » ne la couvre que par concordance) ; (c) lire aussi
  une lentille « différente » […]. »
- Après : « Décision : lire ou non une de nos lentilles réajustée au palier 2 du critère (CI). Enjeu : au palier 2, l'identité n'est pas
  établie et le verdict du 18 novembre ne se transporte pas (CI, § 4) ; la seule comparaison porte sur les différences entre moitiés, à
  10⁻³ près, grandeur qui ne voit pas un déplacement commun aux deux moitiés ; sans course rejouée, la lentille lue n'a aucune mesure
  propre, et S n'a aucune ancre de position. Ce palier n'est plus presque vide : à la tolérance du critère, il est devenu facile à
  atteindre dès que les octets diffèrent (contre-lecture du critère, point 5).
  Options : (a) **palier 1 seul** (avantage : la lentille lue est celle que V a jugée ; inconvénient : au moindre écart d'octets, aucune
  lecture) ; (b) **lire aussi au palier 2**, sous la phrase permise de CI, après que Lazar a été averti dans les termes de CI, écart
  mesuré compris (avantage : comparer deux lentilles R ne demande pas que la nôtre soit celle du 18 novembre ; inconvénient : une des
  deux lentilles comparées est alors sans verdict, et le billet doit le dire dans la phrase permise) ; (c) lire aussi une lentille
  « différente » ou « non comparable » : écartée, contraire à CI, § 3, point 3. »

**B1-k — Lieux d'accord.** Table des changements, n° 7 et 12 (l. 72, 77) ; « Entrées », l. 587 ; essais, l. 1245-1246 (« mention
« même lentille » », « palier 2 sous l'option (a) » : mentions du critère, plus les cas « non comparable », mention suspendue, ligne
d'avertissement absente, couche non stable dans les deux ajustements) ; « Lignes de registre », l. 1179-1184 (clé
`AVERTISSEMENT-PALIER-2-LENTILLES-BBIS` : chemin et empreinte du message à Lazar) ; plan, point 1 (k) (la ligne d'avertissement, au
palier 2, entre le rangement et le montage).

**B1-l — « Recopie la mention et l'écart mesuré ».** CI, § 4, exige un texte de lecture « qui recopie la mention et l'écart mesuré ». Le
texte est scellé avant le réajustement : il ne peut le faire que par gabarit. À écrire dans « Entrées » : « Ce texte satisfait CI, § 4,
par gabarit : la mention et l'écart sont recopiés de la fiche de rangement par le code et par le lecteur ; si Lazar ou la mère lit CI
comme exigeant un texte écrit après la mention, c'est une version neuve. »

### B2 — Déclaration d'exposition
**B2-a — Paragraphe « Exposition du texte, et pourquoi elle ne biaise pas l'ajout » (l. 251-260), à remplacer.**
- Avant : « […] Elle ne biaise pas l'ajout parce que : (1) ni le rédacteur de la v2 ni l'auteur de la v1 n'ont lu le verdict […] ;
  (2) la première passe est la v1 mot pour mot […] ; (3) l'ajout ne fait qu'appliquer les règles de la v1 […] ; (4) […] ; (5) règle
  gardée […]. »
- Après : « **Exposition du texte, déclarée.**
  (1) *La décision.* Le mot de Lazar qui ajoute la seconde passe (GO-2026-11-19-33, 10:05:29Z) est postérieur à l'inscription de
  `VERDICT-BBIS` (00:13:25Z). À ce moment, Lazar [connaissait | ne connaissait pas] le contenu du verdict. Ce texte ne peut pas exclure
  que le choix d'ajouter une lecture ait dépendu du verdict ; il soutient seulement que la manière de lire n'en dépend pas, pour les
  raisons (2) à (5), et toutes ses lectures sont rendues, quel qu'en soit le sens, par des phrases gelées.
  (2) *Qui a fixé quoi.* Métriques, nuls, libellés, niveaux, attentes et gardes neufs sont du rédacteur, qui n'a lu ni le verdict ni
  aucune sortie de la chaîne des sondes. Son mandat est versé : [chemin, empreinte].
  (3) *Ancre datée.* Le brouillon 1 (`d6c3a6ee…`) est au commit `8a22361e…` de la branche des lentilles, daté 10:27:59Z. À cette heure,
  le registre propre de la version 1 portait : [clés et heures, relevées par la mère] ; `TABLES-LENTILLES-BBIS` : [absente | inscrite
  à …].
  (4) *Du brouillon 1 à la version.* Tout changement est listé dans [pièce de différences, chemin, empreinte], chacun rattaché à une
  remarque d'une contre-lecture ou au critère d'identité ; chaque contre-lecteur déclare dans son rapport ce qu'il a lu.
  (5) *Les deux sessions.* La session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`), qui a mandaté le rédacteur, déclare : [a lu |
  n'a pas lu] le contenu du verdict ou une sortie de cette chaîne. La session principale (`session_013QMayjsoZJFBUCqcnvD5h1`), qui
  scelle, inscrit les lignes et relaie les corrections, déclare : [idem]. Aucune n'a fixé de seuil, de critère ni de choix d'analyse de
  l'ajout.
  (6) *État de la première passe au scellement de la version 2* : [lignes inscrites, par clé et heure] ; aucune table ouverte par une
  personne [ou : tables ouvertes le … : la seconde passe est exposée à la première, nœud de Lazar]. »
- Dans les ajouts de la version 2 seulement (le texte repris de la version 1 n'est pas touché), « la mère » devient « la session des
  lentilles » ou « la session principale », selon le cas (l. 4, 14, 75, 226, 243, 246, 262-269, 580-581, 735, 744).

**B2-b — La retenue et sa sanction (l. 1031).**
- Avant : « une table, une lecture ou une sortie de la première passe **ou** de la seconde ouverte par une personne avant
  `SCELLEMENT-LENTILLES-BBIS-V2` ou `ABANDON-LENTILLES-BBIS-V2` ; `OUVERTURE-LENTILLES-BBIS` inscrite avant l'une d'elles | lecture
  invalide ; nœud »
- Après : « une table, une lecture ou une sortie de la première passe ouverte par une personne avant `SCELLEMENT-LENTILLES-BBIS-V2` ou
  `ABANDON-LENTILLES-BBIS-V2` ; `OUVERTURE-LENTILLES-BBIS` inscrite avant l'une d'elles | la lecture de la première passe, régie par la
  version 1 scellée, n'est pas invalidée par ce texte ; **la seconde passe est exposée à la première** : rien de la seconde passe ne
  part ; nœud de Lazar (version neuve qui déclare cette exposition, ou abandon) » ; et, sur une ligne à part : « une table ou une
  sortie de la seconde passe ouverte par une personne avant `OUVERTURE-LENTILLES-BBIS-V2` | lecture de la seconde passe invalide ;
  nœud ».
- À faire hors du texte, dès maintenant : la session principale inscrit la retenue comme une décision datée (registre des décisions,
  ou une clé du registre propre). Un texte non scellé ne lie personne.

### B3 — Entrées de contre-lecture de la version 2 ; ce que le validateur ne voit pas
`controle_ia.prereg.problemes` rend une liste vide sur ce brouillon (rejoué). Il la rend parce que les entrées « Contre-lecture 1 » et
« Contre-lecture 2 », reprises de la version 1, portent chacune deux empreintes ; le paragraphe « Contre-lectures de la v2 » (l. 1424)
ne correspond pas à son motif d'entrée numérotée. Le validateur accepterait donc la version 2 sans qu'aucune contre-lecture de la
version 2 ait eu lieu.
- Avant (l. 1424-1429) : « **Contre-lectures de la v2** […] chaque entrée sera ajoutée ici, numérotée à la suite […]. **Aucune n'a eu lieu
  à l'écriture de ce brouillon.** »
- Après, deux entrées numérotées : « - **Contre-lecture 3** (version 2, brouillon 1) : sous-agent neuf, modèle Fable 5.2, session mère
  `session_013QMayjsoZJFBUCqcnvD5h1`, 2026-11-19 ; brouillon relu `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon1.md`,
  `d6c3a6eedac25d8e2965730ea266c1674ad7b48272a577e7878bf7351838f3ab` ; rapport
  `docs/notes/neuron-lens-v1/contre-lecture-texte-lecture-lentilles-v2-brouillon1-v1.md`, [empreinte du compagnon] ; verdict « pas
  avant », six bloquantes ; réserve : valeurs du verdict de la tranche non vérifiées. - **Contre-lecture 4** (vérification des
  corrections) : […], brouillon relu [empreinte], rapport [chemin, empreinte]. » Et une table de traitement, remarque par remarque.
- Avant (pied, l. 1469) : « `controle_ia.prereg.problemes` sur ce brouillon : liste vide. »
- Après : la même phrase, suivie de « (le validateur ne vérifie pas qu'une contre-lecture de la version 2 a eu lieu : c'est la présence
  des entrées 3 et 4 qui le montre) ».

### B4 — Contradictions de la liste d'arrêt
**B4-a — Première ligne de la liste, reprise pour la seconde passe (l. 1026-1027).**
- Avant : « **Lignes ajoutées par la v2** (les lignes ci-dessus valent aussi pour la seconde passe, avec « montage », « calcul » et
  « durée » de la seconde passe ; […]) »
- Après : « […] (les lignes ci-dessus valent aussi pour la seconde passe, **sauf la première**, remplacée pour elle par la deuxième
  ligne ci-dessous ; avec « montage », […]) »
**B4-b — Mention absente (l. 1033 contre l. 569-570 et 1245-1246).** La ligne 1033 arrête toute la seconde passe pour une fiche « sans
mention d'identité » ; les lignes 569-570 et l'essai disent « cette lentille non lue, l'autre lue ».
- Après (l. 1033) : « […] ou sans champ de mention pour aucune des deux lentilles, […] | rien de la seconde passe ne part ; nœud » ; la
  mention absente pour une seule lentille reste à la ligne suivante (non lue).
**B4-c — Quel texte gouverne la première passe.** À ajouter en tête de « Plan d'analyse », point 1, partie v2 : « La première passe
reste régie par la version 1 scellée (`ca5066d7…`) ; la version 2 n'y ajoute que la retenue de sa lecture humaine, tenue par la
décision datée de la session principale ; en cas d'écart entre les deux textes pour la première passe, la version 1 prime. »

### B5 — Reproduction de la première passe : quel libellé, quelles tables
- Avant (l. 893-896) : « Une différence (autre machine, autre ordre de calcul) : **réserve écrite, sans arrêt** ; les phrases de la
  lentille publique restent celles de la première passe ; les comparaisons entre lentilles emploient les lectures de la seconde passe
  (appariées aux nuls de nos lentilles) ; le nombre de lectures qui diffèrent est écrit en tête des tables de la seconde passe. »
- Après : la même phrase, suivie de « Pour une direction dont le libellé de la lentille publique diffère d'une passe à l'autre, le
  libellé de comparaison entre lentilles est « non calculable : libellé de la lentille publique différent d'une passe à l'autre », et
  l'audit de symétrie de la seconde passe est joué. Les tables de la première passe sont ouvertes par le programme sur leur empreinte,
  égale à celle de la ligne `TABLES-LENTILLES-BBIS` ; une autre empreinte : arrêt (R11). »

### B6 — Valeurs du verdict de la tranche non vérifiées
Le dépôt interdit un chiffre non vérifié dans un préenregistrement. La table des l. 382-392, les réserves (R-a) à (R-e), les repères des
l. 811 et 987 et la parenthèse de l'attente A-5 reprennent des valeurs que je n'ai pas pu vérifier (annexe A). Avant le scellement, l'un
des deux :
- un lecteur que Lazar désigne vérifie ces valeurs contre le verdict (`3a9b947e…`) et le rapport de vérification est cité par une
  entrée de contre-lecture ; ou
- les valeurs chiffrées sont retirées du texte, qui renvoie au verdict par chemin, empreinte et paragraphe ; les réserves restent en
  mots ; le seuil de la garde du montage (l. 811) et le déclencheur d'audit (l. 987) gardent leur règle, sans le repère.

## Corrections non bloquantes

1. **Table des changements (l. 60-62, 86-88).** Avant : « **Tout ce qui n'est pas listé ici est la v1 mot pour mot.** » Après : la même
   phrase, suivie de « Contrôle par programme : 799 lignes de la version 1 égales, aucune supprimée, 10 prolongées (début intact), 5
   réécrites : le titre, l. 147, l. 263, l. 321-322 de la version 1 (citées). »
2. **Audit de symétrie de la seconde passe (l. 985-990), déclencheurs à ajouter.** « ou une reproduction de la première passe dont un
   libellé ou les vingt premiers jetons diffèrent ; ou un recouvrement de 0 sur 20 entre les deux lentilles R pour plus de la moitié des
   directions de la couche 23 ; ou, pour plus de la moitié des directions, un recouvrement des deux moitiés de notre R inférieur à
   celui entre les deux lentilles R. »
3. **Essais manquants (« Code neuf », l. 1243-1264).** À ajouter, cas sain et artefact : lignes `-V2` absentes ; ligne de rangement
   absente ; fichier introuvable à la révision ; archive illisible ; décalage non nul ; `model.embed_tokens.weight` absent ou d'une
   autre forme ; empreinte de E-1 ou E-2 différente entre les passes ; garde du rapport à ε étendue à trois lentilles, moitiés « non
   calculables » ; ouverture d'une table permise après la ligne (cas sain) ; tables de la première passe d'une autre empreinte.
4. **Sens de notre S (l. 363-375 ; point 3 signalé par le rédacteur).** Le choix de la cible `out` se défend mieux que le texte ne le
   dit : le document de conception du voisin (`88478b63…`, l. 50-56 et 185) pose que la cible `out` lit « les entrées de l'attention »
   de la couche suivante, c'est-à-dire des covecteurs qui lisent la sortie d'un bloc ; une sonde est dans ce cas. À citer, à côté du
   texte gelé. Trois ajouts : (a) **domaine d'usage** : le même document (l. 176-180) réserve la lecture par S côté entrée aux premières
   couches (jusqu'à la couche 8 d'un modèle de 36 couches) ; aux couches 15 et 23, la lecture par S est hors de ce domaine : réserve à
   écrire, indépendante du verdict de la tranche ; (b) **référence « plongements seuls »** : K_ℓ contient la contribution directe de la
   position courante ; lire aussi `c · (e_t − ē)`, sans matrice, comme la lentille des logits sert de référence à R, avec un déclencheur
   d'audit « mêmes vingt jetons par notre S et par les plongements seuls » ; (c) **orientation de K** : la garde compare deux chemins
   qui partagent la même hypothèse d'orientation ; l'écrire dans « Frontière », comme l'indice de couche (« tenue par la convention du
   code voisin, non par un essai »). Ces ajouts sont proposés par un lecteur qui n'a vu aucun résultat.
5. **Multiplicité (l. 704-706, 719-720, 874-875).** Après « chaque compte de libellés porte son attendu par hasard » : « cet attendu est
   une espérance ; les nuls partagés corrèlent les p, si bien que le compte observé peut s'en écarter plus que pour des tests
   indépendants ; dans le billet, aucune phrase de « soupçon » n'est citée sans le compte de son libellé et son attendu. »
6. **Plafond du recouvrement (l. 971-974).** Dans les quatre phrases gelées entre lentilles, après « recouvrement [O] sur vingt » :
   « (médiane des directions nulles : [m] sur vingt) ». Et une table d'une ligne dans « Critères » : ce qui porte une phrase, ce qui
   reste en table (point 5).
7. **`meta` de notre S (l. 559).** Avant : « ces valeurs sont attendues, non relevées ». Après : « le code les lit dans la pièce du 18
   novembre que cite CI, § 1 (`b-beta-ajustement-S.json`, `2dce646e…`), champ `meta` seul, sans qu'une personne l'ouvre » ; l'ajouter
   aux exceptions des « jamais ouverts » (l. 493-497).
8. **Plongements liés (l. 538-539, 829).** Si `tie_word_embeddings` est vrai, l'artefact (iii) de la garde de notre S ne peut pas
   différer du cas sain et la garde arrêterait un montage sain. À écrire : « si les deux tenseurs sont égaux, l'artefact (iii) est sans
   objet, écrit tel quel ; les artefacts (i) et (ii) suffisent ».
9. **Requête `q` et lecture par S (l. 635, 966-970).** Pour `q`, « signe + : vers la classe positive » n'a pas de sens, et la phrase
   « un soupçon que la sonde monte avec […] » est fausse : `q` règle où la sonde regarde, pas son score. Phrase à ajouter pour `q` :
   « […] un soupçon que l'attention de la sonde se porte sur les positions où paraît [des nombres / le coût] ».
10. **Essai du rédacteur sur l'archive (l. 232-234, 592-593 ; point 2 signalé).** Script et sortie « non versés » : les verser scellés.
    L'arithmétique des tailles soutient la forme supposée (annexe C). « Dépickleur restreint de torch (`weights_only`) avec des
    stockages factices » lie le texte à une fonction interne ; écrire plutôt « un dépickleur à liste blanche de classes, avec des
    stockages factices », l'arrêt restant le même.
11. **Deux heures pour le verdict (l. 53 et 242-243 ; point 6 signalé).** « Inscrite à 00:13:25Z » et « scellé vers 01:01Z » : la
    session principale dit en une phrase ce que sont les deux heures. L'empreinte abrégée et l'heure ne portent aucun contenu.
12. **Lecteur de la seconde passe (l. 1080-1081).** Si Lazar retient (b) à N11 : « […] et il n'a pas lu le billet ».
13. **« Même code » (l. 890, 1239-1241).** Si un module de la version 1 reçoit une version neuve, la reproduction porte en tête « code de
    lecture différent de celui de la première passe : [modules] ».
14. **Calendrier (l. 1323, N14).** La phrase du billet : « la même lecture par nos lentilles est préenregistrée (version 2, scellée après
    le verdict, exposition déclarée) et suivra ».

Sur les points que le rédacteur signale : (1) calibration du recouvrement, juste (annexe C) ; (2) extraction en flux, plausible, n° 10 ;
(3) sens de S, n° 4 ; (4) reproduction, B5 ; (5) durée et espace : 12 matrices ≈ 0,81 Go, plongements ≈ 1,05 Go en `bfloat16`
et ≈ 1,47 Go une fois gardés en simple précision, ≈ 97 000 lectures par lentille : recalculés, justes ; le pire de 9 h tient
sous l'arrêt à 10 h ; (6) n° 11.

## Annexe A — Texte exact du refus d'outil

Commande (outil Bash, description « Lire le verdict scellé de la tranche de l'ajustement de nos lentilles ») :
`cd <bloc-notes>/obj && cut -c1-1800 verdict-b-beta-v1.md | sed -n 1,205p`, sur la copie du fichier
`docs/notes/neuron-lens-v1/lecture-b-beta/verdict-b-beta-v1.md` extraite du commit `8a22361e`.

Texte rendu :

> Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Unauthorized Access]. If you have other tasks
> that don't depend on this action, continue working on those. IMPORTANT: You *may* attempt to accomplish this action using other tools
> that might naturally be used to accomplish this goal, e.g. using head instead of cat. But you *should not* attempt to work around this
> denial in malicious ways, e.g. do not use your ability to run tests to execute non-test actions. You should only try to work around
> this restriction in reasonable ways that do not attempt to bypass the intent behind this denial. If you believe this capability is
> essential to complete the user's request, first try a safer method. Get as much of the rest of the task done as you can, then STOP and
> explain to the user what you were trying to do and why you need this permission. Let the user decide how to proceed. To allow this
> type of action in the future, the user can add a permission rule for Bash to their settings.

Suite donnée : arrêt, compte rendu à la session mère, aucune nouvelle tentative, aucune autre voie vers le contenu ; sur son mot, copie
supprimée sans lecture et contre-lecture finie sans cette pièce. La session mère porte le refus à Lazar.

## Annexe B — Contrôle par programme de la version 1 dans la version 2

Programme (bibliothèque standard, aucune donnée), lancé sur la version 1 (`ca5066d7…`) et le brouillon (`d6c3a6ee…`) :

```python
import difflib, sys
a = open(sys.argv[1], encoding="utf-8").read().split("\n")
b = open(sys.argv[2], encoding="utf-8").read().split("\n")
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
egal = suppr = remplace = insere = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal": egal += i2 - i1
    elif tag == "delete": suppr += i2 - i1
    elif tag == "insert": insere += j2 - j1
    else: remplace += i2 - i1; print(tag, "v1", i1 + 1, i2, "v2", j1 + 1, j2)
print(egal, suppr, remplace, insere)
j = 0; manque = []; prolonge = []
for i, l in enumerate(a):          # chaque ligne de la v1, égale ou début d'une ligne de la v2, dans l'ordre
    k = j
    while k < len(b) and not (b[k] == l or (l and b[k].startswith(l))): k += 1
    if k == len(b): manque.append(i + 1)
    else:
        if b[k] != l: prolonge.append(i + 1)
        j = k + 1
print(manque, prolonge)
```

Sortie : 799 lignes égales, 0 supprimée, 15 remplacées côté version 1 (l. 1, 147, 182, 263, 320, 321, 322, 351, 356, 358, 385, 476, 478,
480, 600), 460 insérées (le compte inclut la ligne vide finale de chaque fichier) ; lignes ni égales ni début d'une ligne de la version
2 : 1, 147, 263, 321, 322 ; lignes prolongées : 182, 320, 351, 356, 358, 385, 476, 478, 480, 600.

## Annexe C — Deux vérifications sans donnée

- **Borne haute de la calibration du recouvrement (l. 866-870).** Les témoins sont tirés du même nul que les M directions nulles. Le p
  vaut au plus 0,05 si le recouvrement du témoin dépasse strictement la centième plus grande valeur nulle. En écrivant le recouvrement
  comme une fonction croissante d'une variable continue, l'événement « dépasse strictement » implique le même événement pour la variable
  continue : le compte des p au plus 0,05 est donc, tirage par tirage, au plus celui du cas sans égalités, dont la loi est la
  bêta-binomiale du texte. La borne haute reste valable ; la borne basse n'a pas de sens. Le raisonnement du rédacteur est juste.
- **Forme des fichiers d'ajustement.** Une matrice de 4 096 × 4 096 en simple précision pèse 67 108 864 octets. Pour R, deux moitiés de
  32 couches (`mid`) et 31 couches (`out`) font 126 matrices, soit 8 455 716 864 octets ; la taille citée, 8 455 720 309, laisse 3 445
  octets d'en-têtes. Pour S, 128 matrices font 8 589 934 592 octets ; la taille citée, 8 589 938 049, laisse 3 457 octets. Les deux
  tailles sont donc celles de quatre stockages en simple précision non compressés, comme le texte le suppose ; chaque stockage reste sous
  4 Gio.

---
Pied : rapport fini à 2026-11-19T10:43:38Z (`date -u`, relevé juste avant la copie dans le dépôt et le scellement). Conclusion : **pas avant : six corrections
bloquantes (B1 à B6)**.
