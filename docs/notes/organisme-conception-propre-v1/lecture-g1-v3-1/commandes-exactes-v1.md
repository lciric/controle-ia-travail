# Commandes exactes — lecture des fiches de la course « conception propre » par Astra, outil v3.1

Opérateur neuf de la session mère ; écrit le 14 novembre 2026 à 10:37 UTC (`date -u`), scellé **avant tout appel
payant**. Sous GO-2026-11-13-06, mots de Lazar R-2679 et R-2707 (palier Flex, effort `medium`, plafond 14,20 USD,
premier appel seul, règle de reprise). Conditions : C1 à C7 (rapport v3.1, § 7, `32f858a6…`), K1 à K9 (relecture
courte, § 6, `e246de7a…`).

## Vérifications faites avant d'écrire ce fichier (10:35 à 10:37 UTC)

- **K1 / C1** : `sha256sum -c` des compagnons : outil `95bc46c1…` OK, classement `f9ef3695…` OK, rapport OK, relecture
  courte OK.
- Fiches `a9f9594e…` : empreinte égale à leur compagnon (calculée par `sha256sum`, fichier non ouvert).
- **K7** : attestation `attestation-lecture-g1-v2.json` = `4bfacd35…` (égale à son compagnon) ; nomme OpenAI,
  `gpt-6-astra`, palier flex, `store` false ; empreinte des fiches `a9f9594e…`.
- **K3** : R-2707 (10:35 UTC), antérieure à `preparer`, porte le mot de Lazar sur E1 (plafond 14,20) et E2 (règle de
  reprise).
- **K8 / C6** : `find . -name 'manifeste-envois-v3*' -not -path './.git/*'` → aucune ligne ; dossier
  `lecture-g1-v3-1/` inexistant avant ce fichier.
- Les six noms de l'environnement réduit sont présents (vérifiés par leur nom seul, `${!v+x}`).
- Hôte : `GET https://api.openai.com/v1/models` sans clé, par `urllib`, environnement réduit sans la clé : **401**
  (10:36:20 UTC).

## Dépense antérieure : 0, et pourquoi (divergence avec la consigne de la mère, dite ici)

La consigne de la mère demandait `--depense-anterieure-usd 6.791087`. Or l'outil porte déjà ce retrait dans sa
constante `PLAFOND_ABSOLU_USD = 14.20  # reste du GO-2026-11-13-06 au 14 novembre (21 − 6,791087)` (ligne 115) et
retranche la dépense antérieure de 14,20 (lignes 542 à 547) : avec 6,791087, le plafond disponible serait 7,41 et
`preparer` refuserait le plafond de 14,20 (refus avant toute écriture). La dépense antérieure de l'outil est celle
« comptée depuis le devis » (message de la ligne 541 ; rapport § 7, point 2 : `0` ; condition **K2** :
`depense_anterieure_usd` = 0 ; K8 : une autre valeur seulement pour une préparation après un dossier arrêté). Je
déclare donc **0** : la borne totale reste 6,791087 + 14,20 = 20,991087 ≤ 21 USD. Rien d'autre ne change.

## Commandes (depuis la racine du dépôt ; `DOS` est une variable du shell, non exportée)

```
DOS=docs/notes/organisme-conception-propre-v1
FICHES=runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json
OUTIL=$DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py
CLASSER=$DOS/lecture-classement-v3-1/classer_conception_propre_v3_1.py
```

1. Préparation :
   `.venv/bin/python -I -B $OUTIL preparer --fiches $FICHES --attestation $DOS/attestations/attestation-lecture-g1-v2.json --sortie $DOS/lecture-g1-v3-1/envois --effort medium --palier flex --plafond-usd 14.20 --depense-anterieure-usd 0`
2. **K2 / C2 / C4** (programme, avant tout appel) : lecture de `$DOS/lecture-g1-v3-1/envois/manifeste-envois-v3-1.json`
   par `json` ; exigés : `palier` = `flex` ; `lecteur.reasoning_effort` = `medium` ; `lecteur.service_tier` = `flex` ;
   prix 5,0 / 0,5 / 25,0 ; `garde_depense.plafond_usd` = 14,2 ; `depense_anterieure_usd` = 0 ; 18 envois ; source des
   prix citant `bf211a07`, sans « SUPPOSÉ » ni « barème » ; empreinte de l'attestation = `4bfacd35…` ; plafond ≥ 9,28.
   **K8** : `find` ci-dessus → une seule ligne. Tout écart : arrêt, aucun appel.
3. **Premier appel seul (C3, C7, K6)**, environnement réduit, la clé passée par son nom (jamais sa valeur sur une ligne) :
   `( for v in $(compgen -e); do case $v in PATH|HOME|HTTPS_PROXY|https_proxy|SSL_CERT_FILE|OPENAI_API_KEY) ;; *) unset "$v";; esac; done; exec .venv/bin/python -I -B $OUTIL envoyer --envois $DOS/lecture-g1-v3-1/envois --envois-max 1 )`
   puis `.venv/bin/python -I -B $OUTIL bilan --envois $DOS/lecture-g1-v3-1/envois`.
4. **K4** (programme, sur la sortie de `bilan`) : `anomalies` vide ; `clotures[0].modele_servi` = `gpt-6-astra` ;
   `palier_servi` = `flex` ; `reasoning_tokens ≤ completion_tokens ≤ 32768` ; `cout_usd ≤ pire_cas_usd` ;
   `cout_usd ≤ (14,20 − 1,054) / 16,4 = 0,8016`, lu **0,80 USD** au plus. Sinon : arrêt et rapport. Règle de reprise
   (R-2707) : si l'échec précède toute génération (refus du palier, paramètre refusé, coupure sans usage), une seule
   reprise, dossier neuf (le dossier arrêté déplacé hors de `docs/` et `runs/` n'est **pas** fait par moi sans relire
   K8 : la reprise déclare en `--depense-anterieure-usd` la somme des `depense_comptee_usd` du dossier arrêté) ; tout
   autre cas : nœud de Lazar.
5. Si K4 tient : même commande qu'au point 3 **sans** `--envois-max` (17 appels), puis `bilan` ; **K5** :
   `pret_pour_verifier: true`, `clos: 18`, `en_vol: []`.
6. **K6 / C7** après l'envoi : commande du point 9 du rapport (un booléen seul affiché) → `False`.
7. `.venv/bin/python -I -B $OUTIL verifier --envois $DOS/lecture-g1-v3-1/envois`
8. **K9** (programme) : dans les deux `lecture-verifiee-L*-v3-1.json`, compter les entrées dont `N.motif` vaut
   « valeur de N illisible » (seul le compte est affiché). S'il y en a : lecture dite incomplète, **classement non
   lancé**.
9. Sinon : `.venv/bin/python -I -B $CLASSER --envois $DOS/lecture-g1-v3-1/envois --sortie $DOS/lecture-g1-v3-1/classement`
   (désignation L5 par défaut ; `detachee-v1` jamais sans mot de Lazar).
10. Garde des secrets à 0 avant chaque commit ; commit et poussée par chemins nommés (dossier `lecture-g1-v3-1/` seul).

Interdits rappelés : plafond 14,20 jamais dépassé ; aucun autre modèle ni palier ; aucune valeur de clé affichée ; ni
fiches, ni témoins, ni réponses ouverts au-delà de ce que l'outil affiche pour ses contrôles.
