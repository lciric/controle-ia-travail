VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION DE PROCESSUS. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

# Mandat du rédacteur — préenregistrement du palier 0b, brouillon v16 (les programmes des étapes 3 à 7) — BROUILLON, EN ATTENTE DU MOT DE LAZAR — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur les décisions de la mère (18:26Z, 18:29Z, 18:53Z) et sur la règle R-4333 : aucune étape 3 à 9 ne se joue avant un GO de Lazar sur le texte qui suit la v13. **La v13 scellée (`d9591d5b…`) reste le texte en vigueur. Rien n'est scellé avant le mot de Lazar.**

## Qui

Le rédacteur de la v15 (modèle F). Tu signes « rédacteur de la v15 et de la v16, modèle F ». Tu n'as écrit aucun des programmes ni aucune de leurs vérifications.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

- **Source** : le brouillon v15, `P/brouillon-v15/preenregistrement-heritage-palier-0b-etage-processeur-v15.md` (`33b04ff46d20a55051236d385c38e5e8fd30e7b3d969bd5d46a54a13b62b842f`). Il a été contrôlé conforme : `P/brouillon-v15/controle-v1/controle-palier-0b-v15-v1.md` (`19e2774a…`).
- **Programme des étapes 3 à 6** :
  - programme v2 : `P/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py` (`1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14`) ;
  - rapports : v1 `P/programme-3-5-6-v1/rapport-programme-3-5-6-v1.md` (`ef1196cd…`, § 3, silences n° 1 à 10, § 4 commande) et v2 `P/programme-3-5-6-v2/rapport-programme-3-5-6-v2.md` (`0042de7a…`, silence n° 11, condition 5) ;
  - vérifications : `P/programme-3-5-6-v1/verification-v1/verification-programme-3-5-6-v1.md` (`5dae3b94…`), `P/verification-programme-3-5-6-v2-v1.md` (`beeaf621…`), `P/verification-essais-programme-3-5-6-v3-v1.md` (`59907a0d…`), `P/verification-essais-programme-3-5-6-v4-v1.md` (`3c0b1cb3…`, « Conforme ») ;
  - les essais qui font foi sont ceux de la v4, `P/programme-3-5-6-v4/tests/test_lancer_etapes_3_5_6_v4.py` (`62065d04…`, 33 essais) ; le programme reste le v2.
- **Programme des étapes 6 bis et 7** : `P/programme-6bis-7-v1/lancer_etapes_6bis_et_7_v1.py` (`ed91813a88c9f58e65dd21d5e7a15fd6d4f2ae810787eb57bf57e7caceeb71d0`) ; son rapport `P/programme-6bis-7-v1/rapport-programme-6bis-7-v1.md` (`14158882…`, § 3, silences n° 1 à 10) ; sa vérification `P/programme-6bis-7-v1/verification-v1/verification-programme-6bis-7-v1.md` (`8d891152…`, conforme, aucun code v7).
- **Programme des étapes 8 et 9** : `P/code-v6/outils-dev/lancer_etapes_8_et_9_v1.py` (`67052a4b7af9bd02c5f28f3b8a7926fd7b7ac5a98fb797f14b3d6f424bedc2a5`), que la v15 porte déjà.

## Décisions de la mère à porter

**Programme des étapes 3 à 6** (mère, 18:53Z) :
- Silences n° 1 et 3 à 10 : ils entrent **tels que le rapport v1 les propose**. Cela couvre :
  - un seul lancement et un manifeste par étape ; un arrêt arrête la chaîne ;
  - la racine `famille=organisme|role=racine` et la tâche `palier-0b|etape-4` ;
  - les fichiers écrits ;
  - les sorties sous `<racine>/diag/heritage-palier-0b-v1/etapes-3-a-6/`, chemin fixé par la pièce de contrôle ;
  - les arrêts propagés sans manifeste, à inventorier (R11) ;
  - le verrou et la pièce de contrôle dès l'étape 3 ;
  - le commit du manifeste pris de l'autorisation ;
  - le programme dans son propre dossier ;
  - les chemins et empreintes des fichiers gelés, rendus par 3–6 et reçus par 6 bis–7 ;
  - l'ordre : 3–6, puis 6 bis–7, puis 8–9.
- **Silence n° 2 (garde 17 toujours jouée)** : c'est un rétrécissement de ce que le texte permet. Le texte admet le cas « non jouée, issue suspendue » ; avec ce programme, ce cas finit en arrêt. **Tu le marques comme ÉCART pour Lazar**, avec ta recommandation, dans une section visible. La mère le porte à Lazar avec la v16. Tu ne le tranches pas.
- **Silence n° 11** (le point 5 de la liste d'arrêt est lu à la fin de l'étape 6) : il entre. Tu ajoutes, comme la vérification v2 le demande, qu'à cet arrêt le fichier des réglages reste gelé et que son empreinte est inscrite au manifeste d'arrêt.

**Programme des étapes 6 bis et 7** (mère, 18:26Z et 18:29Z) :
- Le tri des configurations se fait sans code v7. Il est figé par l'empreinte du programme, inscrite au texte et à la pièce de contrôle, et le texte décrit ce tri, qui est déterministe.
- Silence n° 1 : 22 couples (proposeur × dose), pris à leur configuration de référence, soit 66 comparaisons ; à inscrire.
- Silence n° 4 : le verrou est exigé dès une couche non décisive ; la pièce d'autorisation existe avant l'étape 3.
- Silence n° 5 : la pièce de contrôle est au même chemin que pour les étapes 8 et 9, scellée, et porte le commit et l'empreinte de chaque programme. Elle est lue par sous-chaînes : chaque valeur sur sa propre ligne, avec un libellé fixe, et aucune autre empreinte de 64 chiffres hexadécimaux sur ces lignes.
- Silence n° 8 : les arrêts se propagent sans manifeste ; un manifeste d'arrêt est possible sans code v7.
- Silences n° 2, 3, 6, 7 et 9 : jugés justes par le vérificateur ; ils entrent tels que proposés.
- Silence n° 10 : il est fermé par l'existence du programme des étapes 3 à 6 ; tu le dis.
- Point n° 6 de la vérification : le manifeste porte des champs non nuls hors des couches décisives (`texte_sha256`, pièce, heure) ; à inscrire.
- Remarques S8 : S8 (i) est jouée à l'étape 4 (`etape_4` → `verifier_s8_i`). Si S8 échoue, seul le message de la garde est conservé, avec au plus trois comparaisons détaillées.

## Ce que la v16 porte, et rien d'autre

Le nom neuf est `preenregistrement-heritage-palier-0b-etage-processeur-v16.md`. Chaque remplacement passe par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`), à partir d'un JSON écrit avec l'outil d'écriture de fichiers. Chaque ancre est comptée par `grep -c -F -e` avant l'appel. Les passes sont nommées, comme pour la v15.

1. **Une section neuve, « Les programmes de lancement des étapes 3 à 9 »** : les trois programmes avec leur chemin et leur empreinte entière, la commande de lancement de chacun (rapports, § 4), l'ordre, ce que chacun rend et ce que le suivant reçoit, et les essais qui font foi (pour 3 à 6 : la v4, 33 essais, programme v2).
2. **Les décisions de la mère ci-dessus**, aux lieux du texte qu'elles touchent (étapes 3 à 7, liste d'arrêt, annexe C, pièce de contrôle). Chaque décision est citée avec son heure.
3. **La pièce de contrôle de la mère** :
   - ce qu'elle porte : le commit du code v6 ; les empreintes des trois programmes, sur des lignes à libellé fixe ; le dossier des sorties ; les chemins et empreintes des fichiers gelés entre les lancements ;
   - quand elle est écrite : avant l'étape 3 ;
   - une remarque : le dossier des sorties ne porte pas d'espace (la relecture de la sortie du programme 3–6 se fait par lignes de forme fixe).
4. **La phrase de la v15 qui dit qu'aucun programme n'existe pour les étapes 3, 5 et 6 (ou pour 6 bis et 7)**, s'il y en a une : corrigée à chaque lieu où elle apparaît. Tu comptes ces lieux.
5. **Une section ÉCART POUR LAZAR** : la garde 17 (silence n° 2), avec le texte permis, ce que fait le programme, la conséquence (le cas « suspendue » devient un arrêt) et ta recommandation, ainsi que les deux voies : accepter le rétrécissement, ou demander un programme v3 qui offre le chemin « non jouée ».
6. **En remarque, sans règle** : les essais se jouent sur le fichier entier, sans sélection (`-k`, `--deselect`), sinon l'essai `test_le_programme_charge_est_le_v2` est contourné (vérification v4, point 4).
7. **Le nœud** : un GO de Lazar qui nomme la v16. Le blanc `COMMIT_V6` reste en blanc.
8. **Tenue** : titre ; statut « BROUILLON, non scellé, en attente du mot de Lazar » ; date par `date -u` ; ligne de version ; section « Contre-lecture ».

Ensuite :
- le différentiel `diff -u` de v15 à v16 ;
- le compte des lignes qui commencent par « - Commit du code d'analyse : » (1 attendu) ;
- le compte des lieux où apparaissent les trois empreintes entières des programmes ;
- un rapport court, `rapport-redacteur-palier-0b-v16-v1.md` : remplacements, ancres, et les points où la lettre ne suffit pas, en remarque, jamais tranchés.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v16/`. Chaque fichier a son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement d'un programme ni du code, aucun essai, aucun tirage, aucune pièce d'autorisation ni de contrôle. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus, même sans motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
