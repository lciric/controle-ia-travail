# Vérification des corrections : collisionneur v9-v8l (da282cf7…), v2

**Verdict : conforme.** Aucun bloquant ne reste. Les essais passent : 507, et 11 sautés, sans aucune clé dans l'environnement.

**Redirection (vérifiée en premier, avec un vrai transport et deux serveurs locaux)**
- Codes essayés : 301, 302, 303, 307, 308, 300 et 305.
- Chaque fois, `envoyer` lève un refus nommé (« REDIRECTION_REFUSEE »).
- Le second hôte n'est jamais contacté, ni l'en-tête d'autorisation transmis.
- Couverture : envois, comptages et relevés d'OpenAI passent tous par `ouvrir`. Un relevé redirigé demande l'annulation et compte l'envoi au pire.

**Bloquants 1 à 5 : portés**
- Kimi est borné à 128 000 jetons ; pire cas de 1,38 USD pour 50 000 jetons d'entrée.
- Délai de 10 800 s par appel sous `--sortie-max`, déclaré supposé et journalisé ; un délai manquant est refusé.
- Opus 4.6 reçoit la réflexion adaptative.
- L'absence d'effort est déclarée pour Astra et pour le relais de Kimi.
- Les deux gardes d'argent ont maintenant leur essai.
- N2, N3, N4 et N6 sont portés aussi.

**Sans option**
- Réglages et devis sont ceux de la v8j sur les 120 compositions des sept anciennes espèces.
- Le fichier `especes.json` scellé est inchangé quand aucune option n'est donnée : les anciens runs restent repris.

**Opus 4.6 à l'effort « max » sans `--effort-max`**
- La règle « sans option, rien ne change » n'est pas cassée : l'espèce n'existait pas dans la v8j, et aucun réglage d'une composition de la v8j ne change.
- Pas d'effet sur l'argent : le pire cas reste borné par le plafond (64 000 jetons).
- Mais l'arbitre a dit « comme les autres modèles d'Anthropic », et les autres ne sont à « max » qu'avec l'option. Pour Opus 4.6, `--effort-max` ne fait donc rien.
- Recommandation, non bloquante, à soumettre à l'arbitre : réflexion adaptative toujours, effort « high » par défaut et « max » avec l'option.

**Mutants : 29 rejoués, 26 pris, 3 survivants**
- Les deux survivants des gardes d'argent (K4, K6) sont maintenant pris.
- Les 13 mutants neufs de la v8l (R1 à R13) sont tous pris, dont les trois sur la redirection.
- Restent les trois non-bloquants déjà signalés : K5, K13, K14.

**Non porté et non bloquant :** N1, l'usage lu seulement au morceau de fin.
