# Essai négatif du vérificateur de citations (v1)

Fichier d'épreuve : deux citations justes et sept fausses. Le programme doit compter 7 échecs et rendre le code 1.

1. Juste : `DiscoveryAgent/director_workflow.py:917` « `while query_num <= self.max_queries:` »
2. Mauvaise ligne : `DiscoveryAgent/director_workflow.py:918` « `while query_num <= self.max_queries:` »
3. Extrait altéré : `DiscoveryAgent/director_workflow.py:917` « `while query_num < self.max_queries:` »
4. Fichier absent : `DiscoveryAgent/inexistant.py:1` « `x` »
5. Lignes hors du fichier, sans extrait : `DiscoveryAgent/base_llm.py:68-70`
6. Juste : (papier p. 25 « The system is built from two nested loops. »)
7. Mauvaise page : (papier p. 26 « The system is built from two nested loops. »)
8. Plage de pages : (annexe p. 69-70 « despite a configured review interval »)
9. Bloc altéré :

Source : `DiscoveryAgent/director_workflow.py:577-578`
```text
        if self.explicit_hypothesis_step is not None:
            return False # We're not using explicit hypotheses
```
