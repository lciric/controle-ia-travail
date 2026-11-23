# Passation de la session fille de la garde de calcul (rang de GO à trois chiffres), reprise sur un autre compte

Écrite le 2026-11-23 vers 06:27Z. Classe C. Session `session_013QMaymAMVSEV3Ps3N2sVE8`, fille de la mère `session_013QMayjbmQUdDuDs2S3i3XD`. Demandée par la mère (mot de Lazar, GO-2026-11-23-09). Suit `registres/passations/2026-11-22-1956-garde-go-rang-trois-chiffres.md` (`9f8776c5…`), qui reste en vigueur pour tout ce qu'elle dit.

## Mandat
Corriger le défaut R-5013 de la garde de calcul : les expressions `GO_ID` et `LIGNE_GO` de `.claude/hooks/garde_calcul.py` n'admettaient que deux chiffres de rang.
- Admettre deux ou trois chiffres, sans rien changer d'autre.
- Écrire des essais neufs, sains et artefacts.
- Vérifier d'abord les lignes de rang 100 et plus du registre des accords.
- Faire contre-lire la correction par un sous-agent neuf, ouvrir une demande de fusion en brouillon, en rendre compte à la mère.
- Puis, à la demande de la mère (R-5026), dresser l'inventaire des épingles de l'ancienne empreinte de la garde et des fichiers à deux chiffres.

## Fait
- **Correction** : `09ecf2e0`. Inventaire : `0cb1837d`. Passation du 22 novembre : `0b350768`.
- **Fusion** : la demande n° 71 a été fusionnée par la mère le 2026-11-22 vers 23:35Z (R-5031). Sur la branche principale, la garde porte l'empreinte `4fae077c…`, égale à son compagnon.
- **Vérification de sécurité de 20:39Z** : rien à faire (pas de conflit, pas de revue).
- **Versement du bloc-notes**, ce jour : `docs/notes/garde-go-rang-trois-chiffres-v1/versement-bloc-notes-2026-11-23/`, chaque fichier avec son compagnon `.sha256`. Il contient :
  - `verif_rang3.py` : vérification par programme des 24 lignes de rang 100 et plus ;
  - `epreuve_registre_reel.py` : épreuve directe du crochet sur le registre réel ;
  - `verif_contre_lecteur.py` : les 22 cas limites du contre-lecteur ;
  - `ancien-arbre-contre-lecteur/` : son arbre temporaire, ancienne garde et essais ;
  - `garde_calcul_ancienne_73be0638.py` : copie de la garde d'avant la correction ;
  - `entete.md` et `inv.md` : brouillons de la note d'inventaire ;
  - `sortie-recherche-empreinte-b46z7yjl4.txt` et `sortie-lot-essais-interrompu-bxc4g4kkh.txt` : sorties de deux commandes ; le lot d'essais a été arrêté sur dépassement de délai ;
  - `transcription-contre-lecteur-a6f673dc.jsonl` : transcription entière de la contre-lecture.
- **Recherche de secrets** sur le versement : aucune valeur de clé, aucune adresse personnelle. Les mots « token » ou « clé » n'y paraissent que dans des comptes de jetons et des noms de variables.
- **Non versés**, et pourquoi :
  - `etat.md` et `dec.md` : copies de `registres/etat.md` et de `registres/decisions.md` lues sur `origin/main` = `43505ffb`, donc déjà sur GitHub ;
  - les caches `__pycache__` : sous-produits.

## Reste
- Non corrigés, hors du périmètre (réserves de la contre-lecture) :
  - la révocation se teste par sous-chaîne : une révocation qui citerait l'accord 117 révoquerait aussi l'accord 11 ;
  - 36 fichiers de `src/` et `scripts/` gardent l'expression à deux chiffres. Leur liste est dans la note d'inventaire.
- Suite d'essais complète non lancée dans cette session, faute de bibliothèques installées (ni scipy ni PyTorch).

## Réserves
- `registres/t07-etape-b-bis/feu-bbis-v7.txt`, geste 2 (b), attend encore l'ancienne empreinte `73be0638…`. L'étape est close.
- Les couples non appliqués du lanceur v3 des bassins étroits portent une condition d'empreinte devenue caduque (note de la mère, R-5031).

## Prochaine action
Aucune pour cette session.

## Branches et commits
- Branche `garde/go-rang-trois-chiffres-v1`, repartie de `origin/main` = `2311d156` après la fusion de la demande n° 71. Elle porte ce versement et cette passation.
- Commits antérieurs, fusionnés : `09ecf2e0`, `0cb1837d`, `0b350768`.

## Tâches planifiées actives
Aucune. La vérification de sécurité unique de la demande n° 71 s'est déclenchée à 20:39Z, puis s'est désactivée d'elle-même.

## Instances actives
Aucune. Aucune dépense.
