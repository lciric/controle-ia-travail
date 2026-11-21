# Vérification des corrections de la conception des générations du collisionneur, v1

21 novembre 2026, 19:55Z (`date -u`). Contre-lecteur : Claude Opus 5.5, le même que pour `contre-lecture-conception-generations-opus-v1.md` (même dossier). Aucun appel à un modèle, aucune clé lue, aucune dépense, aucun commit. Au registre des accords, seule la ligne 668 a été ouverte, par son numéro, sans recherche. Aucun dossier de course, aucune réponse de modèle, aucun résultat lu.

## Pièces vérifiées (`sha256sum -c`, toutes « OK »)

| pièce | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/generations-v1/conception-generations-jusqu-au-plateau-v2.md` | `cf273283c6cb1cf3e5da0ada7c69ae8ed8e7f25d19ac3fd68194d2c6bce965c6` |
| `docs/notes/collisionneur-v9/generations-v1/calculs-devis-et-seuils-generations-v2.py` | `6d1c6addaf618637bbbf760b781aa77cecf933deee2c8303660e77ce0a393632` |
| `docs/notes/collisionneur-v9/generations-v1/calculs-devis-et-seuils-generations-v2-sortie.txt` | `63d1cef61a04db80e92a917d1efd6634083bb59f33e3d90a3132038134645056` |
| `docs/notes/collisionneur-v9/generations-v1/contre-lecture-conception-generations-opus-v1.md` (ma contre-lecture) | `21a84cbfd233673d2bc8eb1a2ac5d75b2fcb236f4fcfda08298eb6ac44063cfc` |

Aussi ouverts : la version 1 de la note et de l'annexe (sceaux « OK »), `collisionneur_v9_v7.py` (`319a7b66b5b9…`, importé par l'annexe), `collisionneur_v9_v8.py` (`b85690310f5c…`, lignes 526 à 580), `docs/decisions/decision-N-058-v1.md` (`854f2724864f…`, point 1).

Annexe rejouée dans mon bloc-notes (`python3 -B … collisionneur_v9_v7.py`, sans écriture de cache) : sortie identique à l'octet à la sortie scellée, code 0, « contraires à l'attendu : 0 ».

## Verdict

**À corriger, sur deux points mineurs introduits par les corrections ; les douze remarques sont corrigées.** Les deux reprises tiennent en une ligne chacune et peuvent passer par un erratum. La première touche ce que Lazar gèle au nœud 2. Le calcul, les essais et les textes servis aux modèles tiennent.

## Les douze remarques, une à une

| n° | corrigée ? | ce que j'ai vérifié |
|---|---|---|
| 1 | oui | La ligne 668 de `registres/go.md` dit, mot pour mot, « la priorité vers la conception du produit ; une propriété fixée d'avance par un tiers, vérifiée par programme, avec repli ». La section 5 la cite en entier, dit qu'elle porte sur les tâches et le produit, et ne prend que la forme, par analogie. Le nœud 2 n'a plus de défaut. Un accord est exigé par `--go-critere` à la dérivation de la génération 2 (sections 4.1, 4.2 condition 4, et 5.2). |
| 2 | oui | Section 5.6 : l'arrêt est une règle de conduite, hors de la décision N-058. La question « une génération de plus vaut-elle son prix » est renvoyée à l'épreuve sur le monde planté, et présentée comme une extension proposée, pas comme la lettre de la décision. La citation du point 1 de N-058 (« quels modèles proposent, dans quel rôle, à quelle part du budget », « seuls ») est exacte. La section 1, point 1, est en accord. |
| 3 | oui | L'option (a) est écrite dans le corps : table de la section 5.3, condition 5 de la section 4.2 (« plateau déclaré » ouvre la suite), sections 5.1 et 9.2, schéma, verdict. Le mandat demande l'essai d'une lignée « tout TENUE puis recopie » qui obtient « plateau déclaré », avec la génération 3 ouverte. Le défaut (a) du nœud 3 est le choix prudent : il retire au programme le pouvoir d'arrêter. |
| 4 | oui | Égalité exacte après `normaliser_enonce` (annexe, section 6) : 24 essais, aucun contraire, dont mes trois (0,05 devenu 0,01 ; « ne fait pas mieux » ; 200 paires devenues 20), tous rendus « différent ». La consigne A.2 dit maintenant « recopie-le tel quel ; si tu y changes un mot, un nombre ou un signe, marque-la MODIFIEE ». Par programme : seule la dernière phrase de l'énoncé de A.2 change, A.1, A.3, A.4 et A.5 sont égaux à l'octet à la version 1, et aucun des sept blocs de l'annexe A ne contient un motif de la garde de la version 8. Essais en plus, de mon côté : « a**2 » égale « a 2 » et « 10⁻³ » égale « 10-3 ». Ce sont des cas de bord sans portée pour des énoncés d'expérience, pas un défaut. |
| 5 | oui | Commandes et options nommées, chacune avec sa forme (section 4.1). Plafond de chaîne défini, sans valeur par défaut, valeur proposée au nœud 1 (86 et 68 USD, soit deux lignes ; elles couvrent les 77 à 85 et les 62,1 à 66,6 de deux générations). Options `--admettre` (identité et longueur seulement) et `--ecarter`, plus le bloc « état absent » (A.6). La phrase sur la garde de motifs est juste : lignes 530 à 578 de la version 8, refus sans admission. Recopie mesurée par Jaccard sur les ensembles de suites de trois mots, en temps linéaire ; la formule (1 − 3p)/(1 + 3p) est retrouvée, et 0,90 correspond bien à p ≈ 1,75 %. N_p est défini, avec le cas de moins de trois lignées. |
| 6 | oui | La liste fermée est en annexe B et dans le code, section 9 : 26 pièces témoins et 35 mots témoins, aucun contraire. Le témoin sain demandé (« fable », « opus » en mots ordinaires, un modèle nommé comme objet) passe. La branche (b) signale sans bloquer, et cet affaiblissement est dit (section 9.10). Reste un défaut neuf, au point A ci-dessous. |
| 7 | oui | Section 4.2 : « unité non dite dans la source, lue comme des jetons ». Le texte de 73 728 caractères de Carbon et d'Argon dépasse la borne et passe par l'option. L'annexe, section 8, le recalcule à partir du catalogue. |
| 8 | oui | « adjudant » : cinq lignées déduites de 15 cellules, composition « non vérifié ». Les sommes sont données sans lui (432 à 473) et avec lui (509 à 558), recalculées à la main. L'attendu est donné avec ses deux bases, dites non comparables (17,15 à 21,13 et 13,2 à 17,2, conformes à la sortie). |
| 9 | oui | « Borne stricte sans relance, sous les hypothèses de projection du script », avec 113,36 et 83,58 USD avec relances, dans le verdict et dans le tableau. Les deux constantes SUPPOSÉES sont nommées. |
| 10 | oui | La lecture est dite approchée. Les cinq cas exacts de la section 5 bis sont recalculés et égaux à la note (0,240 ; 0,280 ; 0,214 et 0,120 ; 0,276 et 0,160 ; 0,250 et 0,107). |
| 11 | oui | La formule écrite est celle que j'avais proposée. Elle est contrôlée pour N de 2 à 7, sans écart. L'ordre affiché pour cinq propositions, générations 2 à 4, est juste. |
| 12 | oui | La ligne a été ouverte par son numéro, et les sujets des lignes voisines ont été retirés. Un écart de méthode neuf est dit en en-tête (une liste sur le dossier de cache voisin, sans nom de fichier rendu). Rien n'en est tiré, et il ne touche aucun lieu interdit. |

Les dix changements faits hors de la lettre des remarques sont cohérents avec le reste. Le cas de la filiation et du rapport du parent copié dans le dossier de la génération 3 tient bien avec « `plateau` ne lit que le dossier enfant ». En effet, les registres de départ de la génération 3 sont dans `etat/`, puisque ce sont les réponses de la génération 2.

## Points à reprendre, introduits par les corrections

A. **La garde d'identité refuse « such as Claude » et « tu as Claude », et ces cas ne sont pas dans les faux positifs connus (section 3.3, point 2 ; section 9.10 ; annexe B ; annexe de calcul, `FORMULES`).** La formule `\b(?:as|moi,?) (?=(?:claude|gemini|chatgpt|gpt|kimi)\b)` n'est pas ancrée en tête de phrase. Essai dans mon bloc-notes avec `garde_identite` de l'annexe : « The monitor could be a model such as Claude Opus 5.5, taken as an object of study. » donne un refus (auto-désignation, position 34). « Tu as Claude Opus 5.5 comme lecteur possible » donne aussi un refus. Or nommer un modèle comme objet est justement ce que la correction voulait laisser passer avec un simple signalement. L'arbitre peut admettre la pièce, donc rien n'est perdu, mais la liste des faux positifs connus est incomplète. Correction, au choix : ajouter ces deux formes aux faux positifs connus de la section 9.10, avec deux témoins de plus à l'annexe ; ou n'accepter « as » qu'en tête de phrase (après un début de pièce, une fin de phrase ou un saut de ligne), avec un témoin sain « such as Claude ».

B. **Ce que Lazar gèle au nœud 2 est moins que ce que la section 5.2 appelle « constantes du critère ».** La section 5.2 dit que les constantes sont les quatre seuils, les trois seuils de l'alerte, « la borne de huit entrées actives et la règle d'égalité », et qu'elles « ne valent que gelées par un accord de Lazar ». Le nœud 2 n'énumère que les sept seuils. Un accord donné sur le texte du nœud laisserait donc deux constantes du critère sans gel, alors que le script les porte. Correction : énumérer les neuf au nœud 2, la règle d'égalité désignée par `normaliser_enonce` et l'empreinte de l'annexe ; ou dire au nœud 2 que l'accord porte sur toutes les constantes de la section 5.2. Les seuils de l'audit symétrique et de la recopie (0 ; 0,90 ; une entrée sur cinq ; 0,90) ne produisent que des réserves. La note peut dire en une ligne s'ils sont gelés avec les autres ou non.

## Observation, sans correction demandée

- Section 5.4 : pour une lignée non jugeable, « comptée comme entièrement renouvelée » et « ses mesures groupées portent sur les lignées jugeables » se lisent ensemble ainsi : la lignée compte pour les conditions 2 et 4, et elle est exclue des conditions 1 et 3. Le verdict n'en dépend pas, puisque la condition 2 tombe. Mais l'audit symétrique et l'alerte en dépendent. Une ligne qui le dit éviterait que le développeur doive rendre ce cas à la mère.
- Comparaisons aux seuils : l'annexe compare avec une marge de 1e-9. La note ne dit pas comment le script compare « au plus égal ». En fractions exactes, la question ne se pose pas. Ce n'est pas un défaut introduit (la version 1 était muette aussi). C'est un cas que le mandat renvoie déjà à la mère.

## Nœuds qui reviennent à Lazar

Aucun nœud neuf. Le point B change seulement le texte du nœud 2 avant que Lazar ne le lise. Les nœuds 1 à 6 de la note restent tels quels.
