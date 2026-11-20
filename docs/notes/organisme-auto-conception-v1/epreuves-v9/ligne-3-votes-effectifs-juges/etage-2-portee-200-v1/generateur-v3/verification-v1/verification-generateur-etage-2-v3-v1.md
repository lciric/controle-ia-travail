# Vérification du générateur de l'étage 2 à 200 (ligne 3) — v3 — v1

Pièce de travail (classe C), 2026-11-20, par le contre-lecteur neuf, modèle S, sous le mandat `83711f92e5308584c8f8a85d47f52c16ae9ce50250d0000af947aff437db7402` (en-tête compris). Suite de `contre-lecture-generateur-etage-2-v1.md` (`d3b72675…`) et de `verification-generateur-etage-2-v2-v1.md` (`4532e695…`). Le fichier des cartes n'a été ouvert ni par moi, ni par un programme que j'ai lancé ; rien sous `archives-reponses-modeles/` ; aucun appel à un fournisseur, aucune clé, aucune écriture dans le dépôt ni dans le clone.

## Verdict : Conforme

Les cinq décisions de la mère sont portées ; rien d'autre ne change ; 101 essais passent ; l'ordre « tout avant l'unique ouverture » est tenu ; la répartition des pièces sous le second déclencheur est conforme au texte. Trois remarques non bloquantes (R1 à R3, § 6).

## 1. Table et pièces

`table-empreintes-generateur-v3.txt` (`8e87f2bd51178a2f87ab9f296a7533864a1894df7c98740b0b6fe153fc79b412`) : compagnon égal ; les six lignes recalculées égales : programme `f5de9c3c94be525d1ec48d3e7954135473894a298aafe908475f043934278ae0`, essais `7e064c90fe90a79ee9336b968c141b569b608df865e58ec25a00ff227a741a0f`, fragments `a66cf6d4…` (octets identiques à v1 et v2), différentiels `b88de2f0…` et `04be8ad2…`, rapport `f677bd08…`.

## 2. Essais : lecture d'abord, puis rejeu

Lu avant tout lancement (`essais_generer_temoins_ligne_3_v3.py`) :
- **Cartes** : le chemin réel n'apparaît que dans une comparaison de chaînes (l. 830-831) ; `EntreeCartes.production()` est construite, jamais lue (l. 834-835). Les garde jouées passent par `EntreeCartes.essai` (l. 159, 1128). Les appels de `principal(["garde", …])` sans entrée explicite (l. 1101, 1106) ont `jouer_la_garde` remplacée par une fonction qui lève. `principal(["creer-journal-rejeux", "--journal", …])` (l. 665) est refusé par `len(argv) != 1` avant toute création (programme, bloc `try` du geste).
- **Git** : tous les essais qui touchent à git le font dans des dossiers temporaires du système, par `GIT_ESSAI` (`git -c user.name=… -c commit.gpgsign=false`) : `initialiser_depot(d)` (l. 116-121 : `git init` et une validation vide dans `d`) ; l'artefact (l. 1217-1226) et le cas « hors dépôt » (l. 1233) sur `mkdtemp`. `historique_connait` n'est jamais appelée avec `DEPOT` : `lieu(dossier)` passe `depot=dossier` (l. 113) ; la voie de production (`LieuDuJournal.production()`, l. 670) est seulement construite. Aucun `git` n'est lancé dans le dépôt de travail. Aucune commande de réseau (`init`, `commit`, `add`, `rm`, `log` seulement).
- **Réseau** : l'essai M6 (l. 1189-1195) bloque `socket.socket` et `socket.create_connection` et coupe les mandataires, comme en v2.

Rejeu sur copie (`copie-G3/`), Python 3.13.18 : **101 passed in 10.69s** (`sortie-essais-v3-rejoues-v1.txt`).

## 3. Différentiels refaits : rien d'autre ne change

`diff -u` des couples v2 → v3 refaits par moi (`diff-programme-v2-v3-refait-v1.diff`, `diff-essais-v2-v3-refait-v1.diff`) : corps identiques à ceux du développeur, hors les deux lignes d'en-tête (271 et 293 lignes ; `comparer_differentiels_v3_v1.py`, `sortie-comparaison-differentiels-v3-v1.json`). Lu en entier, le différentiel du programme ne contient que les neuf rubriques du rapport § 3 : la comparaison des bardeaux, le rapport, le repli, le compte et le refus au sixième rejeu, l'audit, la composition ne sont pas touchés. Le différentiel des essais ne retire d'assertion que celles de ce qui change : cartes à clé `id` (forme liste), essai des « formes admises » (devenu « forme réelle seule »), identifiants plus longs que le nom de repli, texte de la pièce du (4) sans portée.

## 4. Les cinq décisions

1. **Historique git** (`historique_connait`, diff l. 150-165) : `git -C DEPOT log --all --format=%H -- <chemin relatif>`, lecture seule, `stdin` fermé, délai 120 s ; sortie non vide → `ManifesteJournalConnuDeLHistorique` ; chemin hors dépôt, git absent ou code de retour non nul → `HistoriqueGitIllisible`, sans repli. Ordre dans `creer_journal_rejeux` : manifeste présent (v2) → historique → journal présent sans manifeste → création. `--all` couvre aussi les références distantes déjà tirées, ce qui répond à ma remarque R2 de la v2 à condition que le manifeste ait été poussé (voir R1). Essais : sain, artefact (validé puis retiré), hors dépôt.
2. **Forme réelle seule** (`cartes_du_fichier`) : objet non vide, clés de treize caractères, valeurs objets portant un `contenu` objet ; sinon `FormatCartesInconnu` avant toute comparaison ; repli par égalité exacte. La forme est celle que j'ai établie en v1 (`course2_v56.py:366-367`, identifiants `"f"` + 12 hexadécimaux, `course2_v53.py:246, 428`, `course2_v56.py:217`, `graines_v53.py:65-67` ; `contenu` dictionnaire : `fiches_v53.py:31-32`). Risque résiduel : un identifiant qui ne ferait pas treize caractères coûterait une ouverture comptée ; je n'en vois aucun dans le code de l'organisme.
3. **Portée** (`LIGNE_PORTEE`, `exiger_controle_conforme(…, repli)`) : exactement une valeur dans la pièce (deux lignes identiques passent, deux valeurs différentes ou aucune → `ControleQuatrePorteeAbsente`) ; « garde entière » sans `--repli`, « repli seul » avec → sinon `ControleQuatrePorteeAutre`. Essais : quatre formes saines, cinq artefacts, tous avant l'ouverture.
4. **Journal existant sans manifeste** : `JournalExisteSansManifeste` ; à la ligne de commande, toute exception du geste ne rend que `{"refus": classe, "ligne": n}` sur la sortie d'erreur (ma remarque R3 de la v2 est close).
5. **Lecture unique de la pièce du (4)** (`_lire_piece`) : octets lus une fois, empreinte vérifiée sur ces octets, analyse de ces mêmes octets ; l'essai (l. 1285-1305) interdit toute seconde lecture et tout recalcul sur disque.

## 5. Écart déclaré : cause du repli et pièce vérifiées avant la pièce du (4)

Dans `jouer_la_garde` (diff l. 240-250), le bloc « cause dans les deux déclencheurs ; pièce du déclencheur par chemin et empreinte » précède maintenant `exiger_controle_conforme`, qui reçoit `repli`. L'ordre complet reste : dossier de sortie, manifeste de création (`exiger_manifeste_du_journal`), journal, [repli : cause et pièce], pièce du (4) à verdict et à portée, mot de la mère et refus au sixième rejeu, lecture de la banque, de la seconde entrée, écriture du manifeste de la garde, ligne « ouverture », puis l'unique `lire_octets`. **Tout est donc encore avant l'unique ouverture** ; le changement ne fait qu'ordonner les refus (la portée dépend de la validité du repli). Aucun refus n'est perdu : seul le nom de la classe rendue peut changer quand deux fautes coexistent. Conforme.

**Répartition des pièces sous le second déclencheur** : la pièce « Portée : repli seul », qui porte « Conforme » et l'empreinte du programme, va à `--controle-4` ; la pièce du déclencheur (le « non conforme » sur l'entrée des 94 cartes) va à `--piece-repli`, vérifiée par chemin et empreinte seulement (le code n'y exige ni « Conforme » ni absence de « Non conforme »). C'est la lecture du texte l. 263 : le déclencheur est le « non conforme » sur l'entrée ; sous le repli, la garde ne tourne que si la contre-lecture a rendu « conforme », par écrit, les autres points et le chemin du repli, ce que dit la pièce « repli seul ». Elle vaut aussi pour le premier déclencheur (refus écrit de la mère en `--piece-repli`). Conforme.

## 6. Remarques non bloquantes

- **R1 (pour la mère)** : le refus par l'historique ne vaut que pour les commits connus du clone au moment de la création. Pousser le manifeste dès sa création et le journal après chaque passage reste nécessaire (ma R2 de la v2) ; en cas de dépôt recloné, `git fetch` avant tout `creer-journal-rejeux`. Un `git` indisponible ou un propriétaire de dépôt jugé douteux par git (code de retour non nul) donne un refus nommé : sûr, mais à savoir au jour de la création.
- **R2** : sous le repli, la pièce « repli seul » est soumise à la règle « aucune ligne commençant par Non conforme » : le contrôleur ne doit pas y recopier, en début de ligne, le « Non conforme » du déclencheur ; la pièce du déclencheur est un fichier à part. À dire au contrôleur avec la forme de la ligne de portée (rapport § 1).
- **R3** : deux lignes de portée identiques sont admises ; une seule valeur par pièce est la règle écrite. Sans conséquence.

## 7. Écarts de cette vérification

1. Un `ls` du dossier du générateur v3 (désigné par le coordinateur).
2. Deux `diff -u` de fichiers du dépôt, redirigés vers mon dossier ; un `grep -n "^-"` et un `grep -c` sur des différentiels du dépôt (lecture).
3. Copie de G3 dans `copie-G3/` ; les essais ont écrit, dont des dépôts git d'essai, sous le dossier temporaire du système.

## 8. Pièces de ce dossier

`verification-generateur-etage-2-v3-v1.md` ; `sortie-essais-v3-rejoues-v1.txt` ; `diff-programme-v2-v3-refait-v1.diff`, `diff-essais-v2-v3-refait-v1.diff` ; `comparer_differentiels_v3_v1.py`, `sortie-comparaison-differentiels-v3-v1.json` ; `copie-G3/` (travail). Chaque pièce a son compagnon `.sha256` ; `table-empreintes-verification-v3-v1.txt` en donne la liste.

Contre-lecteur, modèle S.
