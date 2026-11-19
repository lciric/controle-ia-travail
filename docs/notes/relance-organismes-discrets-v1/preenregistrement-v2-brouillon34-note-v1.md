# Note du rédacteur — brouillon 34 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même que pour les brouillons 21 à 33. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon34.md`, `0b6413d9d75a838f17aabf46ff714a34c5b086f939e44d6a864326a7e1b247a3`, scellé. 2 210 lignes.
- **Point de départ** : le brouillon 33 (`dc3bc0236e9103454c988fa24997c698306ef78a2328587430bed553a5020c4a`), inchangé.
- **Heures (UTC)** : commencé le 2026-11-19T23:21:25Z ; texte scellé à 23:27:35Z.
- **Méthode** : 37 remplacements exacts, chacun sur une ancre trouvée une seule fois ; texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé, chaque étape conditionnant la suivante.
- **Pièces traitées** :
  - `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v10-bras-a-v1.md`, `538f09c0934dd63902596e48e35aaefa6f520b2f14993f91c7a76043b35172e1` ;
  - `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v10.md`, `a386c070071e6877a2e39f6d29bbfa0e0661865545cf91ef9201ca3b337f5916` ;
  - `docs/notes/relance-organismes-discrets-v1/verification-brouillon33-bras-a-v1.md`, `3cdd53ca1d5287a5680679555687f0343e870981f9238258535c7af0c0eaed17`.
- **Aucune fiche n'est ajoutée** : aucun point ne fixe l'issue d'une hypothèse (partie 6, réserve 1).

## 1. Points traités

| point demandé | ce que le texte écrit | où |
|---|---|---|
| 1. Vérification du code, C-1 | une course n'a qu'une première livraison ; une ouverture de lecture est scellée dans le dossier des arrêts avant toute lecture ; ensuite toute autre pièce exige une ligne de GO, et seul le rejeu de la même pièce reste permis ; une configuration de rang supérieur à 1 inscrit un registre figé | conventions ; 6.9 ; 8.4 |
| 1, suite. D'où vient le registre figé pour une première livraison | sa configuration n'en inscrit aucun. La seule ligne lue avant elle est celle de l'écart à R9 : sa pièce est l'état du registre au commit où cette ligne est inscrite, copié par la session qui lance le tirage de la table, et son empreinte est inscrite dans la configuration scellée du lanceur de l'étape de discrétion | 6.2 ; 13.2 |
| 2. Phrase d'accord de l'écart à R9 | la cellule d'objet de la ligne de GO est exactement « écart à R9 accordé pour la table des identifiants opaques », sans égard à la casse ni aux accents, ponctuation finale admise. La même règle vaut pour une livraison refaite : « livraison refaite du côté habilité accordée pour le bras A » | 13.2 ; 8.4 |
| 3. A.1 | la pièce arrêtée par une garde ordinaire se relit par la règle d'octroi, sous une configuration neuve et une ligne de GO. L'acte de reprise porte alors deux fois la même empreinte, ce qui n'est admis que si la ligne cite un constat de pièce donnée | 6.9 ; 8.4 |
| 3. A.3 | recomposer reste permis après un arrêt à l'étape (n), sur le fichier de l'étape (m) ; les grandeurs de l'étape (n) restent « non rapportées » | 6.9 ; 8.4 |
| 3. A.4 | un constat cité vient d'une première livraison : la configuration qu'il nomme n'inscrit aucun registre figé | 6.9 ; 8.4 |
| 3. A.5 | le constat d'erreur de rangement porte les deux empreintes ; « la même pièce » est celle que scelle le compagnon, sinon celle des octets donnés | conventions ; 6.9 ; 8.4 |
| 3. A.6 | la valeur « en attente » est écrite : garde ordinaire sans issue ; la pièce arrêtée est consignée par un constat ; la valeur ne survit pas au scellement | conventions ; 6.9 ; 8.4 |
| 4. Vérification du code, M-2 | un contrôle ne vaut que pour le rejeu qui le suit ; une trace de rejeu scellée le lie à ce rejeu ; un contrôle est exigé pour le rejeu d'une première livraison aussi | conventions ; 6.9 ; 8.4 |
| 5. Nom du programme du constat | `scripts/constat_de_lancement_discretion_bras_a_v3.py`, `6ee84152920d0dffe46f0a289279a961648946812ea53e0a86fd28ad7368b17c` | en-tête ; conventions ; 13.2 |
| 6. Brouillon 33, M-1 | il n'était pas porté. Le programme consigne l'erreur de rangement dès le refus ; une pièce d'une autre empreinte redonnée ensuite passe par la règle d'octroi | conventions ; 6.9 ; 8.4 |

**En plus**, sans demande expresse, parce qu'ils tiennent aux mêmes passages :
- les autres mineurs de la vérification du code : M-3 (rien à changer), M-4 (limite écrite : une autre course, et ce que montre le registre), M-5 (porté avec A.6) ;
- les points B.3, B.6 à B.8 et B.10 à B.12 du relevé, écrits comme le code les porte ;
- le mineur M-2 de la vérification du brouillon 33 : le registre des GO est relu.

**Fichiers scellés neufs que le texte nomme** :
- `ouverture-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json`, dossier des arrêts, quatre champs ;
- `erreur-de-rangement-bras-a-<seize signes>.json`, dossier des arrêts, cinq champs ;
- `piece-en-attente-d-un-choix-bras-a-<seize signes>.json`, dossier des arrêts, quatre champs ;
- `rejeu-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json`, dossier de la livraison, quatre champs.

## 2. Contrôles par programme

| contrôle | résultat |
|---|---|
| sections 12, 7.1 à 7.8 et 10 | **identiques** au brouillon 33 |
| hypothèse au seuil ; 6.3 à 6.8 ; 6.10 à 6.12 ; 8.1 à 8.3 ; 8.6 ; sections 9 et 11 | identiques |
| titres | 53, identiques hors le titre de niveau 1 |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 20 ; `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| citations entre guillemets du brouillon 33 | 1 236, aucune absente |
| citations du brouillon 20 | 935 ; les deux mêmes absentes qu'aux brouillons 32 et 33 |
| marque des cases | 6 lignes, toutes en 13.1, les mêmes cases |
| table d'en-tête | 174 empreintes recalculées, toutes égales ; 14 lignes cloisonnées sautées, **aucune empreinte prise sur elles** |
| validateur `problemes()` | les deux problèmes attendus |
| nom du programme du constat | plus aucune version 1 ni 2 dans le texte actif |

## 3. Registre relu

Registre des GO de la branche principale distante, au commit `a42ac1f5d` : neuf lignes de plus depuis ma dernière lecture, GO-2026-11-19-84 à -92. Aucune ne touche le bras A. Le mot de Lazar du 19 novembre vers 22:00Z n'y est pas encore inscrit. La consigne de cloisonnement sur sa ligne n'est donc pas rompue.

## 4. Ce qui sépare encore le texte du scellement

Les listes des notes des brouillons 32 (partie 5) et 33 (partie 4) valent toujours. S'y ajoutent :
1. **Session principale** : dire laquelle des cellules d'une ligne du registre est celle de l'objet ; inscrire les lignes de GO avec les deux phrases d'accord à la lettre.
2. **Lanceur de l'étape de discrétion** (côté habilité) : sa configuration scellée inscrit l'empreinte et le commit de l'état figé du registre où se lit la ligne de l'écart à R9.
3. **Session de relance** : le code en version 11 (partie 5), contre-lu ; les pièces des demandes à mettre à jour sur ces deux points, et sur le nom du programme du constat, que la demande 29 de la pièce du lecteur donne encore en version 2.

## 5. Ce que le code de la version 11 doit porter

1. **Ouverture de lecture** : avant toute lecture d'une première livraison, et après les gardes ordinaires qui reconnaissent la pièce, écrire sans reste et sceller `ouverture-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json` dans le dossier des arrêts, aux quatre champs (`evenement`, `sha256_de_la_piece`, `sha256_de_la_configuration`, `sha256_du_constat_de_lancement`).
2. **Une seule première livraison** : dès qu'une ouverture existe dans le dossier des arrêts, toute pièce d'une autre empreinte exige une ligne de GO et un acte de reprise, sous quelque configuration et à quelque rang que ce soit. La même pièce, sous la même configuration, sans résultat écrit, est un rejeu.
3. **Rang supérieur à 1** : une configuration rangée dans `livraison-<rang>`, rang supérieur à 1, sans registre figé, arrête le programme.
4. **Phrases d'accord** : la cellule d'objet de la ligne est comparée entière à la phrase, sans casse ni accents, ponctuation finale admise. Une phrase seulement contenue dans la cellule n'ouvre rien. Vaut pour les deux phrases.
5. **Contrôle et rejeu** :
   - un contrôle est exigé pour tout rejeu, y compris celui d'une première livraison, que l'ouverture signale ;
   - au départ du rejeu, écrire et sceller la trace `rejeu-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json` dans le dossier de la livraison, aux quatre champs ;
   - un contrôle que porte déjà une trace n'ouvre aucun autre rejeu ;
   - « le plus récent » est le plus grand `date_utc` ; « après le constat d'origine » est strict. C'est déjà ce que fait le code.
6. **Constat d'erreur de rangement** : un cinquième champ, `sha256_que_scelle_le_compagnon`, `null` si le compagnon est absent ou illisible. « La même pièce » est celle de ce champ quand il est rempli, sinon celle des octets donnés. Une pièce d'une autre empreinte redonnée après ce constat est refusée sans ligne de GO.
7. **Constat de pièce en attente d'un choix** : sous la valeur « en attente », quand le motif est rencontré, écrire et sceller `piece-en-attente-d-un-choix-bras-a-<seize signes>.json`, aux quatre champs, avant l'ouverture et avant l'acte.
8. **Pièce arrêtée relue (A.1)** : sous une configuration neuve et une ligne de GO qui cite son constat de pièce donnée, la même pièce est lue. L'acte porte alors deux fois la même empreinte. Cela reste refusé quand la ligne cite un fichier d'arrêt.
9. **Constat cité (A.4)** : il doit venir d'une première livraison, c'est-à-dire d'une configuration sans registre figé.
10. **Recomposer (A.3)** : permis après un arrêt à l'étape (n), sur le fichier de l'étape (m) et ses constats ; les grandeurs de l'étape (n) restent « non rapportées » ; le fichier des scores par unité n'est pas rouvert.
11. **Rapport** : compter l'ouverture et les trois sortes de constats.
12. **Essais (R5)**, cas sain et artefact, pour chaque point. Les deux lignes neuves de 8.4 les énumèrent : « une seule première livraison par course » et « phrases d'accord des lignes de GO ».

## 6. Réserves

1. **Aucun point ne m'a paru toucher une règle de jugement.** Le défaut C-1 et ses suites ferment des voies de lecture ; ils ne disent l'issue d'aucun cas. Le vérificateur du code tenait déjà les six points de la partie A du relevé pour des précisions.
2. **Ce que j'ai conçu au-delà des mots demandés**, à faire voir :
   - l'ouverture de lecture porte un quatrième champ, l'empreinte du constat de lancement, par symétrie avec l'acte de reprise ;
   - la trace de rejeu est un fichier neuf. Le vérificateur demandait qu'un rejeu suivant ne puisse pas reprendre un contrôle ; sans trace scellée au départ du rejeu, rien ne le montre après une seconde panne ;
   - le constat de pièce en attente d'un choix est un fichier neuf, sur le modèle du constat de provenance. Sa valeur fixe dit que le motif est présent dans la pièce, sans dire où ;
   - la phrase d'accord d'une livraison refaite est reprise du code, que j'ai lu par recherche pour ces deux chaînes.
3. **La valeur « en attente » ne survit pas au scellement.** Je l'ai écrit, parce que le texte ne se scelle qu'une fois le point 20 tranché. Elle ne sert donc qu'au code éprouvé avant. Si le coordinateur veut qu'une course puisse partir sous elle, c'est un autre texte, et la question de ce qui suit devient une règle à poser.
4. **Le registre figé d'une première livraison** : je l'ai rattaché à la porte de l'écart à R9, seul endroit où une ligne se lit avant une première livraison. Cela demande une inscription de plus au lanceur du côté habilité, qui n'est pas encore écrit ni demandé dans les pièces.
5. **Les pièces des demandes en version 8 sont en retard sur ce brouillon** : nom du programme du constat, cellule d'objet, registre figé du lanceur.
6. **Limite écrite, non fermée** : une autre course, avec un autre dossier des arrêts, ne voit pas l'ouverture de la première. Ce qui tient est le registre, où une seconde configuration de rang 1 se voit.
7. **Je n'ai pas relu le texte en entier** : seulement les passages touchés (en-tête, conventions, 6.2 pour une phrase, 6.9, lignes de 8.4, 13.2, 14.45, « Contre-lecture »).

## 7. Fichiers ouverts

- Les trois pièces nommées en tête, en entier.
- Du code de la relance, qui ne porte aucun interne de moniteur, par recherche seulement : `src/controle_ia/organismes_discrets/graines_bras_a_v10.py` (les deux phrases d'accord) ; `analyse_bras_a_v10.py` (noms, champs et natures des constats de pièce donnée) ; `configuration_bras_a_v10.py` (la valeur « en attente »).
- `scripts/constat_de_lancement_discretion_bras_a_v3.py` : son empreinte seulement.
- Le brouillon 33, par passages et par programme ; le brouillon 20 et le fichier des fiches du brouillon 23, par programme.
- Le registre des GO de la branche principale distante, par `git show` après un `git fetch`, seul appel réseau.
- **Non ouverts** : aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé. Aucun appel de modèle, aucun sous-agent, aucune dépense. Rien de committé ; `registres/` et `.claude/` non touchés.
