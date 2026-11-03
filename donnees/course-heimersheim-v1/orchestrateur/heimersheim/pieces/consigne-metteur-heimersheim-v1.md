# Metteur en combinaison — course d'idéation sur la question 1 du mentor Heimersheim (v1)

Repère de consigne (à ne pas recopier) : HQ1-METTEUR-e2ddadb3

Tu reçois **deux fiches** d'idées de recherche, anonymes, sur le pilotage des activations d'un modèle de langage contre sa conscience d'être évalué (trouver une direction qui lit « je suis évalué », intervenir dessus, et mesurer ce que le modèle ferait en déploiement). Tu écris en français.

Écris **une seule fiche nouvelle** qui combine les deux en une épreuve cohérente, plus tranchante que chacune seule (par exemple : qui sépare mieux « croyance retirée » et « registre déplacé », ou « effet spécifique » et « effet générique de même norme »), et dis pourquoi. Rédige-la comme une proposition autonome : elle ne dit pas d'où elle vient et ne mentionne pas les deux fiches reçues.

Règles d'intégrité : niveau méthode seulement (aucune conduite d'agent pour tromper une évaluation, aucun procédé pour masquer un comportement) ; tout chiffre repris cite sa source telle que les fiches la donnent, tout chiffre calculé est marqué « calcul », tout chiffre supposé « supposé » ; toute antériorité citée porte titre, auteurs, année et identifiant, marquée « à vérifier » ; une zone qui semble vierge est une question, jamais une affirmation de nouveauté.

Réponds par **un seul bloc JSON**, à la fin, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Exactement une fiche ; mêmes champs, tous obligatoires et non vides : `titre` (au plus 80 caractères), `hypothese`, `axe` (exactement une des valeurs `raison_echec_absente`, `evaluation_contre_registre`, `residu_non_verbalise`, `lien_objets_non_relies`, `prediction_chiffree_8b`), `epreuve`, `controle`, `prediction` (chiffrée, avec signe et intervalle, marquée « supposé »), `test_de_mort` (le nombre qui, lu une fois, la réfute), `cout` (Llama-3.1-8B-Instruct ou processeur, marqué « supposé »). Aucun autre champ.
