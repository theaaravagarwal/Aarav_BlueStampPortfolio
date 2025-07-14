// Test model for SCAD viewer
// This demonstrates various shapes and scaling

// Main body
cube([20, 30, 10], center=true);

// Top cylinder
translate([0, 0, 10])
cylinder(h=15, r=8, center=true);

// Side protrusion
translate([15, 0, 0])
cube([5, 20, 8], center=true);

// Bottom base
translate([0, 0, -12.5])
cube([25, 35, 5], center=true);

// Small details
translate([-8, 10, 5])
sphere(r=2);

translate([8, -10, 5])
sphere(r=2); 