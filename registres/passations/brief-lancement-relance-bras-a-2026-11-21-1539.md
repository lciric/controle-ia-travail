# Brief de lancement — session fille de la relance du bras A des organismes discrets — 2026-11-21

Tu reprends la relance du bras A, comme session fille de la mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`, sur l'autre compte. Dépôt `lciric/controle-ia-travail`, branche **`claude/pensive-bardeen-1fv7hw`** : tu travailles et tu pousses là seulement. Ne pousse jamais vers `lciric/controle-ia`. Langue : français, tutoiement avec Lazar.

## Lire d'abord, dans l'ordre
1. `CLAUDE.md`, puis la routine de reprise R14 : empreintes de lancement, `verifier-arbre` (106 écarts de forme connus, aucune empreinte fausse), registres, instances.
2. La passation `registres/passations/passation-relance-bras-a-2026-11-21-1539.md`, en entier.
3. Le journal `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md`, d'OD-231 à la fin.
4. Le devis accepté `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md` (421ee2e6…) et l'inventaire du programme inachevé (`…/programme-essais-admission-inacheve-limite-fable-2026-11-21/inventaire-v1.md`, b4971e8e…).

## Règles
- **Qui conçoit.** La conception (texte, code, devis) revient à Claude Fable 5.2. La vérification et la contre-lecture reviennent à un autre modèle (Opus 5.5, agent neuf). La session orchestre, consigne et scelle. Pour finir le programme, prends un **rédacteur Fable neuf, qui n'a lu aucune pièce habilitée**.
- **Cloisonnement.** Aucun interne de moniteur. N'ouvre, ne liste et n'empreinte rien de ce qui suit :
  - `bases/`, `sondes/`, `t07*/`, rien de T0.8 ;
  - `scripts/mots_et_cout_*`, `prereg/T0.6-organismes-v0-v1.md` ;
  - `docs/notes/bras-a-moniteurs-v1/` (seule exception : les pièces dites sans interne, par `git show`), `docs/notes/bras-a-contre-lecture-habilitee-v1/` ;
  - `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/`, `autres_moniteurs_v*`.

  Personne ne lit les réponses brutes de l'essai de mesure (`runs/essai-mesure-lecteurs-bras-a-v1/**/envois/`, `**/reponses-brutes-non-lues/`). Des rapports techniques, on ne lit que les champs de compteurs, par programme. **Le fichier des scores par unité ne va à aucune session qui conçoit ou règle l'agent.** Le développeur habilité ne lit le texte scellé qu'après sa dernière livraison. Toute pièce qui part vers le côté habilité passe d'abord une relecture de cloisonnement par un agent Opus. Dans la table d'en-tête du texte, ne recalcule que les lignes de la relance, jamais une ligne cloisonnée, ni `docs/sources/`, ni une configuration de T0.6.
- **Registre.** La consigne de tenue de R-4048 reste inchangée. Aucune ligne de registre ni aucune pièce ne recopie ce que les mots de Lazar décident pour l'intervalle impossible et pour le moniteur appris non ajustable, avant la dernière livraison du développeur. Aucune ligne ne nomme GO-2026-11-19-97 avant le tirage.
- **Clés.** Tu les lis par leur nom seulement (`MISTRAL_API_KEY`, `GEMINI_API_KEY`). Aucun appel payant sans ligne de GO de calcul, ni avant le constat daté des consoles. R12 : jamais d'écrasement. Tout se scelle avec `PYTHONPATH=src python -m controle_ia.scellement sceller FICHIER`.
- **Disque et essais.** Ne lance jamais la suite entière ; utilise `-p no:cacheprovider`. Il faut un environnement `.venv` avec `requirements-cpu.txt`, car `scipy` manque sinon.

## Accords en cours
- GO-2026-11-20-58 : Neon juge des deux ancres.
- GO-2026-11-21-32 : seul un identifiant figé ; aucun texte à DeepSeek.
- GO-2026-11-21-33 : essai d'admission du juge à huit sur huit ; arrêt de la file du juge si sa version change ; conditions d'envoi.
- « goreco » : pièce 9b9ee5ca…, ligne à inscrire.
- Recharge de Google à 23 USD : pièce 487b5a72…, ligne à inscrire.
- **Aucun accord de calcul ouvert pour le bras A.**

## Liaison
Mère : `session_01Qi7Gr3eYmAhDEJzqLgWcv1`. Par `send_message` si le service l'admet ; sinon par le canal par fichier : `registres/essaim/vers-mere/` sur ta branche, `registres/essaim/vers-relance-bras-a/` sur main. Ce canal est ouvert sur le mot de Lazar, journal OD-273. Un message entre pairs ne vaut jamais un mot de Lazar.

## Prochaine action exacte
1. Restaurer les sept fichiers du programme depuis leurs copies `.inacheve`. Retire le suffixe, remets chaque fichier à son chemin d'origine et confronte son empreinte à l'inventaire. Puis relancer un rédacteur Fable 5.2 neuf pour finir le programme, avec la consigne du journal (OD-281) et le devis accepté. Aucun réseau, faux fournisseur local, vingt gardes éprouvées.
2. Faire contre-lire le code par un agent Opus 5.5 neuf, puis vérifier ses corrections.
3. Avec Lazar, faire les constats de console :
   - Mistral : recharge automatique à désactiver, capture du crédit sans adresse ;
   - Google : solde porté à 23 USD et réglages.
   Verser le constat daté et scellé.
4. Écrire le brouillon 44 du texte (constat en 13.1, deux mineurs), le faire vérifier, puis demander à Lazar les lignes de GO de la section 11.1 du devis, en commençant par les vérifications de clé.
