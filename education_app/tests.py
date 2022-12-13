import pytest
from django.urls import reverse

from .models import Work

# Create your tests here.
def test_home_page_accessability(client):

    url = reverse("home")

    response = client.get(url)

    assert response.status_code == 200
    assert "Главная страница" in response.content.decode("utf-8")


@pytest.fixture
def default_work():
    work = Work(name="Работа по умолчанию", description="Описание по умолчанию")
    work.save()


@pytest.fixture
def default_another_work():
    work = Work(name="НЕ Работа по умолчанию", description="НЕ Описание по умолчанию")
    work.save()


@pytest.fixture
def works_group(default_work, default_another_work):
    pass


@pytest.mark.django_db
def test_works_list(client, works_group):

    url = reverse("works-list")

    response = client.get(url)

    assert response.status_code == 200
    assert "Работа по умолчанию" in response.content.decode("utf-8")
    assert "НЕ Работа по умолчанию" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_works_detail_one(client, default_work):

    url = reverse("works-detail", args=[1])

    response = client.get(url)

    assert response.status_code == 200
    assert "Работа по умолчанию" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_works_detail_two(client, works_group):

    url = reverse("works-detail", args=[2])

    response = client.get(url)

    assert response.status_code == 200
    assert "НЕ Работа по умолчанию" in response.content.decode("utf-8")


@pytest.mark.django_db
@pytest.mark.parametrize(
    ["pk", "name"],
    [
        [1, "Работа по умолчанию"],
        [2, "НЕ Работа по умолчанию"],
    ],
)
def test_works_detail(pk, name, client, works_group):

    url = reverse("works-detail", args=[pk])

    response = client.get(url)

    assert response.status_code == 200
    assert name in response.content.decode("utf-8")
