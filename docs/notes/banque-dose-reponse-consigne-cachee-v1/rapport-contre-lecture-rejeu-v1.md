# Contre-lecture du rejeu diagnostique de la contre-vérification (classe B) — v1

Fichier : `src/controle_ia/environnements/rejeu_contre_verification_banque_v1.py` (commit 52515442), comparé à `preparer_contre_verification` et `lire_contre_verification` de `extraire_banque_dose_reponse_v1.py` (rôle « echantillon »), à `extraction.py` et à `corpus_arxiv.traiter_papier`. Rien exécuté de `preparer` ; rien ouvert sous `donnees/` ni dans les dossiers de travail des papiers ; j'ai lu les métadonnées du rejeu déjà écrites dans `diag/20261124-133630-rejeu-contre-verification-96/preparation-rejeu.json` (clés et forme seulement).

**VERDICT : utilisable en l'état** (0 bloquante, 0 majeure, 5 mineures, 2 suggestions ; la préparation, déjà jouée et scellée, a franchi son contrôle des textes ; la lecture juge comme `lire_contre_verification`).

## (a) La préparation reproduit celle d'une ronde — oui
- Échantillon : lu du résultat scellé `echantillon-contre-verification` du 7 octobre (16 papiers) ; la ronde 1 de ce run est bien la ronde « echantillon », de 16 papiers, tous à la tentative 1, sans échec (relu : rôle, effectif, ensemble égal à l'échantillon, tentatives {1}). Le module exige 16 papiers à la tentative 1.
- Sorties à juger : archive `sorties-tentative-1.tar` ouverte par `lire_archive` (empreinte consignée à la validation), puis, par papier, empreinte de chaque sortie comparée à `validation-tentative-1` : même chaîne que `preparer_contre_verification`.
- Dossier et consigne : `eb._dossier_agent(…, modele, "verifier_avis", a_verifier)` avec la consigne scellée du contre-vérificateur, `copie_de_lecture` du texte, script scellé, invites H.9 et H.10 : mêmes appels, mêmes arguments que la ronde.
- Textes : régénérés par `ca.traiter_papier` scellée (même version que les pages, bornes, pandoc 3.9, même filtre), avec l'ouvreur « reprenable » ; statut « gardé » et `texte_sha256` égal à celui de `corpus.json` du 6 octobre exigés pour chacun, avant la création du manifeste (arrêt R11 sans rien écrire de scellé). La préparation a abouti : le contrôle a donc été passé pour les 16.
- Épinglage : `fichiers_scelles` identique à celui d'une étape du run ; l'empreinte du module du rejeu est consignée.
- Rien d'inventé : aucun appel au modèle, aucune graine (`creer_manifeste(…, [])`), aucune modification de code scellé.

## (b) La lecture juge comme `lire_contre_verification` — oui
Même ordre : entrées modifiées (`_entrees_modifiees`), `avis.json` absent ou illisible avec les mêmes codes, `anomalies_avis` sur des entrées intactes seulement, accord du script scellé (`codes_du_script` puis `exiger_accord_script`, désaccord = arrêt), `retour_sans_texte`, motifs par `motifs_echec_avis(avis, cibles, h10)`, `cibles_defectueuses` et `cibles` calculés pareil, archive des avis scellée par `archiver`, détails dans `donnees/`. Comparaison à l'octobre par papier (`verdict_octobre`), liste des échecs, comptage par motif.
Écarts avec la ronde, sans effet sur le verdict : pas de `classification` ni de `compute_plausible` dans les fiches (voir CL-7) ; pas de seuil ni d'audit (voulu) ; pas de `_ouvrir_run` (voir CL-3).

## (c) Aucun texte de papier dans `diag/` — oui
La préparation écrite ne contient que : chemins de dossiers, empreintes des entrées, nombre de parties, invite de lancement, motifs d'octobre (listes vides). La lecture n'écrira que codes d'anomalie, forme du retour sans texte, motifs (chaînes fixes de `motifs_echec_avis`, sans citation), compteurs ; avis et dernière ligne brute vont dans `donnees/`. Les messages d'arrêt ne portent que des codes ou des identifiants.

## (d) Remarques

### CL-R1 — mineure — relecture des textes avec traduction des fins de ligne
Ligne 64 : `(…/"textes"/f"{pid}.md").read_text(encoding="utf-8")` traduit `\r\n` et `\r` en `\n`, alors que `lire_texte` (utilisé par la ronde réelle) lit les octets et décode sans traduction, et que l'empreinte a été contrôlée sur les octets. Si un texte converti contenait un `\r`, la copie de lecture du rejeu différerait de celle de la ronde (donc des citations vérifiées par le script) sans que l'empreinte le signale. Probabilité faible (pandoc écrit des `\n`). Correction : `read_bytes().decode("utf-8")` ; et, pour la préparation déjà jouée, compter les `\r` des 16 textes régénérés (un décompte suffit) ; s'il y en a zéro, le défaut est sans conséquence.

### CL-R2 — mineure — aucune pause entre les 16 téléchargements
Boucle des lignes 56-64 : `traiter_papier` est appelée sans `dormir(PAUSE_S)` entre deux papiers, contrairement à la sélection (`constituer_depuis`) ; la politesse demandée par arXiv est d'une requête toutes les trois secondes. La conversion pandoc entre deux requêtes en atténue l'effet. Conséquence d'un blocage : un papier « exclu : source indisponible » donne l'arrêt R11 « texte régénéré différent », sans corruption mais run à refaire sous un autre nom. La préparation a abouti, donc sans effet ici ; à corriger si le module sert de nouveau.

### CL-R3 — mineure — le module qui juge n'est pas recontrôlé à la lecture
`lire` compare `fichiers_scelles` mais pas l'empreinte du module du rejeu (consignée dans `config["module"]`), ni la racine du run ; or c'est lui qui décide ici. Correction : comparer `empreinte(__file__)` à `m["config"]["module"]` et `racine.resolve()` à `config["racine"]`.

### CL-R4 — mineure — détails non encodables
Ligne 139 : `details[pid]["avis"] = avis` sans le test `_encodable` de la ronde ; un avis portant un caractère non encodable en UTF-8 ferait lever `ecrire_donnees` après l'écriture de l'archive (reprise possible, idempotente, mais lecture interrompue). Correction : `avis if eb._encodable(avis) else None`.

### CL-R5 — mineure — aucun essai du module
Aucun fichier de `tests/` ne le référence : l'arrêt R11 sur un texte différent, l'arrêt sur une sortie d'archive altérée, l'accord du script, le cas « entrées modifiées » et la lecture complète ne sont éprouvés ni sur un cas sain ni sur un artefact (R5). Pour un instrument à usage unique et dont la préparation est déjà jouée, un déroulé jetable sur un dépôt de test (à la manière de `test_deroule_complet_banque`) serait un minimum avant la lecture.

### CL-R6 — suggestion — exiger que `--donnees` soit `donnees/<run>`
`_retours`, `archiver` et `ecrire_donnees` travaillent sous `donnees/<run_id>/` ; si `--donnees` désigne un autre dossier, les textes et les avis se trouvent dans deux endroits. Exiger l'égalité à la préparation évite l'erreur à la lecture.

### CL-R7 — suggestion — rapporter aussi la classification
Les fiches de la ronde réelle gardent `classification` et `compute_plausible`. Pour séparer une dérive du juge d'une dérive de l'extracteur, les désaccords de classification (non motifs d'échec) sont une information de plus, sans coût. Ajouter les deux champs dans les fiches lisibles et leur décompte au résultat.

## À noter pour la lecture du résultat
Ce rejeu ne sépare que le juge de l'extracteur : un 0 échec reproduit (le juge d'aujourd'hui reste clément sur les sorties d'octobre) pointe vers l'extracteur ou le tirage de papiers ; un ou plusieurs échecs « énoncé révélateur » sur les sorties d'octobre pointent vers une dérive du juge. Les sorties d'octobre ayant été jugées par un autre modèle, un écart peut aussi tenir à la différence de modèle ; à écrire dans la lecture.
