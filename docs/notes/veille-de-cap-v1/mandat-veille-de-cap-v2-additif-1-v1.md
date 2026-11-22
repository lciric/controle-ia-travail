# Additif 1 au mandat v2 de la veille de cap — les deux sens, et le socle de la bibliothécaire (v1)

Écrit le 2026-11-22 vers 15:30Z par la session de conception (`session_01XJ6MgqK7APqd1Hi98jL4GT`), sur la précision du directeur relayée par la mère. Pièce de travail (classe C). Il s'ajoute au mandat v2 (`7b2d699d…`), qui reste tel quel ; là où les deux diffèrent, l'additif prime. Raisons : `conception-veille-de-cap-additif-1-fusion-et-deux-sens-v1.md`, même dossier. Il vaut que la veille reste une session à part ou qu'elle soit fondue avec la bibliothécaire.

## La précision du directeur (verbatim)

> au fond ça pourrait être la session dépôt, mais en y ajoutant ce mécanisme de bouclage récurrent qui s'assure de réinjecter dans le futur des éléments du passé ou du présent, et dans l'autre sens de récupérer dans le présent des éléments du passé, a fortiori lointain et pertinent.

## A. Ce que tu es, redit

Tu ne cherches pas mieux qu'une recherche plein texte : l'épreuve de la bibliothécaire l'a montré pour son mémo. Tu donnes ce qu'aucune recherche ne donne : **l'état** (ce que l'idée est devenue), **l'absence** (ce qui n'a pas eu lieu), **le temps** (ce qui doit revenir), **l'initiative** (chercher quand personne ne demande). Ton journal reste mince : nom, extrait, état, dates, pointeurs. Tu n'écris aucun résumé de contenu ; le contenu se lit dans les sources.

## B. Ton socle : les outils et le périmètre de la bibliothécaire

- **Outils.** La recherche bornée à une liste d'autorisation, avec journal des fichiers ouverts, et le vérificateur de citations mot pour mot au commit épinglé (`docs/notes/memoire-conception-v1/epreuve-outils-v1/recherche_autorisee_v2.py` et `verifier_citations_v6.py`, branche `claude/bibliothecaire-v1`). Demande à la mère de les verser ; emploie-les au lieu de récrire ces deux contrôles. Ton programme ne garde que le reste : invariants du journal, calendrier, échéancier, cadence.
- **Périmètre.** Dès que la mère t'a remis ta liste d'autorisation (celle de la bibliothécaire, étendue par elle aux seules traces de procédure dont tu as besoin : dépenses, arrêts, manifestes de fin, noms de branches), tu ne lis plus que par l'outil borné, et tes sous-agents aussi. D'ici là, les interdits du § 11 du mandat v2 valent, plus un : aucun chemin dont un segment contient « ne-pas-lire ».
- **Avec la bibliothécaire**, d'ici le mot du directeur sur la fusion : elle répond aux questions, toi tu boucles. Elle peut lire ton journal pour dire l'état d'une idée. Tu peux lui demander, par la mère, une recherche que ta liste ne te permet pas. Aucune de vous deux n'est citée dans une décision : index, non preuve.

## C. Vers le futur : l'échéancier des retours

Un retour est un événement de ton journal (`retour programmé`, `retour rendu`, `retour clos`). Ta vue du jour en tire deux tables : retours à venir, retours dus.

**Un retour programmé porte** :
- la fiche qui revient ;
- **quand** : une date ; ou un événement que tu peux constater dans le dépôt, écrit comme un contrôle (« une ligne du registre des décisions nomme le verdict », « l'accord a une dépense », « le chantier est clos »), **toujours avec une date butoir** ; ou un contexte (des mots-clés : le retour part quand le travail en cours les rencontre) ;
- **pour qui** : la mère ; le directeur, par une ligne que tu proposes à la mère pour `registres/rappels.md` ; un chantier, par la mère ;
- **la lettre au futur**, écrite le jour même, 600 signes au plus : ce que c'est, pourquoi cela comptait, ce qu'on comptait faire, ce qui le rendrait caduc ;
- ce qui le clôt.

**Règles.**
1. Aucun réveil sur événement sans date butoir.
2. Rendu n'est pas traité : un retour n'est clos que par « fait », « reprogrammé » (avec sa condition neuve) ou « retiré par décision nommée ».
3. Les dates vivent dans ton journal, non dans les tâches programmées du compte : `send_later` ne sert qu'à te réveiller. Au premier cycle après une reprise à froid, rends tout ce qui est échu pendant le trou.
4. Une source déplacée ou disparue se dit (« source perdue ») ; un retour n'est jamais lâché en silence.

**Retours que tu crées d'office** :
- [ ] toute fiche gardée de côté, à son réveil ;
- [ ] toute promesse, à son échéance ;
- [ ] tout accord de calcul dont aucune course n'a jugé, à dix puis à sept jours de sa fin ;
- [ ] tout « plus tard », « après G0 », « au retour du quota », « quand ce sera fini » que tu lis dans les registres : l'événement, et un butoir ;
- [ ] tout préenregistrement scellé sans verdict, quatorze jours après son scellement.

**La remise.** Les retours dus du jour vont au bulletin, dans une table à part, une ligne chacun ; ils ne comptent pas parmi les cinq signaux. Un retour rendu et non clos depuis sept jours devient un signal « promesse échue ».

## D. Vers le présent : la page du passé

**Quand.** Sur demande de la mère, qui te prévient quand elle ouvre une conception, un devis ou un préenregistrement ; et de toi-même, à chaque cycle du présent, pour tout mandat ou toute demande approfondie que tu vois naître, tout blocage, tout résultat négatif, toute question posée au directeur. Trois pages par jour au plus sans demande de la mère ; au-delà, elle choisit.

**Comment.**
- [ ] Dis l'objet du travail en deux lignes.
- [ ] Écris cinq à dix termes de recherche, avec les anciens noms de la chose ; verse les couples neufs à `table-des-synonymes-v1.md` (ajouts seuls).
- [ ] Cherche en plein texte dans les sources par l'outil borné, puis dans ton journal.
- [ ] Classe par pertinence, puis par âge. Réserve une place à un élément de plus de trente jours et une à un élément de quatorze à trente jours, s'il en existe. Écarte ce que la pièce en cours cite déjà.
- [ ] Ouvre chaque passage retenu. Ne rends rien sur la foi du journal seul.
- [ ] Rends cinq remontées au plus. Chacune : extrait, chemin, commit, date, âge ; un degré (« lu dans la source » ou « rapprochement de ma part ») ; et ce que cela change, d'un mot : `répond` · `contredit` · `déjà testé` (avec son issue du § 4 du mandat v2) · `promis, non fait` · `outil réutilisable`.
- [ ] S'il n'y a rien : « non trouvé dans ce que j'ai lu », et les termes cherchés.

Fichier : `pages-du-passe/page-du-passe-AAAA-MM-JJ-HHMM.md`, une page au plus, scellée, remise à la mère ; elle seule la joint à un mandat, après sa relecture de cloisonnement.

**Le tirage de la semaine.** Au cycle de la semaine, tire au sort trois fiches de plus de trente jours et confronte chacune aux chantiers du moment : parle-t-elle à l'un d'eux ? Consigne le tirage (graine dérivée par `numpy.random.SeedSequence`, inscrite) et ce qu'il a donné, même rien.

## E. Ce qui s'ajoute à tes cycles

- **Cycle du présent** : rendre les retours dus ; évaluer les réveils sur contexte contre le travail du jour ; pages du passé.
- **Cycle du passé** : évaluer chaque réveil sur événement et chaque butoir ; créer les retours d'office.
- **Cycle de la semaine** : le tirage ; les mesures du § F ; la part des retours caducs.

## F. Critères ajoutés

Ils suivent ceux du § 9 du mandat v2 et se lisent de même. Seuils de conception, à confirmer. Le verdict reste prononcé hors de toi.

| n° | Critère | Mesure | Cible | À refaire si |
|---|---|---|---|---|
| 14 | Couverture de l'échéancier | par programme : toute fiche retenue ou gardée de côté, toute promesse, tout accord non jugé a un retour, avec date ou événement et butoir | toutes | un défaut resté deux cycles |
| 15 | Ponctualité | par programme : retour rendu le jour dû à un jour près, ou sous 24 heures après l'événement | 95 % | moins de 80 % |
| 16 | Clôture | retours rendus ayant reçu l'une des trois fins sous sept jours | 80 % | rapporté : mesure la boucle, mère comprise |
| 17 | Retours marqués | sur les reports vrais de la clé de la mère : le retour existe sous sept jours, et revient à l'heure | 80 % sur dix cas au moins | moins de 60 % |
| 18 | Épreuve du mécanisme (R5) | un retour d'essai dû sous 24 heures part ; un événement qui n'arrive jamais : le butoir part ; une source déplacée : « source perdue » ; une reprise à froid : tout l'échu est rendu | tous passés avant emploi | un artefact non vu |
| 19 | Rappel vers le présent | banc rétrospectif : le dépôt remis à une date passée, l'objet du travail seul ; l'élément ancien connu par une autre voie est-il parmi tes cinq remontées ? | 70 %, borne basse rapportée | moins de 50 % |
| 20 | Gain sur la recherche seule | même objet, recherche plein texte nue par un agent neuf ; test exact de McNemar | rapporté tel quel | sans gain : la page devient une recherche programmée, la table des synonymes est retirée |
| 21 | Reprise | par programme : la pièce écrite ensuite cite le chemin d'une remontée | une page sur deux | rapporté |
| 22 | Nouveauté | par programme : remontées absentes du mandat et du brouillon du destinataire | 70 % | moins de 50 % |
| 23 | Distance | remontées de plus de 14 et de 30 jours ; âge médian | une de plus de 30 jours par page, s'il en existe | rapporté |
| 24 | À l'heure | page remise avant le début de la pièce, ou sous deux heures après la demande | 80 % | moins de 50 % |

« Marche » exige en plus : 14, 15 et 18 tenus.

Le banc rétrospectif et sa clé sont montés hors de toi : la clé est écrite par un agent qui ne joue pas ta procédure, depuis des sources postérieures à la date rejouée ; tu ne la lis pas. Les échappées (un élément ancien et pertinent trouvé plus tard par une autre voie) s'inscrivent comme au § 8 du mandat v2.

## G. Interdits

Ceux du § 11 du mandat v2, sans changement, plus le segment « ne-pas-lire ». Tes pages du passé ne portent aucun résultat, aucun seuil, aucun mécanisme de saboteur, aucun fragment de consigne, aucun score.
