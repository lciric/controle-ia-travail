VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-I -B`

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DU DOSSIER DU GÉNÉRATEUR. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

**AUCUNE COMMANDE, D'AUCUNE SORTE, SUR UN CHEMIN SOUS `archives-reponses-modeles/`. LE FICHIER DES CARTES N'EST JAMAIS OUVERT. TU N'EXÉCUTES PAS LA GARDE ; TU LIS SON CODE.**

# Mandat du contrôleur de la condition (4) de la garde de recouvrement (ligne 3, étage 2) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur la lettre du texte de la ligne 3 v7 (`4e3680d9…`), ligne 261, condition (4) : « Ces points sont contrôlés dans le code par le vérificateur, agent du modèle O qui n'a pas écrit le code […] ; sans ce contrôle passé et écrit, la garde ne tourne pas et la banque n'est pas scellée. » Et sur l'accord de la mère (14:23Z : « un Opus neuf contrôle la condition (4) »).

## Qui

Un agent neuf, modèle O, qui n'a écrit ni ce générateur, ni le code d'appel, ni le texte de la ligne 3. Tu signes « contrôleur de la condition (4), modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- Le texte v7 : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9…`), lignes 257 à 263 (conditions (1) à (5) et repli).
- Le programme : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/generateur-v1/generer_temoins_ligne_3_v1.py` (`b264760c…`) et le rapport du développeur (`c447ed60…`), § 5 « Points de la condition (4) ».

## Ce que tu contrôles, ligne par ligne du code (à la lettre de la condition (4))

1. **L'entrée unique** : chemin, empreinte `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481` et compte de 94 vérifiés **avant tout usage** ; aucun autre chemin de l'archive ne peut être ouvert (ni par argument, ni par variable d'environnement, ni par une voie d'essai) ; la voie d'essai ne peut pas atteindre le vrai fichier.
2. **Le retrait du champ `meta`** avant tout usage (et à quelle profondeur ; dis si c'est suffisant au sens du texte).
3. **L'absence de toute écriture d'un bardeau ou d'un texte de carte**, messages d'erreur et traces d'exception compris : suis chaque voie de sortie (fichiers, journal, manifeste, rapport, sortie standard, sortie d'erreur, exceptions, avertissements, `repr` d'objets).
4. **La liste fermée des champs de sortie** : chaque écriture passe par la validation ; aucune voie ne la contourne.
5. **Le compte des rejeux** : journal à ajout seul lu au lancement ; absent ou illisible → refus avant l'ouverture ; **refus au sixième rejeu** sans le mot de la mère ; le premier passage n'est pas un rejeu ; toute exécution suivante qui ouvre le fichier en est un.
6. **Le chemin du repli** : ses deux déclencheurs seulement ; mêmes règles.

Pour chaque point : « tenu » ou « non tenu », avec fichier:ligne et la raison. Tu peux écrire et lancer un petit programme d'analyse **statique** du code (lecture du texte du programme, arbre syntaxique) ; tu ne lances ni la garde, ni le générateur, ni ses essais.

**Verdict** : « Conforme » (la garde peut tourner une fois la banque prête) ou « Non conforme » avec, pour chaque point, ce qui manque. Le texte dit : sans ce contrôle passé et écrit, la garde ne tourne pas.

Écris `controle-condition-4-garde-recouvrement-v1.md` et son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`) dans `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/controle-condition-4/`.

## Interdits

Voir en tête. Aucun appel à un fournisseur de modèles, aucune dépense, aucune clé lue. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
