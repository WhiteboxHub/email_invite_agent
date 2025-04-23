import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import pytz

load_dotenv()

def send_calendar_invite(to_mail: str, subject: str, title: str, date_str: str, time_str: str,invite_discription : str):
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv("EMAIL_PASS")

    start_dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    end_dt = start_dt + timedelta(hours=1)

    start_ics = start_dt.strftime("%Y%m%dT%H%M%S")
    end_ics = end_dt.strftime("%Y%m%dT%H%M%S")

    pst = pytz.timezone("America/Los_Angeles")
    dt = datetime.now(pst)
    formatted_pst_time = dt.strftime("%Y%m%dT%H%M%S")

    ics_content = f"""BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//Your Organization//Your Product//EN
    METHOD:REQUEST
    BEGIN:VEVENT
    UID:{start_ics}@yourdomain.com
    DTSTAMP:{formatted_pst_time}
    DTSTART:{start_ics}
    DTEND:{end_ics}
    SUMMARY:{title}
    DESCRIPTION: {invite_discription}
    LOCATION:Online
    STATUS:CONFIRMED
    SEQUENCE:0
    BEGIN:VALARM
    TRIGGER:-PT10M
    ACTION:DISPLAY
    DESCRIPTION:Reminder
    END:VALARM
    END:VEVENT
    END:VCALENDAR
    """

    # Main message container
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_mail

    # Alternative part for text
    alternative = MIMEMultipart('alternative')
    msg.attach(alternative)

    # Plain text content
    part_email = MIMEText(f"You have been invited to: {title}", "plain")
    alternative.attach(part_email)

    # Calendar content
    part_calendar = MIMEText(ics_content, "calendar;method=REQUEST;name=invite.ics", _charset="utf-8")
    part_calendar.add_header('Content-Disposition', 'inline; filename="invite.ics"')
    part_calendar.add_header('Content-Class', "urn:content-classes:calendarmessage")
    alternative.attach(part_calendar)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(from_email, password)
            smtp.sendmail(from_email, to_mail, msg.as_string())
        print("Invite sent successfully.")
    except Exception as e:
        print(f"Error sending invite: {e}")

send_calendar_invite("khajamdajmeer@gmail.com"
                     ,"kick off the invite automate",
                     "this is the invite from aka",
                     '2025-04-25',
                     "12:30",
                     "you ar invited to attend the recruter call for the ajmeer")