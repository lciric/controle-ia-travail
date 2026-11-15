# Essais à blanc de l'amorce sans ssh du pilote MR-2 — v1 (procédure v11)

Compte organisme, modèle A. **Aucun appel à un fournisseur, aucune clé réelle, aucun réseau extérieur, aucune dépense.** Joués sur un
dossier jetable de la session (hors de tout dépôt), le @DATE_ESSAIS@.

## Ce qui est joué

- **Dépôt distant** : un dépôt nu local (`file://`, filtres et envois par empreinte permis, comme le dépôt distant), qui porte trois
  branches synthétiques aux mêmes chemins que le dépôt de travail : `lot/compte-organisme-v1` (le vrai paquet de l'arbre `e3d83e47…`,
  le vrai dossier de la sonde v74, les pièces de `sans-ssh-v1/`), `prep/pilote-mr2-compte-organisme-v1` (le vrai texte scellé
  `8aa33014…`), `main` (le vrai `registres/go.md`). La mère du banc y inscrit les empreintes (fichier `registres-essai/inscriptions.md`
  du `main` synthétique) avant chaque feu.
- **Loueur** : `doublure_vast_v1.py` (consigne méthode, chemin, présence de l'en-tête d'autorisation, jamais sa valeur).
- **Mère** : jouée par `essai_amorce_v1.py` **au moyen de l'outil de la session** (`feu-phrase`, `feu-mondes`, `feu-reel`,
  `feu-relance`, `feu-arret`, `etat`) ; deux feux faux sont écrits sans l'outil (même forme de commit) pour éprouver les refus.
- **Lanceur** : `doublure_lanceur_v1.py` (formes de sortie de `repetition-locale/`, codes du scénario ; `bloc` et `secret` délégués au
  vrai lanceur de l'arbre) ; le scénario `sain-integral` joue le **vrai lanceur v74** de bout en bout, le pilote « réel » en mode à
  blanc (seul écart : le mode réel refuse toute configuration autre que la gelée).
- **Clés** : valeurs factices ; après chaque scénario, toute la branche de sortie (tous ses commits) est fouillée pour les quatre
  valeurs factices (brutes et en base64), le secret tiré (brut et hexadécimal) et la phrase de répétition ; et pour les noms interdits
  (`secret.bin`, `phrase.txt`, `MONDES.json`, `cle-phrase.pem`, `prive/`, textes servis).
- Les processus d'un scénario sont arrêtés à sa fin par l'identifiant du groupe de processus créé par le banc (R10).

## Rejouer

```
cd sans-ssh-v1/essais
python3 -B essai_amorce_v1.py DOSSIER_JETABLE resultats.json                  # scénarios rapides (doublure du lanceur)
python3 -B essai_amorce_v1.py DOSSIER_JETABLE resultats.json sain-integral    # vrai lanceur, ≈ 15 min sur 4 processeurs
python3 -B essai_outil_session_v1.py DOSSIER_JETABLE resultats.json            # outil de la session
```

Environnement : @ENVIRONNEMENT@.

## Résultats (scellés, à côté)

@TABLE_RESULTATS@

## Ce que les essais ne prouvent pas

La création chez le loueur et sa lecture réelle de `--env` et de `--args` (la commande imprimée par l'outil a été jouée sur une
doublure de l'outil du loueur, qui a reçu les arguments attendus, `--env` en treize affectations, l'amorce égale à l'octet après
décodage) ; l'interface d'autodestruction du loueur ; le clonage par jeton depuis la machine et la poussée de la branche de sortie sur
le dépôt distant ; la poussée de la branche d'entrée depuis la session (mandataire) ; l'image `python:3.13-bookworm` ; les appels
réels ; le pire cas de durée.
