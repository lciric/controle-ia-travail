# Contre-lecture de la fiche de lancement de la course Jang-Feng (brouillon 2) — v1

Contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni le kit ni la fiche. 3 novembre 2026, 14:37 UTC (`date -u`).
Aucun appel payant, aucune clé, aucun fichier existant modifié.
- **Arbre** : arbre partiel neuf `wt-cl-jangfeng2`, au commit `9f9ad98e`.
- **Registre des GO** : `registres/go.md` de `main` à `7957d2fe`, lu par `git show`.
- **Fichier écrit** : ce rapport seul, non scellé, non commité.

Objet : `docs/notes/ideation-organisme-v1/course-jang-feng-v1/fiche-lancement-course-jang-feng-v1-brouillon2.md`,
sha256 `87df2d8fd9a7ad45b7ee6567ae84a964578f5229cbbf832a642156397d80867f`. Son compagnon `.sha256` est vérifié : OK. Les
numéros de ligne renvoient à ce brouillon.

## Verdict

**À corriger, dans le texte et au registre ; pas de code.** Aucun constat bloquant.

- **Constat majeur** : CLJ2-01. La variante de repli `sans-opus` doit partir sous GO-2026-11-03-12, mais le périmètre écrit
  de cette ligne ne la nomme pas.
- **Constats mineurs** : trois.
- **Brouillon 1** : CLJ-01 à CLJ-04 sont corrigés ou déclarés de façon acceptable.

## Points demandés

### 1. CLJ-01 à CLJ-04

- **CLJ-01, corrigé.**
  - Deux variantes neuves sans Opus. Fable y tient l'aiguilleur, le juge et le lecteur ; Fable est aussi metteur.
  - Les pièces et la garde lexicale sont identiques à celles de `cinq-especes`.
  - Le risque est décrit, avec les sources communes à la pièce Scheurer (l. 73-80). Fable non plus n'est pas éprouvé, et la
    fiche le dit.
- **CLJ-02, corrigé** (l. 188-189).
- **CLJ-03, corrigé** pour GO-12. Un reste sur GO-13 en CLJ2-03.
- **CLJ-04, acceptable tel que déclaré.**
  - Les exemples de témoin de K4 et l'axe `comparaison_a_la_boite_noire` sont déclarés comme choix du rédacteur. Leur origine
    dans la pièce est donnée (l. 90-92, l. 99-101, l. 185-186).
  - Ils n'orientent pas la réponse : K4 reste « la valeur **ou** une limite ».
  - Les sorties des juges sont rapportées à part et ne gardent ni n'écartent rien.
  - Les retirer demanderait des consignes, des configurations, une table et une répétition neuves. Ce n'est pas justifié pour
    un cadrage mineur.

### 2. Le repli déclaré d'avance (l. 63-71)

Le repli est sans ambiguïté sur les points demandés :
- un premier run dans un dossier neuf (`cinq-especes`, sinon `avec-kimi`, sinon `sans-kimi`) ;
- puis un second run, dans un **second dossier neuf** : `sans-opus-argon` sous GO-13 si Argon est libre, sinon `sans-opus`
  sous GO-12 ;
- rien n'est rejoué à Opus (R-486), et il n'y a aucune autre relance ;
- chaque run garde son registre et son S17.

Deux réserves. La première, sur GO-12, fait l'objet de CLJ2-01. La seconde, sur le constat du refus, fait l'objet de
CLJ2-02.

### 3. S17, appariement et vérification

- **S17 : chacun respecte « entier > 1,2 × pire cas »** (calcul) :
  - 198 > 197,57 (cinq espèces) ;
  - 198 > 167,36 (avec Kimi) ;
  - 198 > 138,29 (sans Kimi) ;
  - 198 > 191,44 (sans Opus) ;
  - 237 > 236,30 (sans Opus, avec Argon).
  - La règle « le plus grand de 198 et de l'entier supérieur » est déclarée (l. 119-123). L'arrêt d'étape vaut 0,9 × S17.
- **Relais des variantes neuves** : chacun couvre son pire cas, et leur somme fait le S17.
  - `sans-opus` : Claude 130,7 ≥ 104,34 ; Astra 65,3 ≥ 54,40 ; Kimi 2 ≥ 0,79.
  - `sans-opus-argon` : Claude 148,3 ≥ 124,72 ; Astra 83,7 ≥ 69,69 ; Argon 3 ≥ 1,72.
- **Plafonds de session** : l'aiguilleur passe à 0,9, au-dessus du pire cas 0,8465 de Fable. Les autres sont inchangés.
- **Vérification `lancer_course_jangfeng_v2.py verifier`**, avec `GO_ID` égal à `--go-attendu` et le registre de `main`
  `7957d2fe` : **code 0 pour les cinq configurations**.
  - Sous GO-12 : `cinq-especes`, `avec-kimi`, `sans-kimi`, `sans-opus`.
  - Sous GO-13 : `sans-opus-argon`.
- **Un mauvais appariement est refusé**, en **code 2**, avant tout appel. J'ai essayé trois cas : `sans-opus-argon` sous GO-12,
  `sans-opus` sous GO-13 et `cinq-especes` sous GO-13. Le message est « A15 : la ligne … porte 198 USD, pas exactement le
  plafond requis 237 USD ».
  - Le contrôle porte **sur le montant seulement**. N'importe quelle ligne à 198 USD passerait, d'où CLJ2-01.

### 4. Diff `ce3dec8a..9f9ad98e`

- **Le diff n'ajoute que des fichiers** (36 fichiers, 5 201 lignes ajoutées, 0 retirée). Aucun fichier v1 n'est modifié (R12).
  Les trois configurations v1 gardent leurs empreintes : `073528eb…`, `b3501965…`, `c4270524…`.
- **Table v2** : 60 lignes, toutes OK par `sha256sum -c`. `table_pieces_gelees_jangfeng_v2.py --verifier` donne « conforme :
  60 pièces gelées ». Tous les compagnons du kit sont OK.
- **Empreintes citées, toutes exactes** : `fccdac4f…` (sans-opus), `b2baa681…` (sans-opus-argon), devis v2 `9eeb769e…`,
  course à blanc v2 `9f580bf4…`, mutations v2 `db539fcd…`, répétition v2 `107e1912…`, lanceur shell v2 `13d08682…`.
- **Marqueurs** : le seul est `<<EMPREINTE_RAPPORT>>`, à la l. 14. Plus aucun `-NN`.

## Constats

### CLJ2-01 — majeur — `sans-opus` partirait sous une ligne de GO dont le périmètre ne la nomme pas

- **Où** : l. 36-37, l. 51 et l. 69-70 de la fiche ; `registres/go.md` de `main`, l. 232 (GO-2026-11-03-12).
- **Le constat** :
  - Le périmètre de GO-12 nomme le kit `ce3dec8a`, le devis v1 `b3204219…` et les variantes « cinq espèces […], sinon quatre
    avec Kimi, repli sans Kimi ». Il ne nomme pas le kit v2, ni la configuration `sans-opus` (`fccdac4f…`), ni son devis
    (v2, pire cas 159,53).
  - GO-13, lui, nomme exactement sa configuration et son devis v2.
  - Le lanceur ne voit pas l'écart, puisqu'il ne contrôle que le montant (point 3).
  - Or une dépense doit avoir un GO sur devis (« Interdits » des consignes du dépôt), et une ligne de GO ne se modifie jamais.
- **Correction** (au choix de session-depot ; l'une ou l'autre suffit) :
  - **(a)** Inscrire une ligne neuve, par exemple GO-2026-11-03-14, à 198 USD. Elle aurait pour périmètre le repli `sans-opus`,
    le kit `9f9ad98e`, `fccdac4f…` et le devis v2, avec la même référence au mot de Lazar. Faire renvoyer la fiche à cette ligne
    pour `sans-opus`.
  - **(b)** Garder GO-12, mais écrire dans une ligne de décision (et à la l. 51) que GO-12 est lu comme couvrant `sans-opus`
    sur la décision R-1158. C'est moins net, parce que le texte de GO-12 ne le dit pas.

### CLJ2-02 — mineur — dire comment on constate que c'est Opus qui a refusé

- **Où** : l. 67-70.
- **Le constat** : un C13 à la proposition peut venir de n'importe quel proposeur. Un échec d'Opus peut aussi être technique
  (délai, erreur 5xx) sans être un refus.
- **Correction** :
  - Écrire que le repli se décide sur le journal du relais Claude (8806) et sur le manifeste de fin, lisibles sans ouvrir la
    sortie scellée, avec un statut de refus pour `claude-opus-5-5`.
  - Écrire que tout autre arrêt ne donne pas de relance, comme le dit déjà la l. 70.

### CLJ2-03 — mineur — GO-13 est déjà inscrit

- **Où** : l. 37-38 (« à inscrire par session-depot sur `main` après ce commit »).
- **Le constat** : la ligne est inscrite sur `main` à `7957d2fe` (l. 233 du registre).
- **Correction** : écrire « inscrite sur `main` à `7957d2fe` ».

### CLJ2-04 — mineur — perte probable des fiches de Kimi, non déclarée

- **Où** : § 7, l. 178-179. Registre : R-1155.
- **Le constat** :
  - Dans les courses Kirchner (seconde) et Ibrahim, toutes les fiches de Kimi ont très probablement été refusées au format
    (`refusees_au_format` égal au quota), avec des consignes 2 à 2,4 fois plus longues que celle de Heimersheim.
  - La consigne Jang-Feng fait 21 797 octets, du même ordre.
  - La R-1155 demande de déclarer cette perte possible. La course continue alors : ce n'est pas un C13.
- **Correction** : une ligne au § 7, « non éprouvé : fiches de Kimi peut-être toutes refusées au format (R-1155) ».
