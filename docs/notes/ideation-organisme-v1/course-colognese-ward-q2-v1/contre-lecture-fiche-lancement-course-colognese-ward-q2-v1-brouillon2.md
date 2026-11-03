# Contre-lecture de la fiche de lancement Colognese-Ward Q2, brouillon 2 (variantes sans Opus) — v1

Contre-lecteur neuf (règle R2), sous-agent qui n'a écrit ni le kit ni la fiche. 3 novembre 2026, 15:20 UTC (`date -u`).

Conditions de la lecture :
- aucun appel payant, aucune clé, aucun fichier existant modifié ;
- arbre partiel neuf `wt-cl-colognese2`, au commit `271e616f` ;
- registres de `main` (`c266f6a2`) lus par `git show` ;
- de la sortie du premier run, seul le rapport a été lu : `rapport-course-colognese-ward-q2-v1.md`, empreinte `00535656…`
  vérifiée ;
- seul fichier écrit : ce rapport, non scellé, non commité.

Objet : `docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/fiche-lancement-course-colognese-ward-q2-v1-brouillon2.md`,
sha256 `247b76c755f7025b56b9c970604c4280d723fc560be942435f2155bf4a0e28e0`, compagnon vérifié. Les numéros de ligne renvoient à
ce brouillon.

## Verdict

**Scellable après corrections mineures, dans le texte seulement.** Aucun constat bloquant, aucun majeur.

- **Ce qui est conforme** : la v2 se borne à retirer Opus. Elle ne sert la question à aucune lignée qui ne l'ait déjà reçue au
  premier run. La règle du repli est conforme à la R-1161, et chaque variante a sa ligne de GO, qui la nomme.
- **Ce qui reste** : quatre constats mineurs.

## Points demandés

### Transposition des constats Jang-Feng

**CLJ-01 (risque de refus et repli) : traité.**
- Le risque de refus de Fable est déclaré (l. 71-72) : Fable a accepté la question comme proposeur au premier run, mais n'a été
  éprouvé ni comme aiguilleur, ni comme juge, ni comme lecteur.
- Le repli sans Opus existe, en deux variantes.

**CLJ-02 (règle des refus sourcée) : traité.**
- La R-486 est citée dans son sens strict (« refus pas rejoué à Opus », l. 23).
- La R-1161 borne le repli (l. 22, l. 50-51).

**CLJ-03 (numéro de GO) : traité pour les numéros, mais le texte est en retard** (CLC2-01).

**CLJ-04 (cadrages déclarés) : repris tels quels de la fiche v1.** Consignes et pièces sont identiques (comparaison des
configurations : `pieces` et garde lexicale égales à `cinq-especes`).

**CLJ2-01 (périmètre de la ligne de GO) : traité.**
- GO-15 et GO-16 nomment chacune leur configuration, le kit `271e616f`, le devis v2, et les conditions « Fable OK » et « si Fable
  refuse, arrêt sans relance ».
- Réserve sur le contrôle du lanceur, en CLC2-03.

**CLJ2-02 (comment on constate les refus) : traité.**
- Le statut d'Opus et celui de Fable sont lus au rapport du premier run (relais Claude : Opus REFUS à 14:48:50, Fable OK à
  14:46:47), avec la réserve « non lu au journal de proposition » (l. 20-21).
- Pendant le second run, la règle n'a pas besoin de distinguer les cas : tout refus de Fable arrête la course sans relance.

**CLJ2-04 (perte des fiches de Kimi) : à moitié.** Les 6 fiches « refusées au format » sont mentionnées, mais pas leur
conséquence pour le second run (CLC2-02).

### La règle du repli et le statut de Fable

La règle (l. 46-52) est sans ambiguïté :
- un seul second run, dans un dossier neuf ;
- `sans-opus-argon` sous GO-16 si Argon est libre, sinon `sans-opus` sous GO-15 ;
- si Fable refuse, arrêt, et rien n'est rejoué ni à Fable ni à d'autres modèles ;
- chaque run a son registre.

Le statut de Fable est établi d'avance par le rapport du premier run. C'est la condition de la R-1161 : seul le refus des deux
modèles Claude exclut le repli.

### La v2 ne fait que retirer Opus

- Proposeurs des variantes neuves : Fable, Kimi, Astra, plus Argon dans `sans-opus-argon`. **Toutes ces lignées ont reçu la
  question au premier run** : les cinq espèces y étaient proposeurs (rapport, « Comptes »).
- Fable prend les rôles d'aiguilleur, de premier juge et de premier lecteur. Il avait déjà reçu la question et les pièces comme
  proposeur, et l'avait acceptée.
- Le contrôle d'Opus (« réponds seulement par le mot OK ») ne porte pas la question (l. 54-55).
- **Aucune lignée nouvelle ne reçoit la question.**

### S17

- `sans-opus` : 198 > 1,2 × 159,53 = 191,44 (calcul). `sans-opus-argon` : 237 > 1,2 × 196,92 = 236,30 (calcul).
- Les variantes v1 sont à 198, qui dépasse 197,57 (cinq espèces), 167,36 et 138,29.
- Relais des variantes neuves, chacun au-dessus de son pire cas ; leur somme fait le S17 :

| Variante | Claude | Astra | Kimi | Argon |
|---|---|---|---|---|
| `sans-opus` | 130,7 ≥ 104,34 | 65,3 ≥ 54,39 | 2 ≥ 0,79 | — |
| `sans-opus-argon` | 148,3 ≥ 124,72 | 83,7 ≥ 69,69 | 2 ≥ 0,79 | 3 ≥ 1,72 |

- Plafond de session de l'aiguilleur : 0,9, au-dessus du pire cas de Fable (0,8465).

### Appariement des lignes de GO

`lancer_course_colognese_v2.py verifier` a été joué sur le registre de `main` (`c266f6a2`), avec `GO_ID` égal à `--go-attendu`.

| Configuration | Ligne de GO | Code |
|---|---|---|
| `cinq-especes`, `avec-kimi`, `sans-kimi` | GO-11 | 0 |
| `sans-opus` | GO-15 | 0 |
| `sans-opus-argon` | GO-16 | 0 |
| `sans-opus-argon` | GO-15 (croisé) | 2 (A15, montant) |
| `sans-opus` | GO-16 (croisé) | 2 (A15, montant) |
| `sans-opus` | GO-11 | 0 |
| `sans-opus` | GO-14, ligne de la course Jang-Feng | 0 |

Les deux derniers cas sont acceptés parce que le contrôle ne porte que sur le montant (CLC2-03).

### Table, empreintes, marqueurs

- **Diff** `f56beeee..271e616f` : 36 fichiers ajoutés, aucune ligne retirée (R12). Les trois configurations v1 gardent leurs
  empreintes : `63e48ad9…`, `608768c6…`, `a38c6759…`.
- **Table v2** : 61 lignes, toutes OK par `sha256sum -c`. `table_pieces_gelees_colognese_v2.py --verifier` donne « conforme :
  61 pièces gelées ». Tous les compagnons du kit sont OK.
- **Empreintes citées, toutes exactes** :
  - configurations : `9aa94613…`, `696b9e97…` ;
  - devis v2 : `bbf02d2c…` ;
  - course à blanc v2 : `2cf69798…` ;
  - mutations v2 : `b0fc6581…` ;
  - répétition v2 : `88bf49ee…` ;
  - lanceur shell v2 : `43ea777e…` ;
  - rapport du premier run : `00535656…`.
- **Marqueurs** : seul `<<EMPREINTE_RAPPORT>>` reste, à la l. 11.

## Constats

### CLC2-01 — mineur — GO-15 et GO-16 sont déjà inscrites

- **Où** : l. 27-28 (« réservées par session-depot et inscrites sur `main` après ce commit ») et l. 102 (« lignes de GO réelles
  GO-15 et GO-16 » parmi les non éprouvés).
- **Correction** : écrire « inscrites sur `main` à `c266f6a2` ». Le `verifier` sur ces lignes réelles est en code 0 (point
  ci-dessus).

### CLC2-02 — mineur — perte probable des fiches de Kimi au second run

- **Où** : l. 21 et § 6.
- **Le constat** :
  - Le premier run compte 6 fiches « refusées au format ». C'est très probablement tout le quota de Kimi, comme dans les courses
    Kirchner (seconde) et Ibrahim (R-1155).
  - Kimi reste proposeur dans les deux variantes neuves.
- **Correction** : une ligne au § 6, « non éprouvé : fiches de Kimi peut-être toutes refusées au format (R-1155 ; 6 au premier
  run) ; la course continue sans elles ».

### CLC2-03 — mineur — n'importe quelle ligne à 198 USD passe le lanceur

- **Où** : l. 42-44.
- **Le constat** : `sans-opus` passe en code 0 sous GO-11, et même sous GO-14, qui est une ligne de la course Jang-Feng. Le
  lanceur ne lit que le montant.
- **Correction** :
  - Écrire que la seule protection est la commande exacte du § 7, où ligne et configuration sont appariées.
  - Écrire que l'ordre à la fille cite cette commande telle quelle.
  - Dans une version suivante du kit, faire vérifier par le lanceur que le périmètre de la ligne nomme l'empreinte de la
    configuration.

### CLC2-04 — mineur — le contrôle d'Opus reste un point de rupture

- **Où** : l. 54-55.
- **Le constat** : ce contrôle ne sert pas la question, mais un échec technique d'Opus empêcherait une course où Opus ne joue
  aucun rôle (code 3).
- **Correction** : le dire en une ligne au § 5.
