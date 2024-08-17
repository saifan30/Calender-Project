import calendar
from colorama import Fore, Style, init
from datetime import datetime

# Initialize Colorama
init()

events = {}  # Dictionary to store events

def add_event(year, month, day, event_description):
    """Add an event to a specific date."""
    date_key = (year, month, day)
    if date_key in events:
        events[date_key].append(event_description)
    else:
        events[date_key] = [event_description]

def print_colored_calendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)
    
    # Split the month calendar into lines
    lines = month_calendar.splitlines()
    
    # Header
    header = lines[0]
    print(Fore.YELLOW + Style.BRIGHT + header + Style.RESET_ALL)
    
    # Days of the week
    weekdays = lines[1]
    print(Fore.CYAN + weekdays + Style.RESET_ALL)
    
    # Highlight today's date and show events
    today = datetime.now()
    today_day = today.day if today.year == year and today.month == month else None
    
    # Print weeks with highlight
    for line in lines[2:]:
        days = line.split()
        highlighted_days = []
        for day in days:
            day_int = int(day)
            if today_day and day_int == today_day:
                highlighted_days.append(Fore.RED + day + Style.RESET_ALL)
            else:
                highlighted_days.append(day)
            # Print events if available
            if (year, month, day_int) in events:
                event_text = ' | '.join(events[(year, month, day_int)])
                print(Fore.BLUE + event_text + Style.RESET_ALL)
        print(Fore.GREEN + ' '.join(highlighted_days) + Style.RESET_ALL)

def print_year_calendar(year):
    print(Fore.MAGENTA + Style.BRIGHT + f"Year {year}" + Style.RESET_ALL)
    for month in range(1, 13):
        print_colored_calendar(year, month)
        print("\n")

def export_to_html(year, month, file_name):
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)
    
    with open(file_name, 'w') as file:
        file.write("<html><body>")
        file.write(f"<h1>Calendar for {calendar.month_name[month]} {year}</h1>")
        file.write(month_calendar)
        file.write("</body></html>")

# Usage
yy = 2024  # Select year
mm = 8  # Select month

# Add sample events
add_event(yy, mm, 15, "Sample Event 1")
add_event(yy, mm, 15, "Sample Event 2")

print_colored_calendar(yy, mm)  # Print the colored calendar for a specific month
print_year_calendar(yy)         # Print the entire year's calendar
export_to_html(yy, mm, 'calendar.html')  # Export the calendar for a specific month to HTML
