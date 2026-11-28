- **CV3-01** (défaut d'un banc, corrigé) : le cas X08 du banc des vérifications (GO de calcul qui mentionne un retrait
  sans identifiant) portait une apostrophe dans une commande placée entre guillemets simples (`eval`) : la ligne n'était
  pas ajoutée, le registre d'essai perdait la ligne de GO-2026-10-20-07 et le cas sortait en code 1. Trouvé par la passe
  préliminaire (`…/chaine-v3-travail/passe-1/banc-verifications-1.log`) ; apostrophe typographique ; repassé conforme
  (`…/passe-1/banc-verifications-2.log`) avant la passe finale.
- **CV3-02** (réserve levée pendant la correction) : `…/tokeniseur/tokenizer.json` manquait au bloc-notes restauré
  (vérifié sur disque et par recherche hors du dépôt de travail ; listes des archives des sessions 14 et 16 sous
  `registres/passations/` : seul `tokenizer_config.json` y figure). Le banc des contrôles refusait en code 2. J'ai ajouté
  au banc une option explicite, `BANC_TOKENISEUR_SUBSTITUT=1` : sans elle, refus comme avant ; avec elle et seulement si la
  copie de la session manque ou n'a pas son empreinte, un `tokenizer.json` synthétique, annoncé au journal, et une ligne
  de plus changée dans la copie des contrôles (TOK_JSON) ; `tokenizer_config.json` réel exigé. La passe préliminaire l'a
  utilisé (`…/passe-1/banc-controles-2.log`, conforme). La copie de la session est réapparue le 2026-10-21 à 00:06 UTC
  (pas de mon fait), d'empreinte `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` (vérifiée) : la passe
  finale a joué le vrai tokeniseur (journal : « tokeniseur de la session : tokenizer.json 79e3e522635f…,
  tokenizer_config.json réel » ; dix lignes changées, comme en v2) ; la variable était posée, le substitut n'a pas servi.
- **CV3-03** (choix du correcteur, au-delà de la lettre de VC2-donnees-01) : en repli de l'affichage, toutes les lignes
  sont réduites, y compris celle de l'instance gardée ; l'heure limite de destruction ne serait plus lisible, alors que
  RC-depense-02 et la paire 5 disent que la récupération en échec l'écrit. La récupération réécrit donc, après la sortie
  filtrée et seulement en repli, la ligne de l'instance gardée entière, hors du filtre : forme fixe (identifiant de 6 à 10
  chiffres, deux états de l'outil réduits aux lettres, chiffres, points, tirets et soulignés, 20 caractères chacun, heure
  limite calculée) ; aucune donnée de la branche. La même réduction des états vaut pour toutes les lignes « instance
  gardée ». Phrase ajoutée à la paire 7. Éprouvé par l'artefact « repli de l'affichage » (dernière ligne entière, les
  autres réduites). Se retire sans toucher au reste si la session le refuse.
- **CV3-04** (information, banc) : le banc du lanceur dépend du jour UTC (l'accord d'essai est daté du jour au début) : la
  passe préliminaire a franchi minuit et vingt cas ont échoué après M03 (« ligne du jour (2026-10-21) attendue »),
  `…/passe-1/banc-lanceur-1.log` ; aucun défaut de la chaîne (le lanceur réel refuse justement un accord de la veille).
  Passe finale jouée d'un seul tenant le 2026-10-21. La répétition préliminaire a franchi minuit (passage 1 de 23:43 à
  00:17 UTC) sans écart.
- **CV3-05** (information) : la paire 5 précise « Récupération en échec (code 1, ou refus en code 2 faute de place disque
  ou de clonage) » : le troisième refus en code 2 (traces d'un autre lancement) n'écrit ni état ni heure limite, car
  l'instance n'y est pas reconnue comme celle du lancement (identifiant, commit ou création autres) ; la phrase ne
  l'affirme plus.
- **CV3-06** (information) : la commande `paires-v2` d'`outils_essais_p4_v1.py` est remplacée par `paires-v3` (même
  forme, phrases de la v3) ; `…/chaine-v2-travail/fabriquer_c_essai_v2.sh` ne s'applique plus à la chaîne v3 :
  `…/chaine-v3-travail/fabriquer_c_essai_v3.sh` (module v3, chaîne v3, paires du module v3 puis de la chaîne v3).
- **CV3-07** (information) : les journaux bruts citent la cible du lien du bloc-notes
  (`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/bloc-notes-session14/p4-instrument/…`),
  là où les scripts nomment `…/50508bff…/scratchpad/p4-instrument` (`realpath`) ; sans effet sur les empreintes (comme
  VC2-depense-08).
- **CV3-08** (information) : cas ajoutés au-delà de ceux du traitement, pour fermer des formes proches : X06 (type en
  gras), X07 (identifiant de décision entre guillemets inversés), X08 (témoin sain), A15 à A17 (étiquette en majuscules,
  suivie d'une espace, numérique), T09c et T09d, F16 à F18 (lien vers un dossier, lien donné en argument, tube nommé),
  J33 (refus en code 2 de trop).
- **CV3-09** (information) : la tête du dépôt de travail a bougé pendant la correction (`0591049`, `9ecd952`, `0a44ee6` :
  commits d'autres sessions) ; le banc final lit les registres réels à `0a44ee6` (`git show main:…`), égaux à ceux de
  l'arbre de travail (R00c). Le dépôt n'a été que lu (commandes git de lecture, `GIT_OPTIONAL_LOCKS=0`) et cloné par
  référence dans le dossier de travail.
