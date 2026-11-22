# Contre-lecture de la porte de périmètre (étape 4) — v1

Lecteur neuf : Claude Sonnet 5.5, 22 novembre 2026. Lu : `porte_perimetre_v1.py`, `test_porte_perimetre_v1.py`, l'avis de fusion (lignes de l'étape 4), `listes_lecture_v3.py` et `recherche_bornee_v5.py` par appel seulement. Rien modifié ; essais dans `/tmp/cl/pp` (dépôt jetable `/tmp/cl/r2`).

## Verdict : non conforme en l'état

Le jugement ligne par ligne est juste (bras, commit ancêtre, chemin ouvrable, champs fermés, ligne illisible, rapport exclusif, chemins sans contenu). Mais la porte peut « tenir » sans avoir rien jugé, et un agent peut la faire tenir en lisant librement. Trois défauts bloquants, quatre à corriger, trois remarques.

## Bloquants

### P1 — Journal absent ou vide : « tient » (faux tient)
- `porte_perimetre_v1.py` l. 102 et 82.
- Sorties réelles : journal inexistant → `{"verdict":"tient","lignes":0}`, code 0 ; fichier vide → idem. Un journal supprimé, tronqué à zéro ou jamais écrit passe donc. Aucun essai ne couvre ce cas.
- Correction : journal absent = arrêt (code 1) ; zéro ligne = « sans objet » ou « tombe », jamais « tient », sauf si la mère déclare explicitement une journée sans lecture (`--zero-lecture-attendu`).

### P2 — Le journal est choisi par l'appelant : `--journal /dev/null` supprime toute trace
- Origine : `recherche_bornee_v5.py` (`--journal` obligatoire mais libre) ; effet sur la porte.
- Essai : `lire registres/decisions.md --bras memo --agent biblio --journal /dev/null` lit le fichier et ne laisse aucune ligne ; la porte, qui juge un journal vide, tient (P1). Même chose avec un chemin jetable. L'agent peut aussi supprimer ou vider le journal après coup (essai : `sed -i d` → `tient`, 0 ligne).
- La limite déclarée (« une lecture hors outil ne laisse pas de ligne ») est ici plus large : une lecture **par l'outil** peut ne pas en laisser.
- Correction : le journal n'est pas une option de l'agent : chemin figé par la mère (variable d'environnement posée au lancement, ou constante), fichier en ajout seul, propriété de la mère ou non modifiable par l'agent ; un journal par session, nommé par le lanceur.

### P3 — Le nom d'agent est déclaré par l'agent : le fichier des rôles ne lie rien
- `porte_perimetre_v1.py` l. 69-75 ; `--agent` et `--bras` libres dans l'outil.
- Essai réel : la bibliothécaire appelle `--bras boucle --agent cycle` et lit `registres/veille-de-cap/journal.jsonl` (partition « mère », contenu `mere secret` montré) ; la ligne journalisée porte `agent: cycle`, `bras: boucle`, que le fichier des rôles assigne à `cycle` → `tient` (code 0).
- La porte vérifie la cohérence du journal avec lui-même, pas l'identité de l'appelant. C'est la remarque 1 de la contre-lecture des outils (bras choisi par l'appelant) qui ressort ici sans garde : la porte devait la couvrir « après coup » et ne le peut pas.
- Correction : rôle attaché au **journal** (un fichier par session, le lanceur de la mère fixe son bras, l'outil lit le bras dans l'environnement et refuse `--bras`), la porte jugeant chaque fichier contre le bras du lanceur ; le nom d'agent ne sert qu'à l'affichage.

## À corriger

### P4 — Aucune preuve de complétude (troncature à la limite de ligne, lignes supprimées)
- Un journal tronqué en milieu de ligne tombe (ligne illisible), c'est bien. Tronqué à une limite de ligne : essai, 2 lignes réduites à 1 → `tient`. Aucune borne basse : agents des rôles sans aucune ligne acceptés (essai : le rôle `cycle` n'apparaît pas, `tient`).
- Correction : le lanceur consigne, à la fin de chaque cycle, le nombre de lignes et l'empreinte cumulée du journal ; la porte compare. À défaut : exiger au moins une ligne par agent déclaré actif dans un second fichier de la mère.

### P5 — « Journée entière de cycles » (avis, étape 4) : aucune notion de journée
- Les lignes du journal n'ont pas de date (`journaliser` n'écrit ni `quand` ni session) ; la porte juge tout le fichier qu'on lui donne. Rien n'établit que le fichier couvre la journée ni qu'il ne couvre que celle-ci.
- Correction : l'outil écrit `quand` (UTC) et un identifiant de session ; la porte prend `--jour AAAA-MM-JJ`, refuse une ligne hors du jour, et compte les sessions attendues ; ou rotation quotidienne du journal par le lanceur (et alors l'arrêt P1).

### P6 — Lecture et décodage : plantages au lieu d'arrêts propres
- l. 102 : `open(..., encoding="utf-8")` sans garde. Journal non UTF-8 → `UnicodeDecodeError` (trace, pas de rapport) ; journal qui est un dossier → `IsADirectoryError`. Fail-closed de fait (pas de « tient »), mais pas de rapport écrit : le cycle de la mère ne verra pas « tombe ».
- Correction : `try/except` → arrêt code 1 avec message ; ou lire en `errors="replace"` et compter la ligne comme manquement. Essai manquant.

### P7 — Pas de contrôle que le chemin existait au commit comme fichier ordinaire
- l. 79 : la porte juge la règle de chemin seule. Une ligne forgée ou erronée (chemin inexistant, ou lien) est acceptée. Sans effet sur la fuite, mais un journal de lignes inventées « tient ». Correction : `git cat-file -t commit:chemin` = blob, sinon manquement.

## Remarques
1. Les doublons sont acceptés (essai : journal doublé → 4 lignes, `tient`) : sans conséquence pour la fuite, mais le compte de lignes ne dit rien ; à signaler dans le rapport.
2. `ancetre` : si ni `origin/main` ni `main` n'existe (ou depot erroné, défaut `.`), toutes les lignes tombent « hors de la branche principale » : fermé, mais le message devrait dire « branche principale introuvable ».
3. Essais manquants (en plus de P1 à P7) : journal absent ; journal vide ; deux agents de même nom et bras différents ; ligne à `agent` non chaîne ; BOM ; `chemin` non normalisé ; commit existant mais non ancêtre (un commit réel d'une branche exclue, pas `f*40`) ; essai de bout en bout avec le nouvel outil à journal imposé.

## Constat
Tant que P1 à P3 ne sont pas corrigés, la porte ne constate rien d'utile contre un agent qui choisit son journal, son nom ou son bras ; elle ne détecte que les erreurs d'un agent de bonne foi. Les corrections P2 et P3 touchent l'outil (`recherche_bornee`), pas seulement la porte : à faire ensemble, puis une vérification courte.
