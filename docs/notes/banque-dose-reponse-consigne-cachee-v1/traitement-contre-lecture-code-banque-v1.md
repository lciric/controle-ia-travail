# Traitement de la contre-lecture du code de la banque de 64 tâches neuves — v1

Pièce de classe B (instrument). Rapport : `rapport-contre-lecture-code-banque-v1.md` (même dossier ; contre-lecteur d'un autre modèle que l'auteur ; verdict « utilisable après corrections », 0 bloquante, 3 majeures, 8 mineures, 2 suggestions). Toutes les remarques sont traitées dans le code et les essais (`tests/test_banque_dose_reponse_v1.py`, 32 essais).

| remarque | traitement |
|---|---|
| CL-1 (majeure) module de sélection non épinglé | ajouté à `Chemins.modules` ; essai : sa modification après la tentative 1 arrête l'étape suivante |
| CL-2 (majeure) aucun contrôle final de la banque rendue | `ecarts_de_la_banque` (pure) et `controler_banque` + sous-commande `controler-banque`, sans écriture : 64 distinctes, aucune des 96 (sans version), rang relu dans le tirage scellé = rang du manifeste, au moins 125, version des pages du 6 octobre, rangs strictement croissants, aucun hors-banque ni papier non exclu de rang inférieur au 64e retenu ; essai sain (déroulé) et un artefact par condition |
| CL-3 (majeure) 403 compté comme exclusion | trois « source indisponible » d'affilée arrêtent (panne d'accès présumée) ; une exclusion isolée reste une exclusion de la règle, inchangée ; essais |
| CL-4 besoin non lié | `--besoin` doit valoir 80 (64 + marge 16) ; essais 63 et 100 |
| CL-5 constantes | une seule source (`corpus_arxiv_banque_dose_reponse_v1` : 125, 64, 16, 80), importée par l'extraction ; essai qui les fige |
| CL-6 arrêt non consigné, ordre hérité | garde dans le `try` qui écrit `arret-assemblage` ; ordre vérifié strictement croissant en rang de tirage, banque triée par rang ; essai |
| CL-7 bilan trompeur | `entrainement_insuffisant` à `null` (sans objet) ; clé `noms_des_listes` qui dit ce que sont « evaluation » (la banque) et « entrainement » (hors banque) |
| CL-8 corpus non confronté | chaque fiche, exclus compris, porte l'identifiant de `tirage.json` à son rang ; rangs consécutifs depuis 125 ; manifeste de la sélection : rang de départ 125 et besoin 80 ; empreinte du corpus et chemins relus du manifeste à chaque étape ; essais |
| CL-9 parité et version | constantes de la chaîne comparées à celles du manifeste du 6 octobre ; fiche = identifiant et version de l'entrée des pages ; essais |
| CL-10 modèle des sous-agents | `modele_sous_agents` au manifeste de l'extraction (non nommé par le manifeste des 96 ; écart déclaré à la ligne de registre) |
| CL-11 réserve épuisée | `arret-assemblage` porte sa suite : nœud de Lazar ; suite du tirage existant, jamais un tirage nouveau ; essai |
| CL-12 essais manquants | ajoutés (voir ci-dessus) ; le déroulé contient une exclusion de la sélection |
| CL-13 finitions | entropie sans effet commentée ; fiches écrites au fil de l'eau (`fiches-au-fil.jsonl`, hors du dépôt) ; non-atomicité de `ecrire_resultat` : code scellé, résidu connu, inchangé |
