EXPLORATOIRE, NON OPPOSABLE (R-522)

# Différences entre le brouillon 3 (`cb39c12b…`) et le brouillon 4 du texte de l'organisme retenu

Les brouillons 1, 2 et 3 restent intacts. Le brouillon 4 est écrit comme un fichier entier par `assembler-brouillon4-v1.py`, rendu : il lit le brouillon 3, vérifie son empreinte, applique 47 retouches dont chaque ancre se trouve exactement une fois, et écrit le texte. Tout passage non listé ici est égal au brouillon 3 ; le relancer le montre.

## 0. Ce que le fichier des différences du brouillon 3 n'avait pas déclaré (du brouillon 2 au brouillon 3)
Comparaison directe des deux brouillons, section par section, refaite ici. Sections 3, 11 et 14 : égales. Changées sans être toutes déclarées :
- **Section 9** (déclarée « inchangée » à tort) : la sensibilité et le rejet du flagrant se calculent pour « chaque oracle, pour ses propres conditions (10.3) » et non plus pour « l'oracle de la règle ; l'autre rapporté » ; la lisibilité du jumeau, pour « chaque oracle, sur sa propre passe » ; les renvois de nœud renumérotés (9 devient 6).
- **Section 2** : 2.2, renvoi « (nœud 2) » devenu « (6 bis) » ; 2.3 point 3, « selon la ligne Oracle de la règle » devenu « selon l'issue de la règle composée », les deux variantes de la consigne scellées avant l'étalonnage ; 2.3 point 7, ce qui est rendu à la session (existence des deux variantes et leurs empreintes).
- **Section 7** : ligne « ancre commune » (première action à coupe conforme et à coût lisible) ; entrée de la règle : « l'oracle que l'issue de la règle composée a nommé ».
- **Section 12** : paragraphe ajouté (la règle composée et le contrôle du premier coût ne coûtent aucun appel) ; renvoi de nœud (10 devient 7).
- **Section 16** : ligne 9 (quatre composantes) ; lignes 14 et 15 ajoutées (désignation après l'étalonnage ; contrôle chiffré du premier coût).

## 1. Ce qui change de fond, du brouillon 3 au brouillon 4
1. **Quatrième issue « non calculable », écrite d'avance** (M1) : en-tête, 5.1, 10.3 étape 1, 10.6, section 15, `designation_v5`. La coupe en échec met les deux oracles en défaut : issue « ne part pas », en 10.3 comme en 15. Plus aucun « arrêt, nœud » : aucune issue ne mène à une décision prise après l'étalonnage.
2. **Les sept nœuds se tranchent avant le scellement** (M2) : table des nœuds en tête (une ligne chacun, défaut = recommandation) ; section 17 récrite en entier, avec la variante du texte sous chaque option ; options non dimensionnées dites « non prêtes ». Le plafond de tours (10.2) reçoit deux entrées scellées de plus, fixées par le nœud 7 (oracles par tour ; actions d'oracle hors tours), écrites pour chaque option.
3. **Nœud 2, option (b), dimensionnée** par un passage déclaré d'avance, unique, à entropie neuve : 5.2 bis (neuve), 10.4 ter (neuve), variantes en 10.2, 10.3, 10.6. Le nœud n'est pas tranché ; la recommandation passe de (b) à (a), par la règle écrite avant le passage.
4. **La page pour le directeur** (M3) : 5.3 (plage par dispersion ; effet d'un texte portant un huitième du niveau ; paragraphe « cette page ne penche pas »), 5.4 récrite, 5.5.
5. **Contrôle du premier coût** (M4, m1, m3, m9) : risque de non-validité écrit en clair en 6 bis.2 ; aucune sixième donnée ; discrétisation de la convolution (scores × 1 008) ; garde de validité portée par `controle_premier_cout_v5`, cas sain et artefact ; approximation normale du passage dite.
6. **Pente de fuite** (m5) : loi dite approchée et un peu libérale, niveau réel écrit ; loi de Student rapportée, non retenue.
7. **Auteurs** : un second rédacteur ; « je » défini en en-tête. Outil d'assemblage du brouillon 3 dit perdu ; annexe C refaite (deux scripts de dépendance, empreintes entières, ordre des arguments).

## 2. Retouches, section par section
| section | retouche |
|---|---|
| titre, en-tête | brouillon 4 ; brouillon 3 parmi les textes intacts ; quatrième issue ; deux encadrés neufs (sept nœuds ; nœud 2 (b)) ; statut ; auteurs |
| table des nœuds | neuve, avant la section 0 |
| 0 | ligne « règle composée » : « non calculable » ; chiffres sous l'instrument planté |
| 1.2 (e) | « approche » les quantiles, avec les écarts (m2) |
| 1.4 | heures déclarées, non vérifiables (m11) ; point 7 neuf (brouillon 4, passage neuf, outil perdu) |
| 5.1 | points 4 et 5 ; refus du second passage porté par le lanceur (m8) ; coupe en échec ; nœuds tranchés avant le scellement |
| 5.2 bis | neuve |
| 5.3, 5.4, 5.5 | M3 ; m7 |
| 6 bis.1, 6 bis.2, 6 bis.3, 6 bis.5 | discrétisation ; risque de non-validité ; loi jouée ; 1,3 devient 1,4 |
| 8 | loi de la pente de fuite ; 85 % devient 84 % (m4) ; deux sens de « non calculable » ; la pente ne distingue pas fuite de code et texte porteur |
| 10.2, 10.3 | R_plafond et ses entrées par option du nœud 7 ; m_P ; étape 1 ; coupe commune ; variantes des nœuds 2 et 4 |
| 10.4 ter | neuve |
| 10.6 | phrase « part » sous le nœud 2 (b) ; phrase « en défaut » (m10) ; phrase « non calculable » |
| 12 | coût par option du nœud 7 ; (b) du nœud 2 sans effet sur le coût |
| 13 | `epreuve_centrage_v5` (essai de l'erreur type robuste) ; `designation_v5` ; `controle_premier_cout_v5` ; `branches_v5` ; puissance de la grandeur de lecture non dimensionnée |
| 15 | trois lignes ; phrase finale |
| 16 | ligne 16 neuve ; l'ancienne 16 devient 17 |
| 17 | récrite en entier |
| 18 | une ligne changée (m7), trois ajoutées |
| Vérification ; annexe A (neuve) ; annexe A bis (l'ancienne A, ligne m1 corrigée) ; annexe B (une ligne) ; annexe C (refaite) | — |

## 3. Chiffres qui changent ou s'ajoutent
| grandeur | brouillon 3 | brouillon 4 |
|---|---|---|
| [N], conditions remplies au point situé, instrument planté | « non dimensionné » | 0,0 % ; 0,0 % ; 0,0 % (régénéré, même passage : 0,0 % ; 0,0 % ; 0,7 %) |
| [N], conditions remplies sur la grille, instrument planté | — | 3,7 % ; 8,3 % ; 9,4 % (régénéré : 7,5 % ; 12,3 % ; 11,6 %) |
| règle composée sous l'instrument planté : issue [N] / [P] / ne part pas | — | 4 % à 9 % / 84 % à 89 % / 6 % à 7 % |
| bascule contre le maître ancré, instrument planté | — | 82 % ; 69 % ; 70 % (régénéré : 71 % ; 57 % ; 63 %) |
| part à tort contre un excès tenu en niveau, instrument planté | — | 89 % ; 85 % ; 84 % (régénéré : 86 % ; 81 % ; 82 %) |
| marge de moitié ôtée pour [N] (rapporté) : conditions remplies au point situé | « non dimensionné » | 8 % ; 26 % ; 38 % ; issue [N] là où [N] ne distingue pas le maître ancré : 4 % ; 13 % ; 19 % |
| pente de fuite, arrêt à tort | 1,7 % | 1,7 % (passage d'origine) ; 1,6 % à 1,9 % (passage neuf) ; Student : 1,5 % à 1,8 % |
| texte à un huitième, composante | 85 % à 89 % | 84 % à 89 % |
| dommage sous le seuil du contrôle du premier coût, ancrage 0,94 | 1,3 décade | 1,4 décade |
| [N] part à ancrage 0,7 (page) | 26 % à 62 % | 26 % à 62 % aux dispersions 0,05 et 0,08 ; 5 % à 11 % à 0,12 ; 15 % à 41 % si le texte porte un huitième du niveau |

## 4. Ce qui ne change pas
Organisme ; les deux oracles, leurs constantes, leurs épreuves et leurs niveaux ; règle d'acceptation ; conditions de départ sous les options par défaut ; règle composée (ordre, thèses, consignes) ; contrôle du premier coût (statistique, niveau, usage par défaut) ; témoin ; graines ; sections 2, 3, 4, 6, 7, 9, 10.1, 10.4, 10.4 bis, 10.5, 11, 14.
