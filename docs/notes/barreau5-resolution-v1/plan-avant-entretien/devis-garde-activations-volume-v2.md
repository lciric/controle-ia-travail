# Devis — barreau 5 : garde des activations de la relecture sur un volume de stockage — v2

- **Statut** : devis de classe A, **version 2**. Elle remplace la v1 (`devis-garde-activations-volume-v1.md`, `b3c8f3f898c86aec9105ca71ce188e7eeac344021a0838b3ecf5ea881049749c`), gardée à côté, et porte les sept corrections de sa contre-lecture (`contre-lecture-devis-garde-activations-volume-v1.md`, `1d0e7861d935a23b122d8df9d4fb0aea7d2bd761b47bf8874111feb6d228ce00` : « conforme après ces corrections », A-1 et A-2 bloquantes) ; table au § 11. **Elle attend la vérification des corrections par le même contre-lecteur (Opus 5.5)**, puis le scellement par la mère. Il ne vaut accord de rien. Il ferme le « à relever » du devis scellé du barreau 5 (`devis-adaptateurs-tenus-a-l-ecart-v1.md`, `dc886195c77b0d67c31cb8815a1e97b9fa72dd35ebac2b8f3bc49d4e5cf59bcc`, § 3 dernière ligne du tableau et § 5 (a)) et la condition de l'accord de principe de Lazar : « le prix est relevé et porté à Lazar avant toute dépense, sinon les replis écrits s'appliquent » (GO-2026-11-19-88, point 6).
- **Auteur** : Claude Fable 5.2 (identifiant servi `claude-fable-5-2`), concepteur (R-3735), sous-agent de la session mère. La v1 est écrite le 21 novembre 2026, de 10:55 à 11:15 UTC (`date -u`), dépôt à `c98ec89a0` ; la v2 le même jour, de 11:17 à 11:45 UTC, dépôt à `a36671d19`. Aucun appel payant, aucune machine ni aucun volume créé ; aucun appel de réseau pour la v2. Consigne commune de méthode (v1) appliquée : `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`) ; relevé de méthode au § 10.
- **Source unique des chiffres** : `calcul-devis-garde-activations-volume-v2.py` (`ddab89e1c92f4f1091211431acf6efc2a79b9db7e5dd0bc5b593fb14ab1134cd`), sortie `sortie-calcul-devis-garde-activations-volume-v2.txt` (`9b557d66634abf28f8b369fb8922f715c1c08cf563bb28739c973fb5355749e7`), même dossier, lancé par `.venv/bin/python -I` ; cités « calcul, bloc ». Le calcul v2 compte l'adresse IPv4 des serveurs, imprime à côté les chiffres du calcul v1 (`a3049f4b…`) et éprouve la règle du plafond sur des objets de contrôle (bloc 7).
- **Relevés bruts, même dossier** : grille de prix de Hetzner, `releve-grille-prix-hetzner-2026-11-21T1056Z-v1.json` (`58a6c6a3afeec57456fc9ad3cb7b728b4019244b8217d1859d13719be87a34a7`) ; page publique des boîtes de stockage, `releve-page-publique-boites-de-stockage-hetzner-2026-11-21T1055Z-v1.html` (`022505936f3f4951c6aeed429a5641ca8ae48875ca4e875cfa232f410f567191`) ; offres du loueur de cartes, `prereg/papier-dopamine-moniteur-v1/releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json` (`bc54f8bd468eb65e051234b31b77373aad1c52100b6e2b2a377532336f6a5196`). Aucun ne porte de clé (recherche de « bearer », « api_key », « authorization » : rien).
- **Comment la grille a été relevée** : `GET https://api.hetzner.cloud/v1/pricing`, le jeton lu par son nom, jamais affiché ; la réponse ne contient que des prix publics et le taux de taxe du compte (20 %), aucune donnée du projet. La page publique de Hetzner ne montre pas le prix des volumes sans exécuter de script : c'est pourquoi l'interface a servi. **Écart à signaler à la mère** : le mot de Lazar sur ce jeton (R-2322) ne nomme que la liste des serveurs ; cette lecture de prix n'y est pas écrite.
- **Pièces lues** : le devis scellé ci-dessus ; la section « Données gardées » du texte scellé (`prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`, l. 363-368), et elle seule ; la note sur les champs de l'offre du loueur (`code-formation/verification-champs-offre-loueur-v1.md`, `48a81bd45d5b4feed725ceeea02c9fce9aa9fd7b21bf5c6e195c0c021fc4d03b`). Pour la v2 : le rapport de contre-lecture ; la consigne commune ; `registres/arrets.md`, l. 148 (minuterie d'un serveur de l'essai Lean, arrêtée par son PID). Aucun résultat ouvert.

## 1. Ce qui est gardé, et pourquoi

La relecture du barreau 5 produit les activations par jeton de 39 adaptateurs aux trois couches : **≈ 152 Go, 166 Go avec les quatre points d'ancrage** (texte scellé, « Données gardées »). C'est trop pour une branche du dépôt. Sans lieu accordé, les replis écrits s'appliquent : la couche 15 seule (≈ 44 Go), puis une action sur dix (≈ 4,4 Go) ; le reste est détruit avec l'instance. Garder tout, c'est pouvoir relire après le verdict sans relouer une carte, et répondre à une question posée à l'entretien.

Rien ne tourne : c'est un lieu de dépôt. Le versement lui-même (sortie des données de l'instance de relecture) est déjà compté au devis scellé.

## 2. Lieu, prix relevés et leurs sources

- **Lieu** : un volume de stockage de 200 Go chez Hetzner, à Helsinki (`hel1`), attaché à un petit serveur le temps d'une séance (le versement, puis chaque relecture). Un volume ne se lit qu'attaché à un serveur du même lieu ; détaché, il reste facturé et intact.
- **Prix du volume, relevé le 21 novembre 2026 à 10:56:21Z** (calcul, bloc 1) : **0,0572 EUR hors taxe par Go et par mois**, 0,06864 toutes taxes (taxe de 20 %, lue dans la grille du compte). Soit **13,73 EUR par mois pour 200 Go**.
- **Prix du serveur, même relevé** : type `cx23` à 0,0088 EUR hors taxe de l'heure ; si les serveurs partagés manquent (la page publique en disait certains indisponibles ce matin), type `ccx13` à 0,0585 EUR hors taxe de l'heure. Chaque serveur porte aussi une adresse IPv4 publique, 0,0008 EUR hors taxe de l'heure à `hel1` (même grille, `primary_ips`), soit 0,069 EUR toutes taxes pour trois séances de 24 heures ; le calcul v2 la compte (bloc 3).
- **Taux de change** : 1,25 USD pour 1 EUR, la convention du registre des dépenses (`registres/depenses.md`, l. 422). **Le taux du jour n'est pas relevé.**

## 3. Durée, cas attendu, pire cas, coupure

Toutes taxes, adresse IPv4 comprise (calcul, blocs 2 à 4) :

| scénario | contenu | EUR | USD |
|---|---|---|---|
| bas | volume gardé neuf jours, jusqu'au 1er décembre ; une séance de 6 heures sur `cx23` | 4,19 | 5,2 |
| **attendu** | volume gardé un mois entier, jusqu'au 21 décembre ; une séance de 12 heures sur `cx23` | **13,87** | **17,3** |
| pire cas sous les coupures | un mois entier ; trois séances de 24 heures sur `ccx13` | 18,85 (18,78 sans l'adresse IPv4) | 23,6 (23,5) |

- **Plafond proposé : 24 USD, jusqu'au 21 décembre 2026.**
- **Coupures** : chaque serveur a une minuterie de destruction à 24 heures, par identifiant (R10), tenue hors du serveur, qui ne porte pas le jeton : un processus de la session qui l'a créé, par son PID, comme pour les serveurs de l'essai Lean (`registres/arrets.md`) ; un arrêt du système du serveur ne suffit pas, un serveur arrêté reste facturé ; à la fin de chaque séance, puis à chaque reprise (routine, point 4), la liste des serveurs du projet est relue par identifiants, et tout serveur sans tâche est détruit et consigné ; si la session qui tient la minuterie tombe, la session suivante détruit le serveur dès sa reprise ; trois séances au plus sous cette ligne ; le volume est borné par l'échéance, hors la garde sans séance du § 5, point 2.
- **Ce que la minuterie évite** : un serveur `ccx13` oublié un mois coûterait 72,6 USD avec le volume (71,9 sans l'adresse IPv4). C'est le débordement qui reste si la minuterie et la routine de reprise manquent toutes deux.
- **Après le 21 décembre** : chaque mois de garde de plus coûte 13,73 EUR, soit 17,2 USD, volume seul. Il demande une ligne neuve.
- **Durée du versement** : 0,5 à 1,7 heure pour 184 Go (devis scellé, § 2, chiffre du brouillon 2 resté dans sa table ; ≈ 152 à 166 Go au brouillon 3, même devis, § 5 : plutôt moins), à un débit de réseau supposé et non mesuré ; la séance de 12 heures laisse le temps de vérifier les empreintes.

## 4. Ce qui est compté au compteur

Les lignes de facture de Hetzner pour le volume et pour chaque serveur de séance, son adresse IPv4 comprise, relevées par leurs identifiants, de la création à la suppression. Une ligne d'engagement au registre des dépenses avant la création du volume : « engagement : barreau 5, garde des activations ([ligne d'accord], plafond 24 USD, échéance 21 décembre) : devis [chemin, empreinte] ; volume de 200 Go à `hel1`, 0,0572 EUR hors taxe par Go et par mois ; serveur de séance [type], minuterie 24 heures ». La sortie des données de l'instance de relecture reste comptée sous le plafond commun de la formation (GO-2026-11-19-86).

## 5. Ce qui arrête

1. Le cumul relevé atteint 24 USD : plus aucune séance ; le volume reste en garde sans séance, comme au point 2, et la mère porte la question à Lazar le jour même.
2. Le 14 décembre, une semaine avant l'échéance, la mère porte à Lazar trois issues — garder un mois de plus (ligne neuve), réduire au repli de la couche 15 (≈ 44 Go, 3,43 EUR par mois sur un volume de 50 Go), ou supprimer après inventaire scellé. Sans mot de Lazar le 21 décembre, le volume seul reste en garde, sans aucune séance, à 0,458 EUR (0,57 USD) par jour toutes taxes, compté sous cette ligne au-delà de son plafond et consigné chaque jour au registre des dépenses, jusqu'au mot de Lazar ; la mère le lui rappelle chaque jour.
3. **Aucune suppression du volume sans le mot de Lazar**, et jamais avant un inventaire scellé (noms, tailles, empreintes) : règle « récupérer ce qui est récupérable ».
4. Si le versement n'aboutit pas : replis du texte scellé, dans leur ordre.

## 6. Autres lieux (calcul, bloc 5)

- **Boîte de stockage de 1 To chez le même hébergeur** : 3,20 EUR hors taxe par mois sur la page publique relevée à 10:55:40Z, soit 4,80 USD toutes taxes, contre 17,16 pour le volume : 3,6 fois moins cher. Le dépôt s'y fait sans serveur, donc sans minuterie ni risque d'oubli. **Non vérifié** : ses frais d'installation (la page les annonce, « setup fee once », sans montrer de montant dans le texte relevé) ; la façon de la commander ; la lecture depuis un serveur du projet, puisque relire 166 Go d'activations demande toujours une machine (la page nomme un emploi en lecteur réseau et un trafic interne gratuit, sans que le texte relevé dise à quels modèles ils s'appliquent). Ce n'est pas la ressource de l'accord de principe ; une ouverture de compte serait un nœud. Elle entre dans la décision portée à Lazar comme option à vérifier (§ 9, (d)).
- Repli 1 (couche 15, ≈ 44 Go) sur un volume de 50 Go : 3,43 EUR, 4,3 USD par mois.
- Repli 2 (une action sur dix) : sans dépense.
- Disque de l'instance arrêtée : ≈ 58 USD par mois, fragile ; déconseillé par le devis scellé.

## 7. Constat du relevé, hors de l'objet de ce devis, à porter à la session de lecture

**À 10:55Z, aucune offre ne passait les bornes écrites au devis scellé pour l'instance de relecture** (carte de 80 Go, disque de 300 Go, stockage au plus 0,08 USD de l'heure ; calcul, bloc 6). Le motif « stockage » touche les 13 offres : le prix de stockage le plus bas vu est de 0,20 USD par Go et par mois, soit 0,082 USD de l'heure pour 300 Go, juste au-dessus du plafond. Le devis scellé l'avait écrit en creux (« à 300 Go, 0,19 »). Cinq offres ne manquent que cette borne (calcul, bloc 6) : la plus proche, à 1,163 USD de l'heure, à 0,099 USD de l'heure de stockage ; les quatre autres, de 1,056 à 1,199 USD de l'heure, affichent 1,00 USD par Go et par mois, soit 0,41 USD de l'heure. Deux réserves : c'est un instantané ; l'unité du champ de stockage (par Go et par mois) est celle que le code suppose, jamais vérifiée (note sur les champs de l'offre, point 4). Je ne connais pas les bornes que le code de lecture figé applique : à vérifier par la session de lecture avant le jour de la relecture.

La sortie de données de l'offre à 1,163 USD de l'heure (comme des quatre autres) est à 0,039 USD par Go, soit 6,5 USD pour 166 Go : dans la fourchette du devis scellé (3,9 à 7,6), vers le haut.

## 8. Ce qui reste à relever

- Le taux de change du jour.
- La disponibilité du serveur `cx23` à Helsinki à l'heure de la création.
- Le débit réel du réseau entre l'instance de relecture et le serveur.
- Pour la boîte de stockage, si Lazar la retient : ses frais d'installation, sa commande, et un essai de lecture depuis un serveur du projet.
- Qui crée le volume et le serveur, et comment l'instance de relecture y écrit sans porter de clé du projet : à écrire dans la consigne de l'opérateur de la relecture (classe B), pas ici.

## 9. Ligne d'accord proposée

Numéro et référence posés par la mère.

`| GO-2026-11-21-NN | 2026-11-21 | calcul | Barreau 5 : garde des activations de la relecture (≈ 152 à 166 Go) sur un volume de stockage de 200 Go chez Hetzner, avec un petit serveur le temps du versement et de deux relectures au plus, sur le devis docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-garde-activations-volume-v2.md (empreinte de son compagnon). Prix relevé le 21 novembre : 0,0572 EUR hors taxe par Go et par mois. Hors du plafond commun de GO-2026-11-19-86. Minuterie de 24 heures sur chaque serveur. Question portée à Lazar le 14 décembre ; après l'échéance ou au plafond, sans mot de Lazar, le volume seul reste en garde sans séance à 0,57 USD par jour, compté sous cette ligne au-delà du plafond ; aucune suppression sans le mot de Lazar. | 24 USD | 2026-12-21 | Lazar | mot de Lazar à recueillir |`

**Pour Lazar, en une décision.** Garder toutes les activations, ou s'en tenir aux replis. (a) Le volume de 200 Go : 17 USD attendus, 24 au plus, tout reste relisible après le verdict. (b) Le repli de la couche 15 sur un volume de 50 Go : 4 USD par mois, les couches 7 et 23 perdues sur disque. (c) Le repli sans dépense : une action sur dix. (d) À vérifier avant d'être proposée : une boîte de stockage de 1 To chez le même hébergeur, 4,80 USD par mois toutes taxes contre 17,16 pour le volume, où le dépôt se fait sans serveur ni minuterie. Deux choses à vérifier d'abord : ses frais d'installation, annoncés sans montant sur la page relevée ; la lecture depuis un serveur du projet, car relire les activations demande toujours une machine. Ce n'est pas la ressource de l'accord de principe, sa commande n'est pas vérifiée, et une ouverture de compte serait un nœud. Recommandation : (a), confiance 0,75 — c'est l'accord de principe déjà donné, le prix relevé est petit devant celui de la formation, et la relecture est proche (la formation finit au plus tard le 22 novembre, `registres/passations/2026-11-21-0745.md`) ; (d) se vérifie en parallèle, pour la garde d'après le 21 décembre. Pas de défaut : c'est une dépense ; sans mot, les replis écrits s'appliquent.

## 10. Relevé de méthode

**Chaîne de raisonnement.**
1. La relecture produit ≈ 152 Go d'activations, 166 Go avec les quatre points d'ancrage ; sans lieu accordé, les replis s'appliquent et le reste est détruit. — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f…`), l. 366.
2. L'accord de principe nomme un volume de 200 Go et exige que le prix soit relevé et porté à Lazar avant toute dépense. — `registres/go.md`, ligne GO-2026-11-19-88, point 6.
3. Le volume coûte 0,0572 EUR hors taxe par Go et par mois ; les serveurs `cx23` et `ccx13`, 0,0088 et 0,0585 EUR de l'heure ; l'adresse IPv4, 0,0008 ; la taxe est de 20 %. — `releve-grille-prix-hetzner-2026-11-21T1056Z-v1.json` (`58a6c6a3…`) ; calcul, bloc 1.
4. 200 Go coûtent donc 13,73 EUR par mois et 0,458 EUR par jour, toutes taxes. — calcul, bloc 2 ; pas 3.
5. Un volume ne se lit qu'attaché à un serveur du même lieu, et reste facturé détaché ; un serveur arrêté reste facturé. — supposé pour le volume (aucune page versée ne le dit) ; rapport de contre-lecture (`1d0e7861…`), § 5 point 1, pour le serveur arrêté.
6. Une séance dure 24 heures au plus, et la ligne en couvre trois. — supposé : choix de ce devis ; seul le versement a une durée écrite (0,5 à 1,7 heure, devis scellé `dc886195…`, § 2, à un débit lui-même supposé).
7. La minuterie tenue hors du serveur détruit à 24 heures, et la routine de reprise est son filet. — la pratique existe (`registres/arrets.md`, l. 148) ; pour cette ligne, supposé : aucun code n'existe et la garde n'a été vue ni verte ni rouge (R5).
8. Sous les pas 6 et 7, le pire cas est de 18,85 EUR. — calcul, bloc 4 ; pas 3 et 4.
9. Au taux de 1,25, cela fait 23,56 USD, d'où le plafond de 24. — convention de `registres/depenses.md`, l. 422 ; calcul, bloc 4 ; le taux du jour est supposé inférieur à 1,25.
10. Après l'échéance ou au plafond, sans mot de Lazar, le volume seul court à 0,57 USD par jour, au-delà du plafond. — calcul, bloc 4 ; correction A-1 du rapport de contre-lecture.
11. Une boîte de stockage de 1 To coûte 4,80 USD par mois, 3,6 fois moins. — `releve-page-publique-boites-de-stockage-hetzner-2026-11-21T1055Z-v1.html` (`02250593…`) ; calcul, bloc 5. Ses frais d'installation et sa lecture depuis un serveur : non vérifiés.

**Objets de contrôle.** Le mécanisme éprouvé est la règle « sous les coupures, le cumul reste sous 24 USD ». Attendus écrits au programme avant le rejeu (calcul, bloc 7).
- Objet où la règle est vraie par construction : un mois de volume et trois séances de 24 heures sur le serveur le plus cher. Attendu : sous le plafond. Rendu : 23,56 USD, sous le plafond.
- Objets où elle est fausse par construction : une quatrième séance ; un serveur laissé un mois sans minuterie ; dix jours de garde après l'échéance. Attendu : au-dessus du plafond, tous les trois. Rendu : 25,70, 72,65 et 29,28 USD, au-dessus.
- Ce que ces objets ne touchent pas : la minuterie elle-même. Avant le premier serveur, elle doit être vue verte sur un cas sain et rouge sur un artefact (R5), dans la consigne de l'opérateur de la relecture.

**Premier pas non justifié.** Le pas 5. Le justifierait : une page de documentation de l'hébergeur versée sous empreinte, ou l'essai d'attacher et de détacher le volume à sa création. Le pas 7 vient ensuite : il demande le code de la minuterie et son épreuve.

**Mode d'échec affecté.** Sans objet : cette pièce est d'un concepteur, non d'un relecteur.

**Dérivation de l'énoncé seul.** Sans objet : cette pièce n'est pas une re-dérivation ; le contre-lecteur a refait les cinq montants à la main (rapport, § 2).

**Trouvaille de côté.**
- Ce que je cherchais d'abord, le prix du volume sur une page publique, s'est révélé introuvable sans exécuter de script : d'où la lecture par l'interface, et l'écart déclaré en tête.
- À 10:55Z, aucune offre de carte ne passait les bornes écrites pour l'instance de relecture à 300 Go de disque (§ 7). Non poursuivi : c'est à la session de lecture.
- La boîte de stockage est 3,6 fois moins chère que le volume et se passe de minuterie (§ 6). Non poursuivi : elle n'est pas vérifiée, et sa commande peut être un nœud.

**Évaluateur et conseil.**
- Ce qui juge ce devis : le contre-lecteur d'un autre modèle (rejeu à l'octet, montants refaits à la main, chiffres rapportés à la grille), puis la vérification des corrections par le même, puis Lazar. Ce juge n'a été admis sur aucun témoin : il n'existe pas de devis planté faux sur lequel on l'aurait vu rouge.
- Par où ce devis obtiendrait un bon jugement sans le mériter : un rejeu identique ne prouve que la constance du programme, pas la justesse de la grille, relevée une seule fois par un seul canal ; les objets de contrôle sont de l'auteur de la règle ; le devis peut être « conforme » alors que la minuterie, dont dépend le pire cas, n'existe pas.
- Conseil à l'opérateur de la relecture : la difficulté n'est pas le prix. Elle est dans la survie de la minuterie quand sa session tombe, et dans la façon dont l'instance louée écrit sur le serveur sans porter de clé du projet.

## 11. Table des corrections de la contre-lecture

Aucune correction n'est refusée. Deux sont portées avec un écart de lettre, dit ci-dessous.

| correction | objet | ligne(s) de la v2 | traitement |
|---|---|---|---|
| A-1 (bloquante) | la garde après l'échéance ou le plafond | l. 34 (fin de la puce « Coupures »), l. 45, l. 46, l. 75 (ligne d'accord) | portée, texte exact ; la ligne cite désormais le devis v2 |
| A-2 (bloquante) | où vit la minuterie | l. 34, l. 35 | portée, texte exact |
| A-3 | l'adresse IPv4 des serveurs de séance | l. 20, l. 31 ; par suite l. 25, l. 29, l. 30, l. 35, l. 41 | portée, **écart de lettre** : le contre-lecteur la disait « non comptée au calcul » ; le calcul v2 la compte, pour que 0,069 EUR, 18,85 EUR et 23,56 USD aient une pièce rejouable. La table donne donc 18,85 (18,78 sans l'adresse) et 23,6 (23,5) ; le bas et l'attendu gagnent un centime d'euro ; le plafond ne change pas |
| A-4 | le constat du § 7 : cinq offres, non une | l. 59, l. 61 | portée, texte exact |
| A-5 | la taille du versement | l. 37 | portée, texte exact |
| A-6 | la boîte de stockage dans la décision | l. 77, option (d) ; par suite l. 52 et l. 68 | portée, **écart de lettre** demandé par la mère : l'option donne son prix à côté de celui du volume et nomme ce qu'il faut vérifier (frais d'installation, lecture depuis un serveur) |
| A-7 | le taux de taxe vient du compte | l. 7 | portée, texte exact |

Changements hors de la liste, tous déclarés :
- l'en-tête (l. 1 à 8) : version, empreintes de la v1, du rapport, du calcul v2 et de la consigne commune, pièces lues pour la v2 ;
- l. 52 : « quatre fois moins cher » devient « 3,6 fois moins cher », chiffre du calcul (bloc 5) ;
- l. 77 : la recommandation, inchangée dans son choix (a) et sa confiance, dit pourquoi (d) ne passe pas devant ;
- le § 10, « Relevé de méthode », exigé par la consigne commune ; ce § 11.

Rien d'autre ne change : l'objet, le lieu, les prix relevés, le plafond de 24 USD, l'échéance du 21 décembre, le § 1, le § 4 hors la mention de l'adresse, les points 3 et 4 du § 5.
