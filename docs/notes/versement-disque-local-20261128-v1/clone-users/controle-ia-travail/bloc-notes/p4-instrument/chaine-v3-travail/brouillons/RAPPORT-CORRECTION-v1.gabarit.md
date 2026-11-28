# Rapport de correction de la chaîne de P4-instrument (chaîne v3) — v1

Correcteur neuf de la chaîne v3 (je n'ai écrit ni la chaîne v1 ou v2, ni le module, ni aucune relecture ou
vérification). Session 16, du 2026-10-20 vers 23:30 UTC au 2026-10-21 vers {FIN} UTC.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.
Consigne : `…/consigne-correcteur-chaine-v3-v1.md`. Traitement appliqué : `…/traitement-verifications-chaine-v2-P4-v1.md`
(`10664a97505a49aa2b404e7500b6800466a222ed942815bc370cef79a7c90c6e`, sceau vérifié), et les deux rapports qu'il traite :
`…/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md` (`488a7e71…`) et
`…/verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md` (`16298dd2…`), sceaux vérifiés.

## Verdict

**Chaîne v3 conforme sur C d'essai**, avec le module v3. Toutes les décisions du traitement sont appliquées, chacune avec
son cas sain et ses artefacts ; `RAPPORTS_NOMS` porte les vingt-six noms, dans l'ordre exact du traitement. Les sept
bancs sont à 0 cas non conforme ; la répétition jouet est conforme (cinq passages aux codes 0, 2, 1, 124, 1 ; sept
récupérations conformes avec destruction ; vingt-sept artefacts à un seul KO, instance gardée avec état et heure limite ;
trois refus en code 2, dont ceux de la place et du clonage avec état et heure limite ; repli de l'affichage établi ;
lecture jouet : refus sans `--prereg` du run décisif et L3 sur le run non décisif ; aucun jeton ni aucune fenêtre
affichés). `verifications_p4_v1.py preuves` et `repetition` : code 0. Paires du texte écrites ; assemblage du candidat 2
avec les paires du module v3 : `problemes` = [], aucune collision. Aucun désaccord avec le traitement. Réserves : C
d'essai (pas le vrai C) ; quatre rapports à venir ; un choix du correcteur au-delà de la lettre de VC2-donnees-01
(ligne de l'instance gardée réécrite en repli). Le `tokenizer.json` de la session manquait au bloc-notes restauré : la
passe préliminaire du banc des contrôles a joué un substitut, demandé et annoncé ; la copie est revenue à 00:06 UTC et
la passe finale a joué le vrai tokeniseur (CV3-02).

## Ce qui est fait, décision par décision

| décision | fait | cas | journal |
|---|---|---|---|
| VC2-depense-01 (majeur) | `revocations_voisines` = `proposees` du vérificateur, à la lettre ; égale ligne à ligne sur les registres réels (essai unitaire `…/chaine-v3-travail/essais-unitaires/voisines_v3_v1.py`, 20 cas, 0 écart) | V : X01 à X05 (code 2), X06, X07 (code 2), témoins V55 (= V10), V58 (= V12), X08 (passe) ; registres réels à la tête de `main` (`git show`) et de l'arbre de travail : aucune fausse alerte (R00, R00b, R00c) ; L : XL01 à XL05 (code 2, aucune création), XL06 | V, L |
| VC2-depense-02 (mineur) | étiquette comparée dans Python dans l'arrêt et la surveillance | A : A14 à A17 ; S : S15b (code 2, aucune demande d'arrêt, rien de surveillé) | A, S |
| VC2-depense-03 (mineur) | `gardee` définie avant le contrôle de la place, appelée avant les deux sorties en code 2 | R : RX01 (place), RX02 (clonage impossible, artefact neuf), état et heure limite exigés par le module commun ; V : J29 à J31, J33 | R, V |
| VC2-depense-04 (mineur, forme) | ligne prête à quatre cellules, forme exacte du rapport | A : A00 (forme relue par une expression complète) | A |
| VC2-depense-05 (information) | une ligne de plus dans `lancement.txt`, relue avant la création ; phrase de la paire 5 | L : P00 | L |
| VC2-depense-06, -07, -08 | rien (comme décidé) ; -08 : chemins des journaux, voir réserves | — | — |
| VC2-depense, Texte 1 et 2 | paires 2 et 9, blocs à l'identique | comparaison v2 → v3 | — |
| VC2-donnees-01 (mineur) | textes lus à S ; repli : 40 premiers caractères, longueur, empreinte courte ; artefact « repli de l'affichage » à la répétition ; en plus, ligne de l'instance gardée réécrite hors du filtre (CV3-03) | R : `artefact-repli-de-l-affichage`, ligne `REPLI` ; V : J32 | R, V |
| VC2-donnees-02 (mineur) | entrée non ordinaire comptée et refusée (code 1, chemin écrit) par `fenetres`, `jetons` et le contrôle des traces | T : T09, T09b, T09c, T09d ; V : F15 à F18, T03 | T, V |
| VC2-donnees-03, -05, -06, -07, -08 | rien (comme décidé) ; -07 couvert par la lecture des textes à S | — | — |
| VC2-donnees-04 et -09 | phrases « Texte à ajouter » 2 et 4 dans la paire 7, mot pour mot ; phrases 1 et 3 aussi (leurs corrections sont faites) | comparaison v2 → v3 | — |
| `RAPPORTS_NOMS` | vingt-six noms ; bancs adaptés (K00, commentaires ; les bancs des contrôles et du scellement lisent la liste) ; `RAPPORTS_CONNUS` et paire 11 | V : K00 à K05 ; C ; E | V, C, E |

Détail ligne à ligne : `NOTES-CHAINE-v3.md`, section 2.

## Résultats des bancs

{RESULTATS}

## Paires du texte

`paires-candidat2-chaine-v3-v1.json` : `{SHA_PAIRES}` (onze paires ; 2, 5, 7, 9 et 11 changent ; détail :
`NOTES-CHAINE-v3.md`, section 5). Assemblage avec les sept paires du module v3 (`324c164f…`), dans les deux ordres :
même texte `{SHA_CANDIDAT}`, `problemes` = [], aucune collision.

## Constats du correcteur

{CONSTATS}

## Désaccords

Aucun. Toutes les décisions du traitement sont appliquées. Un ajout au-delà de la lettre (CV3-03) est signalé ci-dessus,
pas comme un désaccord : il se retire sans toucher au reste si la session le refuse (une ligne de la récupération, une
phrase de la paire 7, une condition de la ligne `REPLI`).

## Réserves

{RESERVES}

## Fichiers livrés

Chaque fichier a son sceau compagnon `.sha256` (forme « empreinte  nom »). Ce rapport n'est pas dans la table (son
empreinte est dans son propre sceau).

{TABLE_FICHIERS}
