# Relecture du seul différentiel v1 → v2 de la commande de la tranche B-α de « Neuron Lens » — v1

**Verdict : à corriger.** Un seul point bloque (P1, deux phrases de texte) : la règle « prévenir la mère et attendre son signal »,
ajoutée en v2 devant toute destruction manuelle, laisse l'instance facturée **sans aucun automate armé** pendant l'attente dans trois
branches d'échec (étapes 7, 8 et 9). Tout le reste du différentiel est conforme : M1, M2, M3 et les dix-huit mineurs sont portés, aucun
changement hors du différentiel déclaré, rien de dégradé sur les clés, la destruction ni la preuve d'absence. Si la mère préfère ne pas
refaire de version, P1 peut être porté mot pour mot dans son feu écrit ; c'est à elle de le dire.

Lecteur neuf (n'a écrit ni le texte gelé, ni le devis, ni les pièces, ni les commandes), le 2026-11-15, sur la copie détachée
`/home/user/relecture-commande-b-alpha-v2` (branche `prep/neuron-lens-v1`, commit `1bb1ba17`). Lecture seule ; aucune location, aucun
appel au loueur, aucune valeur de clé lue, rien ouvert sous `donnees/` ni `docs/verdicts/`, aucun commit, aucune poussée, aucun code du
dépôt voisin exécuté. Seuls gestes hors lecture : `diff`, `sha256sum`, un contrôle de syntaxe (`bash -n`, sans exécution) des deux
gestes nouvellement écrits, une ligne d'arithmétique, une lecture de la liste des processus.

## 0. Empreintes (fichier recalculé contre son compagnon)

| pièce | sha256 | compagnon |
|---|---|---|
| `docs/notes/neuron-lens-v1/commande-b-alpha-v1.md` | `633e193f54f253ceeee835381a97b778d456390c18ece4119a853aaac362cfc7` | égal |
| `docs/notes/neuron-lens-v1/commande-b-alpha-v2.md` | `cf437d9532799d0f6871a1a211e3c46742ec122bfba39b7344829e990552cd66` | égal |
| `docs/notes/neuron-lens-v1/devis-b-alpha/verification-courte-devis-v2-et-pieces-b-alpha-v1.md` | `e68d6f1496b88f2655cae92e95a7e4a2d8ddf476db10440d3db811f92f9fa116` | égal |

Pièces de code lues, égales aux empreintes du tableau de la commande v2 (l. 247 à 259) : lanceur `99a3eb9d…`, amorce v3 `ffe371c8…`,
partie 2 `1cedde7e…`, dépôt réduit v4 `d2f85d19…`, garde de dépense v4 `6a98d816…`, minuterie v4 `45113683…`, suivi v6 `2ecaaeed…`.
Décision R-2885 lue (`registres/decisions.md`, l. 2845) ; règle R-2864 lue (l. 2824).

## 1. Point bloquant

**P1 — Attente du signal de la mère sans aucun automate armé (commande v2, l. 82, 83-84, 95, avec l. 165).** En v1, un échec à
l'étape 7 (instance créée mais sortie non conforme), à l'étape 8 (prix lu au-dessus de la borne) ou à l'étape 9 (minuterie non armée)
menait à la destruction immédiate. En v2 ces trois branches renvoient à l'étape 15, qui commence par « Prévenir la mère (R-2864) et
attendre son signal » (l. 165). Or à ces trois moments ni la minuterie (étape 9) ni la garde (étape 10) ne sont encore posées, et la
règle R-2864 fait dépendre le signal de la mère d'un mot de Lazar (`registres/decisions.md`, l. 2824 : la mère « prévient Lazar et
attend son signal ») : l'attente peut durer, l'instance est facturée, et rien de mécanique ne tient le plafond de 12 USD pendant ce
temps. C'est une dégradation de la borne d'argent introduite par le différentiel, non voulue par lui.
- ancien (v2, l. 82, 84, 95) : « destruction éventuelle selon l'étape 15, message » ; « destruction selon l'étape 15 et message » ;
  « Non armée → destruction selon l'étape 15, message ».
- nouveau proposé : ajouter, après la règle R-2864 de l'en-tête (l. 34-36) ou à chacune des trois lignes : « **Avant d'attendre le
  signal, poser les automates manquants** : la minuterie de l'étape 9 puis la garde de l'étape 10, au prix lu sur l'instance (ou, si
  le prix n'a pas pu être lu, au prix de l'offre retenue à l'étape 4) ; si la minuterie ne s'arme pas, la garde seule ; le message à la
  mère dit quels automates sont vivants. L'attente ne commence qu'ensuite. » Les automates ne sont pas concernés par R-2864 (l. 36) :
  ils détruisent à leur échéance même si le signal ne vient pas.
- Sans effet sur le chemin nominal (aucune destruction manuelle avant l'étape 15, où les deux automates vivent déjà).

## 2. Les sept points demandés

**(1) Différentiel exact.** `diff` v1 → v2 : vingt blocs. Chacun se rattache au différentiel déclaré en tête (v2, l. 3-21) :
en-tête et titre (l. 1-21) ; M2 (l. 26, 49, 83, 94, 106, 222-224) ; M1 (l. 53-54, 71, 77-78) ; R-2864 (l. 34-36, 66, 104, 165) ;
M3 et mineur 3 (l. 129-132) ; mineur 1 (l. 45, 82, 84, 95) ; mineur 2 (l. 96-105, 108-119) ; mineur 15 (l. 59-61) ; mineur 12, première
moitié (l. 76) ; mineur 8 (l. 124) ; mineurs 7, 11, 10 (l. 142-148) ; mineur 4 (l. 189-190) ; réserves (l. 205-220) ; deux lignes
d'empreintes ajoutées (l. 229-230, égales aux fichiers). **Aucun autre changement** : la ligne de création ne diffère de la v1 que par
l'ajout de `-e COMMIT_SOURCE=<COMMIT_SOURCE>` ; image, disque, étiquette, entrée, bloc d'authentification, branche, suivi : inchangés
au caractère près.

**(2) M1 — porté, lecture conforme à ce que le lanceur attend.** Défini à l'étape 5 (l. 53-54 : commit complet, 40 caractères, de
`prep/neuron-lens-v1`, le même jeton `<COMMIT_SOURCE>` que l'argument du dépôt réduit) ; transmis à l'étape 7 (l. 71). Chaîne lue dans
le code : la variable est posée sur le conteneur comme `COMMIT_REDUIT` ; l'entrée fait `exec bash` de l'amorce (hérité) ; l'amorce v3
ne la retire nulle part (les `unset` et `env -u` ne visent que `GH_TOKEN`, `HF_TOKEN`, `HUGGING_FACE_HUB_TOKEN`, `HF_HUB_OFFLINE` :
l. 225-247, 265-266, 274, 289) ; `appel` est un sous-shell (l. 264-270) et `lanceur` un appel direct de l'interprète (l. 84) : la
variable, déjà dans l'environnement, passe ; le lanceur la lit dans son propre processus, `os.environ.get("COMMIT_SOURCE", "")`
(l. 568, dans `releve_partie2`, appelé par `etape_partie2`, l. 582-584) ; la partie 2 exige 40 caractères hexadécimaux (l. 75-77) ; la
garde d'environnement du lanceur (l. 139-166) ne refuse pas une variable de plus. Le dépôt réduit v4 normalise le commit reçu par
`git rev-parse` (l. 94) et l'écrit dans `rapport.json` (`commit_source`, l. 134) et dans le message du commit réduit (l. 125).
Réserve R1 ci-dessous : l'égalité entre la valeur de l'étape 7 et celle de l'étape 5 ne repose que sur la main.

**(3) M2 — porté.** Filtre de la recherche `dph_total<=0.79` (l. 49) ; prix relu sur l'instance, « ≤ 0,79 exigé », stockage compris
(l. 83) ; rappel à 9,2 h (l. 106) ; devis de la commande (l. 223) : 13,5 h × 0,79 = 10,665, soit 10,67 USD, sous 10,80. Minuterie :
la garde v4 calcule `int((0,90 × 12 − 0) / 0,79 × 3600)` (l. 48-51) = **49 215 s** (recalculé ; 85 506 s à 0,4547 : recalculé), soit
13,67 h, dans les bornes 600 à 129 600 s ; le pire cas de 13,5 h vaut 48 600 s, 615 s avant l'échéance. Cohérent avec 0,79 et 12 USD.
Réserve R2 ci-dessous sur le sens de « pire cas ».

**(4) M3 — écrit** (l. 129-131), dans les mots de la vérification courte, avec le renvoi au point (b) et au nœud de Lazar ; conforme à
R-2885 (le champ ne vaut pas verdict avant le mot de Lazar ; les trois écarts sont versés).

**(5) Mineurs — tous portés.** 1 : l. 45, 82, 84, 95 (plus aucun renvoi de destruction à l'étape 13). 2 : garde l. 96-105, identique au
geste de la commande v14 (l. 204-213 de celle-ci) aux noms de fichiers et à `--plafond 12` près ; veille l. 108-119. 3 : l. 131-132.
4 : l. 189-190. 5 : en tête seulement (l. 17-18) ; à ma lecture de la liste des processus, aucun `sleep 129600`. 6 : l. 211. 7 : l. 142-143.
8 : l. 124. 9 : l. 211-212. 10 : l. 146-148. 11 : l. 144-146. 12 : l. 76 et l. 212-213. 13 : l. 213. 14 : l. 213-214. 15 : l. 59-61.
16 : l. 206-210. 17 : l. 214-215. 18 : l. 215-217. Points (a), (c), (d) : l. 218-220.

**(6) Argent, clés, destruction, preuve d'absence.** Clés : `HF_TOKEN` et le jeton du programme par leur nom seulement, aux mêmes
endroits qu'en v1 (l. 41, 71) ; aucune valeur ; l'exposition de quelques secondes dans les arguments du processus de création est
maintenant déclarée (l. 76). Destruction manuelle : toujours par identifiant, avec `-y`, entrée fermée (l. 166) ; preuve d'absence par
le suivi avec témoin, code 0 exigé (l. 166-167) : inchangées. Garde : plafond 12, 7,20 et 10,80 (l. 104-105). Intouchables inchangés
(l. 31-32). **Dégradé : la seule borne d'argent des branches d'échec, P1.**

**(7) Préavis à la mère — écrit** : règle en tête (l. 34-36) ; avant la création (l. 66) ; avant toute destruction manuelle (l. 165 ;
les étapes 7, 8, 9 et 10 y renvoient, l'étape 10 le redit, l. 104) ; les automates armés exceptés, comme le veut la règle. Réserve R3.

## 3. Réserves non bloquantes

- **R1 (M1, l. 53-54 et 71).** Rien de mécanique n'assure que la valeur passée à l'étape 7 est celle de l'étape 5 : une autre suite de
  40 caractères hexadécimaux passerait la partie 2 sans écart et fausserait la provenance. Proposé, sans nouveau code : à l'étape 7,
  recopier `commit_source` et `commit_reduit` depuis le `rapport.json` de l'étape 5, et le dire dans la consigne de `pids-b-alpha-v1.txt`.
- **R2 (M2, l. 124, 211 et 223).** « Pire cas complet 13,5 h » est la somme du devis ; les bornes réellement codées sont plus
  larges, et la commande v2 le déclare en deux endroits sans refaire la somme : amorce 2 h au lieu de 1,5 h (deux fois, course et
  réinstallation), étape 7 du devis 1,0 h au lieu de 0,8 h. Somme des bornes codées : 9,9 + 2,0 + 2,8 = 14,7 h, soit 11,61 USD à 0,79 :
  au-dessus de l'arrêt dur. **L'argent reste borné** (garde à 10,80, minuterie à 49 215 s) ; ce qui change est la phrase : dans ce cas
  extrême la course serait coupée par l'arrêt dur avant sa fin, elle ne « tient » pas dessous. La décision de R-2885 (0,79) a été
  prise sur 13,5 h ; à la mère de dire si la phrase suffit (les bornes codées tiendraient sous 10,80 à 0,73 USD/h au plus ; sans effet
  au prix du jour, voisin de 0,50 : 7,35 USD).
- **R3 (l. 153-157 contre l. 165).** Le tableau de l'étape 13 dit « aussitôt, selon l'étape 15 » alors que l'étape 15 commence par
  l'attente du signal : « aussitôt » se lit désormais « sans autre condition que le signal ». À écrire à la prochaine version.
- **R4 (veille, l. 108-119).** Le geste est neuf (la v14 n'en avait pas) et n'a été joué nulle part ; sa syntaxe passe (`bash -n`), sa
  logique est lue juste (24 tours de 300 s, PID relu dans le fichier, nom du script cherché dans les arguments). Elle **consigne** une
  mort, elle ne réarme pas : la v1 disait « veille qui réarme » ; en v2 le réarmement est un geste de la session à la lecture du
  journal (l. 118-119). La veille meurt avec le conteneur de la session comme les automates qu'elle surveille : ce sont les rappels de
  l'étape 11 et le contrôle de l'étape 13 qui rattrapent. Déclaré ici, sans effet sur le feu.
- **R5 (en-tête, l. 19-20).** L'en-tête dit les mineurs 8, 12 et 15 « regroupés en fin de commande » ; ils sont portés à leur étape
  (l. 124, 76, 59-61). Tous y sont ; seule la phrase de l'en-tête est inexacte.
- **R6 (l. 96-97).** « (P, puis) : » est une coquille pour « préambule P, puis : » ; sans effet.

## 4. Ce que je n'ai pas vérifié
Le prix du jour, le crédit, l'état des instances témoins (aucun appel au loueur) ; la transmission réelle des variables par l'outil du
loueur (lue par analogie avec `COMMIT_REDUIT`, que l'amorce exige déjà) ; la simulation de la partie 2 citée l. 77-78 (non rejouée : je
m'en tiens à la lecture du code) ; la veille et la garde en vrai.
