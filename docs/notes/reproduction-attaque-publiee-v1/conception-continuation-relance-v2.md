# Conception — continuation de la relance du témoin de Bailey au-delà du tour coupé — v2 (brouillon, 15 novembre 2026)

Session `session_016QhUrudziqEQujXt4ofM8u`, branche `claude/compassionate-meitner-d4ryyk`. Mot de Lazar : « prépare la
continuation à froid, go ». Remplace la v1 (`conception-continuation-relance-v1.md`, `eb26b686…`, gardée, R12) après sa
contre-lecture (`contre-lecture-conception-continuation-v1.md`, `1da5b75f…`, 7 constats bloquants, notés CL-1 à CL-14
ci-dessous). Ne lance rien, ne dépense rien. Aucune note de sonde ni de juge lue. Code public au commit `9c1f4b1a…`
(arbre `c7cf686c…`), lu hors du dépôt, jamais copié.

## 0. Ordre imposé (CL-7, R1, R4)
Si Lazar retient la continuation, **l'addendum 7 est scellé avant toute lecture des notes de la relance**, donc avant le
verdict R13 au régime réduit. Le verdict au régime réduit (K′ ≈ 34) reste celui du texte, rendu le premier et jamais
remplacé. Le verdict de l'assemblage (« 72 tours, discontinu au tour e₀ ») est second ; les deux sont rapportés côte à
côte, sans règle d'arbitrage, et aucun ne se lit avant le scellement de l'addendum. Si Lazar ne retient pas la
continuation, le verdict au régime réduit se fait sans attendre.

## 1. État transmis d'un tour au suivant (corrigé, CL-2, CL-3, CL-10)
Sonde (sauvegardée `…_ade_e.pkl`, `torch.save` du module) ; paramètres de l'attaquant (sauvegardés ; `SoftParams.reinit`
les recopie **en place** depuis `init_params`, `obf_reps/models/__init__.py` l. 80-85) ; **état d'Adam de l'attaquant**
(moments et compteur de pas : l'optimiseur, construit une fois, `optimizers.py` l. 160 et 218-219, n'est jamais
reconstruit ; **non sauvegardé**) ; `metric.reps_bank` et `test_cached_reps` (mémoire seule) ; `params_last_train_epoch` ;
état du journaliseur v3 (`_suffixes`, `_tour`, comptes de pas) ; générateurs aléatoires (non sauvegardés).
`test_reps_bank` et l'analyse en composantes principales sont inertes ici (CL-11).

## 2. Mécanisme v2 : rejeu complet de l'attaquant, sonde chargée, puis tours neufs
Exécution neuve, même code public, même configuration (`zf-iter-100-mlp`, surcharges inchangées, K = 72), même graine,
**même modèle de carte que la relance (A100 SXM4 80 Go)** et hôte d'au moins autant de mémoire vive (CL-12), dossiers
neufs, module neuf `execution_continuation_v1` (sur le modèle d'`execution_v4` : `runpy`, journaliseur substitué). Pour
les tours rejoués e = 0 … e₀ − 1 :
- **L'attaquant est réentraîné** comme dans la relance (aucun `load_tunable_params_path` ; CL-1 levé : le lien entre
  Adam et les paramètres n'est jamais rompu ; CL-2 levé : l'état d'Adam au tour e₀ est reconstitué par le calcul même).
  Coût : ≈ 16 min par tour en plus de la v1.
- **La sonde n'est pas réentraînée** : `metric.refit(e)` est remplacée par sa première moitié publique (représentations
  sous les paramètres de l'attaquant, ajout à `reps_bank`, assertion `len == e + 2` gardée) suivie de
  `load_pretrained(…_ade_{e+1}.pkl)` ; au tour e₀ − 1 elle charge `…_ade_{e₀}.pkl`. La sonde initiale publique est
  construite puis remplacée par `…_ade_0.pkl` (sans contrôle d'empreinte de fichier : CL-4).
- **Garde « rejeu fidèle » (CL-4)**, sur l'instance, par programme, sans note : à la fin de l'entraînement de
  l'attaquant de chaque tour rejoué, écart maximal absolu entre les paramètres réentraînés et `params_e` sauvegardés ;
  tolérance fixée dans l'addendum avant tout lancement (proposition : 0 sur la même carte si l'essai à blanc montre
  l'égalité exacte, sinon la valeur maximale observée à l'essai à blanc multipliée par 10, scellée avant le run). Garde
  tombée : arrêt par PID avant tout tour neuf (R10), continuation non lue, consignée. Seuls le booléen, le tour et
  l'écart sont journalisés. Les notes du juge, échantillonnées (`do_sample`, température 0,6, `top_p` 0,9), ne servent à
  aucune garde.
- **Journaliseur v4 à deux régimes (CL-3)** : tours rejoués → journal de rejeu distinct (`rejeu/…`), gardes du rejeu
  seulement (nombre de pas de l'attaquant, rejeu fidèle) ; tours neufs → journal ordinaire avec les gardes par tour du
  texte ; les lignes « MARK » des tours rejoués ne comptent pas comme tours complets ; le premier tour complet du
  journal ordinaire est e₀.
- **e₀ et les fichiers (CL-5)** : e₀ = K′ lu sur les journaux scellés de la relance (tours complets) ; dossier de
  chargement neuf contenant exactement `params_0 … params_{e₀−1}` (pour la garde) et `…_ade_0 … …_ade_{e₀}` (sondes),
  copiés depuis le serveur 176187199 et vérifiés par empreinte contre les listes poussées ; tout autre fichier refusé.
  Si `…_ade_{e₀}` manque (coupure avant la sauvegarde de la sonde du tour e₀), la sonde du tour e₀ est **réentraînée**
  par la `refit` publique à la fin du tour e₀ − 1, sur la banque reconstituée, et l'écart est déclaré.
Pour e ≥ e₀ : boucle publique inchangée.

Coût du rejeu : ≈ 16 min (attaquant) + ≈ 8 min (évaluations, génération et juge) + passage du modèle sur 1 600
exemples, par tour ; ≈ 25-30 min × 34 ≈ 14-17 h.

## 3. Ce qui reste non reproduit (déclaré)
Générateurs aléatoires à partir du tour e₀ (génération échantillonnée des évaluations, mélange de la banque, entraînement
de la sonde) ; ordre des blocs de `reps_bank` (contenu égal, ordre non, CL-8) ; machine différente au tour e₀.

## 4. Écarts au préenregistrement (CL-6), tous à l'addendum 7
1. Troisième mode d'exécution non prévu (« une seule relance entière », l. 371 ; tronqué sans relance, l. 338, 372).
2. « Seule la relance porte le verdict » (l. 371) : l'assemblage porte un second verdict.
3. Règle du nombre de tours, B et D (l. 248-258, 374) : K = 72 gardé ; B nouveau, D compté de zéro pour la
   continuation, plafond hors enveloppe (GO-2026-11-10-10, amendé par GO-2026-11-11-01).
4. Sondes et suffixes sortis de l'instance (l. 316-319, 353) : copiés sur un serveur tiers puis sur l'instance neuve.
5. Comportement du code public changé à l'exécution (l. 173-175) : `refit` remplacée pour les tours rejoués.
6. Gardes par tour et de fin de run réécrites pour deux régimes (journaliseur v4, lecture neuve).
7. Mise en place refaite sur une autre machine (gardes de mise en place reprises telles quelles).
8. État d'Adam reconstitué par rejeu ; générateurs non reconstitués.
9. Grandeurs de coût (devis neuf).

## 5. Devis (corrigé, CL-12 ; à refaire sur `sortie-durees-v3.jsonl` après le transfert)
- Tours neufs 34 … 71 : 104 h au modèle a + b·e (a ≈ 0,27 h, b ≈ 0,047 h), × 1,4 pour l'écart observé : **104 à
  146 h** ; les tours 22-31 (moyenne 111 min) donnent plutôt la borne haute.
- Rejeu : 14 à 17 h. Mise en place, essai à blanc, transferts : ≈ 2 h.
- Total ≈ 120 à 165 h ; à 1,17 USD/h : **≈ 140 à 195 USD** ; à 1,6 USD/h : jusqu'à ≈ 265 USD. 5 à 7 jours.
- Run neuf de 72 tours, pour comparaison : 139 à 195 h, ≈ 165 à 230 USD à 1,17 USD/h, sans discontinuité ; la
  continuation n'économise donc qu'≈ 25 à 35 USD et ≈ 1 jour, au prix des écarts 1 à 9.

## 6. Essai à blanc (CL-13)
Sur une petite carte, à la charge du devis : run à K = 2, puis continuation à K = 3 avec e₀ = 2 (deux tours rejoués,
un tour neuf entraîné) ; il mesure la tolérance de la garde « rejeu fidèle », vérifie le lien Adam-paramètres au tour
neuf (le suffixe change pendant l'entraînement du tour e₀) et les deux régimes du journaliseur.

## 7. Recommandation
La continuation est faisable, mais elle coûte presque autant qu'un run neuf (écart ≈ 25 à 35 USD) et porte neuf écarts
au texte. **Recommandation : verdict au régime réduit maintenant ; si le régime publié est nécessaire, run neuf de
72 tours préparé à froid plutôt que continuation** ; confiance moyenne (la borne basse du devis de la continuation
pourrait la rendre plus intéressante si les durées réelles l'y placent). La sauvegarde reste gardée tant que Lazar n'a
pas tranché.
