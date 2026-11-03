# Metteur en combinaison — course d'idéation sur la question 1 de la mentore Ibrahim (v1)

Repère de consigne (à ne pas recopier) : IQ1-METTEUR-f06a7843

Tu reçois **deux fiches** d'idées de recherche, anonymes : deux premières expériences candidates sur la tenue d'une persona installée par entraînement de caractère après un apprentissage par renforcement, et sur la sycophancie. Tu écris en français.

Écris **une seule fiche nouvelle** qui combine les deux en une première expérience cohérente, plus tranchante que chacune seule, et dis pourquoi. Rédige-la comme une proposition autonome : elle ne dit pas d'où elle vient et ne mentionne pas les deux fiches reçues.

Règles d'intégrité : niveau méthode seulement (aucune conduite d'agent pour tromper une évaluation, aucun procédé pour masquer un comportement) ; aucun identifiant inventé ; tout chiffre repris cite sa source telle que les fiches la donnent, tout chiffre calculé est marqué « calcul », tout chiffre supposé « supposé » ; une zone qui semble vierge est une question, jamais une affirmation de nouveauté.

Réponds par **un seul bloc JSON**, à la fin, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Exactement une fiche ; mêmes champs, tous obligatoires et non vides : `titre` (au plus 80 caractères), `hypothese`, `axe` (exactement une des valeurs `tenue_de_la_persona`, `sycophancie_apres_rl`, `mesure_et_juge`, `resultat_trompeur`), `epreuve`, `controle` (ce qui rendrait le résultat trompeur, et le contrôle qui le détecte), `prediction` (chiffrée, avec signe et intervalle, marquée « supposé »), `test_de_mort`, `cout` (marqué « supposé »). Aucun autre champ.
