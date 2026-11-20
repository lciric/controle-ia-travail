# Vérification du code d'appel de l'étage 2, version 2 (ligne 3, organisme v9) — v1

Pièce d'instrument (classe B), écrite le 2026-11-20 par le contre-lecteur, modèle S, même mandat (`5bf7858c…`, en-tête compris) ; vérification des corrections C1 à C3 de
`contre-lecture-code-appel-etage-2-v1.md` (`4bcab58a79459e66711bfb1105f833c8453448d2d93ef1fa06efe658b5628f98`). Aucun appel, aucune dépense, aucune clé lue, aucun relais lancé, mode réel jamais lancé.
Par consigne de la coordination, **je ne juge pas la liste blanche d'environnement de la v2** (la v3 la reprend) ; je n'en rends que les faits relevés (§ 6).

## Verdict

**Conforme** pour C1, C2 et C3, et pour le reste du différentiel : rien d'autre ne change que ce qui est déclaré.

## 1. La table

`code-appel-v2/` : `sha256sum -c` de la table (`e06fb39f…`) : six lignes OK ; compagnon de la table : OK. Programme `1a0b08d5…`, essais `b1767abb…`, rapport `f79a5707…`, chacun égal à son compagnon.

## 2. Essais rejoués

Sur une copie de `code-appel-v2/` dans mon dossier (`copie-v2/`), commande du mandat, en tâche de fond : **93 passed in 124.41s**, aucun échec, aucun saut (93 attendus).

## 3. Différentiel, refait par moi

`diff -u` v1 → v2 du programme et des essais, redirigés vers `diff-programme-cl-v1-v2.txt` et `diff-essais-cl-v1-v2.txt` (mon dossier). Le différentiel du programme est identique à celui du rapport § 6.1 : en-tête, nom de version,
constantes `VARIABLES_PERMISES` et `NOM_DE_VARIABLE`, bloc `if relance:` (C1), clé `"plomberie"` à l'ouverture (C1), branche de rejeu du contrôle de plomberie (C3), `exist_ok=True` (C2),
`exiger_environnement_epure` et son appel, contrôle de forme de `--nom-cle-claude`, texte d'usage. Rien dans le compteur, le plafond, le plan, la classification des retours, le dépôt ni le chemin réel (`construire_service_reel`). Les essais :
deux lignes retirées seulement (la première ligne du docstring et l'import) ; tout le reste est ajouté : les 85 essais de la v1 ne sont pas affaiblis.

## 4. C1 à C3, lus et éprouvés

- **C1 : conforme, texte repris à la lettre.** Les deux refus et la clé `"plomberie"` sont ceux que j'ai écrits. Ma démonstration de la première passe (relance sur une autre banque, qui était acceptée) est rejouée contre la v2 par
  `demo_relance_autre_banque_cl_v2.py` : « relance sur autre banque REFUSEE », journal inchangé par le refus (octets égaux), puis relance saine sur la même banque : 1 005 envois, 45,3783 USD, aucun arrêt
  (sortie `sortie-demo-relance-autre-banque-cl-v2.txt`). Essais du développeur : sain, autre banque, autre plomberie, rendu hors du plan.
- **C2 : conforme.** `dossier.mkdir(parents=True, exist_ok=True)` ; l'essai laisse un dossier sous le premier identifiant tiré à la relance et la relance part (rejeu en essai 2 sous cet identifiant). Le dossier n'a jamais servi (aucun
  engagement, aucun envoi) : réutiliser son nom ne contredit pas « identifiant jamais repris » (qui porte sur les identifiants engagés au journal).
- **C3 : conforme.** Le contrôle `motif_plomberie` est rejoué, sans envoi, sur tout rendu de plomberie fini dont le juge n'est pas arrêté, avant le `continue`. Lu : dans une exécution normale, un rendu de plomberie n'est jamais fini quand
  on l'atteint, donc la branche ne joue qu'à la relance. Essai du développeur : panne forcée entre le règlement du second rendu et son contrôle ; artefact (plomberie illisible) : arrêt à la relance, 2 envois, aucun du bloc A ; sain : 1 004 envois.
  Je note, sans correction : l'essai ne couvre pas la variante « coût au-dessus de trois fois le tarif » du même contrôle ; elle passe par la même fonction `motif_plomberie`, déjà essayée seule en v1.
- **Reste de la v2** : reproduction du calcul v2 rejouée en entier par les essais (les 85 de la v1) ; nom de clé de forme contrôlée seulement, aucune valeur lue (`nom_cle_claude` refusé minuscule ou d'une lettre, accepté `NOM_VALIDE_1`, essayé par moi) ;
  racine 2026111935 clé 4 inchangée ; « tout refusé » inchangé.

## 5. Ce que je n'ai pas à corriger

Aucune correction. Une remarque pour l'additif : l'essai `test_c3` remplace `motif_plomberie` par un `monkeypatch` le temps de la première exécution (déclaré au rapport § 5, point 3) ; c'est un procédé d'essai, il ne touche pas le programme.

## 6. Liste blanche (faits seulement, pas de jugement sur la v2)

Faits relevés dans mes essais : avec `HTTPS_PROXY` présent, `preparer_reel` refuse avant tout service (« variables hors de la liste blanche ») ; un environnement vide ou limité à la liste passe ; `PYTHONPATH` est refusé ; un nom
de la forme `*_TOKEN` est refusé plus tôt, par le contrôle de noms de clé. Faits lus dans le code, utiles à la v3 : (a) le programme lui-même ne fait aucun appel réseau (`git show`, lecture de fichiers, sous-processus locaux) ; (b) la commande
d'Argon v3d construit un ouvreur sans mandataire pour une adresse locale (`ouvreur(local)`, `ProxyHandler({})`) et l'adaptateur à commande externe ne lui passe que `PATH`, `HOME`, `LANG`, `LC_ALL`, `TMPDIR` plus les variables
transmises ; (c) les relais sont des processus à part, contrôlés par PID : leur environnement et leur sortie réseau ne passent pas par ce programme, que je n'ai pas lu (lanceur de relais) ; (d) l'adaptateur du kit Claude construit
l'environnement de l'agent avec `variables_agent(url_relais)` (non lu). Je ne tranche pas : la mère a déjà jugé la question et la v3 la traite.

## 7. Mes écarts

Lectures par motif sur des fichiers nommés un à un ; copie de `code-appel-v2/` dans mon dossier ; `diff -u` des deux couples de fichiers redirigés vers des chemins complets de mon dossier ; mon programme de démonstration importe le module copié
(interpréteur de `.venv`, `-I -B`) et a laissé `demo-relance-v2/` dans mon dossier. Aucun refus de permission, de classifieur ni de garde. Aucune sortie hors de mon dossier (redirections vers chemins complets).

Contre-lecteur, modèle S.
