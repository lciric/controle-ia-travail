# Vérification du code d'appel de l'étage 2, version 4 (ligne 3, organisme v9) — v1

Pièce d'instrument (classe B), écrite le 2026-11-20 par le contre-lecteur, modèle S, même mandat (`5bf7858c…`, en-tête compris). Elle vérifie le seul différentiel v2 → v4 (v2 déjà jugée « Conforme », `829d0441…` ;
la v3, `969653f2…`, est un état intermédiaire que la v4 reprend : son texte figure dans l'en-tête de la v4). Aucun appel, aucune dépense, aucune clé lue, aucun relais lancé, mode réel jamais lancé.

## Verdict

**Conforme.** Rien ne change hors de la liste blanche, de l'exigence du mandataire, des essais qui les éprouvent et des en-têtes. Aucune correction.

## 1. La table

`code-appel-v4/` : `sha256sum -c` de la table (`49afc8d4…`) : six lignes OK ; compagnon de la table OK. Programme `082d19d6…`, essais `072439a0…`, rapport `96871f49…`, chacun égal à son compagnon.

## 2. Essais rejoués

Sur une copie de `code-appel-v4/` dans mon dossier (`copie-v4/`), commande du mandat, en tâche de fond : **98 passed in 139.32s**, aucun échec, aucun saut (98 attendus).

## 3. Différentiels v2 → v4, refaits par moi

`diff -u` redirigés vers `diff-programme-cl-v2-v4.txt` et `diff-essais-cl-v2-v4.txt` (mon dossier).

**Programme** : quatre changements, tous déclarés. (1) En-tête (texte des v3 et v4 ajouté) et `VERSION = "epreuve_juges_reels_ligne_3_v4"`. (2) `VARIABLES_PERMISES` élargie du mandataire (`HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY` et leurs minuscules) et des
certificats (`SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`, `NODE_EXTRA_CA_CERTS`) ; **aucun nom de clé** (lu : la liste en compte dix-huit, aucune ne contient `KEY`, `TOKEN` ni `SECRET`). (3) `VARIABLES_EXIGEES = ("HTTPS_PROXY",)`.
(4) Dans `exiger_environnement_epure`, refus nommé si une variable exigée manque, après le refus hors liste. Rien dans la garde des noms de clé (`preparer_reel`, expression régulière inchangée, appelée avant l'environnement épuré),
ni dans le compteur, le plafond, le plan, les gardes C1 à C3, le dépôt, le chemin réel ou les constantes épinglées.

**Essais** : lignes retirées de la v2 : le docstring (une ligne), l'import, et quatre retouches de cas : (a) les cas du mode réel passent `dict(ENV_BASE, **env)` et le départ sain `dict(ENV_BASE)` au lieu de `{}` (HTTPS_PROXY factice : première retouche déclarée) ;
(b) `test_environnement_epure_sain_et_artefact` : le sain porte `ENV_BASE` ; `exiger_environnement_epure({}) == []` devient `exiger_environnement_epure(dict(ENV_BASE)) == ["HTTPS_PROXY"]` (conséquence nécessaire de l'exigence : un environnement vide est désormais refusé ;
le refus d'un environnement sans `HTTPS_PROXY` est éprouvé par `test_v3_depart_reel_exige_https_proxy`) ; (c) l'artefact « mandataire refusé » devient `ALL_PROXY` (seconde retouche déclarée) ; (d) `test_mode_reel_environnement_liste_blanche_accepte` porte `**ENV_BASE`.
La retouche (b) sur `{}` n'est pas nommée au rapport mais découle de la même exigence ; sans effet sur la force des essais. Tout le reste de la v2 est inchangé (les 85 essais de la v1 et les 8 essais C1 à C3 et environnement : non touchés, sauf par ces retouches).
Ajouts : `test_v3_depart_reel_exige_https_proxy`, `test_v3_liste_blanche_elargie` (dix noms permis, les deux noms de clé absents de la liste, exigée = `HTTPS_PROXY`, refus hors liste gardé), `test_v4_aucun_nom_de_cle_mandataire_present_depart_accepte`, `test_v4_nom_de_cle_present_refus_nomme` (deux paramètres).
Soit 93 + 5 = 98.

## 4. Départ sain sans nom de clé, artefact refusé pour chaque nom (ma démonstration)

`demo_environnement_cl_v4.py` (sortie `sortie-demo-environnement-cl-v4.txt`), par `preparer_reel` avec registre et constructeur factices, sur le module v4 :
- **accepté** : mandataire, certificats, `PATH`, `HOME`, `GO_ID`, aucun nom de clé ; et `HTTPS_PROXY` seul ;
- **refusé** : `RR_ANTHROPIC_API_KEY_LUC` (refus nommé « noms de variables de clé… »), `GEMINI_API_KEY` (idem), les deux ensemble, `GITHUB_TOKEN` ; sans `HTTPS_PROXY` (même avec `https_proxy` seul) : « variables exigées absentes » ; environnement vide : idem ; `ALL_PROXY` et `PYTHONPATH` : « hors de la liste blanche » ;
- deux services construits exactement (les deux départs sains), aucun pour les refus.
Les deux refus de noms de clé tombent par la garde des noms de clé (inchangée, avant la liste blanche) ; la liste blanche les refuserait aussi (essai du développeur).

## 5. Remarques, sans correction

- Les noms du mandataire et des certificats ne sont pas des noms de clé au sens de la garde (aucun `API_KEY`, `TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIAL`) : ils passent, comme voulu. Les valeurs ne sont jamais lues par ce programme.
- Le programme garde la présence de `HTTPS_PROXY` seule ; `HTTP_PROXY`, `NO_PROXY` et les certificats sont permis, non exigés. Des relais ou sondes locales en `http://127.0.0.1` n'emploient pas `HTTPS_PROXY` ; leur passage dépend de `NO_PROXY` ou de `HTTP_PROXY` absent, ce que la procédure de départ de l'additif vérifiera au premier appel à blanc des relais (`porte_a_blanc`). Je n'ai pas exécuté ce chemin.
- Le départ réel reste non exercé de bout en bout (inchangé depuis la v1).

## 6. Mes écarts

Copie de `code-appel-v4/` dans mon dossier ; `diff -u` redirigés vers des chemins complets de mon dossier ; ma démonstration importe le module copié (interpréteur de `.venv`, `-I -B`) et a laissé `demo-env-v4/` dans mon dossier. Aucune sortie hors de mon dossier ; aucun refus de permission, de classifieur ni de garde.

Contre-lecteur, modèle S.
