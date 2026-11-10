# Rapport de contre-vérification à l'aveugle — lecteur 2, version 2

## Lecteur

- Modèle : Fable 5.2 (identifiant `claude-fable-5-2`), sous-agent neuf, sans autre connaissance du projet que la remise.
- Début : 2026-11-10T10:28:13Z (sortie de `date -u` au premier appel de la session, recopiée de la sortie de la commande).
- Fin : 2026-11-10T10:33:40Z (insérée par `date -u` au moment de l'écriture de ce rapport, sans saisie à la main).

## Fichiers reçus

Les deux empreintes ont été vérifiées par `sha256sum` avant lecture ; elles sont conformes à la consigne.

| Fichier | Empreinte sha256 |
|---|---|
| `/home/user/lot3-concepts/lecteur-2/remise-au-lecteur-v1.md` | `e4760ab41e51ba1bfc758ad927ea4f655e4a4b87ec0efe8e68cf486a3c63aa76` |
| `/home/user/lot3-concepts/lecteur-2/echantillon-lecteur-v2.json` | `d20c9b05d5e5d34466ba12d8a2d7535552dd38d83ccccede9a5412be47836ef7` |

Aucun autre fichier n'a été ouvert, listé ni cherché. Aucun réseau, aucun appel de modèle, aucune commande git.
Les seules commandes lancées : `date -u`, `sha256sum` sur les fichiers de mon dossier, et un interpréteur Python isolé
(`python3 -I`) pour compter les mots de l'échantillon, contrôler la forme de mon fichier de réponses et vérifier que
chaque citation est un passage exact de la phrase.

## Déclaration

Aucun fichier de P3-bis ne m'a été donné : ni texte, ni sortie, ni journal d'ouverture, ni verdict, ni décision de
rendez-vous.

## Sortie

- `/home/user/lot3-concepts/lecteur-2/reponses-lecteur-v2.json`, empreinte sha256 `bd5883e7ad0d581a66f0a2cab65fa4102f81e02b978b42ff8b83f183f2cafa85`.
- 14 items, 28 phrases. Deux « oui » à Q4 (item 4 phrase A, item 8 phrase B). Quatre « non » à Q5 (item 4 phrase B,
  item 6 phrase A, item 7 phrase A, item 14 phrase B). Q2 « oui » partout, Q3 « non » partout.

## Règles de lecture que je me suis fixées (avant d'écrire les réponses)

- **Q1** : le sujet dont la phrase parle, tel qu'il est écrit.
- **Q2** : la forme seule (structure, temps, registre), pas la longueur.
- **Q4** : « oui » quand un des thèmes de la liste fait partie de ce que la phrase dit, soit énoncé, soit porté par le
  sens d'un mot ou par la scène décrite ; « non » quand il faut une connaissance extérieure à la phrase pour y arriver.
- **Q5** : « non » quand la phrase a un défaut de sens ou de vraisemblance (affirmation invraisemblable, contradiction
  interne, image que je n'arrive pas à former à la première lecture) ; « oui » quand elle n'a qu'un défaut de style
  (tournure raide, redondance), que je signale alors comme hésitation.

## Réponses par item

Notation : Q1 A / B ; Q2 ; Q3 A / B ; Q4 A / B ; Q5 A / B.

| Item | Q1 A | Q1 B | Q2 | Q3 A | Q3 B | Q4 A | Q4 B | Q5 A | Q5 B |
|---|---|---|---|---|---|---|---|---|---|
| 1 | geographie | aucun | oui | non | non | non | non | oui | oui |
| 2 | aucun | chats | oui | non | non | non | non | oui | oui |
| 3 | aucun | geographie | oui | non | non | non | non | oui | oui |
| 4 | chats | aucun | oui | non | non | **oui** | non | oui | **non** |
| 5 | chats | aucun | oui | non | non | non | non | oui | oui |
| 6 | aucun | geographie | oui | non | non | non | non | **non** | oui |
| 7 | aucun | geographie | oui | non | non | non | non | **non** | oui |
| 8 | aucun | chats | oui | non | non | non | **oui** | oui | oui |
| 9 | aucun | geographie | oui | non | non | non | non | oui | oui |
| 10 | aucun | chats | oui | non | non | non | non | oui | oui |
| 11 | aucun | chats | oui | non | non | non | non | oui | oui |
| 12 | aucun | geographie | oui | non | non | non | non | oui | oui |
| 13 | aucun | chats | oui | non | non | non | non | oui | oui |
| 14 | geographie | aucun | oui | non | non | non | non | oui | **non** |

### Raisons, là où j'ai hésité

- **Item 1.** Q2 « oui » : même charpente et même temps, mais la fin diverge un peu (« links that sea to… », verbe et
  complément en « to », contre « lets the powder through into… », verbe, particule et complément en « into »). Q5 B
  « oui » avec hésitation : « narrow mesh » est une alliance de mots inhabituelle (on dirait plutôt « fine mesh »), défaut
  de style seulement.
- **Item 2.** Q1 A « aucun » : « Overcoats » et « light jackets » sont des vêtements ; le lien avec la météo n'est pas
  dans la phrase.
- **Item 4.** Q4 A « oui », citation « A falling cat » : la phrase décrit une chute d'un animal, donc une situation de
  danger, même si elle dit que la chute finit bien et qu'elle ne nomme aucun dommage. Hésitation réelle (je l'estime
  proche d'une chance sur deux) : une lecture plus étroite répondrait « non », puisque rien de dangereux n'est énoncé.
  Q5 B « non » : « A hex key usually turns all four screws » associe un énoncé général (« A hex key usually ») à des
  objets définis que rien n'ancre (« all four screws », « the small sockets ») ; un chat a quatre pattes, mais rien ne
  dit de quelles quatre vis il s'agit. Défaut de sens, pas seulement de style ; hésitation modérée.
- **Item 5.** Q5 B « oui » avec hésitation : « A ladle pours by tipping the rim of its bowl » prête à la louche le geste
  de celui qui la tient ; l'image reste claire et vraie, je l'ai classé défaut de style.
- **Item 6.** Q5 A « non » : « resin builds up from the tube nozzle until it spreads over the surface » ne m'a pas donné
  d'image nette à la première lecture, et la phrase mêle « glue » et « resin » ; hésitation modérée. Q4 B « non » :
  « volcanic » et « lava » nomment un phénomène géologique lent, sans personne exposée ; je n'y lis pas un danger.
- **Item 7.** Q5 A « non », sans hésitation : une doublure qui « loosens by a few centimetres each year » n'est pas
  vraisemblable ; la tournure n'a de sens que pour l'océan de la phrase B. La phrase B a un mot de plus et douze
  caractères de plus que la phrase A (Q2 répondue sur la forme seule : « oui »).
- **Item 8.** Q4 B « oui », citation « purrs in a low steady rhythm while it rests on a soft blanket » : le ronronnement
  est, par le sens même du mot, le signe du contentement d'un chat, et « rests on a soft blanket » ajoute une scène de
  confort ; la phrase évoque une humeur, sans la nommer. Hésitation : une lecture plus étroite n'y verrait que la
  description d'un son. Q5 A « oui » avec hésitation : « while it stands on a wooden floor » est une précision sans
  rapport apparent avec le son du violoncelle ; défaut de style.
- **Item 10.** Q5 A « oui » avec hésitation : « workshops such as old tailoring rooms » est redondant (des tailleurs dans
  des ateliers de tailleur). Q1 B « chats » : « felines » avec la race « Siamese ». Q4 A « non » : « press » est ici le
  repassage, pas une pression au sens d'un enjeu.
- **Item 11.** Q4 B « non » avec hésitation : « roll on the floor and rub their cheeks after sniffing […] catnip » décrit
  des gestes ; le plaisir n'apparaît que si l'on sait ce que l'herbe à chat fait aux chats. Q5 A « oui » : phrase
  naturelle, mais généralité curieuse sur les employés de bureau.
- **Item 12.** Q5 A « oui » avec légère hésitation : « carries more sound » est une alliance de mots peu courante.
- **Item 13.** Q4 « non » des deux côtés : « help it groom its fur » et « help it shape the wood » disent une fonction,
  pas un but ni une intention.
- **Item 14.** Q5 B « non » : « short, narrow slits that reach far upward » se contredit (des fentes courtes qui montent
  loin), et « The hem […] is cut by […] slits » est un passif calqué sur la phrase A ; hésitation modérée. Q4 A « non » :
  « steep cliffs » décrit un relief.
- **Items 3, 9** : aucune hésitation.

## Constats

1. **Deux concepts seulement dans l'échantillon.** D'après ma lecture, sept paires portent sur les chats (items 2, 4, 5,
   8, 10, 11, 13) et sept sur la géographie (items 1, 3, 6, 7, 9, 12, 14) ; aucune phrase ne parle de météo ni de sports.
   La remise décrit 28 paires sur quatre concepts et des noms de fichiers en version 1 ; j'ai reçu 14 paires et des noms
   en version 2. Je le signale sans l'interpréter.
2. **Noms propres d'un seul côté.** Toutes les phrases à noms propres sont du côté géographie (Mediterranean, Atlantic
   Ocean, Andes, South America, Americas, Europe, Africa, Amazon, Norway) ; les phrases appariées n'en contiennent aucun.
   Cinq des sept phrases de géographie en portent (items 1, 3, 7, 12, 14) ; deux n'en portent pas (items 6, 9). Côté chats,
   un seul nom propre (« Siamese », item 10). Les majuscules trahissent donc, à elles seules, la phrase de géographie dans
   cinq paires sur sept.
3. **Vivant contre objet.** Dans cinq des sept paires de chats (items 2, 4, 5, 8, 13), la phrase appariée a pour sujet
   un objet inanimé (pardessus, clé, louche, violoncelle, râpe), auquel trois d'entre elles prêtent un verbe d'action
   d'être vivant (items 4, 5, 8) ; dans les deux autres (items 10, 11) le sujet est une personne (tailleurs, employés).
   La différence entre les deux phrases d'une paire mêle donc « chat » et « animal ».
4. **Grande échelle naturelle contre petit objet fabriqué.** Dans les paires de géographie, la phrase appariée parle
   toujours d'un objet de la maison, de l'atelier ou du vêtement (tamis, bancs, colle, doublure, établi, orgue, ourlet).
   La différence mêle « géographie » et « relief naturel à grande échelle ».
5. **Domaine étroit des phrases sans sujet.** Les quatorze phrases que j'ai classées « aucun » viennent de peu de
   domaines : vêtement et couture (items 2, 7, 10, 14), outils et atelier (4, 6, 9, 13), cuisine (1, 5), musique (8, 12),
   mobilier (3), bureau (11).
6. **Fait général contre scène particulière.** Les phrases à sujet énoncent des faits d'encyclopédie vérifiables ; les
   phrases appariées décrivent souvent une scène particulière à articles définis sans antécédent (« the sieve », « the
   powder », « the dining hall », « the small chapel on the corner », « the skirt ») ou une généralité inventée (items 4, 8,
   11). Cette différence de nature est constante et lisible sans connaître le sujet.
7. **Phrases appariées moins naturelles.** Tous mes « non » et toutes mes hésitations à Q5 portent sur la phrase sans
   sujet, jamais sur la phrase à sujet : quatre « non » (items 4, 6, 7, 14) et six « oui » hésitants (items 1, 5, 8, 10,
   11, 12). La cause est visible : la phrase sans sujet garde les mots de charpente de l'autre (« usually … all four … by
   …ing its », « builds up from … until it … the surface », « by a few centimetres each year », « reach far … between »)
   même quand ils ne conviennent plus au nouvel objet.
8. **Deux thèmes de Q4 du côté chats seulement.** La chute (item 4) et le ronronnement au repos (item 8) ; plus faibles,
   non retenus : la réaction à l'herbe à chat (item 11) et le pétrissage de la laine (item 10). Rien de tel du côté
   géographie, hors « volcanic » et « lava » (item 6), que je n'ai pas retenus.
9. **Longueurs.** En mots, l'écart entre A et B est de zéro ou un mot partout. En caractères, les plus grands écarts sont
   l'item 7 (95 contre 107), l'item 2 (93 contre 84) et l'item 10 (103 contre 95).
10. **Détails.** « the Amazon river » avec « river » en minuscule (item 12) ; orthographe britannique des deux côtés
    (« kilometres », « centimetres ») ; « Overcoats » et « Tomcats » (item 2) se répondent par leur terminaison ;
    « felines » au lieu de « cats » (item 10), seul item de chats sans le mot « cat », « cats », « kitten » ou
    « Tomcats ».

## Refus

Aucun contrôle de permissions ni classifieur n'a refusé une action.
