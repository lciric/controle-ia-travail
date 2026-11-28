# Consigne du préparateur neuf du versement C de P4-instrument — v1

Session 16, 2026-10-21 vers 00:40 UTC (heure vraie). Dépôt de travail `/home/user/controle-ia-travail` (noté `R`, lecture
seule pour toi). Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`
(lien vers le bloc-notes ; garde-le tel quel).

## Qui tu es
Un préparateur neuf : tu n'as écrit ni le texte de P4, ni le module, ni la chaîne, ni aucun rapport. Tu prépares, **sans
rien écrire dans le dépôt**, l'arbre exact que la session versera en un commit « C » (le candidat versé), pour gagner du
temps : la chaîne v4 et le candidat 2 relu ne sont pas encore écrits ; tout le reste l'est.

## Ce que tu fais
1. Établis la **liste exacte** des fichiers et chemins que C doit contenir, d'après ce que les scripts exigent : lis
   `…/chaine-v3/sceller_p4_v1.sh`, `…/chaine-v3/controles_avant_depense_p4_v1.sh`, `…/chaine-v3/verifications_p4_v1.py`
   (`RAPPORTS_NOMS`, chemins exigés), `…/chaine-v3/NOTES-CHAINE-v3.md` et `…/chaine-v3/RAPPORT-CORRECTION-v1.md` s'ils
   existent, `…/plan-code-et-chaine-v2.md`, et le candidat 1 `…/P4-instrument-v1-candidat1.md` (sections qui citent des
   chemins du dépôt). Liste de 27 rapports et brouillons : `…/traitement-verification-fidelite-chaine-v2-P4-v1.md`
   (`dde35f6f…`), section « Liste `RAPPORTS_NOMS` de la chaîne v4 ».
2. Construis l'arbre de préparation sous `…/versement-C-preparation/arbre/`, à l'image des chemins du dépôt (`prereg/…`,
   `prereg/contre-lectures/…`, `donnees/P4-tokeniseur-v1/…`, code du module, `docs/…`), en **copiant** chaque pièce qui
   existe déjà sous son nom final : rapports (source dans le bloc-notes, renommés selon la liste), brouillons 1 à 4,
   candidat 1, configuration `…/P4-instrument-config-v1.json`, module v3 (`…/module-v3/`), tokeniseur
   (`…/tokeniseur/tokenizer.json` `79e3e522…` et `tokenizer_config.json` `177c7b61…`). Chaque copie garde l'empreinte de
   sa source (vérifie-la contre le compagnon de la source quand il existe) et reçoit un compagnon `.sha256` à son nom final.
3. Écris `…/versement-C-preparation/TABLE-VERSEMENT-C-v1.md` : une ligne par fichier de C (chemin dans le dépôt ; source
   dans le bloc-notes ; empreinte ; « prêt » ou « attend : chaîne v4 », « attend : candidat 2 relu », « attend :
   vérification de la chaîne v4 », « attend : vérification du candidat 2 ») ; puis la liste des **pièces manquantes ou
   ambiguës** (deux sources possibles, empreinte qui diffère, nom absent) ; puis les commandes exactes que la session
   jouera pour verser (copie de l'arbre dans le dépôt, `sha256sum -c`, `git add` des chemins listés), **sans les jouer**.
4. Vérifie que les fichiers déjà présents dans `R/prereg/contre-lectures/` (lecture par `ls` de ce seul dossier) ne
   créent aucun conflit de nom avec la famille « P4 » exigée par les contrôles.

## Règles
- Écris seulement sous `…/versement-C-preparation/`. Ne modifie aucune source. **Aucune écriture dans le dépôt**, aucune
  commande git d'écriture (`GIT_OPTIONAL_LOCKS=0` pour les lectures).
- Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `R/donnees/`, `R/runs/`,
  `R/diag/`, `R/traces/`, ni `episodes-defaut.json`, ni `chemin-defaut.json`, pas même pour une empreinte. Aucune
  recherche récursive dans le dépôt ni dans le système de fichiers (lis par chemin ; `ls` d'un dossier nommé permis).
- Aucun réseau ; aucun sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemin et empreinte de la table ; nombre de fichiers prêts et en attente ; la liste des pièces
manquantes ou ambiguës ; les commandes de versement.
