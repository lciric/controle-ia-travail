"""Pré-essai de NOTRE harnais (aucun code voisin) : imite les deux mécanismes de `measure` et vérifie proche/loin."""
import importlib.util, math, sys, torch
spec = importlib.util.spec_from_file_location("e", sys.argv[1]); e = importlib.util.module_from_spec(spec); spec.loader.exec_module(e)
lm = e.mini_llama(); docs, ctx, top = e.entrees(); ctx = torch.tensor(ctx[:e.C]); V = e.V
DOSES = (1.0, 4.0); W = 8
def mimic_steer(l, n, s):
    wd = lm.model.layers[l].mlp.down_proj.weight
    delta = torch.stack([torch.zeros_like(wd[:, 0]), s * wd[:, n]])
    rows = delta.repeat_interleave(e.C, 0)[:, None, :]
    pm = (torch.arange(e.T) >= 16)[None, :, None].to(rows.dtype)
    h = lm.model.layers[l].mlp.register_forward_hook(lambda m, a, o: o + rows * pm)
    with torch.inference_mode():
        hs = lm.model(input_ids=ctx.repeat(2, 1)).last_hidden_state[:, 16:].reshape(2, -1, e.D)
        lsm = [torch.log_softmax(lm.lm_head(hs[c]).float(), -1).sum(0) / hs.shape[1] for c in range(2)]
    h.remove(); return (lsm[1] - lsm[0]).half()
def mimic_ablate(l, jobs):  # jobs: (seq, n, pos); batched, right padded
    Tm = max(len(q) for q, _, _ in jobs); ids = torch.zeros(2 * len(jobs), Tm, dtype=torch.long); attn = torch.zeros_like(ids)
    for r, (q, _, _) in enumerate(jobs):
        ids[2*r, :len(q)] = ids[2*r+1, :len(q)] = q.long(); attn[2*r, :len(q)] = attn[2*r+1, :len(q)] = 1
    rows = torch.arange(1, 2 * len(jobs), 2); pos_t = torch.tensor([p for *_, p in jobs]); neu_t = torch.tensor([n for _, n, _ in jobs])
    def ab(m, a):
        x = a[0].clone(); x[rows, pos_t, neu_t] = 0; return (x,)
    h = lm.model.layers[l].mlp.down_proj.register_forward_pre_hook(ab)
    with torch.inference_mode():
        hs = lm.model(input_ids=ids, attention_mask=attn).last_hidden_state
    h.remove(); res = []
    for r, (q, n, pos) in enumerate(jobs):
        end = min(pos + 1 + W, len(q))
        d = torch.log_softmax(lm.lm_head(hs[2*r, pos:end]).float(), -1) - torch.log_softmax(lm.lm_head(hs[2*r+1, pos:end]).float(), -1)
        res.append((d[0].half(), d.sum(0).half(), d[0, int(q[pos+1])].item() if pos + 1 < len(q) else math.nan))
    return res
nok = 0; ecarts = []; seps = []
for l in range(e.NL):
    for n in (5, 40):
        for p in (0, 1):
            for dose in DOSES:
                s = (1 - 2*p) * dose * top[l]["act_top"][p, n].item()
                got = mimic_steer(l, n, s); ref = e.ref_pilotage(lm, ctx, l, n, s)
                sc = ref.abs().max().item(); ecarts.append((got.float() - ref).abs().max().item() / sc)
                ok = e.proche(got, ref)
                fx = [e.ref_pilotage(lm, ctx, l, n, -s), e.ref_pilotage(lm, ctx, l, (n+1) % e.F, s),
                      e.ref_pilotage(lm, ctx, (l+1) % e.NL, n, s), e.ref_pilotage(lm, ctx, l, n, s, debut=0)]
                fx = fx if l < e.NL - 1 else fx[:3]
                seps.append(min((got.float() - f).abs().max().item() / got.float().abs().max().item() for f in fx))
                ok = ok and all(e.loin(got, f) for f in fx); nok += not ok
            jobs = []
            for j in range(e.K - 1):
                d, pos = int(top[l]["top_doc"][p, n, j]), int(top[l]["top_pos"][p, n, j]); jobs.append((docs[d][:pos + 1 + W], n, pos))
            res = mimic_ablate(l, jobs)
            refs = [e.ref_ablation(lm, q, l, nn, pos, W) for q, nn, pos in jobs]
            gp = torch.stack([r[0].float() for r in res]).mean(0); rp = torch.stack([r[0] for r in refs]).mean(0)
            gw = torch.stack([r[1].float() for r in res]).mean(0); rw = torch.stack([r[1] for r in refs]).mean(0)
            fp = torch.stack([e.ref_ablation(lm, q, l, nn, pos - 1 if pos > 0 else pos + 1, W)[0] for q, nn, pos in jobs]).mean(0)
            fn = torch.stack([e.ref_ablation(lm, q, l, (nn + 1) % e.F, pos, W)[0] for q, nn, pos in jobs]).mean(0)
            ok = e.proche(gp, rp) and e.proche(gw, rw) and e.loin(gp, fp) and e.loin(gp, fn)
            for (a, b, c), (x, y, z) in zip(res, refs):
                ok = ok and ((math.isnan(c) and math.isnan(z)) or abs(c - z) <= 1e-3 * abs(z) + 1e-5)
            ecarts.append(max((gp - rp).abs().max().item() / rp.abs().max().item(), (gw - rw).abs().max().item() / rw.abs().max().item()))
            seps.append(min((gp - fp).abs().max().item(), (gp - fn).abs().max().item()) / gp.abs().max().item())
            nok += not ok
print("graine", e.GRAINE, "échecs", nok, "écart relatif max (sain)", max(ecarts), "séparation min (artefacts)", min(seps))
# artefact du harnais lui-même : une imitation fautive (signe opposé, pas de masque de positions) doit être refusée par proche()
l, n, p = 1, 5, 0; s = top[l]["act_top"][p, n].item()
print("imitation fautive (signe) acceptée ?", e.proche(mimic_steer(l, n, -s), e.ref_pilotage(lm, ctx, l, n, s)))
