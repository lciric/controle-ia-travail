# Rapport du développeur — programme des étapes 3, 4, 5 et 6 du palier 0b — v2

**EN ATTENTE DU MOT DE LAZAR.** Pièce de travail (classe C). Rien n'est lancé en vrai ; aucune graine décisive ; rien n'est versé.

- Auteur : développeur, modèle O, le développeur du code v6 et du programme v1. 2026-11-20.
- Mandat : le même que pour la v1, `P0B/mandat-developpeur-programme-etapes-3-5-6-v1.md` (`59370f4a…`). Demande de la session de coordination : une version 2 sur la vérification du programme v1.
- Vérification de la v1 : `P0B/programme-3-5-6-v1/verification-v1/verification-programme-3-5-6-v1.md` (`5dae3b944c9c0f7bed575ad6c490a978f365613aa27dae5e81e34b5f761698d5`, vérifiée contre son compagnon). Verdict « À corriger », un seul point (§ 4), plus la recommandation d'ajouter cinq essais (§ 5).
- La v1 (`programme-3-5-6-v1/`) n'est pas touchée (règle R12).
- Fichiers rendus (sous-dossier `programme-3-5-6-v2/` du bloc-notes ; chacun a son compagnon) :

| fichier | empreinte |
|---|---|
| `lancer_etapes_3_5_6_v2.py` | **`1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14`** |
| `tests/test_lancer_etapes_3_5_6_v2.py` | `1830c842452a119458715566f5c73c1aa37135c5e00760ae16bb34ce36d26e7c` |
| `differentiel-programme-v1-v2.diff` | — |
| `differentiel-essais-v1-v2.diff` | — |
| `essais-v2.log` (premier jeu, 1 erreur, § 3) | — |
| `essais-v2-reprise.log` (jeu final) | — |
| ce rapport | — |
| `table-empreintes-programme-3-5-6-v2.txt` | — |

## 0. Verdict

La correction est faite **sans code v7 ni fonction neuve dans le paquet**. La condition 5 de la liste d'arrêt se lit par une comparaison sur les réglages que rend `etapes.etape_6`, à la lettre du texte. Les cinq arrêts nommés de l'étape 4 ont chacun leur essai.

**Essais : 30 passés, 0 échoué** (814 s), sous la seule couche « essai-de-forme ». Ce sont les 29 essais du programme et l'essai final « aucune graine décisive » du code v6.

Aucun refus de permission, de classifieur ni de garde.

## 1. La correction (vérification, § 4)

- **Le texte.** Liste d'arrêt, point 5 (v13:428 ; v15:436, inchangé) : « la taille de référence n'est atteignable, pour un contraste, à aucune dose non nulle ; ou la force de référence du suiveur de forme n'est pas atteignable » → « arrêt : le banc ne sait pas planter l'effet de référence ; ses valeurs se changent par un erratum contre-lu ». B7 : le contraste de l'héritage se règle par K, celui de la tenue par τ ; la référence est la taille 1 (« valeurs gelées », taille de référence) et la force 1 du suiveur.
- **Le programme v2** :
  - l. 78 : `ArretListeDArretPoint5`, la classe de l'arrêt ;
  - l. 82-97 : `liste_d_arret_point_5(reglages)`. Elle lit les réglages au format de `reglages_pour_le_plan` (None : non atteignable ; une clé absente compte comme non atteignable). Elle rend une cause dans trois cas :
    - K à la taille 1 n'est atteignable à aucune des deux doses non nulles ;
    - de même pour τ ;
    - φ à la force 1 n'est pas atteignable.

    C'est une comparaison, aucun calcul. Les autres tailles et forces, et γ, ne comptent pas.
  - l. 229 : les réglages que rend `EP.etape_6` sont gardés (la v1 les écartait) ;
  - l. 233-238 : si la condition est vraie, l'arrêt est écrit par le chemin `_arreter` : cause scellée (`arret.txt`), manifeste de l'étape 6 « arrêt », qui inscrit les fréquences vérifiées et l'empreinte du fichier des réglages, déjà gelé par `etape_6`. Le programme s'arrête alors, avec un code non nul.
- **Silence** (proposition marquée). Le texte ne dit pas à quelle étape ce point se lit. La v2 le lit à la fin de l'étape 6, qui en produit la donnée. Si la mère préfère qu'il soit lu ailleurs (étape 8, analyse), la v15 doit le dire. Un arrêt au point 5 laisse le fichier des réglages gelé et inscrit, pour l'erratum qui changerait les valeurs.

Différentiel complet : `differentiel-programme-v1-v2.diff`. Hors de ces lignes, seuls changent le docstring (version 2, nom du fichier dans l'usage) ; rien d'autre.

## 2. Essais ajoutés (cas sain et artefact, R5)

| essai | cas sain | artefact |
|---|---|---|
| `test_v2_liste_d_arret_point_5_a_la_lettre` | référence atteignable aux deux doses ; ou à une seule dose par contraste (doses différentes) : condition fausse ; tailles autres que 1 et γ non atteignables : sans effet | K non atteignable aux deux doses ; τ de même ; φ à la force 1 non atteignable ; K et τ ensemble (deux causes) ; clé de φ absente : condition vraie |
| `test_v2_point_5_artefact_k_et_tau_non_atteignables_arrete_l_etape_6` | — | l'artefact de la vérification : K et τ de référence non atteignables aux deux doses, φ atteignable (réglages plantés, `etape_6` remplacée le temps de l'essai, gel par la fonction du code v6). Résultat : arrêt de l'étape 6 écrit, cause « liste d'arrêt, point 5 » scellée, manifeste « arrêt » avec l'empreinte des réglages gelés, programme arrêté |
| `test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue` | référence atteignable à une seule dose par contraste, φ atteignable : étape 6 « tenue », aucun fichier d'arrêt | — |
| `test_v2_arrets_nommes_de_l_etape_4` (5 essais) | la chaîne entière | `ArretMecanique`, `ArretFrequences`, `DesaccordOrganisme`, `ArretGenerateur`, `ArretEtapes`, chacun planté : arrêt de l'étape 4 écrit et scellé, manifeste « arrêt », étapes 5 et 6 non jouées, aucun résultat de l'étape 4 |
| `test_chaine_entiere_reduite_sous_essai_de_forme` (changé, § 3) | étapes 3 à 5 « tenue » ; étape 6 « tenue », ou close « arrêt » par la seule cause du point 5, scellée ; fréquences et réglages gelés et inscrits | — |

Les autres essais de la v1 sont repris à l'identique : pièces, couche, tailles, dossier, copie de l'organisme, arrêts des étapes 3, 5 et 6, ligne de commande, essai final.

## 3. Constat d'essai, et ce que j'en ai fait

Au premier jeu (`essais-v2.log` : 29 passés, 1 erreur), la chaîne entière réduite s'est arrêtée à l'étape 6, au point 5 : « force de référence du suiveur de forme (1.0) non atteignable ». C'est la garde neuve qui joue, sur des données d'essai :
- couche « essai-de-forme » ;
- fréquences mesurées sur une source de deux proposeurs à la dose 0,5 ;
- 2 000 sources d'étalonnage.

C'est un constat d'essai, sans portée pour le palier (règle R4 : il est dit, il n'est pas lu). Il montre seulement qu'aux tailles d'essai le suiveur n'atteint pas sa force de référence ; rien ne dit qu'il en irait de même aux tailles gelées. Je n'ai pas cherché de tailles d'essai qui feraient passer la garde.

L'essai de la chaîne entière l'admet désormais : l'étape 6 y est close « tenue » ou « arrêt », et, dans ce dernier cas, par la seule cause du point 5, écrite et scellée. Tout autre arrêt fait échouer l'essai. Les deux lectures de la garde sont éprouvées à part, sur des réglages plantés. Au jeu final (`essais-v2-reprise.log`), **30 passés**.

## 4. Commande de lancement (NON LANCÉE, en attente)

```
env -C <RACINE>/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B <CHEMIN>/lancer_etapes_3_5_6_v2.py <TEXTE> <RACINE> <COPIE_DE_L_ORGANISME>/orchestrator <DOSSIER_NEUF>
```

Elle est inchangée hors du nom du fichier. La pièce de contrôle de la mère et le texte suivant doivent porter **l'empreinte de la v2**, `1f04cb46…`, à la place de celle de la v1 : le programme exige que la pièce de contrôle la porte.

## 5. Silences

Les dix silences du rapport v1 sont inchangés ; la vérification les juge justes ou les renvoie à la mère (n° 2 et 5). S'y ajoute **le n° 11** : le moment de la lecture du point 5 (fin de l'étape 6, § 1). Proposition marquée : à inscrire en v15.

## 6. Gestes, écarts

- Essais : `env -C <bloc-notes>/dev-palier-0b-v6/code-v6 PYTHONPATH=src HERITAGE_DEPOT=… HERITAGE_COPIE_ORGANISME=… /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider <v2>/tests/test_lancer_etapes_3_5_6_v2.py <code-v6>/tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`. Ils tournent sur la copie du code v6 du bloc-notes, égale à la table `639335b9…`.
- Deux jeux. Le premier a eu 1 erreur, le constat du § 3 ; son journal est gardé. Le second est le jeu final, après le seul changement de l'essai de la chaîne ; le programme n'a pas changé entre les deux.
- Aucune commande de liste ni de recherche de processus ; aucune commande d'arrêt ; aucune graine décisive ; aucune couche réelle ; aucune écriture dans le dépôt ; aucun commit ; aucun appel à un fournisseur ; aucune dépense.
- Écart : les deux variables d'environnement des essais, comme pour la v1.

Développeur, modèle O.
