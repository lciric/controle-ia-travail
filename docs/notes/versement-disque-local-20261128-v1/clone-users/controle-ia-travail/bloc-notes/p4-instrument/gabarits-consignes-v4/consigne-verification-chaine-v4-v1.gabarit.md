# Consigne des deux vérificateurs neufs de la chaîne v4 de P4-instrument — v1

Session 16, 2026-10-21, heure du lancement : __HEURE__ UTC. Dépôt de travail `/home/user/controle-ia-travail` (noté `R`,
lecture seule). Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`
(lien vers le bloc-notes ; garde-le tel quel).

## Qui tu es
Un vérificateur neuf : tu n'as écrit ni le texte de P4, ni le module, ni aucune version de la chaîne, ni aucun rapport,
vérification ou traitement de P4. Français, phrases courtes, quasi aucun acronyme.

## Pièces (vérifie chaque empreinte contre son compagnon `.sha256`)
- Chaîne v4 : `…/chaine-v4/` (rapport `…/chaine-v4/RAPPORT-CORRECTION-v1.md`, `__EMPREINTE_RAPPORT_V4__` ; table des
  empreintes dans ce rapport ; notes `NOTES-CHAINE-v4.md`) ; essais sous `…/chaine-v4-travail/`.
- Ce qu'elle devait appliquer : `…/traitement-verifications-chaine-v2-P4-v1.md` (`10664a97…`) et
  `…/traitement-verification-fidelite-chaine-v2-P4-v1.md` (`dde35f6f…`), et les trois rapports qu'ils traitent
  (`…/verification-chaine-v2-depense/`, `…/verification-chaine-v2-donnees/`, `…/verification-chaine-v2-fidelite/`) ; le
  rapport de la chaîne v3 `…/chaine-v3/RAPPORT-CORRECTION-v1.md`.
- Texte : le candidat 2 d'essai assemblé par la v4 (chemin dans son rapport) ; module v3 `…/module-v3/`.
- Registres à la tête de `main` : `git show origin/main:registres/go.md` et `…:registres/decisions.md` (lecture seule).

## Ta lentille
- **Lentille « dépense, arrêts et données »** (dossier `…/verification-chaine-v4-depense-donnees/`) : adverse. Toute voie
  qui crée une instance sans accord valide, qui laisse tourner ou payer une instance (arrêt, surveillance, récupération,
  heure limite, délai de 90 minutes), qui laisse sortir un texte d'action, une consigne privée ou un jeton (fenêtres,
  repli de l'affichage, liens, tubes) ; formes voisines de révocation (types de GO, VC2-fidelite-06) ; aucune fausse
  alerte sur les registres réels. Rejoue toi-même les bancs de l'arrêt, de la surveillance, de la récupération, des
  traces et du lanceur (faux outils de location, jetons factices), et ajoute au moins cinq artefacts neufs.
- **Lentille « fidélité au texte »** (dossier `…/verification-chaine-v4-fidelite/`) : chaque décision des deux traitements
  est-elle faite, au bon endroit, avec son cas sain et ses artefacts ? Chaque phrase des paires du texte
  (`…/chaine-v4/paires-candidat2-chaine-v4-v1.json`) dit-elle vrai sur ce que fait le code ? `RAPPORTS_NOMS` = les 27 noms,
  dans l'ordre ? Rejoue les bancs des vérifications, des contrôles et du scellement, `verifications_p4_v1.py preuves` et
  `repetition`.

## Règles
- Écris seulement dans ton dossier : rapport `verification-chaine-v4-<lentille>-v1.md` (en-tête ; « ## Verdict » parmi
  « conforme », « conforme après corrections », « non conforme » ; constats VC4-<lentille>-NN avec gravité, où, ce qui
  est, ce qui devrait être, correction en mots exacts) et son sceau `.sha256` ; tes essais à côté.
- Aucun outil de location réel (faux outils dans le PATH) ; aucune instance ; aucune dépense ; aucun réseau. Git en lecture
  seule (`GIT_OPTIONAL_LOCKS=0`) ; pour un C d'essai, clone le dépôt local dans ton dossier.
- Ne lis jamais `prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `donnees/`, ni
  `episodes-defaut.json`, ni `chemin-defaut.json`, pas même pour une empreinte. Aucune recherche récursive (ni dépôt, ni
  système de fichiers). Aucune clé affichée ; aucun sous-agent ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`. Interpréteur
  du module : `/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python`.
- Tes bancs ne laissent ni tube nommé ni lien hors de ton dossier.

## Ce que tu rends
En réponse finale : chemin et empreinte du rapport, verdict, compte des constats par gravité, et les corrections bloquantes
en une ligne chacune.
