import os


def generate_invitations(template, attendees):
    # --- Type validation ---
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # --- Empty checks ---
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --- Process attendees ---
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template

        for key in placeholders:
            value = attendee.get(key)

            # Replace missing or None with N/A
            if value is None:
                value = "N/A"

            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(output)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
