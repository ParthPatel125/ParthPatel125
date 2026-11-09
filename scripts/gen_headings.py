#!/usr/bin/env python3
"""Render section headings in Caveat (handwriting font, embedded as base64)
with a hand-drawn green underline. Usage: gen_headings.py <caveat.woff2> <out_dir>"""

import base64
import sys

# text -> (slug, measured width at 44px via Chrome getComputedTextLength)
HEADINGS = {
    "experience": ("experience", 151.0),
    "building now": ("building-now", 183.4),
    "what i work with": ("what-i-work-with", 255.6),
}

THEMES = {
    "dark": {"text": "#f0f6fc", "accent": "#3fb950"},
    "light": {"text": "#1f2328", "accent": "#1a7f37"},
}


SIZE = 34  # px; widths in HEADINGS were measured at 44px
SCALE = SIZE / 44.0


def build(text, width, theme, font_b64):
    c = THEMES[theme]
    w = int(width * SCALE) + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="50" viewBox="0 0 {w} 50" role="img" aria-label="{text}">
<defs><style>
@font-face {{ font-family: 'Caveat'; src: url(data:font/woff2;base64,{font_b64}) format('woff2'); font-weight: 700; }}
text {{ font-family: 'Caveat', 'Comic Sans MS', cursive; font-weight: 700; font-size: {SIZE}px; }}
</style></defs>
<text x="2" y="33" fill="{c['text']}">{text}</text>
<path d="M3 42 Q {w * 0.5:.0f} 46 {w - 5} 40" fill="none" stroke="{c['accent']}" stroke-width="2.5" stroke-linecap="round" opacity="0.9"/>
</svg>
'''


if __name__ == "__main__":
    font_b64 = base64.b64encode(open(sys.argv[1], "rb").read()).decode()
    out = sys.argv[2]
    for text, (slug, width) in HEADINGS.items():
        for theme in THEMES:
            path = f"{out}/h-{slug}-{theme}.svg"
            with open(path, "w") as f:
                f.write(build(text, width, theme, font_b64))
            print("wrote", path)
