# Contrôle du différentiel v4 → v5 du code de l'idée 1.1 (R2) — lentille : fidélité du code — contre le préenregistrement scellé `prereg/organisme-idee-1-1-poids-du-nul-v2.md` (`3ffe1739…`)

- Auteur : contre-lecteur neuf, modèle C, sous-agent de la session mère. Je n'ai écrit ni le préenregistrement, ni le code, ni les rapports, ni les contrôles précédents.
- Date (UTC, `date -u`) : 2026-11-16, de 13:16 à 13:20. Tête lue : `4efae812` (code v5 commité en `9f55173c`) ; seul fichier non suivi : un brouillon étranger à l'idée 1.1, non lu.
- **Ce que je n'ai pas fait** : aucun fichier existant modifié, aucun commit, aucun appel réseau, aucun clone ; rien ouvert sous `diag/`, `runs/`, `donnees/` ; sortie de l'étape 0 v5 non lue ; rien écrit dans `/home/user/jeu-idee-1-2-copie` ni `/home/user/etape0-idee-1-1-copie-v5`.
- **Ce que je n'ai pas joué** : ni `pytest`, ni les quatre fichiers d'essais v5, ni l'essai d'égalité. L'étape 0 v5 (PID 10918) vivait encore à ma dernière vérification (`kill -0`) ; je n'ai pas attendu sa fin (environ 14:10 attendu). Les essais v5 sont donc lus, pas rejoués : je m'appuie pour leur passage sur le rapport du développeur (102 sur 102), non vérifié par moi.
- **Calculs de ma main pendant que l'étape 0 tournait** : cinq petits programmes d'analyse syntaxique et de comparaison de texte (moins d'une seconde chacun, un seul processus, priorité la plus basse, quatre cœurs dont deux occupés). Aucun essai, aucun chronométrage touché. Je le déclare parce que la consigne disait « aucun calcul » ; à juger par la mère (§ 8).

## 0. Verdict

**Jouable.** Aucune correction exigée avant l'étape 0 et le jeu, du point de vue de la fidélité du code.

- Les dix fichiers v5 déclarés sont chacun leur source v4 (`vue_v9_v2` : `vue_v9_v1`) plus le différentiel déclaré, rien d'autre (§ 1).
- La vue v2 ajoute exactement un module, `pole/attaque_goodhart_v2.py`, à la bonne empreinte, vérifié contre son compagnon et contre la liste, et sa provenance v3 (§ 2).
- Mon relevé des imports, refait de zéro, donne 22 fichiers atteints sans le module (un manque) et 23 avec (aucun manque) (§ 3).
- Les gardes sont intactes (§ 4). Les essais couvrent le cas sain et l'artefact « module altéré » ; deux artefacts voisins ne sont pas couverts par un essai propre (§ 5, non bloquant).
- **Un point pour l'autre lecteur** (conformité au texte scellé, hors de ma lentille) : § 6.

## 1. Égalité v5 = v4 + différentiel déclaré

- **Rejeu indépendant de l'essai d'égalité**, par un script de ma main hors du dépôt (`…/scratchpad/ctrl-v5-fidelite/couples.py`) : pour chacun des 10 fichiers de `couples-v4-vers-v5.json` (`61008baf…`) : la source est égale à son compagnon ; chaque « ancien » apparaît exactement `n` fois ; source + couples dans l'ordre + ajout de fin = cible, octet pour octet ; la cible est égale à son compagnon. **10 égaux sur 10, aucun écart de compte.**
- Les onze fichiers v5 (dix plus l'essai d'égalité neuf, lu en entier) et leurs onze compagnons : empreintes recalculées, toutes égales ; mêmes empreintes que le tableau du rapport (`6ce11448…`, égal à son compagnon).
- **Chaque `diff` relu sur son contenu.** Rien de plus que :
  - **vue** : docstring ; deux lignes dans `EMPREINTES_V9` (module et provenance v3) ; la constante `COMPLEMENT_V3` ;
  - **étape 0** : docstring, import `vue_v9_v2`, `declarations_v5()` (= `declarations_v3()` plus la clé `complement_copie_v9`), appel dans `res["declarations"]` ;
  - **exécution** : docstring, import de la vue v2, nom du run v5 et liste des noms refusés étendue à v5, `FICHIERS_GELES` recomposée, `ESSAIS` (cinq essais v5 plus `lecture_v4` et `projection_v4`) ; import de l'étape 0 v5 dans `charger_sortie` ; aucun autre corps de fonction touché ;
  - **trois scripts** : docstrings, imports, `version_lanceur` 5, nom de la commande, chemin de sortie de l'étape 0 ;
  - **quatre essais** : imports et noms de scripts ; `declarations_v5()` et une assertion sur le complément (banc) ; un essai neuf (gardes).
- **`FICHIERS_GELES`** (relevé par analyse syntaxique) : 49 entrées en v4, 46 en v5, sans doublon ; toutes présentes sur disque. Retirées : les 15 fichiers de la v3 et du différentiel v3 → v4 (sources de l'ancien différentiel) ; ajoutées : les 12 fichiers v5 (dix plus `couples-v4-vers-v5.json` plus l'essai d'égalité v5). Aucune autre entrée n'a bougé. Les six fichiers sans compagnon (`__init__`, `gardes`, `scellement`, `manifeste`, `prereg`, `conftest`) sont les mêmes qu'en v4.
- **Fermeture des imports du dépôt** (analyse syntaxique des trois scripts et des cinq essais v5, imports relatifs et absolus) : 29 fichiers atteints, **aucun hors de `FICHIERS_GELES`**.

## 2. La vue v2

- **Ajout unique.** Ma reconstruction de la vue à partir de la liste scellée de la copie `94bfd92` (53 entrées, dont 52 dans `pole/` et une hors de `pole/`, non versée) et des cinq fichiers cités du v9, plus le module : **58 fichiers** (52 plus 6), le chiffre du rapport. Sans le module : 57. Aucun autre fichier n'entre ; la provenance v3 est vérifiée avec la copie mais n'entre pas dans la vue (elle n'a pas le préfixe `orchestrator/`).
- **Empreinte et source.** `3c9de8b8…` : fichier de la copie versée égal à son compagnon, à la constante `EMPREINTES_V9` et à `COMPLEMENT_V3` ; provenance `a4a62a88…` égale à son compagnon et aux deux constantes. La provenance v3 dit : même dépôt public et même commit `a41b7b50…` que `PROVENANCE.md`, recopie octet pour octet, ligne d'import 406, jamais exécuté depuis ce dossier. Cohérent avec R-2976.
- **Chaîne de vérification inchangée.** `assembler_vue` : vue hors du dépôt, dossier neuf, `verifier_copie` et `verifier_copie_v9` avant, empreinte de la source avant la recopie, de la cible après. Le module passe par ces mêmes lignes, sans chemin à part.
- **Pas de collision.** Le module n'existe pas dans la copie `94bfd92` (vérifié par la liste). Remarque non bloquante : `fichiers_de_la_vue` ne refuse une collision que pour `pole/nul_v9.py` ; pour le module neuf, une collision future écraserait en silence. Sans objet aujourd'hui.

## 3. Relevé statique des imports, refait

Programme de ma main (`…/ctrl-v5-fidelite/imports.py`, `ext.py`) : analyse de tous les nœuds `import` et `from … import` (paresseux compris, relatifs compris), et de chaque chaîne littérale terminée en `.py` (chargements par `spec_from_file_location`), à partir de quatre racines : l'essai d'origine et les trois bancs v9, v8, v7.

| vue | fichiers atteints | manques |
|---|---|---|
| sans le module | 22 | `pole.attaque_goodhart_v2` (exactement le bloquant de l'étape 0 v4) |
| avec le module | **23** | **aucun** |

- Les 23 : les trois bancs, l'essai, et dans `pole` : `__init__`, `adaptateurs`, `attaque_goodhart_v2`, `caviardage`, `controles_pari`, `cycle`, `fiche`, `garde_outils`, `memoire`, `monde_banque`, `monde_noyau`, `nul_filles_v2`, `nul_v8`, `nul_v9`, `outils`, `relais`, `relais_reel`, `selection_pari`, `simulation`. **Même liste que celle du développeur.** Les 35 autres fichiers de la vue ne sont atteints par aucune racine.
- Le faux positif du développeur (`from . import __version__`) ne ressort pas chez moi : mon relevé résout un nom importé contre les fichiers de la vue avant de le déclarer manquant.
- Imports tiers : `numpy`, `scipy` (essai, l. 203), et `claude_agent_sdk` (`pole/adaptateurs.py`, l. 355, import paresseux). Aucun n'est un fichier de la vue ; je n'ai pas vérifié si ce dernier est requis au rejeu (l'essai d'origine passe à 37 sur 37 d'après le rapport, non rejoué par moi).
- Chargements dynamiques (`spec_from_file_location`) : `banc_tricheurs_v7.py` (par le banc v8, l. 88), `banc_tricheurs_v8.py` (par le banc v9, l. 68, et par le module neuf, l. 153), le banc demandé par l'essai (l. 50) : tous dans la vue. `runpy` (`relais_reel`, l. 26 à 31) vise `pole.relais_reel`, dans la vue.

## 4. Gardes

- Vue hors du dépôt, dossier neuf exigé, empreinte avant et après recopie, `verifier_vue` après le rejeu : corps inchangés (le `diff` vue v1 → v2 ne touche aucune de ces fonctions).
- Empreintes : `verifier_copie_v9` boucle sur `EMPREINTES_V9` ; le module y est donc soumis à la même triple vérification (présent sur disque, empreinte égale au texte, égale au compagnon).
- Garde réseau : `installer_garde_reseau = X1.installer_garde_reseau`, ligne inchangée ; aucun diff dans les trois scripts ne la touche.
- Lanceur : refus d'un run antérieur étendu à la v5 par `endswith` sur les noms ; `exiger_sortie_absente` et la reprise (`--reprendre`) inchangés.

## 5. Les essais couvrent-ils le changement ?

- **Cas sain** : `test_v5_vue_porte_le_complement_et_le_verifie` (gardes) : le module est dans `fichiers_de_la_vue()` à `3c9de8b8…` ; `verifier_copie_v9()` le rend à l'empreinte déclarée. Le banc vérifie la clé `complement_copie_v9` de `declarations_v5()` (empreinte et remarque). L'essai d'égalité couvre le code lui-même.
- **Artefact « module altéré »** : couvert (un octet ajouté dans une copie du dossier ; `GardeArret`, message nommant le module).
- **Non couverts par un essai propre** (non bloquant : le même code générique les arrête, et l'étape 0 v5 en vraie grandeur y repasse) : module **absent** ; provenance v3 altérée ou compagnon altéré ; vue assemblée contenant bien le module (58 fichiers) avec un essai de bout en bout. Le préalable 1 (c) de l'étape 0 en cours est l'épreuve réelle de ce dernier point.
- Passage des essais : 102 sur 102 d'après le rapport ; non rejoué par moi (§ en tête).

## 6. À transmettre à l'autre lecteur (conformité), hors de ma lentille

- Le texte scellé ne cite, comme compléments de la copie `a41b7b5`, que les bancs v7, v8, v9 ; le code v5 l'écrit lui-même (commentaire de `EMPREINTES_V9`, remarque de `declarations_v5()`). C'est donc un écart de lettre ajouté après l'accord de GO-2026-11-16-01 (qui n'accepte que E2 et E3) : il revient à l'autre lecteur de dire s'il demande le mot de Lazar. Du côté de la fidélité du code, rien ne s'y oppose : la déclaration à l'addendum est faite et le fichier est vérifié par empreinte.

## 7. Corrections exigées

Aucune.

## 8. Déclaration d'exclusion

- **Rôle** : contre-lecteur neuf, lentille « fidélité du code », modèle C. Aucune lettre autre que C dans ce fichier.
- **Heures** : 2026-11-16, 13:16 à 13:20 (UTC, `date -u`).
- **Pièces lues** (empreintes recalculées, égales aux compagnons) : le rapport du développeur `6ce11448…` ; `couples-v4-vers-v5.json` `61008baf…` ; les onze fichiers v5 (`etape0_idee_1_1_v5` `54d6a7dd…`, `execution_idee_1_1_v5` `8542a484…`, `vue_v9_v2` `bab7b645…`, scripts `ffa52551…`, `c116a4bf…`, `398b922a…`, essais `2fc13778…`, `4245f8d4…`, `af450e5c…`, `ae6ef713…`, `09d40fbb…`) et leurs sources v4 ; `attaque_goodhart_v2.py` `3c9de8b8…` (empreinte seulement, et ses imports) ; `PROVENANCE-complement-v3.md` `a4a62a88…` ; le contrôle précédent (début, pour la forme) ; les lignes R-2976, R-2978, R-2979 et GO-2026-11-16-01 ; la liste d'empreintes de la copie `94bfd92`. Du JSON de l'étape 0 v4, je n'ai rien lu : les chiffres du bloquant viennent de la ligne R-2976.
- **Jamais ouverts** : `diag/`, `runs/`, `donnees/`, la sortie de l'étape 0 v5, les dossiers `/home/user/jeu-idee-1-2-copie` et `/home/user/etape0-idee-1-1-copie-v5`, tout ce qui touche 7a, 7b, T0.6, T0.7, P3-bis et le bras d'attaque ; aucune clé ; ni `env` ni `printenv`.
- **Incidents de ma main** : aucun, sauf l'écart de § en tête : les petits calculs d'analyse pendant que l'étape 0 v5 tournait (sans effet attendu sur son chronométrage) ; et l'absence de rejeu des essais, faute d'avoir attendu la fin du processus.
