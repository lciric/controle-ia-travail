# Ronde 1 élaguée de la boucle extérieure du pilote 4 — sortie partielle, NON LUE — LISEZMOI v1

Versée le 27 octobre 2026 vers 06:40 UTC par conv-audit, avant la passation de la lignée à une instance nouvelle sur un
autre compte, pour qu'elle ne se perde pas avec le conteneur. **Personne ne l'a lue ni vérifiée** : le sous-agent (Opus 5.5,
brief `BRIEF-ronde-1-elaguee-v1.md`, `2a3e9572…`) a écrit sa pièce de périmètre (16:55 UTC), son diff et l'objet corrigé
(18:11 à 18:16 UTC, heures des fichiers) ; aucun rapport final n'a été trouvé sur disque ; la priorité est passée au pôle
scientifique automatique (Lazar, 18:29 heure de Paris), et la vérification prévue (passation v3, § 3, point 1) n'a pas été
faite.

- Correction proposée : **un seul facteur, F01** (nombre minimal de rondes avant la déclaration de fin), `principal.py`
  l. 2106 : `(critere_qualite or critere_convergence or derniere_ronde) and r_idx >= 3` ; version 6.2.2 ; détail dans
  `perimetre-ronde-1-elaguee-v1.md` et `correction-ronde-1-elaguee-v1.diff` (`0ba157e2…`).
- Archive : `ronde1-elaguee-sortie-partielle-v1.zip` (`753aa625…`) = le dossier `sortie/` du sous-agent **sans** ses
  copies de travail `essais/tmp-*` ; les pièces fournies ne sont pas versées (leurs empreintes : `EMPREINTES-fournis-v1.txt`).
- Avant tout usage : la vérification de la passation v3 (§ 3, point 1) — chemins de json cités revérifiés, les 68 essais
  de l'organisme relancés sur `objet-corrige/`, diff limité aux lignes du facteur de la carte v2, hors zones interdites,
  sans score ni identifiant de tâche. **Rien de ceci n'est servi à un organisme.** Aucune course de la v6.2.2 sans
  décision de Lazar (dépense : mot direct dans la session de session-depot).
- Recherche de clés faite sur tout ce qui est versé (archive décompressée comprise) : 0 écriture de clé.
