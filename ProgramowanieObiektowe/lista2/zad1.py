class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    # Getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    # Setters
    def set_first_name(self, name):
        self.__first_name = name

    def set_last_name(self, name):
        self.__last_name = name

    def full_name(self):
        """Return the full name of the person."""
        return f"{self.__first_name} {self.__last_name}"

    def email(self):
        """Return email in format first.last@wroclaw.merito.pl"""
        return f"{self.__first_name.lower()}.{self.__last_name.lower()}@wroclaw.merito.pl"


if __name__ == "__main__":
    p = Person("Jan", "Kowalski")
    print(p.full_name())           # Jan Kowalski
    print(p.email())               # jan.kowalski@wroclaw.merito.pl
    p.set_first_name("Adam")
    p.set_last_name("Nowak")
    print(p.full_name())           # Adam Nowak

