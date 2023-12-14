class GuestService:
    @staticmethod
    def is_greeting(value: str) -> bool:
        value_lowercase = value.lower()
        return "Welcome to you" in value_lowercase
