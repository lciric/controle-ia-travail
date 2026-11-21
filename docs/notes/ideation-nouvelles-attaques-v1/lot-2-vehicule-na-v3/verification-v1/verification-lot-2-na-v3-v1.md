# Vérification du lot 2 v3 (garde de motifs) du véhicule NA-1 — v1

Vérificateur du lot 2 du véhicule NA-1, modèle S. Pièce de travail (classe C). Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt. Données factices ; les données d'Unicode ne sont pas des données de course.

## Verdict

**Conforme.** La v3 porte les trois décisions de la mère : les ignorables d'Unicode 15.1 pris par propriété, la liste fermée « apparence vide » limitée à U+2800 (déclarée comme écart), et les tirets, soulignements et espaces ramenés à une espace. Les comptes rejoués sont égaux ; les quatre contrôles demandés tiennent ; l'extraction se rejoue à l'octet.

**Deux suites à porter**, qui ne remettent pas en cause ce verdict :
1. **Le lot 3 demande une v2.** Il est écrit sur la garde v2 et refuse une garde v3 (§ 4). Le changement est de noms d'import, pas de logique : 72 essais sur 72 passent après le renommage.
2. **Un essai est sauté dans l'exécution standard** (§ 2) : il faut poser une variable d'environnement. À corriger dans le programme d'application du prochain livrable (pas de repli silencieux, R5).

## 1. Empreintes

| pièce | sha256 | état |
|---|---|---|
| table du livrable v3 | `7759069872fdd8540ba6cf0873b7bae06dc48ab537a355497e55b35e14ad81d3` | égale à l'annonce (`77590698…`) ; les 27 fichiers vérifiés OK par `sha256sum -c` |
| rapport v3 | `a343d9e2c5dc61d06910123c9e775372b995ee1cd39f094bbcb2962f38135f97` | égal à l'annonce |
| source Unicode du livrable | `f55d0db69123431a7317868725b1fcbf1eab6b265d756d1bd7f0f6d9f9ee108b` | égale à l'annonce |
| source tirée de `origin/main` au commit `bed42d47` (`git show` redirigé vers mon dossier) | identique à la source du livrable | `cmp` sans écart |
| données des ignorables | `8e15ad688fbb298ade214fe19986e103e4302f0e67d169b7201f730e416699f7` | égale à celle du rapport |

## 2. Essais et mutations rejoués

Copie neuve de l'orchestrateur (commit `a41b7b50…`, sans `.git`) ; paquet v3 du lot 2 appliqué par son programme.

| | annoncé | rejoué |
|---|---|---|
| essais, exécution standard (`--lancer-essais`) | 118 passés, 0 sauté | **117 passés, 1 sauté** |
| essais, avec `NA_SOURCE_UNICODE_15_1_0` posée sur la source versée | 118 passés | **118 passés, 0 sauté** (lot 1 : 62 ; lot 2 : 56) |
| mutations | 98 sur 98 tuées (42 + 35 + 21 neuves) | **98 sur 98 tuées** ; témoin non muté passe ; témoin inerte survit (même variable posée) |

L'essai sauté en exécution standard est `test_extraction_reelle_rejouee_egale_a_l_octet` (`test_na_v3_garde_motifs.py:555`) : il se saute sans la variable. C'est l'essai qui prouve que l'extraction se rejoue. Je l'ai rejoué moi-même (§ 3), mais un saut silencieux dans le programme d'application contredit « aucun repli silencieux ». **Correction demandée** : que le programme d'application pose la variable sur la source du livrable, ou que l'essai échoue au lieu de sauter. Non bloquant.

Mutations adaptées au texte v3 (suffixe « c » ou « b ») : L2-01c à L2-06c, L2-09c, L2-10b, L2-11c, L2-15b, X-30b, X-32b, X-35c. Chacune vise la même garde que l'originale, sur son nouvel emplacement ; je les juge justes.

## 3. Les quatre contrôles demandés

**a) 27 plages et 4 174 points, tirés par programme du seul fichier versé, rejouables : oui.**
- Mon extraction indépendante (un découpage à moi de la source, sans réutiliser le code du livrable) donne 27 plages, 4 174 points, et le total écrit par la source est 4 174. Les plages et les points sont égaux à ceux du paquet.
- Le programme d'extraction du livrable (`pole/extraire_ignorables_unicode_na_v1.py`) est rejoué sur la source tirée de `origin/main` : sa sortie est égale **à l'octet** au fichier de données du paquet (`8e15ad68…`, 1 197 octets).
- Il vérifie l'empreinte de la source, sa version (première ligne), l'ordre des plages, le total et la propriété exacte ; la source est citée dans les données par son chemin, son empreinte, son commit et son en-tête.

**b) L'essai d'égalité des versions refuse toute version autre que 15.1.0 : oui.** Mes sondes : `15.0.0`, `16.0.0`, `15.1`, la chaîne vide et `None` sont refusées ; une version d'interpréteur `16.0.0` est refusée ; des données déclarant `16.0.0` sont refusées au chargement. Essais : `test_autre_version_refusee`, `test_versions_differentes_refusees`, `test_donnees_refusees_sous_un_interprete_d_une_autre_version` ; mutations N3-08, N3-09, N3-21 tuées. Le relevé sur l'interpréteur de la course (`/usr/local/bin/python3`, 3.13.18) donne `unidata_version` 15.1.0.

**c) Le code de la course ne dépend en rien de `regex` : oui.** Aucun module de `pole/` n'importe `regex` (une seule occurrence, dans un commentaire d'en-tête). Il n'apparaît que dans le contrôle et son essai, sous `.venv`, avec un saut explicite s'il est absent. Sous `/usr/local/bin/python3 -I`, le journal du livrable donne `regex_charge: false`, 4 174 points chargés, les huit formes refusées et un texte sain qui passe.

**d) U+2800 est déclaré comme écart : oui.** Il l'est dans l'en-tête du module (l. 5-9 et 58-61 : « écart franc à `par propriété` », avec la raison), dans la constante `APPARENCE_VIDE` (liste fermée), dans le rapport (§ 3, point 1) et dans les remarques (§ 6, point 1). U+2800 est de catégorie « So », non ignorable par défaut et non espace (vérifié) ; un essai vérifie que chaque élément de la liste n'est ni « Cf », ni ignorable, ni espace (`test_liste_fermee_d_apparence_vide`) ; N3-02 tuée.

## 4. Sondes sur la normalisation

Mes sondes de la première passe, rejouées sur la v3, mordent toutes : U+FE0F, U+034F, U+3164, U+2800 dans le mot, un tiret, un tiret long, un soulignement, une tabulation, une fin de ligne, U+2028, une espace insécable, plusieurs espaces, des caractères pleine chasse, une étiquette U+E0041 et U+180E. Les octets d'une requête saine qui contient tirets, soulignement, insécable et tabulation ne sont pas changés par la garde et leur empreinte est celle des octets d'origine. Restent hors des motifs, comme il se doit : un point médian, un point, l'absence d'espace, un accent combinant, un homoglyphe cyrillique.

Les 4 174 points se répartissent en 138 « Cf », 263 « Mn », 4 « Lo » et 3 769 non assignés en 15.1 : le fichier d'Unicode les range tous parmi les ignorables, c'est la définition par propriété.

## 5. Compatibilité du lot 3 : une v2 du lot 3 est nécessaire

Le programme d'application du lot 3 refuse la copie v3 : « fichier requis absent ou d'une autre empreinte : `tirage_na_v2.py` ». Plus grave : le lot 3 importe `garde_motifs_na_v2`. Les classes de la v3 sont d'autres classes que celles de la v2. Sonde sur une copie où les deux coexistent :

- une garde construite par la v3 n'est pas une `GardeMotifs` de la v2 ; `journaliser_envoi` la refuse (`LigneRefusee : la garde de motifs du lot 2 est exigée`) ;
- `ArretMotifInterdit` de la v2 et celui de la v3 sont deux classes distinctes : un `except` de la v2 ne rattraperait pas l'arrêt de la v3.

Sans v2 du lot 3, le lot 4 ne peut donc pas utiliser la garde v3, qui est celle que la mère a décidée.

**Ce qui change dans la v2 du lot 3 (aucune logique)**
- `pole/journal_na_v1.py` : `from pole import garde_motifs_na_v2` devient `…_v3` ; le nom de version du module passe en v2.
- `pole/requete_na_v1.py` : `from pole import tirage_na_v2` devient `…_v3`.
- `essais/aides_na_lot3_v1.py`, `essais/test_na_v1_requete.py`, `essais/test_na_v1_journal.py` : `aides_na_v2`, `garde_motifs_na_v2` et `tirage_na_v2` deviennent `…_v3`. La garde d'essai se construit par `aides_na_v3.garde_essai()`, qui prend déjà le normaliseur.
- `essais/mutations_na_lot3_v1.py` : la liste des fichiers copiés suit (v3, plus les données des ignorables, plus `extraire_ignorables_unicode_na_v1.py`).
- Programme d'application et manifeste du lot 3 : ils exigent le paquet v3 du lot 2 à ses empreintes, non plus le v2.

**Preuve que cela suffit.** Sur une copie neuve avec le paquet v3, j'ai posé les fichiers du lot 3 puis seulement renommé les trois noms ci-dessus : **72 essais sur 72 passent**. Les essais du lot 3 qui touchent la normalisation (« graine factice » et sa requête portant un motif) restent justes avec la garde v3.

À reporter au mandat du lot 4 : l'erratum 1 dit que la garde est « la version vérifiée la plus récente du lot 2 » : c'est désormais la v3, avec la construction `Normaliseur(charger_donnees_ignorables(chemin, empreinte))`, puis `charger_liste_motifs(chemin, empreinte, normaliseur)`, puis `GardeMotifs(liste)`. Le lanceur (lot 8) épingle trois empreintes : programme, liste et données.

## 6. Points à porter à l'additif du véhicule

1. **U+2800** : écart franc à « par propriété », liste fermée, tout ajout est une version neuve du programme. Il est retiré, non ramené à une espace : mis à la place d'une espace, il colle les deux mots (« graine⠀factice » passe, confirmé). À confirmer.
2. **Signe moins U+2212** : exception nommée parmi les tirets, hors de la catégorie « Pd ».
3. **Conséquence pour la liste des motifs réelle** : le texte comparé n'a plus ni tiret, ni soulignement, ni tabulation, ni fin de ligne. Une expression régulière qui attendrait un de ces caractères ne mord plus sur son témoin et le départ est refusé. La rédaction de la liste (modèle F) doit l'écrire contre ce texte (une espace à la place de « - » et de « _ »).
4. **Ordre des opérations** (retrait, compatibilité, casse, compatibilité, retrait, tirets et soulignements, espaces, suites) : valeur du développeur, à écrire.
5. **Version d'Unicode de l'interpréteur de la course** : 15.1.0 (interpréteur 3.13.18). Un changement d'interpréteur refuse le départ, ce qui est voulu.
6. **Source** : chemin, commit `bed42d47`, empreinte, à épingler avec les données (`8e15ad68…`).

## 7. Ce que je n'ai pas fait

Je n'ai pas relu la source Unicode ligne à ligne ; je l'ai lue par un programme indépendant qui retrouve les mêmes plages. Je n'ai pas écrit de mutations neuves sur la v3 : les 21 neuves du développeur couvrent les règles ajoutées, et mes 35 sont rejouées.

— vérificateur du lot 2 du véhicule NA-1, modèle S
