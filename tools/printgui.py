#!/usr/bin/env python3
"""
Launcher for 3D Print Timelapse Visualizer GUI

This script checks for required dependencies and launches the GUI application.
"""

import sys
import subprocess
import importlib

def check_dependencies():
    """Check if all required dependencies are available."""
    required_packages = ['numpy', 'matplotlib', 'PIL']
    missing_packages = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def install_dependencies():
    """Install missing dependencies."""
    print("Installing required dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install dependencies. Please install them manually:")
        print("pip install -r requirements.txt")
        return False

def main():
    """Main launcher function."""
    print("3D Print Timelapse Visualizer - GUI Launcher")
    print("=" * 50)
    
    # Check dependencies
    missing = check_dependencies()
    
    if missing:
        print(f"Missing dependencies: {', '.join(missing)}")
        response = input("Would you like to install them now? (y/n): ")
        
        if response.lower() in ['y', 'yes']:
            if not install_dependencies():
                return
        else:
            print("Please install the required dependencies manually:")
            print("pip install -r requirements.txt")
            return
    
    print("All dependencies found. Launching GUI...")
    
    # Import and run the GUI
    try:
        from printvis import main as gui_main
        gui_main()
    except ImportError as e:
        print(f"Error importing GUI: {e}")
        print("Make sure printvis.py is in the same directory.")
    except Exception as e:
        print(f"Error launching GUI: {e}")

if __name__ == "__main__":
    main() 