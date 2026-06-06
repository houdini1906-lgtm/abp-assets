#!/usr/bin/env python3
"""Composite the Apollo Benz Productions LinkedIn banner."""
import os
from PIL import Image, ImageDraw, ImageFont
from rembg import remove

BASE = os.path.dirname(os.path.abspath(__file__))
BG_PATH = os.path.join(BASE, "ABP_BANNER_BG_v1.png")
COMPASS_PATH = os.path.join(BASE, "ABP_COMPASS_MARK_v2.png")
COMPASS_T_PATH = os.path.join(BASE, "compass_transparent.png")
OUT_PATH = os.path.join(BASE, "ABP_LINKEDIN_BANNER_v1.png")

W, H = 1584, 396
GOLD = (217, 178, 94)  # #D9B25E

TITLE_FONT = "/mnt/skills/examples/canvas-design/canvas-fonts/IBMPlexSerif-Bold.ttf"
TAG_FONT = "/mnt/skills/examples/canvas-design/canvas-fonts/IBMPlexSerif-Italic.ttf"

# Step 2: remove black background from compass mark
print("Removing black background from compass mark...")
with open(COMPASS_PATH, "rb") as f:
    cut = remove(f.read())
with open(COMPASS_T_PATH, "wb") as f:
    f.write(cut)
print(f"Saved {COMPASS_T_PATH}")

# Step 3: resize/center-crop background to 1584x396
print("Resizing background to LinkedIn banner size (center-crop to fill)...")
bg = Image.open(BG_PATH).convert("RGBA")
scale = max(W / bg.width, H / bg.height)
new_size = (round(bg.width * scale), round(bg.height * scale))
bg = bg.resize(new_size, Image.LANCZOS)
left = (bg.width - W) // 2
top = (bg.height - H) // 2
bg = bg.crop((left, top, left + W, top + H))

# Step 4: compass -> ~300px tall, 25% opacity, centered
print("Compositing compass (300px tall, 25% opacity, centered)...")
compass = Image.open(COMPASS_T_PATH).convert("RGBA")
c_scale = 300 / compass.height
compass = compass.resize((round(compass.width * c_scale), 300), Image.LANCZOS)
# apply 25% opacity by scaling the alpha channel
r, g, b, a = compass.split()
a = a.point(lambda v: int(v * 0.25))
compass.putalpha(a)
cx = (W - compass.width) // 2
cy = (H - compass.height) // 2
bg.alpha_composite(compass, (cx, cy))

# Steps 5 & 6: gold serif text, upper-left
print("Adding gold serif text...")
draw = ImageDraw.Draw(bg)
title_font = ImageFont.truetype(TITLE_FONT, 52)
tag_font = ImageFont.truetype(TAG_FONT, 30)
tx, ty = 70, 90
draw.text((tx, ty), "APOLLO BENZ PRODUCTIONS", font=title_font, fill=GOLD)
# place tagline beneath the title
tb = draw.textbbox((tx, ty), "APOLLO BENZ PRODUCTIONS", font=title_font)
draw.text((tx, tb[3] + 16), "not below. outside.", font=tag_font, fill=GOLD)

# Step 7: save final
final = bg.convert("RGB")
final.save(OUT_PATH)
print(f"Saved {OUT_PATH} ({final.width}x{final.height})")
