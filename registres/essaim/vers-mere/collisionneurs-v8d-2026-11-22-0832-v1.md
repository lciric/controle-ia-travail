# Collisionneurs v8d, compte rendu 35 : tirage au hasard arrêté par la garde de motifs (Neon), file des six dossiers arrêtée

Écrit à 2026-11-22T08:32:41Z (`date -u`).

- `runs/collisionneur-protocole-x-tirage-au-hasard-v1-20261122-080414` : tour III.1 complet (six cellules OK, 3,43 USD) ; à 08:31:59Z, envoi de `E3-T2-critique-croisee-A` refusé avant l'envoi, code 7 : « chemin interne ». Recherche par programme sur les six conceptions : une seule occurrence, dans `E3-T1-conception-F` (Neon), forme `scripts/` (motif `(?<![\w/.-])(?:docs|runs|scripts)/` de la v8d). C'est un chemin relatif écrit par le modèle, pas un chemin de notre dépôt servi au fournisseur. Rien n'a été envoyé ni retiré.
- Selon la règle de l'enchaîneur (tout code autre que 0 ou 5 arrête tout), la **file des six dossiers est arrêtée** : les cinq dossiers suivants ne sont pas partis. La seconde voie (reprise de l'ancienne file, cinq espèces) continue.
- **Décision de l'arbitre (toi, ou Lazar)**, options :
  - (a) `--accepter-absence E3-T1-conception-F` : le dossier continue sans la conception de Neon, qui ne sert alors ni aux critiques ni à sa propre réponse. Sans code neuf. Mais on perd l'apport de Neon sur ce dossier.
  - (b) Nouvelle version de la v8d (v8g, classe B, contre-lue) avec une acceptation nommée d'un motif par l'arbitre (`--accepter-motif CELLULE:catégorie`, journalisée), ou un motif `scripts/` resserré aux seuls chemins de notre dépôt. Le dossier continue avec Neon. Coût : une heure environ de code et de contre-lecture.
  - (c) Arrêter ce dossier et relancer la question dans un dossier neuf, au risque d'un nouveau refus.
  - **Recommandation** : relancer tout de suite la file des cinq dossiers suivants, telle quelle, la garde restant en place ; pour celui-ci, (b) si Neon doit compter dans ce dossier, sinon (a). Confiance moyenne : Neon et les autres modèles peuvent écrire d'autres chemins relatifs dans les dossiers suivants.
