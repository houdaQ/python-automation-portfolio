# Web Scraping Tool

Professional Python web scraper for extracting data from websites and exporting to CSV/Excel format.

## Features

- Extract data from any public website using CSS selectors
- Handle multiple pages with automatic rate limiting
- Export to CSV or Excel format
- Comprehensive error handling and logging
- Progress tracking and summary statistics
- Timestamp tracking for all scraped data
- Respectful scraping with built-in delays

## Use Cases

- E-commerce product data extraction
- Real estate listings collection
- Job posting aggregation
- News article scraping
- Price monitoring and comparison
- Lead generation
- Research data collection

## Requirements

```
requests>=2.31.0
beautifulsoup4>=4.12.0
pandas>=2.0.0
openpyxl>=3.1.0
lxml>=4.9.0
```

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from web_scraper import WebScraper

# Initialize scraper
scraper = WebScraper("https://example.com")

# Define URLs to scrape
urls = [
    "https://example.com/page1",
    "https://example.com/page2"
]

# Define CSS selectors
selectors = {
    'title': 'h1.title',
    'price': 'span.price',
    'description': 'p.desc'
}

# Scrape pages
scraper.scrape_multiple_pages(urls, selectors, delay=2)

# Export results
scraper.export_to_csv('output.csv')
```

## Demo Example

The script includes a working demo that scrapes quotes from `quotes.toscrape.com`:

```bash
python web_scraper.py
```

**Output:**
- Scrapes 3 pages of quotes
- Extracts quote text, author, and tags
- Exports to `quotes_data.csv`
- Displays summary statistics

## Configuration Options

### Rate Limiting

Control request frequency to avoid overloading servers:

```python
scraper.scrape_multiple_pages(urls, selectors, delay=2)
```

- `delay=1` - Fast (60 requests/min) - Use for small sites
- `delay=2` - Recommended (30 requests/min) - Default
- `delay=5` - Conservative (12 requests/min) - For sensitive sites

### CSS Selectors

Find CSS selectors using browser developer tools:

1. Right-click element → Inspect
2. Copy selector from Elements panel
3. Use in selectors dictionary

**Example selectors:**
```python
selectors = {
    'title': 'h1.product-title',           # Class selector
    'price': '#price-value',                # ID selector  
    'rating': 'div.rating > span:first-child', # Child selector
    'description': 'p[class*="desc"]'       # Attribute selector
}
```

## Export Formats

### CSV Export

```python
scraper.export_to_csv('data.csv')
```

Output: UTF-8 encoded CSV file with headers

### Excel Export

```python
scraper.export_to_excel('data.xlsx')
```

Output: Excel file with formatted columns

## Output Example

**CSV Structure:**
```csv
quote,author,tags,url,scraped_at
"The world as we have created it...",Albert Einstein,change,http://...,2025-01-15 10:30:45
"It is our choices...",J.K. Rowling,abilities,http://...,2025-01-15 10:30:47
```

## Error Handling

The scraper includes robust error handling:

- **Network errors:** Automatic retry with timeout
- **Parsing errors:** Fallback to 'N/A' for missing data
- **Rate limiting:** Built-in delays between requests
- **Invalid URLs:** Skip and continue with next URL

## Ethical Scraping Guidelines

Always scrape responsibly:

- Check robots.txt before scraping
- Use appropriate delays between requests
- Don't overload servers with concurrent requests
- Respect copyright and terms of service
- Only scrape publicly available data

## Troubleshooting

**"Connection timeout"**
- Increase timeout in fetch_page method
- Check internet connection
- Verify website is accessible

**"No data extracted"**
- Verify CSS selectors are correct
- Check if website uses JavaScript (consider Selenium)
- Inspect HTML structure of target site

**"Rate limited / Blocked"**
- Increase delay between requests
- Add more diverse User-Agent headers
- Consider using proxies for large-scale scraping

## Advanced Features

### Custom Headers

Modify headers for specific websites:

```python
scraper.session.headers.update({
    'User-Agent': 'Your custom user agent',
    'Accept-Language': 'en-US,en;q=0.9'
})
```

### Multiple Selectors per Field

Extract multiple elements:

```python
soup.select('div.item')  # Returns list of all matching elements
```

## Technical Details

- **Language:** Python 3.8+
- **Parser:** BeautifulSoup4 with lxml
- **HTTP Client:** Requests with session management
- **Data Processing:** Pandas DataFrames
- **Export:** CSV (UTF-8) and Excel (XLSX)

## Portfolio Value

This script demonstrates:
- Clean, object-oriented Python code
- Professional error handling
- Industry best practices for web scraping
- Comprehensive documentation
- Production-ready features

## License

Free to use for personal and commercial projects.

## Contact

Built by Houda Najib - Available for custom web scraping projects

Portfolio: github.com/houdaQ/python-automation-portfolio

---

**Need custom scraping solutions?** Contact me for freelance web scraping projects!