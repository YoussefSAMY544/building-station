import imaplib
import email
from email.header import decode_header
import re
def fetch_otp_from_email():
    # Email account credentials and server settings
    EMAIL = "yousef_sami2010@yahoo.com"
    PASSWORD = "rvxjbxeyoyrnlpek"
    IMAP_SERVER = "imap.mail.yahoo.com"
    IMAP_PORT = 993

    try:
        # Connect to the IMAP server
        print("Connecting to IMAP server...")
        imap = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

        # Login to the email account
        print("Logging in to email account...")
        imap.login(EMAIL, PASSWORD)

        # Select the mailbox (inbox)
        print("Selecting INBOX...")
        imap.select("INBOX")

        # Search for the latest email containing the OTP from qa@ilsainteractive.com
        print("Searching for emails...")
        status, messages = imap.search(None, '(FROM "qa@ilsainteractive.com")', '(SUBJECT "OTP Code for Build Station")', 'UNSEEN')

        if messages:
            print("Found new email(s).")
            # Fetch the latest email containing the OTP
            latest_email_id = messages[0].split()[-1]
            status, msg_data = imap.fetch(latest_email_id, "(RFC822)")

            # Parse the email content
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    # Extract email body
                    email_body = msg.get_payload(decode=True).decode()
                    # Search for all OTP patterns within the email body
                    otp_pattern = r'\b\d{6}\b'  # Pattern for a 6-digit OTP
                    otp_matches = re.findall(otp_pattern, email_body)
                    if otp_matches:
                        # Return the last OTP found
                        return otp_matches[-1]

        else:
            print("No new emails matching the search criteria found.")

    finally:
        # Logout and close the connection
        if imap:
            print("Logging out and closing connection...")
            imap.logout()
