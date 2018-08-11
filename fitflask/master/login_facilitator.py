from flask_login import login_user

class LoginFacilitator:
    """Uses flask functionality to set the current_user for use throughout app """ 
    
    def log_user_in(self, user):
        login_user(user)
