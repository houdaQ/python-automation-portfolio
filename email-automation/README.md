# 📧 Automated Email Sender

Professional Python tool for sending personalized bulk emails from CSV data. Built for email marketing, outreach campaigns, and automated notifications.

## Features

- Bulk email sending from CSV files
- Personalized messages with variable substitution
- Rate limiting to prevent spam detection
- Comprehensive error handling and retry logic
- Progress tracking and detailed logs
- Gmail/Outlook/Custom SMTP support
- Professional summary statistics

## Demo

![Email Output Example](./email_output_example.png)

*Example of automated email sent with personalization. The script successfully delivered a professional email with custom formatting and feature highlights.*

## Use Cases

- Email marketing campaigns
- Customer outreach
- Newsletter distribution
- Automated notifications
- Event invitations
- Follow-up sequences

## Requirements

```
pandas>=1.5.0
```

Install with:
```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Prepare Your CSV File

Create `contacts.csv` with these columns:

```csv
email,name
john@example.com,John Smith
jane@example.com,Jane Doe
contact@company.com,Company Name
```

**Required column:** `email`  
**Optional column:** `name` (for personalization)

### 2. Configure Email Settings

Edit the script configuration:

```python
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
YOUR_EMAIL = "your.email@gmail.com"
YOUR_PASSWORD = "your_app_password"
```

### 3. Set Up Gmail App Password

**Important:** Don't use your regular Gmail password!

**Steps:**
1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Go to Security → App Passwords
4. Generate password for "Mail" on "Windows Computer"
5. Copy the 16-character password
6. Use this in the script

### 4. Customize Your Email

```python
SUBJECT = "Your Subject Here"
BODY = """Hello {name},

Your personalized message here.
Use {name} for automatic name insertion.

Best regards,
Your Name
"""
```

### 5. Run the Script

```bash
python email_sender.py
```

## Output Example

```
Email Automation Tool
==================================================
Loaded 50 contacts from contacts.csv

Starting bulk email send...
Subject: Product Launch Announcement
Total recipients: 50
Delay between emails: 2s

Sent to john@example.com
Sent to jane@example.com
Sent to contact@company.com
...

==================================================
SUMMARY
==================================================
Successfully sent: 48
Failed: 2
Duration: 112.3 seconds
==================================================

Process complete!
```

## Configuration Options

### Rate Limiting

Control sending speed to avoid spam detection:

```python
sender.send_bulk_emails(CSV_FILE, SUBJECT, BODY, delay=2)
```

- `delay=1` - Fast (60 emails/min) - risky
- `delay=2` - Recommended (30 emails/min)
- `delay=5` - Safe (12 emails/min)

### SMTP Settings for Different Providers

**Gmail:**
```python
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

**Outlook/Hotmail:**
```python
SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_PORT = 587
```

**Yahoo:**
```python
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
```

## Security Best Practices

- Never commit passwords to GitHub
- Use environment variables for credentials
- Use App Passwords, not account passwords
- Keep CSV files with real emails in `.gitignore`

## Advanced Usage

### Using Environment Variables (Recommended)

```python
import os

YOUR_EMAIL = os.getenv('EMAIL_ADDRESS')
YOUR_PASSWORD = os.getenv('EMAIL_PASSWORD')
```

Set in terminal:
```bash
export EMAIL_ADDRESS="your.email@gmail.com"
export EMAIL_PASSWORD="your_app_password"
```

### HTML Emails

Modify the `create_message` method to support HTML:

```python
msg.attach(MIMEText(body, 'html'))
```

## CSV Format Tips

**Basic format:**
```csv
email,name
john@example.com,John
```

**With additional data:**
```csv
email,name,company,position
john@example.com,John Smith,Tech Corp,Manager
```

Use `{company}` and `{position}` in your email template for personalization.

## Troubleshooting

**"Authentication failed"**
- Use App Password, not regular password
- Enable 2-Factor Authentication first
- Check if "Less secure app access" is needed (older accounts)

**Emails going to spam**
- Reduce sending rate (increase delay)
- Warm up your email (start with small batches)
- Avoid spam trigger words
- Include unsubscribe option

**"Connection refused"**
- Check SMTP server and port
- Verify firewall settings
- Ensure internet connection

## Professional Implementation Tips

1. **Start small:** Test with 5-10 emails first
2. **Warm up:** Gradually increase daily volume
3. **Personalize:** Use recipient names and relevant content
4. **Track results:** Monitor open rates and responses
5. **Follow laws:** Comply with CAN-SPAM Act and GDPR

## Portfolio Value

This script demonstrates:
- Clean, professional code structure
- Comprehensive error handling and logging
- User-friendly interface design
- Production-ready features and best practices

Ideal for demonstrating email automation capabilities to potential clients.

## License

Free to use for personal and commercial projects.

## Contact

Built by Houda Najib_Alaoui - Available for freelance automation projects

---

Star this repository if you find it useful.
