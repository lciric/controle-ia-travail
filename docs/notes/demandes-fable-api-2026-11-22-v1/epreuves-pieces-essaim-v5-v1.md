# Épreuves rejouées sur la version 5 des pièces de la comparaison essaim contre isolé, v1

22 novembre 2026, Opus 5.5. Pièce éprouvée : `pieces-comparaison-essaim-v5.md` (sha256 681d341cbbb8700c7af6591247969cee4ba6d03abd5f979cf48946042602301a). Règle : « code de référence de l'article 4 » de la relecture de Fable (`relecture-pieces-essaim-v4/relecture-fable-api.md`, sha256 c1cebee3a8abec9cc142c458a6eb05800f2095fcef576fc99c0a93a974c7b4d7), lu par programme dans la relecture et exécuté tel quel. Python 3.13.18, `python3 -I`, depuis ce dossier.

**Verdict.**
- **Épreuve des balises, lot de pièges et cas sains : PASSE.** 10 sains sur 10, 8 pièges sur 8, 10 anciens textes sans balise sur 10 au verdict attendu ; les deux motifs de l'article 4 sont identiques à ceux du code ; les trois mutations sont prises.
- **Lot aveugle de l'article 9 (six textes d'un agent neuf qui n'a lu que les consignes balisées) : NON JOUÉ.** Deux raisons : je n'ai pas d'outil pour lancer un agent neuf ; et les consignes balisées n'existent pas encore (le texte à insérer est donné par Fable, sa place dans la consigne du tour III.3 n'est pas fixée : voir la table des corrections, points ouverts). La pièce 1 n'est donc pas scellable d'après le verdict de la relecture.
- **Épreuve aveugle dans la forme de la v2 : rejouée, sortie brute jointe.** Ancienne règle de la v4 : 0 sur 3 (5, 4 et 0 duels pour 3, 3 et 2 attendus), les mêmes nombres que `epreuve-aveugle-motifs-v2.md` (8720522f…) ; les ouvertures imprimées sont exactement celles de la trace à la main de Fable. Règle de la v5 : les trois textes, écrits sans balise, sont « non conformes », comme attendu ; ce n'est pas un succès de repérage, seulement le verdict que l'article 4 prescrit pour un tour sans balise.

## Ce qui change dans l'épreuve des motifs, et pourquoi (d'après le seul texte de Fable)

- **Règle éprouvée.** L'article 4 ne cherche plus H_A, H_B ni la section (b) (correction 50, « Aucun motif ne cherche H_A, H_B ni la section (b) ») : l'ancien script, qui éprouvait ces motifs, ne s'applique plus. Le nouveau script `epreuve_motifs_v5_v1.py` (sha256 050377a49d51638c5818ec5332dda7098d751adf3256d4c8aa92c1bcd9dcad38) exécute la fonction `duels_balises` de la relecture, et vérifie que ses deux motifs sont ceux écrits à l'article 4 de la v5.
- **Forme de l'épreuve.** L'article 9 remplace les dix textes synthétiques par deux lots (correction 51) : un lot aveugle et un lot de huit pièges au verdict fixé d'avance, nommés un à un. Seul le lot de pièges est jouable ici.
- **Gardé de l'épreuve v4.** Les dix textes de la v4 servent deux fois : balisés à la main selon la forme imposée (cas sains, nombre attendu inchangé), et tels quels (sans balise : « non conformes » attendus, c'est le piège « H_A et H_B sans balise »).
- **Ajouté pour la règle R5.** Trois mutations de la règle, chacune retirant une condition écrite à l'article 4 (compte de la clôture, ancrage en début de ligne, clôture unique), doivent faire échouer l'épreuve. Cinq suppléments hors verdict décrivent des cas de bord que l'article 4 tranche aussi.

## Protocole

- Textes et verdicts : `textes-epreuve-balises-v5-v1.json` (sha256 4346f288ad5ab22343853617bb2effe0a907e790caa6c7c96fdda6f73cb1d916), écrits par Opus 5.5 et scellés avant la première exécution de la règle. Verdicts fixés d'après le texte de l'article 4 de la v5. **Réserve** : leur auteur a lu la pièce et la règle ; ce lot montre que le code suit le texte de l'article 4, pas que les modèles écriront des tours conformes.
- Anciens textes : lus dans `epreuve_motifs_correction_28_v2.py` (sha256 d1caea7b…) par analyse syntaxique, sans l'exécuter.
- Épreuve aveugle : `epreuve_aveugle_v5_v1.py` (sha256 1422e08e14dbb89900c3f0472eb7c72b4a238c70dedadbba975187d6ba960080), mêmes textes que la v1 et la v2 (`textes-aveugles-epreuve-v1.json`, sha256 1dbdcb40…) ; l'ancienne règle compte la longueur de la liste des ouvertures, non celle du couple rendu (l'erreur de la v1).
- Codes de sortie : 0 pour les deux scripts.

## Constats sans changement de texte

- **Reste de ligne.** Une balise en gras (« **[DUEL 1]** ») laisse « ** » comme première ligne du duel (piège 7). Sans effet sur les mots pleins de l'article 5 ; noté seulement.
- **Préfixe admis.** « 1. [DUEL 1] » (liste numérotée), « `[DUEL 1]` » (accents graves) et « [Duel 1] » (casse) ne sont pas reconnus : tour non conforme (suppléments 1 à 3). La consigne de Fable demande la balise « seule sur sa ligne » ; ce que valent ces formes chez les modèles, seul le lot aveugle le dira.
- **Limite déclarée.** Un duel omis avec un compte ajusté passe inaperçu et se fond dans le duel précédent (supplément 4), comme l'article 4 l'écrit.
- **Espace insécable.** « [FIN DES DUELS : 2] » avec une espace insécable avant le deux-points est reconnu (sain 10).

## Sortie brute — épreuve des balises (`python3 -I epreuve_motifs_v5_v1.py`)

~~~
motifs de l'article 4 identiques à ceux du code de référence : True
  ouverture : ^[\s>#*_|-]*\[DUEL\s*(\d+)\]
  clôture   : ^[\s>#*_|-]*\[FIN DES DUELS\s*:\s*(\d+)\]

CAS SAINS : 10/10 au verdict attendu
  sain 1 (ancien texte 1, tour III.1, liste numérotée) : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : 1. Expérience 1. H_A : la sonde détecte le sabotage diffus ; contre H_B : elle n
      duel 2 : 2. Expérience 2. H_A : le score croît avec la longueur de l'épisode ; contre H_B
  sain 2 (ancien texte 2, titres de duel) : attendu conforme, n = 3 ; obtenu conforme, n = 3 : PASSE
      duel 1 : #### Duel 1
      duel 2 : #### Duel 2
      duel 3 : #### Duel 3
  sain 3 (ancien texte 3, plusieurs H_A par duel) : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : **Expérience 1 : H_A contre H_B**
      duel 2 : **Expérience 2 : H_A contre H_B**
  sain 4 (ancien texte 4, tour III.3, renvoi « duel 1 » sans crochets) : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : ### Duel 1 (corrigé) — H_A contre H_B
      duel 2 : ### Duel 2 (corrigé) — H_A contre H_B
  sain 5 (ancien texte 5, H₁ contre H₂, balises dans une liste indentée) : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : - Expérience 1 : H₁ contre H₂.
      duel 2 : - Expérience 2 : H₁ contre H₂.
  sain 6 (ancien texte 6, un duel, sans section (c)) : attendu conforme, n = 1 ; obtenu conforme, n = 1 : PASSE
      duel 1 : - Duel unique. H_A : l'audit à 2 % suffit ; H_B : il ne suffit pas. Métrique : d
  sain 7 (ancien texte 7, H_A en section (c)) : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : - Duel 1. H_A : la collusion élève les scores ensemble ; H_B : les scores resten
      duel 2 : - Duel 2. H_A : le juge d'une autre lignée résiste ; H_B : il cède comme les aut
  sain 8 (ancien texte 8, balise et duel sur la même ligne) : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : Duel 1 : HA, le moniteur est contourné par paraphrase ; HB, il ne l'est pas. Seu
      duel 2 : Duel 2 : HA, la détection baisse avec la longueur ; HB, elle reste stable.
  sain 9 (ancien texte 9, H_A et H_B en section (a)) : attendu conforme, n = 3 ; obtenu conforme, n = 3 : PASSE
      duel 1 : 1. H_A : le signal est dans les activations ; H_B : il est dans le texte seul. S
      duel 2 : 2. H_A : le signal survit au changement de famille ; H_B : non.
      duel 3 : 3. H_A : l'effet croît avec la dose ; H_B : il est plat.
  sain 10 (ancien texte 10, duels en paragraphes, espace insécable avant le deux-points) : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : Expérience 1. On oppose H_A, selon laquelle le saboteur informé contourne la son
      duel 2 : Expérience 2. On oppose H_A, selon laquelle l'audit au hasard borne le dommage,

PIÈGES : 8/8 au verdict attendu
  piège 1 : balise omise : attendu non conforme ; obtenu non conforme : PASSE
  piège 2 : numéro sauté : attendu non conforme ; obtenu non conforme : PASSE
  piège 3 : clôture absente : attendu non conforme ; obtenu non conforme : PASSE
  piège 4 : clôture double : attendu non conforme ; obtenu non conforme : PASSE
  piège 5 : clôture au mauvais compte : attendu non conforme ; obtenu non conforme : PASSE
  piège 6 : balise citée en cours de phrase : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : - H_A : l'audit suffit ; H_B : il ne suffit pas.
      duel 2 : - H_A : le juge résiste ; H_B : il cède, comme on le verra après le [DUEL 1] du 
  piège 7 : balise en gras ou en titre : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : **
      duel 2 : - H_A : le juge résiste ; H_B : il cède.
  piège 8 : H_A et H_B sans balise : attendu non conforme ; obtenu non conforme : PASSE

ANCIENS TEXTES SANS BALISE : 10/10 au verdict attendu
  ancien texte 1 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 2 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 3 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 4 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 5 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 6 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 7 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 8 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 9 sans balise : attendu non conforme ; obtenu non conforme : PASSE
  ancien texte 10 sans balise : attendu non conforme ; obtenu non conforme : PASSE

SUPPLÉMENTS (hors verdict) : 5/5 au verdict attendu
  supplément 1 : balise après un numéro de liste « 1. [DUEL 1] » : attendu non conforme ; obtenu non conforme : PASSE
  supplément 2 : casse « [Duel 1] » : attendu non conforme ; obtenu non conforme : PASSE
  supplément 3 : balise entre accents graves : attendu non conforme ; obtenu non conforme : PASSE
  supplément 4 : duel omis avec compte ajusté (limite déclarée) : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : - H_A : l'audit suffit ; H_B : il ne suffit pas.
      duel 2 : - H_A : le juge résiste ; H_B : il cède.
  supplément 5 : cellule en anglais, balises inchangées : attendu conforme, n = 2 ; obtenu conforme, n = 2 : PASSE
      duel 1 : - H_A: the probe reads sabotage; H_B: it reads the topic.
      duel 2 : - H_A: the signal is concentrated; H_B: it is spread.

reste de la ligne d'ouverture compris dans le duel (sain 8) : True (' Duel 1 : HA, le moniteur est ')

MUTATIONS (chacune doit échouer)
  compte de la clôture ignoré : 3 cas au mauvais verdict : mutation détectée
  motifs sans ancrage en début de ligne : 1 cas au mauvais verdict : mutation détectée
  clôtures multiples admises (la première compte) : 1 cas au mauvais verdict : mutation détectée

RÉSULTAT : PASSE
~~~

## Sortie brute — épreuve aveugle dans la forme de la v2 (`python3 -I epreuve_aveugle_v5_v1.py`)

~~~
RÈGLE 1 — ancienne règle de la v4 (sortie brute)
texte 1 : attendu 3, obtenu 5, section (b) lignes (6, 26) : ÉCHOUE
    ouverture : - H_A : la sonde détecte le sabotage indépendamment du sujet de la tâche.
    ouverture : - Seuil : 0,70. Si H_A est vraie, l'aire reste au-dessus de 0,70 une fois le sujet apparié ; sous H_
    ouverture : - Falsification : une aire < 0,55 sur les paires appariées réfute H_A ; une aire > 0,70 avec permuta
    ouverture : - Falsification : rappel de H_A — si aucune couche ne dépasse 0,05, H_A tombe ; si une couche dépass
    ouverture : - H_A : l'aire est stable (écart < 0,03) quand la consigne est paraphrasée ; H_B : elle chute de plu
texte 2 : attendu 3, obtenu 4, section (b) lignes (8, 17) : ÉCHOUE
    ouverture : | # | H₁ | H₂ | Métrique | Seuil | Contrôle négatif | Ce qui falsifie |
    ouverture : | 1 | Le juge d'une autre lignée détecte mieux que le juge de même lignée | Les deux juges ont le mê
    ouverture : | 2 | La conscience d'évaluation fait baisser le sabotage | Elle ne change rien | Taux de sabotage a
    ouverture : Duel 3 : H₁ = la couverture de 0,92 suffit à dater le dommage, H₂ = il faut l'extrait cité vérifié p
texte 3 : attendu 2, obtenu 0, section (b) lignes (6, 9) : ÉCHOUE
règle 1 : 0 sur 3

RÈGLE 2 — article 4 de la v5 (balises)
texte 1 : attendu non conforme ; obtenu non conforme : PASSE
texte 2 : attendu non conforme ; obtenu non conforme : PASSE
texte 3 : attendu non conforme ; obtenu non conforme : PASSE
règle 2 : 3 sur 3 au verdict attendu (non conforme)
~~~
