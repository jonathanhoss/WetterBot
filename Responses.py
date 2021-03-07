import Wetter

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("wetter"):
        response = Wetter.dhv_wetter()
        return response
        
    if user_message in ("katze", "kätzchen"):
        return "Miau"

    return "/help for more info"