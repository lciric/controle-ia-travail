# Rapport de correction de la chaîne de P4-instrument (chaîne v2) — v1

Correcteur neuf de la chaîne. 2026-10-20, fin vers @@heure@@ UTC.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

## Verdict

@@verdict@@

## Ce qui est fait

- Chaîne v2 écrite dans `…/chaine-v2/`, copie de `…/chaine/` (v1 intacte), mêmes noms, vingt et un scripts dont
  quatre neufs (`arreter_p4_v1.sh`, `controler_traces_p4_v1.sh`, `essais_arret_p4_v1.sh`, `essais_traces_p4_v1.sh`).
  Liste CHAINE mise à jour (scellement, lanceur, bancs ; répétition finale : 21 attendus).
- Toutes les décisions de la session appliquées (détail constat par constat : `NOTES-CHAINE-v2.md`, section 2).
- Bancs complétés : chaque correction a son cas sain et ses artefacts ; cas des relecteurs repris (formes voisines
  de révocation, fenêtres décalées, texte échappé, traces seules, étiquette « p4-v1 x », 4 096 colonnes, longueurs
  doublées, motif d'arrêt recopié).
- Sept bancs et la répétition jouet rejoués sur les versions finales (C d'essai `@@c_essai@@`, module v2, candidat 2
  d'essai tiré du candidat 1 réel par `ecrire_candidat2_v1.py` et les paires de la chaîne v2). Cinquième passage
  ajouté (arrêt du module pendant le run).
- `verifications_p4_v1.py preuves` (sept journaux des bancs) : code @@code_preuves@@. `verifications_p4_v1.py
  repetition` : code @@code_repetition@@.
- Paires exactes du texte : `paires-candidat2-chaine-v2-v1.json` (`@@paires@@`).

## Résultats

@@resultats@@

## Constats du correcteur

@@constats@@

## Texte à ajouter au candidat (exact)

Chaque phrase remplace l'ancre indiquée du candidat 1, trouvée une seule fois (fichier `paires-candidat2-chaine-v2-v1.json`).

@@textes@@

## Fichiers livrés

@@fichiers@@
