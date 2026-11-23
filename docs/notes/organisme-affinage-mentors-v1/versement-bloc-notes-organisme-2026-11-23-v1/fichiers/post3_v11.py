_a = src.index("2. **couverture et plafond de la part Claude**")
_b = src.index("4. **Astra** :")
src = src[:_a] + '''2. **part Claude sur LUC** (GO-2026-11-22-124, mots de Lazar, qui simplifie GO-2026-11-22-111) : le solde de LUC n'est pas lu
   et n'est pas une condition de départ (recharge automatique) ; aucun plancher ni couverture déclarée ; la règle « Minuit
   compté au prix relevé » est retirée ; **plafond propre de la part Claude : 45 USD** (R-4995), paramètre nommé
   `changements_v11.plafond_part_claude_usd` de la configuration v11, égal à la constante du lanceur (sinon refus : un plafond
   retiré ou relevé ne part pas) ; le relais Claude est lancé à ce plafond exactement ; GO-2026-11-22-124 est lu au registre et
   prolonge l'exception GO-2026-11-22-107 au 15 décembre ;
3. **arrêt au fil de l'eau** : l'état du relais Claude et son journal (statuts seulement, jamais de texte) sont relus toutes
   les `intervalle_surveillance_s` secondes ; au **premier refus de l'interface** (statut 400, 401, 402 ou 403 au journal :
   crédit insuffisant, clé, plafond), au premier refus du relais (état `refus` > 0, 402), à une part engagée (dépense +
   montants réservés des appels en vol) qui atteint 45 USD, ou à un état ou un journal illisible trois fois de suite : arrêt
   propre de l'orchestrateur par son PID, alerte scellée `alerte-arret-part-claude.json`, **code 7**, sans relance ; le plafond
   d'arrêt de 150 USD ne change pas ;
''' + src[_b:]
r('''Codes : 0, 2, 3, 4, 6 comme la v10 ; **5** : arrêt par la garde de crédit d'un relais dispensé (v10) **ou** arrêt propre sur la
part Claude (premier 402 du relais Claude, plafond atteint, état illisible) — le fichier d'alerte dit lequel.''',
  '''Codes : 0, 2, 3, 4, 5, 6 comme la v10 ; **7** : arrêt propre sur la part Claude (premier refus de l'interface ou du relais
Claude, plafond de 45 USD atteint, état ou journal illisible), sans relance.''')
r('''# v11 : part Claude estimée du devis v10 (deux proposeurs, aiguilleur, premier juge ; marge comprise ; table du § 4) ; la
# couverture de LUC (solde + recharge déclarés) doit la dépasser avant le départ ; puis compte au fil de l'eau.''',
  '''# v11 : part Claude estimée et haut du devis v10 (deux proposeurs, aiguilleur, premier juge ; marge comprise ; table du § 4) :
# écrits au manifeste pour information ; GO-2026-11-22-124 : aucune condition de départ sur le solde de LUC.''')
r('''    - v11 : clé Claude (LUC) : `solde_console_usd` et `recharge_declaree_usd` (nombres ≥ 0, sources écrites) exigés ;
      couverture = leur somme ; alerte (code 3) si elle ne dépasse pas la part Claude estimée ; la part au pire (150) n'y est
      plus confrontée (compte au fil de l'eau pendant la course, `SurveillanceCleClaude`) ; « non lisible » refusé.''',
  '''    - v11 (GO-2026-11-22-124) : clé Claude (LUC) : aucune condition (solde non lu, recharge automatique) ; la ligne du relevé,
      si elle est écrite, est recopiée pour information ; la part Claude est tenue par le plafond propre et l'arrêt au premier
      refus de l'interface (`SurveillanceCleClaude`).''')
r('''# --- v11 : part Claude sur LUC, comptée au fil de l'eau (couverture, GO-2026-11-22-111 ; plafond propre, R-4995) --------------''',
  '''# --- v11 : part Claude sur LUC, comptée au fil de l'eau (GO-2026-11-22-124 ; plafond propre, R-4995) -------------------------''')
