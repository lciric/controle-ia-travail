# Vérification neuve du lot 13 v1 (mini-passe)
Verdict : NON CONFORME en l'état (deux défauts bloquants), le reste conforme.

Essais : 6 passés (pytest). Artefacts : verif13_essais.py, verif13_relance_kimi.py (même dossier).

## Défauts
1. GO : `verifier_go(registre, ids=GO_EXIGES)` fixe son défaut à la définition. L'enveloppe change `m.GO_EXIGES`, mais `main` appelle `P.verifier_go(o.registre_go)` sans `ids` : la vérification utilise (46, 48, 54), pas (70, 54). Constaté : `verifier_go.__defaults__` = (46,48,54), alors que `M.P.GO_EXIGES` = (70,54). GO-70 n'est jamais contrôlé ; 46 et 48 sont exigés à tort. Le test ne regarde que la constante. Correctif : `P.verifier_go(o.registre_go, GO_EXIGES)`.
2. Relance de Kimi impossible : sous-part 6,05 = une seule tentative réservée au pire. Après la première (coût réel ~0,05), `cumul + 6,05 > 6,05` : arrêt n° 12. Constaté : Kimi coupé en « length » fait 1 appel, « sans réponse ». La relance unique est donc inopérante pour Kimi. Google 18,15 pour 3 proposeurs (argon, carbon, neon) : 3 tentatives au pire ; les relances dépendent des coûts réels et de la course.

## Conformes
- Gardes du lot 11 conservées : surcharge limitée à `_juger`/`unite`/`courir` ; `tentative`, `chaine`, `_reserver`, garde Google, pire ≤ 6,05, arrêts 12/13, repli, quarantaine intacts.
- Altération du module : empreinte vérifiée contre le compagnon avant chargement ; empreintes/rangs/version posés comme globaux lus à l'exécution (effectifs) ; seul le GO est affecté (défaut 1).
- Garde réduite : fin normale et texte non vide ; testée.
- Relance unique : transport → même requête ; réflexion/coupure → `cran_en_moins` ; deuxième défaut « sans réponse » ; une seule relance.
- Sous-parts : 18,15 + 6,05 = 24,20 ≤ 26,13 ; pires par tentative 1,32 / 2,74 / 0,97 / 0,99. Mais le plafond 26,13 n'est écrit nulle part dans le code (P_X = 199,65).
- Empreinte du texte = constante 2bf01492…7e38 (constatée).
- Aucun texte de réponse dans journal ni sortie (SECRETREPONSE absent) ; configuration et plan ont leur empreinte compagnon.
