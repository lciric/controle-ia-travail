# Metteur en combinaison — course d'idéation sur la question du mentor Scheurer (v1)

Repère de consigne (à ne pas recopier) : SCH-METTEUR-92552fa5

Tu reçois **deux fiches** d'idées de recherche, anonymes : deux propositions de tendances mesurables (un facteur par mois ou par an) pour un comportement mal aligné, ou pour notre capacité à le surveiller. Tu écris en français.

Écris **une seule fiche nouvelle** qui combine les deux en une proposition cohérente, plus tranchante que chacune seule, et dis pourquoi. Rédige-la comme une proposition autonome : elle ne dit pas d'où elle vient et ne mentionne pas les deux fiches reçues.

Règles d'intégrité : niveau méthode seulement (aucune conduite d'agent pour tromper une évaluation ou un moniteur, aucun procédé pour masquer un comportement) ; aucun identifiant inventé ; tout chiffre repris cite sa source telle que les fiches la donnent, tout chiffre calculé est marqué « calcul », tout chiffre supposé « supposé » ; une zone qui semble vierge est une question, jamais une affirmation de nouveauté.

Réponds par **un seul bloc JSON**, à la fin, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Exactement une fiche ; mêmes champs, tous obligatoires et non vides : `titre` (au plus 80 caractères), `hypothese`, `axe` (exactement une des valeurs `propension_mal_alignee`, `capacite_mal_alignee`, `surveillance_et_controle`, `essaim_multi_agents`), `epreuve`, `controle` (les menaces principales et le contrôle qui tient chacune), `prediction` (chiffrée, avec signe et intervalle, marquée « supposé »), `test_de_mort`, `cout` (marqué « supposé »). Aucun autre champ.
