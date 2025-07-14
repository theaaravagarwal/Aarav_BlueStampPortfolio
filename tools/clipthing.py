from solid2 import *
import math

# ───────────── Parameters ─────────────
arm_length     = 50.0    # mm, length of each straight arm
arc_radius     = 2.5     # mm, radius of the arc
arc_angle_deg  = 75      # degrees, sweep of the arc
arc_steps      = 60      # resolution of the arc

band_thickness = 7.5     # mm, thickness of the band (strip)
clip_width     = 15.0     # mm, extrusion width

open_gap       = 5.0     # mm, gap between the arms
cutout_radius  = open_gap / 2
cut_margin     = 0.2     # mm, tiny overlap so the box fully clears
cut_depth      = clip_width + 2  # mm, extra depth for the 3D cuts

# ───────────── Path Generator ─────────────
def open_clip_path():
    arc_angle = math.radians(arc_angle_deg)
    pts = [
        (-arc_radius, 0),
        (-arc_radius, arm_length),
    ]
    for i in range(arc_steps + 1):
        theta = math.pi/2 + arc_angle/2 - (arc_angle * i / arc_steps)
        x = arc_radius * math.cos(theta)
        y = arm_length + arc_radius * math.sin(theta)
        pts.append((x, y))
    pts += [
        ( arc_radius, arm_length),
        ( arc_radius, 0),
    ]
    return pts

# ───────────── Main Solid ─────────────
def open_clip_band_hollow():
    path    = open_clip_path()
    outer   = offset(r=band_thickness/2)(polygon(path))
    inner   = offset(r=-band_thickness/2)(polygon(path))
    band2d  = difference()(outer, inner)
    band3d  = linear_extrude(clip_width)(band2d)

    # box to cut out the gap
    cut_box = translate([-open_gap/2,
                         -1000,     # deep enough to clear entire profile
                         0])(
        cube([open_gap,
              arm_length + 1000 - cut_margin,
              cut_depth],
             center=False)
    )

    # semicircle fillet at top center
    arc_angle = math.radians(arc_angle_deg)
    # top‐most point of your arc
    py_top    = arm_length + arc_radius * math.sin(math.pi/2)

    semicircle = translate([0, py_top - cutout_radius, 0])(
        linear_extrude(cut_depth)(
            circle(r=cutout_radius, _fn=arc_steps)
        )
    )

    return difference()(band3d, cut_box, semicircle)

# ───────────── Render ─────────────
scad_render_to_file(
    open_clip_band_hollow(),
    'spring_clip.scad',
    file_header='$fn = %d;' % arc_steps
)

print("success")
