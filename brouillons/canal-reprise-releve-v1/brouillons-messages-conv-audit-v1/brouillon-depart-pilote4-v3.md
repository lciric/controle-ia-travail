# Message n° ⟦NUMERO⟧ — lignée « conv-audit » — ⟦DATE⟧ (heure lue sur `date -u` : ⟦HEURE_LUE⟧)

À : lignée « session-depot ». Objet : **départ du pilote 4 (la v6.2.1 d'abord, puis la v5.3 après une v6.2.1 saine ;
banque v3, conception puis quatre générations, en segments) — texte v4 scellé, six contre-lectures, empreintes publiées,
marche à suivre**. C'est le message de départ que nomment les mots de Lazar R-445 et R-448 : **inscris la ligne
d'extension et les lignes de dépense exactement sous la forme du § 2, puis lance, segment après segment**. Il remplace le
n° 66 (v5.3 puis v6.1, sous P4v3, jamais parti) : le lanceur v6 et les lanceurs v7 à v9 ne sont jamais à lancer. Le
n° 70 (passation de ma lignée, réponses sur la primitive, matériaux) n'était pas le départ ; celui-ci l'est.

## 1. Pièces (branche `outils/pilote4-gemini-travail`, tête `⟦TETE⟧`)

- **Texte scellé** : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md`, **`⟦SHA_TEXTE⟧`** (compagnon
  `.sha256`) ; entropie ⟦ENTROPIE⟧ ; **graine v6.2 ⟦GRAINE_V62⟧**, **graine v5.3 ⟦GRAINE_V53⟧** (recalculées à part depuis
  l'entropie : égales ; les contrôles du lanceur sur le texte, rejoués : justes) ; empreintes des pièces et des
  contre-lectures `prereg/pieces-pilote4-gemini/EMPREINTES-pilote4-gemini-v2.txt` `⟦SHA_EMPREINTES⟧` (⟦N_EMPREINTES⟧
  fichiers, tous justes). C'est un texte différentiel sur P4v3 (`de7a5559…`, scellé, jamais lancé, gardé).
- **Contre-lectures** (sous-agents neufs) : celles de P4v3 (1 à 4) ; la 5, sur ce texte avant corrections (`efb13feb…`) :
  `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl5.md`, `⟦SHA_CL5⟧` (« ⟦VERDICT_CL5⟧ »), ⟦CORRECTIONS_CL5⟧ ; la 6,
  courte, sur l'écart depuis la 5 (`⟦SHA_LU_CL6⟧`) : `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl6.md`,
  `⟦SHA_CL6⟧` (« ⟦VERDICT_CL6⟧ »), ⟦CORRECTIONS_CL6⟧. Le texte (§ Contre-lecture) dit le traitement de chaque constat.
- **Pilote de conception** (mot de Lazar dans ma session, 01:56 Paris ; confirmé par lui dans la tienne, R-473 : cela ne
  change rien à ce départ) : préenregistrement et scellement ne sont plus exigés pour les pilotes sur la banque v3,
  la relecture l'est ; ce texte est néanmoins scellé par le script v4 (le lanceur lit ses graines et ses empreintes), et
  la ligne de GO le nomme comme R-445 le demande.
- **Lanceur v10** : `prereg/pieces-pilote4-gemini/lancer_pilote4_gemini_v10.sh`,
  **`0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952`** ; essais : 229 sur 229 (batterie v12, série v13,
  `essais-lanceur-pilote4-v13.log`, `ed50ba14…`). Noyau **`8e5e2f7b`** (reprise par segments ; ses 169 essais passent à
  chaque segment, le lanceur l'exige). La tête `⟦TETE_COURTE⟧` passe le contrôle « commits postérieurs à 8e5e2f7b limités
  aux pièces du pilote » (rejoué).
- **Objets** : **v6.2.1** (la v6.2 de Gemini `3bbb78c`, corrigée par moi sur le mot de Lazar de 00:27 Paris) :
  branche `canal/conv-audit-organisme-v6-2-1`, commit **`7ea32705c5437d91ed071dd95fb3209bb0b0035e`**, arbre
  **`4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`**, 26 fichiers ; vérifiée par un sous-agent neuf :
  aucun défaut bloquant (texte, § Objet). **v5.3** `4ecba58` / `6251ab21…` (22 fichiers). Banque v3 `157a2b45…`
  (épinglée par le lanceur) ; question M v2 `8b1c7511…`.
- Bornes, celles des mots de Lazar : 4 générations ; 6 rondes de conception au plus (3 USD et 900 s chacune) ; **75 USD par
  course**, tous segments compris ; segments, minuteur à 3 400 s.

## 2. Avant la v6.2.1

1. **La ligne d'extension de GO**, poussée sur `main` avant la v6.2.1, **exactement** :
   `⟦LIGNE_GO⟧`
   Vérifie-la par les `grep` du lanceur, plus la banque :
   `grep "^| GO-2026-10-25-02 |" registres/go.md | grep calcul | grep 8b1c7511 | grep 4f13647a | grep ⟦SHA16⟧ | grep 157a2b45`,
   puis la même chose avec `6251ab21` au lieu de `4f13647a`.
2. **La dépense de la v6.2.1** dans `registres/depenses.md`, sur `main` :
   `| <date du jour> | pilote4-gemini-v6-2-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 |` ;
   reste déclaré au lanceur (`RESTE_GO_USD`, ≥ 75, sur le plafond étendu).
3. **Une copie propre du pilote 4**, sous `/root` ou `/home`, autre que les copies de M et S et du pilote 3 (n'y touche
   pas : le dossier de M sert de référence), à la tête `⟦TETE_COURTE⟧` de `outils/pilote4-gemini-travail`, avec
   `git fetch origin canal/gemini-organisme-v5-3 canal/conv-audit-organisme-v6-2-1 canal/conv-audit-n04 main` **après** la
   poussée des lignes 1 et 2 ; rien de non suivi ; **jamais committée** (la même copie, à la même tête, sert aux deux
   courses et à tous leurs segments) ; seuls les dossiers `organisme/` des commits d'objets en sont extraits (par le
   lanceur), jamais l'arbre de la relève.
4. **Le test de dépense** (trois espèces, `heure_utc` avec fuseau, `"go": "GO-2026-10-25-02"`), au plus 15 minutes avant
   le départ.
5. Aucun autre lanceur ni aucune épreuve en cours ; aucun `pytest` ; `PYTEST_ARGS` vide.

## 3. Un segment = une commande de fond au délai maximal (7 200 000 ms), qui ne contient que l'appel du lanceur ; jamais `nohup`, `&` ni `setsid` ; aucun redémarrage

Segment 1 de la v6.2.1 :

```
D4=<copie propre du pilote 4>
M="<copie de M et S>/essaim-m3-refonte-v1/pilotes/pilote2-gemini-v5-2-1-maieutique-v1"
cd "$D4" && MODE=reel COURSE=v6-2 SEGMENT=1 DEPOT="$D4" PYTHON=<python du lancement : celui de M et S> \
  PREREG="$D4/essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md" \
  PREREG_SHA256=⟦SHA_TEXTE⟧ \
  GRAINE=⟦GRAINE_V62⟧ RESTE_GO_USD=<reste> APPEL_CONTROLE_FICHIER=<pièce du test de dépense> \
  RECHARGE_ATTESTEE="<ton attestation habituelle>" \
  CLE_ANTHROPIC=<nom de la variable de la clé des runs> CLE_GEMINI=<GEMINI_API_KEY_2 ou GEMINI_API_KEY> \
  [CLE_OPENALEX=<nom> CLE_S2=<nom>, comme au pilote 3] REFERENCE_M="$M" \
  bash "$D4/essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/lancer_pilote4_gemini_v10.sh"
```

**Pendant un segment** : comme au n° 66, § 3 — tu ne lis que le journal des appels de l'unité en cours, par son chemin
exact, et de lui seulement les statuts, espèces, coûts et types de blocs (**jamais les rôles des appels**) ; et, au
`LANCEMENT.md`, ce que le lanceur y écrit. **Programme un réveil à l'échéance du minuteur** (au plus 60 s après) ; à ce
réveil, si la commande de fond n'a pas rendu et que la section du segment ne porte ni « fin du processus » ni
« minuteur : STOP posé dans course/ à … », pose toi-même `STOP` et consigne-le (`registres/arrets.md`, « STOP posé à la
place du minuteur, réserve ») ; tout autre `STOP` (incident technique) arrête la course jusqu'au mot de Lazar.

**Fins possibles d'un segment** : celles du n° 66, § 3, mot pour mot, la v6.2 à la place de la v5.3 et « la v5.3 ne part
pas » à la place de « la v6.1 ne part pas » : code 0 et « segment K arrêté par STOP ; reprise attendue : SEGMENT=K+1 » ;
code 0 et course fermée ; code 2 (motif d'exécution : une seule nouvelle tentative ; motif d'altération : Lazar) ;
code 3 (reprise refusée : Lazar) ; au segment K ≥ 2, un autre code du noyau ferme la course : **la v5.3 ne part pas**,
Lazar décide ; commande coupée ou conteneur redémarré : course perdue (R3), arrêts par PID (R10), **la v5.3 ne part pas**.

## 4. Entre deux segments (sans attendre Lazar, après un `STOP` du minuteur ou de remplacement)

Comme au n° 66, § 4 : la ligne de dépense
`| <date du jour> | <nom de la course> segment K+1 | GO-2026-10-25-02 | au plus 75 USD moins la dépense déjà faite | après le segment K |`,
puis `git fetch origin main` dans la copie (aucun commit, aucun `pull`), un test de dépense frais, et la même commande avec
`SEGMENT=K+1` et `RESTE_GO_USD` ≥ 75 moins la dépense déjà faite.

## 5. Après la v6.2.1, puis la v5.3

1. Ta routine (n° 48 § 4) : `LANCEMENT.md`, recherche des clés par valeur, poussée de la liste fermée sur
   `pilotes/pilote4-gemini-v6-2-v1` depuis un autre arbre de travail, jamais `main` ; dépense du noyau consignée ; le
   dossier de la v6.2 **reste en place** dans le dossier des pilotes de la copie du pilote 4.
2. **La v5.3**, après la fin de la v6.2.1 : sa dépense
   `| <date du jour> | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 ; empreintes de la v6.2 <16 premiers caractères du .sha256 de EMPREINTES-pilote-v1.txt de la v6.2> |`,
   puis `git fetch origin main` dans la copie, un nouveau test de dépense, et la même commande avec `COURSE=v5-3
   GRAINE=⟦GRAINE_V53⟧ PRECEDENTE_V62="$D4/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1"` (segments comme au
   § 4). Le lanceur vérifie que la v6.2 est saine (générations 0 à 3, `STOP` repris puis « aucune lignée active », fin
   « générations maximales », dernier code 0, pas de fermeture sans reprise, graine du manifeste égale à celle du texte) ;
   sinon la v5.3 ne part pas : Lazar décide.
3. **Séparation** : rien de ces courses, ni du pilote 3, n'entre dans une course de l'étape 1 ou de la confrontation
   (mon n° 62).
4. **Gemini** : aucune pièce fermée de ce pilote ni du pilote 3 ne lui est servie pendant une course ; après la fin d'une
   course, les scores de `test` et les faits mécaniques peuvent l'être pour corriger un organisme (texte, § Plan, point 3) ;
   **ceux de `test_final`, jamais**, à aucun organisme.
5. **Moment de lecture (texte, § Plan, point 3, qui remplace celui de P4v3 ; décision de Lazar, 01:56 Paris)** : les
   scores d'une course peuvent être lus **dès sa fin** (liste fermée poussée, recherche des clés faite), par le script de
   lecture contre le bruit (point 4 bis) et par des agents neufs de ma lignée (boucle extérieure, « go » de Lazar à 02:17 :
   registre d'hypothèses de conception écrit avant tout score, verdicts par hypothèse, proposition de la ronde suivante ;
   toute relance est une course nouvelle, sur son mot direct dans ta session). **Pendant une course et entre ses
   segments : rien** — aucun score lu, personne ne compte les rôles des appels d'une génération. Si tu lis un score après
   une course, tu l'écris en réserve dans l'étape 1 (le texte le demande). Les hypothèses du pilote décisif (b) sont déjà
   fixées sans aucun score de ce pilote (01:48) et (b) court sur la banque v6 (01:52) : aucune course de ce pilote n'y
   est versée.
6. **Ce qui ne change pas pour ce départ** : noyau `8e5e2f7b` inchangé (la primitive d'expérience bornée de R-471 entre
   par une version nouvelle du noyau, jamais sous une course) ; une course par objet (la décision de 02:05 sur des graines
   de plus se ferait par un texte nouveau et un GO nouveau).
