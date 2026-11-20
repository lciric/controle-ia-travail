# Rapport du développeur — banc des juges scriptés de la ligne 3, v4, mode « portée à 200 » — v1

Pièce d'instrument (classe B), à contre-lire par un autre modèle. Écrit le 2026-11-20 sur le mandat
`mandat-developpeur-banc-v4-portee-200-v1.md` (`89462f4d97595cefde51e218c3548ec9c189598c5dfab08fd19617b7ff0f03fc`,
égale à son compagnon). Développeur, modèle O.

**Aucune racine neuve n'a été dérivée, aucune mesure n'a été lancée.** Seule la racine des essais 2026111930 a été
dérivée (essais, contrôle des défauts réintroduits). Aucune écriture dans le dépôt `/home/user/controle-ia-travail`,
aucun appel de modèle, aucune dépense. Règle d'aveugle tenue : rien n'a été ouvert sous `execution-etage-1-v1/`,
`verdict-etage-1-v1/` ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`.

## 1. Ce qui fait foi, vérifié

| pièce | où | sha256 | contrôle |
|---|---|---|---|
| additif 3 v3 (en entier ; § 5 cahier des charges) | `git show 0bb14c64:prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md` | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` | égale au compagnon et à l'attendue |
| additif 2 v3 (§ 6, § 7 ; lu en entier) | même commit | `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a` | égale au compagnon |
| banc v3 | `…/code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` (disque) | `09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0` | égale au compagnon, inchangé à la fin |
| chronométrage v3, essais v3, contrôle v3 | même dossier | `8cb61afb…`, `28ad0e89…`, `b4078e71…` | égaux aux compagnons |
| calcul de référence et sa sortie | `…/ligne-3-votes-effectifs-juges/calcul_predictions_ligne_3_v2.py`, `calcul-predictions-ligne-3-v2.json` | `802d4dd2…`, `2cf1eba7…` | égaux aux compagnons |

## 2. Fichiers écrits

Dossier du code : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-banc-v4-portee-200/code/`
(copie des quatre programmes du dossier du banc v3 et de leurs compagnons, inchangés, puis fichiers neufs). Chaque
fichier neuf a son compagnon `.sha256`.

| fichier | sha256 |
|---|---|
| `banc_juges_scriptes_ligne_3_v4.py` | `79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7` |
| `chronometrer_portee_200_ligne_3_v1.py` | `6b9d2cbfd9bbf638d30c0d314531de510d85a4a2b28c8da40100ec8c7be51b90` |
| `essais_banc_juges_scriptes_ligne_3_v4.py` | `9b9141912f70c3296f1a90e201c7bef04c58d3b9e2837ebef47becc96a49a0e7` |
| `controle_defauts_reintroduits_ligne_3_v4.py` | `8e33404baa66a38f000922e054993e4641e65eb833773a0d14965061dfbffb81` |
| `rapport-defauts-reintroduits-ligne-3-v4.json` (mode « visé ») | `85cec7ec5493c9dc11dc0d7b6c5ff701145d126997c7a0d07458ccb4ff5b4e9c` |
| `rapport-defauts-reintroduits-fichier-entier-ligne-3-v4.json` (mode « complet ») | `261775ac578cf15f1adc1988f65b91763c4afe3f1bfc2dab58a8f6febe61fd26` |
| `differentiels-v3-v4/banc-v3-v4.diff` | `746974ccbae0f4585ac5011be62d559a9267a09a14b871f1a869560b71fb9a4e` |
| `differentiels-v3-v4/essais-v3-v4.diff` | `13e25b37c9970654123182f3ff3e05e8c5156a64bf783f7c240c0a2f2e16dfea` |
| `differentiels-v3-v4/controle-v3-v4.diff` | `7fb14d5d6bdc38dd2a6272e45689555491e30281ad968f7e40c9956d03c6158d` |
| `differentiels-v3-v4/chronometrage-v3-portee-200-v1.diff` (chronométrage v3 → chronométrage de la portée v1) | `34fc9a2eb7cecb29214c55e88dbc92337f04a5f1669dcab526a0b4bf426b0f13` |

Copiés sans changement (empreintes égales aux compagnons du v3) : `banc_juges_scriptes_ligne_3_v3.py`,
`chronometrer_banc_ligne_3_v3.py`, `essais_banc_juges_scriptes_ligne_3_v3.py`,
`controle_defauts_reintroduits_ligne_3_v3.py`, avec leurs compagnons. Le banc v3 copié sert à la preuve d'égalité
(chargé par son empreinte).

## 3. Essais et sortie

Commande (dossier temporaire dans le bloc-notes) :

```
env -C DOSSIER_DU_CODE PYTHONDONTWRITEBYTECODE=1 TMPDIR=<bloc-notes>/tmp-essais-final \
    /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_banc_juges_scriptes_ligne_3_v4.py
```

Sortie : **157 passed in 13.83s** (Python 3.13.18). Le v3 en comptait 115 ; les essais du v3 sont gardés, ceux qui
nommaient les racines de l'étage 1 sous autorisation, le mode « decisif », le chronométrage de l'étage 1 ou les noms
de sortie en v3 sont adaptés.

Contrôle des défauts réintroduits, rejoué et étendu :

```
env -C DOSSIER_DU_CODE PYTHONDONTWRITEBYTECODE=1 /home/user/controle-ia-travail/.venv/bin/python -B \
    controle_defauts_reintroduits_ligne_3_v4.py --banc banc_juges_scriptes_ligne_3_v4.py \
    --chronometrage chronometrer_portee_200_ligne_3_v1.py --essais essais_banc_juges_scriptes_ligne_3_v4.py \
    --travail <bloc-notes>/travail-controle-vise-final --sortie rapport-defauts-reintroduits-ligne-3-v4.json --mode vise
```

- Mode « visé » : essais visés sur le banc sain : 123 passés ; **138 défauts vus sur 138** (les 93 du v3, rejoués
  sans changement de texte : v1 27, contre-lecture 35, c2 1, v2 1, graines 6, silence 1 10, silence 2 11, égalité 2 ;
  plus 45 neufs : `v4_portee_200` 39, `v4_chronometrage` 6). « tous vus : True ».
- Mode « complet » (fichier d'essais entier, arrêt au premier échec ; la famille « graines » reste visée) :
  fichier entier sur le banc sain : 157 passés ; **138 défauts vus sur 138**, mêmes familles ; « tous vus : True »
  (même commande, `--mode complet`, travail `<bloc-notes>/travail-controle-complet-final`, sortie
  `rapport-defauts-reintroduits-fichier-entier-ligne-3-v4.json`).

Un défaut neuf n'a pas été vu au premier passage (`V4-F02`, ancres des formules retirées) : l'artefact « formule
faussée » de l'essai était aussi vu par le contrôle des mondes faisables ; il a été rendu plus fin (faute de 1e-6,
cohérente avec elle-même), et il n'est plus vu que par les ancres. Aucun autre ajustement.

Chaque garde du § 6 de l'additif 3, sur un cas sain et sur un artefact (règle R5), aucune dérivation des racines neuves :

| garde | cas sain | artefacts (chacun vu, refus avant toute dérivation) |
|---|---|---|
| racines | `verifier_racine` accepte 2026112031 (clés 2 et 12), 2026112032 (clé 2), 2026112033 (clé 12), `.spawn(210)`, autorisation juste — sans dériver | sans autorisation ; empreinte fausse ; additif absent ; tâche hors de l'additif 3 à chaque racine ; `.spawn(209)`, `.spawn(1)` ; 2026112034 ; 2026111931 à 2026111937, **avec ou sans autorisation juste** ; modes « decisif » et « chronometrage » inconnus ; `--decisif` refusé par la ligne de commande ; étage 1 refusé hors essai |
| taille | n = 200 | n = 100, 400, 199, 200.0, « 200 », absent, booléen |
| configuration gelée | `CONFIGURATION_PORTEE_200` épinglée | configuration réduite, `dossier_du_code` imposé, mode du chronométrage, hors essai |
| dossier du code propre (dépôt git jetable créé sous le dossier temporaire des essais) | dossier suivi et propre, sortie hors du code : l'exécution part (cas sain du mode neuf) | fichier étranger ; fichier suivi modifié ; fichier étranger en sous-dossier ; sortie sous le code ; sortie égale au code ; hors dépôt (`GIT_CEILING_DIRECTORIES`) ; `archives-reponses-modeles/` dans le code |
| une exécution par dossier | dossier neuf | dossier déjà présent ; second lancement dans le même dossier |
| formules | `d` et écart vrai égaux au calcul de référence, 210 cellules ; treize mondes faisables à 0,10 égaux à ceux du calcul de référence et de l'additif 3 ; deux ancres écrites à la main (ρ = 0 : 1,2 d et 0,6 d) | bissection faussée partout ; bissection faussée à ρ > 0 seulement ; formule faussée de 1e-6 ; liste des mondes attendus altérée : `BancInvalide` avant tout tirage |
| règle de lecture | 1 000 sur 2 000 : issue A ; 999 : B ; comparaison sans cellule : B | règle codée à l'envers (« > ») : l'aide rend B à 1 000, la garde rend le banc invalide |

Cas sain du mode neuf (racine des essais, 12 répliques, 40 tirages, n = 200) : 210 cellules dans l'ordre gelé (42,
42, 126) ; treize mondes faisables à 0,10 ; `d`, a, b et écart vrai égaux à ceux de `calcul_predictions_ligne_3_v2`
(et `d` arrondi égal à sa sortie) ; moitié « lecture » de 50 bons et 50 mauvais ; une cellule rejouée sur les mêmes
enfants rend la même chose à n = 200 et autre chose à n = 100 ; comptes entiers égaux aux puissances ; manifeste
(dérivations : deux, de 210 enfants, clés 2 et 12 ; `dossier_du_code_propre` vrai ; empreintes).

Égalité : sur la racine des essais seule, les fichiers de résultat de l'étage 1 du v3 et du v4 sont égaux à l'octet
une fois le nom de version remplacé (une seule occurrence), sur deux configurations d'essai ; aucune clé ajoutée ni
retirée ; manifestes : mêmes graines, mêmes dérivations, même configuration et même empreinte ; `cellule_puissance` à
n = 200 rend la même cellule dans les deux bancs. L'essai final vérifie qu'aucune SeedSequence n'a été créée sur
2026111931 à 2026111937 ni sur 2026112031 à 2026112033.

Essais de la ligne de commande dans le bloc-notes (aucune dérivation) : `--portee-200` avec une autorisation fausse :
« refus : dossier du code hors d'un dépôt git » (le bloc-notes n'est pas un dépôt), code 2 ; `--decisif` : refus
d'argparse, code 2 ; chronométrage avec une autorisation absente : « refus : racine 2026112031 : additif absent »,
code 2.

## 4. Ce qui change, et rien d'autre

**Banc v4** (différentiel `banc-v3-v4.diff`) :
1. `VERSION` en v4 ; empreinte de l'additif 3 en constante (`EMPREINTE_ADDITIF_3_PORTEE_200`), portée au manifeste
   du mode neuf (`additif_qui_fait_foi_sha256`).
2. Graines : `RACINES_TOUJOURS_REFUSEES` = 2026111931 à 2026111937 ; `RACINES_SOUS_AUTORISATION` = les trois racines
   neuves ; tâches permises par racine neuve (2031 : clés 2 et 12 ; 2032 : clé 2 ; 2033 : clé 12) et `.spawn(210)`
   seul. Les contrôles de `generateurs` passent dans `verifier_racine` (pure), que `generateurs` appelle d'abord.
3. `MODES` : « chronometrage » et « decisif » de l'étage 1 retirés ; « chronometrage_portee_200 » (2031, 2031) et
   « portee_200 » (2032, 2033) ajoutés. `executer_etage_1` refuse tout mode autre que « essais » ; ses fichiers de
   sortie sont nommés en v4.
4. `commit_du_depot` et `construire_manifeste` prennent un dossier du code facultatif (défaut inchangé).
5. Section neuve « mode portée à 200 » : `CONFIGURATION_PORTEE_200` (répliques 2 000, tirages 2 000, écarts 0,05 ;
   0,10 ; 0,15, lois 1 et 3, sept ρ, trois ρ′, n = 200) ; `MONDES_FAISABLES_A_0_10` ;
   `faisabilite_cellule_puissance` ; `issue_de_la_regle_de_lecture` (comptes entiers, 2 k ≥ R pour A) ;
   `verifier_gardes_portee_200` ; `verifier_dossier_du_code_propre` ; `verifier_variables_de_chemin_non_posees` ;
   `comptes_gagnes` ; `criteres_portee_200` (aide) ; `executer_portee_200` (ordre : taille, mode, configuration gelée
   hors essai, dossier de sortie neuf, dossier du code propre, racines et autorisation, gardes déterministes, puis
   dérivations ; résultat `resultat-portee-200-ligne-3-v1.json`, manifeste `manifeste-portee-200-ligne-3-v1.json`,
   chacun avec son compagnon).
6. `main` : `--portee-200` seul (`--decisif` retiré), refus si une variable de chemin est posée.

Aucune fonction de calcul ne change : `cellule_puissance`, `resoudre_dissymetrie`, `erreurs_equilibrees_formules`,
`holm`, `p_valeur_unilaterale`, `poids_covariance`, `indices_moities`, `puissance_qui_decide` et les autres sont
identiques au v3.

**Chronométrage** `chronometrer_portee_200_ligne_3_v1.py` (neuf, sur le modèle du v3) : dérive la seule racine
2026112031 (clés 2 et 12, `.spawn(210)` chacune) ; joue une cellule faisable (la première à 0,10 : unanimité, loi 1,
ρ = 0, rang 14) à n = 200 sur un échantillon de répliques avec B = 2 000, et extrapole au nombre de cellules faisables
(49) et à 2 000 répliques ; n'imprime que trois lignes de durées ; hors essai, avant toute dérivation : variables de
chemin non posées, autorisation juste aux deux tâches, banc chargé du même dossier, dossier du code propre, dossier du
manifeste neuf.

**Essais v4** et **contrôle v4** : voir § 3 et les différentiels.

## 5. Les deux commandes de lancement (gabarit de l'additif 3, § 5, complété)

Depuis le dossier du code, une fois commité tel quel dans le dépôt (tous ses fichiers suivis, rien d'autre) ; sans
`BANC_LIGNE_3_CHEMIN` ni `CHRONOMETRAGE_LIGNE_3_CHEMIN` ; `DOSSIER` et `DOSSIER_NEUF` n'existent pas encore et sont
hors du dossier du code ; le chronométrage d'abord, puis la mesure, une fois.

```
env -C DOSSIER_DU_CODE PYTHONDONTWRITEBYTECODE=1 python3 -B chronometrer_portee_200_ligne_3_v1.py --autorisation-additif CHEMIN --empreinte-additif HEX --manifeste DOSSIER
```

```
env -C DOSSIER_DU_CODE PYTHONDONTWRITEBYTECODE=1 python3 -B banc_juges_scriptes_ligne_3_v4.py --portee-200 --autorisation-additif CHEMIN --empreinte-additif HEX --sortie DOSSIER_NEUF
```

`CHEMIN` (absolu) et `HEX` : l'additif de code de cette mesure, scellé, et l'empreinte de son compagnon — à porter par
l'additif de code. Sorties : `DOSSIER/manifeste-chronometrage-portee-200-ligne-3-v1.json` ;
`DOSSIER_NEUF/resultat-portee-200-ligne-3-v1.json` et `DOSSIER_NEUF/manifeste-portee-200-ligne-3-v1.json`, chacun
avec son compagnon. Au manifeste de la mesure, la mère trouve : `programme_sha256` (à comparer à `79865552…`),
`autorisation`, `configuration` et `configuration_sha256`, `graines` (racines 2026112032 et 2026112033, table des
clés, deux dérivations de 210 enfants), `depot.dossier_du_code_propre`, `fichiers` (empreinte du résultat),
`additif_qui_fait_foi_sha256` ; au manifeste du chronométrage, `programme_chronometrage_sha256` (à comparer à
`6b9d2cbf…`).

## 6. Remarques (points que la lettre de l'additif 3 ne tranche pas)

1. **Garde « dossier du code propre »** : appliquée au banc et aussi au chronométrage (qui dérive 2026112031) ; elle
   refuse en plus un dossier du code qui contient `archives-reponses-modeles/` et, à la ligne de commande, une
   variable de chemin posée (additif 2, § 7, points 1 et 2, rendus durs). `git status --porcelain` est pris à la
   lettre : un fichier ignoré par `.gitignore` n'y paraît pas. Conséquence pratique : tous les fichiers du dossier
   du code (rapports JSON et différentiels compris) doivent être commités avant le lancement, sinon refus.
2. **Racines neuves** : `verifier_racine` impose la table du § 2 (tâches par racine) et `.spawn(210)` ; c'est plus
   strict que la lettre, qui le dit au § 2 sans dire qu'une garde l'impose.
3. **Comptes entiers** : `cellule_puissance` n'est pas modifiée ; le compte est relu sur la puissance (k = arrondi de
   p × R, et k / R doit valoir p exactement, sinon `BancInvalide`).
4. **« Près du seuil »** : 0,478 à 0,522 lus bornes comprises (956 à 1 044 sur 2 000) ; la lettre ne dit pas si les
   bornes sont comprises. La mention est dans l'aide, sans effet sur l'issue.
5. **Aide** : elle porte aussi la lecture du banc v3 (`puissance_qui_decide`) sur les mêmes cellules, pour contrôle,
   et la liste des cellules au minimum (ex aequo compris).
6. **Faute du banc (§ 6)** : le code ne compare pas `d`, a, b à ceux du résultat de l'étage 1 (il ne lit aucune
   mesure) ; c'est à l'agent qui prononce. Les gardes déterministes couvrent la part qui ne dépend d'aucune mesure.
7. **Interruption** (§ 6, exécution unique, point 1) : le code ne peut pas l'écrire au manifeste d'une exécution
   relancée ; c'est à la mère.
8. **Noms de sortie de l'étage 1** en v4 (joignable en essai seulement) ; l'égalité au v3 est donc montrée sur le
   contenu, à l'octet, nom de version remplacé.
9. La preuve d'égalité v2 → v3 du v3 est remplacée par la preuve v3 → v4 (les défauts « égalité » E01 et E02 du v3
   sont visés sur elle) ; l'égalité au v2 tient par le v3.
10. Le chronométrage extrapole sur les 49 cellules faisables de la configuration (tous écarts), d'après une seule
    cellule ; c'est une durée, ni critère ni garde.

## 7. Écarts au mandat, déclarés

1. `FETCH_HEAD` ne désignait plus main après mon `git fetch origin main` (une autre session avait réécrit ce
   fichier : il pointait `98a8dc98…`, où l'additif 3 n'existe pas à ce chemin). J'ai lu l'additif 3 et l'additif 2 sur
   le commit `0bb14c6403ad1390fa1be7a1adc06c3049d7fac4` (= `origin/main` après mon fetch, le commit de scellement
   nommé par le mandat) ; empreintes égales aux attendues.
2. « Copie du dossier du banc v3 » : sans commande de liste, je n'ai copié que les fichiers nommés à l'additif 2,
   § 3.1 et § 3.2 (les quatre programmes et leurs compagnons), pas les rapports, journaux ni différentiels v2 → v3.
3. Outil de travail hors du dossier du code : `outils/mondes_faisables.py` (bloc-notes), lancé une fois sur le banc v3
   copié, par formule seule (aucun tirage, aucune graine), pour écrire la constante des treize mondes ; les essais la
   recoupent avec le calcul de référence. Recherches de motif bornées à un fichier (ma copie du banc, la sortie du
   calcul de référence, mon rapport de contrôle) ; un `sed -i` sur mon propre fichier de contrôle (renommage des
   identifiants neufs en `V4-…`, après un refus « identifiants en double » du contrôle, qui n'avait rien lancé).
4. Le chronométrage n'a pas été lancé hors essai (il dériverait 2026112031) : le mandat interdit toute dérivation des
   racines neuves.

Développeur, modèle O.
