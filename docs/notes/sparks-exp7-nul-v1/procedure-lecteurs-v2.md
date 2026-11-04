# SPARKS-EXP7-NUL — procédure de lancement des lecteurs — v2 (addendum n° 1)

Écrite par le rédacteur-développeur neuf du brouillon 2 de l'addendum, le 4 novembre 2026 (`date -u`), **sans lancer
aucun lecteur**. Remplace la v1 (`procedure-lecteurs-v1.md`, gardée, R12) pour les seuls points ci-dessous ; tout le
reste de la v1 (transport A recommandé, transport B, pilotes, quota, ordre des cas, hors de portée des lecteurs) vaut
tel quel. Textes qui font foi : `prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md` (`4bacf20d…`) et l'addendum n° 1
scellé (`prereg/SPARKS-EXP7-NUL-addendum-1.md`, brouillon 2 : `prereg/SPARKS-EXP7-NUL-addendum-1-brouillon2.md`).

## Ce qui change

1. **Modules** : `controle_ia.sparks_exp7_nul_v2` (harnais, mise à disposition, bac, outil, analyse) au lieu de la v1.
2. **Consigne principale v2** : `consigne-lecteur-principal-v2.txt`, sha256
   `c74c13276776b88610b6744232971d87eeefaf685e109e516a09fd5cafedfe48` (écart E-2 : tâche (2) et phrase de la réponse
   finale ne présupposent plus une différence ; aucun autre mot ne change, essai ligne à ligne). Ancre : v1, inchangée.
   Au secours seulement : `principal-secours` et `ancre-secours`, écrites au portage par
   `consignes.deriver_secours` (quatre substitutions fermées), prélude porté éprouvé par `consignes.eprouver_prelude`
   avant tout service ; leurs chemins et empreintes, et ceux du prélude, dans le manifeste du portage passé au
   harnais (`--secours`). Jamais écrites si le secours ne sert pas.

   ```
   PYTHONPATH=src python -I -B -m controle_ia.sparks_exp7_nul_v2.harnais ouvrir \
       --sessions SESSIONS --lecteur opus --cas cas_<hex> --servi SERVI --variante principal
   PYTHONPATH=src python -I -B -m controle_ia.sparks_exp7_nul_v2.harnais tour --session SESSIONS/opus/cas_<hex> --reponse R.md
   ```
3. **Réponse finale en deux temps** (E-3) : un rappel de forme pour toute faute ; ensuite « invalide » (probabilités
   ou bloc) = échec, compté avec les infractions dans la ligne des 10 % ; « composants_invalides » = probabilités
   comptées, composants vides, hors de la ligne des 10 %, rapporté à part. Réponse scellée : `reponse-v2.json`.
4. **Copies par lots** (E-4) : la session reçoit les copies par lots de 4 cas (3 si moins de 10 Go sont libres :
   `mise_a_disposition lots --libres OCTETS --noms …`), chaque lot par un redémarrage court de l'instance arrêtée ;
   **avant chaque redémarrage**, garde de dépense (`depense projeter ETAT.json`, refus au-delà de 40 USD projetés) et
   commande littérale imprimée par `scripts/lancer_sparks_exp7_nul_v2.sh`.
5. **Couches du départ** : apportées avec le premier lot (`couches-depart-v1.safetensors`), empreinte contrôlée contre
   le manifeste (`fabrication-complement-v2.json`), rangées **hors** du dossier servi, des sessions et du dépôt (jamais
   montées dans le bac).
6. **B3 et B4 au service, avant tout lecteur du cas** : `mise_a_disposition servir …` (v2) sert le cas, passe le
   contrôle de fuite, puis calcule B3 et B4 sur les deux copies servies sans lire la clé, au coffre seul
   (`bases-poids-principal-v1.json`) ; rien n'est imprimé. Après le dernier cas : `aveugle.engager_bases` (empreinte au
   manifeste).
7. **Ouverture unique** : `aveugle.ouvrir_coffre` (v2) exige en plus l'empreinte engagée des bases et en écrit la copie
   scellée ; l'analyse (`analyse.analyser`, v2) lit cette copie, le rapport de fabrication (B3 et B4 de l'étalonnage),
   les 102 réponses scellées, les six générateurs neufs (`plan.generateurs_neufs()`) et `bootstrap`.
8. **Contrôle causal** : seconde session de carte (`PHASE=causal`), par lots si l'essai d'égalité passe sur
   l'instance, sinon sans lots, déclaré, seulement si la garde de dépense le permet.
9. **Fin** : contrôle causal fini → sorties scellées copiées, puis **destruction** de l'instance par son identifiant
   (`depense instance ETAT.json` dit « copier », puis « detruire » et imprime `vastai destroy instance <id> -y` : sans
   `-y`, vastai 1.8.3 demande confirmation et ne détruit rien, R-1482 ; la sortie brute de `vastai` n'est ni affichée
   ni journalisée, R-1480, seuls le code de retour et l'identifiant sont consignés) ; à partir du 16 novembre sans fin en vue : nœud de
   Lazar ; à l'échéance (fin du 18) sans réponse : destruction. Entre deux redémarrages, l'instance arrêtée est « en
   tâche » pour la routine de reprise.

## État de dépense (écrit par la session, lu par la garde)

```json
{"prix_heure_carte": 0.62, "prix_heure_stockage": 0.03, "cree_le": "2026-11-0XT..Z", "heures_demarrees": 3.4,
 "facture_usd": null, "phases_faites": ["fabrication", "etape0"], "redemarrages_restants": 12, "egalite_lots": true,
 "sorties_copiees": false, "instance": "12345678"}
```
