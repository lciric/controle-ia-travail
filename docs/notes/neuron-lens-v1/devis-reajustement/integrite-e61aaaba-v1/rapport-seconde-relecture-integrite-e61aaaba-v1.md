# Seconde relecture d'intégrité du rangement des lentilles réajustées, révision e61aaaba — rapport v1

Session fille (Opus 5.5, effort moyen), 2026-11-24 vers 10:34Z, sur le mot de Lazar du 24 novembre vers 10:31Z (« go »). Commande
v11 du réajustement des lentilles, § 3, étape 16 (`docs/notes/neuron-lens-v1/commande-b-beta-v11.md`). Aucune dépense, aucune machine.
Aucun contenu ouvert : ni poids, ni lecture, ni score ; seules les empreintes calculées en flux (octets passés au calcul d'empreinte,
rien écrit sur le disque) et les métadonnées de la plateforme (noms, tailles).

## Verdict
- **Les 172 fichiers copiés au rangement sont présents et égaux en taille et en empreinte** à celles de l'inventaire clos, à la révision
  `e61aaabac7abd50cf68e5b608af2704f7faaa1e6`. Code 0 du programme de relecture, comme à la première relecture (étape 14 bis).
- **Manquent les 34 pièces d'export de moitié non copiées** (moitié paire : 9 sur 68 ; moitié impaire : 25 sur 68), comme annoncé ;
  aucune n'est au dépôt. Rien d'autre ne manque.
- **La clé restreinte de rangement peut être révoquée : oui.** La seconde relecture a été faite avec la clé gardée de la session
  (variable `HF_TOKEN`, lecture seule), sans la clé restreinte.

## Ce qui a été fait
1. Clé de la plateforme de modèles employée par son nom (`HF_TOKEN`), en lecture ; accès accordé.
2. Liste des métadonnées du dépôt de rangement à la révision épinglée (noms, tailles, empreinte déclarée par la plateforme pour les
   fichiers volumineux) : 173 fichiers, soit les 172 copies prévues et `.gitattributes` (fichier de la plateforme). Les 172 tailles et
   les 162 empreintes déclarées sont égales à l'inventaire ; 10 petits fichiers n'ont pas d'empreinte déclarée (couverts par l'étape 3).
   Programme : `lister_distant_v1.py` ; sortie : `liste-distante-noms-tailles-20261124-v1.json` (ce dossier).
3. Relecture de l'étape 16, en flux :
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.rangement_lentilles_v2 relire --inventaire diag/20261122-073402-neuron-lens-b-beta/inventaire/inventaire-029.json --cle-nom HF_TOKEN --revision e61aaabac7abd50cf68e5b608af2704f7faaa1e6 --sortie docs/notes/neuron-lens-v1/devis-reajustement/relecture-rangement-2-20261124T103430Z-v1.json`
   → `{"toutes_egales": true, "n": 172}`, code 0, aucune erreur.

## Décompte par pièce (inventaire clos 029)
| Pièce | Copiées et égales | Prévues |
|---|---|---|
| Fichier d'ajustement principal de R | 1 | 1 |
| Fichier d'ajustement de S | 1 | 1 |
| Export entier de R | 68 | 68 |
| Export de la moitié paire de R | 59 | 68 |
| Export de la moitié impaire de R | 43 | 68 |
| **Total** | **172** | **206** |

Liste nominative des 34 manquants : `docs/notes/neuron-lens-v1/devis-reajustement/non-copies-inventaire-clos-029-v1.txt`.

## Les 34 exports de moitié sont-ils à refaire ?
**Pas maintenant, et pas pour révoquer la clé.** Ils ne sont nécessaires ni à la comparaison d'identité (le programme de comparaison v4
ne lit que des pièces JSON, déjà versées : R-5044, motif b) ni à la révocation. Ils sont à refaire **seulement si** une lecture ou un
emploi ultérieur exige les poids des deux moitiés : dérivables du fichier d'ajustement principal copié et relu égal ici (critère
d'identité v8, § 1), avec la réserve déjà inscrite que cette dérivation n'a jamais été essayée sur une autre machine. Refaire demanderait
une machine à carte graphique, donc un devis et un GO.

## Réserves
- L'étape 16 prévoyait cette relecture **après** la révocation ; elle est faite avant, sur le mot de Lazar, puisqu'elle en conditionne
  la révocation. Elle emploie déjà la clé gardée et non la clé restreinte : la révocation ne change rien à son résultat.
- Les empreintes de l'inventaire clos sont celles calculées sur la machine ; leur sceau est vérifié (`inventaire-029.json`,
  `8e1f87bf…`, égal à son compagnon).

## Empreintes
- `relecture-rangement-2-20261124T103430Z-v1.json` : `0c8591690426ab108110f2aad09397868ddaf2a224bf67ebbae50913c509e89d`
- `integrite-e61aaaba-v1/liste-distante-noms-tailles-20261124-v1.json` : `4cfc814324d0b816d2c886fca03d448236d8b51ab312447b41fcab82b43d9e63`
- `integrite-e61aaaba-v1/lister_distant_v1.py` : `5d6a7dca1ced2f32acf827bd75feadbf94f71460398cdb6b234f7b9d0a0409ec`
