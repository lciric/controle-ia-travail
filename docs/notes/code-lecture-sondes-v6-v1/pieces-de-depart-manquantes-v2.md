# Pièces de départ qui manquent encore pour lancer la lecture des sondes du barreau 8 (code de la lecture v6) — v2

Remplace la v1 (`pieces-de-depart-manquantes-v1.md`, `4b7198e7…`, scellée à côté) : l'identifiant de l'accord de lecture est réservé, le bordereau du code est écrit, et trois remarques de la contre-lecture de conformité s'ajoutent. Écrite le 2026-11-24 par le développeur du côté des moniteurs. Pièce de travail (classe C). Constats faits **par les noms et l'existence des fichiers seulement** : aucune pièce de la course n'a été ouverte.

## Déjà en place (constaté)

- Lignes `SCELLEMENT-SONDES-IIB`, `SCELLEMENT-ADDITIF-1-SONDES-IIB` (2026-11-24T04:21:08Z), `SCELLEMENT-ADDITIF-2-SONDES-IIB` (10:34:26Z), `CODE-PASSE-IIB` (11:31:45Z) et `LIVRAISON-PASSE-IIB` (13:08:00Z) au registre propre ; les deux dernières sont postérieures à la ligne de l'additif 2.
- **Bordereau du code de la lecture** (neuf clés) : `docs/notes/code-lecture-sondes-v6-v1/bordereau-code-lecture-sondes-barreau8-v6.json`, `dd816daf…2d4e`, avec l'accord `GO-2026-11-24-28` ; relu sur le dépôt réel par la fonction de la lecture (modules, textes, table neuve, pièces D-14 : tenus).
- Table neuve des constantes et pièces de la condition D-14 : présentes, à leurs empreintes, « report ».
- Pièce d'attestation de l'ordre (D-6 lue avec M-3), `8f6b5025…e76a` : acceptée par le code.
- Verdict du témoin positif planté et sa pièce d'issue (D-9) : présents par leur nom ; empreintes contrôlées au lancement.

## Ce qui manque, et qui le produit

| # | pièce ou ligne | condition | qui la produit | quand |
|---|---|---|---|---|
| 1 | **Ligne `GO-2026-11-24-28` au registre des accords**, première cellule = l'identifiant seul, une seule ligne ainsi | D-4 | mot de Lazar ; la session mère l'inscrit | avant la lecture (sans elle, refus `[D-4]`) |
| 2 | **Ligne `CODE-LECTURE-SONDES-IIB`** (proposée dans `registres/lignes-a-verser/code-lecture-sondes-v6-v1.md`), strictement après la ligne de l'additif 2 | M-5 ; lignes 5, 23, 30 | session mère | dès maintenant |
| 3 | **Mandats scellés du lecteur et du juge** : chacun cite l'empreinte de la liste des exclus et celle du registre « qui a lu quoi » ; celui du lecteur cite en plus l'attestation de l'ordre (`8f6b5025…`), l'attestation de la course et de l'oracle (pièce 6), la référence boîte noire si elle existe. **Remarque de la contre-lecture** : les mandats doivent aussi citer la liste des exclus à sa section (`1:8`, champ `exclus.section` de l'attestation de l'ordre) ; le code ne le contrôle pas (lettre du texte scellé), la session mère le tient. Les projets de mandats existants (brouillon 2) précèdent les additifs | D-5 ; D-6 ; D-15 | session mère | après la pièce 6 |
| 4 | **Aires minimales détectables** : commande `puissance`, sortie scellée et committée | D-10 | côté moniteurs, sur processeur ; 1,6 à 4,8 heures estimées, budget 12 heures ; exige la ligne de la pièce 2 | après la pièce 2 |
| 5 | **Extrait des seuls états** `docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json` et son compagnon (13 états), et **ligne `ETATS-COURSE-IIB`** | D-12 ; RP-10 ; ligne 3 | extrait : programme du côté exposé ; ligne : session mère | ordre (v) de l'additif 2 |
| 6 | **Attestation de la course et de l'oracle** `docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json`, scellée, « conforme » | D-15 ; ligne 22 | un agent du côté exposé | après les lectures du dommage et de la diffusion, avant la lecture des sondes |
| 7 | **Heure de remise de la note d'interface version 7**, passée par `--remise-note-v7`. **Remarque de la contre-lecture** : aucune pièce scellée ne porte cette heure ; la session mère l'atteste avec sa source, de préférence dans le mandat du lecteur ou une pièce scellée citée par lui | RP-14, ligne (vi) | session mère | avant la lecture |
| 8 | Référence boîte noire (**facultative** ; absente, LD-4 « non jouée ») | LD-4 | côté exposé | avant la lecture, si elle est faite |

## Risques et remarques à porter à la session mère

- **Dossier de la livraison.** La garde r2 exige que le dossier du bordereau de livraison ne contienne que les fichiers de la livraison et leurs compagnons. La ligne `LIVRAISON-PASSE-IIB` cite un chemin sous `versement/` : un inventaire, un journal ou un autre fichier dans ce dossier ferait refuser la réception (`[r2]`). Je n'ai rien ouvert sous `versement/`.
- **Arbre de travail propre** pour `puissance` et `lecture` (manifeste) : livraison, extrait, registre, bordereaux, sortie de la recette committés ou ignorés par git.
- **Ligne (xi) des lignes de tête** : écrite à la lettre de l'additif 1 ; l'écart déclaré par l'additif 2 pour sa propre chaîne (comptes de la note version 7) n'est pas recopié par le code (RP-14 ne le demande pas) ; au juge de l'écrire en tête du verdict si la session mère le veut.
- **Essai de la suite du dépôt** : un essai de la lecture v5 (`test_refus_de_tourner[registre des accords absent]`) a échoué une fois, sous charge, pendant que d'autres calculs tournaient, puis a passé seul (34 sur 34) ; code v5 non touché par ce travail.
