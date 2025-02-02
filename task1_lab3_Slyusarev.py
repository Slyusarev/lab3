class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        """
        Инициализация объекта книги.

        Args:
            name (str): Название книги.
            author (str): Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """
        Возвращает название книги.

        Returns:
            str: Название книги.
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Возвращает автора книги.

        Returns:
            str: Автор книги.
        """
        return self._author

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта книги.

        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс, представляющий бумажную книгу."""

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация объекта бумажной книги.

        Args:
            name (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц в книге.
        """
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """
        Возвращает количество страниц в книге.
        """
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self._pages = value

    def __str__(self) -> str:
        return f"{super().__str__()} Страниц: {self.pages}"


class AudioBook(Book):
    """Класс, представляющий аудиокнигу."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом с плавающей точкой.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self) -> str:
        return f"{super().__str__()} Продолжительность: {self.duration} мин."
