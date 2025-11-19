"""
Professional Email Automation Tool
Sends personalized bulk emails from CSV data with rate limiting and error handling
"""

import pandas as pd
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import sys

class EmailAutomation:
    def __init__(self, smtp_server, smtp_port, email, password):
        """Initialize email automation with SMTP credentials"""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        self.sent_count = 0
        self.failed_count = 0
        
    def load_contacts(self, csv_file):
        """Load contacts from CSV file"""
        try:
            df = pd.read_csv(csv_file)
            print(f"✓ Loaded {len(df)} contacts from {csv_file}")
            return df
        except Exception as e:
            print(f"✗ Error loading CSV: {e}")
            sys.exit(1)
    
    def create_message(self, to_email, subject, body, name=None):
        """Create personalized email message"""
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Personalize body if name provided
        if name:
            body = body.replace('{name}', name)
        
        msg.attach(MIMEText(body, 'plain'))
        return msg
    
    def send_email(self, to_email, subject, body, name=None):
        """Send single email with error handling"""
        try:
            msg = self.create_message(to_email, subject, body, name)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            
            self.sent_count += 1
            print(f"✓ Sent to {to_email}")
            return True
            
        except Exception as e:
            self.failed_count += 1
            print(f"✗ Failed to send to {to_email}: {e}")
            return False
    
    def send_bulk_emails(self, csv_file, subject, body_template, delay=2):
        """
        Send bulk emails from CSV file
        
        Args:
            csv_file: Path to CSV with 'email' and optionally 'name' columns
            subject: Email subject line
            body_template: Email body (use {name} for personalization)
            delay: Seconds to wait between emails (avoid rate limits)
        """
        contacts = self.load_contacts(csv_file)
        
        print(f"\n📧 Starting bulk email send...")
        print(f"Subject: {subject}")
        print(f"Total recipients: {len(contacts)}")
        print(f"Delay between emails: {delay}s\n")
        
        start_time = datetime.now()
        
        for index, row in contacts.iterrows():
            email = row['email']
            name = row.get('name', None)
            
            self.send_email(email, subject, body_template, name)
            
            # Rate limiting - wait between sends
            if index < len(contacts) - 1:
                time.sleep(delay)
        
        # Summary
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print(f"\n{'='*50}")
        print(f"📊 SUMMARY")
        print(f"{'='*50}")
        print(f"✓ Successfully sent: {self.sent_count}")
        print(f"✗ Failed: {self.failed_count}")
        print(f"⏱ Duration: {duration:.1f} seconds")
        print(f"{'='*50}\n")

# Example usage
if __name__ == "__main__":
    
    # CONFIGURATION - Edit these with your details
    SMTP_SERVER = "smtp.gmail.com"  # Gmail SMTP
    SMTP_PORT = 587
    YOUR_EMAIL = "your.email@gmail.com"  # Your email
    YOUR_PASSWORD = "your_app_password"  # App password (not regular password!)
    
    # Email content
    SUBJECT = "Test Email - Python Automation"
    BODY = """Hello {name},

This is an automated email sent via Python.

This script demonstrates professional email automation capabilities including:
- Bulk sending from CSV
- Personalization
- Rate limiting
- Error handling
- Progress tracking

Best regards,
Automated Email System
"""
    
    # CSV file with contacts (must have 'email' column, 'name' optional)
    CSV_FILE = "contacts.csv"
    
    # Initialize and send
    print("Email Automation Tool")
    print("="*50)
    
    sender = EmailAutomation(SMTP_SERVER, SMTP_PORT, YOUR_EMAIL, YOUR_PASSWORD)
    sender.send_bulk_emails(CSV_FILE, SUBJECT, BODY, delay=2)
    
    print("✅ Process complete!")
