# Mandat donné au rédacteur du brouillon 1 du texte de lecture v2 (versé après coup, B2 de sa contre-lecture) — v2

- v2 = v1 (`mandat-redacteur-texte-lecture-v2-brouillon1-v1.md`, `87cca750…`, archivée) corrigée : la v1 se disait « recopiée à
  l'identique » alors que ses listes avaient été remises en paragraphes ; la v2 donne le texte de l'appel **mot pour mot**, mise en forme
  comprise. Versé par la session des lentilles le 2026-11-19 (contre-lecture du brouillon 1, `42024aa9…`, B2).
- Mandat donné vers 10:07 UTC au rédacteur (sous-agent neuf de la session des lentilles, modèle Claude Opus 5.5) ; brouillon 1 issu :
  `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon1.md`, `d6c3a6ee…`, commit `8a22361e` (10:27:59Z).

---

Tu es le **rédacteur neuf** d'une version neuve d'un préenregistrement (pièce de classe A), dans le dépôt `/home/user/controle-ia-travail`. Français, sans acronyme nu, choses nommées en clair. Règles du programme : `CLAUDE.md` (R1 à R14, interdits) ; décisions sur les classes de pièces : ligne GO-2026-11-19-26 de `registres/go.md` (branche principale : `git show origin/main:registres/go.md`). Tu n'as écrit ni le texte scellé ni le devis cités ci-dessous.

## Ce qu'on te demande
Écrire **la version 2** du texte scellé `prereg/lecture-sondes-bbis-par-lentilles-v1.md`. Il se trouve sur la branche principale : `git show origin/main:prereg/lecture-sondes-bbis-par-lentilles-v1.md`, empreinte `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`, vérifie-la.

Cette v1 décrit, au processeur et sans dépense, quels jetons et quels pôles poussent les directions des sondes apprises sur la tâche (étape B bis de T0.7) et des lecteurs honnêtes. Elle les lit par la **lentille publique** R de Neuronpedia et la lentille des logits. Son nœud N10 et sa section « Frontière », point 6, disent qu'aucune robustesse d'une lentille ajustée à une autre n'est mesurée.

**La v2 ajoute nos propres lentilles.** Lazar a décidé, le 2026-11-19, que cette lecture avec nos lentilles entre dans le billet (GO-2026-11-19-33, mot « 1 2 et 3 », pièce 3 de `docs/notes/neuron-lens-v1/place-lentilles-billet-v1.md`, `a6e91e25…`). Il s'agit de :
- notre lentille R côté sortie, ajustée par nous sur Llama 3.1 8B Instruct ;
- et, si tu montres qu'elle a un sens pour une direction de sonde, notre lentille S côté entrée.

On compare la lecture par notre R à celle par la R publique. **Tout le reste de la v1 reste inchangé**, sauf ce que l'ajout exige. Chaque changement est listé en tête avec sa raison.

## Faits à prendre en compte (pièces à lire, autorisées)
1. **Nos lentilles n'existent pas aujourd'hui.** Elles ont été détruites avec la machine le 19 à 05:45Z. Elles seront réajustées, si Lazar confirme le devis, selon `docs/notes/neuron-lens-v1/devis-reajustement/devis-reajustement-lentilles-b-beta-v2.md` (`49dcbc93…`) et sa vérification `verification-difference-devis-reajustement-v1-v2.md` (`3cc64c86…`, réserve N-1 sur la tolérance du critère d'identité), puis rangées dans un dépôt privé chez la plateforme de modèles.
   - La v2 doit dire à quelle condition elles sont lues : critère d'identité du devis, § 4, paliers 1 à 3. Elle doit aussi dire d'où et comment elles sont téléchargées et vérifiées par empreinte.
   - Elle doit dire ce qui se passe si elles sont « différentes » ou absentes : la lecture par la lentille publique reste, et rien n'est remplacé en silence.
2. **Ce qu'on sait de nos lentilles** : texte gelé de la tranche `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` (`f5d46860…`), et verdict scellé et accepté `docs/notes/neuron-lens-v1/lecture-b-beta/verdict-b-beta-v1.md` (`3a9b947e…`, « partiel »).
   - Tu peux lire ce verdict, pour dire aux couches 7, 15 et 23 lues par la v1 si la stabilité et les autres mesures de nos lentilles tiennent, et pour en tirer des réserves.
   - Déclare dans le texte que tu l'as lu avant d'écrire.
   - Les fichiers de format et d'export de nos lentilles sont décrits dans `diag/20261118-164930-neuron-lens-b-beta/b-beta-export.json` et `b-beta-ajustement-R.json`. Tu peux en lire les noms de clés et la structure, pour les formats et les empreintes.
3. Le texte gelé de la tranche donne les formules de lecture de R et S (§ M.1, M.2). Le code voisin public `stdlogits/neuron-lens` au commit `849bfe16` est en copie de lecture dans `/tmp/claude-0/-home-user-controle-ia-travail/ff3e16f4-e2c5-5d31-b08c-99762b9cded7/scratchpad/voisin/` (vérifie par `git log -1`).
4. Calendrier : le billet n'accueille la section de l'étape B bis que si son verdict est scellé au plus tard le dimanche 22 novembre (règle de Lazar R-2716 (2)). Le réajustement demande ≈ 13 h de machine et ≈ 1 jour de préparation.

## Cloisonnement — ce que tu ne lis JAMAIS
- toute la liste « Jamais ouverts » de la v1 ;
- les sorties, scores, tables, lectures et verdicts de l'apprentissage des sondes sur la tâche (étape B bis), y compris son verdict : seule la présence de la clé `VERDICT-BBIS` dans `registres/t07-etape-b-bis-v1.md` t'est connue, inscrite le 2026-11-19 à 00:13:25Z ;
- toute table, lecture ou sortie de la lecture par la lentille publique (la v1 en cours de codage) ;
- les branches `donnees/*`, `calcul/*`, et les `diag/` ou `runs/` autres que les deux fichiers de la tranche nommés plus haut ;
- les sorties de P3, P3-bis, T0.6, T0.7, de l'étape B, du bras d'attaque et du saboteur à budget.

**Exposition à traiter dans le texte.** La v1 exigeait que son scellement précède `VERDICT-BBIS`. La v2 sera scellée après ; c'est le cas « texte exposé » de sa liste d'arrêt. La v2 doit :
- déclarer cette exposition et dire pourquoi elle ne biaise pas l'ajout : ni le rédacteur ni l'auteur de la v1 n'ont lu le verdict ;
- garder la règle « aucune table de la v1 ni de la v2 n'est ouverte par une personne avant le scellement de la v2 » ;
- et la présenter comme un nœud pour Lazar.

## Exigences de forme
- Gabarit `prereg/gabarit-preregistrement-v1.md` ; validateur `src/controle_ia/prereg.py` (essaie-le sur ton brouillon si sa commande le permet, et dis-le).
- Prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt, code neuf à écrire (le module `src/controle_ia/lentilles_sondes_bbis/` est en cours de développement pour la v1 : dis ce qui s'ajoute), rôles, coût (le réajustement relève du devis ; la lecture reste à 0 USD au processeur), nœuds.
- Aucun chiffre de la littérature sans pièce (R7). Graines par `SeedSequence`, clés neuves pour ce qui est neuf (R9).

## Où tu écris
- Brouillon dans `/tmp/claude-0/-home-user-controle-ia-travail/ff3e16f4-e2c5-5d31-b08c-99762b9cded7/scratchpad/redacteur-v2/`.
- Puis copie dans `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon1.md` sur la branche de travail, scellé comme brouillon : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon1.md`. Ce n'est pas le scellement du préenregistrement, que la mère fera après contre-lecture.
- Aucun commit, aucun push, aucune machine, aucune dépense, aucun modèle chargé.

## Rends-moi
Le chemin et l'empreinte ; la liste des changements par rapport à la v1, en une ligne chacun ; les nœuds ouverts pour Lazar ; les expositions déclarées ; et la confirmation que tu n'as rien ouvert d'interdit.
