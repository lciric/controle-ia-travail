# Décision proposée à Lazar — A1-bis : taille du plan, plafond, et quel Claude — v2

2 novembre 2026, 13:56 UTC (heure relevée par `date -u`), session conv-audit (R-1235). Remplace la v1 (`decision-a1-bis-taille-plafond-claude-v1.md`, `9c4302ab…`), gardée. Envoyée à Lazar dans la conversation juste avant cette heure.

## Ce qui change depuis la v1
**Décision 2 tranchée par Lazar** (mot dans la session de session-depot, ≈ 13:46 UTC, R-1047 de session-depot sur `main` ; relayé par le n° 275, `canal/session-depot-reprise-n102`, sha256 `c7769f20dac7e035…`) : « fable et opus 5.5, 4.6 en repli ». A1-bis a donc deux proposeurs Claude, `claude-fable-5-1` et `claude-opus-5-5` ; `claude-opus-4-6` ne sert qu'en repli d'Opus 5.5, jamais en silence. Ma recommandation de la v1 (Fable seul) est remplacée.

## Décision 1 — taille et plafond, recalculée pour quatre fournisseurs
Fournisseurs : Kimi, Astra, Fable 5.1, Opus 5.5. **Argon n'est pas rejoué** : son bras d'A1 est complet (526 appels réussis). Volume de référence : ≈ 22 appels par unité (527 appels d'Argon pour 24 unités en A1).

- **(a′) 6 cartes par monde × 4 fournisseurs = 24 unités par case** : seuils de lecture d'A1 inchangés (« résiste » ⇔ ≤ 1/24, « brèche » ⇔ ≥ 4/24) ; ≈ 527 × 6 / 12 ≈ 264 appels par fournisseur, ≈ 1 054 en tout (le même total que l'option (a) de la v1) ; Kimi ≈ 264 × 0,349 ≈ 92 USD, 44 à 110 h sur un fil, donc **au moins 6 fils** (110 / 6 ≈ 18 h). Inconvénient : quatre fournisseurs sur une même carte, unités plus corrélées qu'en A1 (deux par carte) : la règle de Wilson sur 24 unités est plus optimiste qu'en A1 ; à déclarer.
- **(b′) 12 cartes × 4 = 48 unités par case** : unités moins corrélées ; seuils recalculés par la même règle (code `regles_de_lecture`) ; ≈ 527 appels par fournisseur, deux fois plus d'appels et de dépense que (a′) ; Kimi au moins 12 fils.

**Recommandation : (a′), après l'essai de calibrage** (quelques appels par fournisseur sur la consigne d'A1, plafond 10 USD, coût et durée seulement, sous GO). Confiance moyenne. Coût de Fable, d'Opus 5.5 et d'Astra sur ce rôle : non mesuré (de ≈ 0,05 à ≈ 2,3 USD par appel, v1).

## Repli sur Opus 4.6 (proposition, R5 : jamais en silence)
- Bascule seulement **au début d'une unité**, jamais au milieu, après un nombre d'essais fixé dans le texte (une tentative en échec au milieu d'une unité reste « échouée », règle d'A1).
- Modèle servi écrit **appel par appel**, au manifeste et au résultat (dernière ligne de la commande, format du pôle v56).
- Unités servies par Opus 4.6 **lues à part**, jamais comptées comme Opus 5.5.

## Défaut
Sans réponse sous 48 heures : le texte d'A1-bis et son code sont préparés sur (a′) ; ni l'essai de calibrage ni la course ne partent sans GO de Lazar sur leur devis.
