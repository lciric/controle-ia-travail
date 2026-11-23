from pathlib import Path
p = Path("faire_lanceur_v11.py"); t = p.read_text()
def rr(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:100])
    t = t.replace(a, b)
rr("MAX_SORTIE_CARBON = 49152                     # v11 (flux) : provision 28 672 + texte 20 480 ; la sortie compte la pensée",
   "MAX_SORTIE_CARBON = 65536                     # v11 (flux) : limite en flux ; texte 36 864 au-delà de la provision 28 672")
rr("# pire cas d'un appel : 2 618 × 8,3 + 49 152 × 41,5, par million = 2,061538 USD (sous 3,00).",
   "# pire cas d'un appel : 2 618 × 8,3 + 65 536 × 41,5, par million = 2,741473 USD (sous 3,00).")
rr("   `main` (`relais_gemini_v3.py`, `2cf6bc6d…`, port 8791) ; niveau de réflexion « high », provision 28 672, sortie 49 152\n   (texte 20 480 ≥ 16 000 et > 2 cartes × 9 000 caractères), délai 1 500 + 60 s ;",
   "   `main` (`relais_gemini_v3.py`, `2cf6bc6d…`, port 8791) ; niveau de réflexion « high », provision 28 672, sortie 65 536\n   (limite en flux ; texte 36 864 ≥ 16 000 et > 2 cartes × 9 000 caractères), délai 1 500 + 60 s ;")
a = t.index("2. **couverture de LUC** (GO-2026-11-22-111)")
b = t.index("4. **Astra** :")
t = t[:a] + '''2. **couverture et plafond de la part Claude** (GO-2026-11-22-111, R-4995, brouillon 1 du préenregistrement v11) : relevé de LUC
   = solde lu à la console, recharge déclarée, réserves déclarées (sources écrites) ; la règle « Minuit compté au prix relevé »
   est retirée ; **plafond de la part Claude = min(45 USD ; 4/5 × (solde + recharge − réserves))**, arrondi au centime
   inférieur ; sous 20,65 USD (part Claude estimée) : alerte, pas de départ (**code 3**) ; le relais Claude doit être lancé à ce
   plafond exactement (le relevé précède son lancement) ; 45 USD est lu dans la configuration v11 et égal à la constante du
   lanceur (sinon refus : un plafond retiré ou relevé ne part pas) ;
3. **arrêt au fil de l'eau** : l'état du relais Claude est relu toutes les `intervalle_surveillance_s` secondes ; au **premier
   refus du relais** (statut 402, plafond atteint), à une part engagée (dépense + engagé) qui atteint le plafond, ou à un état
   illisible trois fois de suite : arrêt propre de l'orchestrateur par son PID, alerte scellée `alerte-arret-part-claude.json`,
   **code 5**, sans relance ; le plafond d'arrêt de 150 USD (orchestrateur) ne change pas ;
''' + t[b:]
rr("Codes : 0, 2, 3, 4, 5, 6 comme la v10 ; **7** arrêt propre pour couverture de LUC atteinte ou non comptable ; **8** arrêt propre\nau plafond propre de LUC (45 USD), sans relance.",
   "Codes : 0, 2, 3, 4, 6 comme la v10 ; **5** : arrêt par la garde de crédit d'un relais dispensé (v10) **ou** arrêt propre sur la\npart Claude (premier 402 du relais Claude, plafond atteint, état illisible) — le fichier d'alerte dit lequel.\nArgon : emplacement `argon_v11.plafond_session_juge_usd` de la configuration (vide : en attente du mot de la mère) ; rempli, il\nremplace le plafond de session des juges dans la configuration servie (la garde Google juge ensuite le chemin d'Argon).")
rr("PLAFOND_PART_CLAUDE_USD = 45.0   # R-4995 : plafond propre de LUC ; égal à celui de la configuration v11, sinon refus",
   "PLAFOND_PART_CLAUDE_USD = 45.0   # R-4995 : plafond propre de LUC ; égal à celui de la configuration v11, sinon refus\nPART_DE_LA_COUVERTURE = 0.8      # brouillon 1 du préenregistrement v11 : quatre cinquièmes de la couverture nette")
rr('''            solde, recharge = x.get("solde_console_usd"), x.get("recharge_declaree_usd")
            sources = (x.get("source"), x.get("recharge_source"))
            if x.get("non_lisible") is True or not (_reel_positif(solde) and _reel_positif(recharge)) \\\\
                    or not all(isinstance(s, str) and s.strip() for s in sources):
                raise Refus(f"relevé des crédits : clé {nom} : solde_console_usd et recharge_declaree_usd (nombres ≥ 0) et leurs "
                            "sources (source, recharge_source) exigés (GO-2026-11-22-111) ; « non lisible » n'est pas admis")
            couverture = round(float(solde) + float(recharge), 6)''',
   '''            solde, recharge, reserves = x.get("solde_console_usd"), x.get("recharge_declaree_usd"), x.get("reserves_declarees_usd")
            sources = (x.get("source"), x.get("recharge_source"))
            if x.get("non_lisible") is True or not (_reel_positif(solde) and _reel_positif(recharge) and _reel_positif(reserves)) \\\\
                    or not all(isinstance(s, str) and s.strip() for s in sources):
                raise Refus(f"relevé des crédits : clé {nom} : solde_console_usd, recharge_declaree_usd, reserves_declarees_usd "
                            "(nombres ≥ 0) et les sources (source, recharge_source) exigés (GO-2026-11-22-111) ; « non lisible » "
                            "n'est pas admis")
            couverture = round(float(solde) + float(recharge) - float(reserves), 6)
            plafond_part = math.floor(min(PLAFOND_PART_CLAUDE_USD, PART_DE_LA_COUVERTURE * couverture) * 100 + 1e-9) / 100''')
rr('''                 "solde_console_usd": solde, "recharge_declaree_usd": recharge, "couverture_usd": couverture,''',
   '''                 "solde_console_usd": solde, "recharge_declaree_usd": recharge, "reserves_declarees_usd": reserves,
                 "couverture_usd": couverture, "plafond_part_claude_usd": plafond_part,''')
rr('''                 "regle": "part Claude comptée au fil de l'eau : arrêt propre au plafond propre (45 USD, code 8) ou à la couverture "
                          f"moins {RESERVE_APPEL_CLAUDE_USD} USD (code 7)"}
            motifs = []
            if couverture <= PART_CLAUDE_ESTIMEE_USD:
                motifs.append(f"couverture {couverture} (solde {solde} + recharge {recharge}) ≤ part Claude estimée "
                              f"{PART_CLAUDE_ESTIMEE_USD}")''',
   '''                 "regle": "plafond de la part Claude = min(45 ; 4/5 × (solde + recharge − réserves)) ; relais Claude lancé à ce "
                          "plafond ; arrêt propre au premier 402 du relais (code 5)"}
            motifs = []
            if plafond_part < PART_CLAUDE_ESTIMEE_USD:
                motifs.append(f"plafond de la part Claude {plafond_part} (min(45 ; 4/5 × ({solde} + {recharge} − {reserves}))) < part "
                              f"Claude estimée {PART_CLAUDE_ESTIMEE_USD} : pas de départ")''')
p.write_text(t)
print("ok")
