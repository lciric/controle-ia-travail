# Vérification courte de la pièce diffusable de la mémoire des problèmes, version 3 — version 1

Vérificateur neuf (le même qui a vérifié la pièce de la version 2 : `registres/memoire-problemes-v2-commune-diffusable-verification-v1.md`, `7dadc1f013993b60d4f16341bf563708fcf3f82cc1ec53a6eedc2bb504f9ab72`) ; ni rédacteur de la version 3, ni auteur du programme. Aucune dépense, aucun réseau, aucun fichier existant modifié, aucun commit.

**Conclusion : diffusable telle quelle.**

## 0. Empreintes

| pièce | empreinte attendue | constatée | compagnon |
|---|---|---|---|
| `registres/memoire-problemes-v3.md` | `5a0693e1992d94239edc889a5abf0f33fad1e8cfa5733c1811a5325b094de3ea` | identique | identique |
| `registres/memoire-problemes-v3-commune-diffusable.md` | `44b94ec2a00b6b26a1b99616ae4ada2292be56dfa6e6a4e6687cdd2cbe3a5e3e` | identique | identique |
| `scripts/memoire_problemes_extraire_commune_v2.py` | `9f3066249423fd4f42c24f76721dd81d55890facf9629c13248ce11e65105671` | identique | identique |
| `registres/memoire-problemes-v3-correspondance-empreintes.md` | (non donnée) | `f3f758a4e4ecad418c99e59dc493c048eea5ab6fc680f1e4fcdf23996e5a841a` | identique ; ses trois empreintes sont celles du tableau ci-dessus |

## 1. Pièce relue en entier (310 lignes)

### Les six fuites bloquantes de la vérification précédente

| point | ligne(s) en version 3 | état |
|---|---|---|
| (a) empreinte de la source dans l'en-tête | 3 | **fermé** : « la correspondance entre les deux empreintes est consignée par la mère, hors de cette pièce » ; aucune empreinte dans la pièce. Le fichier de correspondance n'est pas nommé par la pièce. |
| (b) script qui coupait des chaînes pour passer la garde de calcul | 102 (M-006) | **fermé** : « un script pour passer outre la garde de calcul ». |
| (c) « jeu », durées exactes, addenda | 32 (M-001), 235 (M-017) | **fermé** : « calcul long… tué bien avant sa fin prévue, à relancer sous un texte neuf » ; « deux calculs ». Plus aucun « jeu » : lignes 101 et 222 disent « avant de la jouer », « avant de jouer la commande ». « addendum » remplacé par « texte d'écart scellé » (189, 193, 256). |
| (d) reprise d'une course d'une autre session, « étape non mesurée » | 285-286 (M-021) | **fermé** : « l'outil avait de nouveau vidé son dossier, rien à reprendre » ; « un outil d'orchestration qui conserve ses produits intermédiaires ». |
| (e) citation d'un texte scellé, « invalide une lecture » | 307 (M-040) | **fermé** : « un texte scellé qui fait d'un essai du dépôt en échec une cause d'arrêt ». |
| (f) règle 4 contredite par la pièce | 10 | **fermé** : « rien n'y dit à quoi travaille une autre session, ni où en est son travail ». |

### Corrections conseillées de la vérification précédente

- M-017 (ligne 236) : issue technique ramenée à « un autre participant déclaré échoue, la tentative est consommée ». Plus d'étape nommée. Fait.
- M-006 (ligne 101) : « sur la décision de Lazar, qui retient l'ajout d'une règle de permission bornée à cette seule ligne ». Vérifié sur les deux lignes sources du registre des décisions, ouvertes pour cela seul : le mot direct de Lazar porte « Tu ajoutes une règle de permission pour cette ligne de création : go », et la règle écrite est bornée à cette ligne. Fidèle. Rien du chantier de ces lignes ne passe dans la pièce.
- M-010 (ligne 154) : « budget de dépense », « plafond de dépense quotidien ». Fait.
- « session hôte » remplacée par « session fille » (lignes 86, 138). Fait.
- M-001 (ligne 34) : « observé : non rapporté dans cette pièce », sans classe d'attente. Fait.
- Lignes « vu » : « N renvois aux registres de la session mère ». Fait.
- Règles 2 et 3 réécrites comme proposé (« ne fait foi sur rien », définition de « écrit avant », « heures d'horloge », « aucun mécanisme d'expérience », « aucun montant »). Fait.
- M-011 : signal élargi à « une heure que tu n'as lue ni dans la sortie de `date -u`… ni dans la pièce citée ». Fait.

### Glossaire neuf (lignes 14 à 21) : aucune fuite

- **feu** : écrit de la mère qui autorise un opérateur, geste par geste. Générique.
- **amorce** : script de démarrage de la machine louée (clonage, installation, essais, gardes). Générique, sans mécanisme d'expérience.
- **ligne d'accord** : ligne du registre des accords, avec plafond et échéance. Nomme le registre en clair, sans chemin ni numéro ; c'est déjà dans les consignes permanentes de toute session.
- **ligne de forme** : générique.
- **crochet** : décrit ce que la garde bloque (lancement payant sans ligne d'accord, arrêt par motif). C'est ce que disent déjà les consignes permanentes. Rien sur la façon de la passer.
- **mandataire** : générique.
- **loueur** : sans nom de fournisseur.

### Autres fuites ou doutes

Je n'ai trouvé aucune fuite nouvelle : aucun nom de fournisseur, de modèle, de loueur ni de chantier ; aucun résultat, aucun seuil chiffré, aucun score, aucun contenu de verdict, aucun montant, aucun fragment de consigne. Pas non plus de renvoi R-, de date, d'heure d'horloge, ni d'identifiant de machine, de session, de commit ou d'empreinte.

Restent deux points faibles, déjà classés « garder » à la vérification précédente, qui n'empêchent pas la diffusion :
- le trou de numérotation entre M-021 et M-039 dit que d'autres entrées existent (leur existence, pas leur contenu) ;
- M-014 dit que la vérification de l'arbre ne parcourt que six dossiers, ce que le code montre aussi.

## 2. Programme d'extraction, version 2 (éprouvé dans le bloc-notes, aucun fichier du dépôt touché)

- **`--help`** : répond (usage, description, trois chemins, option d'auto-essai), code 0.
- **Auto-essai** : passe, code 0 (« cas sain accepté ; 20 artefacts refusés ; transformation conforme ; sortie existante jamais écrasée ; garde qui refuse : aucun fichier créé ni vidé ») ; il travaille dans un dossier temporaire du système, hors du dépôt.
- **Ordre des gestes, d'après le code** : la sortie et la correspondance sont refusées d'emblée si elles existent (`os.path.lexists`, code 2). La pièce est fabriquée et jugée en mémoire avant toute ouverture. Les fichiers ne sont ouverts qu'ensuite, en création exclusive (`"xb"`).
- **Mes épreuves**, dans `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/v3/refus/` :

| épreuve | attendu | observé |
|---|---|---|
| sortie existante (14 octets) | code 2, sortie intacte, correspondance non créée | conforme |
| correspondance existante, sortie absente | code 2, sortie non créée, correspondance intacte | conforme |
| garde qui refuse (copie de la version 3 dans le bloc-notes, « un jeu long » injecté dans la partition commune) | code 1, aucun fichier créé | conforme : « ARRET : la garde refuse la pièce, rien n'est écrit : ligne 29 : \b[jJ]eux?\b » ; aucun fichier |
| garde qui refuse, sortie préexistante | sortie ni vidée ni touchée | conforme : code 2, sortie intacte |
| lien symbolique cassé comme sortie | refus, cible non créée | conforme : code 2, cible non créée |
| cas sain | pièce identique | conforme : code 0 |

- **Rejeu** sur `registres/memoire-problemes-v3.md` vers le bloc-notes : la pièce est **identique à l'octet** à `registres/memoire-problemes-v3-commune-diffusable.md` (`cmp` sans différence, même empreinte `44b94ec2…5e3e`). La correspondance rejouée porte les mêmes empreintes de source, de pièce et de programme. Seuls diffèrent le chemin de sortie et l'heure d'extraction, ce qui est attendu.

## 3. Refus d'outil

Aucun.
