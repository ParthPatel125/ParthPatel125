#!/usr/bin/env python3
"""Generate the intro SVGs: bold Archivo Black type, slide-up entrance,
looping shine sweep across the name. Font embedded as base64 so it renders
the same on every machine."""

import base64
import sys

NAME = "parth patel"
TAGLINE = "I build apps and websites."

THEMES = {
    "dark":  {"name": "#f0f6fc", "tag": "#9da7b3", "accent": "#3fb950"},
    "light": {"name": "#1f2328", "tag": "#59636e", "accent": "#1a7f37"},
}

FONT_B64 = base64.b64encode(
    open(sys.argv[2], "rb").read()
).decode()

FAMILY = "'Archivo Black', 'Arial Black', Arial, sans-serif"


def build(theme):
    c = THEMES[theme]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="130" viewBox="0 0 880 130" role="img" aria-label="{NAME}. {TAGLINE}">
<title>{NAME}</title>
<defs>
<linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="220" y2="0">
<stop offset="0" stop-color="{c['accent']}" stop-opacity="0"/>
<stop offset="0.5" stop-color="{c['accent']}" stop-opacity="0.9"/>
<stop offset="1" stop-color="{c['accent']}" stop-opacity="0"/>
<animateTransform attributeName="gradientTransform" type="translate" values="-240 0; 980 0; 980 0" keyTimes="0; 0.3; 1" dur="4.5s" begin="1s" repeatCount="indefinite"/>
</linearGradient>
<style>
@font-face {{
  font-family: 'Archivo Black';
  src: url(data:font/woff2;base64,{FONT_B64}) format('woff2');
  font-weight: 400;
  font-style: normal;
}}
.name, .tag {{ font-family: {FAMILY}; }}
.name {{ font-size: 42px; letter-spacing: -1px; }}
.tag  {{ font-size: 18px; letter-spacing: -0.25px; }}
.in   {{ animation: rise 0.65s cubic-bezier(0.22, 1, 0.36, 1) both; }}
.d1   {{ animation-delay: 0.1s; }}
.d2   {{ animation-delay: 0.35s; }}
.bar  {{ transform-origin: 0 0; animation: grow 0.55s cubic-bezier(0.22, 1, 0.36, 1) 0.55s both; }}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(16px); }} to {{ opacity: 1; transform: translateY(0); }} }}
@keyframes grow {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
</style>
</defs>
<g class="in d1">
<text class="name" x="0" y="52" fill="{c['name']}">{NAME}</text>
<text class="name" x="0" y="52" fill="url(#shine)">{NAME}</text>
</g>
<rect class="bar" x="2" y="66" width="240" height="7" fill="{c['accent']}"/>
<text class="tag in d2" x="0" y="108" fill="{c['tag']}">{TAGLINE}</text>
</svg>
'''


if __name__ == "__main__":
    out_dir = sys.argv[1]
    for theme in THEMES:
        path = f"{out_dir}/intro-{theme}.svg"
        with open(path, "w") as f:
            f.write(build(theme))
        print("wrote", path)
