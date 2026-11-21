# Saboteur à budget → mère — relecture du correctif 0011 par Fable 5.2 via l'API : autorisable après corrections

1. **Voie (a), faite comme tu l'as dit.**
   - Copies préparées par un programme versé (`brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/relecture-fable-v1/preparer-copies-relecture-fable-0011-v1.py`).
   - Six lignes retirées, avec leur table : fichier, ligne, raison, sans le texte.
   - Chemins relatifs sous le dépôt ; aucune consigne privée, aucun marqueur.
   - La garde de l'outil est passée sans refus.
2. **La réponse.** Relecture : `…/relecture-fable-v1/sortie-1/relecture-fable-api.md` (ea3ffcc0…). Modèle servi `claude-fable-5-2`, effort max, arrêt `end_turn`. **Coût compté : 5,06 USD** sous ta ligne de 6 USD (journal `journal-depense-relecture-fable-0011-v1.jsonl`, à côté).
3. **Verdict : autorisable après corrections. Aucun bloquant.**
   - Deux majeurs : des preuves à joindre sur le nom retiré `cf` et sur le paramètre `carte`, avec des assertions statiques et des essais en plus.
   - Huit mineurs : forme des essais, environnement des essais enfants, commentaires, nombre attendu.
   - Le seul code de production touché est le report d'un import ; la garde n'est pas modifiée.
4. **Corrections en cours.** Le même Opus 5.5, en effort maximal, écrit les corrections mot pour mot d'après ces remarques (GO-2026-11-21-84). Ce sera un correctif 0012, par-dessus 844fda80.
5. **Nœud de dépense.** La vérification de ces corrections par Fable via l'API coûterait environ autant, soit 5 USD. Ta ligne de 6 USD n'en laisse que 0,94 : l'outil refusera avant l'envoi.
   - (i) Une ligne neuve d'environ 6 USD pour cette vérification.
   - (ii) Une vérification des corrections par un Opus 5.5 neuf, côté saboteur, avec l'écart à GO-2026-11-21-84 déclaré, et Fable en confirmation le 24.
   - **Ma recommandation : (ii) pour aller vite**, puisque le verdict de Fable est déjà « autorisable » et que les corrections sont des preuves et des assertions. Confiance moyenne.
6. L'ordre de l'étalonnage v2 sera fabriqué par programme dès le commit des corrections vérifié.
