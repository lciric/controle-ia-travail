# Contre-lecture, suite du lot de classe B (requirements-cpu, inventaire v4 et son essai) — v1

**Verdict : Conforme.** Les trois points tiennent. Une réserve de portée (pas une casse) sur l'essai v4, en fin de pièce.

Cible : branche `lot/compte-organisme-v1`, commit `33742cb3`. Lecteur neuf, hostile, aucune pièce écrite par moi. Aucune écriture hors de mon dossier, aucun commit, aucun paquet installé, aucune clé lue.

| Point | Résultat |
|---|---|
| 1. `requirements-cpu.txt` | **Tenu.** Fusion strictement additive, même roue et même version que `requirements-donnees.txt`. |
| 2. Inventaire v4 = contenu du v3 | **Tenu.** 76 entrées, 12 fichiers de lecteurs admis (23 noms), un dossier hors inventaire, tous identiques. |
| 3. Essai v4 : voit retrait et ajout, indépendant du conteneur | **Tenu.** 18 passés sous chaque interpréteur ; mutation 1 tuée ; mutation 2 tuée seulement par la garde (réserve). |

## Relevé de méthode

### Chaîne de raisonnement
1. La fusion : `git show origin/main:requirements-cpu.txt | diff - requirements-cpu.txt` (branche) ne rend que `21a22,24` : trois lignes ajoutées après la ligne 21 (`anthropic==2.12.0`), aucune ligne retirée ni modifiée. Le différentiel de dépôt `git diff origin/main lot/compte-organisme-v1 --stat -- requirements-donnees.txt requirements-cpu.txt` ne cite que `requirements-cpu.txt`, 3 insertions, 0 suppression. Empreinte du fichier de la branche : `04491d0237e479280397fcc9bc72c588f92dfe6bace16e39c813b54ae588184e` (le lisez-moi cite `0f790a13…`, empreinte de la version avant fusion avec `main` : écart attendu, sans effet).
2. Même roue, même version : `grep -n pypandoc requirements-donnees.txt requirements-cpu.txt` rend `pypandoc_binary==1.17` aux deux endroits (ligne 3 du fichier de données, ligne 24 du fichier cpu). `requirements-donnees.txt` n'est pas touché par la branche (pas dans le différentiel avec `main`). Le fichier de données porte aussi l'empreinte de la roue manylinux en commentaire ; la ligne cpu ne la répète pas (ligne non épinglée par empreinte, mais même nom et même version : tenu).
3. Transcription par ma voie : script `transcrire_et_comparer.py` (dans mon dossier), qui lit le v3 par l'arbre syntaxique (`ast.parse`, évaluation des seules affectations `COUVERT`, `EXEMPT`, `REGISTRE`, `LECTEURS_DE_CIBLES_ADMIS`, `HORS_INVENTAIRE`, noms résolus en `couvert` et `exempté`), puis compare au JSON v4. Rendu : registre v3 76, JSON 76 ; clés en trop 0 ; clés manquantes 0 ; valeurs (statut, raison) différentes 0 ; lecteurs admis identiques (12 fichiers, 23 noms) ; hors inventaire identique (`controle_ia/verite_dommage/`) ; 33 couverts et 43 exemptés ; l'ordre diffère (JSON trié), sans effet. Contre-vérification de dénombrement indépendante de l'arbre : `grep -c '^    "controle_ia/[^"]*::' tests/test_cibles_invisibles_v3.py` = 76 (pas de clé dupliquée écrasée à l'évaluation). Empreintes : JSON v4 `ffbda4a0ef2632dd9e91aecb62205a9830ec1f83e9f5fd782e1f5f13eadef878` (égale à son compagnon `.sha256`) ; essai v4 `f1bd4064248d18ccbec472cc1baf981ef44483a884205280dd42b6fd1d85708e` ; essai v3 `93a6df4343f876cad58c01933d2636e65858bc8d55a99285edd4125cb5d504a9`.
4. Détecteurs : lecture du code des deux fichiers. `APPELS_D_INVITE`, `CLES_CACHEES`, `_fonctions`, `_constructeurs_lus` (motifs d'appel, dictionnaire à clé « role », définitions `consigne_privee` et `observation`), la détection de `charger_invite("H12")` et le contrôle des lecteurs sont les mêmes que dans le v3 ; seule la mémorisation de la lecture de l'arbre (`_DEJA_LUS`) est neuve et ne se fonde que sur (dossier, exclusions). Les collecteurs à marqueur restent au v3 : l'essai v4 ne couvre donc que l'inventaire, non le passage du marqueur aux invites.
5. Jeu sous les deux interpréteurs, depuis le dépôt, `PYTHONPATH=src`, `TMPDIR` dans mon dossier, `-B -m pytest -q -p no:cacheprovider tests/test_cibles_invisibles_v4.py` : `/usr/local/bin/python3` : « 18 passed in 10.40s » ; `.venv/bin/python` : « 18 passed in 10.58s ». `git status --short` vide ensuite.
6. Indépendance du conteneur : l'essai `test_essai_independant_du_conteneur` lit l'arbre de l'essai lui-même (importations limitées à `__future__`, `ast`, `json`, `pathlib`, `pytest` ; aucun `environ`, `getenv`, date, sous-processus ; aucun chemin absolu écrit). Sa preuve de fait : il passe sous l'interpréteur du système, où le v3 (qui importe `torch`) ne se collecte pas selon le lisez-moi (non rejoué par moi : je n'ai pas joué le v3).
7. Mutations de ma façon, sur des copies dans mon dossier (arbre `m1/`, `m2/`, `m3/` : copie de l'essai, JSON muté, `src` en lien vers le dépôt, aucun fichier du dépôt touché).
   - **M1**, prédiction : tuée. Changement : la clé `…/environnements/pilote_a.py::jouer_pilote` devient `…::jouer_pilotex`. Attendu : la vraie fonction devient « non examinée » et l'entrée devient « sans fonction ». Résultat : « 12 failed, 6 passed » ; échecs de `test_inventaire_tout_constructeur_d_invite_est_examine` et de `test_inventaire_registre_a_jour` (comme prédit) ; les dix échecs de `test_garde_mutation_module_du_tri_retire` sont collatéraux (leur précondition `non_examines(inv) == []` est fausse sur l'inventaire muté). **Tuée.**
   - **M2**, prédiction : survit sur l'arbre réel. Changement : `hors_inventaire` élargi à `controle_ia/couche2/` (dossier sans entrée de registre ni lecteur admis). Attendu : aucun contrôle sur l'arbre réel n'épingle la liste d'exclusion. Résultat : « 1 failed, 17 passed » ; seule `test_garde_de_l_inventaire_voit_un_constructeur_et_un_lecteur_plantes` échoue, parce que son module planté vit dans `couche2` et devient invisible ; tous les contrôles de l'arbre réel passent. Ma prédiction est donc **juste pour l'arbre réel, fausse pour l'ensemble du fichier** (la garde l'a tuée, par accident de lieu).
   - **M2 bis** (ajoutée pour séparer ce hasard) : `hors_inventaire` élargi à `controle_ia/organismes/` et `controle_ia/sondes/`. Résultat : « 18 passed » : **survit en entier**.
8. Conséquence de 7 : un dossier peut être retiré du balayage en éditant la seule liste `hors_inventaire` du JSON sans qu'aucun essai ne s'en émeuve, hors `couche2`. Même faiblesse dans le v3 (liste `HORS_INVENTAIRE` écrite dans l'essai, éditable de même) : pas une régression. Le v3 gardait de plus `DOSSIERS_SANS_LECTEUR` testé sur le même `HORS_INVENTAIRE` : mêmes limites.

### Objets de contrôle
- Objet faux (le mécanisme doit crier) : inventaire retiré d'une fonction réelle (M1), prédit « échec », rendu « échec » ; module planté dans `couche2` et lecteur de `cibles` planté (garde de l'essai), vu par `non_examines` et `lecteurs_hors_mesures` (essai passé).
- Objet vrai (le mécanisme doit se taire) : le JSON réel, joué sous deux interpréteurs : 18 passés ; la copie saine du module planté (`sain`) ne signale rien (assertion finale de la garde, passée).
- Limite : l'objet « faux » M2 bis n'est pas vu : l'essai ne peut échouer sur une exclusion élargie d'un dossier sans entrée.

### Premier pas non justifié
Pas 6, seulement pour la moitié « le v3 ne se collecte pas sous l'interpréteur du système » : c'est une affirmation du lisez-moi, que je n'ai pas rejouée (consigne : ne jouer que l'essai v4). Ce qui la justifierait : `python3 -B -m pytest -q -p no:cacheprovider --collect-only tests/test_cibles_invisibles_v3.py` sous l'interpréteur du système. Elle n'affecte pas le verdict.

### Trouvaille de côté
- L'essai v4 ne vérifie plus qu'une entrée « couvert » a un collecteur : le statut n'est qu'une étiquette dans le JSON, le v3 garde les collecteurs. L'inventaire v4 seul ne prouve pas la couverture ; il suppose que le v3 est toujours joué. À consigner, sans suite ici.
- Le compagnon `.sha256` de l'inventaire n'est pas lu par l'essai : un JSON modifié sans mise à jour de l'empreinte passerait (à rapprocher de la vérification d'arbre du dépôt, que je n'ai pas jouée).
- Aucune course ouverte pour suivre ces points.

### Évaluateur et conseil
Ce qui juge : l'essai v4 lui-même (18 contrôles) et mes deux interpréteurs ; la comparaison d'inventaire est jugée par mon script, qui sait lire le v3 mais n'a été éprouvé que sur ce couple (objet faux : M1 montre que le JSON est lu et que le test distingue ; mon script n'a pas été joué sur un JSON altéré, c'est une limite). Par où le produit pourrait être jugé bon sans le mériter : une exclusion élargie dans `hors_inventaire` (M2 bis) ; un statut « couvert » sans collecteur ; un compagnon d'empreinte non vérifié.

## Réserve, en une ligne
Ni cassure ni correction exigée : si Lazar veut un essai plus dur, épingler `hors_inventaire` à `("controle_ia/verite_dommage/",)` dans l'essai v4 fermerait M2 bis ; décision de la mère.
