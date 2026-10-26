# Brief — relecture indépendante du script de lecture contre le bruit du pilote 4 — v1

Écrit par la lignée conv-audit le 26 octobre 2026 à 03:42 UTC (heure lue sur `date -u`) pour un sous-agent neuf, qui n'a
écrit ni le script, ni ses essais, ni le texte du pilote, ni le noyau. Langue : français, sans acronymes. Le script sera
exécuté par une autre lignée sur des données réelles que personne ne doit voir avant une décision : une erreur de calcul ou
une fuite dans sa sortie ne se rattraperait pas. **Ton rôle est de chercher ce qui est faux**, pas de confirmer.

## Ce que tu relis (lecture seule ; tu travailles sur une copie)
- Le dossier du script : `/var/tmp/lecture-pilote4-v1/` (`lire_pilote4_v1.py`, `essais_lire_pilote4_v1.py`, le journal des
  essais, `LISEZMOI-script-lecture-v1.md`, les compagnons `.sha256`). Copie-le d'abord dans
  `/var/tmp/relecture-script-lecture-pilote4-v1/copie/` et ne travaille que sur la copie.

## Ce qui fait foi pour la relecture
1. Le brief que l'auteur du script a reçu : `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/lecture-pilote4-v1/BRIEF-script-lecture-pilote4-v1.md`
   (empreinte `c86be1a17e1f394ca91c1e0e24cc157eff8e580528e4380347346ea458f87f3e`).
2. Le texte du pilote : `/home/claude/pilote4/essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md` (empreinte
   `782b858c537222245fd757c23ea6d75abae142df029eed3e53af36d8c78cfa95`), § Plan, **points 3, 4 et 4 bis** ; en cas d'écart
   entre le brief et le texte, **le texte prime** : signale l'écart.
3. Pour la forme réelle des données (lecture seule) : `/home/claude/pilote4/essaim-m3-refonte-v1/essaim_m3/noyau/taches.py`
   (`evaluer`, `wilson_inferieur`, `parser_reponse_tache`), `…/noyau/boucle.py` (l. 700–800), `…/noyau/archive.py`
   (l. 110–150), `…/essaim_m3/banque.py` (l. 1–60 et 150–225), le lanceur
   `/home/claude/pilote4/essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/lancer_pilote4_gemini_v10.sh` (l. 860–900 :
   construction de `ferme.tar.gz`), et les deux scripts de références de la banque
   `/home/claude/banque-v2/essaim-m3-refonte-v1/banque/construction-v3/reference_provenance_conscience_v1.py` et
   `reference_contraste_paires_v2.py` (code seulement).

## Ce que tu vérifies (au moins)
1. **Conformité** : chaque point du brief et des points 3 à 4 bis du texte est fait, ou son absence est déclarée.
2. **Calculs**, refaits par toi indépendamment sur des exemples de ton choix (cas limites compris : classe vide, tout
   juste, tout faux, non-réponses) : exactitude équilibrée selon le noyau ; bornes de Wilson au niveau 97,5 % bilatéral et
   leur moyenne ; borne basse maximale à un score parfait ; test de McNemar exact bilatéral sur les paires discordantes ;
   seuil provisoire à une course ; correction de Holm à deux courses (et à une seule famille de tests si une course
   manque) ; comptes de la règle « catégorie absente du train » comparés au code des références de la banque.
3. **Fuites** : la sortie standard et la sortie d'erreur ne portent aucun score, aucune proportion, aucun nombre décimal,
   dans tous les chemins (succès, refus, exceptions non prévues) ; les fichiers écrits ne portent aucun identifiant de
   tâche, aucun texte, aucune vérité ni réponse par tâche ; rien n'est écrit hors du dossier de sortie, ni dans un dossier
   temporaire du système ; aucun fichier n'est écrasé.
4. **Archive** : ouverte en mémoire ; refus des membres qui ne sont pas des fichiers ordinaires (liens, périphériques),
   des chemins absolus ou remontants, des noms en double ; comportement devant une archive très grande ou malformée ; ce
   qui se passe si un membre attendu manque ou si la structure réelle diffère de l'hypothèse de l'auteur (dis ce que tu
   peux vérifier d'après le noyau et le lanceur, et ce qui reste une hypothèse).
5. **Gardes et surcharges réservées aux essais** : qu'elles ne puissent pas s'activer sans qu'on le voie en production
   (nom de la variable, trace dans la sortie, refus d'une surcharge partielle) ; que chaque garde soit essayée sur un cas
   sain et sur un artefact (règle R5).
6. **Essais** : rejoue la batterie sur ta copie avec `/opt/venv-essaim-sim-v1/bin/python -I` ; puis écris et lance au
   moins cinq artefacts de ton cru (par exemple un lien symbolique dans l'archive, un membre en double, une génération
   notée manquante au milieu, une réponse illisible, une sortie déjà existante) ; garde leur journal.

## Interdits (sans exception)
N'ouvre, ne lis, ne hache aucun fichier de banque de données (`*-cle.json`, `*-secret.json`, `banque-confrontation-v*.json`),
aucun `ferme.tar.gz`, `reponse-question*`, `journal-appels*`, `extrait-mecanique*` d'un pilote réel, aucun dossier
`donnees/`, `runs/`, `diag/`, `pilotes/`, ni `P3-consignes-v1.md`, ni `textes-actions-…`. Aucun `git`, aucun sous-agent,
aucun réseau, aucune clé ; aucune recherche récursive dans les dépôts ; n'exécute ni le lanceur, ni le noyau, ni le code
d'un organisme (tu peux importer des fonctions pures du noyau par `PYTHONPATH` pour recouper). N'écris que sous
`/var/tmp/relecture-script-lecture-pilote4-v1/`. Aucun critère ni stratégie de classement des tâches. Heure lue sur
`date -u` dans la commande même où tu l'écris.

## Ce que tu rends (sous `/var/tmp/relecture-script-lecture-pilote4-v1/`)
`rapport-relecture-script-lecture-v1.md` : constats numérotés RSL-01, RSL-02… (lieu : fichier et ligne ; gravité :
« bloquant », « à corriger avant usage » ou « mineur » ; ce qui est faux ; correction proposée) ; essais rejoués et ajoutés
(nombres, issues) ; verdict en une ligne : « utilisable tel quel », « utilisable après corrections » ou « non
utilisable » ; ce que tu n'as pas pu vérifier. Avec son compagnon `.sha256` et le journal de tes essais. À la fin, réponds
en trois lignes : le verdict, les constats bloquants ou à corriger (numéros), l'empreinte du rapport.
