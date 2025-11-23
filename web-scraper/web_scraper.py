"""
Professional Web Scraping Tool
Extracts data from websites and exports to CSV/Excel with error handling
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import sys

class WebScraper:
    def __init__(self, base_url):
        """Initialize web scraper with target URL"""
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.data = []
        
    def fetch_page(self, url):
        """Fetch webpage content with error handling"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            print(f"✓ Successfully fetched: {url}")
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"✗ Error fetching {url}: {e}")
            return None
    
    def parse_content(self, html, selectors):
        """
        Parse HTML content using CSS selectors
        
        Args:
            html: HTML content string
            selectors: Dictionary mapping field names to CSS selectors
        
        Returns:
            Dictionary of extracted data
        """
        soup = BeautifulSoup(html, 'html.parser')
        extracted = {}
        
        for field, selector in selectors.items():
            try:
                element = soup.select_one(selector)
                extracted[field] = element.text.strip() if element else 'N/A'
            except Exception as e:
                print(f"✗ Error parsing {field}: {e}")
                extracted[field] = 'N/A'
        
        return extracted
    
    def scrape_multiple_pages(self, urls, selectors, delay=2):
        """
        Scrape multiple pages with rate limiting
        
        Args:
            urls: List of URLs to scrape
            selectors: Dictionary of CSS selectors
            delay: Seconds to wait between requests (avoid rate limiting)
        """
        print(f"\n  Starting web scraping...")
        print(f"Total pages to scrape: {len(urls)}\n")
        
        for idx, url in enumerate(urls, 1):
            print(f"[{idx}/{len(urls)}] Processing...")
            
            html = self.fetch_page(url)
            if html:
                data = self.parse_content(html, selectors)
                data['url'] = url
                data['scraped_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.data.append(data)
            
            # Rate limiting - be respectful to servers
            if idx < len(urls):
                time.sleep(delay)
        
        print(f"\n✓ Scraping complete! Collected {len(self.data)} items\n")
    
    def export_to_csv(self, filename='scraped_data.csv'):
        """Export scraped data to CSV file"""
        if not self.data:
            print("✗ No data to export!")
            return False
        
        try:
            df = pd.DataFrame(self.data)
            df.to_csv(filename, index=False, encoding='utf-8')
            print(f"✓ Data exported to: {filename}")
            print(f"  Total rows: {len(df)}")
            print(f"  Columns: {', '.join(df.columns)}")
            return True
        except Exception as e:
            print(f"✗ Error exporting data: {e}")
            return False
    
    def export_to_excel(self, filename='scraped_data.xlsx'):
        """Export scraped data to Excel file"""
        if not self.data:
            print("✗ No data to export!")
            return False
        
        try:
            df = pd.DataFrame(self.data)
            df.to_excel(filename, index=False, engine='openpyxl')
            print(f"✓ Data exported to: {filename}")
            return True
        except Exception as e:
            print(f"✗ Error exporting to Excel: {e}")
            return False
    
    def display_summary(self):
        """Display summary statistics of scraped data"""
        if not self.data:
            print("No data scraped yet.")
            return
        
        df = pd.DataFrame(self.data)
        print("\n" + "="*60)
        print("SCRAPING SUMMARY")
        print("="*60)
        print(f"Total items scraped: {len(df)}")
        print(f"Fields extracted: {len(df.columns)}")
        print(f"\nFirst 3 items preview:")
        print(df.head(3).to_string())
        print("="*60 + "\n")


# EXAMPLE USAGE - Scrape quotes from quotes.toscrape.com
if __name__ == "__main__":
    
    print("="*60)
    print("WEB SCRAPING DEMONSTRATION")
    print("="*60)
    print("Target: quotes.toscrape.com (demo site)")
    print("="*60 + "\n")
    
    # Initialize scraper
    scraper = WebScraper("http://quotes.toscrape.com")
    
    # Define URLs to scrape (first 3 pages)
    urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
        "http://quotes.toscrape.com/page/3/"
    ]
    
    # Define CSS selectors for data extraction
    # This example scrapes the first quote on each page
    selectors = {
        'quote': 'span.text',
        'author': 'small.author',
        'tags': 'div.tags a.tag'
    }
    
    # Scrape the pages
    scraper.scrape_multiple_pages(urls, selectors, delay=1)
    
    # Display summary
    scraper.display_summary()
    
    # Export to CSV
    scraper.export_to_csv('quotes_data.csv')
    
    print("\n✅ Demo complete! Check quotes_data.csv for results.\n")
    print("="*60)
    print("CUSTOMIZATION GUIDE")
    print("="*60)
    print("To scrape different websites:")
    print("1. Change 'urls' list to your target URLs")
    print("2. Update 'selectors' dictionary with your CSS selectors")
    print("3. Run the script!")
    print("="*60)
