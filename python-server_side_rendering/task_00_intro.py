import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        content = template
        content = content.replace("{name}", str(attendee.get("name") or "N/A"))
        content = content.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        content = content.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        content = content.replace("{event_location}", str(attendee.get("event_location") or "N/A"))
        
        filename = f"output_{i}.txt"
        with open(filename, 'w') as f:
            f.write(content)
