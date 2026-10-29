"""Builds every SVG in assets/ in dark and light BMW M variants, plus generates README.md.

Run: python3 scripts/build.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
README_PATH = Path(__file__).resolve().parent.parent / "README.md"
OUT.mkdir(parents=True, exist_ok=True)

SERIF = "'Iowan Old Style', 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "dark": dict(
        page="#0a0d14",
        card="#101624",
        chip="#161f33",
        grid="#141c2e",
        line="#1e2942",
        dim="#4b5d80",
        faint="#7287ad",
        soft="#a2b7db",
        ink="#f0f5ff",
        m_light="#0084ff",
        m_dark="#18367a",
        m_red="#e61238",
        glow="#0084ff",
        meter="#00e5ff",
    ),
    "light": dict(
        page="#f7f9fd",
        card="#edf3fc",
        chip="#e1ecfa",
        grid="#dfebf9",
        line="#cbd9ee",
        dim="#8e9fb8",
        faint="#617494",
        soft="#3f506e",
        ink="#0d172a",
        m_light="#0066b1",
        m_dark="#152b5e",
        m_red="#cc0c29",
        glow="#0066b1",
        meter="#0284c7",
    ),
}

def mono_w(text, size):
    return len(text) * size * 0.611

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

# ---------------------------------------------------------------- HERO BANNER

HERO = dict(
    name="Ritwik Ala",
    role="AWS Certified Data Engineer",
    role2="Big Data & Cloud Lakehouse Architect",
    building=[
        "Cloud E-Commerce Medallion Lakehouse",
        "560K+ Record PySpark Distributed Engine",
        "Algorithmic Trading & Risk Analytics Pipeline",
        "Snappy Parquet Optimization (-79% Storage)",
    ],
    pills_row1=[
        "AWS Certified Data Engineer – Associate",
        "VIT-AP · B.Tech Data Analytics (8.68 CGPA)",
    ],
    pills_row2=[
        "Databricks · PySpark · Airflow · S3",
        "BMW M TwinPower Telemetry",
    ],
    engine_title="B58 INLINE-6 · DATA TELEMETRY",
    cylinders=[
        ("CYL 1", "BRONZE INTAKE", "560K+ REST FX & S3"),
        ("CYL 5", "DATABRICKS", "PySpark 10K+ Dedup"),
        ("CYL 3", "TWIN TURBO", "Snappy Parquet (-79%)"),
        ("CYL 6", "SILVER LAYER", "Strict Schema Rules"),
        ("CYL 2", "STAR SCHEMA", "SCD 2 History Track"),
        ("CYL 4", "GOLD EXHAUST", "Athena SQL & Streamlit"),
    ],
    engine_spec="Firing 1-5-3-6-2-4 · 24.5 PSI Boost · 99% Athena Cost Reduction",
)

def m_stripes(t, x, y, h=18):
    w, gap, dx = 6, 3, 5
    return (f'<g class="m-stripes" transform="translate({x},{y})">'
            f'<polygon points="0,{h} {w},{h} {w+dx},0 {dx},0" fill="{t["m_light"]}"/>'
            f'<polygon points="{w+gap},{h} {2*w+gap},{h} {2*w+gap+dx},0 {w+gap+dx},0" fill="{t["m_dark"]}"/>'
            f'<polygon points="{2*(w+gap)},{h} {3*w+2*gap},{h} {3*w+2*gap+dx},0 {2*(w+gap)+dx},0" fill="{t["m_red"]}"/>'
            f'</g>')

def firing_leds(t, x0, y):
    """BMW Inline-6 Firing Sequence 1-5-3-6-2-4 cycling animation."""
    order = [0, 4, 2, 5, 1, 3]  # indices corresponding to 1, 5, 3, 6, 2, 4
    css, leds = [], []
    for step, cyl_idx in enumerate(order):
        start = round((step / 6.0) * 100, 1)
        peak = round(((step + 0.5) / 6.0) * 100, 1)
        end = round(((step + 1.0) / 6.0) * 100, 1)
        prev = max(0.0, round(start - 0.1, 1))
        css.append(
            f"@keyframes fire{cyl_idx}{{"
            f"0%,{prev}%{{fill:{t['line']};filter:none}}"
            f"{start}%,{peak}%{{fill:{t['m_light']};filter:drop-shadow(0 0 5px {t['glow']})}}"
            f"{end}%,100%{{fill:{t['line']};filter:none}}"
            f"}}.fled{cyl_idx}{{animation:fire{cyl_idx} 3.6s infinite}}"
        )
    for i in range(6):
        leds.append(f'<circle class="fled{i}" cx="{x0 + i * 13}" cy="{y}" r="3.2" fill="{t["line"]}"/>')
    return "\n".join(css), "".join(leds)

def hero(t):
    h = HERO
    leds_css, leds = firing_leds(t, 94, 82)
    stripes = m_stripes(t, 58, 73, 18)

    words = "".join(
        f'<text class="w{i}" x="228" y="286" font-family="{MONO}" font-size="17" fill="{t["ink"]}">'
        f'{esc(w)}<tspan class="cur" fill="{t["m_light"]}">▍</tspan></text>'
        for i, w in enumerate(h["building"])
    )

    pills = []
    # Row 1
    px = 58.0
    for p in h["pills_row1"]:
        w = round(mono_w(p, 11.5) + 22)
        pills.append(
            f'<rect x="{px:g}" y="332" width="{w}" height="26" rx="13" fill="{t["chip"]}" stroke="{t["line"]}"/>'
            f'<text x="{px + 11:g}" y="349.5" font-family="{MONO}" font-size="11.5" fill="{t["soft"]}">{esc(p)}</text>'
        )
        px += w + 8
    # Row 2
    px = 58.0
    for p in h["pills_row2"]:
        w = round(mono_w(p, 11.5) + 22)
        pills.append(
            f'<rect x="{px:g}" y="368" width="{w}" height="26" rx="13" fill="{t["chip"]}" stroke="{t["line"]}"/>'
            f'<text x="{px + 11:g}" y="385.5" font-family="{MONO}" font-size="11.5" fill="{t["soft"]}">{esc(p)}</text>'
        )
        px += w + 8

    # Right side: Inline-6 Telemetry & Lakehouse Engine Box
    cyl_pos = [
        (760, 126), (1014, 126),
        (760, 186), (1014, 186),
        (760, 246), (1014, 246),
    ]

    cyl_elements = []
    for i, ((cyl_tag, role, note), (cx, cy)) in enumerate(zip(h["cylinders"], cyl_pos)):
        d = f"animation-delay:{i * 0.4:.2f}s"
        cyl_elements.append(
            f'<g class="cyl-block" style="{d}">'
            f'<rect x="{cx}" y="{cy}" width="232" height="50" rx="10" fill="{t["card"]}" stroke="{t["line"]}"/>'
            f'<rect class="cyl-ring fled{i}" x="{cx}" y="{cy}" width="232" height="50" rx="10" fill="none" stroke="{t["m_light"]}" stroke-opacity="0.25"/>'
            f'<rect x="{cx + 10}" y="{cy + 12}" width="42" height="26" rx="6" fill="{t["chip"]}" stroke="{t["line"]}"/>'
            f'<text x="{cx + 31}" y="{cy + 29}" text-anchor="middle" font-family="{MONO}" font-size="10.5" font-weight="600" fill="{t["m_light"]}">{esc(cyl_tag)}</text>'
            f'<text x="{cx + 60}" y="{cy + 26}" font-family="{MONO}" font-size="12" font-weight="600" fill="{t["ink"]}">{esc(role)}</text>'
            f'<text x="{cx + 60}" y="{cy + 42}" font-family="{MONO}" font-size="10" fill="{t["faint"]}">{esc(note)}</text>'
            f'</g>'
        )

    manifold_path = "M 876 120 L 1130 120 L 1130 300 L 876 300 Z"
    pulses = "".join(
        f'<circle r="2.8" fill="{t["m_light"]}" opacity=".9" filter="url(#glow)">'
        f'<animateMotion dur="3.6s" begin="{b}s" repeatCount="indefinite" path="{manifold_path}"/></circle>'
        for b in ("0", "1.2", "2.4")
    )

    label = f"{h['name']} — {h['role']} and {h['role2']}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="430" viewBox="0 0 1280 430" role="img" aria-label="{esc(label)}">
<style>
@keyframes drift{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(40px,20px)}}}}
@keyframes word{{0%{{opacity:0;transform:translateY(6px)}}3%,22%{{opacity:1;transform:none}}25%,100%{{opacity:0;transform:translateY(-6px)}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes live{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}
.g1{{animation:drift 12s ease-in-out infinite}}
.w0{{animation:word 12s infinite;animation-delay:0.0s;opacity:0}}
.w1{{animation:word 12s infinite;animation-delay:3.0s;opacity:0}}
.w2{{animation:word 12s infinite;animation-delay:6.0s;opacity:0}}
.w3{{animation:word 12s infinite;animation-delay:9.0s;opacity:0}}
.cur{{animation:blink 1s step-end infinite}}
.live{{animation:live 1.6s ease-in-out infinite}}
{leds_css}
{REDUCED}
</style>
<defs>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{t["grid"]}" stroke-width="1"/></pattern>
<radialGradient id="fade" cx="75%" cy="50%" r="65%"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
<mask id="m"><rect width="1280" height="430" fill="url(#fade)"/></mask>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
<filter id="glow" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="2"/></filter>
<clipPath id="clip"><rect x="1" y="1" width="1278" height="428" rx="20"/></clipPath>
</defs>
<g clip-path="url(#clip)">
<rect width="1280" height="430" fill="{t["page"]}"/>
<rect width="1280" height="430" fill="url(#grid)" mask="url(#m)"/>
<circle class="g1" cx="1020" cy="110" r="180" fill="{t["m_light"]}" opacity="0.12" filter="url(#blur)"/>
<circle class="g1" cx="800" cy="310" r="140" fill="{t["m_red"]}" opacity="0.08" filter="url(#blur)"/>
</g>
<rect x="0.5" y="0.5" width="1279" height="429" rx="20" fill="none" stroke="{t["line"]}"/>

<!-- Top Metadata Bar -->
<g class="top-meta">
  {stripes}
  <text x="180" y="87" font-family="{MONO}" font-size="13.5" fill="{t["faint"]}">~/ritwik-byt · b58-data-engine</text>
  {leds}
  <text x="760" y="87" font-family="{MONO}" font-size="12" letter-spacing="1.2" fill="{t["faint"]}">{esc(h["engine_title"])}</text>
  <circle class="live" cx="1218" cy="83" r="3.5" fill="{t["m_light"]}"/>
  <text x="1208" y="87" text-anchor="end" font-family="{MONO}" font-size="11.5" fill="{t["faint"]}">7,200 RPM · 24.5 PSI</text>
</g>

<!-- Left Column: Title, Role, Typing & Badges -->
<text x="58" y="162" font-family="{SERIF}" font-size="56" font-weight="400" letter-spacing="-1.2" fill="{t["ink"]}">{esc(h["name"])}</text>
<text x="60" y="210" font-family="{SANS}" font-size="21" font-weight="400" letter-spacing="0.2" fill="{t["soft"]}"><tspan fill="{t["ink"]}">{esc(h["role"])}</tspan><tspan fill="{t["m_light"]}">  /  </tspan>{esc(h["role2"])}</text>
<g><text x="60" y="286" font-family="{MONO}" font-size="17" fill="{t["faint"]}">$ now tuning</text>{words}</g>
<g>{"".join(pills)}</g>

<!-- Right Column: B58 Inline-6 Engine Block -->
<g class="engine-telemetry">
  <path d="{manifold_path}" fill="none" stroke="{t["line"]}" stroke-width="1.8" stroke-dasharray="4 6"/>
  {pulses}
  {"".join(cyl_elements)}
  <text x="760" y="324" font-family="{MONO}" font-size="11" fill="{t["faint"]}">{esc(h["engine_spec"])}</text>
</g>
</svg>
'''

# ---------------------------------------------------------------- ENGINE SCHEMATIC (Car Parts Graphic)

def engine_telemetry(t):
    """Full-width technical blueprint schematic mapping BMW engine components to Data Lakehouse systems."""
    label = "BMW M TwinPower Data Architecture — Engine Telemetry Blueprint"
    modules = [
        ("FORCED AIR INTAKE & DIRECT FUEL INJECTION", "Bronze Ingestion Layer",
         "Ingests 560K+ transactional records + live REST API foreign exchange rates into Amazon S3 Bronze storage with zero data loss.",
         ["Amazon S3", "REST APIs", "Raw Ingestion", "Daily FX Snapshots"],
         "High-flow intake & multi-point fuel rails feeding raw data volume into storage"),
        ("TWIN-SCROLL TURBOCHARGER & INTERCOOLER", "PySpark Optimization Engine",
         "Converts raw CSVs into Snappy Parquet with partition pruning, achieving 79% S3 storage compression and 99% Athena scan reduction.",
         ["PySpark", "Snappy Parquet", "-79% Storage", "-99% Scan Cost"],
         "Twin-scroll exhaust turbine compressing data density for maximum boost"),
        ("INLINE-6 COMBUSTION CHAMBER & CRANKSHAFT", "Databricks Distributed Refinery",
         "Executes distributed transformation jobs enforcing schema rules, eliminating 10K+ duplicate records, and building Star Schema / SCD Type 2.",
         ["Databricks", "Star Schema", "SCD Type 2", "Zero Null Drift"],
         "Naturally balanced 6-cylinder block delivering pure linear compute torque"),
        ("DIGITAL MOTOR ELECTRONICS & COCKPIT HUD", "Airflow & Analytics Serving",
         "Orchestrates automated daily batch workflows via Airflow DAGs with least-privilege IAM policies, streaming to Streamlit & Plotly.",
         ["Apache Airflow", "AWS Athena", "AWS IAM", "Streamlit / Plotly"],
         "CAN-bus digital telemetry & driver cockpit streaming live metrics at 7,200 RPM"),
    ]

    cards = []
    for i, (eng_part, data_layer, desc, chips, analogy) in enumerate(modules):
        x = 44 + (i % 2) * 612
        y = 78 + (i // 2) * 156
        chip_svg = []
        cx = x + 20.0
        for ch in chips:
            cw = round(mono_w(ch, 11) + 18)
            chip_svg.append(
                f'<rect x="{cx:g}" y="{y + 104}" width="{cw}" height="24" rx="12" fill="{t["chip"]}" stroke="{t["line"]}"/>'
                f'<text x="{cx + 9:g}" y="{y + 120}" font-family="{MONO}" font-size="11" fill="{t["soft"]}">{esc(ch)}</text>'
            )
            cx += cw + 6

        cards.append(
            f'<g class="eng-card">'
            f'<rect x="{x}" y="{y}" width="580" height="142" rx="14" fill="{t["card"]}" stroke="{t["line"]}"/>'
            f'<rect x="{x + 20}" y="{y}" width="48" height="2" fill="{t["m_light"] if i % 2 == 0 else t["m_red"]}"/>'
            f'<text x="{x + 20}" y="{y + 28}" font-family="{MONO}" font-size="11" font-weight="600" letter-spacing="1.2" fill="{t["m_light"]}">{esc(eng_part)}</text>'
            f'<text x="{x + 20}" y="{y + 50}" font-family="{SERIF}" font-size="18" fill="{t["ink"]}">{esc(data_layer)}</text>'
            f'<text x="{x + 20}" y="{y + 72}" font-family="{SANS}" font-size="12.5" fill="{t["soft"]}">{esc(desc[:95])}...</text>'
            f'<text x="{x + 20}" y="{y + 90}" font-family="{MONO}" font-size="10.5" fill="{t["faint"]}">{esc(analogy)}</text>'
            f'{"".join(chip_svg)}'
            f'</g>'
        )

    stripes = m_stripes(t, 44, 32, 18)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="420" viewBox="0 0 1280 420" role="img" aria-label="{esc(label)}">
<rect x="0.5" y="0.5" width="1279" height="419" rx="18" fill="{t["page"]}" stroke="{t["line"]}"/>
{stripes}
<text x="80" y="46" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{t["faint"]}">BMW M TWINPOWER DATA ARCHITECTURE · MECHANICAL SCHEMATIC</text>
<text x="1236" y="46" text-anchor="end" font-family="{MONO}" font-size="12" fill="{t["m_light"]}">560K+ Events · 79% Compression · Zero Latency</text>
{"".join(cards)}
</svg>
'''

# ---------------------------------------------------------------- PROJECT CARDS

CARDS = [
    dict(
        slug="lakehouse",
        title="Cloud E-Commerce Medallion Lakehouse",
        badge="Production",
        live=True,
        metric="B58 Turbo: -79% Storage · -99% Athena Query Cost",
        text=[
            "Architected a 3-tier Medallion (Bronze/Silver/Gold) Lakehouse ingesting 560K+",
            "transactional records & live REST foreign exchange rates into Amazon S3.",
            "PySpark in Databricks eliminates 10K+ duplicates and builds Star Schema + SCD 2.",
        ],
        chips=["PySpark", "Databricks", "Amazon S3", "AWS Athena", "Airflow", "Star Schema"],
        url="ecommerce-lakehouse...streamlit.app",
        href="https://ecommerce-lakehouse-ahdfgrhrsgvv8u4hn4z7sn.streamlit.app/",
        alt="Cloud E-Commerce Medallion Data Lakehouse with AWS and Databricks",
    ),
    dict(
        slug="trading",
        title="Algorithmic Trading & Analytics Pipeline",
        badge="Live Demo",
        live=True,
        metric="Telemetry Screener: 7,000+ Records · 30-Day Volatility",
        text=[
            "Automated Python ETL pipeline processing 7,000+ historical stock market",
            "records into a relational MySQL database with zero data drift.",
            "Advanced SQL window functions compute rolling volatility, daily returns & risk.",
        ],
        chips=["Python", "Pandas", "MySQL", "SQL Window Functions", "Streamlit", "Plotly"],
        url="trading-analytics...onrender.com",
        href="https://trading-analytics-dashboard-bw5o.onrender.com",
        alt="Algorithmic Trading and Quantitative Financial Pipeline",
    ),
    dict(
        slug="fxe",
        title="Multi-Currency Live FX Ingestion Engine",
        badge="Pipeline",
        live=False,
        metric="Direct Injection: Real-Time Currency Normalization",
        text=[
            "Automated REST API service polling live global foreign exchange rates,",
            "partitioning currency snapshots into S3 Bronze storage for Lakehouse",
            "multi-currency conversion across 560K+ international transactions.",
        ],
        chips=["Python", "REST APIs", "Amazon S3", "Batch ETL", "Data Validation"],
        url="github.com/ritwik-byt/ecommerce-lakehouse",
        href="https://github.com/ritwik-byt/ecommerce-lakehouse",
        alt="Multi-Currency Live FX Ingestion Engine for AWS Lakehouse",
    ),
    dict(
        slug="iam",
        title="AWS Least-Privilege IAM & Airflow DAGs",
        badge="Cloud Security",
        live=False,
        metric="ECU Telemetry Bus: Project-Scoped S3 Actions & Airflow",
        text=[
            "Hardened data engineering infrastructure utilizing least-privilege IAM",
            "bucket policies restricted strictly to lakehouse execution boundaries.",
            "End-to-end daily incremental batch workflows orchestrated via Apache Airflow.",
        ],
        chips=["Apache Airflow", "AWS IAM", "Amazon S3", "CloudWatch", "Airflow DAGs"],
        url="github.com/ritwik-byt/ecommerce-lakehouse",
        href="https://github.com/ritwik-byt/ecommerce-lakehouse",
        alt="AWS IAM Least-Privilege Policy and Airflow Orchestration",
    ),
]

def card(c, t):
    bw = round(mono_w(c["badge"], 12) + 33)
    bx = 572 - bw
    dot = t["m_light"] if c["live"] else t["dim"]
    lines = "".join(f'<tspan x="28" dy="{0 if i == 0 else 20}">{esc(s)}</tspan>' for i, s in enumerate(c["text"]))
    
    chips, x = [], 28.0
    for ch in c["chips"]:
        w = round(mono_w(ch, 11) + 18)
        chips.append(
            f'<rect x="{x:g}" y="146" width="{w}" height="26" rx="13" fill="{t["chip"]}" stroke="{t["line"]}"/>'
            f'<text x="{x + 9:g}" y="163" font-family="{MONO}" font-size="11" fill="{t["soft"]}">{esc(ch)}</text>'
        )
        x += w + 5.5

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="220" viewBox="0 0 600 220" role="img" aria-label="{esc(c["title"])}">
<style>
@keyframes sweep{{0%{{transform:translateX(-140px)}}60%,100%{{transform:translateX(740px)}}}}
@keyframes live{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}
.sweep{{animation:sweep 6s ease-in-out infinite}}
.live{{animation:live 1.6s ease-in-out infinite}}
{REDUCED}
</style>
<defs>
<linearGradient id="shine_{c['slug']}" x1="0" x2="1"><stop offset="0" stop-color="{t["m_light"]}" stop-opacity="0"/><stop offset=".5" stop-color="{t["m_light"]}" stop-opacity=".06"/><stop offset="1" stop-color="{t["m_light"]}" stop-opacity="0"/></linearGradient>
<clipPath id="c_{c['slug']}"><rect x="1" y="1" width="598" height="218" rx="16"/></clipPath>
</defs>
<g clip-path="url(#c_{c['slug']})">
<rect width="600" height="220" fill="{t["card"]}"/>
<rect class="sweep" x="0" y="0" width="140" height="220" fill="url(#shine_{c['slug']})"/>
<rect x="28" y="0" width="70" height="2" fill="{t["m_light"]}"/>
</g>
<rect x="0.5" y="0.5" width="599" height="219" rx="16" fill="none" stroke="{t["line"]}"/>
<text x="28" y="44" font-family="{SERIF}" font-size="23" font-weight="400" letter-spacing="-0.3" fill="{t["ink"]}">{esc(c["title"])}</text>
<rect x="{bx}" y="24" width="{bw}" height="26" rx="13" fill="none" stroke="{t["line"]}"/>
<circle class="live" cx="{bx + 14}" cy="37" r="3" fill="{dot}"/>
<text x="{bx + 24}" y="41.5" font-family="{MONO}" font-size="11.5" fill="{t["soft"]}">{esc(c["badge"])}</text>
<text x="28" y="65" font-family="{MONO}" font-size="11" fill="{t["m_light"]}">{esc(c["metric"])}</text>
<text y="88" font-family="{SANS}" font-size="13.5" fill="{t["soft"]}">{lines}</text>
{"".join(chips)}
<text x="572" y="198" text-anchor="end" font-family="{MONO}" font-size="11" fill="{t["faint"]}">{esc(c["url"])} ↗</text>
</svg>
'''

# ---------------------------------------------------------------- TOOLKIT

TOOLKIT = [
    ("BIG DATA & DISTRIBUTED COMPUTE", ["PySpark", "Apache Spark", "Databricks", "Apache Airflow", "Medallion Architecture"]),
    ("CLOUD & STORAGE OPTIMIZATION", ["Amazon S3", "AWS Athena", "AWS IAM", "Snappy Parquet", "Partition Pruning"]),
    ("DATABASES & DATA MODELING", ["MySQL", "Star Schema", "SCD Type 2", "SQL Window Functions", "Schema Enforcement"]),
    ("LANGUAGES, ANALYTICS & DEPLOY", ["Python", "Java", "SQL", "Streamlit", "Plotly / Render"]),
]

def toolkit(t):
    label = "Toolkit: " + "; ".join(f"{k}: {', '.join(v)}" for k, v in TOOLKIT)
    rows = []
    for i, (k, items) in enumerate(TOOLKIT):
        y = 48 + i * 58
        rows.append(f'<circle cx="44" cy="{y}" r="2.4" fill="{t["m_light"]}"/>'
                    f'<text x="58" y="{y + 5}" font-family="{MONO}" font-size="12" letter-spacing="1.4" fill="{t["faint"]}">{esc(k)}</text>')
        rows += [f'<text x="{320 + j * 192}" y="{y + 6}" font-family="{SANS}" font-size="17" fill="{t["ink"]}">{esc(s)}</text>'
                 for j, s in enumerate(items)]
        if i < len(TOOLKIT) - 1:
            rows.append(f'<line x1="40" x2="1240" y1="{y + 33}" y2="{y + 33}" stroke="{t["line"]}"/>')
    body = "\n".join(rows)
    stripes = m_stripes(t, 1200, 16, 14)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="274" viewBox="0 0 1280 274" role="img" aria-label="{esc(label)}">
<rect x="0.5" y="0.5" width="1279" height="273" rx="18" fill="{t["card"]}" stroke="{t["line"]}"/>
{stripes}
{body}
</svg>
'''

# ---------------------------------------------------------------- README CONTENT

def generate_readme():
    return f'''<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
  <img src="./assets/hero-light.svg" width="100%" alt="Ritwik Ala — AWS Certified Data Engineer · Big Data & Cloud Lakehouse Architect">
</picture>

**[Portfolio](https://github.com/ritwik-byt/portfolio)** &nbsp;·&nbsp; [Resume](./assets/Ritwik_Ala_Resume.pdf) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/avv-ritwik-b90046382/) &nbsp;·&nbsp; [LeetCode](https://leetcode.com/u/AlaRitwik/) &nbsp;·&nbsp; [Email](mailto:alaritwik@gmail.com)

</div>

<br/>

Computer Science undergraduate specializing in **Data Analytics** at **VIT-AP** (CGPA: 8.68/10) and **AWS Certified Data Engineer – Associate**. I architect distributed cloud data pipelines and analytical lakehouses: orchestrating **PySpark** batch transformations in **Databricks**, enforcing strict schema rules and Star Schema dimensional modeling, and tuning **Snappy Parquet** storage for a **79% footprint reduction** and **99% Athena scan cost savings**. Seeking a **Data Engineering Internship** to build fault-tolerant, high-torque data platforms.

### BMW M TwinPower Data Architecture

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/engine-telemetry-dark.svg">
  <img src="./assets/engine-telemetry-light.svg" width="100%" alt="BMW M TwinPower Data Architecture — Engine Telemetry Blueprint">
</picture>

<br/>

### Featured Systems

<p align="center">
<a href="https://ecommerce-lakehouse-ahdfgrhrsgvv8u4hn4z7sn.streamlit.app/"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/lakehouse-dark.svg"><img src="./assets/lakehouse-light.svg" width="49%" alt="Cloud E-Commerce Medallion Lakehouse — Live Streamlit Demo"></picture></a>&nbsp;<a href="https://trading-analytics-dashboard-bw5o.onrender.com"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/trading-dark.svg"><img src="./assets/trading-light.svg" width="49%" alt="Algorithmic Trading & Quantitative Analytics Pipeline — Live on Render"></picture></a>
<a href="https://github.com/ritwik-byt/ecommerce-lakehouse"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/fxe-dark.svg"><img src="./assets/fxe-light.svg" width="49%" alt="Multi-Currency Live FX Ingestion Engine"></picture></a>&nbsp;<a href="https://github.com/ritwik-byt/ecommerce-lakehouse"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/iam-dark.svg"><img src="./assets/iam-light.svg" width="49%" alt="AWS Least-Privilege IAM & Airflow DAG Orchestration"></picture></a>
</p>

### Toolkit

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/toolkit-dark.svg">
  <img src="./assets/toolkit-light.svg" width="100%" alt="Toolkit — Big Data: PySpark, Databricks, Airflow · Cloud: S3, Athena, IAM · Databases: MySQL, Star Schema, SCD 2 · Languages: Python, Java, SQL, Streamlit">
</picture>

<sub>Off the clock: BMW M Performance engineering, twin-scroll turbochargers, and the timeless mechanical balance of a straight-six engine.</sub>
'''

if __name__ == "__main__":
    for mode, t in THEMES.items():
        (OUT / f"hero-{mode}.svg").write_text(hero(t))
        (OUT / f"engine-telemetry-{mode}.svg").write_text(engine_telemetry(t))
        (OUT / f"toolkit-{mode}.svg").write_text(toolkit(t))
        for c in CARDS:
            (OUT / f"{c['slug']}-{mode}.svg").write_text(card(c, t))
    
    src_pdf = Path("/Users/avvritwik/.gemini/antigravity/brain/63e8b693-2241-4ffc-8009-52fe92a6e95e/.user_uploaded/media_1793277759473_9db856df.pdf")
    if src_pdf.exists():
        (OUT / "Ritwik_Ala_Resume.pdf").write_bytes(src_pdf.read_bytes())
        
    README_PATH.write_text(generate_readme())
    print("Successfully built all assets and README.md!")
