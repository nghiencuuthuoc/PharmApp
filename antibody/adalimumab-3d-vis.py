import os
import Bio.PDB
from Bio.PDB import *
import pymol
import requests
from pathlib import Path

class AdalimumabVisualizer:
    def __init__(self, pdb_id="6GRL"):  # 6GRL is one of the PDB IDs for adalimumab
        self.pdb_id = pdb_id
        self.pdb_file = f"{pdb_id}.pdb"
        self.parser = Bio.PDB.PDBParser(QUIET=True)
        
    def download_structure(self):
        """Download PDB file if not already present"""
        if not os.path.exists(self.pdb_file):
            url = f"https://files.rcsb.org/download/{self.pdb_id}.pdb"
            response = requests.get(url)
            if response.status_code == 200:
                with open(self.pdb_file, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded PDB file: {self.pdb_file}")
            else:
                raise Exception(f"Failed to download PDB file: {response.status_code}")
                
    def analyze_structure(self):
        """Analyze the protein structure"""
        structure = self.parser.get_structure(self.pdb_id, self.pdb_file)
        
        # Get basic structure information
        chains = list(structure.get_chains())
        residues = list(structure.get_residues())
        atoms = list(structure.get_atoms())
        
        print(f"\nStructure Analysis of Adalimumab ({self.pdb_id}):")
        print(f"Number of chains: {len(chains)}")
        print(f"Number of residues: {len(residues)}")
        print(f"Number of atoms: {len(atoms)}")
        
        return structure
    
    def visualize_pymol(self):
        """Create PyMOL visualization"""
        pymol.finish_launching()
        cmd = pymol.cmd
        
        # Load structure
        cmd.load(self.pdb_file)
        
        # Clear previous settings
        cmd.delete("all")
        cmd.load(self.pdb_file)
        
        # Basic representation
        cmd.hide("all")
        cmd.show("cartoon")
        cmd.color("marine")
        
        # Highlight important regions
        cmd.select("binding_site", "resi 91-102")  # Example binding site residues
        cmd.color("yellow", "binding_site")
        cmd.show("sticks", "binding_site")
        
        # CDR regions (complementarity-determining regions)
        cdr_regions = {
            "CDR-H1": "resi 31-35",
            "CDR-H2": "resi 50-65",
            "CDR-H3": "resi 95-102",
            "CDR-L1": "resi 24-34",
            "CDR-L2": "resi 50-56",
            "CDR-L3": "resi 89-97"
        }
        
        colors = ["red", "green", "blue", "orange", "purple", "cyan"]
        
        for (cdr, selection), color in zip(cdr_regions.items(), colors):
            cmd.select(cdr, selection)
            cmd.color(color, cdr)
            cmd.show("sticks", cdr)
        
        # Additional visualization settings
        cmd.set("cartoon_transparency", 0.5)
        cmd.set("sphere_transparency", 0.5)
        cmd.set("stick_radius", 0.3)
        cmd.set("surface_quality", 1)
        
        # Set view
        cmd.zoom()
        cmd.orient()
        
        # Add surface representation
        cmd.show("surface", "all")
        cmd.set("surface_transparency", 0.3)
        
        print("\nVisualization controls:")
        print("- Left mouse: Rotate")
        print("- Middle mouse: Zoom")
        print("- Right mouse: Translate")
        print("- Ctrl+Left mouse: Clip")
        
        # Keep PyMOL session open
        pymol.cmd.rock()

def main():
    # Initialize visualizer
    viz = AdalimumabVisualizer()
    
    try:
        # Download structure
        viz.download_structure()
        
        # Analyze structure
        structure = viz.analyze_structure()
        
        # Create visualization
        viz.visualize_pymol()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        
if __name__ == "__main__":
    main()
