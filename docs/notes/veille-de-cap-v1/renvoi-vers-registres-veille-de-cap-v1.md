# Renvoi — les fichiers vivants de la veille de cap sont sous `registres/veille-de-cap/` (v1)

Pièce de travail (classe C), écrite le 2026-11-22 vers 18:20Z par un cycle à contexte neuf de la veille de cap (fusion avec la bibliothécaire, option accordée en GO-2026-11-22-90), en exécution de R-4958 (décision de routine : les fichiers vivants de la veille passent sous `registres/veille-de-cap/`) et de R-4974 (fuite fermée avant le déplacement : liste stricte v4, outils v3).

**Ce qui a été fait.** Six fichiers, et leurs compagnons d'empreinte, ont été copiés octet pour octet, lus par l'outil borné (`docs/notes/memoire-conception-v1/fusion-outils-v1/recherche_bornee_v5.py`, bras « boucle », au commit `ff12c703`), chaque copie vérifiée par l'empreinte de l'outil et par son compagnon :

| ancien emplacement (gardé, inchangé) | nouvel emplacement | empreinte (16 premiers signes) |
|---|---|---|
| `calendrier-de-relecture-v1.md` | `registres/veille-de-cap/calendrier-de-relecture-v1.md` | `aada7b841ec84789` |
| `etat/etat-de-la-veille-2026-11-22-1604.md` | `registres/veille-de-cap/etat/etat-de-la-veille-2026-11-22-1604.md` | `c764b7400a66f9c8` |
| `journal-des-idees-v1.jsonl` | `registres/veille-de-cap/journal-des-idees-v1.jsonl` | `67072344acacef9f` |
| `journal-des-idees-v1-partie-0002.jsonl` | `registres/veille-de-cap/journal-des-idees-v1-partie-0002.jsonl` | `e45bc1f16bf4684e` |
| `mesures-de-la-veille-v1.md` | `registres/veille-de-cap/mesures-de-la-veille-v1.md` | `e6450eaec4324054` |
| `reinjections-datees-v1.md` | `registres/veille-de-cap/reinjections-datees-v1.md` | `3b57a074db1d7445` |

**Ce qui reste ici.** Tout ce dossier garde ses fichiers ; rien n'est effacé ni réécrit (R12). Restent ici et n'ont pas été déplacés : les mandats, la conception et ses additifs, l'avis de fusion (pièces qui font foi pour la veille) ; les pièces scellées (bulletins, vues, pages du passé, l'ancien `etat-de-la-veille.md`, le registre v1, les échéances des accords) ; le programme de contrôle et ses essais (`outils/`, pièce d'instrument).

**À partir de maintenant.** Toute écriture vivante de la boucle (journal, état, calendrier, mesures, réinjections) se fait sous `registres/veille-de-cap/`, jamais ici. Proposé à la mère, non décidé : les bulletins, vues et pages du passé neufs aussi sous `registres/veille-de-cap/` (sous-dossiers du même nom).

**Cloisonnement.** `registres/veille-de-cap/` est hors de la liste stricte de la bibliothécaire, sauf le seul sous-dossier `commune/` (extraits de la partition commune) ; la boucle y lit et écrit par le bras « boucle ».
