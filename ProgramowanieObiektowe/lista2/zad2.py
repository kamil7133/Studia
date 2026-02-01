class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    def full_name(self):
        """Return the full name of the person."""
        return f"{self._first_name} {self._last_name}"

    def email(self):
        """Return email in format first.last@wroclaw.merito.pl"""
        return f"{self._first_name.lower()}.{self._last_name.lower()}@wroclaw.merito.pl"


if __name__ == "__main__":
    p = Person("Anna", "Wiśniewska")
    print(p.full_name())           # Anna Wiśniewska
    print(p.email())               # anna.wiśniewska@wroclaw.merito.pl
    p.first_name = "Magda"
    p.last_name = "Zielińska"
    print(p.full_name())           # Magda Zielińska