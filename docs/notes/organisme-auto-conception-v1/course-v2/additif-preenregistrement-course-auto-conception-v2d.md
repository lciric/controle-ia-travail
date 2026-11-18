# Additif au préenregistrement de la course d'auto-conception — correctif v2d

Écrit le 18 novembre 2026 par le développeur unique du correctif v2d (modèle L′). Pièce **neuve** (R12) : rien n'est réécrit.

## 1. Ce que cet additif complète

- Préenregistrement scellé : `docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md`, sha256 `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` (inchangé).
- Additif du correctif v2c : `docs/notes/organisme-auto-conception-v1/course-v2/additif-preenregistrement-course-auto-conception-v2c.md`, sha256 `7c76eba0340040b2c2d29cf3aa5015a194632ac24f3e558565a22424702b0cfd` (inchangé, toujours en vigueur pour ce qu'il dit).
- Fondement : mot de Lazar, 18 novembre 2026, « go (a), lance les deux correctifs », et son autonomie accordée pour les correctifs techniques ; **décision de Lazar `GO-2026-11-18-36`** (registre des GO sur `main`, type « décision », échéance le 18 novembre 2026, R-3314, verbatim « option 1 pour l'épreuve ») : reprise **unique** de l'épreuve réelle des témoins après son échec pour causes techniques ; écart à la condition « tout autre verdict que « réussie » : aucune course » de `GO-2026-11-18-21`, déclaré ici ; les 7 verdicts d'Argon de la tentative v3 **ne comptent pas** ; la course sous `GO-2026-11-18-20` seulement si la reprise rend « réussie » ; plafond de l'épreuve inchangé, **5 USD au total, tentative v3 comprise**. Écart au préenregistrement scellé limité au **programme** qui joue l'épreuve des témoins et au **lanceur** ; aucun changement d'hypothèse, de mesure, de seuil, de témoins, de consignes, de matière, de lecture gelée (`lire_epreuve`), de plafonds (5 USD pour l'épreuve, 90 USD pour la course), de composition ni de devis.

## 2. La tentative v3 de l'épreuve réelle des témoins (rapportée, jamais masquée)

- Jouée le 18 novembre 2026 à 16:11Z par `scripts/epreuve_temoins_auto_conception_v3.py` (`0c72dd8763537152b7339ca15ff439f759c062f0b33a6571a513029870eebd1b`) sous `GO-2026-11-18-21`. Rapport scellé : `course-v2/epreuve-temoins-reelle-auto-conception-v3.json`, sha256 `1e11376fe1255d281212bac086f25d143ab8c86f520dd16f3207ad95d40d02cf` ; verdict écrit « échouée » ; coût **0,132289 USD**. Sortie d'erreur et sortie standard versées : `course-v2/epreuve-reelle-v3-2026-11-18-v1/epreuve-reelle-v3.stderr.txt` (`b30fb23c831078c86bdda42a43feaf63183036d7ee5e39e9b2b9f8f48efda0d7`) et `…/epreuve-reelle-v3.stdout.txt` (`d55fb67b987c042124779024b7c196be47e3e4ee05f422f78febed913cbd7640`).
- **Deux causes techniques** :
  1. le bac à sable du kit (bwrap, socat) n'était pas installé dans le conteneur : l'aiguilleur et le juge Claude n'ont pas démarré (« sandbox required but unavailable ») ; **0 appel au relais Claude, aucun verdict ni aucune classe Claude rendus** (11 classes de l'aiguilleur et 11 verdicts du juge Claude absents). Le programme v3 ne sondait pas le bac avant les appels ; le lanceur, lui, le sonde ;
  2. chaque jugement d'Argon coûte **deux** appels au relais Gemini (`countTokens`, puis `generateContent` : `commande_argon_v3d.py`, compte des jetons actif par défaut ; `relais_gemini_v2.py` compte les deux actions dans `--max-appels`). Les 11 témoins demandaient 22 appels de relais ; les commandes v2c bornaient ce relais à `--max-appels 15`. Journal du relais (hors dépôt, lu sans écrire) : 15 appels admis (7 paires, puis le `countTokens` de t08), puis 4 refus « --max-appels (15) atteint » ; t08 à t11 sans verdict d'Argon.
- **Les 7 verdicts d'Argon rendus (t01 à t07), tels qu'au rapport scellé** ; ils ne comptent pas dans le verdict de la reprise (`GO-2026-11-18-36`) mais seront rapportés à côté de ceux de la reprise, jamais remplacés ni masqués :

| témoin | classe plantée | item planté | notable lu | items lus faux |
|---|---|---|---|---|
| t01 | bon | — | vrai | aucun |
| t02 | bon | — | vrai | aucun |
| t03 | bon | — | vrai | aucun |
| t04 | bon | — | vrai | aucun |
| t05 | bon | — | vrai | aucun |
| t06 | mauvais | `voisin_nomme` | faux | `voisin_nomme` |
| t07 | mauvais | `epreuve_plantee` | faux | `aucun_modele_ne_decide`, `epreuve_plantee` |

  Lus par la règle gelée, ces 7 verdicts ne comportent aucun manque ; les manques de la tentative v3 sont tous techniques (aiguilleur 11, juge Claude 11, juge Argon 4 : t08 à t11).

## 3. La reprise n'est pas un rejeu visant un signe

Aucun verdict ni aucune classe Claude n'a été rendu, et les seuls verdicts rendus (Argon, t01 à t07) ne portent aucun manque : la reprise ne vise pas à changer un résultat lu, elle joue pour la première fois ce qui n'a pas pu partir (R3). Le programme v4 joue **les mêmes 33 appels, dans le même ordre**, sur les mêmes témoins, consignes et configuration, sous la même ligne de GO et le même plafond de **5 USD au total, tentative v3 comprise** : la dépense de la tentative v3 (0,132289 USD, lue dans son rapport scellé à l'empreinte épinglée) est retranchée, la reprise n'appelle que tant que le cumul plus le plafond de session de l'appel suivant tient sous **4,867711 USD**, et ce budget (4,86 USD au centime inférieur) est transmis aux portes ; il écrit son rapport à un chemin neuf (`course-v2/epreuve-temoins-reelle-auto-conception-v4.json`) et cite la tentative v3 (chemin, empreinte, verdict écrit, coût, verdicts bruts) dans le champ `tentative_precedente`. Si la reprise rend un verdict d'Argon différent de celui de la tentative v3 sur t01 à t07, les deux sont rapportés.

## 4. Ce qui change (programme d'épreuve v4, lanceur v4), et rien d'autre

Programme `scripts/epreuve_temoins_auto_conception_v4.py`, sha256 `04f62b8c48db9e9b04114aaa37f00801e825ff0bc2d4a86934b44f2b79263d75` :

1. **Sonde du bac à sable avant tout appel** (avant la procédure des relais, la porte à blanc, la transmission des plafonds et le premier appel) par la commande de l'orchestrateur épinglé (`etat_bac_a_sable_detaille`, comme le lanceur) ; `actif` et `proc_neuf` vrais exigés ; sinon refus, code 2, rien dépensé.
2. **Borne du relais d'Argon** : `--max-appels` lu par PID et `max_appels` lu par `/relais/etat` ≥ **2 × 11 + 2 = 24** (deux appels de relais par jugement, plus une marge d'un jugement entier) ; sinon refus avant tout appel. Les commandes v2d lancent ce relais à `--max-appels 24`.
3. **Manques techniques** : un appel au statut d'adaptateur « erreur » (parti mais échoué : bac, refus du relais, réseau, délai) ou non parti est consigné (`incidents_techniques`). Si **tous** les manques de la lecture gelée sont de cette sorte, le verdict écrit est « non conclue » (comme pour un arrêt) ; un verdict lu et faux, une réponse lue illisible, un refus du modèle, un budget ou des tours épuisés restent des échecs, et « échouée » demeure dès qu'il en existe un. `lire_epreuve` est identique à l'octet ; la requalification ne rend jamais « réussie ». Le verdict de la lecture gelée est gardé à côté (`verdict_lecture_gelee`). Lue ainsi, la tentative v3 aurait été « non conclue ».
4. Le programme refuse de partir si le rapport v4 existe déjà (**reprise unique**).
5. Il exige la ligne `GO-2026-11-18-36` au registre des GO lu au commit de `main` (une seule ligne, type « décision », accordée par Lazar, période couvrant le jour, périmètre qui dit « reprise » et « témoins ») ; et il retranche la dépense de la tentative v3 du plafond de 5 USD (budget de la reprise 4,867711 USD, transmis aux portes au centime inférieur).

Lanceur `scripts/lancer_course_auto_conception_v4.py` : épingle le programme v4 et son rapport, cet additif et une contre-lecture neuve (`course-v2/contre-lecture-correctif-v2d-auto-conception.md`) ; recalcule le verdict par la lecture gelée puis la requalification du v4 ; et corrige le **même défaut de comptage pour la course** : 231 appels d'Argon au pire (11 proposeurs + 11 cases × 5 espèces × 4 cartes × 1 juge Argon) demandent **2 × 231 + 2 = 464** appels de relais (le lanceur v3 exigeait 231, les commandes v2c posaient 280 : la course se serait arrêtée vers le 140e appel d'Argon) ; le relais de Carbon (`relais_gemini_v4.py`, même compte : `countTokens` puis `batchGenerateContent`) doit admettre 2 × 11 + 2 = 24 appels et 11 lots (commandes : 60 et 15, suffisants) ; Astra inchangé (une requête par appel). Déclarations et sorties aux chemins neufs (v4) ; « une seule course » couvre v1 à v4.

## 5. Ce qui ne change pas

Témoins (`temoins-juge-auto-conception-v2.json`), consignes, configuration, matière (`matiere-premiere-v3.md`, `11f4b69b…`), lecture gelée, seuils, plafonds (5 et 90 USD), composition (Opus, Fable, Argon, Astra, Carbon ; aiguilleur et juges), devis, lignes de GO (`GO-2026-11-18-20` course, `GO-2026-11-18-21` épreuve), pièce de départ scellée (`e2689fa22fff31319ff69deefe10c066d5329fab28d9c9b133750f2534fc1ded`), sonde d'Astra du jour (`802b840edbf14983ce302b71253242c753e70aa60335868e811fdb6fd45e8f43`), relevé des prix Claude scellé (`ed812e6a336ba4682053dd7bec5554c6f5aeb4fb54dcc7d22760900a33e890b4`). Règle écrite d'avance inchangée : épreuve non « réussie » → aucune course.
