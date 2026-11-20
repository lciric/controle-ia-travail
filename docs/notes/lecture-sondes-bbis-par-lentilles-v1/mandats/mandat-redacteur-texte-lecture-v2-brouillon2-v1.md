# Mandat donné au rédacteur du brouillon 2 du texte de lecture v2 (sous-agent sur Fable 5.2) — v1

- Versé par la session des lentilles le 2026-11-19, mot pour mot, mise en forme comprise (marqueur
  `DECLARATION_DE_LA_SESSION_DES_LENTILLES` du brouillon 2). Deux pièces : (1) le mandat initial, donné vers 10:52 UTC ; (2) le
  complément du même rédacteur, envoyé vers 11:03 UTC, avec les décisions de Lazar relayées par la mère.
- Brouillon issu : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon2.md`, `ff121bdd…`, commit `30fefa12`.

## (1) Mandat initial

Tu es le **rédacteur neuf du brouillon 2** du préenregistrement « lecture des sondes de l'étape B bis par lentilles, v2 » (pièce de classe A), dans le dépôt `/home/user/controle-ia-travail`. Tu es sur le modèle Fable : la règle de Lazar R-3735 (section « Qui conçoit » de `CLAUDE.md`, branche principale) confie à Fable la conception de ce qui est délicat. Français, sans acronyme nu, choses nommées en clair. Règles : `CLAUDE.md` (R1 à R14). Tu n'as écrit ni la v1, ni le brouillon 1, ni le critère, ni le devis.

## Pièces
- **Brouillon 1** : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon1.md` (`d6c3a6eedac25d8e2965730ea266c1674ad7b48272a577e7878bf7351838f3ab`). Rédigé sur Opus 5.5. Son mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-redacteur-texte-lecture-v2-brouillon1-v2.md` (`6d1b1280…`).
- **Sa contre-lecture** (branche principale) : `git show origin/main:docs/notes/neuron-lens-v1/contre-lecture-texte-lecture-lentilles-v2-brouillon1-v1.md` (`42024aa9…`). Conclusion : « pas avant », six corrections bloquantes B1 à B6 et quatorze non bloquantes, avec le texte avant et après. **Tu les traites toutes.** Le traitement de chacune va dans une table en tête : faite, ou refusée avec sa raison.
- **La v1 scellée** : `git show origin/main:prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d7…`).
- **Le critère d'identité v4** : `docs/notes/neuron-lens-v1/devis-reajustement/critere-identite-reajustement-lentilles-v4.md` (`60df6c53…`), en contre-lecture. Pour B1, le texte s'aligne sur **cette** version, dans les douze lieux que liste la contre-lecture. Retire le mot « équivalente ». Supprime « couverte par concordance ». Respecte ce que chaque mention autorise (§ 4 du critère v4) : seul le palier 1 établit l'identité, et en variante A au palier 2 aucune lecture sans nœud de Lazar.
- **Le devis v4** : même dossier, `devis-reajustement-lentilles-b-beta-v4.md` (`770a7794…`).
- **Le programme de comparaison** (code d'instrument de la session des lentilles), pour citer ses sorties : `src/controle_ia/neuron_lens/comparer_reajustement_v2.py`. Une v3 est en cours ; cite-le par son rôle, sans figer une empreinte qui va changer.

## Consignes de la mère (en plus de la contre-lecture)
- **B2** : la déclaration d'exposition dit :
  - que la décision de Lazar (GO-2026-11-19-33, 2026-11-19 vers 10:05Z) est postérieure au verdict de l'étape B bis (clé `VERDICT-BBIS`, 00:13:25Z) ;
  - qu'il y a deux sessions « mère » et quelles sont leurs déclarations ;
  - le mandat du rédacteur du brouillon 1, versé ci-dessus ;
  - l'état de la première passe au scellement.
  L'ancre datée est le commit du brouillon 1, `8a22361e`, à 10:27:59Z. Corrige aussi la sanction de la retenue, qui vise la mauvaise passe.
- **B3** : ajoute les entrées de contre-lecture 3 et 4 de la v2.
- **B4 et B5** : résous les trois contradictions de la liste d'arrêt, et écris la règle de la reproduction.
- **B6** : les valeurs de la tranche (tirées du verdict « partiel ») ne sont pas vérifiées. Lazar choisira entre une vérification par un lecteur qu'il désigne et le retrait des valeurs chiffrées. Écris le brouillon 2 pour que les deux options restent possibles, par exemple avec les valeurs dans un bloc séparable, nommé et borné, que l'on peut retirer sans toucher au reste.
- **Point 7** : le compte des lignes de la v1 touchées est « 10 lignes prolongées et 5 réécrites », non « 15 prolongées ». Vérifie-le toi-même par un diff.

## Cloisonnement — tu ne lis JAMAIS
- la liste « Jamais ouverts » de la v1 ;
- toute sortie, tout score, toute table, toute lecture ou tout verdict de l'apprentissage des sondes sur la tâche (étape B bis), y compris son verdict ;
- toute table ou sortie de la lecture par la lentille publique ;
- les branches `donnees/*` et `calcul/*` ;
- tout `diag/` ou `runs/`, sauf les noms de clés et la structure de `diag/20261118-164930-neuron-lens-b-beta/b-beta-export.json` et `b-beta-ajustement-R.json` si tu en as besoin ;
- P3, P3-bis, T0.6, T0.7, l'étape B, le bras d'attaque, le saboteur à budget.

Tu peux lire le verdict « partiel » de la tranche (`docs/notes/neuron-lens-v1/lecture-b-beta/verdict-b-beta-v1.md`). Déclare-le.

**Refus d'outil** : tout refus d'une permission ou d'un classifieur n'est ni rejoué, ni reformulé, ni contourné. Tu le déclares.

## Forme et lieu
- Gabarit `prereg/gabarit-preregistrement-v1.md`. Lance le validateur sur ton brouillon et donne son résultat : `PYTHONPATH=src .venv/bin/python -c "from controle_ia import prereg; print(prereg.problemes(open('<chemin>').read()))"`, ou la forme que donne `src/controle_ia/prereg.py`.
- Travaille dans `/tmp/claude-0/-home-user-controle-ia-travail/ff3e16f4-e2c5-5d31-b08c-99762b9cded7/scratchpad/redacteur-fable-texte-v2b2/`.
- Copie ensuite dans `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon2.md` et scelle-le comme brouillon : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon2.md`.
- En tête : l'auteur (toi, modèle Fable 5.2), les heures `date -u`, et la table de traitement.
- Aucun commit, aucun push, aucune machine, aucune dépense, aucun modèle chargé. Ne modifie aucun fichier existant.

## Rends-moi
- le chemin et l'empreinte ;
- la table de traitement de B1 à B6 et des quatorze non bloquantes, une ligne chacune ;
- les nœuds pour Lazar, dont B6 et la règle du palier 2 ;
- les expositions et refus éventuels ;
- la confirmation que tu n'as rien ouvert d'interdit.

## (2) Complément

Les décisions de Lazar pour le brouillon 2 sont arrivées. Écris-les comme tranchées, avec les identifiants des lignes. Le mot de Lazar est « 1a, go recos », vers 10:57Z, R-3743, relayé par la mère.

- **B6, GO-2026-11-19-39, option (a).** Les valeurs de nos lentilles recopiées dans le texte (le bloc séparable) sont vérifiées contre le verdict de la tranche par un lecteur neuf. Ce lecteur n'a écrit ni le texte ni le critère, et il est d'un autre modèle que toi : Lazar l'a désigné sur Opus 4.6 (mot « lecteur opus 4.6 », 11:01Z). Son rapport est scellé et cité par le texte avant le scellement. Laisse dans le texte une place pour le chemin et l'empreinte de ce rapport.
- **N11 à N15, GO-2026-11-19-40**, selon les recommandations du contre-lecteur :
  - N11 (b), avec la déclaration B2 ;
  - N12 (b), réécrite : lecture au palier 2 sous la phrase permise du critère scellé, après une ligne de registre disant que Lazar a été averti de l'écart mesuré ;
  - N13 (a), avec les trois ajouts de la contre-lecture ;
  - N14 (a) ;
  - N15 (a) si la clé gardée est en lecture seule et du compte de Lazar, ce que vérifie l'essai d'un octet ; sinon (b).

Le reste de ta mission est inchangé.
