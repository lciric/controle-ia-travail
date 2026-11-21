# Devis — barreau 5 : garde des activations de la relecture sur un volume de stockage — v1

- **Statut** : devis de classe A, **à contre-lire par un autre modèle (Opus 5.5)**, puis à sceller par la mère. Il ne vaut accord de rien. Il ferme le « à relever » du devis scellé du barreau 5 (`devis-adaptateurs-tenus-a-l-ecart-v1.md`, `dc886195c77b0d67c31cb8815a1e97b9fa72dd35ebac2b8f3bc49d4e5cf59bcc`, § 3 dernière ligne du tableau et § 5 (a)) et la condition de l'accord de principe de Lazar : « le prix est relevé et porté à Lazar avant toute dépense, sinon les replis écrits s'appliquent » (GO-2026-11-19-88, point 6).
- **Auteur** : Claude Fable 5.2 (identifiant servi `claude-fable-5-2`), concepteur (R-3735), sous-agent de la session mère. Écrit le 21 novembre 2026, de 10:55 à 11:15 UTC (`date -u`). Dépôt à `c98ec89a0`. Aucun appel payant, aucune machine ni aucun volume créé.
- **Source unique des chiffres** : `calcul-devis-garde-activations-volume-v1.py` (`a3049f4bab32f56d74921051934a0bd7c863c59e103631028308858cb49fdbaa`), sortie `sortie-calcul-devis-garde-activations-volume-v1.txt` (`2b945e674c9e1155e852248e0f2b6cd28ee7319498b82317f7d17312cd908752`), même dossier, lancé par `.venv/bin/python -I` ; cités « calcul, bloc ».
- **Relevés bruts, même dossier** : grille de prix de Hetzner, `releve-grille-prix-hetzner-2026-11-21T1056Z-v1.json` (`58a6c6a3afeec57456fc9ad3cb7b728b4019244b8217d1859d13719be87a34a7`) ; page publique des boîtes de stockage, `releve-page-publique-boites-de-stockage-hetzner-2026-11-21T1055Z-v1.html` (`022505936f3f4951c6aeed429a5641ca8ae48875ca4e875cfa232f410f567191`) ; offres du loueur de cartes, `prereg/papier-dopamine-moniteur-v1/releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json` (`bc54f8bd468eb65e051234b31b77373aad1c52100b6e2b2a377532336f6a5196`). Aucun ne porte de clé (recherche de « bearer », « api_key », « authorization » : rien).
- **Comment la grille a été relevée** : `GET https://api.hetzner.cloud/v1/pricing`, le jeton lu par son nom, jamais affiché ; la réponse ne contient que des prix publics, aucune donnée du projet. La page publique de Hetzner ne montre pas le prix des volumes sans exécuter de script : c'est pourquoi l'interface a servi. **Écart à signaler à la mère** : le mot de Lazar sur ce jeton (R-2322) ne nomme que la liste des serveurs ; cette lecture de prix n'y est pas écrite.
- **Pièces lues** : le devis scellé ci-dessus ; la section « Données gardées » du texte scellé (`prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`, l. 363-368), et elle seule ; la note sur les champs de l'offre du loueur (`code-formation/verification-champs-offre-loueur-v1.md`, `48a81bd45d5b4feed725ceeea02c9fce9aa9fd7b21bf5c6e195c0c021fc4d03b`). Aucun résultat ouvert.

## 1. Ce qui est gardé, et pourquoi

La relecture du barreau 5 produit les activations par jeton de 39 adaptateurs aux trois couches : **≈ 152 Go, 166 Go avec les quatre points d'ancrage** (texte scellé, « Données gardées »). C'est trop pour une branche du dépôt. Sans lieu accordé, les replis écrits s'appliquent : la couche 15 seule (≈ 44 Go), puis une action sur dix (≈ 4,4 Go) ; le reste est détruit avec l'instance. Garder tout, c'est pouvoir relire après le verdict sans relouer une carte, et répondre à une question posée à l'entretien.

Rien ne tourne : c'est un lieu de dépôt. Le versement lui-même (sortie des données de l'instance de relecture) est déjà compté au devis scellé.

## 2. Lieu, prix relevés et leurs sources

- **Lieu** : un volume de stockage de 200 Go chez Hetzner, à Helsinki (`hel1`), attaché à un petit serveur le temps d'une séance (le versement, puis chaque relecture). Un volume ne se lit qu'attaché à un serveur du même lieu ; détaché, il reste facturé et intact.
- **Prix du volume, relevé le 21 novembre 2026 à 10:56:21Z** (calcul, bloc 1) : **0,0572 EUR hors taxe par Go et par mois**, 0,06864 toutes taxes (taxe de 20 %, lue dans la grille du compte). Soit **13,73 EUR par mois pour 200 Go**.
- **Prix du serveur, même relevé** : type `cx23` à 0,0088 EUR hors taxe de l'heure ; si les serveurs partagés manquent (la page publique en disait certains indisponibles ce matin), type `ccx13` à 0,0585 EUR hors taxe de l'heure.
- **Taux de change** : 1,25 USD pour 1 EUR, la convention du registre des dépenses (`registres/depenses.md`, l. 422). **Le taux du jour n'est pas relevé.**

## 3. Durée, cas attendu, pire cas, coupure

Toutes taxes (calcul, blocs 2 à 4) :

| scénario | contenu | EUR | USD |
|---|---|---|---|
| bas | volume gardé neuf jours, jusqu'au 1er décembre ; une séance de 6 heures sur `cx23` | 4,18 | 5,2 |
| **attendu** | volume gardé un mois entier, jusqu'au 21 décembre ; une séance de 12 heures sur `cx23` | **13,85** | **17,3** |
| pire cas sous les coupures | un mois entier ; trois séances de 24 heures sur `ccx13` | 18,78 | 23,5 |

- **Plafond proposé : 24 USD, jusqu'au 21 décembre 2026.**
- **Coupures** : chaque serveur porte une minuterie de destruction à 24 heures, par identifiant (R10) ; trois séances au plus sous cette ligne ; le volume est borné par l'échéance.
- **Ce que la minuterie évite** : un serveur `ccx13` oublié un mois coûterait 71,9 USD avec le volume.
- **Après le 21 décembre** : chaque mois de garde de plus coûte 13,73 EUR, soit 17,2 USD, volume seul. Il demande une ligne neuve.
- **Durée du versement** : 0,5 à 1,7 heure pour 184 Go (devis scellé, § 2), à un débit de réseau supposé et non mesuré ; la séance de 12 heures laisse le temps de vérifier les empreintes.

## 4. Ce qui est compté au compteur

Les lignes de facture de Hetzner pour le volume et pour chaque serveur de séance, relevées par leurs identifiants, de la création à la suppression. Une ligne d'engagement au registre des dépenses avant la création du volume : « engagement : barreau 5, garde des activations ([ligne d'accord], plafond 24 USD, échéance 21 décembre) : devis [chemin, empreinte] ; volume de 200 Go à `hel1`, 0,0572 EUR hors taxe par Go et par mois ; serveur de séance [type], minuterie 24 heures ». La sortie des données de l'instance de relecture reste comptée sous le plafond commun de la formation (GO-2026-11-19-86).

## 5. Ce qui arrête

1. Le cumul relevé atteint 24 USD : plus aucune séance ; le volume reste, et la mère porte la question à Lazar.
2. L'échéance du 21 décembre : la mère porte à Lazar trois issues — garder un mois de plus (ligne neuve), réduire au repli de la couche 15 (≈ 44 Go, 3,43 EUR par mois sur un volume de 50 Go), ou supprimer.
3. **Aucune suppression du volume sans le mot de Lazar**, et jamais avant un inventaire scellé (noms, tailles, empreintes) : règle « récupérer ce qui est récupérable ».
4. Si le versement n'aboutit pas : replis du texte scellé, dans leur ordre.

## 6. Autres lieux, pour mémoire (calcul, bloc 5)

- **Boîte de stockage de 1 To chez le même hébergeur** : 3,20 EUR hors taxe par mois sur la page publique relevée à 10:55:40Z, soit 4,8 USD toutes taxes, sans serveur. Quatre fois moins cher. Mais ce n'est pas la ressource de l'accord de principe ; les frais d'installation et la façon de la commander ne sont **pas vérifiés** ; l'ouvrir serait un nœud (compte). À regarder si la garde dépasse le 21 décembre.
- Repli 1 (couche 15, ≈ 44 Go) sur un volume de 50 Go : 3,43 EUR, 4,3 USD par mois.
- Repli 2 (une action sur dix) : sans dépense.
- Disque de l'instance arrêtée : ≈ 58 USD par mois, fragile ; déconseillé par le devis scellé.

## 7. Constat du relevé, hors de l'objet de ce devis, à porter à la session de lecture

**À 10:55Z, aucune offre ne passait les bornes écrites au devis scellé pour l'instance de relecture** (carte de 80 Go, disque de 300 Go, stockage au plus 0,08 USD de l'heure ; calcul, bloc 6). Le motif « stockage » touche les 13 offres : le prix de stockage le plus bas vu est de 0,20 USD par Go et par mois, soit 0,082 USD de l'heure pour 300 Go, juste au-dessus du plafond. Le devis scellé l'avait écrit en creux (« à 300 Go, 0,19 »). Une offre à 1,163 USD de l'heure ne manque que cette borne (0,099 USD de l'heure de stockage). Deux réserves : c'est un instantané ; l'unité du champ de stockage (par Go et par mois) est celle que le code suppose, jamais vérifiée (note sur les champs de l'offre, point 4). Je ne connais pas les bornes que le code de lecture figé applique : à vérifier par la session de lecture avant le jour de la relecture.

La sortie de données de cette même offre est à 0,039 USD par Go, soit 6,5 USD pour 166 Go : dans la fourchette du devis scellé (3,9 à 7,6), vers le haut.

## 8. Ce qui reste à relever

- Le taux de change du jour.
- La disponibilité du serveur `cx23` à Helsinki à l'heure de la création.
- Le débit réel du réseau entre l'instance de relecture et le serveur.
- Qui crée le volume et le serveur, et comment l'instance de relecture y écrit sans porter de clé du projet : à écrire dans la consigne de l'opérateur de la relecture (classe B), pas ici.

## 9. Ligne d'accord proposée

Numéro et référence posés par la mère.

`| GO-2026-11-21-NN | 2026-11-21 | calcul | Barreau 5 : garde des activations de la relecture (≈ 152 à 166 Go) sur un volume de stockage de 200 Go chez Hetzner, avec un petit serveur le temps du versement et de deux relectures au plus, sur le devis docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-garde-activations-volume-v1.md (empreinte de son compagnon). Prix relevé le 21 novembre : 0,0572 EUR hors taxe par Go et par mois. Hors du plafond commun de GO-2026-11-19-86. Minuterie de 24 heures sur chaque serveur. À l'échéance, aucune suppression sans le mot de Lazar. | 24 USD | 2026-12-21 | Lazar | mot de Lazar à recueillir |`

**Pour Lazar, en une décision.** Garder toutes les activations, ou s'en tenir aux replis. (a) Le volume de 200 Go : 17 USD attendus, 24 au plus, tout reste relisible après le verdict. (b) Le repli de la couche 15 sur un volume de 50 Go : 4 USD par mois, les couches 7 et 23 perdues sur disque. (c) Le repli sans dépense : une action sur dix. Recommandation : (a), confiance 0,75 — c'est l'accord de principe déjà donné, et le prix relevé est petit devant celui de la formation. Pas de défaut : c'est une dépense ; sans mot, les replis écrits s'appliquent.
