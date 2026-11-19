EXPLORATOIRE, NON OPPOSABLE (R-522)

# Différences entre le brouillon 2 (`a5dc6b36…`) et le brouillon 3 du texte de l'organisme retenu

Les brouillons 1 et 2 restent intacts. Le brouillon 3 est le brouillon 2 retouché par un outil (`assembler-brouillon3-v1.py`) : chaque retouche remplace un passage repéré une seule fois ; les sections non listées ici sont égales au brouillon 2.

## Ce qui change de fond
1. **La ligne de désignation est remplie** : l'oracle de la règle est désigné après l'étalonnage par une règle composée scellée avant lui ([N] si faisable, sinon [P], sinon rien) — décision de Lazar. Section 5 récrite en entier : la règle, les revendications par issue, la page, les deux désignations fixes écartées avec leurs raisons. Erreurs de la règle composée en 10.4 bis. Module `designation_v5`.
2. **La page dit une plage, non un point** (5.2) : trois colonnes, une par lecture de la troisième donnée. Quatrième donnée déclarée. La grandeur que l'étalonnage rapporte pour mesurer la lecture est définie (section 13).
3. **Épreuve de fuite avec règle** : quatrième composante de l'épreuve du centrage de [N], « pente de fuite » ; les quatre composantes passent au niveau 1/80 (elles étaient trois à 1/60). Dimensionnée par un passage déclaré.
4. **Contrôle chiffré du premier coût** : section 6 bis neuve ; cinquième donnée déclarée ; passage déclaré à part ; module `controle_premier_cout_v5`.
5. **Deux variantes de la consigne du maître**, scellées avant l'étalonnage ; l'issue choisit (2.3).
6. **Nœuds** : dix deviennent sept. Tranchés : la désignation ; le contrôle du premier coût. Clos par passage : la fuite. Neuf : l'instrument de la branche [N] (nœud 2) ; le contrôle du premier coût comme règle (nœud 1).

## Chiffres qui changent ou s'ajoutent
| grandeur | brouillon 2 | brouillon 3 |
|---|---|---|
| [N] au point situé, maîtres distingués | aucun | aucun, deux ou trois selon la lecture |
| [N], conditions de départ remplies au point situé | « ne part jamais » | 0,0 % à 0,3 % selon la lecture |
| épreuve du centrage de [N] | trois composantes à 1/60 ; arrêt à tort 4,7 % | quatre à 1/80 ; arrêt à tort 5,1 % à 5,4 % |
| fuite d'un quart, de moitié, entière | non vue | arrêtée 100 % des fois |
| biais de réécriture de 0,05 par pas | arrêté 63 % | 60 % à 79 % selon la lecture |
| premier coût : ×2 vu sur 64 épisodes | non chiffré (×1,8 : une fois sur deux ; ×3,2 : 98 %, premier coût normal) | 96 % (loi mesurée, valeurs rondes) |
| issue de la règle composée | — | [N] 8 % à 13 % ; [P] 80 % à 85 % ; rien 7 % |

## Mineurs traités
« Première action bornable exigée » aligné sur 2.2 ; 98 % dit « en moyenne des neuf cellules, 97 % au point situé » ; ×6 dite aussi pour ce qu'elle concède au cumul ; compagnons `.sha256` pour chaque fichier ; heures par `date -u` dans les grilles et le journal.

## Ce qui ne change pas
Organisme ; les deux oracles et leurs constantes ; fenêtre de lecture ; réécriture couplée ; instrument régénéré ; conditions de départ de chaque oracle et leurs seuils ; témoin ; coût en appels ; sections 3, 4 (hors une phrase), 9, 11, 14.
