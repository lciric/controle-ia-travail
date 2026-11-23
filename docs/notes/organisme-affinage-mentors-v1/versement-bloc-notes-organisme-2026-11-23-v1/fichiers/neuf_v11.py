

# --- v11 : garde des appels à Google (règle gelée de CLAUDE.md, GO-2026-11-21-71) -----------------------------------------------


ROLES_GOOGLE = {"carbon": (("proposeur_ideation", "proposeur", "consigne_proposeur"),),
                "argon": (("proposeur_ideation", "proposeur", "consigne_proposeur"), ("juge_ideation", "juge", "consigne_juge"))}
MOTIF_CAPTURE = "capture du lanceur v11 : rien n'est envoyé"


class FauxAmontGoogle:
    """Faux amont local de l'interface de Google : `countTokens` rend un compte (octets / 4), toute génération
    (`generateContent`, `streamGenerateContent`, `batchGenerateContent`) est **capturée** et reçoit un 503. Aucun réseau."""

    def __init__(self):
        self.captures = []
        moi = self

        class H(BaseHTTPRequestHandler):
            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                brut = self.rfile.read(n)
                try:
                    objet = json.loads(brut or b"{}")
                except ValueError:
                    objet = None
                if self.path.split("?")[0].endswith(":countTokens"):
                    code, rep = 200, {"totalTokens": max(1, len(brut) // 4)}
                else:
                    moi.captures.append({"chemin": self.path, "corps": objet})
                    code, rep = 503, {"error": {"code": 503, "message": MOTIF_CAPTURE}}
                donnees = json.dumps(rep).encode("utf-8")
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(donnees)))
                self.end_headers()
                self.wfile.write(donnees)

            def do_GET(self):
                self.send_response(404)
                self.end_headers()

            def log_message(self, *a):
                pass

        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.serveur.daemon_threads = True
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"

    def fermer(self):
        self.serveur.shutdown()
        self.serveur.server_close()


def charger_garde_google(chemin: Path, attendu: str):
    if not chemin.is_file() or sha256_fichier(chemin) != attendu:
        raise Refus(f"garde des appels à Google absente ou d'une autre empreinte que {attendu[:12]}… ({chemin})")
    spec = importlib.util.spec_from_file_location("garde_google_pour_lanceur_affinage_v11", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def arguments_enveloppe_argon(enveloppe: Path) -> list:
    """Arguments que l'enveloppe d'Argon (épinglée) passe à sa commande : ceux de sa ligne `exec` (lignes continuées
    jointes), après `"$COMMANDE"`, `"$@"` retiré (l'orchestrateur n'en passe aucun)."""
    texte = enveloppe.read_text(encoding="utf-8").replace("\\\n", " ")
    lignes = [l for l in texte.splitlines() if l.strip().startswith("exec ")]
    if len(lignes) != 1:
        raise Refus(f"enveloppe d'Argon : {len(lignes)} ligne(s) « exec » (une exigée)")
    jetons = shlex.split(lignes[0])
    if "$COMMANDE" not in jetons:
        raise Refus("enveloppe d'Argon : « $COMMANDE » absent de la ligne exec")
    return [j for j in jetons[jetons.index("$COMMANDE") + 1:] if j != "$@"]


def _remplacer_option(args: list, option: str, valeur: str) -> list:
    if option not in args:
        return list(args) + [option, valeur]
    out = list(args)
    for k, a in enumerate(out[:-1]):
        if a == option:
            out[k + 1] = valeur
    return out


def capturer_corps_google(python: str, commande: Path, args: list, env_plus: dict, consigne: str) -> dict:
    """Joue la commande épinglée hors ligne devant le faux amont ; rend {code, captures}."""
    amont = FauxAmontGoogle()
    try:
        env = {"PATH": os.environ.get("PATH", os.defpath), "LANG": "C.UTF-8", **env_plus}
        p = subprocess.run([python, "-I", "-B", str(commande)] + _remplacer_option(args, "--url-base", amont.url + "/v1beta"),
                           input=consigne.encode("utf-8"), env=env, capture_output=True, timeout=180)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"garde Google : commande {commande.name} non jouée hors ligne ({type(e).__name__})") from None
    finally:
        amont.fermer()
    return {"code": p.returncode, "captures": amont.captures}


def corps_de_generation(capture: dict) -> tuple:
    """(corps de génération, mode de la garde) : lot → la requête unique du lot ; flux ou synchrone → le corps lui-même. Le
    relais v3 passe un `generateContent` à l'amont en flux : une commande qui parle au port de Carbon est en mode « flux »."""
    chemin, corps = capture["chemin"].split("?")[0], capture["corps"]
    if not isinstance(corps, dict):
        return None, None
    if chemin.endswith(":batchGenerateContent"):
        try:
            return corps["batch"]["input_config"]["requests"]["requests"][0]["request"], "non_diffuse"
        except (KeyError, IndexError, TypeError):
            return None, "non_diffuse"
    return corps, ("flux" if chemin.endswith(":streamGenerateContent") else "non_diffuse")


def _provision(args: list, corps: dict):
    v = _valeur_arg(args, "--provision-pensee-jetons")
    if v is not None:
        try:
            return int(float(v))
        except ValueError:
            return None
    pensee = ((corps or {}).get("generationConfig") or {}).get("thinkingConfig") or {}
    return pensee.get("thinkingBudget")


def controler_chemins_google(r: "Reglages", decl: dict, pieces: dict, fixe: dict, liste: dict) -> dict:
    """Pour chaque commande Google déclarée (Argon, Carbon) et chaque rôle qu'elle tient : corps réel capturé hors ligne,
    `verifier_reglages_google` de la garde épinglée (mode « flux » pour Carbon, que le relais v3 sert en flux ; « non diffusé »
    pour Argon et le lot), limite de l'invite d'un proposeur (cartes × 9 000 caractères, un jeton au plus par caractère) sous
    le plafond de texte. Rend {espèce: {conforme, roles}} ; aucune consigne n'y est écrite."""
    garde_chemin = Path(pieces["garde_google"]["absolu"])
    garde = charger_garde_google(garde_chemin, pieces["garde_google"]["sha256"])
    plus_long = max((texte_de_case(f) for f in liste["fils"]), key=len)
    out = {"garde": {"chemin": pieces["garde_google"]["chemin"], "sha256": pieces["garde_google"]["sha256"],
                     "version": getattr(garde, "VERSION_GARDE", None)}}
    for nom in ("argon", "carbon"):
        b = decl["fournisseurs"].get(nom)
        if b is None:
            continue
        if nom == "carbon":
            c = b["commande"]
            commande, args, env_cle = Path(c[3]), (_remplacer_option(list(c[4:]), "--garde", str(garde_chemin)) if "--garde" in c[4:] else list(c[4:])), {}
        else:
            commande = Path(pieces["commande_argon"]["absolu"])
            args = arguments_enveloppe_argon(Path(pieces["enveloppe_argon"]["absolu"]))
            env_cle = {"GEMINI_API_KEY": "factice-relais"}  # comme l'enveloppe : jeton factice, la vraie clé reste au relais
        roles = []
        for role_pole, role_plafond, consigne_piece in ROLES_GOOGLE[nom]:
            consigne = consigne_servie_proposeur(Path(pieces[consigne_piece]["absolu"]).read_text(encoding="utf-8"), plus_long)
            env = dict(env_cle, PLAFOND_SESSION_USD=str(fixe["plafonds_session"][role_plafond]), ROLE_POLE=role_pole)
            jeu = capturer_corps_google(r.python, commande, args, env, consigne)
            problemes, reglages = [], None
            gens = [corps_de_generation(x) for x in jeu["captures"]]
            if len(gens) != 1 or gens[0][0] is None:
                problemes.append(f"aucun corps de génération capturé (code {jeu['code']}, {len(gens)} capture(s)) : la "
                                 "commande n'a pas atteint l'envoi, rien ne peut être vérifié")
            else:
                corps, mode = gens[0]
                if nom == "carbon":
                    mode = "flux"
                provision = _provision(args, corps)
                problemes += list(garde.verifier_reglages_google(nom, corps, provision=provision, mots=None, mode=mode))
                config = corps.get("generationConfig") if isinstance(corps.get("generationConfig"), dict) else {}
                reglages = {"mode": mode, "provision": provision, "maxOutputTokens": config.get("maxOutputTokens"),
                            "thinkingConfig": config.get("thinkingConfig")}
                plafond = config.get("maxOutputTokens")
                if role_plafond == "proposeur" and isinstance(plafond, int) and isinstance(provision, int):
                    limite = int(fixe.get("cartes_par_appel") or 1) * CARACTERES_PAR_CARTE_MAX
                    if limite >= plafond - provision:
                        problemes.append(f"limite de l'invite : {limite} caractères (≤ {limite} jetons) ≥ plafond de texte "
                                         f"{plafond - provision}")
            roles.append({"role": role_pole, "plafond_session_usd": fixe["plafonds_session"][role_plafond],
                          "code_commande": jeu["code"], "reglages_captures": reglages, "problemes": problemes})
        out[nom] = {"commande": str(commande), "commande_sha256": sha256_fichier(commande), "roles": roles,
                    "conforme": all(not x["problemes"] for x in roles)}
    return out


def verifier_palier_astra(pieces: dict, liste: dict) -> dict:
    """v11 : prix d'Astra à palier (R-4905) : l'entrée la plus longue servie (consigne servie en octets, plus les 1 024 octets
    de marge de la commande d'Astra ; un jeton au plus par octet) reste sous 272 000 jetons."""
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    borne = max(len(consigne_servie_proposeur(consigne, expurger(texte_de_case(f))[0]).encode("utf-8")) for f in liste["fils"]) + 1024
    if borne >= PALIER_ASTRA_JETONS:
        raise Refus(f"Astra : entrée bornée à {borne} jetons ≥ palier {PALIER_ASTRA_JETONS} : prix 16 / 60, hors devis")
    return {"borne_entree_jetons": borne, "palier_jetons": PALIER_ASTRA_JETONS, "prix_usd_par_million": list(PRIX_ASTRA)}


# --- v11 : part Claude sur LUC, comptée au fil de l'eau (couverture, GO-2026-11-22-111 ; plafond propre, R-4995) --------------


STATUTS_REFUS_INTERFACE = (400, 401, 402, 403)  # v11 : refus de l'interface (crédit, clé) ou du relais (402, plafond)


class SurveillanceCleClaude:
    """GO-2026-11-22-124. Relit l'état du relais Claude et son journal (statuts seulement) ; `depasse()` rend {code: 7, motif}
    ou None : premier refus du relais (état `refus` > 0 : 402, plafond atteint), premier statut de refus de l'interface au journal
    (400, 401, 402, 403 : crédit insuffisant, clé, plafond), part engagée (dépense + réservé des appels en vol) au plafond propre,
    ou état ou journal illisible trois fois de suite. Une lecture manquée isolée est comptée, jamais tue."""

    def __init__(self, r: "Reglages", url: str, plafond_part: float, journal: str | None = None):
        self.r, self.url, self.plafond_part, self.journal = r, url, plafond_part, journal
        self.illisibles, self.lectures, self.derniere, self.refus, self.vu = 0, 0, None, None, 0

    def _refus_au_journal(self):
        if not self.journal:
            return None
        p = Path(self.journal)
        if not p.exists():
            return None  # aucun appel encore : le relais crée son journal au premier appel
        lignes = p.read_text(encoding="utf-8", errors="replace").splitlines()
        for ligne in lignes[self.vu:]:
            if not ligne.strip():
                continue
            o = json.loads(ligne)  # une ligne illisible lève : comptée comme lecture manquée
            if o.get("statut") in STATUTS_REFUS_INTERFACE:
                return o.get("statut"), o.get("motif") or o.get("chemin")
        self.vu = len(lignes)
        return None

    def depasse(self):
        try:
            etat = (self.r.lire_etat_relais or _etat_relais)(self.url)
            engagee = float(etat.get("depense_usd") or 0.0) + float(etat.get("engage_usd") or 0.0)
            refus = etat.get("refus", 0) or 0
            if not (math.isfinite(engagee) and _nombre(refus)):
                raise ValueError("non fini")
            interface = self._refus_au_journal()
        except Exception as e:  # noqa: BLE001
            self.illisibles += 1
            if self.illisibles >= LECTURES_ILLISIBLES_MAX:
                return {"code": 7, "motif": f"état ou journal du relais Claude illisible {self.illisibles} fois de suite "
                                            f"({type(e).__name__}) : part Claude non comptable"}
            return None
        self.illisibles, self.lectures = 0, self.lectures + 1
        self.derniere, self.refus = round(engagee, 6), refus
        if interface:
            return {"code": 7, "motif": f"premier refus de l'interface lu au journal du relais Claude (statut {interface[0]}, "
                                        f"{str(interface[1])[:120]}) ; part engagée {self.derniere} USD"}
        if refus > 0:
            return {"code": 7, "motif": f"premier refus du relais Claude ({refus} refus : statut 402, plafond de la part Claude "
                                        f"{self.plafond_part} USD atteint) ; part engagée {self.derniere} USD"}
        if engagee >= self.plafond_part - 1e-9:
            return {"code": 7, "motif": f"part Claude engagée {self.derniere} USD ≥ plafond de la part Claude {self.plafond_part} USD"}
        return None

    def bilan(self) -> dict:
        return {"plafond_part_claude_usd": self.plafond_part, "lectures": self.lectures, "derniere_part_engagee_usd": self.derniere,
                "refus_du_relais": self.refus, "illisibles_de_suite": self.illisibles, "journal": self.journal}


# --- (6) orchestrateur --------------------------------------------------------------------------------------------------------
