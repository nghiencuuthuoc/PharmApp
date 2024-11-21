import Bio.PDB
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import requests
import pandas as pd
import numpy as np
from Bio import SeqIO
from Bio.PDB import *
from Bio.PDB.DSSP import dssp_dict_from_pdb_file
import warnings
warnings.filterwarnings('ignore')

class AdalimumabAnalyzer:
    def __init__(self):
        # Adalimumab heavy chain sequence
        self.heavy_chain = """
        EVQLVESGGGLVQPGRSLRLSCAASGFTFDDYAMHWVRQAPGKGLEWVSAITWNSGHIDYADSVEGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCAKVSYLSTASSLDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK
        """
        # Adalimumab light chain sequence
        self.light_chain = """
        DIQMTQSPSSLSASVGDRVTITCRASQGIRNYLAWYQQKPGKAPKLLIYAASTLQSGVPSRFSGSGSGTDFTLTISSLQPEDVATYYCQRYNRAPYTFGQGTKVEIKRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC
        """
        
    def calculate_basic_properties(self, sequence):
        """Calculate basic physicochemical properties"""
        # Remove whitespace and create ProteinAnalysis object
        sequence = sequence.replace("\n", "").replace(" ", "")
        protein = ProteinAnalysis(sequence)
        
        properties = {
            "Molecular Weight (Da)": round(protein.molecular_weight(), 2),
            "Theoretical pI": round(protein.isoelectric_point(), 2),
            "Aromaticity": round(protein.aromaticity(), 3),
            "Instability Index": round(protein.instability_index(), 2),
            "GRAVY (Grand Average of Hydropathy)": round(protein.gravy(), 3),
        }
        
        return properties
    
    def calculate_amino_acid_composition(self, sequence):
        """Calculate amino acid composition"""
        sequence = sequence.replace("\n", "").replace(" ", "")
        protein = ProteinAnalysis(sequence)
        composition = protein.get_amino_acids_percent()
        return {k: round(v * 100, 2) for k, v in composition.items()}
    
    def calculate_secondary_structure(self, sequence):
        """Predict secondary structure composition"""
        sequence = sequence.replace("\n", "").replace(" ", "")
        protein = ProteinAnalysis(sequence)
        helix, turn, sheet = protein.secondary_structure_fraction()
        return {
            "Alpha Helix (%)": round(helix * 100, 2),
            "Beta Sheet (%)": round(sheet * 100, 2),
            "Turn (%)": round(turn * 100, 2)
        }
    
    def calculate_extinction_coefficient(self, sequence):
        """Calculate extinction coefficient"""
        sequence = sequence.replace("\n", "").replace(" ", "")
        protein = ProteinAnalysis(sequence)
        
        extinction_coeffs = {
            "Extinction coefficient (all Cys form disulfide bonds)": 
                protein.molar_extinction_coefficient()[0],
            "Extinction coefficient (no Cys form disulfide bonds)": 
                protein.molar_extinction_coefficient()[1]
        }
        return extinction_coeffs
    
    def analyze_flexibility(self, sequence):
        """Analyze protein flexibility"""
        sequence = sequence.replace("\n", "").replace(" ", "")
        protein = ProteinAnalysis(sequence)
        flexibility = protein.flexibility()
        return {
            "Average Flexibility": round(np.mean(flexibility), 3),
            "Maximum Flexibility": round(max(flexibility), 3),
            "Minimum Flexibility": round(min(flexibility), 3)
        }
    
    def get_complete_analysis(self):
        """Perform complete analysis of both chains"""
        results = {}
        
        # Analyze heavy chain
        results["Heavy Chain"] = {
            "Basic Properties": self.calculate_basic_properties(self.heavy_chain),
            "Amino Acid Composition (%)": self.calculate_amino_acid_composition(self.heavy_chain),
            "Secondary Structure": self.calculate_secondary_structure(self.heavy_chain),
            "Extinction Coefficient": self.calculate_extinction_coefficient(self.heavy_chain),
            "Flexibility": self.analyze_flexibility(self.heavy_chain)
        }
        
        # Analyze light chain
        results["Light Chain"] = {
            "Basic Properties": self.calculate_basic_properties(self.light_chain),
            "Amino Acid Composition (%)": self.calculate_amino_acid_composition(self.light_chain),
            "Secondary Structure": self.calculate_secondary_structure(self.light_chain),
            "Extinction Coefficient": self.calculate_extinction_coefficient(self.light_chain),
            "Flexibility": self.analyze_flexibility(self.light_chain)
        }
        
        # Calculate whole antibody properties
        complete_sequence = self.heavy_chain + self.light_chain
        results["Complete Antibody"] = {
            "Basic Properties": self.calculate_basic_properties(complete_sequence),
            "Amino Acid Composition (%)": self.calculate_amino_acid_composition(complete_sequence),
            "Secondary Structure": self.calculate_secondary_structure(complete_sequence),
            "Extinction Coefficient": self.calculate_extinction_coefficient(complete_sequence),
            "Flexibility": self.analyze_flexibility(complete_sequence)
        }
        
        return results
    
    def generate_report(self):
        """Generate a formatted report of the analysis"""
        results = self.get_complete_analysis()
        
        print("=== Adalimumab Physicochemical Properties Analysis ===\n")
        
        for chain in ["Heavy Chain", "Light Chain", "Complete Antibody"]:
            print(f"\n{chain} Analysis:")
            print("-" * 50)
            
            # Basic Properties
            print("\nBasic Properties:")
            for prop, value in results[chain]["Basic Properties"].items():
                print(f"{prop}: {value}")
            
            # Secondary Structure
            print("\nSecondary Structure Composition:")
            for struct, value in results[chain]["Secondary Structure"].items():
                print(f"{struct}: {value}")
            
            # Extinction Coefficient
            print("\nExtinction Coefficients:")
            for coeff, value in results[chain]["Extinction Coefficient"].items():
                print(f"{coeff}: {value}")
            
            # Flexibility
            print("\nFlexibility Analysis:")
            for flex, value in results[chain]["Flexibility"].items():
                print(f"{flex}: {value}")
            
            # Amino Acid Composition
            print("\nAmino Acid Composition (%):")
            aa_comp = results[chain]["Amino Acid Composition (%)"]
            for aa, percentage in aa_comp.items():
                print(f"{aa}: {percentage}%")
            
            print("\n" + "="* 50)
        
        return results

def main():
    analyzer = AdalimumabAnalyzer()
    analyzer.generate_report()

if __name__ == "__main__":
    main()
