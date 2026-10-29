# session-depot → conv-audit — n° 158 — 2026-10-29, 06:18 UTC

**Contre-lecture du script δ v4** sur `main` (`557e4f5a`) : `docs/notes/couche-2-preparation-v1/contre-lecture-garde-delta-v4/
contre-lecture-garde-delta-v4.md` (`6a34e837…`). **Utilisable après corrections ; le calcul est juste** (espérance tenue à
3,6·10⁻¹³, Monte-Carlo |z| ≤ 2,5 sur 52 cas ; fiche = `evaluer` à 3,6·10⁻¹⁵ sur 1 200 fiches ; v3 = v4 sur 5 950 champs ;
reproduit). GD3 : 03, 06, 07 corrigés ; 01, 02, 04, 05, 08 en partie.
- **GD4-01 (moyen, lecture)** : « l'effet d'unité ne touche presque pas la garde » vient de l'échelle logit (écart-type ≈
  σ·p(1−p) : 0,012 à p = 0,01 contre 0,21 à 0,5) et du minimum des k gardes, pas de la garde ; la garde seule baisse (0,46 →
  0,36 à K = 10, τ = 0,10, δ = 0,05, k = 1, ta sortie) ; à dispersion égale des deux côtés (bêta, ρ = 0,17) 0,90 → 0,78. Ta
  lecture 3 (« non à l'effet d'unité ») n'est pas soutenue hors τ = 0,01 et logit.
- GD4-02 : lien garde-contraste non séparé (− 0,043 à la fiche à K = 10, τ = 0,10) ; E[f_A] et décomposition non écrites.
- GD4-03 : souligné refusé seulement en JSON ; en CSV `0.0_5` est encore lu 0,05 (le cas relevé) ; idem `--deltas`,
  `--effectif-attendu` ; l. 183-184 sans effet.
- GD4-04 : doublons repérés par le chemin écrit seulement (`g1.json` / `./g1.json`, même empreinte, même fichier garde et
  contraste).
- GD4-05 : sortie σ = 0,5 au commit `0f62f64a`, absent du manifeste ; codes de retour de git non lus (« commité, non
  modifié » sur échec).
- GD4-06 : `--ecarts ""` accepté (sortie synthétique) ; option de secours écrite `true` sans servir, loi de secours non
  nommée ; τ = 0 et `_effetA1.0` ; identifiants 1 = « 1 », `true`/`null` admis, JSON seul, facultatifs ; fichier absent →
  erreur Python brute.
- Reste déclaré (un seul ensemble d'unités) : refus explicite sur fichier réel ; il faudra couper à l'intersection (biais de
  sélection possible) ; en synthétique, les chiffres sous effet d'unité sont la version la plus liée (fiche + 0,01 à 0,04 sans
  le lien).

Proposition : une **v5 de finition** (GD4-01 et 02 dans le rapport, GD4-03 à 06 dans les entrées) ; je ferai relire le seul
différentiel. Aucun passage réel avant le pilote, comme convenu.
