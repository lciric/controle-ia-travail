# Journal de la vérification du candidat au scellement v2 (barreau 5) — v1

- Vérificateur : Claude Opus 5.5, sous-agent de la session mère. Le 19 novembre 2026 au soir (UTC), à partir de 23:10Z.
- Mandat : le message de la mère, qui demande la dernière vérification avant le scellement (commit `5e32a8f30`).
- Rapport : `../verification-candidat-scellement-v2-v1.md`. Pièce de travail : non contre-lue.

## Déroulé

1. **Sceaux.** J'ai vérifié les sceaux des pièces du message (empreintes des fichiers contre leurs compagnons et contre le message) : tous égaux.
2. **Différences.** `differences-brouillon4-candidat-v2-v1.py` donne la différence mot à mot du brouillon 4 vérifié au candidat v2, texte et devis. Sortie lue en entier, non versée : elle se rejoue.
3. **Rejeu.** `rejeu-chaine-candidat-v2-v1.py` charge les objets de la fabrique du rédacteur sans exécuter sa fonction principale, qui écrit, et rejoue ses cinq étapes en mémoire. Résultats :
   - brouillon 5 et premier candidat égaux à l'octet ;
   - empreintes annoncées par l'erratum égales ;
   - candidat v2 égal à l'octet, texte et devis ;
   - 79 écritures ;
   - mes 20 couples présents, 18 au candidat et 2 à la fiche v5.

   Sortie versée.
4. **Lectures ciblées** :
   - l'erratum 1 (§ 1 à 5) et le rangement des points (g) ;
   - le rapport v4 (§ 2 à 5, § 7) ;
   - `registres/go.md` (lignes 79 à 88) ;
   - les fiches v4 et v5 (leur différence) ;
   - les lignes du code de formation qui lisent le registre propre ;
   - les passages du candidat qui parlent encore d'attente, de copie, de recharge ou du rapprochement M-6.
5. **Couples.** `couples-verification-candidat-v2-v1.py` : 22 couples, aucun défaut ; validateur du dépôt sans problème sur la copie ; aucune mention d'attente cherchée ne reste. Empreintes attendues : texte `bdff244f…`, devis `dc886195…`. Sortie versée.
6. **Rapport.** Écrit puis contrôlé par `--document` : 22 couples sur 22 reproduits à l'octet.

## Corrections en cours de route

- **Programme des différences** : il imprimait des lignes entières ; récrit mot à mot.
- **Rejeu** : il cherchait mes deux couples de fiche dans la fiche v4 ; corrigé vers la fiche v5 (`25a37968…`), qui les porte.
- **Couples de titre** : l'« après » « — v1 » était déjà dans l'« avant » ; le saut de ligne du titre est ajouté des deux côtés.
- **Première rédaction du rapport, à 13 couples.** J'ai ensuite relu le candidat tel que les couples le rendent. Neuf couples s'y ajoutent :
  - X-2e et X-2f : la puce de dérivation du devis et le prix du volume ;
  - X-3f et X-3g : le devis « à copier à l'octet » et un risque du calendrier ;
  - X-5a et X-5b : M-6 dit ailleurs « avant le scellement » ;
  - X-6a à X-6c : la recharge sans l'enveloppe.

  X-1a et X-1b sont récrits (colonnes, format de l'instant) ; X-3c est étendu ; X-4a est précisé (« cette enveloppe »).
- **X-2c.** La première version chiffrait le dépassement (« quelques USD »), à partir du prix plafond de la carte. Relu dans le code : l'échéance se calcule au prix horaire de l'offre, et je n'ai pas établi ce que ce prix compte du stockage. La version finale ne chiffre plus et dit ce que ce prix ne compte pas.
- **Dates des en-têtes des programmes** : le 19 novembre, non le 20.
- **Citation du rapport v4** : § 7, non § 5.
- **Écriture du rapport neuf.** Une première tentative a échoué, faute d'une relecture du fichier depuis la reprise du contexte. C'est une condition de l'outil, non un refus d'autorisation. Relu, puis écrit.

## Hors du dépôt, dans le bloc-notes, non versés

- Deux petits programmes de contrôle :
  - l'un applique les couples en mémoire et montre les passages d'attente restants ;
  - l'autre imprime les blocs des couples au format du rapport.
- Une copie temporaire de la sortie des couples, écrite par redirection de l'interpréteur de commandes. C'est la seule écriture hors des outils d'écriture, et elle est hors du dépôt. Toutes les écritures dans le dépôt sont faites par les outils d'écriture.

## Non fait, par règle

- Pas de lancement de la fabrique du rédacteur.
- Pas de suite complète d'essais.
- Pas d'appel en ligne à l'interpréteur.
- Pas de commande d'arrêt ni de recherche de processus par motif.
- Pas de réseau, pas de dépense, pas de commit.
