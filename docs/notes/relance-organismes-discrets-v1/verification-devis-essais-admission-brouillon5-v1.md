# Vérification du devis des deux essais d'admission (Mistral Large 4, second lecteur ; `gemini-4-neon`, juge des deux ancres), brouillon 5 — bras A — v1

- **Pièce vérifiée** : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1-brouillon5.md`, `421ee2e6ec909c8b…` (« OK » contre son compagnon), 901 lignes, écrit par Claude Fable 5.2.
- **Point de départ** : le brouillon 4, `31189b57dcacd6b3…` (« OK »), et sa contre-lecture, `contre-lecture-devis-essais-admission-brouillon4-v1.md`, `7b1b3d54e11cfa97…` (« OK ») : deux corrections, sept mineurs.
- **Vérificateur** : Claude Opus 5.5, agent neuf, le 2026-11-21 vers 14:30 UTC. Je n'ai écrit ni ce devis, ni ses brouillons, ni leurs contre-lectures, ni le texte du bras A. Le rédacteur est d'un autre modèle.
- **Ce que j'ai fait** : comparaison au brouillon 4 par `diff`, sections touchées listées par programme ; lecture des sections 0 à 15 du brouillon 5 et de sa section 19 ; huit règles, signe, clés du constat et tableaux inchangés comparés par programme (`verif_b5.py`) ; tous les chiffres refaits par programme (`calc_b5.py`), en décimal exact, arrondi au centime supérieur comme le devis. Les deux programmes sont dans le bloc-notes de la session, hors du dépôt. Je juge ; je ne corrige rien. Aucun appel de modèle, aucun appel réseau, aucune clé, aucun sous-agent, aucune dépense. Rien scellé, rien committé.
- **Texte en vigueur** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad915815…` (« OK »).

## Verdict

**Engageable.** Le brouillon 5 peut être scellé comme version acceptée **sans brouillon de plus**.

- Les deux corrections et les sept mineurs du brouillon 4 sont levés, fidèlement. Les ajouts au-delà de la contre-lecture sont déclarés et justes.
- La recharge de Google en une fois, à 23 USD, est portée fidèlement à la pièce `487b5a72…`. Les trois seuils de gardes changés sont justes et suffisent ; 19,76 USD est le plus petit seuil qui tienne, même au pire, la promesse de la pièce.
- Tous les chiffres sont justes, les deux neufs compris (72,94 ; 31,27). Les huit règles, le signe, les critères, les plafonds, les excès, les tarifs et les délais sont inchangés, vérifiés par programme.
- Quatre mineurs restent. Aucun ne touche un chiffre de garde, un plafond, un crédit ou un critère. Ils se disent à Lazar avec la demande des lignes, sans retoucher le texte scellé (partie 5).

## 1. Corrections et mineurs du brouillon 4

### Les deux corrections

| correction | levée ? | constat |
|---|---|---|
| **C-1.** « Un seul excès » au régime courant | **levée** | Écrit en tête, en 0 (point 12), en 4.6 (limites), en 6.3, en 6.4 (« Au régime courant »), en 6.5, en 13 (point 28). Section 11 : crochet de la ligne 4 et de la ligne 3 ; alinéa « Ce que Lazar accepte » réécrit : « un seul envoi » est tenu par le compteur au régime prudent ; au régime courant, il suppose de plus que la borne se comporte à 32 768 comme à 256 ; sinon jusqu'à neuf envois de la file Neon. En 11.1, ligne 4. Le « une fois » sans condition est retiré de 6.5 (« Ce que le crédit ne permet pas »). Le prix de la recharge en deux temps est dit (de 10,82 à 14,48 USD au départ de la file Neon : un excès de 7,58 n'est pas couvert) ; la recharge en deux temps est ensuite écartée par Lazar. Recherche par programme dans les sections 0 à 15 : aucun « une fois » ni « un seul excès » sans condition ne reste, hors de l'histoire du brouillon 3 (6.4, « ce qui le rend vrai »), lue avec l'alinéa suivant. |
| **C-2.** « La dépense ne peut pas passer le solde prépayé » | **levée** | La phrase devient : la dépense est bornée par le solde prépayé, plus tout autre crédit Google Cloud admissible du compte de facturation ; ce que fait le service au solde nul n'est pas relevé. Quatre réserves en 6.4. Clé neuve au constat, `google_autres_credits_admissibles`, seule valeur admise `aucun`, avec deux artefacts à la garde 9 (`300`, `oui`). Écrit aux lignes 2 et 4 (section 11 et 11.1), en 6.4, en 6.5, en 13 (point 29), et aussi en 0 (points 4 et 12), en 4.6 et en 13 (points 20 et 23), extension déclarée. Recherche par programme : « ne peut pas passer » ne reste qu'en 6.4, cité comme ce qu'écrivait le brouillon 4 ; « quoi qu'il arrive » : absent ; « est une borne dure » : seulement pour Mistral. |

### Les sept mineurs

| mineur | levé ? | constat |
|---|---|---|
| m-1 | levé | « Envoi coupé » défini en 6.4 : délai, borne en octets, connexion coupée en route ; refus du mandataire à sa signature exclu ; un code d'erreur n'en est pas un ; dans une file, la reprise reste due. Repris en 4.1 (relevé et lecture de la console), 4.4 ligne 6, supposition 3 de 6.4, 7, garde 20 (cas sain « refus du mandataire : aucune pièce » ; artefact « connexion coupée en route à un appel de vérification, refait sain, sans pièce : la file ne part pas »), 11, 11.1, 12 point 13, 13 point 30. |
| m-2 | levé | 6.5 : 5 USD « au premier prépaiement » ; pour un complément, non relevé (S). Redit au geste de paiement de la section 11 et en 13 (point 10). Le geste de 11.1 ne le redit pas ; le complément de 7,00 passe 5 USD de toute façon. |
| m-3 | levé, et étendu | Garde 10 : crédit du dernier constat, moins la dépense comptée des lignes de Google jouées depuis, au moins 16,08 USD, avant toute file Neon, sonde « comprise » ou non. Artefact : constat à 20,00, dépense comptée 4,10, solde vu 19,90 : le contrôle donne 15,90, la file ne part pas (recalculé). Extension déclarée (14). |
| m-4 | levé | 6.5, 11 et 11.1 (ligne 2) : une seconde ligne de vérification exige de nouveau 19,76 USD vus ; après une première ligne au pire, il reste 19,32 : recharge d'au moins 0,44 USD (recalculé : 19,76 − 19,32). Constat neuf après toute recharge. |
| m-5 | levé | Section 9, ligne `google_offre_payante` : la lettre du mot « b a b go », « offre payante (projet avec un compte de facturation actif) », puis la forme constatée, « un crédit prépayé est visible à la console ». Lettre égale à la ligne 11 de la pièce `00af2aa8…`, que j'ai lue. |
| m-6 | levé | 0, point 12 ; crochet de la ligne 3 en section 11 ; 11.1, ligne 3 : « ou après un majorant démenti en file ». |
| m-7 | levé | 13, point 28 : « le solde restant au départ de la file », de 19,32 à 22,98 USD après la recharge à 23,00 (de 12,32 à 15,98 sur les seuls 16,00). |

### Ni plus ni moins ?

**Rien ne manque. Les ajouts sont tous déclarés (14, « Ce que la consigne fixait et que j'ai étendu »), et je les garde.**
- C-2 et m-3 étendus au-delà des endroits nommés : cohérent, plus prudent.
- Le cas ouvert du régime courant est dit aussi pour la file Mistral, au crochet de la ligne 3 et en 11.1, avec un chiffre neuf en 6.4. Cela suit la logique de C-1 (dire aux lignes ce que suppose « un seul »). Observation : chez Mistral, plusieurs excès demandent que **deux** suppositions manquent ensemble — la borne à 32 768 et le majorant sur les envois coupés — car au régime courant un envoi coupé est compté au moins à 32 768 jetons. La ligne 3 n'en nomme qu'une. C'est une surestimation du risque, du côté prudent ; sans effet.
- Le nombre de clés du constat : treize, compté par programme (douze au brouillon 4). Le rédacteur a raison (13, point 38) : la contre-lecture du brouillon 4 écrivait « treize » pour un tableau de douze.

## 2. La recharge en une fois, à 23 USD

### Est-elle portée fidèlement à la pièce `487b5a72…` ?

**Oui.**
- La pièce : solde d'environ 16 USD, celui du compte Google de la clé par défaut ; compte en prépaiement ; « go » lu comme l'accord de l'option (a), « porter le solde prépayé de Google à 23 USD (complément d'environ 7 USD), pour que, même au pire, il reste de quoi couvrir le plafond de la file Neon et un excès » ; « le montant exact est celui du devis accepté ».
- Le devis : 23,00 USD en une fois ; complément de 7,00 pour un solde de 16,00, « au juste, 23,00 moins le solde vu » ; « environ 16 » dit parole, non relevé (13, point 34). Écrit en tête, en 0 (point 4), en 6.5, aux lignes 2 et 4, au geste de paiement de la section 11 et de 11.1.
- Ce que la pièce dit dû avant toute vérification — constat de la console de Google (solde vu, prépaiement, recharge automatique désactivée, partage des journaux désactivé, journaux à 7 jours, aucun autre crédit admissible) ; compte Mistral à 9,50 USD — est entier dans la section 9 et en 6.5.
- **Réserve de lettre, déjà déclarée** (13, point 34) : le verbatim de la pièce répète la question « Ce compte est-il en prépaiement ? » avant le « go ». Que ce « go » vise l'option (a) est la lecture de la session. Lazar la confirmera en accordant la ligne 2, qui écrit « porté à 23,00 USD avant la ligne ».

### Les seuils des gardes (réserve 1 du rédacteur) : justes et nécessaires ?

**Justes. 19,76 est exactement le seuil qui tient la promesse de la pièce ; 16,08 en est la garde directe.**
- **Garde 9, 19,76 USD vus avant la vérification de Google.** C'est le « à couvrir » de la recharge en une fois : plafond et excès de la vérification (1,50 + 2,18), plafond et excès de la file (8,50 + 7,58). Recalculé : 19,76 − 3,68 = **16,08 exactement**. C'est donc le plus petit crédit de départ qui laisse, même si la vérification prend plafond et excès, le plafond de la file Neon et un excès : la lettre de la pièce (« même au pire »). Un seuil plus bas laisserait une seconde recharge possible avant la file ; un seuil plus haut (23,00) exigerait la marge de 15 %, qui couvre un écart de prix et non un excès. Le motif du brouillon 4 est gardé : seuil au « à couvrir », versement avec la marge (12,18 et 14,50 alors ; 19,76 et 23,00 ici).
- **Garde 10, 16,08 USD avant la file Neon, quelle que soit l'issue de la sonde.** Au brouillon 4, une sonde « comprise » n'exigeait que 8,50. Le cas que C-1 laissait ouvert est précisément celui où la caisse coupe une file qui tiendrait ; la pièce demande « un excès » même au pire. Exiger 16,08 dans tous les cas est la traduction directe du mot de Lazar. Avec 23,00 chargés et la garde 9 à 19,76, la garde 10 passe toujours après une seule ligne de vérification ; elle ne coûte rien et ferme les cas d'une seconde ligne de vérification et d'un solde vu en retard (m-3).
- **Garde 20** : le solde vu porté par la pièce de la lecture de la console doit atteindre « ce que 6.5 exige pour la ligne » : 16,08 avant la file Neon, 19,76 avant une seconde vérification. Cohérent.
- Observation sans effet : la garde 9 lit le crédit du constat, sans en ôter la dépense comptée. Pour une seconde ligne de vérification demandée sans envoi coupé (par exemple, trois appels pris par des codes 429), elle lit donc un crédit ancien. Sans conséquence : une telle ligne a pris au plus son plafond, 1,50 ; et la garde 10 contrôle par la dépense comptée avant la file.

### Avec 16 USD seulement, la vérification de Google ne part pas : est-ce voulu ?

**Oui, et c'est la seule lecture qui tienne « en une fois » et « même au pire » ensemble.** Sur 16,00, la vérification pourrait partir (16,00 ≥ 12,18), mais il resterait de 12,32 à 15,98 au départ de la file Neon : jamais 16,08, même au mieux (recalculé ; il manque 3,76 au pire, 0,10 au mieux). La file attendrait alors une seconde recharge et un constat neuf : la recharge en deux temps que Lazar a écartée. Charger avant la vérification n'expose rien de plus qu'un crédit prépayé qui reste au compte. L'artefact est écrit (garde 9 : `google_credit_utilisable_usd` à 16,00, « ni vérification ni file »), comme R5 le veut. Le rédacteur le dit sa lecture (13, point 35) : je la confirme.

## 3. Les deux chiffres neufs (réserve 3)

Refaits par programme, sur les prix comptés (3 et 15 USD par million chez Google ; 0,77 et 2,31 chez Mistral), entrées bornées à 5 000 et 24 000 octets, 200 jetons par seconde, délai du relais de 2 690 secondes.

| grandeur | devis | recalculé |
|---|---|---|
| envoi coupé de la file Neon, régime prudent | 8,085 ; 8,142 | 8,085 ; 8,142 |
| neuf envois Neon d'appariement (contre-lecture) | 72,77 ; 4,56 comptés | 72,765 → 72,77 ; 4,55868 → 4,56 |
| **neuf envois Neon dont trois de couverture** | **72,94** | 6 × 8,085 + 3 × 8,142 = 72,936 → **72,94** |
| envoi coupé de la file Mistral au délai total | 1,25 ou 1,27 | 1,24663 ; 1,26126 |
| **25 envois coupés de la file Mistral** | **environ 31,27** | 18 × 1,24663 + 7 × 1,26126 = 31,26816 → **31,27** |

**72,94 est le bon majorant ; 72,77 ne l'est pas tout à fait.** La file Neon a six entrées d'appariement et deux de couverture. Neuf envois coupés, c'est un par appel et un second sur un même appel (deux pannes sur un appel arrêtent la file) : au plus trois de couverture. Au compteur, les seize envois tiennent sous le plafond (8,33 USD à la réserve ; recalculé), donc le cas est atteignable.

**31,27 est juste, comme majorant.** 24 appels, 18 d'appariement et 6 de couverture ; 25 envois coupés, dont au plus 7 de couverture. Le cas est atteignable au compteur : au régime courant, un envoi coupé à peu d'octets est compté environ 0,08 USD, et les 48 envois tiennent sous le plafond (3,99 USD). Il suppose un flux vivant jusqu'au délai total (un jeton qui rend moins d'un octet) ; si le flux se tait, la coupure au silence de 590 secondes ramène le cas à environ 7,01 USD.

**Les garder.** Les deux sont justes et disent un cas déclaré.
- 31,27 reste en 6.4 seulement. Les lignes n'en portent pas de chiffre, ce qui convient.
- 72,77 reste aux lignes, 72,94 en 6.4 et en 13 (point 40). L'écart est de 0,17 USD sur un cas chiffré à un débit supposé, sans mesure. Il ne touche aucune garde, aucun crédit, aucune décision : dans les deux cas, seul le solde borne la perte. Je n'en fais pas une correction. **À dire à Lazar avec la ligne 4** : « 72,77 vaut pour neuf envois d'appariement ; au plus haut, 72,94 (13, point 40) » (mineur v-1).

## 4. Ce qui ne change pas, vérifié par programme

- **Huit règles de 3.4** : lignes 457 à 465 du brouillon 5 (titre et huit règles) contre lignes 521 à 529 du brouillon 43 : **neuf lignes égales caractère pour caractère, espaces de tête compris** (longueurs 85, 337, 879, 223, 240, 248, 207, 452, 685), règle 6 comprise. Égales aussi aux lignes 446 à 454 du brouillon 4. Le renvoi « lignes 521 à 529 » de la section 7 est exact.
- **Signe de la section 11** (lignes 573 à 576) contre celui de 4.5 (lignes 151 à 154) : **quatre lignes égales**, espaces de tête ôtés (longueurs 182, 174, 47, 663). Égal aussi au signe de 4.5 du brouillon 4. « 4.5 fait foi » est écrit.
- **Sections non touchées par le `diff`** (programme) : 1, 3, 4.2, 4.3, 4.5, 5.1 à 5.6, 6.1, 6.2, le tableau de 6.3, 8, et les gardes 1 à 8 et 11 à 19. Dans les sections touchées, sept tableaux comparés ligne à ligne sont **égaux** au brouillon 4 : lignes de calcul de la section 11 (plafonds, excès), excès de 6.4 (aux trois débits), réserves du compteur de 6.4, coûts de 6.3, délais de 5.6, tarifs de 6.1, réglages de 5.1. Le seul ajout à la section 7 est « ou par une connexion coupée en route » (m-1), dans ce qui est rapporté, hors des règles.
- **Critères** : 22 sur 24 pour Mistral ; huit sur huit pour Neon ; un seul nom servi. Inchangés.
- **Plafonds** 0,25 ; 1,50 ; 4,75 ; 8,50 ; 0,25 : somme 15,25 (15,00 sans le repli). **Excès** 1,17 ; 2,18 ; 0,64 ; 7,58 ; 1,17 : somme 12,74 (11,57). **Plafonds et excès** 27,99 (26,57). Recalculés.
- **Tarifs** : 0,77 et 2,31 ; 3 et 15. **Délais** : 600 et 2 700 secondes chez Mistral ; 2 700 et 900 chez Google ; délais globaux 144 840, 48 680, 8 700 et 3 300 secondes ; débit minimal 32 768 ÷ 2 690 = 12,18 jetons par seconde. Recalculés.
- **Décisions « goreco »** (pièce `9b9ee5ca…`, lue) et **conditions du mot « b a b go »** (pièce `00af2aa8…`, lue) : inchangées.

### Le tableau des soldes de 6.5, refait

| solde de départ | reste au pire (− 3,68) | reste au mieux (− 0,02) | couvre 8,50 au pire | couvre 16,08 | à charger pour 23,00 |
|---|---|---|---|---|---|
| 16,00 | 12,32 | 15,98 | oui | non : il manque 3,76 au pire, 0,10 au mieux | 7,00 ; 8,40 avec une taxe de 20 % |
| 23,00 | 19,32 | 22,98 | oui | oui, 3,24 de plus au pire ; deux excès (23,66) : non | rien |

Ligne « S quelconque » : 8,50 au pire dès 12,18 ; 16,08 au pire dès 19,76, au mieux dès 16,10. Crédits : Google 19,76 × 1,15 = 22,724, soit 23,00, et 27,60 avec la taxe ; Mistral 8,23 × 1,15 = 9,4645, soit 9,50, et 11,40. Taxe prise sur la recharge : 23,00 ÷ 1,2 = 19,17, sous 19,76 ; 9,50 ÷ 1,2 = 7,92, sous 8,23. Seconde vérification : 0,44 dû, 3,68 pour revenir à 23,00. **Tout est juste.** Une remarque de forme : la colonne « au mieux » prend l'attendu de la vérification (0,02), non un minimum ; c'est ce que faisait déjà la contre-lecture.

## 5. Les cinq lignes de GO de 11.1

**Exactes en leurs chiffres, et fidèles aux mots de Lazar. Le texte des cinq phrases peut être cité tel quel. La demande ne peut pas partir avant que les empreintes qu'elle cite existent, et elle porte avec elle les quatre mineurs ci-dessous.**

- **Fidélité** :
  - « goreco » : « trois appels au plus » en toutes lettres aux lignes 1, 2 et 5 ; sortie maximale de 32 768, tenue dans les délais si le service rend 12,2 jetons par seconde ou plus, débit non mesuré, ajouté aux lignes 3 et 4 ; ligne 5 accordée d'avance, sous le signe de 4.5 et la garde 15, avec l'élargissement du signe dit et la voie de retrait.
  - « b a b go » : les conditions ne sont pas redites aux lignes, mais chaque ligne cite le constat ; le constat les porte toutes (section 9).
  - Pièce `487b5a72…` : ligne 2, « porté à 23,00 USD avant la ligne » ; ligne 4, « après la recharge à 23,00 » ; geste de paiement, complément de 7,00 pour un solde de 16,00.
- **Exactitude** : chaque chiffre des cinq lignes est égal au tableau de la section 11 et à mes recalculs : 0,25 ; 1,17 ; 32 768 octets ; 1,50 ; 2,18 ; 900 secondes ; 19,76 ; 4,75 ; 0,64 ; 262 144 octets ; 8,50 ; 7,58 ; 72,77 ; 19,32 ; prix comptés. C-1 et C-2 y sont faits.
- **Les quatre mineurs, à porter avec la demande, sans retoucher le texte scellé** :
  - **v-1** : ligne 4 : 72,77 vaut pour neuf envois d'appariement ; au plus haut, 72,94 (6.4 ; 13, point 40). Partie 3.
  - **v-2** : ligne 4 : « dont il reste au moins 19,32 USD au départ de la file » vaut après **une seule** ligne de vérification. Après une seconde ligne et la recharge minimale de 0,44 USD, il reste au moins 16,08, ce que la garde 10 tient dans tous les cas. Le plafond et un excès restent couverts ; seul le coussin de 3,24 USD n'est pas garanti.
  - **v-3** : 11.1 (« Chaque ligne ajoute ») reprend moins que la section 11 n'exige de chaque ligne. Il y manque la variable de la clé (`MISTRAL_API_KEY`, `GEMINI_API_KEY`), le compte qui paie, et le brouillon du texte en vigueur. Aux lignes 3 et 4, il manque aussi l'attente de 600 secondes au plus sur un code 429, les délais de 5.6, et le départ seulement après une vérification saine (sonde « comprise » ou mot de Lazar). La section 11 fait foi : la demande joint ces éléments. C'est appliquer le devis, non le changer.
  - **v-4** : les empreintes que chaque ligne cite (devis accepté, constat, deux pages de prix, et fichier des règles aux lignes 3 et 4) ne sont pas encore faites : la demande attend qu'elles existent. Pour le fichier des règles, la section 9 dit qu'il est refait sous un nom neuf si le brouillon du texte change entre son scellement et le premier envoi. Or un brouillon du texte doit inscrire les relevés des vérifications avant la file (12, point 13). Une empreinte du fichier citée à la ligne 3 ou 4 avant les vérifications risque donc d'être périmée au départ de la file. Deux voies, au choix de la session : demander les lignes 3 et 4 après les vérifications et le brouillon qui inscrit leurs relevés ; ou faire écrire à ces deux lignes que l'empreinte du fichier des règles est inscrite à l'engagement, comme le devis le fait déjà pour le point d'accès. Aucune garde n'en dépend : la garde 12 compare le fichier à la configuration, non à la ligne de GO.

## 6. Verdict, et ce qui sépare encore de la première vérification de clé

**Engageable.** Aucune correction. Le brouillon 5 peut être scellé comme version acceptée sans brouillon de plus, sous un nom neuf (R12) et avec son compagnon (R6). Les mineurs v-1 à v-4 se portent à la demande des lignes.

**Ce qui sépare encore de la première vérification de clé** (celle de Mistral comme celle de Google) :
1. Le scellement de la version acceptée, son empreinte inscrite.
2. Les deux pages de prix, versées et scellées (6.1).
3. Les réglages des deux consoles par Lazar. Chez Google : recharge jusqu'à 23,00 USD (complément d'environ 7,00), recharge automatique désactivée, aucun autre crédit admissible. Chez Mistral : 9,50 USD chargés. Puis le constat daté, versé et scellé, aux treize clés (section 9).
4. Un brouillon du texte qui inscrit le constat à la case « lecteurs et juge des ancres » de 13.1 (section 9).
5. Le programme qui conduit les essais, en version neuve : configuration, deux relais (Mistral en flux, fermeture vers l'amont, origine `mandataire` ; Google sans flux, 890 et 2 690 secondes), programmes d'extraction, de forme, du rapport et des règles, faux fournisseur local, et les vingt gardes éprouvées sur un cas sain et un artefact (R5), les artefacts neufs des gardes 9, 10 et 20 compris.
6. La contre-lecture de ce code par un agent neuf d'un autre modèle, puis la vérification de ses corrections.
7. Les lignes de GO accordées par Lazar (au moins les lignes 1, 2 et 5 pour les vérifications), inscrites à `registres/go.md` ; la ligne d'engagement au registre des dépenses.
8. Les trois hôtes permis par le réseau de la session, et les deux clés présentes par leur nom (13, point 15).
9. L'inscription au registre de la branche principale des pièces `487b5a72…`, `9b9ee5ca…` et `00af2aa8…`, par chemin et empreinte, comme chacune le demande.

Le fichier des règles n'est dû qu'avant le premier envoi d'une file (mineur v-4 pour l'ordre).

## Fichiers ouverts

Empreintes vérifiées par `python -m controle_ia.scellement verifier`, toutes « OK » :
- le brouillon 5, `421ee2e6ec90…` : sections 0 à 15 lues ; section 19 lue par le `diff` ; sections 16 à 18 non relues (reprises sans retouche, sauf une phrase ajoutée à la 18, lue par le `diff`) ;
- le brouillon 4, `31189b57dcac…` : comparé par `diff` et par programme ; non relu en entier ;
- `contre-lecture-devis-essais-admission-brouillon4-v1.md`, `7b1b3d54e11c…` : lue en entier ;
- `mots-de-lazar-compte-google-prepaye-bras-a-2026-11-21-v1.md`, `487b5a725b61…` ; `mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md`, `9b9ee5ca4e89…` ; `mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md`, `00af2aa83604…` : lues en entier ;
- `credits-essai-google-et-gemini-releve-v1.md`, `26ba69eeae69…` : lu en entier ;
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91…` : section 3.4 en entier (lignes 495 à 535).

Tous sous `docs/notes/relance-organismes-discrets-v1/` sauf le texte.

## Écarts

- **Titres du brouillon 43** : pour trouver 3.4, j'ai cherché les titres « 3.4 », « 3.5 » et « 4 ». Les titres de 3.5 et de 4 se sont affichés ; je n'ai pas lu ces sections.
- **Sorties longues** : le harnais a gardé d'office, hors du dépôt, sous `/root/.claude/projects/…/tool-results/`, les sorties longues du brouillon 5, du `diff` et des pièces ; je les ai relues de là. J'ai aussi copié trois extraits (brouillon 5, lignes 461 à 690 ; brouillon 43, lignes 495 à 535) et le `diff` dans le bloc-notes de la session, hors du dépôt, pour les lire.
- **Chemins cloisonnés nommés dans le texte lu** : 3.4 nomme `docs/notes/bras-a-contre-lecture-habilitee-v1/…` et des chemins sous `runs/` ; le devis nomme `scripts/chef_essai_mesure_lecteurs_bras_a_v1.py`, le journal, et des chemins sous `runs/` et `registres/`. **Je ne les ai ni suivis, ni listés, ni empreintés.**
- **Recherches de chaînes** : sur le brouillon 4, le brouillon 5 et le brouillon 43, fichiers nommés seulement.
- **Aucune liste de dossier.** Le rapport a été vérifié absent avant écriture par un `ls` sur son chemin exact.
- **Chiffres mesurés du devis** (longueurs de 6.2, octets des consignes) : non vérifiés. Ils viennent de pièces sous `runs/`, non ouvertes. L'arithmétique part des valeurs déclarées.
- **Fichiers écrits** : celui-ci. Dans le bloc-notes de la session, hors du dépôt : `verif_b5.py` (règles, signe, clés, sections touchées), `calc_b5.py` (tous les chiffres), et les extraits nommés plus haut. Rien scellé, rien committé, aucun compagnon.
- **Aucun chemin cloisonné ouvert, listé ni empreinté.** `.claude/`, `registres/`, `runs/` et le journal non touchés. Aucun appel de modèle ni appel réseau, aucune clé, aucun sous-agent, aucune dépense.
