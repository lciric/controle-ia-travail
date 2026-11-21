# Mandat du rédacteur Fable 5.2 neuf — brouillon 44 du préenregistrement du bras A — v1

Écrit par la session fille de la relance du bras A, le 2026-11-21. Ce mandat est donné tel quel au rédacteur, après une relecture de cloisonnement par un agent Opus 5.5 neuf (« peut partir après corrections », quatre corrections appliquées).

## Ce que tu fais
Tu es un rédacteur neuf (Claude Fable 5.2). Tu n'as lu aucune pièce du côté habilité. Tu écris le **brouillon 44** du préenregistrement du bras A des organismes discrets. Tu pars du brouillon 43, en le changeant le moins possible.

Réponds en français. Nomme les choses par ce qu'elles sont et ce qu'elles font, pas par un sigle seul.

## Pièces à lire
1. `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md` (4f91b535…), en entier : c'est ta base.
2. Sa note, `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon43-note-v1.md`, et sa vérification, `docs/notes/relance-organismes-discrets-v1/verification-brouillon43-bras-a-v1.md`, qui donne deux mineurs pour le prochain brouillon.
3. L'avenant 1 au devis des essais d'admission, version 3, **accepté** : `docs/notes/relance-organismes-discrets-v1/avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md`, et sa vérification `verification-avenant-1-v3-devis-essais-admission-v1.md`.
4. Le devis accepté `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md` (421ee2e6…), sections 7 et 9 seulement.
5. La ligne GO-2026-11-21-68 du registre, et elle seule : `git show origin/main:registres/go.md | grep GO-2026-11-21-68`. Pas de `git fetch` : la session l'a déjà fait.

## Ce que le brouillon 44 change, et rien d'autre
1. **Conditions d'envoi (section 3.4 et case « lecteurs et juge des ancres » de 13.1).** Lazar a abandonné le constat ligne par ligne aux consoles (GO-2026-11-21-68). Écris :
   - ce qui reste constaté : la confidentialité de l'API Mistral, constatée le 21 novembre à 15:25, heure de Paris, pièce 4ff7e8d6… ; deux captures de facturation Google, décrites dans l'avenant ;
   - ce qui est levé, clé par clé, comme dans la pièce de constat de l'avenant ;
   - la réserve qui en découle (contamination possible si un projet n'était pas à l'offre payante, ou si le partage des journaux était actif).
   
   Tu ne changes pas le mot « b a b go » (GO-2026-11-21-33) : tu inscris sa levée partielle par GO-2026-11-21-68.
2. **Le juge des deux ancres sur deux clés.** Le critère « huit lectures sur huit » s'applique à une file coupée entre deux clés Google, avec le partage par rang de l'avenant. Écris exactement ce qui reste jugé et ce qui ne l'est plus, comme l'avenant le déclare. Ne change pas le critère lui-même. Si le texte ne peut pas le porter sans changer une règle, arrête-toi et dis-le.
3. **Les deux mineurs** de la vérification du brouillon 43.
4. **La table d'en-tête des pièces** : n'ajoute ou ne recalcule que les lignes des pièces de la relance (`docs/notes/relance-organismes-discrets-v1/` hors de son sous-dossier `essai-mesure-lecteurs-bras-a-v1/`, et le préenregistrement). Ne relance aucun script de contrôle d'un brouillon précédent. Corrige la phrase d'en-tête sur les empreintes recalculées pour qu'elle dise ce périmètre. Ne recalcule jamais une ligne cloisonnée, ni `docs/sources/`, ni une configuration de T0.6 : recopie-les telles qu'au brouillon 43.

Les huit règles de la section 3.4, lignes 521 à 529 du brouillon 43, restent **inchangées caractère pour caractère**, sauf si Lazar l'a dit. Si leur numéro de ligne bouge, dis-le dans ta note : le fichier des règles cite ces lignes.

## Ce que tu livres
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon44.md`.
- `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon44-note-v1.md`, qui donne :
  - chaque changement, avec ses lignes avant et après ;
  - les nouveaux numéros de ligne des huit règles ;
  - un diff contrôlé par programme contre le brouillon 43, qui montre qu'aucune autre ligne n'a bougé ;
  - ce que tu as ouvert.

## Interdits absolus
- Aucun réseau, aucun appel, aucune clé lue ni affichée. Pas de `git fetch`.
- **Cloisonnement.** N'ouvre, ne liste, ne cherche et n'empreinte rien de ce qui suit, même pour vérifier qu'un fichier existe :
  - `bases/`, `sondes/`, tout chemin dont un élément commence par `t07`, rien de T0.8 ;
  - `scripts/mots_et_cout_*`, `prereg/T0.6-organismes-v0-v1.md` ;
  - `docs/notes/bras-a-moniteurs-v1/`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`, `docs/notes/bras-a-sans-interne-v1/` ;
  - `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/` et tout ce qui s'appelle `autres_moniteurs_v*` ;
  - `runs/essai-mesure-lecteurs-bras-a-v1/` en entier, et `docs/notes/relance-organismes-discrets-v1/essai-mesure-lecteurs-bras-a-v1/` ;
  - tout fichier de scores par unité ; rien sous `runs/` ; des rapports techniques, aucun champ autre que les compteurs ;
  - `docs/sources/`, `registres/` (sauf la ligne de GO dite plus haut), `.claude/settings.json`.

  Le brouillon 43 cite des chemins cloisonnés dans sa table d'en-tête : tu les recopies, tu ne les suis pas.
- **Registre.** Ne recopie rien de ce que les mots de Lazar décident pour « l'intervalle impossible » ou pour « le moniteur appris non ajustable », au-delà de ce que le brouillon 43 en porte déjà. Ne nomme aucune ligne de GO du 19 novembre que le brouillon 43 ne nomme pas déjà, et n'ajoute aucune mention de celles qu'il nomme.
- N'écrase rien. Ne scelle rien, ne committe rien.

## Compte rendu
Moins de 200 mots :
- ce qui change ;
- les nouvelles lignes des huit règles ;
- ce que tu n'as pas pu faire ;
- tout chemin ouvert hors de la liste, déclaré.
