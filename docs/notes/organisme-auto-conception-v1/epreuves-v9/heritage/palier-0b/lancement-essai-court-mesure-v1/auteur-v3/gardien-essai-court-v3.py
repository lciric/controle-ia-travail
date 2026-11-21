"""Gardien de l'essai court de mesure du palier 0b — v3 (corrections 1 à 6 de l'erratum 1, et 1 à 2 de l'erratum 2).

v3, erratum 2 :
  1. Le gardien ne part pas tant qu'un descendant relevé (identifiant et heure de départ égaux) vit : processus lancé absent,
     il garde ses lignes, l'arrêt de place et l'arrêt de mesure, appliqués à ces descendants par identifiant (signal de fin,
     puis arrêt forcé au délai ; au groupe aussi s'il porte encore un descendant relevé) ; il part quand tous sont absents,
     avec une dernière ligne qui le dit.
  2. « Dossier figé » prouvé : après l'arrêt et avant la mesure, deux relevés (n, nombre de fichiers, octets apparents et
     alloués du dossier etape-4) à une seconde d'écart ; « figé » seulement s'ils sont égaux ; sinon au plus dix paires, puis
     « dossier NON figé » avec les deux derniers relevés, la projection marquée de même.

Lancé détaché (demarrer-gardien-essai-court-v2.sh). Une ligne par intervalle (valeur d'emploi : 60 s) dans
DOSSIER_DE_TENUE/journal-de-tenue-essai-court.txt : heure, identifiant de démarrage, processus vivant, absent ou non identifié
(par /proc/PID), étape en cours, étapes dont le manifeste existe, présence d'un fichier d'arrêt (toute entrée dont le nom
commence par « arret », à toute profondeur du dossier des sorties, noms seulement), n (dossiers de source présents sous
etape-4/couche-mecanique/bras-1-a-3/ à la profondeur proposeur/dose/source, sur 648), descendants vivants relevés, octets
occupés par le dossier des sorties (apparents et alloués), octets libres du système de fichiers.

Il n'interprète aucun contenu des sorties : ses décisions ne dépendent que de noms, tailles et heures de fichiers. Seule lecture
d'octets, permise par la session (erratum 1, correction 5) : l'inventaire d'une étape close (dès que son manifeste et son
compagnon existent) porte les empreintes de ses fichiers, donc les octets en sont hachés, sans être interprétés. Il ne
supprime rien.

Identité (correction 1) : l'heure de départ du processus (22e champ de /proc/PID/stat, en tops depuis le démarrage de la
machine), écrite au lancement par le script de départ dans depart-processus-essai-court.txt, est comparée avant tout signal à
celle que le gardien relit ; un écart, un fichier absent ou illisible, un autre démarrage : aucun signal, raison écrite.

Descendants (correction 3) : à chaque tour, le gardien relève l'arbre des descendants du processus lancé par la chaîne des
parents dans /proc/*/stat (identifiants seulement) et garde chaque identifiant vu avec son heure de départ.

Arrêt (corrections 2 et 3), dans deux cas seulement, écrits dans arret-gardien.txt avec la raison et l'heure :
  - arrêt de place : octets libres sous le seuil (valeur d'emploi : 8 000 000 000 octets) ;
  - arrêt de mesure : le manifeste de l'étape 3 existe, et n atteint le seuil (13), ou l'étape 4 dure depuis plus de la durée
    (45 min, comptée depuis t3) — la première des deux.
Signal de fin au groupe écrit (pgid-essai-court.txt), et, par identifiant, à chaque descendant relevé hors du groupe encore
vivant avec la même heure de départ ; attente que TOUS les membres du groupe (trouvés par leur numéro de groupe dans
/proc/*/stat) et tous ces descendants aient disparu ; s'il en reste un au délai (valeur d'emploi : 60 s) : arrêt forcé du
groupe, et par identifiant des descendants hors du groupe.

Mesure instantanée (correction 4) : à l'arrêt de mesure, le signal part d'abord ; t_arrêt est l'heure de son envoi ; n et s4
sont relevés après la fin de tous les processus, sur le dossier figé ; mesure-essai-court.txt porte t3, t_arrêt, n, s4 et les
deux projections du complément (bornes basses ; n >= 2 exigé, sinon « projection impossible » ; au-delà de quatre heures de
durée projetée, la mention « relance entière peu sûre entre deux redémarrages »).

Il s'arrête lui-même quand le programme (le processus lancé) est absent, après une dernière ligne.
"""
import argparse
import datetime
import hashlib
import os
import signal
import stat
import sys
import time

TOTAL_SOURCES = 648
SORTIES_EMPLOI = "/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1"
TENUE_EMPLOI = "/home/user/journaux-palier-0b-essai-court-v1/"
SOUS_DOSSIER_SOURCES = ("etape-4", "couche-mecanique", "bras-1-a-3")
ETAPES = ("3", "4", "5", "6")
PREFIXE_ARRET = "arret"
QUATRE_HEURES_S = 4 * 3600
MENTION_QUATRE_HEURES = "relance entière peu sûre entre deux redémarrages"


def heure(t=None):
    t = time.time() if t is None else t
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def lire_valeur(chemin):
    with open(chemin, encoding="ascii") as fh:
        return fh.read().strip()


def lire_valeur_ou_none(chemin):
    try:
        return lire_valeur(chemin)
    except (FileNotFoundError, UnicodeDecodeError, IsADirectoryError):
        return None


def boot_id():
    return lire_valeur("/proc/sys/kernel/random/boot_id")


def lire_stat(pid):
    """État, parent, groupe, session, heure de départ (tops depuis le démarrage) lus dans /proc/PID/stat ; None si absent."""
    try:
        with open(f"/proc/{pid}/stat", encoding="ascii", errors="replace") as fh:
            s = fh.read()
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None
    champs = s[s.rindex(")") + 2:].split()
    # champs[0] = état (3e champ), [1] = parent (4e), [2] = groupe (5e), [3] = session (6e), [19] = heure de départ (22e)
    return {"pid": pid, "etat": champs[0], "parent": int(champs[1]), "groupe": int(champs[2]), "session": int(champs[3]),
            "depart": int(champs[19])}


def present(s):
    """Un processus compte s'il existe et n'est pas un zombie (déjà fini, en attente de son parent)."""
    return s is not None and s["etat"] not in ("Z", "X")


def table_processus():
    """Tous les processus visibles, par identifiant : lecture de /proc/*/stat (identifiants seulement, aucun motif)."""
    t = {}
    for nom in os.listdir("/proc"):
        if nom.isdigit():
            s = lire_stat(int(nom))
            if s is not None:
                t[s["pid"]] = s
    return t


def heure_de_depart_murale(tops):
    """Heure murale du départ d'un processus : btime (/proc/stat) + tops / SC_CLK_TCK ; pour le journal seulement."""
    try:
        with open("/proc/stat", encoding="ascii") as fh:
            for l in fh:
                if l.startswith("btime "):
                    return heure(int(l.split()[1]) + tops / os.sysconf("SC_CLK_TCK"))
    except (OSError, ValueError):
        pass
    return "inconnue"


def parcourir(chemin):
    """Une passe, par lstat seulement : (octets apparents, octets alloués, nombre d'entrées non dossiers, chemins relatifs des
    entrées dont le nom commence par PREFIXE_ARRET). (0, 0, 0, []) si absent. Ne suit aucun lien."""
    apparents = alloues = fichiers = 0
    arrets = []
    if not os.path.lexists(chemin):
        return 0, 0, 0, []
    pile = [chemin]
    while pile:
        c = pile.pop()
        try:
            st = os.lstat(c)
        except FileNotFoundError:
            continue
        apparents += st.st_size
        alloues += st.st_blocks * 512
        if c != chemin and os.path.basename(c).startswith(PREFIXE_ARRET):
            arrets.append(os.path.relpath(c, chemin))
        if stat.S_ISDIR(st.st_mode):
            try:
                with os.scandir(c) as it:
                    for e in it:
                        pile.append(e.path)
            except (FileNotFoundError, NotADirectoryError):
                continue
        else:
            fichiers += 1
    return apparents, alloues, fichiers, sorted(arrets)


def sous_dossiers(chemin):
    try:
        with os.scandir(chemin) as it:
            return sorted(e.path for e in it if e.is_dir(follow_symlinks=False))
    except (FileNotFoundError, NotADirectoryError):
        return []


def compter_sources(sorties):
    """n : dossiers présents à la profondeur proposeur/dose/source sous etape-4/couche-mecanique/bras-1-a-3/."""
    base = os.path.join(sorties, *SOUS_DOSSIER_SOURCES)
    n = 0
    for proposeur in sous_dossiers(base):
        for dose in sous_dossiers(proposeur):
            n += len(sous_dossiers(dose))
    return n


def octets_libres(chemin):
    """Octets libres (disponibles hors réserve) du système de fichiers qui porte `chemin` ou son plus proche parent présent."""
    c = os.path.abspath(chemin)
    while not os.path.exists(c):
        c = os.path.dirname(c)
    st = os.statvfs(c)
    return st.f_bavail * st.f_frsize, c


def manifeste(sorties, etape):
    return os.path.join(sorties, f"etape-{etape}", "manifeste.json")


def projection(t3, t_arret, n, s4, total=TOTAL_SOURCES):
    """Les deux projections du complément 1 v3 (bornes basses) : durée (t_arrêt − t3) × total / (n − 1) ; place
    s4 × total / (n − 1). None si n < 2 (projection impossible)."""
    if n < 2:
        return None
    return {"duree_s": (t_arret - t3) * total / (n - 1), "place_octets": s4 * total / (n - 1)}


def lignes_projection(t3, t_arret, n, s4_alloc, s4_app, total=TOTAL_SOURCES):
    """Lignes de projection écrites dans mesure-essai-court.txt (marquées « borne basse » ; mention au-delà de 4 h)."""
    p_alloc = projection(t3, t_arret, n, s4_alloc, total)
    p_app = projection(t3, t_arret, n, s4_app, total)
    if p_alloc is None:
        return [f"projection impossible (n = {n} < 2)"]
    d = p_alloc["duree_s"]
    lignes = [f"durée projetée de l'étape 4, borne basse : (t_arrêt − t3) × {total} / (n − 1) = ({t_arret:.6f} − {t3:.6f}) × "
              f"{total} / {n - 1} = {d:.1f} s ({d / 3600:.3f} h)",
              f"place projetée de l'étape 4, borne basse : s4 × {total} / (n − 1) = {s4_alloc} × {total} / {n - 1} = "
              f"{p_alloc['place_octets']:.0f} octets alloués ({p_alloc['place_octets'] / 1e9:.3f} Go)",
              f"place projetée, borne basse (octets apparents) : {s4_app} × {total} / {n - 1} = "
              f"{p_app['place_octets']:.0f} octets ({p_app['place_octets'] / 1e9:.3f} Go)"]
    if d > QUATRE_HEURES_S:
        lignes.append(f"durée projetée au-delà de quatre heures : {MENTION_QUATRE_HEURES}")
    return lignes


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def ecrire_compagnon(chemin):
    sha = sha256_fichier(chemin)
    with open(chemin + ".sha256", "x", encoding="ascii") as fh:
        fh.write(f"{sha}  {os.path.basename(chemin)}\n")
        fh.flush()
        os.fsync(fh.fileno())
    return sha


class Gardien:
    def __init__(self, a):
        self.a = a
        self.tenue = a.tenue
        self.sorties = a.sorties
        self.journal = os.path.join(self.tenue, "journal-de-tenue-essai-court.txt")
        self.f_arret = os.path.join(self.tenue, "arret-gardien.txt")
        self.f_mesure = os.path.join(self.tenue, "mesure-essai-court.txt")
        self.pid = int(lire_valeur(os.path.join(self.tenue, "pid-essai-court.txt")))
        pg = lire_valeur(os.path.join(self.tenue, "pgid-essai-court.txt"))
        self.pgid = int(pg) if pg.isdigit() else None
        self.boot_ecrit = lire_valeur(os.path.join(self.tenue, "boot-id-essai-court.txt"))
        dep = lire_valeur_ou_none(os.path.join(self.tenue, "depart-processus-essai-court.txt"))
        self.depart_ecrit = int(dep) if (dep is not None and dep.isdigit()) else None
        self.depart_brut = "(fichier absent)" if dep is None else dep
        self.vus = {}  # descendants relevés (hors le processus lancé) : identifiant -> heure de départ (tops)
        self.arret_fait = None
        self.chef_confirme = False  # vrai dès qu'un relevé a vu le processus lancé identifié (v3)
        self.note_reste = False  # vrai dès que la ligne « garde continuée sur les descendants » est écrite (v3)
        s = lire_stat(self.pid)
        lu = s["depart"] if s is not None else None
        self.ecrire(f"prise de garde {heure()} : processus {self.pid}, groupe {pg}, démarrage écrit {self.boot_ecrit} "
                    f"(lu {boot_id()}), heure de départ écrite (tops) {self.depart_brut}, heure de départ lue (tops) {lu} "
                    f"({heure_de_depart_murale(lu) if lu is not None else 'processus absent'}), sorties {self.sorties}, "
                    f"seuil de place {a.seuil_libre_octets} o, seuil n {a.seuil_n}, durée de l'étape 4 {a.duree_etape_4_s} s, "
                    f"intervalle {a.intervalle_s} s, délai d'arrêt forcé {a.delai_force_s} s, total {a.total}, "
                    f"gardien processus {os.getpid()}")
        ok, pourquoi = self.identite()
        self.ecrire(f"identité à la prise de garde : {'confirmée' if ok else 'NON confirmée'} ({pourquoi})"
                    + ("" if ok else " ; aucun signal ne partira tant qu'elle ne sera pas confirmée"))

    # -- écriture
    def ecrire(self, texte, fichier=None):
        with open(fichier or self.journal, "a", encoding="utf-8") as fh:
            fh.write(texte + "\n")
            fh.flush()
            os.fsync(fh.fileno())

    def ligne(self, champs):
        self.ecrire(" ; ".join(f"{k}={v}" for k, v in champs))

    # -- identité (correction 1)
    def identite(self):
        """(confirmée, raison). Confirmée seulement si : même démarrage, heure de départ écrite lisible, processus présent
        (non zombie), heure de départ lue égale à l'écrite, groupe écrit connu, égal à l'identifiant et au groupe lu."""
        if boot_id() != self.boot_ecrit:
            return False, "autre démarrage de la machine"
        if self.depart_ecrit is None:
            return False, f"heure de départ écrite absente ou illisible ({self.depart_brut})"
        s = lire_stat(self.pid)
        if not present(s):
            return False, f"processus {self.pid} absent"
        if s["depart"] != self.depart_ecrit:
            return False, (f"heure de départ lue {s['depart']} différente de l'écrite {self.depart_ecrit} "
                           f"(identifiant repris ou fichiers périmés)")
        if self.pgid is None:
            return False, "groupe inconnu au départ"
        if self.pgid != self.pid or s["groupe"] != self.pgid:
            return False, f"groupe lu {s['groupe']}, groupe écrit {self.pgid}, processus {self.pid} : pas le chef du groupe écrit"
        return True, "processus présent, même démarrage, même heure de départ qu'au lancement, chef du groupe écrit"

    def etat_programme(self):
        """« vivant » (identité tenue), « absent » (fini, autre démarrage, ou identifiant repris), « non identifié »
        (présent, mais heure de départ écrite absente ou illisible : aucun signal possible)."""
        if boot_id() != self.boot_ecrit:
            return "absent"
        s = lire_stat(self.pid)
        if not present(s):
            return "absent"
        if self.depart_ecrit is None:
            return "non identifié"
        return "vivant" if s["depart"] == self.depart_ecrit else "absent"

    # -- descendants (correction 3)
    def relever_descendants(self, table=None):
        """Ajoute à self.vus les descendants présents du processus lancé (chaîne des parents), en partant du processus lancé
        s'il est identifié, et de chaque descendant déjà vu encore présent avec la même heure de départ (les orphelins d'un
        descendant vu restent ainsi atteints). Rend la table lue."""
        table = table_processus() if table is None else table
        racines = []
        if self.etat_programme() == "vivant":  # même démarrage, présent, même heure de départ qu'au lancement
            racines.append(self.pid)
            self.chef_confirme = True
        racines += [p for p, d in self.vus.items() if present(table.get(p)) and table[p]["depart"] == d]
        enfants = {}
        for s in table.values():
            enfants.setdefault(s["parent"], []).append(s)
        pile = list(racines)
        dejavu = set(pile)
        while pile:
            p = pile.pop()
            for s in enfants.get(p, []):
                if s["pid"] in dejavu or s["pid"] == os.getpid():
                    continue
                dejavu.add(s["pid"])
                if present(s) and s["pid"] != self.pid and s["pid"] not in self.vus:
                    self.vus[s["pid"]] = s["depart"]
                pile.append(s["pid"])
        return table

    def membres_du_groupe(self, table):
        """Membres présents du groupe écrit (même numéro de groupe et de session : la session neuve créée au départ)."""
        if self.pgid is None:
            return []
        return sorted(p for p, s in table.items() if present(s) and s["groupe"] == self.pgid and s["session"] == self.pgid)

    def descendants_hors_groupe(self, table):
        """Descendants relevés encore présents avec la même heure de départ, hors du groupe écrit."""
        return sorted(p for p, d in self.vus.items()
                      if present(table.get(p)) and table[p]["depart"] == d and table[p]["groupe"] != self.pgid)

    def descendants_vivants(self, table):
        return sorted(p for p, d in self.vus.items() if present(table.get(p)) and table[p]["depart"] == d)

    def signaler_par_identifiant(self, pid, sig):
        """Signal à un descendant relevé, après relecture de son heure de départ ; rend un texte."""
        s = lire_stat(pid)
        if not present(s) or s["depart"] != self.vus.get(pid):
            return f"{pid} : absent ou autre processus (aucun signal)"
        try:
            os.kill(pid, sig)
            return f"{pid} (groupe {s['groupe']}, session {s['session']}) : signal {sig.name} envoyé"
        except ProcessLookupError:
            return f"{pid} : disparu avant le signal"

    # -- relevés (noms, tailles, heures seulement)
    def releve(self):
        t = time.time()
        etat = self.etat_programme()
        table = self.relever_descendants()
        closes = [e for e in ETAPES if os.path.exists(manifeste(self.sorties, e))]
        presentes = [e for e in ETAPES if os.path.isdir(os.path.join(self.sorties, f"etape-{e}"))]
        en_cours = [e for e in presentes if e not in closes]
        n = compter_sources(self.sorties)
        app, alloc, nf, arrets = parcourir(self.sorties)
        libres, fs = octets_libres(self.sorties)
        return {"t": t, "etat": etat, "closes": closes, "en_cours": en_cours, "arrets": arrets, "n": n,
                "apparents": app, "alloues": alloc, "fichiers": nf, "libres": libres, "fs": fs,
                "descendants": self.descendants_vivants(table)}

    def ecrire_ligne(self, r, note=None):
        a = r["arrets"]
        champs = [("heure", heure(r["t"])), ("demarrage", boot_id()),
                  ("processus", f"{self.pid}:{r['etat']}"),
                  ("etape_en_cours", ",".join(r["en_cours"]) or "aucune"),
                  ("manifestes", ",".join(r["closes"]) or "aucun"),
                  ("fichier_arret", ("oui (" + str(len(a)) + " : " + ", ".join(a[:5]) + (", …" if len(a) > 5 else "") + ")")
                   if a else "aucun"),
                  ("n", f"{r['n']}/{self.a.total}"),
                  ("descendants_vivants", ",".join(map(str, r["descendants"])) or "aucun"),
                  ("occupes_apparents", r["apparents"]), ("occupes_alloues", r["alloues"]), ("fichiers", r["fichiers"]),
                  ("libres", r["libres"])]
        if note:
            champs.append(("note", note))
        self.ligne(champs)

    # -- inventaires des étapes closes (empreintes permises : correction 5)
    def inventaires(self):
        for e in ETAPES:
            m = manifeste(self.sorties, e)
            if not (os.path.isfile(m) and os.path.isfile(m + ".sha256")):
                continue
            inv = os.path.join(self.tenue, f"inventaire-etape-{e}-essai-court.txt")
            if os.path.lexists(inv):
                continue
            racine = os.path.join(self.sorties, f"etape-{e}")
            entrees = []
            for d, sd, fs in os.walk(racine):
                sd.sort()
                for f in sorted(fs):
                    c = os.path.join(d, f)
                    st = os.lstat(c)
                    sha = sha256_fichier(c) if stat.S_ISREG(st.st_mode) else "(non régulier : non haché)"
                    entrees.append((os.path.relpath(c, self.sorties), st.st_size, sha))
            entrees.sort()
            with open(inv, "x", encoding="utf-8") as fh:
                fh.write(f"# inventaire de l'étape {e} de {self.sorties}, écrit le {heure()} : empreinte sha256, taille "
                         f"(octets), chemin relatif au dossier des sorties ; {len(entrees)} fichiers\n")
                for chemin, taille, sha in entrees:
                    fh.write(f"{sha}  {taille}  {chemin}\n")
                fh.flush()
                os.fsync(fh.fileno())
            sha = ecrire_compagnon(inv)
            self.ecrire(f"{heure()} : inventaire de l'étape {e} écrit : {inv} ({len(entrees)} fichiers), sha256 {sha}, "
                        f"compagnon {inv}.sha256")

    # -- arrêt (corrections 1, 2, 3)
    def restants(self, table):
        return self.membres_du_groupe(table), self.descendants_hors_groupe(table)

    def groupe_continu(self, table):
        """Vrai si le groupe écrit porte encore un descendant relevé présent (identifiant et heure de départ égaux) : son
        numéro n'a pas pu être repris depuis ce relevé (v3)."""
        return any(p in self.vus and table[p]["depart"] == self.vus[p] for p in self.membres_du_groupe(table))

    def attendre_fin(self, delai, signales, sig):
        """Attend au plus `delai` s que le groupe et les descendants relevés aient disparu ; relève les nouveaux descendants
        pendant l'attente et leur envoie `sig` par identifiant s'ils sont hors du groupe. Rend (membres, hors_groupe)."""
        fin = time.monotonic() + delai
        while True:
            table = self.relever_descendants()
            membres, hors = self.restants(table)
            for p in hors:
                if p not in signales:
                    signales.add(p)
                    self.ecrire(f"{heure()} : descendant hors du groupe relevé pendant l'attente : "
                                f"{self.signaler_par_identifiant(p, sig)}", self.f_arret)
            if not membres and not hors:
                return [], []
            if time.monotonic() >= fin:
                return membres, hors
            time.sleep(0.2)

    def arreter(self, raison, details):
        """Rend l'heure d'envoi du signal de fin, ou None si aucun signal n'est parti ; et vrai si tout est absent au bout."""
        self.arret_fait = raison
        self.ecrire(f"raison : {raison}\nheure : {heure()}\n{details}", self.f_arret)
        ok, pourquoi = self.identite()
        table = self.relever_descendants()
        if ok:
            mode = "groupe"
        else:
            reste = self.descendants_vivants(table)
            if (self.chef_confirme and boot_id() == self.boot_ecrit and self.etat_programme() == "absent" and reste):
                # v3 (erratum 2, correction 1) : processus lancé absent, descendants relevés encore présents
                mode = "descendants"
                pourquoi = (f"processus lancé {self.pid} absent ({pourquoi}) ; descendants relevés encore présents {reste}, "
                            f"même heure de départ qu'au relevé")
            else:
                self.ecrire(f"{heure()} : aucun signal envoyé : identité non confirmée ({pourquoi})", self.f_arret)
                return None, False
        hors = self.descendants_hors_groupe(table)
        t_signal = time.time()
        if mode == "groupe":
            os.killpg(self.pgid, signal.SIGTERM)
            self.ecrire(f"{heure(t_signal)} : signal de fin envoyé au groupe {self.pgid} ({pourquoi}) ; membres présents "
                        f"{self.membres_du_groupe(table)}", self.f_arret)
        else:
            self.ecrire(f"{heure(t_signal)} : arrêt des descendants relevés ({pourquoi})", self.f_arret)
            if self.groupe_continu(table):
                try:
                    os.killpg(self.pgid, signal.SIGTERM)
                    self.ecrire(f"{heure()} : signal de fin envoyé au groupe {self.pgid} (il porte encore un descendant "
                                f"relevé : membres {self.membres_du_groupe(table)})", self.f_arret)
                except ProcessLookupError:
                    self.ecrire(f"{heure()} : groupe {self.pgid} disparu avant le signal de fin", self.f_arret)
        signales = set()
        for p in hors:
            signales.add(p)
            self.ecrire(f"{heure()} : descendant hors du groupe : {self.signaler_par_identifiant(p, signal.SIGTERM)}",
                        self.f_arret)
        membres, hors = self.attendre_fin(self.a.delai_force_s, signales, signal.SIGTERM)
        if not membres and not hors:
            self.ecrire(f"{heure()} : tous les membres du groupe {self.pgid} et tous les descendants relevés sont absents "
                        f"après le signal de fin (descendants relevés : {sorted(self.vus) or 'aucun'})", self.f_arret)
            return t_signal, True
        self.ecrire(f"{heure()} : après {self.a.delai_force_s} s, encore présents : membres du groupe {membres}, "
                    f"descendants hors du groupe {hors}", self.f_arret)
        if membres and (mode == "groupe" or self.groupe_continu(self.relever_descendants())):
            # Le numéro du groupe ne peut être repris tant qu'un membre le porte : le groupe est toujours celui du départ,
            # identifié au signal de fin (mode groupe), ou porteur d'un descendant relevé (mode descendants).
            try:
                os.killpg(self.pgid, signal.SIGKILL)
                self.ecrire(f"{heure()} : signal d'arrêt forcé envoyé au groupe {self.pgid}", self.f_arret)
            except ProcessLookupError:
                self.ecrire(f"{heure()} : groupe {self.pgid} disparu avant l'arrêt forcé", self.f_arret)
        for p in hors:
            self.ecrire(f"{heure()} : arrêt forcé : {self.signaler_par_identifiant(p, signal.SIGKILL)}", self.f_arret)
        signales_kill = set(hors)
        membres, hors = self.attendre_fin(10, signales_kill, signal.SIGKILL)
        if membres and (mode == "groupe" or self.groupe_continu(self.relever_descendants())):
            try:
                os.killpg(self.pgid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        tout_absent = not membres and not hors
        self.ecrire(f"{heure()} : après l'arrêt forcé : " + ("tous absents" if tout_absent else
                    f"ENCORE PRÉSENTS : membres {membres}, hors du groupe {hors}"), self.f_arret)
        return t_signal, tout_absent

    # -- mesure instantanée (correction 4)
    def releve_etape_4(self):
        """(n, fichiers, octets apparents, octets alloués) du dossier etape-4, et l'heure du relevé (noms et tailles seulement)."""
        t = time.time()
        n = compter_sources(self.sorties)
        app, alloc, nf, _ = parcourir(os.path.join(self.sorties, "etape-4"))
        return (n, nf, app, alloc), t

    @staticmethod
    def texte_releve(v, t):
        return f"[{heure(t)} : n {v[0]}, {v[1]} fichiers, {v[2]} octets apparents, {v[3]} octets alloués]"

    def figer(self, paires=10, ecart_s=1.0):
        """v3 (erratum 2, correction 2) : au plus `paires` paires de relevés à `ecart_s` s d'écart ; rend (figé, numéro de la
        paire, premier relevé, heure, second relevé, heure) ; figé seulement si les deux relevés d'une paire sont égaux."""
        for i in range(1, paires + 1):
            a, ta = self.releve_etape_4()
            time.sleep(ecart_s)
            b, tb = self.releve_etape_4()
            if a == b:
                return True, i, a, ta, b, tb
        return False, paires, a, ta, b, tb

    def mesure(self, t_signal, tout_absent, r):
        m3 = manifeste(self.sorties, "3")
        t3 = os.lstat(m3).st_mtime
        fige, k, a, ta, b, tb = self.figer()
        n, s4_nf, s4_app, s4_alloc = b
        total = self.a.total
        if t_signal is None:
            t_arret = r["t"]
            etat_signal = "aucun signal envoyé (identité non confirmée) : t_arrêt est l'heure de la décision"
        else:
            t_arret = t_signal
            etat_signal = "t_arrêt est l'heure d'envoi du signal de fin" + (
                "" if tout_absent else " ; des processus relevés restaient présents après l'arrêt forcé")
        if fige:
            etat_dossier = (f"dossier figé : deux relevés à une seconde d'écart égaux (paire {k}) : "
                            f"{self.texte_releve(a, ta)} = {self.texte_releve(b, tb)}")
        else:
            etat_dossier = (f"dossier NON figé : {k} paires de relevés à une seconde d'écart, toutes inégales ; deux derniers "
                            f"relevés : {self.texte_releve(a, ta)} puis {self.texte_releve(b, tb)}")
        lignes = [f"état : {etat_signal}",
                  f"état du dossier : {etat_dossier}",
                  f"t3 (heure de dernière modification du manifeste de l'étape 3) : {heure(t3)} ({t3:.6f} s)",
                  f"heure de l'arrêt (t_arrêt) : {heure(t_arret)} ({t_arret:.6f} s)",
                  f"heure du relevé de n et s4 retenu (dernier) : {heure(tb)}",
                  f"n : {n} sur {total}",
                  f"s4 (taille du dossier etape-4) : {s4_alloc} octets alloués ; {s4_app} octets apparents ; {s4_nf} fichiers"]
        proj = lignes_projection(t3, t_arret, n, s4_alloc, s4_app, total)
        if not fige:
            proj = ["[dossier NON figé] " + l for l in proj]
        lignes += proj
        with open(self.f_mesure, "x", encoding="utf-8") as fh:
            fh.write("\n".join(lignes) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        return lignes

    # -- un tour
    def tour(self):
        r = self.releve()
        self.ecrire_ligne(r)
        self.controles(r)
        self.inventaires()  # après les contrôles : le hachage d'une étape ne retarde pas un arrêt
        return r

    def controles(self, r):
        if self.arret_fait or (r["etat"] == "absent" and not r["descendants"]):
            return  # v3 : processus lancé absent mais descendants relevés présents : les contrôles s'appliquent à eux
        if r["libres"] < self.a.seuil_libre_octets:
            self.arreter("arrêt de place", f"octets libres {r['libres']} (système de fichiers de {r['fs']}) sous le seuil "
                                           f"{self.a.seuil_libre_octets}")
            return
        m3 = manifeste(self.sorties, "3")
        if os.path.exists(m3):
            t3 = os.lstat(m3).st_mtime
            if r["n"] >= self.a.seuil_n:
                cause = f"n = {r['n']} a atteint le seuil {self.a.seuil_n}"
            elif r["t"] - t3 > self.a.duree_etape_4_s:
                cause = f"l'étape 4 dure depuis {r['t'] - t3:.1f} s (depuis t3), plus que {self.a.duree_etape_4_s} s"
            else:
                cause = None
            if cause:
                t_signal, fige = self.arreter("arrêt de mesure", cause)
                try:
                    lignes = self.mesure(t_signal, fige, r)
                    self.ecrire(f"{heure()} : mesure écrite dans {self.f_mesure} :\n" + "\n".join(lignes), self.f_arret)
                except Exception as e:  # la mesure manquée est écrite
                    self.ecrire(f"{heure()} : ERREUR de la mesure : {type(e).__name__} : {e}", self.f_arret)
                    self.ecrire(f"{heure()} : ERREUR du gardien (mesure) : {type(e).__name__} : {e}")

    def garder(self):
        debut = time.monotonic()
        k = 0
        while True:
            try:
                r = self.tour()
                chef_absent = r["etat"] == "absent"
                reste = self.descendants_vivants(self.relever_descendants()) if chef_absent else []
            except Exception as e:  # aucun repli silencieux : l'erreur est écrite, la garde continue
                self.ecrire(f"{heure()} : ERREUR du gardien : {type(e).__name__} : {e}")
                chef_absent = self.etat_programme() == "absent"
                try:
                    reste = self.descendants_vivants(self.relever_descendants()) if chef_absent else []
                except Exception:
                    reste = []
            if chef_absent and reste and not self.note_reste:
                self.note_reste = True
                self.ecrire(f"{heure()} : processus lancé {self.pid} absent ; descendants relevés encore présents {reste} : "
                            f"la garde continue sur eux (lignes, arrêt de place, arrêt de mesure, par identifiant)")
            if chef_absent and not reste:
                r = self.releve()
                note = ("programme et tous les descendants relevés absents : dernière ligne, fin du gardien"
                        if not r["descendants"] else
                        f"programme absent ; descendants relevés encore présents : {r['descendants']} (relevé de fin)")
                self.ecrire_ligne(r, note=note)
                try:
                    self.inventaires()
                except Exception as e:
                    self.ecrire(f"{heure()} : ERREUR du gardien (inventaires) : {type(e).__name__} : {e}")
                return 0
            k += 1
            attente = debut + k * self.a.intervalle_s - time.monotonic()
            if attente > 0:
                time.sleep(attente)


def analyser(argv):
    p = argparse.ArgumentParser(description="Gardien de l'essai court de mesure du palier 0b (v3).")
    p.add_argument("--tenue", default=TENUE_EMPLOI)
    p.add_argument("--sorties", default=SORTIES_EMPLOI)
    p.add_argument("--seuil-libre-octets", type=int, default=8_000_000_000)
    p.add_argument("--seuil-n", type=int, default=13)
    p.add_argument("--duree-etape-4-s", type=float, default=45 * 60)
    p.add_argument("--intervalle-s", type=float, default=60)
    p.add_argument("--delai-force-s", type=float, default=60)
    p.add_argument("--total", type=int, default=TOTAL_SOURCES)
    return p.parse_args(argv)


if __name__ == "__main__":
    sys.exit(Gardien(analyser(sys.argv[1:])).garder())
