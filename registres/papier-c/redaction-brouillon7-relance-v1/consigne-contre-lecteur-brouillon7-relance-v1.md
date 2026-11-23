# Papier C — consigne du contre-lecteur du brouillon 7 de relance du préenregistrement (R2) — v1

Date : 2026-11-22. Écrite par le rédacteur du brouillon 7 de relance, pour un sous-agent neuf sur un autre modèle
(Opus 5.5) qui n'a écrit aucune version de ce texte. Classe C. La session qui te lance peut la compléter ; elle ne
la réduit pas.

## 1. Ce que tu relis
- Le texte : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22.md` ; vérifie d'abord
  son empreinte contre son compagnon `.sha256`.
- Sa source : `registres/papier-c/redaction-brouillon7-relance-v1/source/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r3.md`
  (`160730b4c3980d8d96b0d05ed4041f011b5bf78a7d8dc7f927ee1ed0c2463cac`).
- Dans `registres/papier-c/redaction-brouillon7-relance-v1/` : la note des différences, le programme de construction
  et son journal (`travail/`), les points ouverts pour le directeur, l'additif à la fiche du module, le journal du
  rédacteur, le contrôle des empreintes citées, la sortie du validateur.
- Sur la branche `claude/papier-c-preenregistrement-v1` (commit `48e08c72`), dossier
  `registres/papier-c/redaction-brouillon6-relance-v1/` : le rapport de la contre-lecture de r2
  (`contre-lecteur/rapport-contre-lecture-brouillon6-relance-r2-v1.md`, `71996527…`), sa table de traitement
  (`redacteur/table-traitement-contre-lecture-r2-v1.md`, `2d146ba8…`), la liste finie des cases
  (`redacteur/liste-finie-cases-grille-v1.md`, `0c62072c…`), le rapport de la grille et sa contre-lecture, la fiche
  du module v3, les décisions exigées v3 et v4.
- Sur `main` : `CLAUDE.md` ; `docs/brief-claude-code-programme-complet-v2.md` (T0.6, T0.7, T0.9, porte G0,
  section 9) ; `docs/programme-controle-ia-v2.md` (section 5) ; `docs/decisions/` : N-005 et N-006, N-013, N-023,
  N-026, N-053, N-065, N-068 ; `prereg/gabarit-preregistrement-v1.md` ; `src/controle_ia/prereg.py` ; les lignes
  GO-2026-11-19-53, GO-2026-11-19-74, GO-2026-11-22-77, GO-2026-11-22-93 et GO-2026-11-22-113 de `registres/go.md`.

## 2. Interdits
Aucun résultat d'expérience : rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. Rien dont le nom contient
« consigne-privee », « conception-ii-b », « vérité », « rendu » ou « scores » ; ni `brouillons/ii-b-saboteur-budget-v1/` ;
ni les branches `lot/compte-4-v1` et `prep/quarantaine-*` ; ni la ligne R-2059 ; ni N-063 ni N-054 si leur texte porte
un résultat (leur ligne de `CLAUDE.md` suffit). Aucune dépense, aucun appel payant, jamais la suite d'essais
complète. Tu écris dans ton seul dossier, `registres/papier-c/redaction-brouillon7-relance-v1/contre-lecteur/`. Au
premier refus de permission : arrêt, texte exact rendu, aucun contournement. Inscris-toi à la liste « qui a lu
quoi » avant d'ouvrir le texte (ligne proposée à la session qui te lance).

## 3. Ce que tu vérifies, dans cet ordre
1. **Le différentiel est celui de la table.** Rejoue le programme de construction dans ton dossier ; la sortie doit
   avoir l'empreinte du texte ; relis les 41 remplacements un à un contre la note des différences. Un changement
   hors de la table est une remarque bloquante.
2. **Rien de ce qui est tranché n'a bougé.** Énoncés de HC1, HC2, HC2b, HC3 ; prédictions, marges, seuils ; les vingt
   décisions D-1 à D-20 ; les 37 précisions de r3. Dis-le explicitement, ou dis où cela a bougé.
3. **La version r3 a-t-elle porté CR-01 à CR-10 ?** Elle n'a jamais été vérifiée. Reprends le rapport `71996527…`
   remarque par remarque et la table de traitement ; pour chaque remarque : portée, portée en partie, non portée.
   Même chose pour ce que r3 tire de la contre-lecture de la grille (CG-01, CG-03, CG-05 à CG-10).
4. **Les ajouts de r3 jamais contre-lus** : la liste finie de 144 cases et ses dimensions (chacune vient-elle des
   mots de la clause ?) ; la précision 37 et sa « raison de principe » (est-ce une précision, ou un changement de ce
   qui compte comme « établie » ?) ; les trois issues écrites d'avance ; la règle de remplissage du bras
   « contrôlabilité ». Réserve de méthode déclarée par le rédacteur du 19 novembre : les effectifs de la grille et
   ses huit modèles ont été écrits après lecture des taux simulés.
5. **Les ajouts de ce brouillon** (propositions D-21 et D-22) :
   - précision 38 : la règle est-elle entière et mécanique ? couvre-t-elle tous les cas d'un verdict de G0 jugé par
     famille et par dose ? la citation du brief est-elle exacte (T0.7 ; critère 3 de la porte G0) ? le choix du plus
     petit écart favorise-t-il un signe ?
   - réserve 20 : l'argument (« une sonde qui lit la trace de la consigne reste immobile sous le plaidoyer ») est-il
     juste au vu des cellules du plan ? la mention est-elle bien posée sur toutes les lignes, sans changer un
     verdict ?
   - précision 39 : les deux parts sont-elles bien définies, calculables par le module avec la fonction de
     reconstruction du point 14, et lisibles sans ambiguïté ? ce qu'elles « ne disent pas » est-il complet ? la
     relecture d'un épisode honnête sous la condition du saboteur pose-t-elle un problème que le point 14 ne
     prévoit pas ?
   - ces ajouts créent-ils une revendication, une réfutation ou une confirmation nouvelle ? Ils ne le doivent pas.
6. **R7.** Aucun chiffre de l'état de l'art n'est ajouté par ce brouillon : vérifie-le sur le différentiel. Puis, sur
   un échantillon d'au moins dix citations chiffrées du texte dont le PDF est au dépôt (`docs/sources/pdf/`),
   contrôle le chiffre et la page ; dis lesquelles tu as contrôlées, et lesquelles ne peuvent pas l'être faute de
   PDF.
7. **R6 et R11.** Rejoue le contrôle des empreintes citées ; toute pièce citée comme présente et introuvable est une
   remarque.
8. **Validateur.** `controle_ia.prereg.problemes` doit rendre : la section « Contre-lecture » à remplir, et seize
   marqueurs (les quinze de r3 et `<<MOT_DU_DIRECTEUR_D21_D22>>`).
9. **Forme.** Français, aucun sigle seul, chaque précision nommée dans le passage qu'elle fixe (CR-01).

## 4. Ce que tu rends
Un rapport `rapport-contre-lecture-brouillon7-relance-v1.md`, scellé, dans ton dossier : remarques numérotées (lieu,
citation, pièce, constat, correction demandée, gravité : bloquante, majeure, mineure), réponse à chacun des neuf
points, avis d'ensemble (« scellable », « scellable après corrections », « non scellable »). Tu ne corriges pas le
texte. Tu vérifieras ensuite les corrections du rédacteur.
