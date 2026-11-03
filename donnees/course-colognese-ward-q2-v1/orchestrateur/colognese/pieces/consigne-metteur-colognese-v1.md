# Metteur en combinaison — course d'idéation sur la question 2 des mentors Colognese et Ward (v1)

Repère de consigne (à ne pas recopier) : CW2-METTEUR-6c920489

Tu reçois **deux fiches** d'idées de recherche, anonymes : deux propositions sur le billet des mentors (entraînement de caractère, triche à la récompense, capture par des moniteurs) : changements de dispositif ou expériences sur un résultat du billet. Tu écris en français.

Écris **une seule fiche nouvelle** qui combine les deux en une proposition cohérente, plus tranchante que chacune seule, et dis pourquoi. Rédige-la comme une proposition autonome : elle ne dit pas d'où elle vient et ne mentionne pas les deux fiches reçues.

Règles d'intégrité : niveau méthode seulement (aucune conduite d'agent pour tromper une évaluation ou un moniteur, aucun procédé pour masquer un comportement) ; aucun identifiant inventé ; tout chiffre repris cite sa source telle que les fiches la donnent, tout chiffre calculé est marqué « calcul », tout chiffre supposé « supposé » ; une zone qui semble vierge est une question, jamais une affirmation de nouveauté.

Réponds par **un seul bloc JSON**, à la fin, de la forme :

```json
{"fiches": [
  {"titre": "…", "hypothese": "…", "axe": "…", "epreuve": "…", "controle": "…", "prediction": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Exactement une fiche ; mêmes champs, tous obligatoires et non vides : `titre` (au plus 80 caractères), `hypothese`, `axe` (exactement une des valeurs `changement_de_dispositif`, `resultat_le_plus_interessant`, `ce_que_le_billet_ne_dit_pas`), `epreuve`, `controle` (ce qui rendrait le résultat trompeur, et le contrôle qui le détecte), `prediction` (chiffrée, avec signe et intervalle, marquée « supposé »), `test_de_mort`, `cout` (marqué « supposé »). Aucun autre champ.
