import pytest
from main import BooksCollector

@pytest.fixture # фикстура, создает экземпляр класса BooksCollector
def collector():
    return BooksCollector()
