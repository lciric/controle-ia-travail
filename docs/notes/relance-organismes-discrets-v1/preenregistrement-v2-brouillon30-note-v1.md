# Note de changements — brouillon 30 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 à 29.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon30.md`, `0b51d1dde38a8a7471a92fabd2ab1cd2d54312ce77b690ea8c4967447d008963` (2 123 lignes). Les brouillons 20 à 29 ne sont pas modifiés.
- **Demandes à la session principale, version 5**, écrites avant le brouillon et citées par lui :
  - `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v5.md`, `fc3f3c1338ac4effa4ec3ca88ecd785e28426fae9d4ef2f8098cb5b074130e2d` ;
  - `docs/notes/relance-organismes-discrets-v1/demandes-au-lecteur-habilite-et-a-lazar-bras-a-v5.md`, `7c7c8c4c52094be02297dc57cab4e1b9278c94d5630e5de752680cd3db3877f3`.
  Les versions 4 ne sont pas modifiées.
- **Fiches pour Lazar : aucun fichier neuf.** Aucun point porté ne touche une règle de jugement. Celles du brouillon 23 restent en vigueur (`f20abfed…`).
- **Sources** : la vérification du brouillon 29 (`774c996d…`, « engageable après corrections »), en entier ; la vérification des corrections du code de la version 8 (`e8786ca7…`), son en-tête et ses parties 2 et 3 ; son complément 1 (`71e9a60b…`), en entier.
- **Méthode** : copie du brouillon 29 par `cp`, puis 31 remplacements exacts, chacun vérifié unique par programme. Les deux pièces des demandes sont des copies des versions 4, retouchées par remplacements exacts.
- **Registre des accords** : relu sur la branche principale distante au commit `f637e163` ; aucune ligne de plus.
- **Heures (UTC, `date -u`)** : début 19:01:30Z le 2026-11-19 ; brouillon scellé à 19:06:18Z.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucun module du code ouvert ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; aucun sous-agent.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| section 12 ; « Critères de lecture gelés » en entier ; section 10 | identiques, caractère pour caractère, au brouillon 29 |
| titres ; consignes figées | inchangés ; `98a9bd34…` et `ecf590ea…` recalculées |
| citations à la lettre | brouillon 20 : 935 sur 935 ; brouillon 29 : 1 189 sur 1 189 |
| table d'en-tête, sans les fichiers cloisonnés | 163 lignes à empreinte : 149 recalculées et égales, 0 différente, 14 sautées et non ouvertes |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | les deux problèmes attendus |
| pièce du développeur, version 5 | aucune chaîne hexadécimale de huit signes ou plus ; aucun nom d'une version précédente ; vingt-trois demandes |

## 1. Ce qui est porté

| source | objet | ce que le texte dit maintenant | où |
|---|---|---|---|
| texte, C-1 | gardes de `piece_source` et des dossiers | cas sains et artefacts à la ligne « ce qui n'est pas un refus d'une livraison » | 8.4 |
| texte, M-1 | ordre ; `piece_source` mal formé | la garde de la provenance joue avant toute garde de la liste fermée ; mal formé, ou sans la clé inscrite : provenance non établie, sans l'issue du point 21 | 6.9 ; 8.4 |
| texte, M-2 | borne haute écrite en long | pleine précision demandée pour les aires, les aires des plis et les bornes hautes ; l'épreuve de forme le vérifie | 6.9 ; 13.1 |
| texte, M-3 | empreinte du programme du constat | huitième champ du constat ; cinquième entrée de `pieces_attendues` ; le programme d'analyse confronte les deux | conventions ; 6.9 ; 8.4 |
| code, C-1 | révocation reconnue au type | **par le sens** : toute ligne entrée depuis l'état figé qui nomme la ligne de GO employée, quel que soit son type, rend le constat malsain ; de même, dans l'état figé, une ligne de GO que nomme une ligne entrée après elle n'ouvre rien | conventions ; 8.4 |
| code, M-2 | ligne qui retire la configuration | seule la **ligne d'inscription** — type « inscription », `CONFIG-ANALYSE-DISCRETION-BRAS-A`, empreinte entière — inscrit ; toute autre ligne neuve qui cite l'empreinte rend le constat malsain | conventions ; 8.4 |
| code, M-1 | valeur ajustée contraire à l'état | rapportée exacte ; un nombre à virgule affiché porte « arrondie » ; **l'état fait foi** | 6.9 |
| code, M-3 | trace d'un constat malsain | écrit sur la sortie du programme, dans la forme à huit champs ; versé par la session au manifeste du lancement, qui est scellé ; aucun fichier sous le nom du constat | conventions ; 8.4 |
| code, M-4 | moment du constat | constat et lecture dans une même exécution ; l'acte de reprise et les constats de l'étape (m) portent l'empreinte du constat ; un rejeu et l'étape (n) relèvent de la lecture déjà partie | conventions ; 8.4 |

**Le remède d'un constat malsain pour « ligne neuve à voir » est toujours le même** : une ligne de GO neuve, donc un autre mot de Lazar, et une configuration neuve, scellée sur le nouvel état du registre. Le programme ne juge pas ce que la ligne veut dire.

## 2. Ce que le code de la version 9 doit porter

Les cinq écarts du complément 1 de la vérification du code tiennent (acte de reprise, fichier des grandeurs de l'étape (n), constat à champ `ligne_de_go`, lignes de révocation parmi les lignes regardées pour les valeurs fictives, `piece_source` en garde ordinaire). S'y ajoutent, depuis ce brouillon :

1. **Constat de lancement à huit champs** : `date_utc`, `sha256_de_la_configuration`, `sha256_du_registre_fige`, `commit_du_registre_courant`, `configuration_inscrite`, `revocation_entree`, `sha256_du_programme_du_constat`, `ligne_de_go`. Le programme y écrit sa propre empreinte.
2. **`pieces_attendues` à cinq entrées** : s'ajoute `sha256_du_programme_du_constat`. Le programme d'analyse exige l'égalité avec le champ du constat ; sinon garde ordinaire.
3. **Révocation par le sens.** Dans le registre courant, toute ligne absente de l'état figé qui nomme l'identifiant de la ligne de GO employée rend `revocation_entree` vrai, quel que soit son type. L'identifiant se compare en entier : `GO-2099-01-01-011` ne nomme pas `GO-2099-01-01-01`. Essais : type « revocation » sans accent ; type « décision » qui dit l'accord révoqué ; simple mention ; identifiant voisin, qui n'arrête rien.
4. **Inscription par sa forme.** `configuration_inscrite` est vrai quand une ligne de type « inscription », qui porte `CONFIG-ANALYSE-DISCRETION-BRAS-A` puis l'empreinte entière, se lit dans le registre courant. Toute autre ligne absente de l'état figé qui cite cette empreinte rend `revocation_entree` vrai. La chaîne et le type sont à confirmer par la session principale : en faire deux constantes nommées, en un seul endroit.
5. **Dans l'état figé**, pour une reprise : une ligne de GO que nomme une ligne placée après elle n'ouvre rien, quel que soit le type de cette ligne.
6. **Constat malsain** : aucun fichier ; le programme écrit sur sa sortie standard le constat dans la forme à huit champs, en une ligne JSON, et sort en échec. La session verse cette sortie au manifeste.
7. **Acte de reprise à six champs** : `evenement`, `ligne_de_go`, `sha256_de_la_livraison_refusee`, `sha256_de_la_livraison_refaite`, `sha256_du_constat_de_lancement`, `sha256_de_la_configuration`.
8. **Constats de l'étape (m) à onze champs** : s'ajoute `sha256_du_constat_de_lancement`.
9. **Rejeu et étape (n)** : ils exigent le constat déjà présent, sans en demander un neuf ; ils vérifient que son empreinte est celle que portent l'acte de reprise ou les constats de l'étape (m).
10. **`piece_source`** : la garde de la provenance joue avant toute garde de forme. `piece_source` mal formé, ou sans la clé inscrite, lève la même garde ordinaire qu'une empreinte d'un autre module. Jamais l'événement d'arrêt.
11. **Valeur ajustée** : calculée en fractions exactes sur les valeurs rendues ; rapportée exacte ; tout nombre à virgule affiché à côté porte « arrondie ».
12. **Gardes des dossiers** : essais du cas sain et des artefacts de la ligne de 8.4 — dossier `livraison-<rang>` sans configuration, rang avec un zéro devant, dossier des arrêts absent, sous un dossier de livraison, au-dessus de lui, ou autre que celui des configurations voisines.

**Rectification de la note du brouillon 29.** J'y écrivais que le code de la version 8 exigeait que la valeur de la famille « s'écrive comme » la valeur p haute. Le complément 1 montre que ce n'est pas le cas : le code compare déjà les fractions. Il n'y a pas d'écart sur ce point.

## 3. Les demandes, version 5

**Pièce du développeur : ce qui change depuis la version 4, exactement.**
1. Le titre : « v5 ».
2. La phrase sous « Numéros » : « Les demandes 1 à 21 gardent les numéros qu'elles avaient dans les versions précédentes […] ; les demandes 31 et 32 sont neuves. »
3. Deux lignes de plus à la table des numéros : `31 | —` et `32 | 13`.
4. Une section neuve, « IV. Deux demandes de plus sur la forme », après la demande 21 :
   - **demande 31**, la forme de `agregateur_somme_sans_etat` et de `agregateur_maximum_sans_etat` : un nombre par dose, ou une table par dose ; toutes les valeurs sont-elles des nombres de 0 à 1. Réponse : l'une des deux formes ; oui ou non ; pour une table, le nombre de ses champs, **sans leurs noms**.
   - **demande 32**, la pleine précision des aires, des aires des plis et des bornes hautes. Réponse : décimales et arrondi d'aujourd'hui ; oui ou non. La raison donnée ne nomme aucun seuil : « l'analyse compare ces nombres sur leur écriture décimale, sans arrondi ».
5. « Ce qui presse » : 32 rejoint « avant le code de l'analyse » ; 31 rejoint « sans échéance ».

Rien d'autre ne change : la liste de non-ouverture, l'en-tête, la table des cinq cas et les demandes 1 à 21 sont, au mot près, celles de la version 4. La forme d'une ligne de révocation n'y est pas : le registre est tenu par la session principale, non par le développeur.

**Pièce du lecteur habilité et de la session principale : ce qui change depuis la version 4.**
- Le titre, et le nom de la pièce du développeur citée (version 5), avec la mention de ses demandes 31 et 32.
- La ligne « Elle remplace » cite la version 4.
- Le texte visé est le brouillon 30, cité par son chemin.
- **Demande 29** : elle ne demande plus la forme d'une révocation, elle propose deux formes et demande si elles conviennent — la ligne d'inscription de la configuration ; la reconnaissance d'une révocation par le sens. Elle demande aussi, pour information, sous quel type une révocation s'inscrit d'ordinaire. Les bornes de l'exemple fictif sont gardées.

## 4. Réserves

1. **La forme de la ligne d'inscription est de moi** : type « inscription », chaîne `CONFIG-ANALYSE-DISCRETION-BRAS-A`. Je ne sais pas comment le registre des accords est tenu ; la demande 29 la soumet à la session principale. Si elle répond autrement, deux constantes changent.
2. **« Par le sens » fera des faux malsains** : une simple mention de la ligne de GO dans une ligne neuve arrête le lancement, et le remède coûte une ligne de GO neuve. C'est voulu : un faux malsain coûte une ligne, une révocation manquée ferait lire sous un accord retiré.
3. **« Même exécution » n'est pas vérifié par le programme d'analyse** : il vérifie que la lecture porte l'empreinte de son constat ; l'écart de temps se lit au manifeste. Je n'ai pas écrit de durée maximale, pour ne pas inventer un nombre.
4. **La pleine précision des bornes est une demande, non une garde.** Le programme ne refuse pas une borne écrite en long ; l'épreuve de forme doit la voir avant toute dépense.
5. **Les pièces des demandes en version 5 demandent une relecture de cloisonnement** avant de sortir ; les changements de la pièce du développeur sont listés en partie 3.
6. **Je n'ai toujours pas relu le texte en entier.**

## 5. Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/verification-brouillon29-bras-a-v1.md`, en entier.
- `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v8-bras-a-v1.md` : en-tête, parties 2 et 3.
- `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v8-bras-a-v1-complement-1.md`, en entier.
- Les deux pièces des demandes en version 4 : les passages retouchés, et par programme.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon29.md` : par programme, pour les contrôles et les ancres.
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 511.
- Par programme, pour leur seule empreinte : les 149 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Rien d'autre.
