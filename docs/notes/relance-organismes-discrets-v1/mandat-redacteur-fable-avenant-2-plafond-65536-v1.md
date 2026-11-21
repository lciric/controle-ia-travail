# Mandat d'un rédacteur Fable 5.2 neuf — avenant 2 au devis des essais d'admission : plafond de sortie de Google à 65 536 — v1

Écrit par la session fille de la relance du bras A, le 2026-11-21. Ce mandat est donné tel quel ; il a passé une relecture de cloisonnement par un agent Opus 5.5 neuf (« peut partir après corrections », corrections appliquées).

## Ce que tu fais
Tu es un rédacteur neuf (Claude Fable 5.2), qui n'a lu aucune pièce du côté habilité. Tu écris un **avenant 2** au devis des deux essais d'admission du bras A. Une seule décision le fonde : la mère l'a prise sous GO-2026-11-21-69, en application de la règle permanente de Lazar sur les appels aux modèles de Google (GO-2026-11-21-71, CLAUDE.md de la branche principale). Pour le juge des deux ancres `gemini-4-neon` et pour la vérification de ses clés :
- le plafond de sortie passe de 32 768 à **65 536** ;
- le **niveau de réflexion le plus haut est gardé** ;
- la **sonde de borne est exemptée** de la règle « réflexion plus 16 000 » ;
- l'âge du taux de change : le **dernier fixage publié** est admis quand aucun plus récent n'existe.

Réponds en français ; nomme les choses par ce qu'elles font.

## Pièces à lire
- Le devis accepté : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md` (421ee2e6…), en particulier les sections 5.4, 6 (plafonds, excès, crédit) et 11.1.
- L'avenant 1, version 3, accepté : `docs/notes/relance-organismes-discrets-v1/avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md`, et sa vérification `docs/notes/relance-organismes-discrets-v1/verification-avenant-1-v3-devis-essais-admission-v1.md`.
- La confrontation à la règle Google : `docs/notes/relance-organismes-discrets-v1/confrontation-regle-google-livraison3-v1.md`. Elle estime la file vers 16,50 USD, la vérification vers 3,00 USD, et un débit de 24,4 jetons par seconde.
- La règle : `git show origin/main:CLAUDE.md | awk '/^## Appels aux modèles de Google/{f=1} f{print} /^## Qui conçoit/{exit}'`.
- Les lignes GO-2026-11-21-68, -69 et -71 du registre.
- La note de la livraison 4 du programme : `docs/notes/relance-organismes-discrets-v1/note-programme-essais-admission-bras-a-v3.md`, pour la forme des champs de configuration (plafond, réflexion, exemption de la sonde, borne de réflexion, `recharge_comptee`).
- Le relevé du taux : `docs/notes/relance-organismes-discrets-v1/taux-de-change-v1/` (fixage de la Banque centrale européenne du 20 novembre, 1,0990 USD pour 1 €).
- Du journal `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md`, les seules entrées OD-301 et OD-302, par `grep -E '^- OD-30[12] '` ; n'ouvre pas le fichier.

## Ce que l'avenant 2 contient
1. Les écarts au devis et à l'avenant 1, cités à la lettre avec leurs numéros de ligne. Parmi eux, le mot « goreco » (32 768), remplacé pour Google seulement ; Mistral reste à 32 768.
2. **Tous les chiffres refaits par programme**, calcul montré, arrondis vers le haut : réserve d'un envoi, plafonds par ligne, excès possibles, pire cas total, seuils de crédit par projet. Garde la somme des deux dépenses retirée à chaque solde (avenant 1 v3) et la recharge non comptée (`recharge_comptee: false`, décision de la mère). La marge de change est de 5 %.
3. **Le manque en euros par projet**, avant chaque ligne de Google, au taux relevé : projets à 11,93 € et à 15,59 €.
4. La borne de réflexion à déclarer pour la garde « réflexion plus 16 000 » sous un niveau, et sa justification. Si elle ne peut pas être justifiée sans relevé, dis-le, et propose ce qu'il faut relever.
5. Le débit requis et les délais (devis 5.6) : tiennent-ils à 65 536 ? Sinon, ce qui change.
6. L'exemption de la sonde, écrite exactement : la sonde garde un réglage de réflexion explicite et ne produit aucune lecture jugée.
7. Le **texte neuf des lignes de calcul** touchées, à citer tel quel.
8. Les valeurs de configuration définitive que le programme attend, champ par champ.
9. Ce que tu as ouvert.

Livre `docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v1.md`. Compte rendu final en moins de 150 mots.

## Interdits absolus
- Aucun réseau, aucun appel payant, aucune clé lue ni affichée. Pas de `git fetch`.
- **Cloisonnement.** N'ouvre, ne liste, ne cherche et n'empreinte rien de ce qui suit, même pour vérifier qu'un fichier existe :
  - `bases/`, `sondes/`, tout chemin dont un élément commence par `t07`, rien de T0.8 ;
  - `scripts/mots_et_cout_*`, `prereg/T0.6-organismes-v0-v1.md` ;
  - `docs/notes/bras-a-moniteurs-v1/`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`, `docs/notes/bras-a-sans-interne-v1/` ;
  - `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/` et tout ce qui s'appelle `autres_moniteurs_v*` ;
  - rien sous `runs/` ; `docs/notes/relance-organismes-discrets-v1/essai-mesure-lecteurs-bras-a-v1/` ;
  - tout fichier de scores par unité ; `docs/sources/` ; `registres/` (sauf les lignes de GO nommées ici, par `git show origin/main:registres/go.md | grep <identifiant>`) ; `.claude/settings.json`.
  
  Une pièce permise qui cite un chemin cloisonné : tu recopies la citation, tu ne la suis pas.
- **Registre.** Ta pièce ne recopie rien de ce que les mots de Lazar décident pour l'intervalle impossible et pour le moniteur appris non ajustable, même si une pièce permise le porte ; elle ne nomme aucune ligne de GO du 19 novembre.
- N'écrase rien (R12 : une nouvelle version prend un nouveau nom). Ne scelle rien, ne committe rien.
