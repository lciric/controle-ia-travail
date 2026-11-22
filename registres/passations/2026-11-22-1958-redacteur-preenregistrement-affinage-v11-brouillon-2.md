# Passation — rédacteur du préenregistrement v11 de la course d'affinage, brouillon 2 et devis v11

- Écrite le 2026-11-22T19:58:11Z (`date -u +%FT%TZ`), sur la branche `prep/preenregistrement-affinage-v8-v1`. Elle suit la passation `2026-11-22-1855-redacteur-preenregistrement-affinage-v11.md` et son erratum 1, qui restent en place.
- Mandat : `docs/notes/organisme-affinage-mentors-v1/course-v8/mandat-fable-preenregistrement-affinage-v8.md` (`0f7ddc5487459ecc637db8b29f0fbad6b47deda43d7fa47f79fec4a98a8f9ec2`), donné par la session de l'organisme (`session_013QMaymD1EsQJ68Qivpubes`). Aucun appel à un modèle externe, aucune dépense, aucune instance de calcul.

## Fait

Pièces écrites, scellées, toutes sous `docs/notes/organisme-affinage-mentors-v1/` :

| pièce | chemin | sha256 |
|---|---|---|
| devis v11 | `devis-course-affinage-mentors-v11.md` | `34271cb3cb3dba89c897cc076f7a65cbf73630d96f7106f2f40adac9a2590d52` |
| programme de calcul du devis (116 chiffres contrôlés, aucun écart) | `course-v11/calcul-devis-course-affinage-mentors-v11.py` | `deac25b6fe59332b646cd7b67580126221f3aa5f547623a6270c58b2330428ee` |
| brouillon 2 du préenregistrement v11 (326 lignes ; non scellé comme préenregistrement) | `course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-2.md` | `4a7e430b81e1e5e3714725bf3c9884dfba75df94f295147bb0794c57e3eadf38` |
| programme d'assemblage du brouillon 2 | `course-v11/assembler-brouillon-2-preenregistrement-v11.py` | `c04451eddb95539462af85f829626e3f463497d7f74a63a3f02eb8586d42361d` |
| annexe : phrases du brouillon 2 qui supposent une garde du lanceur v11 | `course-v11/phrases-du-brouillon-2-qui-supposent-une-garde-du-lanceur-v11.md` | `abb967a9e2190f0ca607e8f136e1527105137d42c8225ed8f30a8234f9096b95` |

Le brouillon 1 (`cde6b2d34ddaed05fb5bcd7308896dd0c955bf3d6c15d3db2c5dc99e9f0903f8`) reste en place (R12).

Rejeu du brouillon 2, à l'octet près : `python3 -I course-v11/assembler-brouillon-2-preenregistrement-v11.py course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-1.md <sortie> 2026-11-22T19:53:46Z`.

Décisions suivies, chacune relue par le rédacteur sur `main` au commit `9a5f45db503b52b644185f4045b62c810989027c` (`registres/go.md` `ee1c9cec090b150c55cd26aa27c8b23303f5443a1caa5501c2ebfd43b7f0c17e`, `registres/decisions.md` `996cd20acc7ceb37d7279d2d093cec4b16c1a0a45af924ac13879a18289a855b`) :

- R-4995 : « v8 » de GO-2026-11-22-107 se lit « v11 », base v10.
- R-5006 et R-5007 : plafond propre de la part Claude ; Argon sous la garde gelée des appels aux modèles de Google ; plafond de session des juges relevé ; devis v11.
- GO-2026-11-22-124 (mots de Lazar) : plancher de couverture levé, lecture du solde de la clé LUC non exigée, plafond de la part Claude de 45 USD et plafond de 150 USD inchangés, exception portée au 2026-12-15 sous la réserve d'une confirmation de Lazar.
- R-5018 : Argon et Carbon déclarés à 4 et 20 USD par million de jetons, plafond de session des juges à 1,00 USD, mesure préalable de la réflexion d'Argon sans objet.

Contrôles faits sur le brouillon 2 : 17 sections identiques à la v10 scellée (`7fc71712136cf20d86f3603eb581bc61dd6bc35fcfe0650b230cf659674a3856`), hors saut de ligne final : objet, question, hypothèse, ce qui est servi, plan, plan d'analyse et critères de lecture gelés, règles de N-073, ce que la course ne dit pas, et les neuf différentiels hérités ; 8 sections modifiées (espèces, sorties attendues, ce qui est mesuré, critères de bonne fin, liste d'arrêt, plafond, règle des clés, contre-lecture) ; chaque nombre neuf du texte et du devis retrouvé dans la sortie du programme de calcul ou dans une entrée citée ; 70 citations de l'annexe retrouvées aux lignes dites ; numéros de lignes cités du lanceur v10, du relais Claude, de la porte et de la procédure vérifiés.

## Faits trouvés en chemin, portés à la session de l'organisme

1. Page de prix du fournisseur versée sur `main` (`docs/sources/prix/page-prix-gemini-api-20261122T104129Z.html`, `d3aa716e33e77c7df9da385258dac241f7a608926669f190f42293961201c017`) : Argon et Carbon à 2 et 10 USD par million de jetons jusqu'au 30 novembre 2026, 4 et 20 ensuite ; les v6 à v10 les comptaient à 8,3 et 41,5. Tranché par R-5018.
2. Le lanceur v10 lit les lignes de GO par une expression à deux chiffres de rang : GO-2026-11-22-107 et GO-2026-11-22-124 lui sont invisibles ; il ne lit que l'échéance de GO-2026-11-18-14 (2026-11-25). Annexe, section L.
3. Le relais Claude épinglé relaie un refus de l'interface sans le lire ; son journal garde le statut, non le message. D'où la règle d'arrêt par statut (400 à 499, hors 429).
4. Aux prix déclarés et si la commande d'Argon ajoute la provision de réflexion au plafond de sortie, le plafond de session des juges de 1,00 USD ne laisse que 385 jetons de marge sur l'entrée de juge attendue (devis v11, § 2).

## Reste

- Remplir les emplacements du brouillon 2 (19 « EMPREINTE À INSCRIRE », 8 « RÉGLAGE À INSCRIRE ») quand existent le lanceur v11, ses essais, la configuration v11, les gabarits, les commandes de Carbon et d'Argon sous la garde, les sondes d'Astra, le libellé du contre-lecteur ; puis écrire le texte scellable sous le nom `course-v11/preenregistrement-course-affinage-mentors-v11.md`, sans la ligne d'état ni la dernière section.
- Contre-lecture du devis v11 et du préenregistrement v11 par un lecteur neuf d'un autre modèle (R2), organisée par la session de l'organisme.
- Points à trancher ou à confirmer : dernière section du brouillon 2 (plafond de session des juges à 1,00 ou 1,10 USD ; page de prix relue le jour du départ ; période ; écrit de la mère sur les autres dépenses de la clé LUC ; refus de l'interface).

## Réserves

- Deux messages envoyés à la session de l'organisme portaient une heure estimée et non lue (« 19:33Z », puis « 19:40Z (`date -u`) ») ; ils sont partis vers 19:22Z et 19:33Z. La mention « `date -u` » du second était fausse. Les heures de cette passation et des pièces sont lues.
- Lectures faites hors du mandat strict, pour les réglages et les prix : deux notes de contrôle du collisionneur sur `main` (`9cf6799fcf8d48acec9f505929caaf97d516c7d8f443b9df3fbf7d115dbd9a86`, `f6342515fffdb0d31895bee21afdf04638b4cfbe3baefb90a8a3072cd856b512` : réglages et comptes de jetons, aucun contenu de réponse) et deux pages de prix versées. Aucune sortie de course, rien sous `archives-reponses-modeles/`, aucune réponse de modèle.
- Les prix déclarés viennent d'une copie versée de la page du fournisseur, non d'une lecture de la console de facturation.
- La réflexion d'Argon au niveau `high` et celle de Carbon en flux sur les consignes de l'affinage ne sont mesurées dans aucune pièce lue.
- Routine de reprise : étapes 3 et 4 (défauts échus, inventaire des instances) laissées à la session de l'organisme et à la mère ; `registres/etat.md` non touché (branche de préparation) ; essais du dépôt non relancés dans cette seconde partie (aucun code de `src/` ni de `tests/` changé).
- Aucune demande de fusion ouverte : la n° 64 a été fermée par la session de l'organisme, sans fusion.

## Prochaine action

Sur le mot de la session de l'organisme, avec les empreintes réelles : écrire le texte scellable. Sinon, rien.

## Instances actives

Aucune.
