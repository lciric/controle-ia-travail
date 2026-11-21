# Notes d'avancement — auteur v2 du lanceur et du gardien, palier 0b, essai court (au fil de l'eau)

- 2026-11-21 : mandat (32580fd6…8d84) et erratum 1 (d21745f5…193b) vérifiés par `sha256sum`, lus en entier. Pièces v1 et contre-lecture v1 lues en entier.
- Complément 1 v3 extrait par `git show origin/main:… >` dans ce dossier : extraction v1 `complement-1-v3-extraction-v1.md` 1484cd75…7268 (égale à l'attendue) ; extraction v2 `complement-1-v3-extraction-v2.md` 56ed20f8…b867 (pas d'empreinte attendue donnée par l'erratum ; relevée).
- Pièces v2 écrites : gardien-essai-court-v2.py, demarrer-essai-court-v2.sh, lancer-essai-court-v2.sh, demarrer-gardien-essai-court-v2.sh, verifier-commande-v2.py.
- Premier passage des essais (16:44–16:53Z, gardien avant deux retouches : ligne « identité à la prise de garde » ajoutée, condition de racine de l'arbre simplifiée) : refus 0 échec ; projection v1 0 échec, v2 0 échec ; s1 à s9 conformes ; h1 (enfant en session à part arrêté, témoin intact), h3 (n = 826 = fichiers de s4), h4 (membre sourd arrêté de force à 5 s), c2-sain, decoy (aucun signal), decoy périmé (aucun signal), argv et lanceurs altérés (ÉCHEC attendu, obtenu), c5 et c6 conformes. Résultats sous essais/resultats/ et essais/*/e/.
- Passage final sur les pièces dans leur état final : essais/rejouer-tout-v2.sh final (voir le rapport).
- Passage final 16:54:21Z–16:57:43Z : tous conformes (refus 0 échec, projections 0 échec, s1 à s9, h1, h3 (809 = 809), h4, c2-sain, decoy, decoy périmé, argv et altérés, c5, c6). Processus factices du passage final vérifiés absents par `stat`.
- Rapport écrit : rapport-auteur-lanceur-gardien-essai-court-v2.md ; compagnons .sha256 écrits.
- Plan : gardien v2 (corrections 1 à 6), départ v2 (heure de départ du processus écrite), lanceur v2 (inchangé sur le fond), départ du gardien v2, vérificateur v2 ; essais : rejouer auteur-v1/essais et contre-lecture-v1/essais (copiés ici, chemins adaptés), plus un cas sain et un artefact par correction.
