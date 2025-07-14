from solid2 import *

# Length of the charger (in mm)
charger_length = 109.7
# Width of the charger (in mm)
charger_width = 65.5
# Height of the charger (in mm)
charger_height = 24.9

# Extra space around the charger for easy fit (in mm)
tolerance = 2

# Internal length of the case (charger + tolerance)
inner_length = charger_length + 2 * tolerance
# Internal width of the case (charger + tolerance)
inner_width = charger_width + 2 * tolerance
# Internal height of the case (charger + tolerance)
inner_height = charger_height + 2 * tolerance

# Thickness of the case walls (in mm)
wall = 2.8
# Height of the lid lip that fits inside the base (in mm)
lid_lip = 2.0
# Clearance between lid and base for easy fitting (in mm)
lid_clearance = 0.8

# Width of the lid tabs (in mm)
tab_width = 20
# Height of the lid tabs (in mm)
tab_height = 6.0
# Depth of the lid tabs (in mm)
tab_depth = 3.2
# Extra clearance for tabs (in mm)
tab_clearance = 0.4
# Offset of tabs from the edge (in mm)
tab_offset_from_edge = 8

# Width of the cable hole (in mm)
cable_hole_width = 16
# Height of the cable hole (in mm)
cable_hole_height = 25
# Depth of the cable hole (in mm, matches wall thickness)
cable_hole_depth = wall

# Radius for corner fillets (in mm)
fillet_radius = 1.0
# --- Improved snap-fit hook parameters ---
hook_width = 6  # wider for more strength
hook_height = 3  # taller for more engagement
hook_depth = 2.5  # deeper for more catch
hook_offset_from_edge = 12  # further from edge for strength
hook_clearance = 0.2  # tighter fit for snap
hook_ramp_angle = 45  # degrees, for sloped face
hook_flex_gap = 0.5  # gap above hook for flex

from solid2 import rotate_extrude, polygon
import math

def cantilever_hook():
    # 2D profile for the hook: ramp (angled), then vertical catch
    ramp_len = hook_height / math.tan(math.radians(hook_ramp_angle))
    profile = [
        [0, 0],  # base
        [ramp_len, 0],  # end of ramp
        [ramp_len, hook_height],  # up to top
        [0, hook_height],  # back to base
    ]
    return linear_extrude(hook_width)(polygon(profile))

# --- Enhanced fastening: add undercut and flex gap to base ---
def make_base():
    outer = cube([
        inner_length + 2 * wall,
        inner_width + 2 * wall,
        inner_height + wall
    ])
    charger_cutout = translate([wall, wall, wall])(
        cube([inner_length, inner_width, inner_height])
    )
    base = outer - charger_cutout
    cable_hole = translate([
        0,
        (inner_width + 2 * wall - cable_hole_width) / 2,
        wall
    ])(
        cube([cable_hole_depth, cable_hole_width, cable_hole_height])
    )
    front_slot = translate([
        (inner_length + 2 * wall - tab_width) / 2,
        wall - tab_clearance,
        inner_height + wall - tab_depth - tab_clearance
    ])(
        cube([tab_width + 2 * tab_clearance, tab_depth + 2 * tab_clearance, tab_height + 2 * tab_clearance])
    )
    back_slot = translate([
        (inner_length + 2 * wall - tab_width) / 2,
        inner_width + wall - tab_depth - tab_clearance,
        inner_height + wall - tab_depth - tab_clearance
    ])(
        cube([tab_width + 2 * tab_clearance, tab_depth + 2 * tab_clearance, tab_height + 2 * tab_clearance])
    )
    corner_fillets = (
        translate([0, 0, inner_height + wall - fillet_radius])(
            cube([fillet_radius, fillet_radius, fillet_radius])
        ) +
        translate([inner_length + 2 * wall - fillet_radius, 0, inner_height + wall - fillet_radius])(
            cube([fillet_radius, fillet_radius, fillet_radius])
        ) +
        translate([0, inner_width + 2 * wall - fillet_radius, inner_height + wall - fillet_radius])(
            cube([fillet_radius, fillet_radius, fillet_radius])
        ) +
        translate([inner_length + 2 * wall - fillet_radius, inner_width + 2 * wall - fillet_radius, inner_height + wall - fillet_radius])(
            cube([fillet_radius, fillet_radius, fillet_radius])
        )
    )
    # Add undercut (catch) and flex gap for snap hooks
    front_hook_undercut = translate([
        hook_offset_from_edge + wall,
        wall - hook_clearance,
        wall - hook_clearance
    ])(
        cube([
            hook_width + 2 * hook_clearance,
            hook_depth + 2 * hook_clearance,
            hook_height + 2 * hook_clearance
        ])
    )
    back_hook_undercut = translate([
        inner_length + 2 * wall - hook_offset_from_edge - hook_width - wall,
        inner_width + wall - hook_depth - hook_clearance,
        wall - hook_clearance
    ])(
        cube([
            hook_width + 2 * hook_clearance,
            hook_depth + 2 * hook_clearance,
            hook_height + 2 * hook_clearance
        ])
    )
    # Flex gap above hook
    front_flex_gap = translate([
        hook_offset_from_edge + wall,
        wall,
        wall + hook_height
    ])(
        cube([
            hook_width,
            hook_depth,
            hook_flex_gap
        ])
    )
    back_flex_gap = translate([
        inner_length + 2 * wall - hook_offset_from_edge - hook_width - wall,
        inner_width + wall - hook_depth,
        wall + hook_height
    ])(
        cube([
            hook_width,
            hook_depth,
            hook_flex_gap
        ])
    )
    return base - cable_hole - front_slot - back_slot - corner_fillets - front_hook_undercut - back_hook_undercut - front_flex_gap - back_flex_gap

# --- Enhanced fastening: use cantilever snap hooks on lid ---
def make_lid():
    # The lid outer should match the base's outer dimensions, but its thickness should not add to the height
    lid_outer = cube([
        inner_length + 2 * wall,
        inner_width + 2 * wall,
        wall
    ])
    # The lip fits inside the base
    lip = translate([lid_clearance, lid_clearance, -lid_lip])(
        cube([
            inner_length + 2 * wall - 2 * lid_clearance,
            inner_width + 2 * wall - 2 * lid_clearance,
            lid_lip
        ])
    )
    # Tabs and hooks remain unchanged
    front_tab = translate([
        (inner_length + 2 * wall - tab_width) / 2,
        wall - tab_clearance,
        -tab_height
    ])(
        cube([tab_width, tab_depth, tab_height])
    )
    back_tab = translate([
        (inner_length + 2 * wall - tab_width) / 2,
        inner_width + wall - tab_depth - tab_clearance,
        -tab_height
    ])(
        cube([tab_width, tab_depth, tab_height])
    )
    front_bridge = translate([
        (inner_length + 2 * wall - tab_width) / 2,
        wall - tab_clearance,
        -tab_height
    ])(
        cube([tab_width, tab_depth, wall])
    )
    back_bridge = translate([
        (inner_length + 2 * wall - tab_width) / 2,
        inner_width + wall - tab_depth - tab_clearance,
        -tab_height
    ])(
        cube([tab_width, tab_depth, wall])
    )
    tab_fillets = (
        translate([(inner_length + 2 * wall - tab_width) / 2, wall - tab_clearance, -tab_height])(cube([fillet_radius, fillet_radius, fillet_radius])) +
        translate([(inner_length + 2 * wall - tab_width) / 2 + tab_width - fillet_radius, wall - tab_clearance, -tab_height])(cube([fillet_radius, fillet_radius, fillet_radius])) +
        translate([(inner_length + 2 * wall - tab_width) / 2, inner_width + wall - tab_depth - tab_clearance, -tab_height])(cube([fillet_radius, fillet_radius, fillet_radius])) +
        translate([(inner_length + 2 * wall - tab_width) / 2 + tab_width - fillet_radius, inner_width + wall - tab_depth - tab_clearance, -tab_height])(cube([fillet_radius, fillet_radius, fillet_radius]))
    )
    # Cantilever snap hooks (front and back)
    front_hook = translate([
        hook_offset_from_edge + wall,
        wall,
        -hook_height
    ])(
        cantilever_hook()
    )
    back_hook = translate([
        inner_length + 2 * wall - hook_offset_from_edge - hook_width - wall,
        inner_width + wall - hook_depth,
        -hook_height
    ])(
        cantilever_hook()
    )
    return lid_outer + lip + front_tab + back_tab + front_bridge + back_bridge - tab_fillets + front_hook + back_hook

# In model(), position the lid so its top is flush with the top of the base

def model():
    base = make_base()
    # The lid should be translated so its top is at the same height as the top of the base
    # The base's top is at z = inner_height + wall
    # The lid's top is at z = 0 (since it's created at z=0 and extends downward)
    # So, translate the lid to z = inner_height + wall - wall (lid thickness) = inner_height
    lid = translate([inner_length + 2 * wall + 15, 0, inner_height])(
        rotate([180, 0, 0])(make_lid())
    )
    return base + lid

scad_render_to_file(model(), 'batterycase.scad', file_header='$fn = 100;')
