# Question — à Argon seul, au collisionneur (quatre espèces, deux tours), à GPT-6 Astra quand il sera branché, et à conv-audit (réponse propre, à comparer puis fusionner) — la boucle de sélection génération à génération de l'organisme d'idéation — v1

conv-audit, 1er novembre 2026 (heure UTC en tête du registre, R-1044). Demande de Lazar (09:48 UTC) : « envoie-la à Argon, collisionneur, Astra et toi-même, et on compare puis fusionne ». Dépense : nœud chez session-depot (mot direct de Lazar). Niveau méthode ; aucune pièce du bras d'attaque. Toute recommandation des auteurs est retirée et servie au tour 2 seulement. **Objectif fixé par Lazar le 1er novembre** : la course 2 doit produire des idées inédites, originales et **validées par l'expérience** (tests de mort, pôle) ; une idée non concluante ne passe pas à la génération suivante ; seules les hypothèses à tester pour le programme en sortent.

## Pièces servies (faits)

1. Dossier factuel de l'organisme : `docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md` (`0751fc8c…`), § 1 (deux étages ; nœuds du pôle : fiche-loi → gel → expérimentateur → affinage → juge figé → sélection → recombinaison → mémoire → génération suivante), § 6 (juges et juge figé), § 9 (tests de mort ; chaîne réglementaire R1, R2, R7, R13), § 10 (ce qui teste par calcul).
2. Conception du pôle : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/integration-proposeurs-ia-v1.md` (§ 2, l. 42-98 : aptitude = sévérité du test survécu ; archive des éliminées ; recombinaison des survivantes) ; `programme-conception-organisme-v7.md` (l. 23-33 : juge figé, 5 % de fausses promotions, règle de fausses découvertes e-BH entre hypothèses, témoins plantés).
3. Lectures des lancements réels du pôle et de la couche 1 bis (plomberie tenue, « pas de dents » sur la banque réelle) : `…/premier-lancement-reel/lecture-lancement-reel-a-bis-v1.md`, `…/demonstration-couche1-v7/lecture-couche1-v7-v2.md`, `…/demonstration-cycle-v5/lecture-demonstration-cycle-v5-v1.md`.
4. Le pont fiche → loi testable (conception en cours, `…/pont-fiche-loi-v1/`, servi s'il est rendu avant le lancement).
5. Les hypothèses du programme (H1 à H9, HC1 à HC5) : `docs/programme-controle-ia-v2.md` et `docs/decisions/` (N-013, N-035).

## La demande de Lazar, reformulée (c'est l'objet à critiquer)

Concevoir et préenregistrer la boucle de sélection génération à génération de l'organisme : (a) **règle de survie gelée** — une fiche passe à la génération suivante si elle survit à son test de mort *et* est promue par le pôle, avec contrôle des fausses découvertes sur l'ensemble de la génération et partie d'épreuve renouvelée par génération ; (b) **héritage** — les survivantes avec leurs preuves, les éliminées avec leur raison (la mémoire refuse aussi les mortes) ; (c) **règle de sortie vers le programme** — neuve par rapport aux hypothèses du programme et décisive pour une porte, alors seulement préenregistrement ; (d) **garde de diversité** (pas d'effondrement sur une lignée) ; (e) **comptabilité du coût par survivante** ; (f) **ablation préenregistrée** — génération 2 avec et sans filtre du pôle, métriques gelées : survivantes neuves par euro, témoins plantés ; (g) sur le pont fiche → loi, en bac à sable, machine jetable, devis.

## Questions (tour 1 : avis propre — option, confiance, pire cas et garde, option manquante, pièce qui trancherait)

- **Q1 — Règle de survie.** « Survit au test de mort *et* promue par le pôle » : est-ce la bonne conjonction, ou faut-il trois états (morte ; vivante non testée par le pôle, faute de loi traduisible ; promue) et un sort pour la seconde ? Comment contrôler les fausses découvertes sur toute une génération (e-BH ; e-valeurs ; FDR par famille) sans tuer la puissance quand les fiches sont peu nombreuses ?
- **Q2 — Fuite entre générations.** Si la génération 2 est sélectionnée sur la même partie d'épreuve que la génération 1, qu'apprend-elle ? Quelle règle de renouvellement (partie jamais vue par génération ; rotation ; banque croissante) et quel coût en données ?
- **Q3 — Héritage.** Que transmettre exactement : la fiche survivante, sa loi, ses preuves, son rang ? Transmettre les éliminées avec leur raison aide-t-il (ne pas reproposer) ou nuit-il (ancrage) ? Quelle antériorité (algorithmes évolutionnaires avec archive ; MAP-Elites ; novelty search) ?
- **Q4 — Sortie vers le programme.** Quelle règle écrite fait d'une survivante une hypothèse du programme : neuve par rapport à H1–H9 et HC1–HC5, décisive pour une porte, coût borné ? Qui la lit (lecteur neuf, R13) ?
- **Q5 — Diversité et coût.** Quelle garde contre l'effondrement sur une lignée, et comment compter le coût par survivante (appels, carte, temps) pour comparer des générations ?
- **Q6 — Ablation.** Le dessin « génération 2 avec et sans filtre du pôle » est-il jugeable (puissance, témoins plantés, graines) ? Quelle métrique un expert choisirait-il : survivantes neuves par euro, ou autre ?
- **Q7 — Ce qui existe.** Quels systèmes publiés font déjà une sélection génération à génération d'hypothèses par l'expérience (AI Scientist v2, Agent Laboratory, Co-scientist, Robin, algorithmes de qualité-diversité, programmation génétique avec test) et que faut-il reprendre tel quel ?

## Ce que les réponses ne doivent pas contenir

Aucune conception d'attaque ; rien sur l'auto-organisation de l'organisme inspirée d'Avalon (sujet suspendu).
