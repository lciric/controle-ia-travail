# Écarts du devis v2 du pilote « oracles plantés » : chiffres écrits à la main contre rejeu par script — v1

- Classe B (vérification d'instrument), 0 USD, processeur seul, aucun appel de modèle. Vérificateur : un Opus 5.5 neuf, le 22 novembre 2026. Rien n'est corrigé dans le devis : ce texte rapporte.
- Pièce vérifiée : `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v2-brouillon.md` (sha256 `c857e62c1e921cdfc16f1234e54bff2d8dcf1f68bfdb7d8e3dcb96ee1d555ca6`).
- Rejeu : `calculs_devis_pilote_generation_v2.py` et sa sortie `sortie-calculs-devis-pilote-generation-v2.txt` (même dossier ; empreintes dans leurs compagnons `.sha256`), lancé par `.venv/bin/python -I`. Logique reprise en copie du script v1 (`calculs-v1/…`, non modifié).
- Appuis : devis v1 (`6f485216…`, empreinte conforme à celle citée par le v2), relevés de prix (`a7d9073f…`, conforme), brouillon 2 du préenregistrement en différences.
- Tolérance d'arrondi : 0,005 USD. Profils de jetons, heures de machine et montant de fumée : **supposés** (repris du v1 ou écrits au v2), nommés tels dans le script.

## Verdict
Les calculs du § 2 sont justes : les 21 coûts unitaires, les 27 cases de postes et totaux, les deux replis chiffrés, les deux lignes conditionnelles, la réserve écrite et les plafonds se retrouvent au centime près (écarts de 0,002 à 0,004, arrondis). **Un chiffre du texte est faux** (+0,84, § 5) ; quatre chiffres sont des conventions non écrites ou non bornantes ; six incohérences de texte ou chiffres sans source.

## 1. Table ligne par ligne (écarts au-delà de l'arrondi, et arrondis notables)

| § | chiffre du devis | chiffre du script | écart | cause |
|---|---|---|---|---|
| 5 | reformulateur Argon à 2/10 : +0,84 | +0,00 | −0,84 | Argon à 2/10 et Kimi ont le même prix (2/10) : aucun surcoût. La table du § 5 (147,89 = 157,97 − 10,08) ne compte pas ce +0,84 et est juste ; c'est la phrase qui est fausse. Avec +0,84 la case vaudrait 148,73. |
| 2 | fumée 0,10 (« quatre appels d'au plus mille jetons ») | 0,096 à 0,192 selon les modèles | jusqu'à +0,092 | 0,10 n'est pas une borne haute : un appel par modèle (brouillon 2) à 1 000 / 1 000 coûte 0,096 avec Argon à 2/10, **0,108** avec Argon à 4/20 ; 2 Astra + 2 Kimi (lecture du § 7, point 2) 0,120 ; 4 Astra 0,192. Effet sur les totaux ≤ 0,10. |
| 3 | réserve des appels en vol 5,72 = 3 × 1,50 + 2 × 0,32 + 0,576 | 5,716 (formule écrite) ; 5,932 (logique v1) | +0,21 (logique v1) | La formule écrite est juste, mais elle abandonne le relecteur Kimi au pire (3 × 0,072) que le script v1 comptait (« 3 × (plafond + relecteur) »). Sans effet sur le plafond (300 dans les deux cas) ; la réserve inscrite en A6 du brouillon 2 (5,72) en dépend. |
| 3 | 192,79 × 1,5 + 5,72 = 294,91 | 294,905 (valeurs arrondies) ; 294,898 (valeurs exactes) | −0,01 | Chaîne d'arrondis ; 294,90 sur valeurs exactes. Sans effet (300). |
| 3 | plafond machine 65 (« 48 h × 1,30 ») | 62,40 | −2,60 | 65 est 62,40 arrondi aux 5 supérieurs (règle du script v1, bloc 3), règle non écrite au v2. Arithmétique juste, convention à écrire. |
| 2 | P3 bras S attendu 64,06 ; pire 264,58 ; P3 N bas 10,82 | 64,064 ; 264,576 ; 10,816 | ±0,004 | Arrondi. |
| 2 | un monde régénéré 12,50 | 12,496 | −0,004 | Arrondi. |
| 2 | attendu avec conditionnelles 192,79 | 192,788 | −0,002 | Arrondi. |
| 2 | totaux 73,33 / 157,97 / 567,52 ; 76,36 / 165,17 / 590,56 | 73,332 / 157,972 / 567,524 ; 76,356 / 165,172 / 590,564 | ≤ 0,004 | Arrondi. |

Tous les autres chiffres du devis (effectifs 432, 144, 48, 208, 58 ; unitaires ; P1, P2, P4 ; repli juge Kimi −10,08 ; reformulateur Argon à 4/20 +1,68 ; banque de connus refaite 15,12 ; 48 propositions par monde ; 0,444 ; plafond d'appels 300 ; somme 365 ; table du § 5) sont retrouvés à l'identique (sortie, blocs 1 à 7). Les reprises écrites (23,40 / 46,20 / 190,80 ÷ 150 ; 7,80 / 20,40 / 74,40 ÷ 150 ; facteur 0,8 sur Astra ; Kimi 0,032 et « quatre fois ») sont exactes (bloc 2).

## 2. Incohérences et chiffres sans source (rapportés, non corrigés)

1. **P7 sans source.** L'intervalle [110 ; 250] du brouillon 2 n'a aucune formule écrite au devis ni au brouillon. Il ne reprend pas la règle implicite du brouillon 1 ([120 ; 260] autour de 164,28, soit × 0,730 et × 1,583), qui donnerait [115,39 ; 261,41] au v2 (bloc 8). Le bas (73,33 et 76,36) et le pire (567,52 et 590,56) tombent hors de [110 ; 250], comme au v1 ; le plafond d'appels (300) aussi. L'attendu, les deux replis juge Kimi et l'attendu avec conditionnelles (192,79) y tombent.
2. **« Les 58 items ajoutés sont neufs par rapport au v1 »** (§ 2) : seuls les 48 témoins sont des énoncés absents de la sous-banque v1 ; les 10 redoublés sont des énoncés des 150, servis une seconde fois (brouillon 2, « 10 énoncés servis deux fois »). Ce sont 58 appels neufs, pas 58 énoncés neufs. Les effectifs eux-mêmes concordent (150 + 48 + 10 = 208 ; 24 triviaux et 24 grossiers servis, conformes à A4 du brouillon 2).
3. **« Plafond par item : 1,50 »** (§ 2) placé après le coût d'un item S complet (agent + relecteur) : dans le script v1 le plafond borne l'agent seul. Le plafond n'est atteint dans aucun scénario (agent au pire 1,20 ; item au pire 1,272). La phrase « postes dominants : le bras S (plafond par item) » (§ 5) attribue donc le poids du bras S à un plafond qui ne joue pas ; le classement lui-même est juste (S 64,06 puis proposeurs 57,60 à l'attendu ; S 264,58 puis 184,32 au pire, Argon à 4/20).
4. **Appels de fumée** : le § 7, point 2, nomme « Astra et Kimi » ; le brouillon 2 dit « un appel de fumée par modèle » (quatre modèles). Le nombre et la répartition des quatre appels du § 2 ne sont pas écrits ; voir la table pour l'effet sur le montant.
5. **Repli R1 partiellement chiffré** : seul « Astra échoue » est chiffré. « Kimi échoue » (relecteur de S et reformulateur Argon) coûte +7,50 à l'attendu avec Argon à 4/20 (208 relectures + 40 reformulations), +0,00 à 2/10 ; « les deux échouent » (H4 non courue, relecteur Argon) donne 142,85 (2/10) et 155,88 (4/20) (bloc 5). Absents du devis.
6. **Machine (§ 4 contre § 2, P4)** : le § 4 retire de la machine le générateur, les tests de mort et l'analyse, qui faisaient partie de l'enveloppe de 12 / 24 / 48 heures au v1 (§ 2, P4 « génération, bac, tests de mort, analyse »). Les heures ne sont pas réestimées ; le devis le dit (« restent une enveloppe »).
7. **Ligne « appels + machine » absente** au v2 (présente au v1) : 164,69 / 171,89 à l'attendu (30 nov. / 1er déc.), 76,69 / 79,72 au bas, 629,92 / 652,96 au pire (bloc 4).
8. **Convention du bas changée sans le dire** : au v1, le bas prenait le juge Kimi ; au v2, le juge Astra (P1 bas 8,80 contre 3,04 au v1). La comparaison des bas v1 et v2 n'est pas à convention égale.
9. **Profil bas du juge « reconstitué »** : le profil 6k / 2k est écrit tel quel dans le script v1 (`PROFIL_JUGE["bas"]`) ; il n'est pas reconstitué, il est repris. Le chiffre 0,128 est juste.
10. **Course à cheval sur le 1er décembre** : le devis la renvoie au « prix du jour » sans chiffre ; elle est bornée par les deux colonnes, l'écart maximal étant 3,02 (bas), 7,20 (attendu), 23,04 (pire) (bloc 4).

Contrôles sans écart sur le brouillon 2 (bloc 9) : 10 énoncés de forme seuil par monde, dont 6 faux ; P9 (1,00 / 0,50 / 0,50) concorde avec les gabarits écrits.
