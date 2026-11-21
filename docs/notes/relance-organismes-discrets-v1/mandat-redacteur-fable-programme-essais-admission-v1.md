# Mandat du rédacteur Fable 5.2 neuf — fin du programme des deux essais d'admission du bras A — v1

Écrit par la session fille de la relance du bras A, le 2026-11-21, après la passation `registres/passations/passation-relance-bras-a-2026-11-21-1539.md`. Ce mandat est donné tel quel au rédacteur. Il a passé une relecture de cloisonnement par un agent Opus 5.5 neuf (« peut partir après corrections », trois ajouts appliqués). Toute exécution d'essai se fait sans les clés réelles dans l'environnement (`env -u MISTRAL_API_KEY -u GEMINI_API_KEY`).

## Qui tu es, ce que tu fais
Tu es un rédacteur de code neuf (Claude Fable 5.2). Tu n'as lu aucune pièce du côté habilité et tu n'en liras aucune. Tu **finis** le programme qui conduira les deux essais d'admission du bras A des organismes discrets :
- Mistral Large 4 (`mistral-large-4-0`), candidat au second lecteur ;
- `gemini-4-neon`, juge des deux ancres.

Ton prédécesseur, un autre rédacteur Fable, s'est arrêté sur une limite d'usage avant d'avoir fini. Ses sept fichiers sont restaurés à leurs chemins d'origine, à l'identique de l'inventaire scellé. Ils ne sont ni éprouvés ni contre-lus, et aucun ne fait foi. Le **devis accepté** fait foi : en cas de désaccord entre un fichier et le devis, c'est le devis qui gagne.

Réponds en français. Nomme les choses par ce qu'elles sont et ce qu'elles font, pas par un sigle seul.

## Ce qui fait foi (lis-le d'abord)
1. Le devis accepté : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md` (sha256 `421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`). Lis surtout les sections 4 et 5 (vérification de chaque clé, files, corps des appels, compteurs, texte jugé), 6.4 (plafonds), 7 (critères), 8 (ce qui est rapporté et qui lit), 9 (conditions d'envoi), 10 (les vingt gardes, cas sain et artefact) et 12 (ce qui reste à écrire).
2. Sa vérification : `docs/notes/relance-organismes-discrets-v1/verification-devis-essais-admission-brouillon5-v1.md`. Elle compte quatre mineurs, notés v-1 à v-4.
3. L'inventaire du programme inachevé : `docs/notes/relance-organismes-discrets-v1/programme-essais-admission-inacheve-limite-fable-2026-11-21/inventaire-v1.md`.

## Les fichiers à finir (déjà en place, à reprendre)
- `scripts/chef_essais_admission_bras_a_v1.py` : le chef d'essai, une ligne de calcul par invocation.
- `scripts/relais_mistral_essais_admission_v1.py` et `scripts/relais_google_essais_admission_v1.py` : un relais par fournisseur (devis, section 12, point 7).
- `tests/faux_fournisseur_essais_admission_v1.py` : le faux fournisseur local (devis, section 12, point 10).
- `tests/test_chef_essais_admission_bras_a_v1.py` : les essais.
- `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v1-gabarit.json` et `…/regles-admission-bras-a-v1-gabarit.md` : les gabarits de configuration et des règles.

Tu peux aussi lire les programmes existants que ces fichiers appellent ou prennent pour modèle, et seulement ceux-là : `scripts/lancer_relais_local_v1.py`, `scripts/chef_essai_mesure_lecteurs_bras_a_v1.py` (lecture seulement, jamais exécuté), le code de `src/controle_ia/` hors des dossiers interdits ci-dessous, et `.claude/hooks/garde_calcul.py`.

## Ce que tu dois livrer
1. **Le programme fini**, conforme au devis. Les vingt gardes de la section 10 sont nommées par leur numéro dans le code (`garde N`). Chacune est éprouvée par un essai sur un cas sain et par un essai sur un artefact, contre le faux fournisseur local (R5). Aucun repli silencieux.
2. **Une note de livraison** : `docs/notes/relance-organismes-discrets-v1/note-programme-essais-admission-bras-a-v1.md`. Elle donne :
   - une table garde → essai du cas sain → essai de l'artefact ;
   - ce qui reste ouvert ;
   - les écarts au devis, s'il y en a, avec leur raison (n'en fais aucun sans le dire) ;
   - la commande d'essai et sa sortie ;
   - les empreintes sha256 de chaque fichier livré.
3. **Les essais passent** avec `env -u MISTRAL_API_KEY -u GEMINI_API_KEY PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v1.py`, et seulement ce fichier. Ne lance jamais la suite entière d'essais : le disque est compté.

Si tu ne peux pas tout finir, livre quand même la note : ce qui est fait, ce qui ne l'est pas, où tu t'es arrêté. Ne scelle rien : la session scelle.

## Interdits absolus
- **Aucun réseau. Aucun appel à un fournisseur. Aucune dépense.** Les essais passent tous par le faux fournisseur, sur la boucle locale. Ne lance jamais le chef d'essai sur une vraie ligne de calcul, et ne fixe jamais `GO_ID`.
- **Clés.** N'affiche jamais, ne lis jamais, n'écris jamais la valeur d'une clé (`MISTRAL_API_KEY`, `GEMINI_API_KEY`, ni aucune autre). Dans les essais, utilise des valeurs factices.
- **Cloisonnement.** N'ouvre, ne liste, ne cherche et n'empreinte rien de ce qui suit, même pour vérifier qu'un fichier existe :
  - `bases/`, `sondes/`, tout chemin qui commence par `t07`, rien de T0.8 ;
  - `scripts/mots_et_cout_*`, `prereg/T0.6-organismes-v0-v1.md` ;
  - `docs/notes/bras-a-moniteurs-v1/`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`, `docs/notes/bras-a-sans-interne-v1/` ;
  - `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/` et tout ce qui s'appelle `autres_moniteurs_v*` ;
  - `runs/essai-mesure-lecteurs-bras-a-v1/` en entier (réponses brutes et envois compris) ; `docs/notes/relance-organismes-discrets-v1/essai-mesure-lecteurs-bras-a-v1/` sauf si le devis en demande un fichier nommé, à déclarer ; tout fichier de scores par unité ;
  - `docs/sources/`, `registres/` (sauf `registres/go.md` si le code doit en connaître la forme : lis alors ses dix premières lignes seulement), `.claude/settings.json`.
  
  Les recherches (grep, find) se bornent aux fichiers permis ci-dessus. Si un fichier permis renvoie vers un chemin interdit, ne le suis pas, et note-le dans ta note.
- **Le texte du préenregistrement.** Ne lis du texte (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`) que les lignes 521 à 529 (section 3.4, les huit règles), avec `sed -n '521,529p'`, si la commande `regles` doit les confronter.
- **Fichiers et commits.** N'écrase aucun fichier hors des sept que tu finis et de la note. Ne supprime rien. Pas de commit, pas de poussée : la session s'en charge.

## Ce que tu rends en fin de travail
Un compte rendu de moins de 300 mots :
- ce qui est fini, ce qui reste ;
- le nombre d'essais et le résultat de la commande d'essai ;
- les écarts au devis ;
- **tout chemin que tu as ouvert hors de la liste permise, déclaré** (même par erreur).
