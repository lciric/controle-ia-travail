# Rapport du rédacteur — additif 6, additif de code de l'étage 2 à 200 (ligne 3, organisme v9) — v1

Pièce de travail (classe C), écrite le 2026-11-20 (`date -u` : 16:25Z) sur le mandat `mandat-redacteur-additif-code-etage-2-v1.md` (`a9663af401d1fcebfcaf626f2de104847ad44492760b98054cb1ae8478220695`, recalculée sur son seul chemin, en-tête compris). Rédacteur neuf, modèle F : je n'ai écrit ni le texte de la ligne 3, ni ses additifs, ni aucun code, fragment, vérification ou contrôle de l'étage 2.

## 1. Ce qui est rendu

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-code-etage-2/`.

- `additif-6-code-etage-2-preenregistrement-ligne-3-v1.md`, statut « non scellé », et son compagnon.
- Ce rapport et son compagnon.
- Pièces de travail, hors de la pièce : les copies tirées de `origin/main` par `git show` redirigé (`main-go.md`, `main-decisions.md`, `main-additif-3-v3.md`, `main-additif-5-v2.md` et son compagnon, `main-verdict-portee-200-v2.md`) ; `sonde_interpreteur_v1.py`.

Rang 6 : les additifs 1 à 5 existent pour la ligne 3 ; le nom du fichier n'existe pas sur `main` (contrôle sur ce seul chemin, sans liste).

## 2. Choix portés par l'additif

- **Interpréteur** : `/usr/local/bin/python3 -I -B`, Python 3.13.18, numpy 2.5.3, pour tous les gestes. Raison décisive : le kit d'agent de l'adaptateur du juge Opus est présent sous cet interpréteur et absent de celui de l'environnement du dépôt (numpy 2.4.6), sous lequel les essais ont été joués.
- **Chemins** : `X` = `E/execution-v1` ; **DOSSIER** = `E/execution-v1/etalonnage-et-lecture` (un seul chemin absolu, dans le dépôt) ; sortie des appels `S` = `/home/user/sorties-ligne-3-etage-2-portee-200-v1`, hors du dépôt. Tous absents du disque. Placés par moi : à confirmer.
- **Ordre et commandes** : création du journal des rejeux et commit poussé ; composition (2026111934) ; vérification contre le journal de construction ; garde (pièce « Portée : garde entière ») et commit poussé ; partage (contrôle sur pièce) ; audit du générateur (2026111937) ; scellement de la banque ; mot de départ ; une seule commande pour la plomberie et les blocs A et B (2026111935), sous `env -i` et `GO_ID=GO-2026-11-20-68` ; étalonnage v3 ; audit de symétrie ; lecture unique v3 (2026111936) ; verdict.
- **Étalonnage et lecture en version 3** : empreintes données par la coordination pendant l'écriture, recalculées par moi ; table à seize lignes « OK » ; vérification v3 « Conforme » lue.

## 3. Décisions citées par leur ligne

GO-2026-11-20-26, -36, -55, -64, -68 ; R-4246, R-4272, R-4273, R-4287, R-4289, R-4290, R-4293, R-4298, R-4305, R-4310 (M1 à M6), R-4316 (réserves A et B), R-4320 (lectures de 15:55Z).

**Sans ligne au registre lu** (tête `16505cba…`, dernière ligne R-4323), écrites comme telles : « tout refusé » joué arrêt de plomberie levé (14:01Z, par le rapport v2 du code d'appel) ; les cinq décisions de 15:20Z sur le générateur (par son rapport v3 ; R-4316 n'en nomme que les réserves) ; le silence n° 17 (16:01Z) ; les deux points du silence n° 18 (16:12Z) ; le contrôle par programme de `NO_PROXY` (mandat, point 5).

## 4. Ce que j'ai trouvé et que les pièces lues ne disaient pas

1. **Racine 2026111935 déjà dérivée** par les essais et la contre-lecture du code d'appel : ce code n'a ni mode d'essai pour sa graine ni garde d'autorisation. Aucune mesure n'en dépend ; la l. 303 n'est pas tenue pour ce programme.
2. **Réserve 6, marque au journal de construction** : le journal est écrit par programme et n'a aucun champ pour marquer un fragment récrit par le vérificateur. Or `f-epr-dis-01` porte mot pour mot sa phrase, et trois autres fragments viennent de ses remarques.
3. **Le partage est tiré au geste de composition**, avant la garde ; il n'a pas de commande propre.
4. **Essais sous numpy 2.4.6, exécution sous numpy 2.5.3.**
5. **Part du juge Argon** : GO-2026-11-20-64 couvre « le cas haut » (15,41 USD) ; le pire du devis pour ce juge est 30,44 USD ; le compteur ne distingue pas les juges.
6. **Échéance** : GO-2026-11-20-68 échoit le 2026-11-27, non le 30.
7. **Au pire cas du devis, le compteur ne donne pas le rang 1 à 200** : 996 envois, 197 témoins complets, dont les 100 de la moitié « lecture ».
8. **L'empreinte du rapport v3 transmise par la coordination diffère d'un caractère** de celle que je calcule (`…0453bbb8765…` contre `…0453fbb8765…`) ; la valeur calculée est égale à la table et au compagnon ; c'est elle que l'additif porte.

## 5. Silences laissés à la mère (§ 11 de l'additif)

Les principaux : les deux témoins de la plomberie (proposition `t01,t07`) ; la commande de lancement des relais et de leur déclaration ; le contrôle de `NO_PROXY` au mandat de lancement ; la marque de la réserve 6 ; la racine 2026111935 ; les essais à rejouer ou non sous l'interpréteur retenu ; la suite du verdict de l'étage 2 ; la part du juge Argon ; les chemins ; les bases des seuils de 10 % et de la moitié ; la relance en mode réel ; le chemin réel jamais exercé ; l'emplacement du journal des rejeux sous `runs/`.

## 6. Contestation écrite

Une, à la section 12 de l'additif, marquée, sans en faire une règle : la lecture « voisins non citants » part surveillée « sans seuil », sans que rien dise ce que valent ρ et les votes effectifs si les deux juges rendent `reserves_tenues` faux sur les mêmes bons témoins. Proposition : une phrase de réserve écrite avant le départ.

## 7. Écarts

1. Fichiers tirés de `origin/main` par `git show` redirigé vers mon dossier ; aucun `git fetch`.
2. Pour trouver des noms que le mandat ne donnait pas (tables, rapports, vérifications, sortie du calcul, additifs sur `main`) : ouvertures de chemins supposés d'après les noms cités par les pièces ; deux essais de chemin ont échoué (un nom d'additif 3, une vérification des fragments v1). Aucune commande de liste hors de mon dossier.
3. Une recherche bornée aux fichiers `*_v3.py` du dossier de l'étalonnage et de la lecture v3 a porté sur le dossier, non sur un fichier nommé.
4. Recherches par motif sur des fichiers nommés du clone de l'organisme et du dépôt (lanceur de la course v9, adaptateurs, service des juges), lecture seule.
5. `git log -1` sur des chemins nommés un à un, `git rev-parse`, `git check-ignore`, `git cat-file -e`, `stat` : lecture seule.
6. Une sonde écrite par l'outil d'écriture (`sonde_interpreteur_v1.py`), lancée sous les deux interpréteurs avec `-I -B` : versions de Python et de numpy, présence du kit d'agent. Elle n'importe aucun programme de l'étage 2 et ne lit aucune variable d'environnement.
7. `git fetch` borné aux branches nommées dans les commandes de l'additif, là où le mandat dit « `git fetch` ».
8. La coordination m'a écrit trois fois pendant le travail (vérification v2 rendue ; décision de 16:12Z ; empreintes de la v3) : l'additif porte l'état final.
9. Aucun programme de l'étage 2 lancé ; aucune commande sur un chemin sous `archives-reponses-modeles/` ; aucun appel, aucune clé lue, aucune dépense ; aucune écriture dans le dépôt ni dans le clone ; rien sous `/root/.claude/` ; aucune publication. **Aucun refus de permission, de classifieur ni de garde.**

Rédacteur neuf, modèle F.
