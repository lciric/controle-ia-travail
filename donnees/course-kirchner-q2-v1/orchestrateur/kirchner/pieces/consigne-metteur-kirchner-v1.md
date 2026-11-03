# Metteur en combinaison — course d'idéation sur la question 2 du mentor Kirchner (v1)

Repère de consigne (à ne pas recopier) : KQ2-METTEUR-c16e2030

Tu reçois **deux fiches** d'idées de recherche, anonymes, sur un problème d'alignement sous-estimé qui touche les chercheurs d'alignement automatiques (classement, moniteur de triche du même modèle, banc tenu à l'écart, Petri, harnais ouvert). Tu écris en français.

Écris **une seule fiche nouvelle** qui combine les deux en une première expérience cohérente, plus tranchante que chacune seule (par exemple : qui mesure mieux le rappel d'un moniteur sur des tricheries plantées, ou qui dit mieux si un gain sur un banc transfère hors banc), et dis pourquoi. Rédige-la comme une proposition autonome : elle ne dit pas d'où elle vient et ne mentionne pas les deux fiches reçues.

Règles d'intégrité : niveau méthode seulement (aucune conduite d'agent pour tromper un moniteur ou une évaluation, aucun procédé pour masquer un comportement ; les tricheries plantées se décrivent par leur classe et leur rôle de mesure, jamais par un mode d'emploi) ; aucun identifiant inventé ; tout chiffre repris cite sa source telle que les fiches la donnent, tout chiffre calculé est marqué « calcul », tout chiffre supposé « supposé » ; une zone qui semble vierge est une question, jamais une affirmation de nouveauté.

Réponds par **un seul bloc JSON**, à la fin, de la forme :

```json
{"fiches": [
  {"titre": "…", "probleme": "…", "sous_estime": "…", "hypothese": "…", "axe": "…", "premiere_experience": "…", "changer_d_avis": "…", "test_de_mort": "…", "cout": "…"}
]}
```

Exactement une fiche ; mêmes champs, tous obligatoires et non vides : `titre` (au plus 80 caractères), `probleme`, `sous_estime`, `hypothese`, `axe` (exactement une des valeurs `probleme_peu_couvert`, `rappel_apres_selection`, `transfert_hors_banc`, `lien_non_fait`), `premiere_experience`, `changer_d_avis` (chiffré, avec signe et seuil), `test_de_mort` (le nombre qui, lu une fois, la réfute), `cout` (marqué « supposé »). Aucun autre champ.
