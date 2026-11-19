# Papier C — table de remplissage des cases du directeur, version r1 — v1

Écrite par le rédacteur (Claude Fable 5.2), le 2026-11-19. Source des décisions, relue par moi et non prise du seul
message de la conduite : `registres/go.md` sur `origin/main` (commit `784cfcd4`), ligne **GO-2026-11-19-53** ; mot de
Lazar du 2026-11-19 à 12:38:35Z, « go recos », point 5 ; `registres/decisions.md`, ligne R-3802. Texte de la ligne :
« D-1 (b), poids de HC2 0,5 ; D-2 (a), trois niveaux ; D-3 (a) ; D-4 (a), GO-2026-10-17-01 et GO-2026-10-20-07
prolongées jusqu'au 2026-12-31, plafond inchangé ; D-5 (a) ; D-6 (a) ; D-7 (a) ; D-8 (a), masque accepté ; D-9 (a)
sous réserve du rapport de la grille entière et de la ligne C-P3c, sinon (b) ; D-10 à D-14 (a) ; D-15 (i) et (n) ;
D-16 (a) ; D-17 (a). »

Avant : version c2 (`7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61`). Après : version r1
(`e12f16fa1460149344cd5d68b614294ea502c4c7fc24bc86970cafcfbaafc8b2`). « v3 » = `decisions-du-directeur-exigees-v3.md`
(`fb05e3bf…`). Les numéros de ligne « r1 » sont ceux de la version r1 ; « c2 », ceux de la version c2. R- =
identifiant du remplacement dans `travail/construire_brouillon6_relance_r1_v1.py`.

Chaque lettre de la ligne du registre correspond à une option écrite de la liste v3. Aucune n'a deux lectures de
lettre. Un point de lecture, sur la condition de D-9, est dit en bas.

| décision | option retenue | lieu dans r1 | texte recopié depuis | remplacements |
|---|---|---|---|---|
| D-1 | (b), poids 0,5 | Hypothèse, HC2, « Poids de HC2 », l. 459 | v3, l. 51 (« le nombre que tu donnes ») ; nombre de la ligne du registre | R-D1 |
| D-2 | (a), trois niveaux | Plan, section 3, « Niveaux du plaidoyer », l. 1118 ; effectifs, l. 1210 ; verrou 4 ; Combinaisons, « Niveaux » | v3, l. 68 (« k_P = 3 ») ; c2, l. 1212 (« 300 à 600 si k_P = 3 ») | R-D2a, R-D2b, R-V2, R-D15l |
| D-3 | (a), verdict | ligne C-P4c, inchangée (table de prédiction, Seuil, Critères) | texte déjà écrit en c2 dans la version (a) | aucun au corps ; verrou 1 (R-V1) |
| D-4 | (a), prolongation au 2026-12-31, plafond inchangé | verrou 8, l. 179 ; paragraphe GO ; Plan, section 1, titre l. 998 et accord par lancement | ligne du registre (dates et « plafond inchangé ») | R-V8, R-GOb, R-D4a, R-D4b |
| D-5 | (a), non mesurée | Hypothèse l. 468 ; TC.2 l. 1162 ; réserve 19, inchangés | texte déjà écrit en c2 | aucun au corps ; en-tête (R-00c) |
| D-6 | (a), non mesurée | TC.2 l. 1166 ; réserve 19 l. 1340, inchangés | texte déjà écrit en c2 | aucun au corps ; en-tête (R-00c) |
| D-7 | (a), inclus, rapporté | Métrique, point 14, témoin lexical, inchangé | texte déjà écrit en c2 | aucun au corps ; en-tête (R-00c) |
| D-8 | (a), masque accepté | Métrique, point 14, « Lecture filtrée », l. 834 ; Combinaisons, « HC2b et l'intention », l. 1458 | c2, l. 1459-1461 (version (a), mot pour mot) ; c2, l. 818-821 (masque) | R-D8a, R-D8b, R-D8c |
| D-9 | (a) sous réserve du rapport de la grille entière et de la ligne C-P3c ; sinon (b) | Prédiction, stabilité de rang, l. 562-574 | c2, l. 555-556 (version (a)) et l. 556-559 (version (b), mot pour mot, gardée comme repli) ; condition : ligne du registre | R-D9 |
| D-10 | (a), à part | Hypothèse, « Périmètre », l. 489, inchangé | texte déjà écrit en c2 | aucun au corps |
| D-11 | (a), verser puis porter au texte | verrou 2, l. 143, inchangé | texte déjà écrit en c2 | aucun au corps |
| D-12 | (a), la conduite consigne | verrou 2, l. 136 ; Hypothèse l. 395, inchangés | texte déjà écrit en c2 | aucun au corps |
| D-13 | (a), prédictions gardées, contre-indices dits | Prédiction, contre-indices, l. 650, inchangé | texte déjà écrit en c2 | aucun au corps ; verrou 1 (R-V1) |
| D-14 | (a), liste écrite | Métrique, point 14, « Agrégations lues », l. 829 | texte déjà écrit en c2 ; « acceptée par le directeur » à la place de « par ce rédacteur » | R-D14 |
| D-15 | (i) et (n) | Prédiction, « HC2 : confirmation, réfutation et côté négatif », l. 527-548 ; Hypothèse ; table de prédiction ; Seuil ; Critères (ligne C-P4 HC2) ; Combinaisons | c2, l. 533-537 (version (i), mot pour mot, gardée) ; c2, l. 529-531 (version (n), mot pour mot) ; versions (ii) et (m) retirées | R-D15a à R-D15l |
| D-16 | (a), une action décide | Métrique, point 14, « Trajectoire », l. 852 ; Critères, lignes C-P4 et C-P4c | c2, l. 841-843 (version (a), mot pour mot) | R-D16a, R-D16b, R-D16c |
| D-17 | (a), nombres seuls | Seuil, « Bras contrôlabilité », l. 957 ; Métrique, point 19 (b2), l. 894 ; Combinaisons | c2, l. 951-952 (version (a), mot pour mot) | R-D17a, R-D17b, R-D17c |

## Ce qui n'a pas pu être recopié tel quel

1. **D-9, la condition.** La ligne du registre dit « (a) sous réserve du rapport de la grille entière et de la ligne
   C-P3c, sinon (b) ». La liste v3 n'écrivait pas cette condition comme une option (elle était dans ma
   recommandation). Je l'ai écrite ainsi, et c'est une lecture : la version (a) vaut si le rapport existe au
   scellement et couvre la grille entière et C-P3c ; une statistique que ce rapport trouve au-dessus du seuil suit
   la clause de repli déjà écrite (« rapportée sans verdict ») ; sans ce rapport, ou s'il est incomplet, la
   version (b) s'applique. L'autre lecture possible — « si le rapport est défavorable, tout passe en (b) » — n'est pas
   celle que j'ai écrite. La conduite confirme ou corrige à la dernière passe.
2. **D-15, version (n).** La phrase recopiée garde « du côté ou des côtés que fixe la version (i) ou (ii) » ; j'ai
   ajouté « La version retenue étant (i), ce sont les deux côtés ». Dans les lignes de table et de combinaisons, la
   règle retenue est redite en clair (bornes de la version (i), réfutation par niveau), ce qui est une rédaction
   courte et non une recopie.
3. **D-2.** Le cas « k_P = 1 » disparaît des combinaisons et des effectifs, puisque trois niveaux sont retenus ; les
   mentions générales « si k_P ≥ 2 » de la Métrique et du Seuil restent, vraies avec trois niveaux.
4. **D-4.** Aucune option de la liste ne portait de texte à recopier : les dates viennent de la ligne du registre.
