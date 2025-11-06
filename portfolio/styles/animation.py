# animations.py
"""
Reflex-friendly animation dictionaries and helpers for the portfolio.
Design decisions:
- Consistent naming prefixes: page_, scroll_, comp_, hover_
- 'animation' entries reference CSS keyframes defined in style.css
- Use helpers to compose delays / staggered use
"""

from typing import Dict

# Base durations & easings
D = {
    "fast": "0.45s",
    "medium": "0.8s",
    "slow": "1.2s",
    "ease": "cubic-bezier(0.25, 0.46, 0.45, 0.94)",
}

# Page load animations
PAGE_ANIMATIONS: Dict[str, Dict] = {
    "page_fade_in": {"opacity": "0", "animation": f"fade-in-up {D['medium']} {D['ease']} forwards"},
    "page_fade_in_fast": {"opacity": "0", "animation": f"fade-in-up {D['fast']} {D['ease']} forwards"},
}

# Scroll animations (transitions; applied then toggled to final state on intersection)
SCROLL_ANIMATIONS: Dict[str, Dict] = {
    "scroll_fade_in": {
        "opacity": "0",
        "transform": "translateY(30px)",
        "transition": f"opacity {D['medium']} {D['ease']}, transform {D['medium']} {D['ease']}",
    },
    "scroll_fade_left": {
        "opacity": "0",
        "transform": "translateX(-30px)",
        "transition": f"opacity {D['medium']} {D['ease']}, transform {D['medium']} {D['ease']}",
    },
}

# Component-specific
COMPONENT_ANIMATIONS: Dict[str, Dict] = {
    "nav": {"opacity": "0", "transform": "translateY(-12px)", "animation": f"fade-in-right {D['fast']} {D['ease']} 0.15s forwards"},
    "hero_content": {"opacity": "0", "transform": "translateY(20px)", "animation": f"fade-in-up {D['slow']} {D['ease']} 0.25s forwards"},
    "project_card": {"opacity": "0", "transform": "translateY(18px) scale(0.995)", "transition": f"all {D['fast']} {D['ease']}"},
}

# Hover / interactive effects (safely used via _hover in Reflex props)
HOVER_EFFECTS: Dict[str, Dict] = {
    "hover_card_soft": {
        "transition": f"transform {D['fast']} {D['ease']}, box-shadow {D['fast']} {D['ease']}",
        "_hover": {
            "transform": "translateY(-8px) scale(1.02)",
            "boxShadow": "0 20px 40px rgba(0,0,0,0.45)",
        },
    },
    "hover_image_scale": {
        "transition": f"transform {D['slow']} {D['ease']}, filter {D['slow']} {D['ease']}",
        "_hover": {"transform": "scale(1.04)", "filter": "brightness(1.06)"},
    },
}

# Stagger helper (compose)
def with_delay(style: Dict, delay_s: float) -> Dict:
    """Return a copy of style with animation_delay and transition_delay added."""
    out = style.copy()
    d = f"{delay_s:.2f}s"
    # add both keys where relevant
    if "animation" in out:
        out["animation"] = out["animation"].rstrip() + f" {d}"
    out.setdefault("animationDelay", d)
    out.setdefault("transitionDelay", d)
    return out

def stagger_group(base_style: Dict, index: int, step: float = 0.08) -> Dict:
    """Return style with incremental delay depending on index."""
    return with_delay(base_style, delay_s=index * step)

# Combined export
ANIMATIONS = {
    **PAGE_ANIMATIONS,
    **SCROLL_ANIMATIONS,
    **COMPONENT_ANIMATIONS,
    **HOVER_EFFECTS,
}

__all__ = ["PAGE_ANIMATIONS", "SCROLL_ANIMATIONS", "COMPONENT_ANIMATIONS", "HOVER_EFFECTS", "ANIMATIONS", "with_delay", "stagger_group"]
