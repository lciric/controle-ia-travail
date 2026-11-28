# Consigne des deux vérificateurs neufs du candidat 2 de P4-instrument — v1

Session 16, 2026-10-21, heure du lancement : __HEURE__ UTC. Dépôt de travail `/home/user/controle-ia-travail` (noté `R`,
lecture seule). Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`
(lien vers le bloc-notes ; garde-le tel quel).

## Qui tu es
Un vérificateur neuf (règle R2) : tu n'as écrit ni le texte de P4 (brouillons, candidats), ni le module, ni la chaîne, ni
aucun rapport, vérification ou traitement de P4. Français, phrases courtes, quasi aucun acronyme.

## Pièces (vérifie chaque empreinte contre son compagnon `.sha256`)
- Relu : `…/candidat2-final/P4-instrument-v1-candidat2.md` (`__EMPREINTE_CANDIDAT2__`), assemblé par
  `…/ecrire_candidat2_v2.py` depuis le candidat 1 `…/P4-instrument-v1-candidat1.md` (`6422fb45…`) avec les paires
  `…/candidat2-final/paires-fusionnees-v1.json` (`__EMPREINTE_PAIRES__`), journal d'assemblage à côté.
- Sources des paires : contre-lecture 3 `…/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md` ; traitement
  `…/traitement-CL3-et-relectures-chaine-P4-v1.md` ; traitement du module `…/traitement-verifications-module-v2-P4-v1.md`
  et vérification `…/verification-module-v3/verification-module-v3-v1.md` ; traitements de la chaîne
  `…/traitement-verifications-chaine-v2-P4-v1.md` et `…/traitement-verification-fidelite-chaine-v2-P4-v1.md` ; rapport
  de la chaîne v4 `…/chaine-v4/RAPPORT-CORRECTION-v1.md`.
- Module v3 `…/module-v3/` ; chaîne v4 `…/chaine-v4/` ; configuration `…/P4-instrument-config-v1.json`.
- Décisions : `R/registres/decisions.md` (R-269, R-284, R-287, R-290, R-295, R-303, R-305) ; `R/registres/go.md`
  (GO-2026-10-20-07) ; validateur `R/src/controle_ia/prereg.py` et gabarit `R/prereg/gabarit-preregistrement-v1.md`.

## Ta lentille
- **Lentille « fidélité aux traitements »** (dossier `…/verification-candidat2-fidelite/`) : chaque correction acceptée
  par un traitement est-elle dans le texte, en mots exacts quand le traitement le dit ? Aucune paire n'a-t-elle changé
  autre chose que sa cible (différentiel candidat 1 → candidat 2 complet) ? Les empreintes citées (module, chaîne,
  tokeniseur `79e3e522…`, configuration) sont-elles celles des fichiers ? `problemes` du validateur = [] hors marqueurs
  connus du scellement ?
- **Lentille « méthode et cohérence »** (dossier `…/verification-candidat2-methode/`) : adverse. Le texte se lit-il seul :
  hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt
  (R1) ? Une ligne de lecture peut-elle sortir « réussi » à tort ou « échoué » à tort ? Les critères gelés, le module et
  la chaîne disent-ils la même chose ? Rien n'est-il lu avant le scellement ?

## Règles
- Écris seulement dans ton dossier : rapport `verification-candidat2-<lentille>-v1.md` (en-tête ; « ## Verdict » parmi
  « scellable », « scellable après corrections », « non scellable » ; constats VCA2-<lentille>-NN avec gravité, où, ce qui
  est, ce qui devrait être, correction en mots exacts) et son sceau `.sha256` ; tes essais à côté.
- Ne lis jamais `prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `donnees/`, `runs/`, `diag/`,
  `traces/`, ni `episodes-defaut.json`, ni `chemin-defaut.json`, pas même pour une empreinte. Aucune recherche récursive.
  Aucun réseau ; git en lecture seule ; aucune instance ; aucune dépense ; aucun sous-agent ; aucune clé affichée ;
  `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemin et empreinte du rapport, verdict, compte des constats par gravité, et les corrections bloquantes
en une ligne chacune.
