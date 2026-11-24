# Fiche pour Lazar — nœud : troisième condition de séparation du versant honnête — v1

2026-11-24, 11:10Z environ (`date -u` relevé à 11:07Z). Session « dossier de l'entretien », reprise (Opus 5.5). Pièce de travail. **Nœud : pas de défaut** (il touche le cloisonnement d'une famille tenue à l'écart).

**Décision.** Avant de lancer la passe du versant honnête, faut-il fixer dès maintenant que la famille aveugle de réserve du cycle 2 ne prendra pas les tâches du pilote ?

**Les faits.** Attestation de la session habilitée du coffre : branche `attestation/separation-versant-honnete-01qi7-v1`, commit 8475ac9c07, d3d0669a…. Elle donne :
- séparation des 64 tâches d'évaluation, dont les 60 du premier test : **oui** ;
- condition 1 (hors des 96) : **oui** ;
- condition 2 (aucune sortie de l'essai dans l'instrument) : **oui** ;
- condition 3 (disjonction d'avec la famille aveugle de réserve du cycle 2) : **indéterminée**. Aucune banque n'est encore attribuée à cette famille, donc l'intersection vaut zéro aujourd'hui.

**Enjeu.** Le devis de cette famille (`docs/notes/devis-famille-reserve-cycle-2-v1/devis-banque-d-episodes-famille-reserve-cycle-2-v3.md`, 1ab6eb4b…, point 4) laisse ouverts trois choix :
- (a) les 60 tâches du pilote, empreinte `287e8348…` ;
- (b) un tirage disjoint (sa recommandation, confiance 0,6) ;
- (c) les 60 du pilote sous attestation.

Or `287e8348…` est aussi l'empreinte de tâches que citent le premier test et le témoin positif. L'attestation sur manifestes (e3f1ee56…) montre que ces 60 tâches sont incluses dans les 64 du versant honnête. Si la réserve prenait plus tard (a) ou (c), le versant honnête aurait lu des épisodes et des scores sur les tâches de la famille tenue à l'écart : la réserve serait entamée.

**Options.**
- **(a) Fixer maintenant que la réserve du cycle 2 exclut les 96 tâches de l'environnement**, c'est-à-dire l'option (b) de son devis, déjà recommandée. La condition 3 devient vraie par construction et la passe peut partir.
  - Avantage : aucun délai ; cohérent avec la recommandation du devis de la réserve.
  - Inconvénient : la réserve perd l'option gratuite (a) ; le tirage disjoint exige un devis à part.
- **(b) Lancer sans rien fixer**, avec une contrainte écrite : si la réserve prend les 60 du pilote, les sorties du versant honnête sur ces tâches sont à déclarer à sa conception.
  - Avantage : aucune option fermée.
  - Inconvénient : la réserve risque d'être entamée sans retour possible.
- **(c) Attendre le choix de la banque de la réserve.**
  - Avantage : rien d'engagé.
  - Inconvénient : le versant honnête recule, peut-être après l'entretien.

**Recommandation.** (a), confiance 0,75. Le devis de la réserve recommande déjà le tirage disjoint, et seul ce choix rend la condition vraie sans attendre.
