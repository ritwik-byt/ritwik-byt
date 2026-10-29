"""Builds every SVG in assets/ in dark and light BMW M 3D isometric variants, plus generates README.md.

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
        page="#090c13",
        card="#0f1523",
        chip="#151e32",
        grid="#141c2f",
        line="#1c2842",
        dim="#4b5e82",
        faint="#7085ad",
        soft="#9eb4dc",
        ink="#f0f5ff",
        m_light="#0084ff",
        m_dark="#18367a",
        m_red="#e61238",
        glow="#0084ff",
        meter="#00e5ff",
        stage_top="#121a2c",
        stage_side_l="#0a101d",
        stage_side_r="#0e1626",
        stage_grid="#1b253b",
        car_stroke="#5080c8",
        car_accent="#0084ff",
        callout_bg="#131d33",
        callout_border="#243456",
    ),
    "light": dict(
        page="#f8fafd",
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
        stage_top="#e5effa",
        stage_side_l="#ccdcf0",
        stage_side_r="#d6e4f5",
        stage_grid="#c5d7ee",
        car_stroke="#1d4ed8",
        car_accent="#0066b1",
        callout_bg="#e8f1fc",
        callout_border="#b8cfea",
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
        "560K+ Record Medallion Lakehouse on AWS & Databricks",
        "Snappy Parquet Optimization (-79% Storage Footprint)",
        "Algorithmic Trading & Quantitative Volatility Pipeline",
        "B58 TwinPower Telemetry & Distributed Stream Processing",
    ],
    pills=[
        "CSE (Data Analytics) · VIT-AP (8.68 CGPA)",
        "AWS Certified Data Engineer – Associate",
        "3D BMW Telemetry & Lakehouse Engine",
    ],
    tech_line="PySpark · Databricks · Amazon S3 · AWS Athena · Apache Airflow · Snappy Parquet · Star Schema",
)

def m_stripes(t, x, y, h=16):
    w, gap, dx = 5.5, 2.5, 4.5
    return (f'<g class="m-stripes" transform="translate({x},{y})">'
            f'<polygon points="0,{h} {w},{h} {w+dx},0 {dx},0" fill="{t["m_light"]}"/>'
            f'<polygon points="{w+gap},{h} {2*w+gap},{h} {2*w+gap+dx},0 {w+gap+dx},0" fill="{t["m_dark"]}"/>'
            f'<polygon points="{2*(w+gap)},{h} {3*w+2*gap},{h} {3*w+2*gap+dx},0 {2*(w+gap)+dx},0" fill="{t["m_red"]}"/>'
            f'</g>')

def draw_3d_engine_platform(t):
    """Draws a 3D isometric BMW sports car chassis and an Inline-6 TwinPower engine on a raised platform."""
    # Stage coordinates (Isometric rhombus centered at 955, 220)
    # Top face: (955, 128) -> (1190, 218) -> (955, 308) -> (720, 218)
    # Extrusion depth: 16px
    stage = f'''
    <!-- 3D Isometric Platform -->
    <g class="iso-platform">
      <!-- Left Extruded Face -->
      <polygon points="720,218 955,308 955,324 720,234" fill="{t['stage_side_l']}" stroke="{t['line']}" stroke-width="1"/>
      <!-- Right Extruded Face -->
      <polygon points="955,308 1190,218 1190,234 955,324" fill="{t['stage_side_r']}" stroke="{t['line']}" stroke-width="1"/>
      <!-- Top Stage Surface -->
      <polygon points="955,128 1190,218 955,308 720,218" fill="{t['stage_top']}" stroke="{t['line']}" stroke-width="1.2"/>
      
      <!-- Top Surface Isometric Grid -->
      <line x1="778" y1="195" x2="1013" y2="285" stroke="{t['stage_grid']}" stroke-width="1"/>
      <line x1="837" y1="173" x2="1072" y2="263" stroke="{t['stage_grid']}" stroke-width="1"/>
      <line x1="896" y1="150" x2="1131" y2="240" stroke="{t['stage_grid']}" stroke-width="1"/>
      
      <line x1="1013" y1="150" x2="778" y2="240" stroke="{t['stage_grid']}" stroke-width="1"/>
      <line x1="1072" y1="173" x2="837" y2="263" stroke="{t['stage_grid']}" stroke-width="1"/>
      <line x1="1131" y1="195" x2="896" y2="285" stroke="{t['stage_grid']}" stroke-width="1"/>

      <!-- Glowing Stage Perimeter -->
      <polygon points="955,128 1190,218 955,308 720,218" fill="none" stroke="{t['m_light']}" stroke-width="1.5" stroke-opacity="0.4" stroke-dasharray="8 6"/>
    </g>
    '''

    # BMW M Performance Car Silhouette / Wireframe Profile (Isometric 35°)
    # Drawn across the stage from rear-left (760, 205) to front-right (1140, 225)
    car_wireframe = f'''
    <!-- BMW M Car Wireframe Silhouette -->
    <g class="bmw-car" stroke="{t['car_stroke']}" stroke-width="1.5" fill="none" stroke-linejoin="round">
      <!-- Ground Shadow / Base -->
      <path d="M 770,220 L 890,175 L 1080,210 L 1130,225 L 1020,265 L 810,235 Z" fill="{t['chip']}" fill-opacity="0.5" stroke="none"/>

      <!-- Lower Chassis Line -->
      <path d="M 780,215 L 830,195 L 880,185 L 1030,205 L 1110,222 L 1040,250 L 880,230 L 780,215 Z" stroke-opacity="0.8"/>

      <!-- Wheels (Isometric Ellipses with Glowing Rotors) -->
      <!-- Rear Left Wheel -->
      <g transform="translate(820, 218) skewY(21) scale(0.65, 1.1)">
        <ellipse cx="0" cy="0" rx="14" ry="9" fill="{t['card']}" stroke="{t['m_light']}" stroke-width="2"/>
        <circle cx="0" cy="0" r="3" fill="{t['m_red']}"/>
      </g>
      <!-- Front Left Wheel -->
      <g transform="translate(1040, 247) skewY(21) scale(0.65, 1.1)">
        <ellipse cx="0" cy="0" rx="14" ry="9" fill="{t['card']}" stroke="{t['m_light']}" stroke-width="2"/>
        <circle cx="0" cy="0" r="3" fill="{t['m_red']}"/>
      </g>
      <!-- Rear Right Wheel -->
      <g transform="translate(860, 185) skewY(21) scale(0.6, 1.0)">
        <ellipse cx="0" cy="0" rx="12" ry="8" fill="{t['card']}" stroke="{t['dim']}" stroke-width="1.5"/>
      </g>
      <!-- Front Right Wheel -->
      <g transform="translate(1085, 216) skewY(21) scale(0.6, 1.0)">
        <ellipse cx="0" cy="0" rx="12" ry="8" fill="{t['card']}" stroke="{t['dim']}" stroke-width="1.5"/>
      </g>

      <!-- Roofline, A-Pillar, Windshield, Hood -->
      <!-- Aerodynamic Fastback Roofline -->
      <path d="M 770,200 L 800,195 L 830,165 L 900,148 L 965,160 L 1050,192 L 1120,215 L 1125,225" stroke="{t['m_light']}" stroke-width="1.8"/>
      <!-- Greenhouse / Window Edge -->
      <path d="M 830,165 L 895,152 L 955,164 L 980,186 L 850,188 Z" fill="{t['m_light']}" fill-opacity="0.08" stroke="{t['m_light']}" stroke-width="1"/>
      <!-- Hood Center Crease Line -->
      <path d="M 965,160 L 1070,188 L 1120,215" stroke="{t['car_accent']}" stroke-dasharray="3 3"/>
      <!-- Iconic BMW Double Kidney Grille at Front -->
      <g transform="translate(1115, 216) rotate(21)">
        <rect x="-8" y="-6" width="6" height="12" rx="3" fill="{t['card']}" stroke="{t['m_light']}" stroke-width="1.4"/>
        <rect x="0" y="-6" width="6" height="12" rx="3" fill="{t['card']}" stroke="{t['m_red']}" stroke-width="1.4"/>
      </g>
      <!-- Rear Carbon Wing / GT Spoiler -->
      <path d="M 755,190 L 785,180 L 790,195 L 760,205 Z" fill="{t['card']}" stroke="{t['m_light']}" stroke-width="1.6"/>
      <line x1="770" y1="195" x2="770" y2="208" stroke="{t['m_light']}" stroke-width="1.8"/>
      <line x1="780" y1="190" x2="780" y2="204" stroke="{t['m_light']}" stroke-width="1.8"/>
    </g>
    '''

    # B58 Inline-6 Engine Block & Cylinders
    # 6 aligned cylinders firing in order 1-5-3-6-2-4
    cylinders = []
    firing_order = [0, 4, 2, 5, 1, 3] # cylinder indices for 1-5-3-6-2-4
    for i in range(6):
        cx = 910 + i * 24
        cy = 196 + i * 9
        d = f"animation-delay:{firing_order.index(i) * 0.55:.2f}s"
        cylinders.append(
            f'<g class="cyl-piston" transform="translate({cx}, {cy})">'
            f'<!-- Cylinder Bore -->'
            f'<ellipse cx="0" cy="0" rx="8" ry="4.5" fill="{t["card"]}" stroke="{t["line"]}" stroke-width="1.2"/>'
            f'<!-- Piston Head with Cycling Firing Glow -->'
            f'<ellipse class="piston-spark" cx="0" cy="0" rx="6" ry="3.5" fill="{t["m_light"]}" fill-opacity="0.3" stroke="{t["m_light"]}" stroke-width="1.5" style="{d}"/>'
            f'<circle class="spark-core" cx="0" cy="0" r="1.8" fill="{t["ink"]}" style="{d}"/>'
            f'</g>'
        )

    # Twin-Scroll Turbocharger with Spinning Turbine Wheel
    turbo = f'''
    <!-- Twin-Scroll Turbocharger -->
    <g class="turbo-unit" transform="translate(930, 168)">
      <!-- Snail Shell Housing / Volute -->
      <path d="M 0,0 C 12,-10 28,-4 30,10 C 31,20 20,28 8,26 C -4,24 -12,14 -8,2 C -6,-6 -2,-12 14,-16 L 24,-14" fill="{t['card']}" stroke="{t['m_light']}" stroke-width="1.8"/>
      <!-- Compressor Intake Inlet -->
      <ellipse cx="10" cy="10" rx="10" ry="8" fill="{t['chip']}" stroke="{t['line']}" stroke-width="1.4"/>
      <!-- Spinning Turbine Impeller Blades -->
      <g class="turbine-spin" transform="translate(10, 10)">
        <circle cx="0" cy="0" r="2.2" fill="{t['m_light']}"/>
        <line x1="-7" y1="0" x2="7" y2="0" stroke="{t['m_light']}" stroke-width="1.5"/>
        <line x1="0" y1="-6" x2="0" y2="6" stroke="{t['m_light']}" stroke-width="1.5"/>
        <line x1="-5" y1="-4" x2="5" y2="4" stroke="{t['m_light']}" stroke-width="1.2"/>
        <line x1="-5" y1="4" x2="5" y2="-4" stroke="{t['m_light']}" stroke-width="1.2"/>
      </g>
      <!-- Boost Pipe to Intercooler -->
      <path d="M 28,10 C 40,16 50,22 65,28" fill="none" stroke="{t['m_light']}" stroke-width="2" stroke-dasharray="3 3"/>
    </g>
    '''

    # Tactical Isometric Telemetry Callouts (matching Akshay's screenshot)
    # Pins and callout flags with exact technical stats
    callouts = f'''
    <!-- Tactical 3D Callout Pins (Akshay Style) -->
    <!-- Callout 1: Turbo Boost -->
    <g class="callout" transform="translate(850, 110)">
      <line x1="88" y1="58" x2="55" y2="28" stroke="{t['m_light']}" stroke-width="1.2" stroke-dasharray="2 2"/>
      <circle cx="88" cy="58" r="2.5" fill="{t['m_light']}"/>
      <rect x="0" y="0" width="118" height="28" rx="6" fill="{t['callout_bg']}" stroke="{t['callout_border']}" stroke-width="1.2"/>
      <text x="8" y="14" font-family="{MONO}" font-size="10" font-weight="600" fill="{t['m_light']}">BOOST +24.5 PSI</text>
      <text x="8" y="24" font-family="{MONO}" font-size="8.5" fill="{t['faint']}">Twin-Scroll Turbo</text>
    </g>

    <!-- Callout 2: Inline-6 Firing -->
    <g class="callout" transform="translate(1040, 128)">
      <line x1="-40" y1="75" x2="0" y2="28" stroke="{t['m_light']}" stroke-width="1.2" stroke-dasharray="2 2"/>
      <circle cx="-40" cy="75" r="2.5" fill="{t['m_light']}"/>
      <rect x="0" y="0" width="134" height="28" rx="6" fill="{t['callout_bg']}" stroke="{t['callout_border']}" stroke-width="1.2"/>
      <text x="8" y="14" font-family="{MONO}" font-size="10" font-weight="600" fill="{t['ink']}">INLINE-6 · B58</text>
      <text x="8" y="24" font-family="{MONO}" font-size="8.5" fill="{t['m_light']}">Firing 1-5-3-6-2-4</text>
    </g>

    <!-- Callout 3: Parquet Compression -->
    <g class="callout" transform="translate(1060, 275)">
      <line x1="-20" y1="-28" x2="0" y2="0" stroke="{t['m_light']}" stroke-width="1.2" stroke-dasharray="2 2"/>
      <circle cx="-20" cy="-28" r="2.5" fill="{t['m_light']}"/>
      <rect x="0" y="0" width="142" height="28" rx="6" fill="{t['callout_bg']}" stroke="{t['callout_border']}" stroke-width="1.2"/>
      <text x="8" y="14" font-family="{MONO}" font-size="10" font-weight="600" fill="{t['m_light']}">PARQUET -79%</text>
      <text x="8" y="24" font-family="{MONO}" font-size="8.5" fill="{t['faint']}">560K+ Rec · Snappy</text>
    </g>

    <!-- Callout 4: Athena Scan Cost -->
    <g class="callout" transform="translate(710, 260)">
      <line x1="110" y1="-42" x2="80" y2="0" stroke="{t['m_light']}" stroke-width="1.2" stroke-dasharray="2 2"/>
      <circle cx="110" cy="-42" r="2.5" fill="{t['m_light']}"/>
      <rect x="0" y="0" width="128" height="28" rx="6" fill="{t['callout_bg']}" stroke="{t['callout_border']}" stroke-width="1.2"/>
      <text x="8" y="14" font-family="{MONO}" font-size="10" font-weight="600" fill="{t['m_red']}">ATHENA SCAN -99%</text>
      <text x="8" y="24" font-family="{MONO}" font-size="8.5" fill="{t['faint']}">Partition Pruning</text>
    </g>
    '''

    # Bottom Console Bar (matching Akshay's screenshot: T-SPACE MOMENTUM +74.8% ATTACK...)
    console_bar = f'''
    <!-- Bottom Telemetry Console Bar (Akshay Style) -->
    <g class="telemetry-bar" transform="translate(680, 350)">
      <text x="0" y="12" font-family="{MONO}" font-size="9.5" letter-spacing="1" fill="{t['faint']}">TORQUE MOMENTUM:</text>
      <!-- Progress Bar Track -->
      <rect x="114" y="4" width="76" height="8" rx="4" fill="{t['card']}" stroke="{t['line']}" stroke-width="1"/>
      <!-- Glowing Active Meter Bar -->
      <rect class="bar-pulse" x="115" y="5" width="66" height="6" rx="3" fill="{t['m_light']}"/>
      <text x="198" y="12" font-family="{MONO}" font-size="10" font-weight="600" fill="{t['m_light']}">+88.4% HIGH-RPM</text>
      <text x="320" y="12" font-family="{MONO}" font-size="9.5" fill="{t['faint']}">500 N·m · 0-60: 3.8s</text>

      <text x="0" y="27" font-family="{MONO}" font-size="9" letter-spacing="0.8" fill="{t['dim']}">RENDER: B58 TWINPOWER · GPU ACCEL · VITMC 09 · ANTI-ALIAS 4x</text>
    </g>
    '''

    engine_block = f'''
    <!-- Inline-6 Engine Assembly on Chassis -->
    <g class="i6-engine">
      <!-- Crankcase & Cylinder Block Base -->
      <polygon points="900,192 1050,248 1060,242 910,186" fill="{t['card']}" stroke="{t['m_light']}" stroke-width="1.4"/>
      <!-- 6 Cylinders -->
      {"".join(cylinders)}
      <!-- High-Pressure Fuel Rail / Data Pipeline Bus -->
      <line x1="895" y1="188" x2="1055" y2="248" stroke="{t['m_red']}" stroke-width="2" stroke-dasharray="4 4"/>
      <!-- Intake Manifold Plenum -->
      <path d="M 910,185 C 930,170 980,185 1010,195 L 1050,210" fill="none" stroke="{t['m_light']}" stroke-width="2.2"/>
    </g>
    '''

    return f'''
    <g id="3d-engine-viewport">
      {stage}
      {car_wireframe}
      {engine_block}
      {turbo}
      {callouts}
      {console_bar}
    </g>
    '''

def hero(t):
    h = HERO
    stripes = m_stripes(t, 58, 73, 16)
    engine_3d = draw_3d_engine_platform(t)

    words = "".join(
        f'<text class="w{i}" x="228" y="286" font-family="{MONO}" font-size="16.5" fill="{t["ink"]}">'
        f'{esc(w)}<tspan class="cur" fill="{t["m_light"]}">▍</tspan></text>'
        for i, w in enumerate(h["building"])
    )

    pills = []
    px = 58.0
    for p in h["pills"]:
        w = round(mono_w(p, 11) + 22)
        pills.append(
            f'<rect x="{px:g}" y="328" width="{w}" height="26" rx="13" fill="{t["chip"]}" stroke="{t["line"]}"/>'
            f'<text x="{px + 11:g}" y="345" font-family="{MONO}" font-size="11" fill="{t["soft"]}">{esc(p)}</text>'
        )
        px += w + 8

    label = f"{h['name']} — {h['role']} and {h['role2']}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="430" viewBox="0 0 1280 430" role="img" aria-label="{esc(label)}">
<style>
@keyframes drift{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(30px,15px)}}}}
@keyframes word{{0%{{opacity:0;transform:translateY(6px)}}3%,22%{{opacity:1;transform:none}}25%,100%{{opacity:0;transform:translateY(-6px)}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes live{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}
@keyframes spin{{0%{{transform:rotate(0deg)}}100%{{transform:rotate(360deg)}}}}
@keyframes spark{{0%,20%{{fill-opacity:.8;stroke-width:2.2}}30%,100%{{fill-opacity:.15;stroke-width:1}}}}
@keyframes pulse_meter{{0%,100%{{width:66px}}50%{{width:72px}}}}
.g1{{animation:drift 12s ease-in-out infinite}}
.w0{{animation:word 12s infinite;animation-delay:0.0s;opacity:0}}
.w1{{animation:word 12s infinite;animation-delay:3.0s;opacity:0}}
.w2{{animation:word 12s infinite;animation-delay:6.0s;opacity:0}}
.w3{{animation:word 12s infinite;animation-delay:9.0s;opacity:0}}
.cur{{animation:blink 1s step-end infinite}}
.live{{animation:live 1.6s ease-in-out infinite}}
.turbine-spin{{animation:spin 1.8s linear infinite;transform-origin:10px 10px}}
.piston-spark{{animation:spark 3.3s ease-in-out infinite}}
.bar-pulse{{animation:pulse_meter 2.5s ease-in-out infinite}}
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

<!-- Top Metadata Bar (Akshay Style) -->
<g class="top-meta">
  {stripes}
  <text x="105" y="86" font-family="{MONO}" font-size="13" fill="{t["faint"]}">~/ritwik-byt</text>
  <rect x="205" y="72" width="102" height="20" rx="10" fill="{t["chip"]}" stroke="{t["line"]}"/>
  <circle cx="216" cy="82" r="3" fill="{t["m_light"]}"/>
  <text x="225" y="86" font-family="{MONO}" font-size="10.5" fill="{t["soft"]}">3D MOTOR v2</text>
  <rect x="314" y="72" width="56" height="20" rx="10" fill="{t["chip"]}" stroke="{t["line"]}"/>
  <text x="324" y="86" font-family="{MONO}" font-size="10.5" fill="{t["soft"]}">60 FPS</text>

  <!-- Right side header -->
  <text x="730" y="86" font-family="{MONO}" font-size="11.5" letter-spacing="1.2" fill="{t["faint"]}">· 3D MOTOR TELEMETRY · 35° ISOMETRIC</text>
  <circle class="live" cx="1218" cy="82" r="3.5" fill="{t["m_light"]}"/>
  <text x="1208" y="86" text-anchor="end" font-family="{MONO}" font-size="11" fill="{t["m_light"]}">LIVE 7,200 RPM</text>
</g>

<!-- Left Column: Title, Role, Typing & Badges -->
<text x="58" y="158" font-family="{SERIF}" font-size="54" font-weight="400" letter-spacing="-1.2" fill="{t["ink"]}">{esc(h["name"])}</text>
<text x="60" y="206" font-family="{SANS}" font-size="20.5" font-weight="400" letter-spacing="0.2" fill="{t["soft"]}"><tspan fill="{t["ink"]}">{esc(h["role"])}</tspan><tspan fill="{t["m_light"]}">  /  </tspan>{esc(h["role2"])}</text>
<g><text x="60" y="286" font-family="{MONO}" font-size="16.5" fill="{t["faint"]}">$ now tuning</text>{words}</g>
<g>{"".join(pills)}</g>
<text x="60" y="380" font-family="{MONO}" font-size="11.5" fill="{t["dim"]}">{esc(h["tech_line"])}</text>

<!-- Right Column: 3D Isometric Engine & BMW Car Viewport -->
{engine_3d}
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

    stripes = m_stripes(t, 44, 32, 16)
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

<br/>

**[GitHub](https://github.com/ritwik-byt)** &nbsp;·&nbsp; **[LinkedIn](https://www.linkedin.com/in/avv-ritwik-b90046382/)** &nbsp;·&nbsp; **[Email](mailto:alaritwik@gmail.com)** &nbsp;·&nbsp; **[Resume](https://drive.google.com/file/d/1EOpypz-nGTFW8J_EXduz2dsreTF64Ady/view?usp=sharing)** &nbsp;·&nbsp; **[Portfolio](https://portfolio-gilt-nine-48.vercel.app/)** &nbsp;·&nbsp; **[LeetCode](https://leetcode.com/u/AlaRitwik/)**

</div>

<br/>

Computer Science undergraduate specializing in **Data Analytics** at **VIT-AP University, Amaravati** (CGPA: 8.68/10) and **AWS Certified Data Engineer – Associate**. Focused on architecting distributed cloud data pipelines and analytical lakehouses: orchestrating **PySpark** batch transformations in **Databricks**, enforcing strict schema rules, Star Schema dimensional modeling, and tuning **Snappy Parquet** storage for a **79% footprint reduction** and **99% Athena scan cost savings**.

Passionate automotive enthusiast and **BMW M Performance** telemetry follower — analyzing engine telemetry data, forced-induction twin-scroll boost pressure, and power distribution at the intersection of high-torque mechanical engineering and distributed data systems. Actively seeking **Data Engineering Internship** and cloud-native engineering opportunities.

### 🏎️ Interactive 3D Portfolio (BMW & Lakehouse Edition)

<p align="center">
  <a href="https://portfolio-gilt-nine-48.vercel.app/">
    <img src="https://img.shields.io/badge/LIVE%20PORTFOLIO-PORTFOLIO--GILT--NINE--48.VERCEL.APP-0084ff?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Portfolio">
  </a>
</p>

Bespoke automotive-engineered 3D Web Portfolio built with **Three.js**, **Vite**, and **Lenis**:
- **Refinery & Engine Intro:** 10s procedural 3D Medallion refinery & high-speed telemetry sequence.
- **Interactive 3D Lakehouse Pipeline:** Dynamic 3D pipeline stages mapping Bronze ingestion to Snappy Parquet Gold serving.

<br/>

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
        
    README_PATH.write_text(generate_readme())
    print("Successfully built all 3D BMW isometric assets and README.md!")
