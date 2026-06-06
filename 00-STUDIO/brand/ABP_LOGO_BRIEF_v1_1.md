# ABP LOGO BRIEF — v1.1
**Date:** 2026-06-06 (updated from v1, 2026-05-31)
**Status:** Mark LOCKED. Banner LOCKED. Governs the ABP mark, WR mark, and applications.
**Storage:** abp-assets/00-STUDIO/brand/ABP_LOGO_BRIEF_v1_1.md

---

## CHANGELOG (v1 → v1.1)
- Compass mark concept executed and locked (replaced the abstract threshold geometry)
- LinkedIn banner produced and locked
- Asset paths added (canon + abp-assets public CDN)
- Production method documented (MJ render → background removal → composite)

---

## 1 — THE WORD THAT GOVERNS EVERYTHING

**Liberation.** Not sentiment — a spatial act. "I am not below your hierarchy. I am outside it." The mark carries it without explaining it.

---

## 2 — THE LOCKED MARK: THE COMPASS

The ABP mark is a **sacred compass pendant** — a fractured stone-and-gold ring with the Hooded Robin at the center, set against a violet cosmos, with three hanging gold tags reading **A · B · P** and compass crosshairs at the four cardinal points.

**Why the compass (not the halo, not the abstract threshold):**
- A compass is for people who left the map — navigation for those who went outside the structure
- The robin at center = the studio's figure, the operator, true north
- The four directions = the dimensions/chambers of the studio (A·B·P·WR)
- The fractured ring = the open halo lineage, evolved — sacred, not broken
- It reads as a **wearable object** (charm/pendant), not a corporate logo — this was the explicit requirement: something people would want to wear

**Production method (for regenerating/extending):**
- Generated in Midjourney v6, photorealistic jewelry-render direction (NOT illustrated/cartoon)
- Reference: the ADR Open Halo canon object as `--cref --cw 100`
- Key prompt shift that worked: "photographed as real jewelry / product photography / real aged gold / real amethyst — NOT illustrated, NOT 3D render, NOT cartoon"
- Letters added in render (A·B·P on hanging tags); WR reserved for future fourth tag or platform mark

---

## 3 — THE MARKS

### Mark A — ABP compass (PRIMARY, LOCKED)
- The full compass pendant with robin, ring, A·B·P tags
- Studio identity mark — the maker's stamp
- Surfaces: LinkedIn, episode title cards, merch, site footer colophon

### Mark B — WR platform mark (PENDING)
- Not yet built. Same compass DNA, simplified for avatar/favicon/corner use at 32px
- For: site header, social avatars, favicon
- Future work

---

## 4 — LOCKED ASSETS

| Asset | Canon path | Public URL |
|---|---|---|
| Compass mark v2 (photoreal) | `00-STUDIO/brand/ABP_COMPASS_MARK_v2.png` | `raw.githubusercontent.com/houdini1906-lgtm/abp-assets/main/ABP_COMPASS_MARK_v2.png` |
| Banner background (carved gate hybrid) | `abp-assets/ABP_BANNER_BG_v1.png` | `raw.githubusercontent.com/houdini1906-lgtm/abp-assets/main/ABP_BANNER_BG_v1.png` |
| LinkedIn banner (composite, LOCKED) | `abp-assets/ABP_LINKEDIN_BANNER_v1.png` | `raw.githubusercontent.com/houdini1906-lgtm/abp-assets/main/ABP_LINKEDIN_BANNER_v1.png` |
| Transparent compass (bg removed) | `abp-assets/compass_transparent.png` | — |
| Banner build script | `abp-assets/make_banner.py` | — |

---

## 5 — THE LOCKED BANNER

**Concept:** the hybrid — looking through an ancient carved stone gate at the dawn of a new world, the compass ghosted into the center where the light rises.

Three doctrines fused in one frame:
- **Structure** — the carved gate (outside, not below)
- **Liberation** — the dawn breaking over the dark land
- **Archive** — the inscriptions carved into the gate pillars
- **Navigation** — the compass mark, ghosted at center, showing the way through

**Specs:**
- 1584×396 (LinkedIn banner native size)
- Compass mark: background removed (rembg), composited at ~25% opacity, centered
- Type: "APOLLO BENZ PRODUCTIONS" gold serif upper-left; "not below. outside." beneath
- Palette: deep violet, sacred gold, dark stone

**Production method (for regenerating):**
- Background generated in MJ (`--ar 16:6`, carved gate opening onto dawn landscape)
- Composite built locally via Python (rembg for bg removal, Pillow for opacity/composite/text)
- Script committed: `make_banner.py`

---

## 6 — COLOR

Gold (#D9B25E) on black/violet is primary. White on black is the print variant. No multicolor studio mark. Violet stays ADR-resonant; the compass interior carries it.

---

## 7 — WHAT'S STILL OPEN

- WR platform mark (Mark B) — avatar/favicon version, not yet built
- Fourth tag (WR) on the compass — currently A·B·P only; WR could be added as a fourth hanging tag or kept to the platform mark
- Profile picture — the banner is locked, but the profile pic (currently the Chucky-tee photo) is a separate open decision
- Episode title card lockup, merch application, site footer colophon — applications pending

---

## 8 — THE BRIEF IN ONE SENTENCE

*A sacred compass pendant for a liberation studio — the robin at true north, the four directions hanging from a fractured halo — built to be worn, and ghosted into a gate at dawn for the banner.*

---

*Mark locked 2026-06-06. Banner locked 2026-06-06. WR platform mark and profile pic remain open.*
