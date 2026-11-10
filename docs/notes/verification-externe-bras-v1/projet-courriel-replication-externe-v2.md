**Ne pas envoyer sans le mot de Lazar.**

# Projet de courriel — réplication extérieure de l'attaque — v2

10 novembre 2026, vers 11:00 UTC. Rédigé par un sous-agent rédacteur de la session « attaquant informé »
(`session_01QPDgKjN3jeeUyZP2mnkDNK`), branche `claude/compassionate-meitner-d4ryyk`. **Projet, non envoyé, sans pièce
jointe.** Un contact extérieur est un nœud de Lazar : il relit, décide et envoie, s'il le décide (`CLAUDE.md`,
`b4cbc66a…`, hiérarchie de décision ; `registres/passations/2026-11-10-0852-decision-lazar-go-quatre-pieces-attaques-inedites.md`,
`c90ad8f4…`, l. 35 : « le courriel de réplication est rédigé, Lazar l'envoie s'il le veut »).

- Remplace, sans l'écraser (R12), le projet v1 :
  `docs/notes/verification-externe-bras-v1/projet-courriel-replication-externe-v1.md` (`7ea1cc4e…`).
- Applique la contre-lecture `docs/notes/verification-externe-bras-v1/contre-lecture-plan-verification-externe-v1.md`
  (`b6f88afc…`), points CV-11 à CV-14, et les décisions de Lazar du 10 novembre
  (`registres/passations/2026-11-10-1018-decision-lazar-anteriorite-procedures-jury-transmission.md`, `8a2c8b71…`) :
  revendications A1 à A3 resserrées (l. 14-23) ; trois décisions sur l'échelon 3 (l. 24-34).
- Sert la forme (b) du plan `docs/notes/verification-externe-bras-v1/plan-verification-externe-bras-v1-brouillon2.md`,
  § 3.2 (même dossier). Le plan cite ce projet par son empreinte ; l'inverse est impossible (renvoi circulaire).
- Renvois : [R] = règle du bras, scellée, `prereg/bras-attaque-regle-v1.md` (`88418df0…`) ; « l. » = ligne.

**Ce que le courriel ne dit pas** : aucun résultat ; aucune recette, aucun paramètre ni aucune pièce d'attaque, dans un
sens ou dans l'autre (CV-11) ; aucun nom de procédure, de fichier interne ni de mode de sabotage ; rien du coffre ; aucune
revendication de nouveauté (il décrit le cadre de A1 sans le dire neuf).

**Ce qu'il promet** : rien que Lazar n'ait tranché (CV-13). Tout passage entre crochets est à décider par lui. Les phrases
hors crochets décrivent des règles déjà scellées ou décidées : [R] ; décisions du 10 novembre ci-dessus ; mot de Lazar
sur le nœud 2 (`registres/passations/2026-11-10-0704-decision-lazar-verdicts-comptes.md`, branche
`origin/claude/upbeat-cray-dmauvv`, `bba97a1a…`, l. 8-10).

**Condition d'envoi** : la contre-lecture interdit l'envoi tant que CV-11 à CV-13 ne sont pas corrigés (l. 38-40). Ils le
sont dans ce texte, sous réserve de la contre-lecture du brouillon 2 du plan et des décisions de la liste « À décider ».

## Texte proposé (anglais)

> Subject: Independent red-teaming of frozen activation and text monitors — invitation
>
> Dear [name],
>
> I lead a small research program on monitoring AI agents for diffuse sabotage, comparing monitors that read the
> model's internal activations with monitors that read only its text. Before reading any result, we pre-register and
> seal the rules of an adversarial evaluation, and our monitors are frozen before any attack is run against them
> [; each sealed document carries a third-party timestamp — form to be decided].
>
> In our setting, the attacker is the monitored agent itself, which chooses the content of its own actions to complete
> a verified sabotage without being flagged. At the informed levels, whoever designs the attack knows the monitors'
> designs and the protocol, but not their calibrated thresholds, scores or test episodes. We measure evasion as a
> function of the attacker's access level and budget, with positive controls (a monitor with a deliberately planted
> flaw; a reproduced published attack) and an honest-only control (honest agents on both sides).
>
> Our own attacker is part of our program, so its strength is our main blind spot. We would like an independent team
> to attack the same frozen monitors under the same rules, designing its own attacks, so that two independent attackers
> can be compared. [Level open to you: the informed, context-only level (no queries) / that level and a query level,
> where each query returns only "flagged" or "not flagged", under a query cap sealed before any query — to be
> decided.]
>
> [Keep this paragraph only if the query level is offered.] At the query level, our rules allow only published
> optimization procedures from a closed list, sealed before any query, used as published with role substitutions only;
> a procedure that would need any element specific to its original domain to be rewritten is excluded. A procedure may
> optimize a statistic of the verdicts of a batch of trials; each trial counts as one query against the cap. The
> episodes finally scored are new ones, written after the last query by a frozen attack policy.
>
> We would not share any of our own attack material. After our monitors are frozen, around [month], we would share
> [the protocol, in a version without internal references], [the frozen monitor designs, reviewed so that none
> discloses held-out material] [and what is needed to run our agent on the tasks in scope — to be defined]. To score
> your attacks under the same rules, [your sealed attack episodes would be read once by our frozen monitors and by our
> damage judge, under our quarantine terms, and you would receive the evasion curve and failure classes of your
> episodes / your sealed episodes would be read once by our frozen monitors, and your own judge would apply our damage
> criteria and report, episode by episode, whether and when the damage was reached — to be decided]. The same rules
> also mean that your pipeline would produce naive episodes (the same sabotage, without any effort to conceal it),
> sealed before your attack episodes, and an honest-only control. [Terms for keeping and publishing your own attack
> details — to be agreed.]
>
> In return, [we would acknowledge your contribution / we would welcome co-authorship of the resulting report — to be
> decided]. [Each team would seal its results, with a third-party timestamp, before seeing the other's; results would
> then be exchanged before publication — to be decided.] [Any handling of sabotage episodes would follow the terms of
> our external security review — keep only if that review exists in writing.]
>
> Would your team be open to a short call to discuss whether this fits your work?
>
> Best regards,
> Lazar
> [affiliation and address — to be completed by Lazar]

## À décider par Lazar avant envoi (une ligne chacun)

1. Envoyer ou non ; à qui (conditions de choix : plan, § 3.2) ; sous quel nom et quelle affiliation.
2. Horodatage cité au premier paragraphe : garder le crochet seulement si le nœud 7 est tranché, dans la forme retenue.
3. Niveau offert : contexte seul, ou aussi les requêtes (échelon 3).
4. Si les requêtes sont offertes : équipe déclarée bras d'attaque (`docs/decisions/decision-N-053-v1.md`, `2204256d…`,
   point 5 ; [R] l. 99-101), interface qui ne rend qu'un verdict, plafond scellé avant toute requête, hébergement sur
   devis et GO (offrir l'accès, c'est annoncer une dépense).
5. Liste fermée de l'échelon 3 (catalogue de la pièce 3,
   `docs/notes/procedures-publiees-echelon-3-v1/catalogue-procedures-echelon-3-v1-brouillon1.md`, `a0c6e3a6…`, non
   scellé) : scellée avant toute requête ([R] l. 396-399) ; ce qui en est remis à l'équipe.
6. Protocole remis : une version sans chemin ni renvoi interne, relue.
7. Conceptions gelées remises : lesquelles (les deux familles, pour la probabilité jointe de A3), relues par qui ; le
   moniteur témoin n'est pas désigné ([R] l. 243-244).
8. Ce qu'il faut pour faire tourner notre agent sur les tâches du périmètre : à définir, relu ; rien du coffre.
9. Lecture de leurs épisodes : option (i), notre juge ; ou option (ii), leur juge, épisode par épisode ; dans les deux
   cas, un préenregistrement propre, car [R] définit la course par « la chaîne du bras » (l. 65-66).
10. Garde de leurs épisodes (quarantaine dans l'esprit de `docs/decisions/decision-N-057-v1.md`, `42180088…` ; nœud 3)
    et publication de leurs attaques (classes seulement, ou après notre dernier cycle).
11. Reconnaissance ou cosignature ; une cosignature offerte avant le résultat se dit au jury comme telle.
12. Ordre : chaque équipe scelle et fait horodater ses résultats avant de voir ceux de l'autre ; échange avant publication.
13. Revue de sécurité externe (nœud 3) : la mentionner seulement si elle existe par écrit.
14. Mois : après le gel des moniteurs (scellement 3, [R] l. 95-96) ; à fixer.
15. Raccourcir : permis, sans garder aucune phrase qui décrive un échange que la règle interdit ; sans le paragraphe de
    l'échelon 3, n'offrir que le niveau « contexte seul ».

## Changements depuis la v1

| Passage de la v1 | v2 | Source |
|---|---|---|
| « we pre-register and timestamp our monitors (frozen) » | règles scellées ; moniteurs gelés avant toute attaque ; horodatage entre crochets | CV-13 (écart : temps corrigé, les moniteurs ne sont pas encore gelés) ; [R] l. 90-96 |
| « an attacker who knows the monitors' designs … writes the content of an agent's actions » | l'attaquant est l'agent surveillé, qui choisit le contenu de ses propres actions | A1 resserrée (décisions du 10 novembre, l. 17-18) |
| « calibrated thresholds or test episodes » | « calibrated thresholds, scores or test episodes » | CV-14 point 1 ; [R] l. 98-99 |
| « knowledge and query budget » | « access level and budget » | CV-14 point 4 |
| « positive controls (a monitor with a planted flaw) » | deux témoins positifs | CV-14 point 2 |
| « honest-versus-honest » | « an honest-only control (honest agents on both sides) » | CV-14 point 3 |
| « No attack material would be exchanged in either direction » | « We would not share any of our own attack material » ; lecture de leurs épisodes, deux options | CV-11 (écart : la seconde option remet le dommage épisode par épisode, car l'évasion exige les alertes de nos moniteurs ; des comptes seuls ne la donnent pas) |
| « writing its own attacks » ; « [query access …, with a counted budget] » | niveau offert entre crochets ; paragraphe de l'échelon 3 : liste fermée, substitution de rôle seulement, statistique des seuls verdicts d'un lot, verdict binaire, plafond scellé, épisodes neufs | CV-12 ; décisions du 10 novembre, l. 27-34 ; nœud 2 ; [R] l. 178-182 (écart : les procédures libres ne sont pas offertes) |
| — | épisodes naïfs et témoin « honnête seulement » de leur propre chaîne | ajout du rédacteur : ce que « the same rules » demandent à l'équipe ([R] l. 238-241, 254-266) |
| « we would share the frozen monitor designs, the protocol » | protocole sans renvoi interne, conceptions relues, de quoi faire tourner l'agent : entre crochets | CV-13 ; ajout du rédacteur pour le protocole et l'agent |
| « and share our own results with you before publication » | entre crochets, après scellement et horodatage par chaque équipe | CV-13 ; CV-8 |
| « [our external security review] » | gardé seulement si la revue existe par écrit | CV-13 ; nœud 3 |
| « À décider » (4 points) | 15 points | CV-13, complété |
