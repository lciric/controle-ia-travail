# Lot B — confrontation : carte du contrôle et failles internes — lisez-moi — v1

Audit des failles de notre contrôle, lot B, rendu par un sous-agent neuf de la lignée conv-audit. Brief :
`LISEZMOI-brief-audit-v1.md` (`1785c74df8950f7af449012dbe4f58bd4e76ae113fe7aae93df2447b0528c97e`, vérifiée), § 1 à 3 et
lot B du § 4. Horodatage : dernière ligne du fichier (heure lue sur `date -u` dans la commande qui l'a écrite).

## 1. Méthode

1. **Vérifications.** Brief : empreinte conforme. `fournis/` : 47 fichiers sur 47 conformes à `EMPREINTES-fournis-v1.txt`.
   Complément de session-depot : `fournis-complement/audit-litterature-session-depot-v1.md`, empreinte
   `29b32f620cb2310fad83166fd4f2957b3ce43b1c3dea090834d8c28f86e4823b`, conforme au préfixe donné par le coordinateur.
2. **Lecture intégrale** des pièces demandées : programme v2 ; brief v2 ; état de l'art v1 ; dossier `etat-de-l-art/`
   (niveau 1, niveau 2, antériorité, antériorité par transcription, chiffres introuvables, corrections en entier, porte
   GC, réserves R4) ; `decisions/` (35 fichiers, décisions et propositions) ; `hypotheses-pilote-decisif-b-v1.md`, lu pour
   le contexte seulement et sans usage dans les failles.
3. **Ordre de rédaction** : la carte (close à 10:51:07 UTC) ; les failles FI-01 à FI-44 et leurs sections A à F, closes
   à 11:01:39 UTC **avant toute lecture du complément** ; lecture du complément ensuite (vérification de son empreinte à
   11:01:43 UTC) ; puis, dans les failles, les sections G (recoupements avec ses angles morts) et H (divergences),
   ajoutées à la suite sans toucher A à F ; enfin la grille.
4. **Calculs de l'auditeur** : `calculs-auditeur-v2.py`, lancé par `python3 -I` ; graines par
   `numpy.random.SeedSequence` (entropie 20261026, fixée avant toute exécution) ; illustrations analytiques et
   synthétiques (calibrage conforme à 1 %, unité du taux de faux positifs, tau de Kendall à peu de juges, interaction du
   plan 2 × 2, maximum et longueur, malédiction du gagnant, largeur d'un intervalle de rappel). Aucune donnée du
   programme ni des pilotes n'y entre.

## 2. Choix

- **Ce que veut dire « faille »** : la définition du brief (§ 2). Chaque faille est écrite au niveau de la méthode, avec
  où, mécanisme, preuve ou argument, gravité, remède, coût, expérience à préenregistrer et couverture actuelle. Aucune
  procédure ni aucun exemple qui servirait à tromper un moniteur n'est écrit ; les mécanismes sont décrits comme des
  trous de couverture.
- **Sources** : nos seuls documents. Les chiffres internes cités (premier test sur (i-a), bruit honnête du pilote,
  accord des étiqueteurs, demi-largeur d'un nul, sur-dosage de l'organisme) viennent des décisions et propositions
  fournies, jamais des dossiers de données ; aucun chiffre de la littérature n'est attribué à un papier dans les pièces
  du lot B ; les lignes de session-depot de la grille ne reprennent pas ses chiffres.
- **Statut** : toutes les failles sont des **candidates** ; la recherche d'antériorité revient à la synthèse (R8).
- **Gravité** : bloque, affaiblit, précision (définitions : failles, § 0). **Priorité** proposée : P1 à P3 (failles,
  § F.1 ; grille, § 0).
- **Grille** : colonnes d'entrée remplies (ce que dit chaque source, sans jugement), colonnes de la synthèse vides ;
  préfixes **MD-** pour le lot A (à recevoir), **SD-** pour session-depot avec ses numéros, **FI-** pour le lot B ;
  grappes de doublons probables en section 5.
- **Numérotation des calculs** : chaque bloc du script porte le numéro de la faille qu'il nourrit.

## 3. Écarts déclarés

1. **Pièces ajoutées** aux quatre demandées : les calculs de l'auditeur (script, sortie et compagnons), pour que chaque
   chiffre calculé renvoie à un chemin et à une empreinte (R6).
2. **Erratum et nouvelle version des calculs** : dans `calculs-auditeur-v1.sortie.txt`, bloc 3, la ligne « m = 4 »
   affiche « tau >= 0.667 (p = 0.0417) » : un arrondi excluait la valeur 2/3 elle-même ; 0,0417 est la probabilité de
   tau = 1 seul. La v2 calcule le tau en fractions exactes et affiche « tau >= 1.000 (p = 0.0417) » ; toutes les autres
   lignes sont identiques entre v1 et v2. La v1 reste archivée sans modification (R12) ; les pièces citent la v2 ; le
   texte de FI-35 était juste dès l'origine.
3. **Consigne du coordinateur reçue en cours de lot** (complément de session-depot) : appliquée comme demandé, après la
   clôture de mes propres failles. Vérification possible de l'absence d'ancrage : `head -c 86099 failles-internes-v1.md
   | sha256sum` redonne `38d3c8e6ba8a3dedfae91082a8bed6c37bf530e60cd12d6e74a18b4de569d931`, empreinte relevée à la clôture
   de 11:01:39 UTC, avant la lecture.
4. **Corrections avant scellement** : dans la carte, des renvois aux numéros de failles ont été alignés sur la
   numérotation définitive, une note de numérotation provisoire retirée et trois formulations précisées, avant que son
   compagnon `.sha256` existe ; dans la grille, trois renvois « voisine » ont été précisés avant scellement. Aucune pièce
   scellée n'a été réécrite.
5. **Contexte de l'instance** : le système y avait injecté le fichier de consignes du dépôt ; je ne l'ai pas ouvert, je ne
   le cite pas, et aucune affirmation des pièces n'en dépend.
6. **Pièces non fournies dont dépendent certaines lectures** : le brouillon du préenregistrement de G1 (dont G1-P5), le
   préenregistrement du papier C, les registres (application des défauts de P-009, P-010, P-011, P-015), N-020, N-027 et
   le programme fusionné v4. Les failles FI-06, FI-27, FI-28, FI-34, FI-35 et FI-38 sont à vérifier contre eux ; la
   divergence DV-3 aussi.
7. **Limite du lot** : la lecture de nos seuls documents ne faisait pas voir quatre angles morts que la littérature a
   montrés à session-depot (b1, b7, b10, seconde moitié de b6) ; ils sont en lignes dans la grille.
8. **Hygiène** : aucun `git`, aucune clé, aucun réseau, aucun sous-agent ; aucune lecture hors de
   `/var/tmp/audit-failles-controle-v1/` ; écriture seulement dans `sortie-confrontation/` ; Python avec `-I` ; heures
   lues sur `date -u` dans la commande qui les écrit ; rien d'écrasé (`set -C` à chaque création de pièce scellée).
9. **Durée** : de 10:30:22 UTC (vérification du brief) à la clôture ci-dessous, selon `date -u` ; en deçà des deux heures
   visées.

## 4. Pièces et empreintes

Vérification : `cd sortie-confrontation && sha256sum -c *.sha256`.

| pièce | rôle | sha256 |
|---|---|---|
| `carte-du-controle-v1.md` | ce que le contrôle prétend détecter, par quoi, sous quelles hypothèses ; chaque hypothèse du § 5, chaque invariant du § 9 : ce qui la ferait tomber, comment on le saurait | `ad5eaa49f740cf533539c3b296a0ff9f2c2a3268139cf6a9a1d62f79bb0e457c` |
| `failles-internes-v1.md` | 44 failles internes (FI-01 à FI-44), synthèse et décisions de Lazar (§ F) ; recoupements avec session-depot (§ G) ; divergences DV-1 à DV-8 (§ H) | `c854f23f45b7994bb514e0104b3ca828878de8badab33d61cf71b054b20203a6` |
| `grille-de-couverture-v1.md` | grille vide pour la synthèse : 3 gabarits du lot A, 26 failles et 11 angles morts de session-depot, 44 failles internes ; grappes de doublons | `1e0602083e6f54bcb0027cbeb1f55345488ad00fc7b8f8455b00fc24db575cd6` |
| `calculs-auditeur-v2.py` | calculs de l'auditeur, version citée | `dc5d1c9827b37dfdbe593808d93db7f02faa861550a5730ce6dd0924936b0c3e` |
| `calculs-auditeur-v2.sortie.txt` | sa sortie | `ee257a7aef21734812d0e2863fc75d49d57cd40419a37313a74030ec91cc6aba` |
| `calculs-auditeur-v1.py` | version archivée (erratum, écart 2) | `23bb951a8dcf9ccc500daeab20c2bb508a3007f92075f87957d4c74365ce3b14` |
| `calculs-auditeur-v1.sortie.txt` | sa sortie archivée | `a9c32505bdbf5c0d60f9a84590d9bc45e6e49c692f29efbac158dd70782b2276` |
| `LISEZMOI-confrontation-v1.md` | ce fichier ; son empreinte est dans son compagnon | — |

## 5. Pour la synthèse, en bref

- **Les trois failles internes les plus graves** : FI-06 (G1 gagnable par une différence d'information : la sonde lit
  l'indication privée, les négatifs de G1 n'ont pas le témoin apparié) ; FI-01 avec FI-02 (ce qui est mesuré, un champ
  chiffré gonflé dans un mode connu des concepteurs, n'est pas ce qui est revendiqué) ; FI-04 (le lemme garantit en
  unités de score, la sécurité se définit en dommage, et le taux de change n'est pas mesuré).
- **Bloquantes** : FI-01, 02, 03, 04, 05, 06, 15, 27, 28, 34 (au moins un volet).
- **Décisions de Lazar** : quatorze, listées en `failles-internes-v1.md`, § F.3.
- **Divergences avec session-depot** : quatre changent un classement de couverture (DV-1, DV-3, DV-4, DV-5), deux la
  portée d'un remède (DV-2, DV-6), deux sont mineures (DV-7, DV-8).

---
Horodatage : version close le 2026-10-26 à 11:09:48 UTC (heure lue sur date -u dans la commande qui écrit cette ligne).
