# Passation — session « attaquant informé », reprise sur le nouveau compte (20 novembre 2026, 12:55 UTC)

Session `session_01QPDgKiPN5vEiEdmAYKZt3W`, branche `claude/loving-lamport-7ol5ws` (partie de `main` à `da0d389c`).
Passation intermédiaire, écrite pendant l'autonomie de 12 heures (mot de Lazar vers 12:00Z, R-4237, jusque vers
2026-11-21T00:00Z). Une passation finale suivra vers 23:30Z. Ne se réécrit pas (R12).

## Fait

1. Routine de reprise.
   - Empreintes de lancement : correctes.
   - Arbre scellé : 107 écarts, tous des compagnons absents ou un nom de compagnon mal formé ; aucune
     empreinte fausse.
   - `registres/etat.md` non lu (cloison).
   - Passation de clôture lue, avec son empreinte vérifiée (`a3728bd5…`).
   - Rappels : aucun échu le 20 novembre.
   - Calcul : aucun serveur Hetzner ; cinq instances Vast à l'état « exited » (58936096, 58936099, 58936100,
     60988826, 61552174), laissées en l'état. Elles sont déjà arrêtées, une autre session en extrayait le
     contenu, et une destruction est irréversible.
2. Le brief demandait la branche `claude/compassionate-meitner-d4ryyk`. Ce compte n'autorise que
   `claude/loving-lamport-7ol5ws`, et son historique n'a aucun ancêtre commun avec `main`. Je travaille donc
   depuis `main`.
3. Pièces présentes sur l'ancienne branche et absentes de `main`, recopiées à l'octet, empreintes vérifiées :
   - `prereg/bras-attaque-regle-v1.md` (`88418df0…`) et ses addenda 1 et 2 ;
   - `prereg/temoin-attaque-publiee-bailey-v1.md` et ses addenda 1 à 8 (non lus) ;
   - trois briefs de l'attaquant sous `docs/procedures/`.
   La mère les recopiera sur `main` depuis cette branche.
4. Relais des deux directives de Lazar à la mère, scellé :
   `registres/passations/2026-11-20-0953-attaquant-informe-relais-directives-lazar-vers-mere.md` (`ae7c6f5e…`).
   La mère l'a reçu et inscrit (R-4179). La mère du nouveau compte est `session_01QPDgKgejkqwnuaJHJ31Ydo`.
5. Mots de Lazar transmis à la mère, qui les a inscrits (GO-2026-11-20-45) :
   - « ok pour la v4 » : la question de la course v4 (`47160d37…`) est approuvée, en attendant la note ;
   - le collisionneur sur le papier « dopamine » (Carbon, Fable 5.2, Astra, Opus 5.5, Argon, Kimi si
     possible) : pris par la mère, avec devis à Lazar, d'un ordre de grandeur de 30 USD.
6. Papier « dopamine » (Xu, Yuksekgonul et Zou, arXiv 2602.00986v2) :
   - PDF déposé : `docs/sources/pdf/2602.00986v2.pdf` (`da004f53…`) ;
   - mandat à Fable 5.2 : `docs/notes/papier-dopamine-moniteur-v1/mandat-fable-papier-dopamine-v1.md` ;
   - consultation rendue : `…/consultation-fable-papier-dopamine-v1.md` (`afc22a5f…`), non lue par cette
     session (cloison moniteurs), remise à Lazar et à la mère.
7. Note de périmètre sur les modes inédits, scellée par la mère :
   `prereg/ideation-nouvelles-attaques-v1/note-perimetre-modes-inedits-v3.md` (`dd6fea0e…`, R-4236),
   empreinte vérifiée sur `main`. Elle pose dix nœuds à Lazar.
8. Tests (`pytest -n 4`, `requirements-cpu.txt` installé) : 9882 réussis, 196 échecs, 412 sautés.
   - 178 échecs touchent les tests des lanceurs de T0.6 (`test_t06_*`) : leur GO figé finit le
     2026-11-16T23:58Z, et le lanceur refuse donc de démarrer « après l'échéance ». Ce sont des tests datés,
     pas une régression.
   - 18 autres échecs dépendent de l'historique, que `main` sur ce compte a réduit à 51 commits
     (commits cités, noms du dépôt réel), ou d'un module absent (`test_corpus_arxiv`).
   - Aucun échec ne touche les fichiers ajoutés par cette session (textes et PDF seulement).

## Reste

- Réponses de Lazar aux dix nœuds de la note de périmètre, puis son mot sur le devis : la course ne part pas
  avant.
- Scellements 2 (familles aveugles) et 3 (moniteurs gelés) du bras d'attaque ; revue de sécurité externe.
- Nœuds pendants, inchangés, tous au mot de Lazar :
  - effacement des quatre instantanés ;
  - révocation de clés ;
  - purge de l'historique (`2a1c0ff9`) ;
  - pièce 4 (courriel v4).
- Tests datés de T0.6 : à rafraîchir ou à marquer par leurs auteurs. Ce n'est pas le rôle de l'attaquant ;
  signalé à la mère.

## Réserves

- Environnement : aucune clé Anthropic. Les clés OpenAI, Gemini (deux) et Kimi sont présentes, lues par leur
  nom seulement.
- La consultation de Fable n'a pas de contre-lecture (classe C).

## Instances actives

Aucune lancée par cette session. Aucune dépense.

## Prochaine action

Attendre les réponses de Lazar et les pièces de la mère. Points d'étape programmés : 16:01Z, puis passation
finale à 23:30Z.
