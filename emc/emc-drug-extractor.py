import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import re
from datetime import datetime
import time
import logging
from typing import Dict, List, Optional
import os

class EMCDrugExtractor:
    def __init__(self):
        """Initialize the EMC drug data extractor"""
        self.base_url = "https://www.medicines.org.uk/emc"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.session = requests.Session()
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='emc_extraction.log'
        )
        self.logger = logging.getLogger(__name__)

    def search_drug(self, drug_name: str) -> List[Dict]:
        """
        Search for a drug in the EMC database
        
        Parameters:
        drug_name (str): Name of the drug to search for
        
        Returns:
        List[Dict]: List of search results with drug information
        """
        try:
            search_url = f"{self.base_url}/search-results"
            params = {
                "q": drug_name,
                "searchtype": "medicines"
            }
            
            response = self.session.get(search_url, params=params, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = []
            
            # Find all drug results
            results = soup.find_all('div', class_='search-results')
            
            for result in results:
                drug_info = {
                    'name': self._extract_text(result.find('h3', class_='search-results__title')),
                    'url': self._get_full_url(result.find('a', href=True).get('href')),
                    'company': self._extract_text(result.find('div', class_='search-results__company')),
                    'summary': self._extract_text(result.find('div', class_='search-results__description'))
                }
                search_results.append(drug_info)
            
            return search_results
            
        except Exception as e:
            self.logger.error(f"Error searching for drug {drug_name}: {str(e)}")
            return []

    def extract_drug_details(self, url: str) -> Dict:
        """
        Extract detailed information about a drug from its EMC page
        
        Parameters:
        url (str): URL of the drug's EMC page
        
        Returns:
        Dict: Detailed drug information
        """
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            drug_details = {
                'name': self._extract_text(soup.find('h1', class_='title')),
                'active_ingredients': self._extract_active_ingredients(soup),
                'pharmaceutical_form': self._extract_section(soup, 'Pharmaceutical form'),
                'therapeutic_indications': self._extract_section(soup, 'Therapeutic indications'),
                'posology': self._extract_section(soup, 'Posology and method of administration'),
                'contraindications': self._extract_section(soup, 'Contraindications'),
                'special_warnings': self._extract_section(soup, 'Special warnings and precautions for use'),
                'interactions': self._extract_section(soup, 'Interaction with other medicinal products'),
                'pregnancy_lactation': self._extract_section(soup, 'Fertility, pregnancy and lactation'),
                'side_effects': self._extract_section(soup, 'Undesirable effects'),
                'pharmacological_properties': self._extract_pharmacological_properties(soup),
                'last_updated': self._extract_last_updated(soup)
            }
            
            return drug_details
            
        except Exception as e:
            self.logger.error(f"Error extracting drug details from {url}: {str(e)}")
            return {}

    def _extract_active_ingredients(self, soup) -> List[str]:
        """Extract active ingredients from the drug page"""
        try:
            ingredients_section = soup.find('div', id='composition')
            if ingredients_section:
                ingredients = ingredients_section.find_all('p')
                return [ing.text.strip() for ing in ingredients if ing.text.strip()]
            return []
        except Exception as e:
            self.logger.error(f"Error extracting active ingredients: {str(e)}")
            return []

    def _extract_pharmacological_properties(self, soup) -> Dict:
        """Extract pharmacological properties"""
        try:
            properties = {}
            pharma_section = soup.find('div', id='pharmacological_props')
            if pharma_section:
                subsections = pharma_section.find_all(['h3', 'p'])
                current_section = None
                
                for element in subsections:
                    if element.name == 'h3':
                        current_section = element.text.strip()
                        properties[current_section] = []
                    elif current_section:
                        properties[current_section].append(element.text.strip())
            
            return properties
        except Exception as e:
            self.logger.error(f"Error extracting pharmacological properties: {str(e)}")
            return {}

    def save_to_json(self, data: Dict, filename: str):
        """Save extracted data to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            self.logger.info(f"Data saved to {filename}")
        except Exception as e:
            self.logger.error(f"Error saving data to {filename}: {str(e)}")

    def save_to_csv(self, data: Dict, filename: str):
        """Save extracted data to CSV file"""
        try:
            df = pd.DataFrame([data])
            df.to_csv(filename, index=False, encoding='utf-8')
            self.logger.info(f"Data saved to {filename}")
        except Exception as e:
            self.logger.error(f"Error saving data to {filename}: {str(e)}")

    def batch_extract(self, drug_list: List[str], output_dir: str = "drug_data"):
        """
        Extract data for multiple drugs and save results
        
        Parameters:
        drug_list (List[str]): List of drug names to search for
        output_dir (str): Directory to save output files
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            all_results = []
            for drug_name in drug_list:
                self.logger.info(f"Processing drug: {drug_name}")
                
                # Search for drug
                search_results = self.search_drug(drug_name)
                if not search_results:
                    self.logger.warning(f"No results found for {drug_name}")
                    continue
                
                # Extract details for first result
                drug_details = self.extract_drug_details(search_results[0]['url'])
                if drug_details:
                    all_results.append(drug_details)
                    
                    # Save individual drug data
                    drug_filename = re.sub(r'[^\w\s-]', '', drug_name).lower().replace(' ', '_')
                    self.save_to_json(drug_details, 
                                    os.path.join(output_dir, f"{drug_filename}.json"))
                
                # Respect rate limiting
                time.sleep(2)
            
            # Save combined results
            if all_results:
                combined_filename = os.path.join(output_dir, "combined_drug_data.json")
                with open(combined_filename, 'w', encoding='utf-8') as f:
                    json.dump(all_results, f, indent=4, ensure_ascii=False)
                
                # Create summary CSV
                df = pd.DataFrame(all_results)
                df.to_csv(os.path.join(output_dir, "drug_summary.csv"), 
                         index=False, encoding='utf-8')
                
            return all_results
            
        except Exception as e:
            self.logger.error(f"Error in batch extraction: {str(e)}")
            return []

    def _extract_text(self, element) -> str:
        """Extract text from a BeautifulSoup element safely"""
        return element.text.strip() if element else ""

    def _get_full_url(self, path: str) -> str:
        """Convert relative URL to full URL"""
        return f"{self.base_url}{path}" if path.startswith('/') else path

    def _extract_section(self, soup, section_name: str) -> str:
        """Extract content from a specific section"""
        try:
            section = soup.find('h2', string=re.compile(section_name, re.I))
            if section:
                content = []
                for elem in section.find_next_siblings():
                    if elem.name == 'h2':
                        break
                    content.append(elem.text.strip())
                return '\n'.join(filter(None, content))
            return ""
        except Exception as e:
            self.logger.error(f"Error extracting section {section_name}: {str(e)}")
            return ""

    def _extract_last_updated(self, soup) -> str:
        """Extract last updated date"""
        try:
            date_element = soup.find('div', class_='last-updated')
            if date_element:
                date_text = date_element.text.strip()
                date_match = re.search(r'\d{2}/\d{2}/\d{4}', date_text)
                if date_match:
                    return date_match.group()
            return ""
        except Exception as e:
            self.logger.error(f"Error extracting last updated date: {str(e)}")
            return ""

def main():
    """Main function to demonstrate usage"""
    extractor = EMCDrugExtractor()
    
    # Example drug list
    example_drugs = [
        "paracetamol",
        "ibuprofen",
        "amoxicillin"
    ]
    
    # Extract data for example drugs
    results = extractor.batch_extract(example_drugs, "drug_data")
    
    # Print summary
    print("\nExtraction Summary:")
    print(f"Total drugs processed: {len(results)}")
    print("\nExtracted data saved in 'drug_data' directory:")
    print("- Individual JSON files for each drug")
    print("- Combined results in 'combined_drug_data.json'")
    print("- Summary CSV in 'drug_summary.csv'")

if __name__ == "__main__":
    main()
