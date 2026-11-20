VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — additif 3 de la ligne 3 (puissance de la règle de portée à 200) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sous GO-2026-11-20-26 (règle R2 : contre-lecture par un agent neuf d'un autre modèle que le rédacteur).

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit ni le préenregistrement, ni les additifs, ni le code, ni le verdict de l'étage 1. Tu signes « contre-lecteur, modèle O ».

## Règle d'aveugle

Tu ne lis aucune mesure de l'étage 1 (ni `…/execution-etage-1-v1/`, ni `…/verdict-etage-1-v1/`, ni le verdict scellé). Faits admis : verdict « non, pas à cette taille » ; tolérance tenue à 200 et 400, pas à 100 ; puissance qui décide à n = 100 : 0,160.

## Ce qui fait foi (tire de main par `fetch`, puis `git show` redirigé ; vérifie chaque empreinte)

- PR `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`), A1 `prereg/organisme-auto-conception-v9/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` (`e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0`), A2 `prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md` (`f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`), DV `prereg/organisme-auto-conception-v9/devis-ligne-3-etage-payant-v7.md` (`382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270`), `registres/go.md` (ligne GO-2026-11-20-26).
- Le banc : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` (`09bfe0db…`), lu, jamais lancé.
- Dossier A3 = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-3-portee-200-v1/` : le mandat du rédacteur (`c6dac15d…`), `additif-3-preenregistrement-ligne-3-portee-200-v1.md` (`9e189f1af673e07460e96fe17537727f445ee3e415c53cb24429787e9a898915`), `rapport-redacteur-additif-3-portee-200-v1.md` (`6e008e56…`).

## Ce que tu vérifies

1. **Fidélité au GO** : l'additif ne fait que ce que GO-26 décide (mesurer la puissance de la portée à 200 avant toute dépense, puis l'étage 2 à 200 sous 88,36 USD) ; il ne change aucune hypothèse, prédiction, seuil ni critère gelé hors de cet écart ; tout ce qu'il ajoute est soit couvert, soit écrit comme point à Lazar.
2. **La mesure** : même monde, mêmes comparaisons, Holm, « la plus basse », mêmes cellules ; nombre de répliques, faisabilité (« ne dépend pas de n » : vrai d'après le code et PR l. 236 à 241 ?) ; ce qui est rapporté sans décider.
3. **La prédiction ajoutée** (0,30 à 0,50, confiance 0,6) : son calcul est-il écrit et refaisable ? Recalcule-la à la main ou par un calcul exact ou approché que tu écris (sans lancer le banc) ; signale si elle est calée sur une mesure vue.
4. **Les graines** (2026112031 à 2026112033) : neuves, dérivées par `SeedSequence`, refus des anciennes racines écrit.
5. **La règle de lecture** (issues A, B, C ; comptes entiers ; seuil 1 000 sur 2 000 « ou plus » contre « sous 0,5 strict ») : complète, sans trou ni recouvrement, cohérente avec PR l. 240 et 343.
6. **La table d'héritage pour 200** (1 004 appels ; plafond ; banque doublée ; moitié lecture ; « 100 premiers verdicts ») : recalcule les 1 004 appels et le recoupement à 44,78 USD sur les chiffres du devis ; dis ce qui est juste, ce qui manque, ce qui changerait un critère gelé.
7. **Les quatre points laissés à Lazar et le point de procédure** (second additif court pour le code et les racines, ou additif 3 seul) : juge chacun, et recommande.
8. **L'écart déclaré** (deux `git show --name-only`) : l'additif en est-il affecté ?

Rends `contre-lecture-additif-3-portee-200-v1.md` : « Conforme » ou « À corriger », corrections numérotées avec le texte exact (ancien → nouveau, chaque ancre unique dans l'additif, comptée par `grep -c -F -e`). Préfère « non exigé » pour la tenue pure. Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-additif-3-ligne-3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du banc. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
