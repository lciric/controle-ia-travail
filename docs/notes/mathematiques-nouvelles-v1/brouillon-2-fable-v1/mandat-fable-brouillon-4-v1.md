# Mandat pour une session Fable 5.2 (effort maximal) — brouillon 4 du préenregistrement du pilote « oracles plantés » et devis v4 — v1

- Nature : mandat (classe C) pour une pièce décisive (classe A : préenregistrement et devis, liste « Économie de Fable » de `CLAUDE.md`). Émis par la session des mathématiques nouvelles le 2026-11-22 ; servi par une session fille éphémère de l'abonnement créée par la mère (GO-2026-11-22-70), pas par l'interface de programmation.
- Dépôt `lciric/controle-ia-travail`, branche `claude/mathematiques-nouvelles-v1` (lire à la tête de la branche ; ne rien récupérer d'autre). La session Fable écrit sur la branche `claude/mathematiques-nouvelles-fable-b4-v1` (ou celle que la mère nomme) et ne pousse nulle part ailleurs.

## Rôle

Tu es le concepteur des pièces décisives du pilote. Tu as écrit les brouillons 2 et 3 (par l'interface, dans un contexte que tu n'as plus) ; un Opus 5.5 neuf a contre-lu le brouillon 3 (6 remarques bloquantes, 13 à corriger, 8 mineures). Tu écris le **brouillon 4 complet et autonome** et le **devis v4**, en traitant chaque remarque.

## À lire, dans cet ordre (et rien d'autre sans besoin précis)

1. `CLAUDE.md` (règles R1 à R14, « Qui conçoit », interdits, ce qu'on ne dira pas).
2. `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-3.md` et `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v3-brouillon.md` (tes textes ; provenance `LISEZMOI-brouillon-3-et-devis-v3-v1.md`).
3. `prereg/mathematiques-nouvelles-v1/contre-lecture-brouillon-3-v1.md` (`65152d7f…`) — la contre-lecture à traiter.
4. `prereg/mathematiques-nouvelles-v1/calculs-v3/ecarts-devis-v3-main-contre-script-v1.md` et la sortie du script v3 (même dossier).
5. Code : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/note-choix-implementation-lot-b1-v6.md` (§ 10, § 11, ligne 60), `rapport-essais-r5-lot-b1-v6.md`, `verification-corrections-lot-b1-v5.md` (remarques 24 et 25) ; aires de la version 6 : `docs/notes/mathematiques-nouvelles-v1/versement-bloc-notes-2026-11-22-v1/v6-aires.json` (`32cd1781…`) ; code `src/controle_ia/oracles_plantes_v6/` (commit `35ac9e10738ccaac486ec9b9684fe70441f6371a`).
6. Tes notes précédentes : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/notes-au-directeur-fable-v1.md` et `-v2.md`.
7. Le gabarit `prereg/gabarit-preregistrement-v1.md` et le validateur `src/controle_ia/prereg.py` (passe-le sur ton brouillon 4 et rapporte sa sortie).

**Interdits de lecture** : tout fichier dont le nom contient « consigne-privee », « conception-ii-b », « verite », « rendu », « scores » ; rien sous `matiere-premiere/`, `quarantaine/`, `archives-reponses-modeles/`, `brouillons/ii-b-saboteur-budget-v1/`, `docs/notes/bras-attaque/` ; aucune autre branche. Aucun appel à un fournisseur de modèles, aucune dépense.

## Ce que tu tranches

- Les **six remarques bloquantes** de la contre-lecture (lecture de H3 au-dessus du seuil d'aire ; table de lecture de H3 ; seuil 0,75 décidé après la mesure ; recouvrement des verdicts de H1 et sa base aléatoire ; graine racine tirée dans la commande de scellement et non comme blanc ; faux « connu » de H4 sur des instances de théorèmes connus), puis les treize « à corriger » et les huit mineures : pour chacune, acceptée (texte) ou refusée (raison).
- **Le seuil 0,75** : la mesure (aires de 0,939 à 0,982 sur 42 racines d'essai) est connue avant ta décision ; la décision du directeur est en attente, avec pour défaut sous 48 heures « garder 0,75 et lire H3 sur les seuls contre-exemples vérifiés, une version 7 mise au dossier du pilote 2 ». Écris le texte selon ce défaut, en disant que cette branche est attendue et que le seuil a été gardé après lecture de la mesure ; si le mot du directeur te parvient autrement par la mère, suis-le.
- **Les deux choix du code à approuver** : T5 non appliqué aux pièges à la plantation (note v6, ligne 60 ; vérification, remarque 25) ; journal des refus de la règle de retirage absent du manifeste quand les trois racines échouent (remarque 24 : version 7 du code ou exigence au lot B3).
- **COMMIT-CODE** : remplis-le avec la version 6 (`35ac9e10…`) si tu approuves ses choix et ne demandes aucun changement de code ; sinon, liste exacte des changements (une version 7 sera écrite et vérifiée, et le blanc reste).

## Ce que tu rends

Dans le dossier `prereg/mathematiques-nouvelles-v1/` de ta branche :
1. `preenregistrement-pilote-generation-v1-brouillon-4.md` — complet, autonome, avec une section finale « Traitement de la contre-lecture du brouillon 3 » (une ligne par remarque) et « Écarts au brouillon 3 ».
2. `devis-pilote-generation-v4-brouillon.md` — chaque chiffre retrouvable dans une sortie de script versée ou nommé « supposé » avec sa formule.
3. `notes-au-directeur-fable-b4-v1.md` — décisions qui changent une prédiction, un seuil ou le code ; nœuds qui reviennent au directeur.
Scelle les trois (`PYTHONPATH=src python -m controle_ia.scellement sceller FICHIER…`), commite, pousse sur ta branche, et dis à la mère le commit et les empreintes. Relève le modèle qui t'a servi.
