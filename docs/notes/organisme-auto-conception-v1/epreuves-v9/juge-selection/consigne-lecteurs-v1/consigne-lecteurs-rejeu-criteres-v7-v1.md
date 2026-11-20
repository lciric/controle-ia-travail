# Consigne des deux lecteurs — rejeu à blanc du juge de sélection, critères v7 — v1

- **Pièce de travail (classe C).** Écrite le 2026-11-20 (`date -u` : 2026-11-20T05:14:06Z) par un rédacteur neuf, modèle F, qui n'a lu aucune carte, sur mandat de la session du compte de l'organisme (`mandat-redacteur-consigne-lecteurs-rejeu-v1.md`, sha256 `567d212ee7bd0ce45145264555f6acb2935ec756105c5292ec864619127b07c0`). À contre-lire par un autre modèle avant d'être remise aux lecteurs. Processeur seul, aucune dépense, aucun appel de modèle.
- **Une seule consigne pour les deux lecteurs** : le lecteur de la lignée Opus et le lecteur de la lignée Fable. Chacun la reçoit telle quelle, seul.
- **Ce qui fait foi, et que cette consigne ne remplace pas** : les critères v7 scellés, `prereg/organisme-auto-conception-v9/juge-selection/criteres-choix-cartes-v9-v7.md`, sha256 `6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f` (notés « les critères »). Tu les lis en entier avant la première carte. Là où cette consigne et les critères divergeraient, les critères priment, et tu écris l'écart dans ta note de dépôt (§ 9) : tu ne le tranches pas.
- **Décisions de Lazar tenues ici** (GO-2026-11-20-10, point O2) : rejeu à blanc d'abord (décision 1 (a)) ; veto à trois cartes, plafond au nombre visé, retrait par famille (décision 2 (a)) ; lignée reconnue déclarée carte par carte, au rejeu (décision 3 (b)) ; « ajoutable » compte oui (décision 4 (b)) ; masque complet, au rejeu (décision 5 (a)) ; huit confirmations telles qu'écrites.
- **Rejeu à blanc : aucune valeur de sélection.** La course rejouée n'est pas tenue à l'écart. Ta lecture ne fait entrer aucune carte à l'épreuve et n'en écarte aucune.

## 0. Le principe, à garder sous les yeux

« ce sont les essais avec experiences qui doivent trancher in fine les cartes et les tetss de mort » (mot de Lazar ; critères, § 0). Tu ne juges pas la valeur d'une carte. Tu décris l'épreuve qu'elle permet, question par question, à la lettre des critères. Une carte mal notée n'est pas réfutée : elle n'est pas éprouvée.

## 1. Ce que tu reçois

1. **Cette consigne**, et son empreinte.
2. **Les critères v7 scellés**, et leur empreinte. Tu la recalcules ; si elle diffère de celle écrite ci-dessus, tu t'arrêtes et tu le dis.
3. **Le fichier des cartes masquées**, sorti du programme de masque, à un chemin et sous une empreinte que la mère te donne au lancement. Tu recalcules l'empreinte avant de l'ouvrir. C'est le seul fichier de cartes que tu ouvres.
4. **Le nombre de cartes attendues**, donné par la mère. Si le fichier n'en porte pas ce nombre, tu t'arrêtes et tu le dis : tu ne complètes rien, tu ne retires rien.
5. **Ton nom de lecteur et ta lignée**, à écrire lettre pour lettre (§ 3.1).

**Ce que le masque a fait aux cartes** (critères, § 1). Chaque carte t'arrive réduite à son contenu : champs dans un ordre fixe, gras, intertitres et puces retirés, formules imposées retirées, phrases récitées retirées, graphies ramenées à une seule. **Chaque champ est coupé à la longueur médiane de ce champ, au dernier mot entier, sans marque de coupe.** Un champ peut donc s'arrêter au milieu d'une idée, et une règle de lecture écrite en fin de champ peut avoir disparu. Tu réponds sur ce qui est servi : tu ne devines pas la fin d'un champ. Si tu ne peux pas trancher sans inventer, la réponse est « indécidable » (§ 5).

**Ce que tu ne reçois jamais, et que tu ne cherches pas** : l'espèce du proposeur ; le champ `meta` ; le fichier des cartes non masquées ; le classement de l'orchestrateur ; le verdict d'un juge de la course ; la sortie du lecteur par programme ; la table des espèces ; les rejeux antérieurs et leurs lectures ; la lecture de l'autre lecteur ; toute ligne de GO, toute proposition, toute pièce qui nomme des cartes.

## 2. Ce que tu rends

1. **Un fichier JSON, un seul**, au format exact du § 3 : toutes les cartes, puis ta liste de veto. Encodage UTF-8. Le nom du fichier t'est donné par la mère.
2. **Son compagnon d'empreinte** (`sha256sum` du fichier, redirigé vers le même nom suivi de `.sha256`).
3. **Une note de dépôt**, courte, à côté du fichier (§ 9).

**Tu scelles et tu verses ta lecture avant d'ouvrir toute pièce qui nomme des cartes** (critères, § 1). Une lecture versée ne se retouche pas : une correction est une lecture neuve, sous un nom neuf, demandée par la mère.

## 3. Le format, à la lettre

Le programme d'assemblage refuse toute clé en trop, toute clé manquante, toute valeur hors de celles qui suivent. Il ne devine rien : une lecture refusée est une lecture à refaire en entier.

### 3.1 En tête : cinq clés, exactement

| clé | valeur |
|---|---|
| `lecteur` | `"F"` pour le lecteur de la lignée Fable ; `"O"` pour le lecteur de la lignée Opus. Une lettre majuscule, rien d'autre. |
| `lignee` | `"prop-fable"` pour le lecteur de la lignée Fable ; `"prop-opus"` pour le lecteur de la lignée Opus. Lettre pour lettre : minuscules, un tiret, aucun espace. C'est la clé de la table des familles du manifeste ; toute autre graphie est refusée. |
| `independance` | une chaîne non vide : ta déclaration, en toutes lettres (§ 3.2). |
| `cartes` | la liste de toutes les cartes servies (§ 3.3). |
| `veto` | ta liste de veto, ordonnée (§ 7). Une liste, même vide. |

### 3.2 La déclaration d'indépendance

Tu l'écris seulement si elle est vraie, mot pour mot :

> Je n'ai écrit ni ces critères ni aucune carte. Je n'ai lu ni les cartes non masquées, ni les rejeux antérieurs, ni la lecture de l'autre lecteur. J'ai lu seul les cartes masquées servies par le programme.

Si l'une de ces phrases est fausse pour toi, tu ne lis pas : tu t'arrêtes et tu le dis.

### 3.3 Par carte : treize clés, exactement

Tu rends un enregistrement **pour chaque carte servie, même celle où tu vois un cas d'exclusion**. Chaque carte une fois, jamais deux.

| clé | valeur |
|---|---|
| `id` | l'identifiant de la carte, recopié tel que servi. |
| `lignee_reconnue` | **écrite d'abord, avant toute note** (§ 4). L'une des six chaînes du § 4, lettre pour lettre. |
| `exclusion` | `null` ; ou un objet `{"cas": …, "phrase": …}` où `cas` vaut `"X1"`, `"X2"`, `"X3"`, `"X4"` ou `"X5"` et `phrase` est la phrase de la carte qui porte le cas. **Pour `"X1"` seulement**, une troisième clé, `"separable"`, qui vaut `true` ou `false` ; pour les autres cas, cette clé est refusée. Le cas X6 n'est pas à toi : les cartes hors du choix ne te sont pas servies. |
| `voie` | `"I"`, `"P"` ou `"N"` (critères, § 3, les trois questions dans leur ordre). |
| `sous_strate` | en voie P : `"a"`, `"b"`, `"c1"`, `"c2"`, `"c3"`, `"d"` ou `"e"`. En voie I ou N : `null`. |
| `question` | la question, ou l'usage, en une phrase ; `null` si tu ne peux pas l'écrire. **En voie N, `question` à `null` impose `Q` à 0** : le programme refuse toute autre note. |
| `E`, `Q`, `D` | trois entiers, chacun 0, 1 ou 2 (critères, § 4). Des nombres, non des chaînes. |
| `raisons` | un objet à trois clés, `"E"`, `"Q"`, `"D"` : une phrase non vide pour chacune. Une note sans raison est une lecture à refaire. |
| `items` | un objet à dix-huit clés, exactement : `T1`, `T2`, `T3`, `T4`, `B1`, `B2`, `B3`, `B4`, `A1`, `A1i`, `A2`, `A3`, `A4`, `A4i`, `S1`, `S2`, `S3`, `S4`. Valeurs : `"oui"`, `"non"`, `"indecidable"` (sans accent), `"ajoutable"` (§ 5). |
| `phrases` | un objet aux mêmes dix-huit clés : une phrase non vide par réponse. |
| `groupe_fusion` | `null` ; ou une étiquette libre, la même pour toutes les cartes qu'une même épreuve juge — même oracle, mêmes bras, même monde planté (critères, § 6). |

**Clés interdites, dans toute carte** : `meta`, `espece`, `proposeur`, `contenu`. Le programme refuse la lecture entière.

**`A1i` et `A4i`** sont la forme « instrument » des questions A1 et A4. Tu réponds aux deux formes pour toute carte, quelle que soit sa voie (critères, § 5.1).

### 3.4 Gabarit (identifiants et textes fictifs ; aucune carte réelle)

```json
{
  "lecteur": "F",
  "lignee": "prop-fable",
  "independance": "Je n'ai écrit ni ces critères ni aucune carte. Je n'ai lu ni les cartes non masquées, ni les rejeux antérieurs, ni la lecture de l'autre lecteur. J'ai lu seul les cartes masquées servies par le programme.",
  "cartes": [
    {
      "id": "IDENTIFIANT-TEL-QUE-SERVI",
      "lignee_reconnue": "aucune",
      "exclusion": null,
      "voie": "P",
      "sous_strate": "c2",
      "question": "Une phrase.",
      "E": 2, "Q": 1, "D": 2,
      "raisons": {"E": "Une phrase.", "Q": "Une phrase.", "D": "Une phrase."},
      "items": {"T1": "oui", "T2": "non", "T3": "ajoutable", "T4": "indecidable",
                "B1": "non", "B2": "ajoutable", "B3": "non", "B4": "non",
                "A1": "oui", "A1i": "non", "A2": "non", "A3": "oui", "A4": "oui", "A4i": "non",
                "S1": "non", "S2": "oui", "S3": "non", "S4": "non"},
      "phrases": {"T1": "Une phrase.", "T2": "Une phrase.", "T3": "Une phrase.", "T4": "Une phrase.",
                  "B1": "Une phrase.", "B2": "Une phrase.", "B3": "Une phrase.", "B4": "Une phrase.",
                  "A1": "Une phrase.", "A1i": "Une phrase.", "A2": "Une phrase.", "A3": "Une phrase.",
                  "A4": "Une phrase.", "A4i": "Une phrase.",
                  "S1": "Une phrase.", "S2": "Une phrase.", "S3": "Une phrase.", "S4": "Une phrase."},
      "groupe_fusion": null
    }
  ],
  "veto": [
    {"id": "IDENTIFIANT-TEL-QUE-SERVI", "prediction": "Une phrase.", "decision": "Une phrase.", "lignee_reconnue": "aucune"}
  ]
}
```

Le lecteur de la lignée Opus écrit `"lecteur": "O"` et `"lignee": "prop-opus"` ; tout le reste est de même forme.

## 4. La lignée reconnue, carte par carte (décision 3 (b))

**Le champ `lignee_reconnue` porte, pour chaque carte et pour chaque entrée de ta liste de veto, exactement l'une de ces six chaînes, lettre pour lettre, en minuscules, sans espace, sans guillemet ni ponctuation ajoutés : `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra`, `prop-carbon`, ou `aucune`.**

- **Toute autre graphie est une faute que le programme ne voit pas.** Il contrôle seulement qu'un texte est présent. « Opus », « prop-Opus », « fable », « aucun », « inconnue », « prop-opus ? », deux étiquettes dans la même chaîne : chacune passerait, et serait comptée en silence comme « ne croit pas reconnaître sa famille ». C'est une lecture à refaire, non une valeur. Relis ce champ, carte par carte, avant de sceller.
- **Quand l'écrire.** Pour chaque carte, **avant de la noter** : tu lis la carte, tu écris `lignee_reconnue`, puis seulement l'exclusion, la voie, les notes et les réponses. Tu ne reviens pas sur ce champ après avoir noté.
- **Ce que tu y écris.** La lignée que tu crois reconnaître à la manière d'écrire, si tu crois en reconnaître une. Sinon `aucune`, qui est une réponse entière : tu n'es pas tenu de deviner.
- **Si tu crois reconnaître la famille qui réunit `prop-opus` et `prop-fable`, sans pouvoir dire laquelle des deux** : écris celle des deux qui te paraît la plus probable. Le programme ne compare que la famille.
- **Ce champ n'est pas une note.** Il n'entre dans aucune note, aucun rang, aucune liste. Il ne doit changer ni ta voie, ni tes notes, ni tes réponses, ni ton veto. Le programme compte, après coup, si tes notes suivent la lignée que tu as cru reconnaître plutôt que la lignée vraie : c'est une description, que tu ne verras pas avant la fin.
- **Dans la liste de veto**, chaque entrée porte aussi `lignee_reconnue` : tu y recopies la valeur que tu as écrite pour cette carte dans `cartes`, sans la changer.
- Tu ne cherches la lignée vraie nulle part. Tu n'ouvres rien pour vérifier.

## 5. Les dix-huit réponses, et la réponse « ajoutable » (décision 4 (b))

Les questions sont celles des critères, § 5.2, à leur lettre. Elles portent sur **l'épreuve que la carte permet**, non sur sa prose (§ 5.1).

- **`oui`** : la carte le dit, ou cela suit de ce qu'elle dit sans rien inventer. Ta phrase donne les mots de la carte, ou la déduction. Une carte brève qui fixe ce qu'il faut n'est pas moins bien notée qu'une carte longue qui le répète.
- **`non`** : la carte dit le contraire, ou la chose manque et ne peut pas se déduire.
- **`indecidable`** : tu ne peux pas trancher sans inventer.
- **`ajoutable`** : permise sur **sept questions seulement — `T3`, `B2`, `B3`, `B4`, `S1`, `S3`, `S4`**. Sur toute autre question, le programme refuse la lecture. Tu la donnes quand la carte ne dit pas la chose, mais qu'un préenregistrement peut l'ajouter **sans toucher au mécanisme** : un seuil, une quantité appariée nommée, une seconde dose, un contrôle positif, un réglage, une issue intermédiaire, une autre ligne nommée. Ta phrase dit **ce qui serait ajouté**, et pourquoi le mécanisme n'en est pas touché.

**Ce que « ajoutable » vaut, et ce que cela ne change pas pour toi.** Par la décision 4 (b), « ajoutable » compte oui dans le rang de ce rejeu ; les trois régimes sont joués et rapportés. Tu réponds de la même manière sous tout régime :
- si la carte dit la chose, c'est `oui`, non `ajoutable` ;
- si l'ajouter demande de changer le mécanisme, ou si la carte dit le contraire, c'est `non` ;
- si tu ne peux pas dire, sans inventer, que l'ajout laisse le mécanisme intact, c'est `indecidable` ;
- « ajoutable » n'est ni un oui de politesse ni un refuge : elle se donne question par question, avec sa phrase.

## 6. Exclusions, voies, notes d'entrée : renvois

- **Exclusions** (critères, § 2) : tu écris le cas que tu vois, avec la phrase de la carte qui le porte, **et tu notes la carte quand même**, en entier. Tu n'écartes rien : c'est le programme qui écarte, quand les deux lecteurs voient le même cas. Pour X1, tu dis si la mesure est séparable de la décision ; **tu n'amputes jamais une carte**.
- **Voie et sous-strate** (critères, § 3) : par le contenu de la carte, jamais par l'espèce que tu crois reconnaître.
- **E, Q, D** (critères, § 4) : chaque note avec sa raison. Pour D, la lettre du § 4.3 : retirer un module, ou ne pas l'ajouter, est une décision nommée.
- **Ne sont pas des critères** (critères, § 0) : le coût, le nombre de bras, la dépendance à un branchement non écrit, la longueur de la carte, le mot « inédit », tout chiffre ou travail publié cité, l'ordre des identifiants. À l'axe A, tu lis « branchement supposé allumé ».
- **Fusion** (critères, § 6) : même étiquette de `groupe_fusion` pour les seules cartes qu'une même épreuve juge.

## 7. Le veto et sa liste (décision 2 (a))

**Ce qu'il est** (critères, § 8). Une entrée par le contenu, hors de la règle, dans ce qui est proposé en premier. Il ne fait rien adopter, ne retire aucune carte, ne change aucune note ni aucun rang, **et ne s'exerce jamais contre une carte**.

**Ce que tu rends.** Une liste **ordonnée**, de la carte que tu veux le plus voir éprouvée à la moins :
- **trois cartes** de veto, puis **six suppléantes au plus** : **neuf entrées au plus**. Au-delà, le programme refuse la lecture ;
- chaque entrée est un objet à **quatre clés, exactement** : `id` (une carte de ta lecture, recopiée telle que servie), `prediction` (l'issue que tu prédis pour l'oracle, en une phrase), `decision` (la décision de conception que l'épreuve changerait, en une phrase), `lignee_reconnue` (§ 4) ; les quatre non vides ;
- aucune carte deux fois ;
- pas de clé qui distingue les trois premières des suppléantes : c'est l'ordre qui le dit ;
- une liste plus courte, ou vide, est permise. Un veto non exercé ne se reporte pas et ne se cède pas.

**Ce que le programme en fait, après le dépôt des deux lectures, sans toi.** Il lit l'espèce, que tu ne vois pas, et parcourt ta liste dans son ordre. Il passe, sans la compter : une carte de la famille du titulaire (retrait par famille) ; une carte écartée ou rendue à Lazar ; une carte dont la ligne est déjà dans le nombre visé. Il garde les trois premières qui restent ; les suivantes sont des suppléantes non appelées. Si ta liste s'épuise, rien n'est mis à sa place. Les cartes entrées par veto ne dépassent jamais le nombre visé ; à deux lecteurs, ce plafond ne joue pas (six cartes au plus). **Tu n'apprends pas ce qui a été retiré avant la fin de la sélection.**

**Comment désigner.** Sur le contenu, sans voir l'espèce. Tu ne composes pas ta liste d'après la lignée que tu crois reconnaître, ni pour devancer le filtre : les suppléantes sont là pour cela. Chaque veto est une prédiction, vérifiable après l'épreuve.

## 8. Ce que tu ne fais jamais

- **Trancher.** Tu ne dis d'aucune carte qu'elle est bonne, mauvaise, vraie ou réfutée.
- **Adopter ou condamner.** Ni par une note, ni par le veto, ni dans ta note de dépôt.
- **Ouvrir autre chose que les cartes servies**, les critères et cette consigne. Aucune recherche dans le dépôt, aucune archive, aucun autre fichier de cartes, aucun appel à un modèle, aucune source extérieure pour vérifier ce qu'une carte cite.
- **Lire ou chercher l'espèce**, ou écrire une clé `meta`, `espece`, `proposeur` ou `contenu`.
- **Parler à l'autre lecteur**, lire son travail, ou accorder tes réponses aux siennes. Aucun désaccord n'est résolu par discussion.
- **Sauter une carte**, en fusionner deux en un enregistrement, ou laisser une réponse sans sa phrase.
- **Amputer, réécrire ou compléter une carte.**
- **Changer un critère qui te paraît inapplicable.** Tu l'appliques à la lettre et tu écris l'écart dans ta note de dépôt.
- **Régler tes réponses sur un résultat** : ni pour qu'une lignée entre ou sorte, ni pour que la règle range.
- **Retoucher une lecture versée.**

## 9. La note de dépôt

Courte, à côté du fichier JSON, jamais dedans. Dans cet ordre :
1. en première ligne, mot pour mot : « deux lecteurs d'une même famille ; aucun lecteur d'une autre famille sans dépense ; l'écart par famille n'est pas séparable de la préférence pour soi » ;
2. « rejeu à blanc, aucune valeur de sélection » ;
3. les empreintes : cette consigne, les critères, le fichier des cartes masquées, ta lecture ;
4. le nombre de cartes lues, à côté du nombre attendu ;
5. les écarts : tout critère que tu n'as pas pu appliquer à la lettre, toute divergence vue entre cette consigne et les critères, tout champ coupé qui t'a laissé sans réponse sur plusieurs questions — sans identifiant de carte si tu peux le dire sans ;
6. tout refus de permission, de classifieur ou de garde, et tout arrêt.

Elle ne dit rien de la valeur d'une carte.

## 10. Avant de sceller : ce que tu relis

- `lecteur` et `lignee` : lettre pour lettre (§ 3.1) ;
- le nombre d'enregistrements égale le nombre de cartes attendues ; aucun identifiant en double ;
- chaque carte porte ses treize clés, ni plus ni moins ; chaque entrée de veto ses quatre ;
- **chaque `lignee_reconnue`, dans `cartes` et dans `veto`, est l'une des six chaînes du § 4, lettre pour lettre** ;
- « ajoutable » n'apparaît que sur `T3`, `B2`, `B3`, `B4`, `S1`, `S3`, `S4` ;
- `indecidable` est écrit sans accent ;
- hors de la voie P, `sous_strate` vaut `null` ; en voie N sans question, `Q` vaut 0 ;
- `separable` n'apparaît que sous le cas `X1` ;
- neuf entrées au plus dans `veto`, toutes des cartes de ta lecture.

Tu fais ces contrôles sur ton propre fichier, sans lancer le programme d'assemblage : il est à la mère.

La lecture décrit ; la proposition propose ; Lazar choisit ; l'épreuve tranche.

*rédacteur neuf, modèle F*
