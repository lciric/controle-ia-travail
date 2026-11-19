# Note de changements — brouillon 29 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 à 28.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon29.md`, `4446b21e03918251ae7f00c383d4704bc4ee92cae212a4a23fd344d857e0ee3f` (2 100 lignes). Les brouillons 20 à 28 ne sont pas modifiés.
- **Fiches pour Lazar : aucun fichier neuf.** Aucun des points portés ne touche une règle de jugement ; il n'y a donc pas de `decisions-bras-a-brouillon29-v1.md`. Celles du brouillon 23 restent en vigueur (`f20abfed…`).
- **Sources**, lues en entier : le relevé des défauts trouvés en écrivant la version 8 du code (`bbdd75e4437a7ad2bb6b191204d824054b881b73e760e32e3da7e89d5bd46c6c`) ; la vérification du brouillon 28 (`ff63a0f73d50958c96698a76c0cfbd6caeb56961199f37c19b9a498f9e6f6c31`, « engageable », quatre remarques mineures).
- **Méthode** : copie du brouillon 28 par `cp`, puis 35 remplacements exacts, chacun vérifié unique par programme.
- **Registre des accords** : relu sur la branche principale distante au commit `f637e163` ; aucune ligne de plus.
- **Heures (UTC, `date -u`)** : début 18:53:33Z le 2026-11-19 ; brouillon scellé à 18:56:20Z.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucun module du code ouvert (de la note du code de la version 8, les seules lignes qui nomment des fichiers, des champs et le rejeu) ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; aucun sous-agent.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| section 12 ; « Critères de lecture gelés » en entier ; section 10 | identiques, caractère pour caractère, au brouillon 28 |
| titres ; consignes figées | inchangés ; `98a9bd34…` et `ecf590ea…` recalculées |
| citations à la lettre | brouillon 20 : 935 sur 935 ; brouillon 28 : 1 176 sur 1 176 |
| table d'en-tête, sans les fichiers cloisonnés | 156 lignes à empreinte : 142 recalculées et égales, 0 différente, 14 sautées et non ouvertes |
| renvois à la première version des demandes | aucun ne reste ; les deux pièces envoyées sont citées et ont leur ligne à empreinte |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | les deux problèmes attendus |
| l'exemple du relevé, recalculé | `0.0033333333333333333343` dépasse 0,05 ÷ 15 en fractions exactes, comme sa formule 7 ÷ 2 001 ; quinze fois son nombre à virgule ne dépasse pas 0,05 |

## 1. Les cinq points de la partie A : précision, ou fiche ?

**Aucun ne demande une fiche.** Chacun est une précision de forme, de fichier ou de procédure.

| point | avis | ce que le texte dit maintenant | où |
|---|---|---|---|
| 1. arithmétique des états | **la lettre de la règle rendue exacte, non une règle neuve** | toute comparaison qui dit un état se fait en fractions exactes, sur l'écriture décimale de la pièce : valeur de la famille contre les niveaux de Holm, valeur p basse contre 0,05, borne haute contre 0,60 ; les valeurs ajustées rapportées restent des nombres à virgule, et ne disent aucun état | 6.9 |
| 2. rejeu « sous la même configuration » | précision | cinquième champ de l'acte de reprise, `sha256_de_la_configuration` ; pour une première livraison, c'est la session qui lance qui consigne le rejeu | conventions ; 6.9 ; 8.4 |
| 3. résultat de l'étape (n) | précision | un fichier scellé, `grandeurs-de-l-etape-n-bras-a.json`, à cinq champs ; dès qu'il existe, l'étape (n) ne se rejoue pas | conventions ; 6.9 ; 8.4 |
| 4. constat de lancement | précision | (a) ligne de GO en entrée, septième champ `ligne_de_go`, confronté par l'analyse ; (b) constat malsain : aucun fichier, cause affichée, sortie en échec ; (c) et (d) le constat écrit à la main et l'absence au manifeste sont des gardes de procédure, tenues par la session qui lance ; (e) le registre courant porte tout l'état figé, sinon arrêt sans constat et configuration neuve ; (f) formes de « inscrite » et de « révocation », à confirmer | conventions ; 8.4 |
| 5. portée du refus des valeurs fictives | précision | la configuration, et les seules lignes sur lesquelles le constat s'appuie ; une ligne fictive ailleurs au registre n'arrête rien | conventions ; 8.4 |

**Pourquoi le point 1 n'est pas une règle neuve.** Les règles de 6.9 comparent des nombres à des seuils : « au plus le niveau », « dépasse 0,05 », « sous 0,60 ». Les fractions sont ces comparaisons faites sans erreur ; le nombre à virgule en est une approche. Au brouillon 26, le texte affirmait que, sous les conditions (α) et (β), l'état de la valeur rendue est celui de sa formule : c'est vrai en fractions, et l'exemple du relevé montre que ce peut être faux en nombres à virgule. Le code a donc rendu vraie une phrase du texte. Aucun seuil, aucune statistique, aucune issue ne change.

**Un écart au code, sur le point 1.** Le code exige que la valeur de la famille « s'écrive comme » la valeur p haute. Le texte dit : égales comme deux fractions, non comme deux écritures ; 0,050 et 0,05 sont égales.

## 2. La partie B

Je l'approuve, à un point près.

| point | avis | où |
|---|---|---|
| 6. `piece_source` | **approuvé pour la chaîne, non pour la cause de refus.** La chaîne `cle_du_module_dans_piece_source` est nommée. Mais une sortie qui ne vient pas du module inscrit n'est pas « une livraison refusée pour sa forme » : ce n'est pas la pièce attendue, rien n'en est lu. Je la range dans « ce qui n'est pas un refus d'une livraison » : garde ordinaire, sans événement d'arrêt ni issue du point 21 ; nœud de Lazar si la bonne pièce n'existe pas. La liste fermée des refus ne s'allonge pas | conventions ; 6.9 |
| 7. `dossier_des_arrets` | approuvé : relatif au dossier de la configuration ; il existe ; ni un dossier de livraison, ni sous l'un, ni au-dessus | conventions |
| 8. dossier d'une livraison | approuvé : `livraison-<rang>`, rang entier sans zéro devant ; un dossier de ce nom sans configuration arrête | conventions |
| 9. ordre d'écriture de l'étape (m) | approuvé : les constats d'abord, le fichier ensuite | 6.9 |
| 10. deux champs des constats | noms confirmés | — |
| 11. aires de l'agrégateur | approuvé : valeur par valeur, structure gardée | 6.9 |
| 12. `effectifs`, `exclues` | approuvé : tout ou rien ; liste ou table vide reconnue ; `true` et `false` ne sont pas des entiers | 6.9 |
| 13. chemins à élaguer | rien au texte : demande 20 de la pièce du développeur | — |

## 3. Ce qui restait au brouillon 28

- **Renvois aux demandes** : les trois renvois à la première version sont remplacés par les deux pièces envoyées, `demandes-au-developpeur-habilite-bras-a-v4.md` (`837181f2…`) et `demandes-au-lecteur-habilite-et-a-lazar-bras-a-v4.md` (`5598cbcc…`), qui ont chacune leur ligne à la table d'en-tête.
- **Refus de `GO-0000-00-00-00` et de l'empreinte de soixante-quatre zéros** : aux conventions et à la ligne « constat de lancement » de 8.4, avec leur portée.
- **Les quatre mineurs de la vérification du brouillon 28** : M-1, l'incise « la somme et le maximum seulement ; l'aire de la moyenne reste sous la table des formes » ; M-2, valeur par valeur ; M-3, les booléens ; M-4, les lignes à empreinte.

## 4. Ce que le code de la version 9 doit porter

1. **États en fractions exactes** : garder. **Changer** : l'égalité de la valeur de la famille et de la valeur p haute se juge sur les fractions, non sur les écritures. Essai : `0.050` et `0.05`, acceptées.
2. **Acte de reprise à cinq champs** : ajouter `sha256_de_la_configuration`. Au rejeu d'une livraison refaite, exiger que la configuration donnée ait cette empreinte. Essai : rejeu sous une configuration aux mêmes empreintes de module et de rapport mais à d'autres chaînes, refusé.
3. **Fichier des grandeurs de l'étape (n)**, neuf : `grandeurs-de-l-etape-n-bras-a.json`, dans le dossier de la livraison, cinq champs et eux seuls — `etape`, `grandeurs`, `sha256_du_fichier_de_l_etape_m`, `sha256_du_fichier_des_scores`, `sha256_de_la_configuration` —, écrit sans reste. Dès qu'il existe, ou qu'un fichier d'arrêt de l'étape (n) existe, l'étape (n) ne se rejoue pas. Le code de la version 8 laissait rappeler une étape (n) aboutie : ce n'est plus permis.
4. **Constat de lancement à sept champs** : la ligne de GO est une entrée du programme ; septième champ `ligne_de_go`, `null` pour une première livraison. Le programme d'analyse confronte ce champ à la ligne de l'acte de reprise.
5. **Constat malsain** : aucun fichier sous le nom du constat ; cause affichée ; sortie en échec. C'est ce que fait la version 8 : confirmé.
6. **Registre courant** : toutes les lignes de l'état figé doivent s'y trouver, sinon arrêt sans constat. Confirmé.
7. **Valeurs fictives** : portée de la version 8 confirmée — la configuration, et les lignes d'appui. Le texte ajoute les lignes de révocation aux lignes d'appui du registre courant. Essai de plus : une ligne fictive ailleurs au registre n'arrête rien.
8. **Constat écrit à la main, absence au manifeste** : pas de garde dans le code ; c'est une garde de procédure. Retirer tout essai qui prétendrait le refuser.
9. **`piece_source`** : chaîne `cle_du_module_dans_piece_source`, `null` permis. **Changer** : une sortie qui ne porte pas l'empreinte du module inscrit lève une garde ordinaire, non l'événement d'arrêt ; aucun fichier d'arrêt ; le défaut est rendu à l'enchaînement.
10. **Dossiers** : points 7 et 8 du relevé, confirmés. Le dossier de la livraison porte aussi le constat de lancement et le fichier des grandeurs de l'étape (n).
11. **Étape (m)** : constats d'abord, fichier ensuite. Confirmé.
12. **Formes reconnues** : `effectifs` et `exclues` en tout ou rien, `true` et `false` refusés comme entiers ; aires de la somme et du maximum de l'agrégateur valeur par valeur. Le champ `aire` des lectures de l'agrégateur reste sous la table des formes.

## 5. À dire à la session principale

- La demande 29 de la pièce du lecteur habilité porte déjà les formes de « inscrite » et de « révocation » ; le texte les écrit « à confirmer ».
- La demande 14 de la pièce du développeur ne demande que `effectifs` et `exclues`. La forme des deux clés de l'agrégateur (`agregateur_somme_sans_etat`, `agregateur_maximum_sans_etat`) serait à lui demander aussi ; les pièces sont parties, je ne les ai pas touchées.

## 6. Réserves

1. **Le fichier des grandeurs de l'étape (n) est de moi**, nom et champs. Le relevé offrait deux voies ; j'ai pris celle qui donne une pièce à l'étape, par symétrie avec l'étape (m).
2. **Sur `piece_source`, je m'écarte du code**, qui en faisait un refus de forme. Le vérificateur peut en juger autrement ; la différence est qu'un refus de forme entraîne l'issue que Lazar doit trancher, et qu'une pièce qui n'est pas la bonne ne l'entraîne pas.
3. **Le constat écrit à la main n'est plus un artefact refusé par un programme.** C'est une garde de procédure ; je l'ai dit plutôt que d'ajouter au constat une empreinte du programme, qui n'arrête pas une fraude.
4. **Je n'ai toujours pas relu le texte en entier.**
5. **Le texte s'allonge** (2 100 lignes).

## 7. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v8.md`, en entier.
- `docs/notes/relance-organismes-discrets-v1/verification-brouillon28-bras-a-v1.md`, en entier.
- `docs/notes/relance-organismes-discrets-v1/code-v8-bras-a-note-v1.md` : les lignes trouvées par recherche (fichiers, champs, constat, rejeu, provisoire), une cinquantaine, tronquées.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon28.md` : par programme, pour les contrôles et les ancres ; aucun passage neuf lu.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 511.
- Par programme, pour leur seule empreinte : les 142 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Rien d'autre.
