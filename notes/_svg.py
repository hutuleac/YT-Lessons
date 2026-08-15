"""Shared SVG helpers for notes.

Notes are .py files, so a note that needs a computed diagram (a complete graph with 45 edges
is not worth hand-writing) can call one of these at module level and store the result in its
`diagrams` list. Everything returns a plain SVG string using CSS custom properties for colour,
so diagrams theme themselves in light and dark without duplication.
"""
import math


def complete_graph(n, cx, cy, r, node_r=5.5, stroke="var(--interference)", fill="var(--signal)"):
    """Every node connected to every other — the shape of attention.

    n nodes produce n(n-1)/2 edges, which is the whole point being illustrated: the edges are
    what the model has to keep track of, and they grow quadratically while the nodes grow
    linearly.
    """
    pts = []
    for i in range(n):
        a = -math.pi / 2 + (2 * math.pi * i / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = pts[i]
            x2, y2 = pts[j]
            edges.append(
                f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                f'stroke="{stroke}" stroke-width="1" opacity="0.42"/>'
            )
    nodes = [
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{node_r}" fill="{fill}"/>' for x, y in pts
    ]
    return "".join(edges) + "".join(nodes)


def edge_count(n):
    return n * (n - 1) // 2
