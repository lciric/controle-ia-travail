# Vérification de la v2 — devis, instruments, pilote et devis à coût réduit de l'essaim — v1

- Relecteur de la v1 (Claude Opus 5.5, sous-agent), 22 novembre 2026. Aucune dépense, aucun appel de modèle, aucun réseau, aucun commit.
- Pièces : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v2/`, commit `4479e4fa` (`git diff --stat` vide). Les 29 compagnons sont conformes, aucun fichier n'est sans compagnon (`outils/verifier_compagnons_v1.py`).
- Mode d'échec affecté : **chiffre sans pièce**. Outils dans `outils/`, sorties dans `tables-v2/`, mises en place de rejeu dans `copie-v2/` et `rejeu-oracle-v2/`.

## Verdict

**Conforme avec réserves.** Les défauts D1 à D5 sont corrigés, de même que le défaut de l'oracle sur les trois noms essayés. Les quatre calculs se rejouent : à l'octet pour le devis v2, les épreuves du devis et le devis à coût réduit ; aux chemins près pour les épreuves de l'oracle et le pilote. Les puissances annoncées se rejouent par mon propre code.

Six réserves restent :
1. **Deux scripts ne se rejouent pas depuis le commit** : `epreuves_oracle_v67_v2.py` et `calcul_pilote_essaim_v1.py` lisent `../essaim-devis-instruments-v1/`, dossier absent du dépôt (le vrai dossier est `devis-et-instruments-v1/`). Il a fallu reconstruire l'arborescence pour les rejouer.
2. **Le contrôle des nombres laisse passer 3 de mes 9 artefacts** : une redéfinition plus bas, un motif qui figure deux fois, une ligne de la section C.8 dupliquée.
3. **L'oracle v2 laisse encore passer un verdict** sous une clé inventée dans le dictionnaire `lois`, et transmet un verdict écrit dans la valeur de l'identifiant. La classe n'en dépend pas.
4. **« La v1 sous-estimait le pire d'un facteur 1,8 à 2,4 »** est faux : le facteur va de 1,82 à 3,23, Kimi étant à plus de 3.
5. **« Les autres leviers ne donnent chacun qu'un facteur de 1,1 à 2,5 »** est contredit par la même pièce : (a) tout sur le modèle ouvert donne de ×2,2 à ×8,2.
6. **Le pire du pilote (204 USD) n'est un pire que si quatre gardes, encore proposées, existent** : plafonds d'entrée et de sortie, relances au plus 10 %, arrêt de la course au plafond. Avec une relance par appel, il vaut 370 USD.

## 1. Défauts de la v1 : corrigés ou non

| défaut | état | preuve |
|---|---|---|
| D1 : borne au pire 1,50 / 0,80 | **corrigé** : 1,60 / 0,90 / 3,50 lus dans la pièce et utilisés ; Fable 2,80, Argon et Carbon 2,90 par la formule | `epreuves_devis_v2.py` rejoué, sortie identique à l'octet à `epreuves-devis-v2.json` (`9fdc6716…`) ; épreuve « bornes au pire » tenue |
| D2 : un pire qui n'en était pas un | **corrigé** : plafonds de session, messages au plafond (supposé), fausses et copies, objets de contrôle aiguillés, relances 10 %, section C.8 à 105 % | `calcul_devis_essaim_v2.py` rejoué, identique à l'octet (`cb17a4ab…`) ; décomposition du pire haut 10 / 50 : 251 280 × 1,1 × 1,05 = 290 228,4 (`outils/controle_devis_v2_v1.py`) |
| D3 : nombres sans pièce | **corrigé** : 0,25 (l. 40, `8bd1e48a…`) ; 4 × 6 lu à `monde_riche_v4.py` l. 216-217 (relu : `for _p in range(4)` / `for _c in range(6)`) ; « 319 » retiré ; restes rangés sous `supposes` | `provenance_des_nombres` de la sortie |
| D4 : numpy et candidats | **corrigé** : numpy 2.4.6, candidats 226 / 225 / 224, essai 1 déclaré non rejouable | `bases-sans-modele-v2.md` ; conforme à mon rejeu de la v1 |
| D5 : définitions fixées après le monde 1 | **corrigé** (déclarées « à préenregistrer », échec du monde 0 laissé visible) | `bases-sans-modele-v2.md` § 2 |
| oracle : verdict sous un nom non listé | **corrigé pour les nœuds typés** ; **non fermé** pour les clés du dictionnaire `lois` et pour les valeurs (§ 2.2) | `epreuves_oracle_v67_v2.py` rejoué (identique hors chemins) ; mes artefacts E1 à E4 |
| neuf : chemin `../essaim-devis-instruments-v1/` | **nouveau défaut** : chemin mort dans `epreuves_oracle_v67_v2.py` l. 12, `calcul_pilote_essaim_v1.py` l. 17, `devis-essaim-communicant-v2.md` l. 3 et `bases-sans-modele-v2.md` l. 4-5 (les empreintes citées, elles, sont justes) | `tables-v2/` : échec `FileNotFoundError` dans ma copie simple ; rejeu tenu après reconstruction |
| neuf : « facteur 1,8 à 2,4 » | **divergent** : rapports pire v2 / pire v1 de 1,819 à 3,228 (Kimi 3,11 à 3,23 ; première espèce Claude 2,36 à 2,45) | `outils/controle_devis_v2_v1.py` |

## 2. Questions du point 1

### 2.1 Le contrôle des nombres attrape-t-il mes artefacts ?
Résultats dans `tables-v2/artefacts-relecteur-devis-v2.txt` (`outils/artefacts_relecteur_devis_v2.py`, textes en mémoire, la pièce n'est pas touchée).
- **Tenus** :
  - R0, pièce saine : passe.
  - R1, tarif de Kimi : refus.
  - R3, 0.80 écrit 0.8 : passe, comme il se doit.
  - R4, vérificateur scindé en deux affectations : exception `TypeError`, aucune sortie, donc rien de silencieux.
  - R5, borne 1,50 → 1,12 : refus.
  - R8, section C.8 105 % → 110 % : refus.
- **Cassés** :
  - **R2** : une seconde affectation `BORNE_TEST = {… 9.99 …}` placée plus bas **passe**. `affectation()` prend la première affectation rencontrée, alors que Python garderait la dernière.
  - **R6** : « marge de 10 % » → « 15 % » **passe**. Le motif figure deux fois dans la pièce (l. 40 et l. 70), et la valeur 0,10 est écrite en dur, non lue.
  - **R9** : une ligne « 150 % » ajoutée sous celle de la section C.8 **passe**. Le motif ne lit que la première occurrence, et 1,05 est écrit en dur.
- **Portée** : les pièces réelles sont d'abord lues à leur empreinte, donc ces trous ne jouent que sur une pièce changée **avec** une empreinte mise à jour. C'est justement le cas que le contrôle des nombres prétend couvrir.

### 2.2 L'oracle v2 refuse-t-il un verdict sous un autre nom ?
Résultats dans `tables-v2/artefacts-relecteur-oracle-v2.txt`.
- **E1** : une clé `promue_juge` ajoutée dans le dictionnaire `lois` d'une `par_sous_population` **passe**. Code 0, carte classée vraie ; la garde n'examine pas les clés de ce dictionnaire.
- **E2** : `identifiant = "G1-a-01|PROMUE|survit"` **passe** et **se retrouve dans la sortie**. La liste blanche porte sur les clés, pas sur les valeurs.
- **E3** : un type inconnu qui porte `promu` et `rang` passe, classé « rien ». C'est sans effet sur la classe, mais la garde ne lit pas ce nœud.
- **E4** : un verdict codé dans un poids numérique passe, comme prévu : un canal de contenu n'est pas séparable par les noms.
- **Ce qui tient** : dans les quatre cas, la classe ne dépend pas du champ ajouté. La garantie réelle est l'invariance de la classe, qui est rejouée ; ce n'est pas la garde par les noms.

### 2.3 Le vrai pire de la v2 face à mon recalcul
Mon recalcul de la v1 (`tables/pire-alternatif-v1.txt`, P3) donnait 236 448 USD au haut sur l'espèce à 10 / 50 ; la v2 donne 290 228 USD. L'écart s'explique entièrement :
- messages au plafond : +4 248 ;
- aiguillage des objets de contrôle : +10 584 ;
- relances et section C.8 : × 1,155.

La v2 dépasse mon recalcul P3 dans toutes les cellules (par exemple, première espèce Claude au cas attendu : 95 532 contre 73 837).

Le pire de la v2 omet encore deux choses : la majoration de 25 % que propose la même pièce d'affinage (l. 44), et la machine.

## 3. Pièces neuves : table des chiffres

Le pilote a été rejoué dans `rejeu-oracle-v2/` ; sa sortie est identique hors chemins à `calcul-pilote-essaim-v1.json` (`332328df…`). Le devis à coût réduit a été rejoué à l'octet (`dbcc7721…`).

### 3.1 `pilote-instrument-essaim-v1.md` (`5e48b9f3…`)

| chiffre | pièce | rejoué |
|---|---|---|
| coûts P-min / P-std / P-std+b / P-24 × 4 espèces (est. 6 000 et 12 800 ; pire) | `calcul-pilote-essaim-v1.json` | oui (24 cellules, à l'unité) |
| 744 appels ; P-24 − P-std = +57 / +102 / +204 | sortie | oui |
| (b) +47 % ; sans (b) −32 % ; 12 → 8 mondes −33 % ; 3 → 2 générations −33 % ; une espèce −50 % | sortie | oui (+46,7 % à l'estimation à 6 000 ; jusqu'à +50,6 % au pire) |
| B3 : médiane 0,69 ; écart-type 0,1378 ; √2 × 0,1378 = 0,195 | sortie des bases v1 (`4dcdeacf…`) | oui |
| puissances (table § 2, 18 cellules) | sortie, `SeedSequence(20261123)` | **oui**, et retrouvées par mon code indépendant (`outils/puissance_independante_v1.py`, graine 777001) : n = 12, δ = 0,15 → 0,949 (sd 0,15) et 0,789 (sd 0,195), contre 0,944 / 0,803 |
| « puissance 0,80 à 0,94 » | idem | oui **sous hypothèse normale non bornée**. Couverture bornée à 1 et discrète (sur 7 composantes), autour des B3 réelles : **0,885 / 0,698** (même outil) |
| 24 000 ≈ 1,9 × 12 800 | arithmétique | oui (1,875) |
| 12 800 jetons pour deux cartes (Kimi) | `devis_multi_generations_v1.py` l. 29, qui cite un verdict v67 non relu | **non** à la source (cité de seconde main, comme la note le dit) |
| « environ 6 minutes par monde » pour C0 à C8 | aucune pièce citée | **orphelin** |
| « 2 mondes sur 12 en v4 » perdus à deux générations | aucune pièce citée | **orphelin** |
| pire de 204 USD | sortie | **rejoué, mais conditionnel** (§ 4) |

### 3.2 `devis-cout-reduit-essaim-v1.md` (`5f339ddb…`)

| chiffre | pièce | rejoué |
|---|---|---|
| références 2 809 / 4 669 / 8 389 / 10 249 | sortie (égales au devis v2) | oui |
| (a) 2 450 / 3 859 / 6 678 / 8 087, 60 h, pire 426 h ; tout 1 250 (×2,2 à ×8,2), 196 h, pire 1 516 h, 3 283 | sortie | oui ; débits, utilisation et mise en route : HYPOTHÈSES déclarées ; 1,4 USD/h « donné par la commande » (aucune pièce du dépôt) |
| vérificateur 862 USD | `jetons_programme_attendu.tests.fixe_usd` = 862,33 | oui (hors marge ; 948 avec) |
| (b) 1 879 à 5 599 ; cache Fable 6 367 ; lecture 0,20 et écriture 2,0 | sortie ; `relecture_fable_api_v3.py` (`95bea064…`) | oui ; remise de 50 % : hypothèse déclarée |
| (c) 1 139 à 4 937 ; table 1 − (1 − q)^m ; 12 tests par monde | sortie | oui |
| combinaisons 582 / 974 / 1 758 et facteurs | sortie | oui |
| pilote : 57 / 102 ; 204 ; 93 à 8 000 ; ≈ 51 ; modèle ouvert 25 ; pire 347 ; 16,5 h ; 214 h | sortie | oui (214,5 h écrit « 214 ») |
| **facteur caché « mise en route / 5 »** dans le pilote sur modèle ouvert | `calcul_devis_cout_reduit_v1.py` l. 146 | **orphelin** : absent de `hypotheses` et du texte |
| facteurs 28 à 49 (Kimi), 46 à 82 (Claude), « ×23 à ×49 » | arithmétique | oui |
| « les autres leviers : 1,1 à 2,5 chacun » | (a) tout : ×2,2 à ×8,2 dans la même pièce | **divergent** |

## 4. Le pire du pilote, 204 USD sur Kimi, est-il un vrai pire ?

Non au sens arithmétique, oui seulement par une règle d'arrêt.
- 204 = 12 mondes × [24 appels de proposeur × (23 200 × 2 + 24 000 × 10) / 10⁶ + 12 messages × (6 000 × 2 + 2 000 × 10) / 10⁶ + 26 × (même proposeur)] × 1,1 × 1,05 = 176,45 × 1,155 = 203,8. Recalculé à la main, conforme à la sortie.
- La borne tient si quatre conditions sont **imposées** : sortie au plus 24 000 jetons, entrée au plus 23 200, messages au plus 6 000 / 2 000, relances au plus 10 % des appels. Les quatre sont des PROPOSITIONS (« garde du lanceur à exiger »), aucune n'existe.
- 6 000 jetons d'entrée par message, soit deux fois l'hypothèse, n'ont pas de pièce.
- Avec une relance permise par appel, le pire vaut 176,45 × 2 × 1,05 = **370 USD**.
- Seule la règle « arrêt de la course au vrai pire » en fait une borne dure. Elle doit être écrite comme garde du lanceur et éprouvée sur un cas sain et sur un artefact (R5) avant le GO.

## 5. Équité d'information entre B3 et les agents (trois lignes)

Non, la comparaison n'est pas équitable en l'état. B3 ajuste sur 2 000 instances brutes, avec des seuils candidats qui contiennent la régularité publique « seuil 0 ». Les agents ne voient qu'une case d'environ 9 000 jetons, qui ne peut pas contenir ces données. Or la règle d'arrêt du § 5 du pilote ferme le programme sur un « ne bat pas, net » : il faut d'abord recalculer B3 sur l'information servie (recommandation de l'auteur), au préenregistrement et sur les mondes neufs ; sinon un résultat négatif ne dit rien de la communication.

## Relevé de méthode

### Chaîne de raisonnement
1. Les 29 compagnons de la v2 sont conformes, et le dossier est identique au commit `4479e4fa` (`verifier_compagnons_v1.py` : ok=29 ko=0 ; `git diff --stat` vide).
2. `calcul_devis_essaim_v2.py` (`9fde22b0…`), rejoué dans `copie-v2/`, est identique à l'octet à `calcul-devis-essaim-v2.json` (`cmp` vide).
3. `epreuves_devis_v2.py` (`1beea5a5…`), rejoué, est identique à l'octet à `epreuves-devis-v2.json` ; les 11 épreuves sont tenues.
4. D1 est corrigé : par le pas 3, les bornes valent 1,60 / 0,90 / 3,50 / 2,80 / 2,90 ; par le pas 2, `provenance_des_nombres.BORNE_TEST`, ligne 20, `710954c7…`.
5. Le pire haut 10 / 50 se décompose en 251 280 × 1,1 × 1,05 = 290 228,4 (`controle_devis_v2_v1.py`, sur la sortie du pas 2). L'écart avec mon P3 vient de trois postes nommés (§ 2.3).
6. Les rapports pire v2 / pire v1 vont de 1,819 à 3,228 (même outil, sur ma sortie v1 rejouée et sur celle du pas 2) ; « 1,8 à 2,4 » est donc divergent.
7. Mes artefacts R2, R6 et R9 passent le contrôle des nombres (`tables-v2/artefacts-relecteur-devis-v2.txt`). Le code le justifie : `affectation()` rend la première affectation trouvée ; `nombres_affinage` et `nombres_conception` écrivent la valeur en dur et ne cherchent que la ligne.
8. `epreuves_oracle_v67_v2.py` échoue dans une copie simple (`FileNotFoundError` sur `../essaim-devis-instruments-v1/`). Le dossier `docs/notes/organisme-essaim-communicant-v1/essaim-devis-instruments-v1` n'existe pas (`ls`). Rejoué dans `rejeu-oracle-v2/`, il donne des résultats identiques hors chemins (12 fichiers).
9. Mes artefacts E1 et E2 passent l'oracle v2 et la classe reste inchangée (`tables-v2/artefacts-relecteur-oracle-v2.txt`). Le code l'explique : les clés du dictionnaire `lois` ne sont pas examinées (`garde_grammaire`, l. 105-107), et les valeurs de la liste blanche non plus (l. 126).
10. `calcul_pilote_essaim_v1.py` (`b3770331…`) échoue lui aussi dans une copie simple, sur le même chemin mort. Rejoué dans `rejeu-oracle-v2/`, il est identique hors chemins à `calcul-pilote-essaim-v1.json`.
11. Les puissances se retrouvent par un code et une graine indépendants : 0,949 et 0,789 contre 0,944 et 0,803, à n = 12 et δ = 0,15. Sous couverture bornée et discrète : 0,885 et 0,698 (`tables-v2/puissance-independante-v1.txt`).
12. `calcul_devis_cout_reduit_v1.py` (`6c786ba9…`), rejoué, est identique à l'octet à `calcul-devis-cout-reduit-v1.json`. Les chiffres de la note en sont tirés, sauf « 1,1 à 2,5 » (divergent par sa propre table) et le « / 5 » de la ligne 146 (sans déclaration).
13. Le pire de 204 USD se recalcule à la main sur les constantes du script, lignes 21 à 28 (§ 4). Ces constantes sont des PROPOSITIONS ⇒ c'est une borne conditionnelle.
14. **Supposé** : l'évaluateur de la grammaire ignore les clés inconnues, d'après la classe inchangée en E1, sans lecture de `monde_riche_outils_v1.probas`.

### Objets de contrôle
- **Contrôle des nombres.** Vrai par construction : la pièce saine (R0), et 0.8 écrit pour 0.80 (R3) ; je m'attendais à « passe » dans les deux cas, et c'est ce qu'il rend. Faux par construction : R1, R2, R5, R6, R8, R9, où je m'attendais à un refus. Il en rend un sur R1, R5 et R8, mais **laisse passer R2, R6 et R9**. Le mécanisme est donc partiellement mort pour les redéfinitions et les motifs qui figurent deux fois.
- **Garde de l'oracle v2.** Faux par construction, avec verdict glissé : E1 et E2, refus attendu ; ils **passent**. Vrai par construction (les cartes saines de l'auteur, a1) : passe attendu ; passe rendu. Les classes restent invariantes dans tous les cas.
- **Mon simulateur de puissance.** Faux par construction : δ = 0, où le taux de rejet doit rester ≤ 0,05 ; il rend 0,049 et 0,041 (normale), 0,028 et 0,033 (bornée). Vrai par construction : δ = 0,6, où il doit approcher 1 ; il rend 1,000.
- **Mes comparateurs.** `comparer_json_hors_chemins_v1.py` rend « octet : faux, hors chemins : vrai » sur le pilote, où seul le chemin diffère, ce qui était attendu. Sur le devis v2, `cmp` est vide, ce qui confirme l'égalité exacte.

### Premier pas non justifié
Le pas 14 : je n'ai pas lu `monde_riche_outils_v1.probas`. Ce qui le justifierait : lire la branche `par_sous_population` pour voir si une clé non numérique de `lois` est ignorée par construction ou par hasard.

### Mode d'échec affecté
**Tenu avec réserves** pour « chiffre sans pièce » sur la v2. Chiffres divergents :
- « facteur 1,8 à 2,4 » (pas 6) ;
- « 1,1 à 2,5 » (pas 12).

Chiffres orphelins :
- « / 5 » (pas 12) ;
- « 6 minutes par monde » et « 2 mondes sur 12 » (§ 3.1).

Non rejouables depuis le commit : deux scripts, à cause d'un chemin mort (pas 8 et 10).

Tout le reste est rejoué : `tables-v2/`.

### Dérivation de l'énoncé seul
Sans objet : je suis vérificateur, non agent de re-dérivation. La puissance a cependant été recalculée par ma propre voie (pas 11).

### Trouvaille de côté
- Le pire de la v2 ignore la majoration de 25 % que propose la pièce d'affinage, l. 44 : à porter devant le directeur ou à écarter nommément.
- Le pilote sur modèle ouvert compte les messages à 12 800 jetons de sortie, comme les proposeurs (l. 141) ; c'est une sur-estimation sans conséquence.
- `P-2gen` rend 495 appels par troncature (495,99 calculés).

### Évaluateur et conseil
Ce qui juge : l'égalité à l'octet ou hors chemins, admise sur les témoins ci-dessus ; mes artefacts ; mon simulateur, admis à δ = 0 et à δ = 0,6. Un bon jugement immérité viendrait d'une épreuve écrite par l'auteur qui ne vise que les cas qu'il a prévus. C'est ce qu'ont montré R2, R6, R9, E1 et E2 : les épreuves de l'auteur passaient toutes, et les miennes, prises hors de son jeu, en cassent cinq.
