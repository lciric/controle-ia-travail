# Course d'idéation de l'organisme — devis v7 nonies (v44 ; voie (β) lançable : plafond propre à la passe 2 ; ligne de commande exacte)

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` **09:32 UTC**. **Remplace le devis v7 octies** (`43fc1d2a…`,
gardé, R12) ; le reste des v2 à v7 octies vaut. Code : **v44** (412 essais ; LISEZMOI `69d15838…`, EMPREINTES `68126ef3…`, lot
`livrables/lot-ideation-tournoi-v44-v1.zip` `846eae86…` ; relecture CL11 chez session-depot avant tout lancement). Répond à CL10 (`e8736904…`).

1. **Plafonds (ligne de Lazar, R-419, R-429 ; enveloppe 60 USD, R-724 de `main`)** : Claude **40** ; Argon **12,8** = contrôle de la course
   **3,1** + passe 1 **2,5** + **passe 2 3,1** (option neuve `--budget-passe-2-externe-usd`, CL43-01) + juge 3,5 + contrôle du bras 0,2 = **12,4**,
   marge 0,4 ; **total 52,8**. Pire cas au plafond (rejoué) : Claude 40,00, Argon 12,4, total 52,4, classement à trois juges ; fiches réelles
   d'Argon (≈ 4 500 caractères) : Argon 7,96, total ≈ 48.
2. **Ligne de commande (v44)** — relais : `python3 -I -B pole/relais_reel.py --plafond-usd 40 --reserve-par-appel 4 --port 8787 …` ;
   course : `python3 -I -B demonstrations/ideation_v1.py SORTIE --moteur claude-sdk --confirmer-moteur-reel --url-relais http://127.0.0.1:8787
   --liste-blanche LISTE.json --question Q.md --piece … --materiau … --seconde-passe --attestation-materiau ATT.json --temoins TEMOINS.json
   [--piece-juge …] --proposeur-externe argon=gemini-argon --juge-externe argon=gemini-argon --commande-externe "…" [--variable-transmise …]
   --horodatage "…" --taille-max-pieces 750000 --budget-controle-externe-usd 3.1 --budget-passe-2-externe-usd 3.1 --budget-externe-usd 12.8
   --prix-entree-usd-par-million-jetons 8.3 --taille-max-consigne-externe 1490000` ; bras : `… SORTIE --bras-rapporte-differe
   --attestation-lecture-humaine ATTEST.json --juge-externe argon=gemini-argon --commande-externe "…" --prix-entree-usd-par-million-jetons 8.3
   --budget-externe-usd 12.8` (**garde du bras par défaut, 1 166 746 : ne pas donner `-bras 1686000`**, CL43-04). Identifiant de modèle
   `gemini-argon` à confirmer contre la commande réelle. **Les fichiers d'entrée ne changent pas de forme ; une seule option nouvelle.**
3. **Gardes par passe (CL43-02)** : chaque passe d'Argon est gardée avant envoi contre son propre plafond moins une provision de sortie
   (nombre de fiches × taille provisionnée × rapport 5 au prix donné) ; taille provisionnée **8 000 caractères par fiche** (passe 1 ; passe 2 :
   le plus grand de 8 000 et de la plus grande fiche admise d'Argon en passe 1) ; la garde donnée ne désarme pas cette garde. Mesuré à 8,3 :
   contrôle 1 457 167 caractères (3,02 ≤ 3,1) ; passe 1 752 440 (2,23 avec provision ≤ 2,5, garde 884 819) ; passe 2 gardée à 1 173 975 ;
   juge au maximum 2 131 096 (> 1 166 746 : refusé sans dépense, classement sans bras — les 52 fiches réelles feront bien moins).
   **Réserve dite** : la passe 1 ne peut pas être gardée contre la taille de ses propres fiches (elles n'existent pas encore) ; sous (β) elle
   tient tant qu'Argon rend des fiches de moins de ≈ 11 300 caractères en moyenne ; au-delà elle dépasse son plafond — **à vérifier avant le
   GO : la commande réelle d'Argon s'arrête-t-elle d'elle-même à son plafond ?** (session-depot). Rejeu D-β à fiches de 9 066 : passe 2
   **refusée avant envoi** (Argon 5,33, pas 8,5) ; à fiches maximales : passe 1 partie et refusée pour dépassement (Argon 8,23).
4. **Reprise des contrôles (CL43-03, CL40-01 (c))** : un contrôle Claude n'est repris que si la dépense lue au relais n'a pas baissé depuis
   la tentative ; relais relancé → contrôles Claude rejoués. **Effet aux réglages du devis** : relais à 40 = total Claude 40 → une relance
   après contrôles Claude payés oblige à relancer le relais, donc à rejouer 0,4 → somme 40,4 > 40 : **relance refusée sans dépense**.
   Nœud (dépense) pour Lazar : (a) total Claude 40,4 (+ 0,4) pour permettre une relance ; (b) laisser ainsi (toute relance après contrôles
   payés = son mot). Recommandation (a), confiance 0,6, défaut 48 h : (a) — dans l'enveloppe de 60.
5. **Relance bornée** par les sommes **et** par `MAX_TENTATIVES_BRAS` = 3 (CL43-05, dit vrai) ; seuil de taille 1 493 975 (CL43-08) ; clé de
   reprise avec l'empreinte de la consigne (X01, essai).
6. **Mesures de convergence** (Lazar, R-448) : au manifeste de fin seulement, par proposeur et par fiche (distances passe 1 → passe 2,
   nouveauté des sources, pièces citées ; pages lues à null) ; jamais aux juges ni au classement.
7. **Restes** : CL43-06 (la commande réelle d'Argon ne doit nommer aucun fichier qui change entre tentatives), X15/X16/X30/X34 (essais),
   tour (c), `garde_outils`, moisson : après la course. Ordre : `sha256sum -c EMPREINTES-…-v44.txt`, `--mesurer-consignes` avec les vrais
   fichiers, contrôle d'acceptation des trois espèces (corpus, R-439), CL11, lancement sous GO-14 (52,8 ; enveloppe 60).
