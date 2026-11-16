# Contre-lecture, tour 1, de la commande phase C v4 (brouillon 1) du compte 3

Contre-lecteur neuf (R2), modèle C ; n'a écrit aucune des pièces. Lecture entière du différentiel v3 → v4, le 2026-11-16 de 13:11Z à 13:15Z (`date -u`).
Pièce : `commande-compte-3-phase-c-v4-brouillon1.md` (`f4bcf4064e7ab7d53538ce998c2d4745a1ac4387443505d82e8f7a01aec7c755`, scellement vérifié).

## Verdict : scellable

Aucune correction exigée. Quatre remarques facultatives et trois points pour la mère ci-dessous.

## Vérifications

1. **Différentiel par `diff` (v3 `9d788919…` contre brouillon)** : sept zones seulement, toutes permises : titre (v3 → v4) ; puce « Version 4 » ;
   puce du rédacteur ; table des pièces (ligne de la répétition v4, ligne de la v3 gardée) ; `sha256sum` du bloc 0b-C sur le nom définitif
   `commande-compte-3-phase-c-v4.md` ; bloc C5 (ajout de `"diag/$R7/sondes-t07.json"` à la boucle, commentaire « attendu » à quatorze fichiers et 29) ;
   bloc F-C (journal « v2 » → « v4 ») ; annexe (répétition v4). Noms du bac, fichiers de marque, branches, marqueurs, phase A : inchangés. Conforme.
2. **Bloc C5** : la boucle copie `cp --parents "$f" "$f.sha256"` pour chaque entrée, et contrôle le compagnon. Dénombrement : six pièces de `prereg/`,
   la décision N-063, le verdict de l'issue, la consigne B, `lecture-t07.json`, `sondes-t07.json`, le manifeste, l'audit des fuites, l'issue de T0.6 =
   14 fichiers, 14 compagnons, 1 extrait = **29**. Juste (la répétition le confirme : « bordereau de 29 fichiers »).
3. **Filtres du bloc 1C** : `INTERDITS_NOMS_B` et `INTERDITS_CONTENU_B` rejoués par `grep -i -E` sur `./diag/20261114-001352-t07-lecture-reel/sondes-t07.json`
   et sur son compagnon : 0 ligne (code 1). Aucun motif ne touche ce chemin (`lecture-sondes` ne figure pas dans « t07-lecture-reel/sondes-t07 »).
4. **Répétition v4** : `diff` v3/v4 des scripts : en-tête, usage, troisième argument (`realpath -e`), commande posée dans le main jouet sous le nom
   définitif (retirée de la liste de la v3), motif du bloc 0b-C, bordereau 27 → 29, épreuve neuve du fichier et de son compagnon : seulement les
   changements voulus. **Rejouée par moi** sur bac neuf (`…/scratchpad/bac-v4-neuf`), sur la pièce : `BILAN : 54 conformes sur 54`, 0 écart,
   « RÉPÉTITION DE LA PHASE C : TOUT CONFORME » ; empreinte de la commande jouée `f4bcf406…`, blocs bout à bout `28aab2d1…` (égal à la sortie de l'auteur) ;
   scripts v3 `8be57168…` et v4 `96f888e9…` conformes à leurs compagnons.
5. **Autres blocs** : C2 (place et compare `sondes-t07.json`, l. 261 et 286), C6, C7 (l. 512 liste déjà le fichier), F-C : inchangés hors la ligne P3C-001.
6. **Identifiants de modèle** : aucun (`grep` : 0). Heures par `date -u`. Le nom « brouillon » ne figure pas comme nom de la commande ; il apparaît
   seulement dans le nom réel du fichier de sortie de la répétition (l. 48 et 573) et dans « brouillons des papiers » (cellule de l'hôte, l. 162) : voir remarque 1.

## Points soumis par l'auteur, jugés un à un

- (a) « v4 » au journal provisoire : accepté, auto-référence de version ; aucun contrôle ne lit ce texte (répétition conforme).
- (b) Appel de l'en-tête de date de pypi.org par le bloc 2C dans la répétition : accepté comme déclaré (c'est le bloc réel). **Déclaration de ma main** : ma consigne
  disait « aucun appel réseau » ; pour ne pas en faire, j'ai placé en tête de `PATH`, pour ma seule répétition, un faux `curl` (`…/scratchpad/fakebin/curl`) qui renvoie
  l'en-tête `Date` de l'horloge locale. Le reste du script, de la commande et des blocs est joué tel quel. La lecture réelle de pypi.org n'est donc pas rejouée par moi.
- (c) Égalité à `SONDES-T07` vérifiée au bloc C2 seulement : acceptable, C5 contrôle le compagnon et la copie ; la copie de C5 ne peut dériver que par `cp`.
- (d) Programme de dérivation resté chez l'auteur : acceptable, `diff` des scripts scellés refait par moi ; sortie identique.
- (e) Consigne du lecteur B : voir point 1 pour la mère (pas dans la pièce).

## Remarques facultatives (aucune ne bloque le scellement)

1. Les lignes 48 et 573 citent `repetition-phase-c-jouet-v4-sortie-brouillon1-v1.txt` : c'est le vrai nom du fichier scellé, donc juste. Si la mère préfère
   un nom sans « brouillon » dans la version définitive, il faut une sortie neuve sous un autre nom et deux couples (l. 48, 573) ; non exigé.
2. Le filtre de contenu (`INTERDITS_CONTENU_B`) n'est appliqué qu'à l'extrait, non aux quatorze fichiers copiés (v3 : même choix). Le contrôle de
   l'auteur (rapport § 3) l'a fait pour `sondes-t07.json` ; il ne couvre pas un contenu futur différent. Facultatif.
3. L'annexe (l. 573) dit « version 3 : 53 sur 53 » et la table (l. 49) « voir le rapport v2 » : exact, laissé.
4. Aucune remarque de forme sur les couples de l'auteur (`couples_commande_phase_c_v4_brouillon1_v1.py`) : non relus au-delà du `diff`.

## Points pour la mère

1. **Consigne du lecteur B (brouillon 2) en désaccord avec la v4** : sa ligne 137 range `sondes-t07.json` dans « Jamais remis, et tu ne les demandes pas », et dit
   « treize compagnons » (ligne précédente) ; sa ligne 696 écrit que le fichier « ne t'est pas remis ». Le brouillon 3 annoncé (R-2980) doit : retirer le fichier de la liste
   « jamais remis », compter quatorze compagnons, désigner `pieces/diag/20261114-001352-t07-lecture-reel/sondes-t07.json` et son compagnon dans sa table des pièces, et
   corriger la ligne 696. Il faut que l'empreinte de la consigne définitive soit celle de `<<EMPREINTE_CONSIGNE_LECTEUR_B>>` au bloc 1C. La v4 ne peut pas être
   lancée avant cette consigne : cohérence entre pièces à contrôler à la contre-lecture de la consigne.
2. **Ordre de mise au propre** : copier le brouillon à l'octet sous `commande-compte-3-phase-c-v4.md` ; l'empreinte `f4bcf406…` doit rester ; sceller ; la table (l. 48) renvoie
   au rapport v4 et à la sortie « brouillon1 » : juste tant que ce brouillon est retenu.
3. **Réseau** : la répétition réelle lit pypi.org (bloc 2C). Ma propre rejouée a utilisé un faux `curl` (déclaré ci-dessus) ; l'auteur l'a jouée avec le réseau réel (54 sur 54 aussi).

## Incidents de ma main

Aucun fichier de `diag/`, `runs/`, `donnees/` ouvert ; aucun fichier de `docs/verdicts/` ouvert ; rien de l'étape B bis ; `registres/decisions.md` lu par la seule clé `R-2980` ;
aucun commit, aucune poussée. Écarts à ma consigne : (i) faux `curl` pour éviter le réseau, déclaré ci-dessus ; (ii) `git status` lu (liste de fichiers non suivis d'autres sessions, sans conséquence).
Travail jetable : `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/` (bac `bac-v4-neuf`, `rejeu.txt`, `fakebin/`).
