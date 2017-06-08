from __future__ import print_function
import httplib2
import os
import pytz

from apiclient import discovery
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.dirname(os.path.abspath(__file__))
    credential_dir = os.path.join(home_dir, os.pardir ,'.credentials')
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()

    return credentials

def get_calendar_list() :
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    #now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).isoformat() # 'Z' indicates UTC time
    #print(now)
    #print('test')

    #print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=4, singleEvents=True,
        orderBy='startTime').execute()
    events_all = eventsResult.get('items', [])

    if not events_all :
        # print('No upcoming events found.')
        return None

    event_return = []
    for event_part in events_all :
        start = event_part['start'].get('dateTime', event_part['start'].get('date'))
        event_info = [start[:10], start[11:16], event_part['summary']]
        event_return.append(event_info)

    event_return.reverse()
    return event_return


#if __name__ == '__main__':
#    main()