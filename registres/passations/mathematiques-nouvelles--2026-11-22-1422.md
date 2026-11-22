# Passation — session des mathématiques nouvelles — 2026-11-22-1422 (UTC, `date -u` : 2026-11-22T14:22:51Z)

Branche `claude/mathematiques-nouvelles-v1` (tête au moment d'écrire : `813114677f900f05f6237c394e5d09081a84c295`). Brief : `registres/passations/brief-lancement-mathematiques-nouvelles-v1.md` (`152df993…`).

## Fait

- **Prise de poste et routine** (compte rendu `registres/essaim/vers-mere/2026-11-22-1038-mathematiques-nouvelles.md`, `b4bdd4bd…`) : empreintes du lancement OK ; `verifier-arbre` : 39 problèmes antérieurs, hors chantier ; Hetzner 177170935 en tâche d'un autre chantier, non touché ; `vastai` absent du conteneur ; aucune machine créée.
- **Décisions reçues par la mère** (mots de Lazar, session de la mère) : lecture d'antériorité par étages (GO-2026-11-22-40, -42) ; Fable plafond souple 50 USD (GO-43), clé Luc (GO-45) ; conteneur de confiance = cette session, clés plantées tirées au moment réel, scellées et versées dans la même commande, jamais servies ni sur la machine jetable, clé d'interface jamais écrite ; score apparié : repli écrit sans attribution, code public cité en appui ; **GO-2026-11-22-70 : plus d'appel à Fable ni aux modèles Claude par l'interface, sessions filles de l'abonnement créées par la mère, sur mandat en fichier**.
- **Code du lot B1** (générateur de mondes plantés, six tests de mort), écrit par un Opus neuf, contre-lu puis vérifié cinq fois par un autre Opus : versions 1 à 6 sous `src/controle_ia/oracles_plantes_v1/` … `v6/` (v1 à v5 intactes). **Version 6** (`35ac9e10…`, 233 essais passés) : aucune remarque bloquante (`docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/verification-corrections-lot-b1-v5.md`, `045030e2…`) ; 42 racines d'essai plantent sans retirage ; **aire du classifieur de style 0,939 à 0,982, au-dessus du seuil d'emploi 0,75** (`versement-bloc-notes-2026-11-22-v1/v6-aires.json`, `32cd1781…`). Réserves écrites : héritage de mort limité aux reformulations de même préfixe ; tête du registre de lignée à consigner au manifeste de course (lot B3) ; remarques 24 et 25 à faire trancher par Fable.
- **Relevés sans dépense** : prix publics des quatre modèles (`docs/notes/mathematiques-nouvelles-v1/releves-prix-et-source-score-apparie-v1.md`) ; source du score apparié (PDF de Tango non obtenu légalement ; code R `contingencytables` versé) ; `lake comparator` présent dans les sources de Lean v4.35.0, version du Mathlib épinglé (`docs/notes/mathematiques-nouvelles-v1/verification-juge-standard-lean-v4.35.0-v1.md`), non exécuté.
- **Préenregistrement du pilote « oracles plantés »** : deux appels à Fable 5.2 par l'interface (avant GO-70), servi `claude-fable-5-2`, `end_turn`, 1,349760 + 1,430184 = **2,78 USD** (journal `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/journal-depense-fable-mathematiques-v1.jsonl`) : brouillon 2 (en différences), puis **brouillon 3 complet** et devis v3 (`prereg/mathematiques-nouvelles-v1/`). Devis v2 et v3 rejoués par script (`calculs-v2/`, `calculs-v3/`). **Contre-lecture R2 du brouillon 3** par un Opus neuf : 6 bloquantes, 13 à corriger, 8 mineures (`prereg/mathematiques-nouvelles-v1/contre-lecture-brouillon-3-v1.md`, `65152d7f…`).
- **Mandat de la session Fable pour le brouillon 4 et le devis v4** : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/mandat-fable-brouillon-4-v1.md` (`d57c9906…`), envoyé à la mère.
- **Versement du bloc-notes** (sondes, balayages, rejeux d'essai) : `docs/notes/mathematiques-nouvelles-v1/versement-bloc-notes-2026-11-22-v1/`, scellé fichier par fichier.

## Reste

1. Brouillon 4 et devis v4 par la session Fable (mandat ci-dessus), puis vérification des corrections par le même contre-lecteur R2 (relancer un Opus avec `contre-lecture-brouillon-3-v1.md` et le brouillon 4), relecture par Fable, scellement. Si Fable demande une version 7 du code : par un Opus, vérifiée par un autre.
2. Lot B3 (harnais d'appels : gardes A2 à A13, tête du registre au manifeste, consignes des rôles, script d'analyse).
3. Protocole d'antériorité sur la méthode (exécutant et devis à nommer par Lazar).
4. Cartes de cible par Fable (lemme d'impossibilité en version finie, sonde qui ne lit que l'indication, étalonnage du score apparié ; puis l'agrégateur), dont le témoin d'abandon par cible.
5. Suite complète des essais du dépôt : coupée à 50 minutes ; à rejouer par morceaux.

## Nœuds en attente de Lazar (portés par la mère)

- Seuil 0,75 de l'aire du classifieur de style, dépassé partout en v6 : reco (a) garder, H3 lue sur les seuls contre-exemples vérifiés, une version 7 au dossier du pilote 2 ; défaut sous 48 h (a).
- Règle de retirage d'une racine non plantable (sélection avant tout appel) : reco oui, nombre rapporté ; défaut sous 48 h.
- Version 5 plutôt que garder la version 4 (suivi de la recommandation de Fable, défaut appliqué de fait).
- Plafond (300 USD proposé), échéance, exécutant du protocole d'antériorité.

## Réserves

- Copies sans nom servies à Fable (prénom du directeur remplacé), écart déclaré au brief (`copies-sans-nom-v1/LISEZMOI-v1.md`).
- Heures écrites dans trois messages à la mère (13:58Z, 14:20Z, 14:45Z) estimées, non relevées par `date -u` dans la commande (écart à la règle des registres) ; heures réelles plus tôt d'environ 20 minutes pour la dernière.
- Une seconde session lancée par erreur par la mère a poussé sur ma branche (fusion de `main` et un message) ; fusionné sans réécriture (`ed585765`).
- Les essais complets du dépôt n'ont pas fini (coupés à 50 minutes) : aucun compte global.

## Prochaine action

Attendre le commit de la session Fable (brouillon 4) annoncé par la mère, puis lancer la vérification des corrections par un Opus contre-lecteur.

## Instances actives

Aucune créée par cette session. Vu en lecture : Hetzner 177170935 (`essai-3-palier-0b`, autre chantier).
