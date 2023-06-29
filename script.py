import json
from icalendar import Calendar, Event
from datetime import datetime

json_file = input("Enter the JSON file name: ")

# Load JSON data from file
with open(json_file, 'r') as f:
    json_data = f.read()

data_list = json.loads(json_data)['examOffers']

calendar = Calendar()

for data in data_list:
    # Extract exam date and time
    exam_date = data['examDate']['value']
    exam_start_time = data['examStart']['value']
    exam_end_time = data['examEnd']['value']

    # Create calendar event
    event = Event()
    event.add('summary', data['courseName']['value'])
    event.add('description', f"Course ID: {data['courseId']}")
    event.add('dtstart', datetime.strptime(f"{exam_date} {exam_start_time}", "%Y-%m-%d %H:%M:%S"))
    event.add('dtend', datetime.strptime(f"{exam_date} {exam_end_time}", "%Y-%m-%d %H:%M:%S"))

    # Add the event to the calendar
    calendar.add_component(event)

# Write calendar to file
output_file = 'exam_calendar.ics'
with open(output_file, 'wb') as f:
    f.write(calendar.to_ical())

print(f"Calendar file '{output_file}' created successfully.")