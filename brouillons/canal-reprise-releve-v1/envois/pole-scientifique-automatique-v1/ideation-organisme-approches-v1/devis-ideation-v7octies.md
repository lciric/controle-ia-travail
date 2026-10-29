# Course d'idéation de l'organisme — devis v7 octies (v43 ; plafonds 52,6 ; barème 8,3 ; pire cas aux bornes par champ ; contrôles réussis non rejoués)

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` **07:46 UTC**. **Remplace le devis v7 septies**
(`6e9d9d00…`, gardé, R12) ; le reste des v2 à v7 septies vaut. Code : **v43** (405 essais ; LISEZMOI `a9fca6ac…`, EMPREINTES `f23cc576…`, lot
`livrables/lot-ideation-tournoi-v43-v1.zip` `50a60613…` ; relecture CL10 chez session-depot avant tout lancement). Décisions de Lazar
portées : **« 52,6 : go »** (R-419, GO-14 étendu, R-720 de `main`) ; **CL40-01 → (c)** (R-715) ; **borne de 12 000 par fiche retirée**
(R-718) ; **barème d'Argon ≤ 8,3 USD par million de jetons d'entrée** lu par Lazar (R-718).

1. **Plafonds (ligne de Lazar)** : Claude **40** (0,4 de contrôles + 2 × (5 + 9,3) + 4 + 7) ; Argon **12,6** (contrôle de la course **3,0** ;
   passes **2,5 et 3,0** ; juge 3,5 ; contrôle du bras 0,2 = 12,2 ; marge 0,4) ; **total 52,6**.
2. **Tailles au pire cas, aux bornes par champ** (`--mesurer-consignes`, v43, sans appel ; pièce 750 000 + matériau 350 000, huit fiches à
   `fiche_maximale()` = 44 259 caractères) : passe 1 **752 440** ; passe 2 maximale **1 456 692** ; contrôle de la course **1 457 167** ;
   juge au maximum (52 fiches) **2 131 096** ; contrôle du bras 41. Coût d'entrée à 8,3 USD par million de jetons (4 caractères par jeton) :
   contrôle **3,02**, passe 2 ≈ 3,02 + sortie ; à 10 : 3,64. **Le plafond de 3,0 est dépassé de 0,8 % au pire cas théorique** ; les fiches
   réelles sont bien plus petites (la passe 2 est gardée sur sa consigne réelle, point 3), mais le contrôle de la course se fait au pire
   cas. Deux voies, **sans toucher à 52,6** : **(α) `--taille-max-pieces 740000`** (− 1,3 % de pièces ; contrôle ≈ 1 447 000, 3,00) —
   recommandée, confiance 0,7 ; (β) relever le contrôle et la passe 2 à 3,1 (Argon 12,8, total 52,8 : + 0,2, mot de Lazar). **Défaut sous
   48 h : (α).**
3. **Gardes de taille (v43)** : `--prix-entree-usd-par-million-jetons 8.3` ; **course** : par défaut min(plafond du contrôle / prix ;
   plafond de la passe / prix − provision de sortie) ; la provision de sortie **par défaut est de huit fiches de 12 000 caractères au rapport
   5 (480 000)** — la provision au pire cas par champ (huit fiches de 44 259, soit 1 770 360 équivalents, 3,67 USD à 8,3) rendrait toute course
   avec Argon impossible (garde 0) : elle est écartée, dite ici. Garde par défaut à 8,3 : **724 819** (< 1 447 000) : **le lancement passe
   la garde explicitement : `--taille-max-consigne-externe 1450000`** (= 3,0 / 8,3 × 4 millions = 1 445 783 arrondi ; le contrôle réel mesuré
   avant le GO doit être ≤ 1 445 783). **Bras** : `--taille-max-consigne-externe-bras 1686000` (3,5 / 8,3 × 4 millions) ; une consigne de
   juge au maximum théorique (2 131 096) serait refusée **sans dépense**, tentative non relançable et **classement « sans juge externe »**
   écrit (CL42-05) — accepté et dit : les 52 fiches réelles feront bien moins. **Chaque passe d'Argon est gardée sur sa consigne réelle
   avant envoi** (refus sans dépense ; CL42-01).
4. **CL40-01 (c) — contrôles réussis non rejoués** : à la relance d'une SORTIE après une tentative scellée, les contrôles réussis (réponse
   « OK », scellés avec leur coût) sont repris (numéro de tentative, empreintes au manifeste de départ et au journal) ; seuls les échoués
   ou non faits sont repayés ; `relancable` ne compte que ceux-là. **La phrase « trois tentatives » est retirée** ; aux réglages du devis,
   une relance est possible tant que les contrôles à refaire tiennent dans les sommes. Réserve (v43) : la reprise d'un contrôle Claude
   est reconnue par l'adresse du relais, pas par son identité.
5. **Borne de 12 000 retirée** (CL42-04) : bornes par champ seules (9 questions, 12 antériorités, tailles par champ) ; aucune fiche refusée
   pour sa taille totale ; refus pour taille de champ comptés par proposeur au journal et au manifeste de fin.
6. **Repli, mesure, ordre** : échec du repli scellé (`classement-sans-bras-impossible-N.json`, CL42-06) ; **`--mesurer-consignes` avant le
   GO avec les vrais fichiers** (CL42-03 : la marge est de 0,8 % ; une question de 2 000 caractères suffit à la dépasser → (α) ou (β)) ;
   ordre : Argon d'abord (CL41-07) ; `sha256sum -c EMPREINTES-…-v43.txt`, relais `--plafond-usd 40 --reserve-par-appel 4`,
   `--budget-externe-usd 12.6 --budget-controle-externe-usd 3.0`, plafond de la passe 2 à 3,0 (option du lanceur), liste v4,
   `--taille-max-pieces 740000` (α), délais par défaut.
