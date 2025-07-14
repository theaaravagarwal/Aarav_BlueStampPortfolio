$fn = 100;union() {
	difference() {
		cube(size = [119.3, 75.1, 31.7]);
		translate(v = [2.8, 2.8, 2.8]) {
			cube(size = [113.7, 69.5, 28.9]);
		}
		translate(v = [0, 29.549999999999997, 2.8]) {
			cube(size = [2.8, 16, 25]);
		}
		translate(v = [49.65, 2.4, 28.1]) {
			cube(size = [20.8, 4.0, 6.8]);
		}
		translate(v = [49.65, 68.69999999999999, 28.1]) {
			cube(size = [20.8, 4.0, 6.8]);
		}
		union() {
			translate(v = [0, 0, 30.7]) {
				cube(size = [1.0, 1.0, 1.0]);
			}
			translate(v = [118.3, 0, 30.7]) {
				cube(size = [1.0, 1.0, 1.0]);
			}
			translate(v = [0, 74.1, 30.7]) {
				cube(size = [1.0, 1.0, 1.0]);
			}
			translate(v = [118.3, 74.1, 30.7]) {
				cube(size = [1.0, 1.0, 1.0]);
			}
		}
		translate(v = [12.8, 2.5, 2.5]) {
			cube(size = [4.6, 2.1, 2.6]);
		}
		translate(v = [102.5, 70.5, 2.5]) {
			cube(size = [4.6, 2.1, 2.6]);
		}
	}
	translate(v = [134.3, 0, 0]) {
		rotate(a = [180, 0, 0]) {
			union() {
				difference() {
					union() {
						cube(size = [119.3, 75.1, 2.8]);
						translate(v = [0.8, 0.8, -2.0]) {
							cube(size = [117.7, 73.5, 2.0]);
						}
						translate(v = [49.65, 2.4, -6.0]) {
							cube(size = [20, 3.2, 6.0]);
						}
						translate(v = [49.65, 68.69999999999999, -6.0]) {
							cube(size = [20, 3.2, 6.0]);
						}
						translate(v = [49.65, 2.4, -6.0]) {
							cube(size = [20, 3.2, 2.8]);
						}
						translate(v = [49.65, 68.69999999999999, -6.0]) {
							cube(size = [20, 3.2, 2.8]);
						}
					}
					union() {
						translate(v = [49.65, 2.4, -6.0]) {
							cube(size = [1.0, 1.0, 1.0]);
						}
						translate(v = [68.65, 2.4, -6.0]) {
							cube(size = [1.0, 1.0, 1.0]);
						}
						translate(v = [49.65, 68.69999999999999, -6.0]) {
							cube(size = [1.0, 1.0, 1.0]);
						}
						translate(v = [68.65, 68.69999999999999, -6.0]) {
							cube(size = [1.0, 1.0, 1.0]);
						}
					}
				}
				translate(v = [12.8, 2.8, -2]) {
					cube(size = [4, 1.5, 2]);
				}
				translate(v = [102.5, 70.8, -2]) {
					cube(size = [4, 1.5, 2]);
				}
			}
		}
	}
}
