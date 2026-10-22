# Red-Team d'Argon

## Attaque sur Fable et Opus
- Ils ignorent l'overhead VRAM massif d'un steering de 29+ têtes lors du décodage sur A100.
- Ils négligent le plafond opérationnel de `R10` et l'architecture de `instrument_p4_v1.py`.

## Duel d'Hypothèses ($H_A \perp H_B$)
$H_A$ : L'intervention causale ($lpha>0$) suffit à restaurer la clairvoyance du Rédacteur.
$H_B$ : L'hystérésis du KV-cache prévaut, exigeant formellement l'application de `R2` (isolation du Relecteur).
Seul l'exécution sur GPU tranchera.
