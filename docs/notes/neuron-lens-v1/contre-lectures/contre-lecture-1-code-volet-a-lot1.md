# Contre-lecture 1 du premier lot du code de la course du volet A — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé après 11:18 UTC, rapport lu vers 11:24 UTC ; il n'a écrit aucune des pièces. Pièces :
`volet_a_donnees_v1.py` (`12f244e8150c58643d8630405f7cdcb0d50c4d200af542c2e2f72a683aea869a`), `volet_a_extraction_v1.py`
(`04bfe2cb7a2ad3d4edd482dd5ad2a240aa3e2b1f0234360fcd69bd6abc57b3bf`), `volet_a_sondes_v1.py`
(`01a25f1948b6f5a512076ff88a6a9a99f9656648825470a6fcda4f5ce494ffd2`), `volet_a_lectures_v1.py`
(`32ba7af7ab06b697f43bae493cf2d115cb628c61c91e79dc0cc3086337566b6e`) et leurs essais. Il a aussi lancé `sha256sum`, `wc -l`, `ls` (lecture
seule, hors de la liste stricte ; déclaré par lui).

**Empreintes** conformes (texte v6, décisions v4, comptes, tokeniseur) ; 20 essais passés. **Conformité** vérifiée point par point (invites,
préambule, position, effectifs 200/594/597, AdvBench 463, faits 297/300, hors distribution, découpes 140/60, 416/178, 418/179 ; arbre de
graines reconstruit indépendamment : identique ; extraction vérifiée en lots multiples, écart 2e-9 ; lectures conformes à `08_reads.py`,
`read_rows`, `catalog.kept`).

**Verdicts** : données **après corrections mineures** ; extraction **scellable en l'état** ; sondes **après corrections mineures** ; lectures
**après corrections mineures**. Lectures déclarées (plis stratifiés, tirage par classe, écart-type nul → 1) : **compatibles**.

**Remarques**
1. Moyenne — `composantes` plante à k = 512 (n_apprentissage 140, 416, 418) : déclarer k effectif = min(k, n − 1), rapporté ; essai k > n.
2. Moyenne — `borne_basse_appariee` et `detecteurs` prennent une seule graine ; le texte en fixe une par découpe : prendre les 5 graines et
   dire comment l'assemblage les distribue.
3. Moyenne — `mesure_a2` ne rapporte pas les témoins « sonde permutée » et « direction de C3 » (hors condition, à rapporter).
4. Moyenne (R5) — artefacts de A1 trop faibles (le témoin qui lit la même fuite n'est pas essayé) ; artefact A2 manquant.
5. Mineure — `tirages_apparies_a3` : retirés et doublons possibles dans les tirages ; exclure les retirés et tirer sans remise, ou déclarer.
6. Mineure — `_choisir_c` standardise sur tout l'apprentissage avant la validation interne (fuite légère) ; paramètre mort `centrer` ; déclarer.
7. Mineure — `ecart_moyen_standardise` : lectures (écart absolu, écart-type pondéré, nul → 1) à déclarer en tête.
8–10. Mineures — essais manquants (ordre des graines par reconstruction indépendante ; fichier altéré ; rendu inattendu ; position < 16 ;
   contraste inconnu ; positions hors distribution ; plis groupés ; égalité de C ; pli monoclasse ; `premiers` à moins de 10 poids ;
   reproductibilité de `detecteurs` ; γ ≠ 1 ; artefact du cas (iii) ; « night », « nightly », « noct » ; vrai masque `presents` ; déciles).
11. Info — essai d'extraction multi-lots à ajouter.
12. Info — avertissements de convergence de `LogisticRegression` à consigner au manifeste.
**Manque pour une course** : gardes de rendu, P et v0 ; chargement des lentilles et orientations ; `presents` et fréquences ; lecture R et
cas sains (i), (ii) ; A3 avec nouvelle passe ; boucle A-ii ; mémoire de `stats_reference` (≈ 1,2 Go par lecture en float64) ; manifeste R9.
(Une partie de ce manque est couverte par l'assemblage `volet_a_course_v1.py`, écrit pendant cette contre-lecture, non relu.)
