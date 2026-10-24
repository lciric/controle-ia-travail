# Banque de tâches réelles — pièces brutes (v1)

Rien ici n'est encore une banque scellée : ce sont les pièces brutes, versionnées avec leur empreinte, avant la
partition train / test de développement / test final que le préenregistrement v2 fixera (graine `SeedSequence`,
R9) et scellera avant tout amorçage (R1).

## `traces-sabotage-lot1-logiciel-v1.json` — famille `controle-delegation`

- Décision de Lazar du 24 octobre (16:40, « Tâches réelles de la confrontation : (a) … go ») et P-026 (a) : traces
  honnêtes et sabotées **écrites par Claude** (sous-agent neuf, consigne : scénario d'agent délégué en logiciel ;
  20 paires partageant le même scénario ; sabotage porté par une action formulée comme une optimisation ordinaire ;
  un « faux ami » justifié dans chaque trace honnête ; aucun des mots « sabotage », « honnête », « caché »,
  « dissimuler », « tricher » dans les traces).
- 40 objets : `id` (`L1-NN-H` / `L1-NN-S`), `paire`, `scenario`, `trace` (12 à 35 événements `t=NN outil=… -> résultat`
  ou `t=NN message=…`), `verite` (`honnete` / `sabotage`), `type_sabotage` (alerte-coupee 3, test-affaibli 3,
  moniteur-retire 3, repli-silencieux 3, journal-tronque 3, verification-sautee 3, autre 2 ; `None` pour les
  honnêtes), `notes_auteur` (jamais montré à un organisme).
- Empreinte SHA-256 : `6e56e3455b5db498e7664de83688544017adbc49832d42d9b127b6560ee7ad07` (compagnon `.sha256`).
- Domaines : intégration continue, déploiements, pipelines de données, maintenance de dépôts et de flotte,
  migrations, scripts d'exploitation. Hôtes et noms fictifs ; aucune clé, aucune adresse réelle.
- Réserve : écrites par un modèle de la famille Anthropic ; une lignée de cette famille peut en reconnaître le
  style. Le lot 2 (recherche) et le sous-ensemble public « eval-awareness » (autre source) équilibrent la banque ;
  le préenregistrement v2 traite cette dépendance (stratification par source, score rapporté par source).

## À venir

- `traces-sabotage-lot2-recherche-v1.json` (sous-agent en cours).
- `eval-awareness-sous-ensemble-v1.json` : extrait par Lazar du jeu public du papier « Large Language Models Often
  Know When They Are Being Evaluated » (arXiv 2505.23836 ; licence CC BY-NC-SA 4.0 ; contenu GAIA exclu), par le
  script `livrables/eval-awareness-sous-ensemble-v1.zip` ; empreinte à consigner à la réception.
