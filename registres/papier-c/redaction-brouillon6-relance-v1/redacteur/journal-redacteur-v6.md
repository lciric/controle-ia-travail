# Journal du rédacteur du brouillon 6 de relance du préenregistrement du papier C — v6 (cinquième suite)

Suite des journaux v1 à v5, intacts. Même rédacteur (Claude Fable 5.2), même mandat. Heures UTC par `date -u`, le
2026-11-19. Aucun écrit hors de `bloc-notes/redacteur/`. Dépôt intact (`git status` vide ; seul `git fetch origin
main`). Aucun refus de permission. Aucune dépense, aucun appel à un modèle, aucun autre agent, aucune suite d'essais,
aucun calcul de simulation. Aucune suppression, aucune commande `rm` ; aucune pièce rendue écrasée (R12). Rien
ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun fichier « consigne-privee » ni « conception-ii-b » ;
ligne R-2059 filtrée ; ni le code du module, ni le harnais.

## Déroulé
- 14:18 — message de la conduite (passe r3). Accord relu par moi : `git fetch origin main`, puis
  `git show origin/main:registres/go.md | grep 'GO-2026-11-19-74'` et la ligne R-3871 de `registres/decisions.md` :
  D-18 (b), D-19 (a), D-20 (a) ; chaque lettre correspond à une option écrite de la liste v4.
- Lus, empreintes recalculées : contre-lecture de r2 (`71996527…`) ; rapport de la grille (`8d1616fc…`) ; sa
  contre-lecture (`d0485a40…`). Lus au dépôt : vérification courte de la session 16 (`45a0d875…`, ligne sur C-P3c) ;
  devis de la régénération des sondes de P3 et devis de la machine du crible (v), pour la forme ; devis de la
  phase 0 (`16d71feb…`) ; lignes GO-2026-10-17-01, GO-2026-10-20-06, GO-2026-10-20-07, GO-2026-10-04-08 de
  `registres/go.md` ; lignes de prix de `registres/depenses.md` des 18 et 19 novembre. Recompté :
  `git diff --name-status 7a54d43 HEAD -- src tests` : 734 ajoutés, 2 modifiés.
- 14:24 à 14:28 — programme de construction de r3, 67 remplacements exacts sur r2 ; un essai écarté (titre de la
  section 8), gardé sous `travail/essais-r3/` ; version rendue `160730b4…`. Gardes du programme : plus de case
  « À REMPLIR » hors de « Contre-lecture » ; un renvoi par précision.
- 14:28 à 14:33 — validateur ; liste finie (par programme : 144 cases) ; devis ; fiche v3 ; table ; note v6.

## Pièces neuves
- `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r3.md`
- `table-traitement-contre-lecture-r2-v1.md`
- `liste-finie-cases-grille-v1.md`
- `devis-pilote-papier-C-v1-brouillon1.md`
- `points-pour-le-module-et-la-configuration-v3.md`
- `note-differences-brouillon5-brouillon6-relance-v6.md`
- `problemes-brouillon6-relance-r3-v1.txt`
- `journal-redacteur-v6.md`
- Pas de `decisions-du-directeur-exigees-v5.md` : aucune décision neuve posée.
- travail : `travail/construire_brouillon6_relance_r3_v1.py` et son journal ; `travail/fiche_v1_sans_lignes.md` ;
  `travail/essais-r3/`.

## Doutes de cette suite
1. **Précision 37 tranchée sans décision du directeur.** Raison de principe tirée du texte (la réfutation de C-P2
   lit Ḡ là où ĉ n'est pas identifiable). Elle fixe quand C-P3a et C-P3b peuvent être « établies » : la conduite
   peut la requalifier ; les deux lectures et leurs conséquences sont écrites.
2. **Ḡ quand ĉ sort des bornes** : j'écris « celui que la forme fermée donne » sans avoir lu le programme ; à
   vérifier par l'auteur du module.
3. **Effectifs de la grille** (1 000 et 8 000 essais) repris des programmes figés, connus de moi avec leurs taux :
   je ne les ai pas choisis, mais je les ai écrits après avoir lu le rapport. Même réserve pour le choix des huit
   modèles : je les justifie par les mots de la clause, et ce sont ceux que le rapport a joués.
4. **Liste finie : colonnes « jouée »** déduites du rapport v1, non vérifiées sur ses sorties.
5. **D-19 rendue mécanique** : « sans traduction » et « nœud si plusieurs chaînes ou aucune » ne sont pas dans
   l'option (a) ; je ne connais pas le nom du champ qui porte le mode dans la configuration d'un organisme.
6. **CR-10 acceptée en partie** : sous la version (b), une case de C-P3c jouée par le rapport et au-dessus du seuil
   aux deux lectures l'emporte sur la vérification courte.
7. **Marqueur neuf `<<RAPPORT_RESERVE_INTENTION>>`**, non demandé.
8. **Séparateur de la précision 9** : un champ de configuration facultatif choisit entre deux règles de borne ; la
   configuration est scellée avec le texte, mais c'est une branche de plus à contre-lire.
9. **Devis** : la durée attendue, le prix du lancement, l'enveloppe de 150 USD (échéance 2026-11-30, non nommée par
   la prolongation de D-4), son cumul et le plafond de prix restent « À REMPLIR » ; le pire cas du § 3 emploie le
   prix implicite de l'accord (1,50 USD/h).
10. **Fiche v3, sections 0 à 5** : reprises de la fiche v1 par programme (numéros de lignes retirés, sept cellules
    mises à jour) ; non relues phrase par phrase contre r3.
