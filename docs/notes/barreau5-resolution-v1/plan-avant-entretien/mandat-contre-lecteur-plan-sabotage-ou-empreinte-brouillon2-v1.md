# Mandat du contre-lecteur Opus 5.5 du plan « sabotage ou empreinte de l'adaptateur » (brouillon 2) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 15:30Z. Pièce de travail : elle dit quoi lire et quoi rendre, sans rien concevoir.

---

Tu es un contre-lecteur neuf (Claude Opus 5.5) du programme de contrôle boîte blanche, dépôt `/home/user/controle-ia-travail`. Tu n'as écrit aucune des pièces que tu lis (R2). Tu contre-lis une pièce de conception décisive (classe A) écrite par Claude Fable 5.2. Français, mots en clair, identifiants en appui seulement. Aucune dépense, aucun lancement sur carte, aucun commit.

## Objet
Le brouillon 2 du préenregistrement qui doit répondre, avant l'entretien du 1er décembre 2026, à la question du barreau 5 : « la sonde lit-elle le sabotage, ou l'empreinte de cet adaptateur-ci ? ». Contre-lis aussi son devis, la fiche de décisions pour Lazar, et les simulations et calculs qui les portent. Mot de Lazar (`registres/go.md`, ligne `GO-2026-11-19-62`) : il veut cette réponse avant l'entretien. Le plan doit rendre l'issue « sabotage » dicible si elle est vraie, sans la promettre (R3 : aucune course ne vise un signe positif).

## Pièces à contre-lire
Vérifie d'abord chaque empreinte : `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -B -m controle_ia.scellement verifier <fichier>`.
- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon2.md` (8e7c28e1…)
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon2.md` (47e16e26…)
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-decisions-lazar-v2.md` (5fdf87d7…)
- Dans le même dossier : `simulation-puissance-adaptateurs-tenus-a-l-ecart-v3.py` et sa sortie `sortie-simulation-puissance-adaptateurs-tenus-a-l-ecart-v3.json` ; `calcul-devis-adaptateurs-tenus-a-l-ecart-v2.py` et sa sortie `sortie-calcul-devis-adaptateurs-tenus-a-l-ecart-v2.txt`.

## Ce que le rédacteur a reçu et rendu (même dossier)
- Son mandat : `mandat-redacteur-plan-sabotage-ou-empreinte-v1.md` (370787d4…), et les précisions de la mère : `precisions-mere-reprise-redacteur-plan-v1.md`.
- Son rendu, avec ses réserves et la liste de ce qu'il a ouvert : `rendu-redacteur-plan-brouillon2-v1.md`.
- Le brouillon 1 inachevé dont il est parti : dossier `etat-a-l-arret-quota-fable-20261119-1440Z/`.

## À lire pour juger
- **Ce que le rédacteur n'a pas lu et demande de vérifier (marqueur M-8)** :
  - les notes 01, 04, 05 et 06 de `docs/notes/barreau5-resolution-v1/comprendre/`, et les notes 02 et 03, qu'il n'a lues qu'en partie ;
  - dans `docs/notes/barreau5-resolution-v1/concevoir/` : `conception-B-identification-v1.md`, `conception-C-externe-v1.md`, `contre-lecture-note-resolution-barreau5-v1.md` ;
  - les décisions `docs/decisions/decision-N-026-v1.md`, `decision-N-053-v1.md`, `decision-N-056-v1.md` et `decision-N-062-v1.md`.
- **La base** : la note de résolution v2 (`concevoir/note-resolution-barreau5-v2.md`) et le socle (`comprendre/00-socle-des-faits.md`).
- **Les textes scellés** `prereg/validite-adaptateur-v1.md` et `prereg/T0.7-etape-B-bis-v1.md`, et le gabarit `prereg/gabarit-preregistrement-v1.md`.
- **Le code cité (marqueur M-5, non revérifié par le rédacteur)** : `src/controle_ia/t06/lanceur.py`, `src/controle_ia/t06/identite.py`, `src/controle_ia/sondes/familles.py`, `src/controle_ia/t07bbis/etat_impose_v1.py`, et tout autre module que le texte cite.
- **Dans `registres/go.md`**, les lignes `GO-2026-11-19-62` et `GO-2026-11-19-68`.

## Ce que tu juges, au moins
1. **Le mandat**, contrainte par contrainte : calendrier, coût, garde des activations et des textes, invariants, cloisonnement, épreuve à vérité plantée, niveau.
2. **Les trois issues** (« sabotage », « empreinte de l'adaptateur », « non établi à cette puissance ») et l'issue neuve « différence établie, non attribuée ».
   - Sont-elles écrites d'avance avec la même rigueur, chacune avec sa phrase pour le jury ?
   - Une phrase affirme-t-elle plus que ce que l'épreuve permet ?
3. **Les quatre changements de fond déclarés par le rédacteur**, à attaquer un par un : (a) l'épreuve exacte des rangs signés ; (b) le sur-saboteur ; (c) les trois épreuves exigées pour dire « sabotage » ; (d) dix familles tenues à l'écart. Dis s'ils tiennent, et ce qu'ils cassent ailleurs.
4. **Le niveau et la puissance**, refaits par toi.
   - Écris ta propre simulation, avec tes lois inventées, en particulier des membres non échangeables et un bruit asymétrique.
   - Ne recopie pas celle du rédacteur.
   - Vérifie les taux d'erreur annoncés, la tenue du 99 % bilatéral, et le nœud du 95 % sous huit familles.
5. **Le devis**, refait : nombre de cartes, heures, attendu, pire cas, coupure, recharge demandée, volume des activations gardées.
6. **Le calendrier** : le chemin critique, ce qui se coupe d'abord sans perdre l'identification, et le risque principal (le code en trois jours).
7. **Le cloisonnement et l'exposition** : qui forme, qui lit, qui ouvre ; les lignes d'exposition déclarées. Pour le marqueur M-6 (idée du jumeau à coût édité, venue d'une note sur le saboteur à budget) :
   - retrouve la note par le brouillon 1 ;
   - si son nom tombe sous un interdit ci-dessous, ne l'ouvre pas et dis qu'une session habilitée doit faire le rapprochement ;
   - sinon, ouvre-la et fais-le.
8. **Les invariants**, chacun avec le passage du texte qui le tient :
   - aucun score de sonde dans l'entraînement, le choix, l'arrêt ou l'exclusion d'un adaptateur ;
   - contrôle de manipulation par l'oracle du coût seul ;
   - jamais de moyenne ni de médiane sur les jetons dans une sonde de production ;
   - graines selon R9.
9. **R7 et R8** : aucun chiffre de l'état de l'art sans page de PDF vérifiée ; aucune zone déclarée libre.
10. **La fiche** : une page, les seuls choix qui reviennent à Lazar, chaque option honnête, une recommandation et une confiance.

## Forme de ta contre-lecture
- Verdict en tête, l'un des trois : « scellable tel quel », « scellable après ces corrections exactes », « à reprendre ».
- Chaque constat est classé bloquant, majeur ou mineur. Chaque correction est donnée, autant que possible, comme un couple exact « avant → après », dont tu vérifies que le texte « avant » est unique dans le fichier. Sinon, donne une consigne précise au rédacteur.
- Tes outils (simulation, arithmétique) et leurs sorties, sous des noms neufs.

## Sorties (scellées par `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -B -m controle_ia.scellement sceller <fichier>`, non commises)
1. `docs/notes/barreau5-resolution-v1/plan-avant-entretien/contre-lecture-plan-sabotage-ou-empreinte-brouillon2-v1.md`
2. tes outils et leurs sorties dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/contre-lecture-outils-plan-brouillon2-v1/`.

## Interdits
- **N'ouvre jamais :**
  - un fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ;
  - `brouillons/ii-b-saboteur-budget-v1/`, la branche `lot/compte-4-v1`, la ligne R-2059 ;
  - les notes « pour Lazar seul » ;
  - le fichier des scores par unité du bras A ;
  - les valeurs des deux booléens d'aiguillage du texte scellé de validité, où qu'elles soient écrites. Les règles qui les définissent dans `prereg/validite-adaptateur-v1.md` se lisent ;
  - rien sous `/root/.claude/`.
- **Recherches :** pas de recherche plein texte sur tout le dépôt. Limite-toi aux dossiers nommés ici, en excluant les motifs interdits, par exemple `grep -r --exclude='*consigne-privee*' --exclude='*conception-ii-b*' --exclude-dir='ii-b-saboteur-budget-v1' …`. Si une recherche fait apparaître un fichier interdit, ne l'ouvre pas et signale-le.
- **Exécution :** ne lance pas la suite complète des essais. Aucune commande `rm` sur un chemin construit par variable.
- **Refus d'outil :** au premier refus, arrête-toi et dis-le, sans le contourner.
- **Écriture :** écris sur disque tôt et souvent.

## Rends
1. La phrase exacte de ton invite système qui nomme le modèle qui te sert.
2. Les chemins et empreintes de tes sorties.
3. Dix lignes au plus : verdict ; nombre de constats par classe ; les trois plus graves ; ce que ta simulation confirme ou dément ; ce qui menace le calendrier.
4. La liste des fichiers et des dossiers que tu as ouverts, une ligne chacun (registre de « qui a lu quoi »).
