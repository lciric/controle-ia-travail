import json
import subprocess

cfg_raw = subprocess.run(
    ['gh', 'api', '-H', 'Accept: application/vnd.github.raw',
     'repos/lciric/controle-ia-travail/contents/prereg/T0.6-dose-reponse-configuration-course-v1.json?ref=lancement/dose-reponse-v1'],
    text=True, capture_output=True, check=True
).stdout
cfg = json.loads(cfg_raw)
print('=== LANCEMENT BOUNDS IN CONFIG ===')
print(json.dumps(cfg.get('lancement', {}), indent=2, ensure_ascii=False))

raw = subprocess.run(
    ['vastai', 'search', 'offers', 'num_gpus=1 gpu_name=A100_SXM4 gpu_ram>=75 rentable=true verified=true', '--raw'],
    text=True, capture_output=True, check=True
).stdout
offers = json.loads(raw)
print(f'\n=== {len(offers)} A100_SXM4 OFFERS ===')
for o in sorted(offers, key=lambda x: x.get('dph_total', 999)):
    oid = o.get('id')
    dph_base = o.get('dph_base', 0)
    dph_tot = o.get('dph_total', 0)
    st_gb_mo = o.get('storage_cost', 0)
    st_300_hr = st_gb_mo * 300.0 / 730.0
    dl = o.get('inet_down_cost', 0)
    ul = o.get('inet_up_cost', 0)
    ram = o.get('cpu_ram', 0)
    vram = o.get('gpu_ram', 0)
    cores = o.get('cpu_cores_effective', 0)
    disk = o.get('disk_space', 0)
    rel = o.get('reliability2', o.get('reliability', 0))
    cuda = o.get('cuda_max_good', 0)
    geo = o.get('geolocation', '')
    reasons = []
    if dph_base > 1.30: reasons.append(f'dph_base={dph_base:.3f}>1.30')
    if dph_tot > 1.30: reasons.append(f'dph_tot={dph_tot:.3f}>1.30')
    if cores < 16: reasons.append(f'cores={cores}<16')
    if ram < 128000: reasons.append(f'ram={ram}<128000')
    if disk < 300: reasons.append(f'disk={disk:.0f}<300')
    if st_300_hr > 0.08: reasons.append(f'st300_hr={st_300_hr:.4f}>0.08')
    if dl > 0.05: reasons.append(f'dl={dl:.4f}>0.05')
    if vram < 79000: reasons.append(f'vram={vram}<79000')
    tag = 'OK' if not reasons else 'NO(' + '; '.join(reasons) + ')'
    print(f'id={oid} base={dph_base:.4f} tot={dph_tot:.4f} vram={vram} ram={ram} cores={cores:.1f} disk={disk:.0f} st300_hr={st_300_hr:.4f} dl={dl:.4f} ul={ul:.4f} rel={rel:.4f} cuda={cuda} {geo} -> {tag}')
