# Mandat pour une session Fable 5.2 (effort maximal) — brouillon 5 du préenregistrement du pilote « oracles plantés » et devis v5 — v1

- Nature : mandat (classe C) pour une pièce décisive (classe A). Émis par la session des mathématiques nouvelles le 2026-11-22 ; servi par une session fille de l'abonnement créée par la mère (GO-2026-11-22-70).
- Dépôt `lciric/controle-ia-travail`, lire à la tête de la branche `claude/mathematiques-nouvelles-v1` (commit `71b3ce951f3b83a5437757e4e9825a6d3afc6276` ou plus récent) ; écrire sur la branche `claude/mathematiques-nouvelles-fable-b5-v1` (ou celle que la mère nomme), nulle part ailleurs.

## Rôle

Tu es le concepteur. Tu as écrit le brouillon 4 (`prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-4-v2.md`), le devis v4 et tes notes (`notes-au-directeur-fable-b4-v2.md`). Deux vérifications sont rendues. Tu écris le **brouillon 5 complet et autonome** et le **devis v5**.

## À lire (et rien d'autre sans besoin précis)

1. `CLAUDE.md`.
2. Tes pièces du brouillon 4 (ci-dessus), le devis v4 `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v4-brouillon.md`, tes notes b4.
3. `prereg/mathematiques-nouvelles-v1/verification-corrections-brouillon-4-v1.md` (`69b8aa58…`) — vérification de tes corrections par le contre-lecteur du brouillon 3 : 22 tiennent, 5 avec réserve ; remarques neuves 28 à 38.
4. `prereg/mathematiques-nouvelles-v1/calculs-v4/verification-sonde-et-devis-v4-v1.md` (`bd3b37e9…`) — vérification de ta sonde et de ton script du devis v4 : aucun écart bloquant ; deux moyens, quatre mineurs.
5. `registres/go.md` de `main` n'est pas sur la branche : les mots du directeur te sont cités ci-dessous, verbatim de la ligne GO-2026-11-22-77.

**Interdits de lecture** : comme au mandat du brouillon 4 (fichiers « consigne-privee », « conception-ii-b », « verite », « rendu », « scores » ; `matiere-premiere/`, `quarantaine/`, `archives-reponses-modeles/`, `brouillons/ii-b-saboteur-budget-v1/`, `docs/notes/bras-attaque/` ; aucune autre branche). Aucun appel à un fournisseur, aucune dépense.

## Ce que tu tranches et portes

1. **Remarque 28 (bloquante, H2)** : le témoin « un modèle, vote à k, coût apparié » est une chaîne de 24 appels d'Opus qui se voient ; la configuration à deux familles, deux chaînes de 12 qui ne se voient pas ; la redite et l'union des retrouvées se comptent sur la configuration entière, d'où un dessin confondu avec la composition. Le contre-lecteur propose un témoin en deux chaînes d'Opus de 12, indépendantes, sans changement d'appels ni de devis. Tranche et récris H2, H1 (précision) et les critères touchés.
2. **Remarques 29 à 31 (à corriger)** : prix unique d'Argon (« tous les appels d'Argon avant le 1er décembre ou tous après », verdict de H2 lu au prix payé) ; sortie du bras S (le relecteur ne peut que choisir parmi les instances de l'agent, le code retire les autres) ; périmètre de H3 (tranché par le directeur, ci-dessous).
3. **Remarques 32 à 38 (mineures)** et les **réserves** sur les corrections 1, 3, 5, 7, 17 : traite chacune.
4. **Vérification de la sonde** : les deux écarts moyens (le plancher de la règle aveugle mêle trois mécanismes : seuil monotone dépassé, énoncés clos ou à variables bornées, faux presque partout ; le plancher des pièges est un fait de construction, plantation dans ]N, 3N] et plafond servi 3N, à dire, avec ce que tout changement du plafond ou de la plage fait à P11) et les quatre mineurs.
5. **Mots du directeur, à porter dans le texte** (GO-2026-11-22-77, « go maths » sur tes quatre recommandations du brouillon 4) :
   - périmètre de H3 : option (a), les bras S et N courus comme écrit ;
   - plafond : 300 USD d'appels et 65 USD de machine, garde de projection à 293,50 ;
   - échéance : le 13 décembre 2026, 23:59 UTC, ou sept jours après l'appel de fumée si cette date tombe plus tôt ;
   - antériorité : `gpt-6.2-astra` par l'interface, `kimi-k3.1-pro` en second lecteur sur les pièces douteuses, **plafond 40 USD** (ton devis donnait 10,72 / 25,10 / 94,80 : écris la garde qui coupe à 40 et ce qu'une coupure laisse non lu).
6. **Seuil 0,75** : « go maths » ne vise pas explicitement le seuil ; la mère pose la question au directeur. Écris le seuil selon le défaut (gardé après lecture de la mesure, branche haute attendue) et **laisse le blanc « À REMPLIR : DÉCISION-SEUIL » ouvert**, marqué, dans une section que le validateur lit.

Code : version 6 inchangée sauf si la remarque 28 ou 30 exige du code (alors : liste exacte des changements ; ils iront au lot B3 ou à une version 7, dis lequel).

## Ce que tu rends

Dans `prereg/mathematiques-nouvelles-v1/` de ta branche : `preenregistrement-pilote-generation-v1-brouillon-5.md` (complet, avec « Traitement des vérifications du brouillon 4 », une ligne par remarque, et « Écarts au brouillon 4 ») ; `devis-pilote-generation-v5-brouillon.md` (chiffres tracés vers un script versé ; si tu modifies le script, version neuve `calculs-v5/`) ; `notes-au-directeur-fable-b5-v1.md`. Passe `src/controle_ia/prereg.py` et rapporte sa sortie. Scelle, commite, pousse sur ta branche ; dis à la mère le commit, les empreintes et le modèle servi.
