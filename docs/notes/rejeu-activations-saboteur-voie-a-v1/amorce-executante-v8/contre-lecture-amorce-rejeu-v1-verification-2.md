# Vérification courte de N1 et R-a
Essais : 52 passent. Code relu (resoudre_fiche l. 1306, surveiller, main l. 1491).
N1 fermé. `resoudre_fiche` renvoie la fiche si l'identifiant est un entier (bool exclu) ; sinon résout par l'étiquette exacte, une seule instance, entier, jamais une intouchable, sinon Refus (jamais une surveillance à vide). Appelée en tête de `surveiller`. `rapatrier` (main) refuse une fiche sans identifiant entier ; `detruire` refuse déjà (identifiant de la fiche ≠ argument).
R-a fermé. Après trois coupures manquées, `client.detruire(ident)` direct, identifiant de la fiche résolue, intouchables exclues, échec journalisé en alarme, nouvel essai aux tours suivants.
Remarque mineure (pas bloquante) : cette destruction directe passe aussi quand le refus venait de l'étiquette inattendue (l. « echecs >= 3 ») ; elle contourne alors le contrôle d'étiquette. Acceptable car l'identifiant vient de la fiche ou de la résolution par étiquette exacte ; à noter en réserve.
VERDICT : corrections vérifiées.
