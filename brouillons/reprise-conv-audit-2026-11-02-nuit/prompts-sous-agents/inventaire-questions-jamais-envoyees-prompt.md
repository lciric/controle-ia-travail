Tu es un lecteur neuf : tu n'as écrit aucune des questions ni aucun des registres que tu vas lire. Français, sans sigle non développé ; heures par `date -u`.

## La question de Lazar (3 novembre 2026, 11:36 heure de Paris, verbatim)
« d'autres questions scellées pour collisionneur ou course idéation qui traînent et jamais envoyées ? »

## Ce que tu établis
Pour chaque question écrite pour le **collisionneur** (tours de plusieurs espèces), pour **Argon seul** ou pour une **course d'idéation de l'organisme**, son sort, avec la preuve (ligne de registre « CA R-n » ou « SD R-n », message de canal, ou fichier de sortie, avec son chemin) :
- **(a) jouée et finie** (cellules, réponses ou fiches rendues ; synthèse ou lecture s'il y en a) ;
- **(b) lancée mais arrêtée** (refus, plafond, panne), et si une reprise a eu lieu ;
- **(c) écrite et scellée, jamais lancée** : aucune trace de devis, de GO, de lancement ni de sortie ; dis si elle a été envoyée à session-depot (numéro du message) et ce qui l'a bloquée si un registre le dit (GO non donné, remplacée, mot de Lazar, dépense) ;
- **(d) remplacée** par une autre version ou une autre question qui, elle, a tourné (laquelle) ;
- **(e) hors champ** : ce n'est pas une question pour le collisionneur, Argon ou une course (pièce, consigne, question pour les « organismes » de Gemini que Lazar fait tourner lui-même, données brutes `gemini/`).
Ne juge pas l'intérêt d'une question : établis seulement son sort. Une question sans preuve dans un sens ni dans l'autre est classée « indéterminée », avec ce que tu as cherché.

## Matériaux (tous locaux ; dépôt `/home/claude/controle-ia-travail`)
- Point de départ : `/home/claude/scratch/inventaire-questions/inventaire-v1.json` (liste des fichiers « question* » des trois arbres, avec empreintes et mentions trouvées par un premier script ; son indice « lancement » est **peu fiable** : ne t'y fie pas). Les scripts `inventaire_v1.py`, `fins_v1.py`, `sorties_v1.py` du même dossier montrent ce qui a déjà été cherché.
- Arbres, par `git -C /home/claude/controle-ia-travail show <ref>:<chemin>` et `ls-tree` : `HEAD` (branche `canal/conv-audit-n04` : registre de conv-audit `registres/decisions.md`, messages `brouillons/canal-reprise-releve-v1/messages/conv-audit_*.md`) ; `origin/main` (registre de session-depot `registres/decisions.md`, `docs/notes/**`) ; `origin/canal/session-depot-reprise-n139` (messages de session-depot `brouillons/canal-reprise-releve-v1/messages/session-depot_*.md`, copies `envois/session-depot/**`) ; les autres branches `origin/canal/session-depot-reprise-n*` si besoin.
- Les sorties des tours sont souvent sur des branches `donnees/…` : **tu ne les lis pas** (la preuve d'une fin est alors la ligne de registre qui dit « fini », « rendu », « versé », ou une synthèse sur `main`).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; **rien sous `donnees/`**, aucune référence `donnees/*` lue ni listée ; aucun `git fetch` ; aucun appel de réseau ni de modèle ; `nice -n 10` pour les scripts. Tu écris seulement dans `/home/claude/scratch/inventaire-questions/`.

## Rendu
Fichier `/home/claude/scratch/inventaire-questions/sort-des-questions-v1.md` : un tableau (question, version et empreinte courte, date, destinataire, sort (a) à (e) ou indéterminé, preuve, ce qui l'a bloquée). Réponse finale : **la liste des questions de la classe (c)**, une ligne chacune (fichier, date, sujet en dix mots, envoyée ou non à session-depot, cause du blocage si connue) ; puis les comptes par classe ; puis les indéterminées ; le sha256 de ton fichier.
