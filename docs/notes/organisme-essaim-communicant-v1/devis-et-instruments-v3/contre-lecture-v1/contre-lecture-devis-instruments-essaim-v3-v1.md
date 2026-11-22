# Contre-lecture des pièces v3 du devis et des instruments de l'essaim — v1

- Contre-lecteur neuf (Claude Opus 5.5). Je n'ai écrit aucune des pièces. Le 22 novembre 2026, branche `lot/compte-organisme-v1`, commit `36d31b6f3`.
- Travail sur processeur seulement : aucun appel de modèle, aucune dépense, aucun réseau. Rien n'a été modifié ni commité dans le dépôt. Aucun refus d'outil, de garde ou de classifieur n'a été rencontré.
- Pièces lues : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v3/` (noté « V3/ » ci-dessous), la vérification de la v2 (`devis-et-instruments-v2/verification-v1/`) et la réponse 14 de Fable (`origin/main`).
- Mes outils sont dans `outils/`, mes sorties dans `sorties/` (ce dossier).

## Verdict

**À corriger** : la borne de 203,94 USD n'est pas encore une borne dure. Elle vaut par invocation du lanceur et sous des hypothèses que l'adaptateur réel, encore à écrire, peut casser sans signal. Les corrections sont courtes, et tout le reste est conforme ou n'appelle que des réserves.

## 1. Compagnons, rejeu, chiffres

1. Les 31 compagnons `.sha256` sont conformes, et la table d'empreintes du rapport (§ 8) concorde. J'ai vérifié avec `sha256sum -c` et par une comparaison faite par script.
2. Le rejeu court se fait depuis le commit (`rejouer_v3.sh`, sans `--long`). Il tient :
   - le devis, les épreuves du devis, le pilote et le coût réduit sont égaux à l'octet ;
   - les gardes sont égales hors horodatages ;
   - 23 tests pytest passent.
3. **Le rejeu long échoue depuis le commit** (code 1), alors que le rapport (V3/rapport…, l. 221) le dit tenu.
   - Seul le champ `artefacts.E-juge-d-empreinte-differente.motif` diffère, dans les 12 mondes. Ce motif contient l'empreinte d'un juge muté qui embarque le chemin absolu du dossier (`test_de_mort_programme_v2.py`, l. 124). Cette empreinte dépend donc de l'emplacement des pièces.
   - Aucun verdict ne diffère.
   - Mais `set -e` arrête le script avant les bases (`rejouer_v3.sh`, l. 31) : le rejeu long ne va jamais au bout depuis le commit.
4. **J'ai rejoué les bases sur la case en entier** (12 mondes, 4 variantes, environ 25 minutes). La sortie est égale hors horodatages à `bases-case-servie-v1-sortie.json`. Tous les chiffres du § 3 du rapport sont retrouvés.

## 2. R1 (chemins)

- `racine_depot_v1.py` refuse proprement, avec `RacineIntrouvable`, quand il n'y a ni racine au-dessus ni variable d'environnement. Je l'ai éprouvé depuis une copie dans le bloc-notes : `calcul_pilote_essaim_v2`, `bases_case_servie_v1` et `test_de_mort_programme_v2` sortent au code 1, et `rejouer_v3.sh` aussi. Aucune pièce v3 ne cite le bloc-notes.
- **Réserve.** `calcul_devis_essaim_v3.py`, l. 27, garde le défaut `"/home/user/controle-ia-travail"`. Depuis une copie sans variable d'environnement, ce script et `epreuves_devis_v3.py` **réussissent en silence** en lisant ce chemin. Les prix du lanceur passent eux aussi par là (`epreuves_gardes_pilote_v1.prix_kimi`).
  - Ce chemin est deviné. C'est contraire à la règle écrite (« jamais de chemin deviné »), même si les empreintes le rendent sans danger pour le contenu.
  - Le rapport, au § 7, dit pourtant que ce chemin « échoue bruyamment ». C'est faux sur cette machine.

## 3. R2 (contrôle des nombres)

- J'ai rejoué tel quel l'outil du relecteur de la v2 (`artefacts_relecteur_devis_v2.py`), par une cale d'import :
  - sur la v3, 10 / 10 tenues, et la sortie est identique à l'octet à `artefacts-relecteur-sur-devis-v3.txt` ;
  - sur la v2, témoin : 3 cassées.
- **J'ai écrit 8 artefacts neufs** (`outils/artefacts_cl_nombres_v1.py`, `sorties/artefacts-cl-nombres-v1.txt`). Chacun change la valeur que Python exécute, et **tous les 8 passent** :
  - redéfinition dans un bloc `if True:` ;
  - redéfinition dans un bloc `try` ;
  - affectation par indice `BORNE_TEST["kimi"] = …` ;
  - appel `PRIX.update(…)` ;
  - expression d'affectation `(VERIF_PIRE := …)` ;
  - écriture par `globals()[…]` ;
  - « marge de 15 % » écrite avec une espace fine insécable ;
  - « 15 pour cent ».
- Une analyse par script de la pièce réelle scellée (`devis_multi_generations_v2.py`) n'en trouve aucune forme. Le seul bloc de niveau module est `if __name__ == "__main__"`, et le seul appel de méthode est `CENTRAL_TOUR.items()`. Les nombres lus sont donc justes pour les pièces à leur empreinte.
- Le contrôle reste un lecteur de formes, pas un lecteur de valeurs effectives. Le rapport devrait dire « les formes essayées sont fermées » plutôt que « corrigée ». Une voie plus sûre : exécuter l'en-tête de la pièce dans un processus isolé et comparer les valeurs effectives.

## 4. R4 et R5 (facteurs)

- J'ai recalculé les facteurs par mon propre script (`outils/facteurs_cl_v1.py`), lu sur les sorties v1 (`8766775c…`) et v3 (`35bf1757…`). Le rapport pire v3 / pire v1 va de **1,819 à 3,228** (Kimi : 3,110 ; 3,202 ; 3,228). Il n'y a aucun écart avec le champ `rapport_pire_v3_sur_pire_v1`.
- J'ai recalculé les leviers sur `programme_attendu` (`calcul-devis-cout-reduit-v2.json`). Ils concordent avec `facteurs_par_levier` et avec la table du devis à coût réduit (l. 23-33) :
  - (a) « tout » : ×2,25 à ×8,20 ;
  - (c) : ×2,08 à ×2,47 ;
  - (d) : ×20,06 à ×49,02.
- J'ai vérifié que la division par 5 est retirée.
- **À noter.** Au pire, le modèle ouvert est plus cher que Kimi par l'interface payante : ×0,86 pour « tout », ×0,93 pour les proposeurs. Le devis ne donne que les facteurs d'estimation et devrait le dire.

## 5. R6 : les gardes font-elles du pire une borne dure ? (le point dur)

### 5.1 Ce qui tient

- Dans une seule invocation de `courir` avec le plan, les prix et le plafond par défaut, la garde 14 vérifie `dépense + réserve ≤ plafond` avant chaque appel (`garde_pilote_essaim_v1.py`, l. 135-137).
- Sous H1 à H4, le cumul ne peut donc pas dépasser 203,94 USD, quel que soit le mélange d'échecs, de relances ou d'abandons. Mon artefact A10 le montre : 744 échecs sans relance sont arrêtés à 203,84 USD.
- Les 23 épreuves de l'auteur se rejouent.

### 5.2 Mes artefacts d'attaque

Les fichiers : `outils/attaques_lanceur_cl_v1.py`, `sorties/attaques-lanceur-cl-v1.json` et `.stdout`, et un faux fournisseur qui tient sa propre facture.

| artefact | fichier : ligne | résultat | gravité |
|---|---|---|---|
| A1 : plan agrandi (proposeurs doublés) et `plafond_depense=1e6` passés à `courir` | lanceur, l. 47 et 54 ; garde, l. 97-98 | code 0, **348,29 USD** | bloquant |
| A2 : seconde invocation après une fin ou un arrêt | lanceur, l. 54 (garde neuve à chaque appel) | 2 × 176,45 = **352,90 USD**, aucun refus | bloquant |
| A3 : relances internes du kit client (par exemple `max_retries=2`), facturées et invisibles | adaptateur à écrire | la garde voit 176,45, la facture vaut **529,34 USD** | bloquant (H1) |
| A4 : réflexion facturée hors du champ `sortie` de l'adaptateur | adaptateur à écrire | la garde voit 176,45, la facture vaut **235,97 USD** | bloquant (H2) |
| A5 : erreur inattendue après facturation (code 17) | lanceur, l. 86-90 | l'appel en cours n'est pas compté, journal sous-estimé d'un appel | à corriger |
| A6 : prix `(0, 0)` acceptés | lanceur, l. 47 | code 0, garde de dépense vide | bloquant (même correction que A1) |
| A7 : sortie négative rendue | garde, l. 160-161 | arrêt 16, l'appel est compté 0 au lieu de sa réserve | à corriger |
| A8 : entrée rendue à 256 000 jetons (fenêtre), cumul près du plafond | garde, l. 160-166 | arrêt 11 **après** dépassement du plafond de la course (176,627 > 176,6) | à noter : excès d'un appel hors H3, borné par la fenêtre (environ 0,5 USD sur Kimi) |
| A9 : relance d'un message déguisé en proposeur (même identifiant) | garde, l. 113 | acceptée avec les plafonds de 24 000 et 64 960 | à noter (la borne tient par la garde 14) |
| A10 : abandons sans limite (`relancer=False`) | garde, l. 189-191 | non comptés comme relances, arrêt seulement par la garde 14 | à noter |

**Ce qui manque pour une borne dure :**
- un registre de dépense persistant, qui survive d'une invocation à l'autre et soit lu avant tout appel ;
- dans `courir`, des refus si le plan diffère de `plan_pstd()`, si le plafond dépasse la borne, ou si les prix diffèrent de `tarifs()["kimi"]` à l'empreinte ;
- un adaptateur réel avec `max_retries=0` et sans repli, où `sortie` vaut les jetons de complétion réflexion comprise, et où toute erreur après envoi compte la réserve ;
- **une limite côté fournisseur** (crédit prépayé ou plafond du compte, de 204 USD au plus) : c'est la seule borne qui tienne contre une violation de H1 ou de H4.

Le lanceur est aussi strictement séquentiel (code 15 si deux appels sont ouverts). 744 appels d'environ 12 800 jetons de sortie prendront plusieurs jours. Toute version parallèle demandera de nouvelles épreuves, avec une réserve cumulée des appels en vol.

### 5.3 H1 à H4 : peut-on les vérifier avant la course ?

- **H2** (réflexion comprise dans `max_tokens`) : par la documentation du fournisseur, puis par un appel minuscule (`max_tokens` de 16 sur une invite qui pousse à réfléchir). On vérifie la fin `length` et un nombre de jetons de complétion d'au plus 16, réflexion comprise. Coût de l'ordre du centime, **sous GO**.
- **H3** (au moins un octet par jeton, plus 256 jetons) : hors ligne, avec le découpeur publié de Kimi, sur les textes servis réels et le gabarit de conversation. Cela demande un téléchargement, donc du réseau, mais aucune dépense. L'essai de fumée le confirme aussi.
- **H1** (facture ≤ usage rendu) et **H4** (un appel échoué coûte au plus sa réserve) : seulement par l'essai de fumée de la réponse 14 (C.3, palier 0 ; A.4, point 1). Quelques appels sous un petit plafond, dont un délai forcé, puis on rapproche le journal de la console de facturation. Plus la règle de facturation des requêtes interrompues, lue dans la documentation.

## 6. Bases sans modèle sur la case

- Rejouées en entier : égales (voir § 1, point 4).
- **L'anomalie** (B3 couvre 6 conditionnelles sur 14 sur la case, contre 3 sur 14 sur les 2 000 instances) est examinée dans `outils/audit_anomalie_bases_cl_v1.py` et `sorties/audit-anomalie-bases-cl-v1.json`.
  1. **Pas de fuite visible.** K1 plus un effet tiré au hasard (B2, 52 cartes, même case, même définition) couvre **0 sur 14**, sur la case comme sur la référence. La recherche ne lit que les données et l'identité de K1, donnée par l'oracle. Il faut confirmer que K1 est bien servie aux proposeurs.
  2. **La définition de « couverte » est trop large pour une conditionnelle.** Sur les 6 conditionnelles couvertes par B3 sur la case, deux le sont uniquement par attribution, sans la bonne condition :
     - monde 11 : effet planté « trait 7, condition 2 » ; cartes porteuses « trait 7, conditions 1, 4 ou 5 » ;
     - monde 7 : 18 porteuses, en majorité sur d'autres paires ;
     - même cas sur la référence, au monde 0.
     - Trois couvertures sont structurelles (mondes 1, 3 et 4) et une a les rôles inversés (monde 5).
  3. **L'écart est compatible avec le bruit.** Les discordances appariées entre la case et la référence sont de 4 contre 1 ; le test exact bilatéral donne p ≈ 0,375.
  - **Conclusion** : un effet du bruit (cartes plus bruitées, 9,4 fausses par monde contre 5,2) **compté par une définition trop large**, sur 14 objets presque binaires.
- **La barre** (B3R sur la case de 9 000 jetons, 10 sur 14) est la bonne au regard de la réponse 14 (C.3) et de la décision du directeur, puisqu'elle porte sur les conditionnelles.
  - **Elle ne compte pas les formes fausses.** B3R en a jusqu'à 15 ou 16 dans les mondes 1, 5 et 8.
  - Le préenregistrement doit donc ajouter la garde « sans excès de formes fausses » (réponse 14, C.3).
  - Il doit aussi rapporter une couverture **structurelle** (carte porteuse portant la bonne paire condition et trait), à côté de la couverture par attribution.
- Il faut aussi nommer les mondes de la liste `couverture_conditionnelle_par_monde` (ordre 0 à 11, non étiqueté ; rapport, l. 142).

## 7. Test de mort par programme isolé

- **Le juge ne lit jamais la loi plantée.** J'ai suivi le juge gelé (`strace`, monde 3, cartes et tranches du rejeu long). Il n'ouvre dans le dépôt que :
  - le juge lui-même ;
  - `racine_depot_v1.py` ;
  - `monde_riche_outils_v1.py`, l'évaluateur générique, qui n'importe que la bibliothèque standard et numpy ;
  - le marqueur de racine ;
  - les deux entrées.
- Les tranches ne portent que `version`, `n` et `tranches{Z, G, Y}`. L'environnement de l'enfant est vide hors `DEPOT_CONTROLE_IA` et `PATH`. Le processus est neuf (`-I`).
- **Réserves.**
  - L'empreinte gelée du juge est lue dans son propre compagnon (`test_de_mort_programme_v2.py`, l. 64-73), ce qui revient à l'auto-certifier. Il faudrait écrire `f505a30f…` en dur, ou la lire dans les empreintes scellées.
  - `monde_riche_outils_v1.py` n'est pas vérifié à son empreinte dans l'enfant (juge, l. 31).
  - La garde interne permet d'ouvrir tout `.py` des dossiers de code et ne bloque pas `exec` (juge, l. 58). Seul le gel du code protège donc contre un juge fautif.
- **Épreuve près du seuil, sous le juge isolé** (`outils/sonde_seuil_juge_isole_cl_v1.py`, `sorties/sonde-seuil.stdout`). Les cartes mêlent la loi du monde à l'uniforme, réglées sur un gain vrai de 0,010 à 0,040, avec 20 tranches neuves de 400 épisodes.
  - **Équivalence exacte** entre le juge isolé et la règle en processus : écart 0, 0 verdict différent sur 160 (monde 0).
  - La statistique est sans biais (moyenne ≈ cible), mais son écart-type par tranche vaut **0,022**, contre un seuil de 0,02. La survie va de 5 sur 20 à un gain de 0,010, à 10 sur 20 à 0,020, et à 17 sur 20 à 0,040.
  - **Lecture.** L'accord de 4 040 sur 4 040 vient de ce que les cartes du jeu sont loin du seuil. Près du seuil, le test de mort à 400 épisodes est presque une pièce jetée à pile ou face. Il faut le déclarer : écrire au préenregistrement la précision par tranche, ou passer à plus d'épisodes ou à plusieurs tranches.
  - La sonde de la v1 citée par l'auteur (0 sur 240 à 0,015 ; 203 sur 240 à 0,025) est beaucoup plus raide. Ses cartes étaient sans doute de faible variance. À expliquer.
  - Monde 1 (même épreuve) : survie de 2 sur 20 à un gain de 0,010, de 6 sur 20 à 0,020, de 18 sur 20 à 0,040. Arrêtée par son identifiant de processus après deux mondes (durée) ; les sorties sont dans `sorties/sonde-seuil.stdout`, et le fichier JSON agrégé n'a pas été écrit.

## 8. R3 ouverte : est-ce acceptable pour le pilote ?

- **Oui, sous une condition.** La classe de l'oracle est invariante, donc la statistique du pilote n'est pas touchée.
- La condition : **aucune projection de l'oracle portant une chaîne choisie par un proposeur** (identifiant, clé de `lois`) ne doit revenir aux agents. Dans le bras (a), la communication est précisément l'objet de la mesure, et un texte de verdict y contaminerait le canal.
- La sortie simple : reconstruire la projection servie depuis la liste blanche (identifiants donnés par le noyau, nombres seulement), au lieu de la filtrer. Une carte malformée y devient « rien » sans contenu, ce qui lève la contradiction avec le jeu sain de l'auteur (§ 6, point 1 du rapport).

## 9. Liste « bloquant pour le pilote »

1. **Registre de dépense persistant** entre les invocations, lu avant chaque appel (A2).
2. **Dans `courir`, refuser** un plan différent de `plan_pstd()`, un plafond au-dessus de la borne et des prix différents de ceux de la pièce (A1, A6).
3. **Adaptateur réel** écrit et éprouvé sur un cas sain et sur un artefact : relances internes à 0, `sortie` réflexion comprise, toute exception après envoi comptée à la réserve (A3, A4, A5) ; anomalie d'usage comptée à la réserve (A7).
4. **H2 établie avant le GO**, et H1, H3 et H4 rapprochées sur un essai de fumée, sous GO séparé ou imputé au GO du pilote (décision du directeur).
5. **Limite de dépense côté fournisseur**, de 204 USD au plus.
6. **Au préenregistrement** : la case servie gelée ; la garde des formes fausses ; une couverture structurelle rapportée ; la précision du test de mort près du seuil ; la condition de la R3 (§ 8).

## 10. Liste « à noter »

- Le rejeu long casse depuis le commit (§ 1, point 3). C'est une correction d'une ligne : comparer hors de ce motif, ou ne pas embarquer le chemin dans le juge muté.
- Le défaut `"/home/user/controle-ia-travail"` de `calcul_devis_essaim_v3.py`, l. 27 (§ 2).
- Les 8 artefacts neufs du contrôle des nombres (§ 3) : sans effet sur les pièces scellées.
- L'empreinte du juge est auto-certifiée, et l'évaluateur n'est pas vérifié dans l'enfant (§ 7).
- A8, A9, A10 et le lanceur séquentiel (§ 5).
- Au pire, le modèle ouvert est plus cher que Kimi (§ 4).
- La liste par monde de la barre n'est pas étiquetée (§ 6).
- Le tarif de Kimi est repris par citation, et sa pièce primaire n'a pas été relue (déjà signalé par l'auteur).

## 11. Mes fichiers

- Outils (`outils/`) :
  - `attaques_lanceur_cl_v1.py` ;
  - `artefacts_cl_nombres_v1.py` ;
  - `facteurs_cl_v1.py` ;
  - `audit_anomalie_bases_cl_v1.py` ;
  - `sonde_seuil_juge_isole_cl_v1.py`.
- Sorties (`sorties/`) :
  - `rejeu-court/` et `rejeu-long/`, avec `rejeu-long.log` ;
  - `bases-case-servie-v1-sortie-cl.json` ;
  - `attaques-lanceur-cl-v1.json` et `attaques-lanceur-cl-v1.stdout` ;
  - `artefacts-cl-nombres-v1.txt` ;
  - `audit-anomalie-bases-cl-v1.json` ;
  - `strace-juge-monde3.txt` ;
  - `juge-sonde-monde0.json` ;
  - `sonde-seuil.stdout` ;
  - `r1/`, `r2/`.
- Chaque fichier de premier niveau a son compagnon `.sha256`.
