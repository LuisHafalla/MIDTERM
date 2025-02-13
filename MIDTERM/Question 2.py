from datetime import datetime

def convert_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return "Invalid date format. Please enter in mm/dd/yyyy format."

def main():
    date_input = input("Enter the date (mm/dd/yyyy): ")
    formatted_date = convert_date(date_input)
    print("Date Output:", formatted_date)

if __name__ == "__main__":
    main()
