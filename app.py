import phonenumbers

def validate_and_format_phone_number(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Check if the phone number is valid
        if phonenumbers.is_valid_number(parsed_number):
            # Format the phone number in international format
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            return formatted_number
        else:
            return "Invalid phone number"
    except Exception as e:
        return str(e)

# Example usage
phone_number = "+254799999999"
formatted_number = validate_and_format_phone_number(phone_number)
print("Formatted phone number:", formatted_number)
