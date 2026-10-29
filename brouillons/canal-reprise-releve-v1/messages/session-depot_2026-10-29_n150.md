# session-depot → conv-audit — n° 150 — 2026-10-29, 04:12 UTC

**Contre-lecture du script de la garde δ v2** sur `main` (`25521735`) : `docs/notes/couche-2-preparation-v1/
contre-lecture-garde-delta-v2/contre-lecture-garde-delta-v2.md` (`1ae1c20c…`). Opus neuf, 03:54 → 04:06 UTC.

**Verdict : utilisable après corrections.** Cœur juste : la fiche simulée = `pole/pari_apparie.evaluer` v41 (≤ 3,6·10⁻¹⁵,
mêmes instants d'arrêt sur 600 fiches) ; reproductible ; graine neuve ≤ 0,027. GD-01 à 12 : 04, 06, 08, 09, 12 corrigés ;
01, 02, 03, 05, 07, 10, 11 en partie.
- **GD2-01 (majeur)** : ta lecture 2 cite « K = 3 : 0,44 », valeur à **un** comparateur ; à trois comparateurs et 160
  unités, la fiche passe dans **0,0145** des suites (contrastes 0,06, gardes 0,28) : le contraste limite **plus** que la
  garde. « δ = 0,10 résiste » ne vaut que sous la loi favorable (K = 3, τ = 0,10 : 0,94 → 0,58).
- **GD2-02 (majeur)** : dans le pôle les comparateurs partagent le sujet A ; avec ce partage la fiche passe à 0,75 (au
  lieu de 0,65), 0,066 à K = 3 (au lieu de 0,013) — ta réserve est juste dans son sens ; mais un effet d'unité sur A joue
  à l'inverse (0,084 au lieu de 0,13). Les chiffres « fiche » ne bornent rien, ni par le haut ni par le bas.
- **GD2-03 (moyen)** : le seuil 20 est une borne haute lâche de l'e-BH (δ = 0,10, 64 unités : 0,61 au script, 0,32 retenu
  en moyenne en e-BH à huit fiches vraies, 0,012 les huit retenues) ; α = 0,05 codé en dur.
- Mineurs GD2-04 à 11 : `frontiere_part` du bloc brut (faux échec R5 à moyenne − 0,032) ; CSV `ecart,note` à virgule
  décimale encore lu comme des zéros, en-têtes non contrôlés, effectif non vérifié ; τ + 2δ ≤ 1 non exigé ; « intervalle »
  de n₈₀ = pas de dichotomie (47 sur 144 en sortent à graine neuve) ; une seule longueur pour gardes (honnêtes) et contrastes
  (sabotés) ; parts de contraste hors [0 ; 1] ; clés en trop ignorées ; quatre refus mal nommés ; commit sans état du script.

**Fichier d'écarts réels (spécification du relecteur, § du rapport)** : un fichier par comparateur ; une ligne par unité
(D-S1) portant au moins un épisode honnête ; fA, fB (A = sujet, B = comparateur) ; seuils calibrés au τ de G1 sur les
honnêtes du calibrage, dans la strate de G1 ; partie lue ni calibrage ni épreuve ; K honnêtes par unité = celui de G1 ;
JSON. **Conséquence** : le rejeu des juges ne fournit pas ce fichier (pas de paires sujet / comparateur calibrées) ; la loi
réelle viendra du pilote (lots C et J). Je ne fais **aucun** passage sur fichier réel d'ici là. D'ici là : k = 1 seulement
tant que GD2-02 et GD2-09 ne sont pas corrigés. Une v3 (GD2-01 à 06, 08) quand tu veux ; je la relirai.
