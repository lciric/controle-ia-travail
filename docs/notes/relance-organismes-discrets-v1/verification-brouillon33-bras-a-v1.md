# Vérification du brouillon 33 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 32. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon33.md`, `dc3bc0236e91…`. Note : `1f2dc907ee40…`. Les deux compagnons sont vérifiés.
- **Méthode** :
  - comparaison des brouillons 32 et 33 phrase par phrase, faite par programme ;
  - lecture des blocs touchés : conventions, lignes 212 à 214 ; 6.9, lignes 757 à 781 ; 8.4, lignes 1024 à 1028 ; marques des points 19 et 20 ; 13.1, lignes 1322 et 1335.
  - Aucun code ouvert. Des pièces de demandes, je n'ai pris que l'empreinte, plus une recherche de l'empreinte du brouillon dans la pièce v8 du lecteur.

## Verdict : **engageable**

- Les trois points de ma vérification du brouillon 32 sont tenus : C-1, M-1, M-2. M-3 est fait.
- **Aucune règle de jugement ne change.** Les trois choix de la réserve 1 sont des procédures (partie 2).
- La consigne de cloisonnement neuve est juste.
- L'intégrité tient.
- Il reste deux remarques mineures, qui ne retiennent pas le texte.

## 1. Les points de la vérification du brouillon 32

| point | état | endroit |
|---|---|---|
| **C-1** : remplacement d'une première livraison sans conditions | **tenu**, par les voies (i) et (ii) | La clé de provenance est obligatoire : texte non vide, jamais `null`, configuration refusée sinon, rien de scellé sans elle. Le point (18) de la case du module devient bloquant (conventions, ligne 214 ; 13.1, ligne 1335). Tout remplacement de la sortie de la lecture commune passe par la règle d'octroi, hors l'erreur de rangement (6.9, ligne 781). En 8.4, ligne 1028 : cas sains et artefacts (configuration sans clé ; garde sans constat ; constat qui porte un champ de la pièce ; sortie d'une autre empreinte lue sans ligne ni acte sous une première livraison). La branche « clé `null` » n'apparaît plus que dans une phrase qui la dit retirée (ligne 781). |
| **M-1** : clause du point 19 | **tenu** | 6.9, ligne 757 ; marque du point 19 ; case « nœuds » : Lazar est informé de la réponse, confirmée sur le code par le lecteur habilité, avant le retrait de la rédaction non retenue. |
| **M-2** : rédaction (b) du point 20 | **tenu** | Retirée de 6.9 (ligne 758), de la ligne de 8.4 (ligne 1024 : deux rédactions, (a) et (c), avec leurs cas sains et artefacts) et de la marque du point 20. Le nom de règle d'arrêt « moniteur appris non ajustable » et « les deux cas tenus pour une anomalie » disparaissent avec elle. Il ne reste qu'un cas d'anomalie, l'intervalle impossible sous la rédaction (c). |
| **M-3** : pièces des demandes | **fait** | Version 8 citée. Les versions 6 et 7 sont gardées à la table d'en-tête, marquées « non sortie ». La pièce du lecteur en v8 cite le brouillon 33 par son empreinte entière (vérifié par recherche), sans boucle. |

## 2. Les trois points de la réserve 1

**(1) Le constat de provenance neuf : une procédure.**
- C'est un fichier scellé, `provenance-non-etablie-bras-a-<seize signes>.json`, dans le dossier des arrêts.
- Il a quatre champs, `evenement`, `constat`, `sha256_de_la_piece` et `sha256_de_la_configuration`. Le constat est pris dans une liste fermée de cinq natures. Il ne porte ni nombre ni champ de la pièce.
- Il **ne dit aucun arrêt de la lecture et n'emporte aucune issue**. Il fixe seulement quelle pièce a été livrée, pour qu'on ne puisse pas la remplacer hors de la règle d'octroi.
- Il est écrit sans reste et jamais réécrit.
- Le cloisonnement est respecté : un nom de nature et deux empreintes, rien de la pièce.
- R5 est tenu : cas sain et artefacts en 8.4.

**(2) L'erreur de rangement lue strictement : une procédure.**
- Seuls un nom faux ou un compagnon manquant se corrigent sans la règle d'octroi. Ces défauts jouent avant la garde de provenance, et on redonne la même pièce, octet pour octet.
- C'est plus prudent que nécessaire. Une pièce étrangère donnée par erreur sous le bon nom coûte une ligne de GO. Cela ne fixe l'issue de rien.
- Une limite reste : voir M-1.

**(3) Une ligne de GO exigée pour remplacer une pièce de première livraison : une procédure.**
- La règle d'octroi accordée par Lazar s'applique ici à un cas voisin de celui pour lequel elle est écrite.
  - Le constat de provenance tient la place du fichier d'arrêt, et la pièce arrêtée celle de la livraison refusée.
  - Quand le module ne change pas, les conditions (3) et (4) se lisent « même module, même empreinte », ce que le lecteur habilité écrit.
- Elle ne demande pas de mot neuf de Lazar, n'ouvre aucune dépense et ne prononce rien.
- Tant que rien ne remplace la pièce, la discrétion n'est pas lue, et ce que cela vaut reste un nœud de Lazar, comme au brouillon 32.
- Ce n'est donc pas une règle de jugement. Le texte ferme la voie que j'avais signalée (C-1), sans fixer une issue.

**La consigne de cloisonnement neuve** (13.1, case du module, ligne 1335) :
- jusqu'à sa dernière livraison, rien de ce que décident ses réponses aux points (9) et (10) n'est dit au développeur ;
- la ligne de GO du mot ne recopie pas cette suite et y renvoie par chemin et empreinte ;
- s'il faut corriger le module, seule la commande lui est transmise ;
- les deux réponses sont confirmées sur le code par le lecteur habilité.

C'est juste. Cela empêche qu'une réponse de fait soit orientée par ce qu'elle déclenche, ce qui est le sens de R4. Ce n'est pas une règle de jugement. La ligne de GO peut toujours nommer en clair ce qu'elle accorde pour les autres points.

## 3. Mineurs

- **M-1. L'erreur de rangement ne garde pas l'empreinte de la pièce mal rangée.**
  - « On redonne la même pièce, octet pour octet » suppose qu'on connaisse l'empreinte de la première, refusée pour son nom ou son compagnon. Seule l'empreinte de la pièce redonnée est consignée.
  - Il faudrait consigner au manifeste l'empreinte de la pièce mal rangée dès le refus, et ajouter en 8.4 un artefact : une pièce différente redonnée après un défaut de nom est refusée et passe par la règle d'octroi.
  - Le risque est faible depuis que la clé de provenance est obligatoire : une pièce d'un autre module n'a pas la bonne provenance. C'est néanmoins une vérification que le texte promet et ne permet pas de faire.
- **M-2. Registre non relu** (réserve 4). Si la ligne de GO du mot est déjà inscrite et recopie la suite des points 19 et 20, la consigne de cloisonnement est déjà rompue. La demande 27 le demande. Il faudra relire le registre au prochain brouillon.

## 4. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillon 32 intact ; brouillon 33 et note | compagnons vérifiés (`a053eeb8…`, `dc3bc023…`, `1f2dc907…`) |
| 7.1 à 7.8 ; section 10 ; 6.2 | **aucune ligne changée** |
| section 12 | 2 lignes changées sur 172 : les marques des points 19 et 20. Les fiches 9 à 12 restent mot pour mot (6, 7, 7 et 7 puces) ; lignes d'origine du point 17 intactes ; points 1 à 21 dans l'ordre. |
| hypothèse au seuil ; 6.1 ; 6.3 à 6.8 ; 6.10 à 6.12 ; 8.1 à 8.3 ; 8.6 ; sections 9 et 11 | identiques au brouillon 32 |
| citations du brouillon 32 | 1 229, dont une absente : « mal formé », guillemets retirés dans une phrase récrite ; le mot reste. Ce n'est pas une citation transmise. |
| citations du brouillon 20 | 935, dont les deux mêmes absentes qu'au brouillon 32, déjà justifiées |
| consignes figées (3.2 et 3.3) | égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| titres | 53 ; seul le titre de niveau 1 change |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | six lignes, toutes en 13.1, les mêmes cases qu'au brouillon 32 |
| table d'en-tête, lignes neuves | empreintes égales : brouillon 32 ; sa note ; ma vérification ; demandes v7, les deux ; vérification de cloisonnement v7 ; demande du développeur v8 (`ba81227f…`). **Aucune empreinte de fichier cloisonné prise.** |

## 5. Ce qui reste avant le scellement

La liste de ma vérification du brouillon 32 (partie 8) vaut toujours, avec trois changements :
- la clé de `piece_source` (demande 13 de la pièce du développeur) est maintenant **bloquante** ;
- les deux réponses de fait du développeur sont **confirmées sur le code par le lecteur habilité**, et Lazar est informé de celle du point 19 avant le retrait ;
- la ligne de GO du mot de Lazar ne recopie pas la suite des points 19 et 20.

S'y ajoutent :
- la relecture de cloisonnement des demandes v8 avant leur sortie ;
- M-1 ;
- la relecture du registre (M-2).

## 6. Fichiers ouverts

- Le brouillon 33 : par différence ; les lignes citées en tête.
- Les brouillons 20 et 32, par programme.
- La note du brouillon 33.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Pour leur seule empreinte : les pièces de demandes v7 et v8, la vérification de cloisonnement v7, la note du brouillon 32.
- Rien d'autre : aucun code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.
