# Passation — fille des questions du directeur du 24 novembre (2026-11-24, 2026-11-24T14:12:39Z)

Session `session_016QhUrtAyz3dFV4u1BbUBoS`, mère `session_016QhUrvi45g3jX5saFefVED`. Branche `idees/questions-directeur-2026-11-24-v1` (jamais main), PR brouillon n° 97. Dossier : `docs/notes/questions-directeur-2026-11-24-v1/`. Aucune dépense, aucune machine, aucune tâche planifiée.

## Fait (chaque fichier a son compagnon .sha256)
- Mandat `mandat-questions-directeur-v1.md` (ab6f19bb…) : questions 1 à 7 verbatim, dosage, interdits.
- Compléments de la mère, verbatim : `complement-note-latex-spectral-puits-fecondite-v1.md` (pour la note), `complement-questions-8-9-et-corrections-note-v1.md` (questions 8, 9 ; quatre corrections de la note), `complement-questions-10-11-et-apport-q5-v1.md` (questions 10, 11 ; apport pour la 5).
- Reformulations en quatre points des questions 1 à 7 (Fable, élevé) : `demandes-reformulees-quatre-points-v1.md` (52d1cc47…).
- Réponses : question 1, quatre étapes comme oracles (Fable, élevé, 2cc29632…) ; question 2, profondeur (Opus, maximal, 7f4cf73f…) ; question 7, couche des problèmes et hypergraphe (Opus, maximal, 937e3e69…) ; question 3, cinétique (Opus, élevé, af126ebf…, simulation `simulation-cinetique-barriere-v1.py` rejouée identique) ; question 4, émergence (Opus, maximal, 249c611c…, simulation `simulation-emergence-organisme-v1.py` rejouée identique).
- PDF à la page versés dans `docs/sources/pdf/` (arXiv, accès libre) ; les autres gardés par empreinte seule (`empreintes-pdf-lus-q3|q4|q7-v1.md`).
- XeLaTeX installé dans le conteneur (texlive-xetex, lang-french) : à réinstaller sur un conteneur neuf.

## Reste, file exacte (un seul sous-agent à la fois, en série)
1. Question 5 (Carbon et son programme contre Fable ; amender le Plan Turing ?), Opus élevé, avec l'apport de Lazar (puits étroit). Commencée, coupée par la limite d'usage (faux échec, aucun fichier écrit) : relancer sur le même mandat, sortie `reponse-q5-carbon-fable-et-plan-turing-v1.md` ; ne pas refaire la comparaison des hypergraphes (question 7).
2. Reformulations en quatre points des questions 8, 9, 10, 11 par un seul Fable, effort élevé, prompt verbatim de CLAUDE.md, fichier `demandes-reformulees-quatre-points-q8-q11-v1.md`.
3. Questions 6 (démonstration, maximiser la découverte, critères) et 8 (plasticité) par un seul Fable en effort maximal, deux parties distinctes ; antériorités sur PDF listées dans le complément 8-9 ; intégrer R-5241 (extraction lexicale réfutée).
4. Question 10 (forme de l'anomalie et rôle de l'objet manquant, démonstrations) : Fable, effort très élevé (xhigh).
5. Question 9 (exposé pédagogique du graphe méta-mathématique) : Fable, élevé ; Markdown et PDF.
6. Contre-lecture courte de toutes les réponses par un Opus neuf (élevé), puis corrections.
7. Livrable (b) : note LaTeX et PDF du modèle unifié (Opus maximal), avec résonance (co-accélération au-delà de F), φ homomorphisme partiel mesuré par c et κ (κ = part des conflits ; quatre cas confirmé, contredit, absent, trou), deux perturbations (faits : profondeur ; correspondance : étroitesse), coordonnées spectrales et matrice C (Ovsjanikov 2012), analogie des corrélations canoniques (Hotelling 1936, dite comme analogie), couche des questions ouvertes, cinétique, puits profond et étroit, fécondité ; xelatex, zéro glyphe manquant.
8. Livrable (c) : une seule question neutre groupée pour le collisionneur sur les questions 1, 2, 3, 7 et 11 (Fable élevé) ; garde de motifs ; test de devinette par agent neuf sous 0,50 ; devis vérifié (gabarit : `docs/notes/protocole-x-boucle-organisme-controle-v1/devis-…-v2.md`, `verif_devis.py`) ; aucun appel payant, rendu à la mère pour le mot de Lazar.
9. Après chaque livrable (a), (b), (c) : trois lignes à la mère.

## Réserves et nœuds pour Lazar (non tranchés)
- Question 1 : une couverture vraie par la graine mais lue par des modèles lecteurs est-elle l'oracle du monde planté (N-058) ou un score de juge (N-053) ? Recommandation : admise seulement si extraction entièrement programmatique (0,7).
- Question 2 : la portée plantée peut-elle entrer dans l'oracle qui juge les compositions ?
- Errata à faire : registre des idées (IDE-2026-11-23-019, -061, ligne 4 du rapport de priorités : attribution de l'hypergraphe à Carbon) ; IDE-2026-11-23-060 (Diehl et Stroebe : suggestion, non résultat, p. 508-509) ; Zenodo de Gu et Krenn = graphe, pas notes.
- Question 4 : essai dans l'organisme chiffré 315 à 631 USD (tarifs de Neon), non engagé.
- Points « à vérifier » listés en fin de chaque réponse.

## Accords en cause
Mandat de la mère (24 novembre) ; protocole X (GO-2026-11-21-57, GO-2026-11-22-25) ; aucun GO de dépense.

## Ne pas refaire
Reformulations 1 à 7 et réponses 1, 2, 3, 4, 7. N'ouvrir rien sous coffre/*, docs/verdicts/, runs/, diag/, donnees/.

## Prochaine action
Relancer la question 5 (point 1 de la file) quand le quota le permet (limite d'usage levée vers 14:10 UTC).
