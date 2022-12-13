import pytest
from django.test import TestCase
from rest_framework.test import APIClient

from education_app.models import Work

# Create your tests here.
@pytest.fixture
def default_work():
    work = Work(name="Работа по умолчанию", description="Описание по умолчанию")
    work.save()


@pytest.fixture
def default_another_work():
    work = Work(name="НЕ Работа по умолчанию", description="НЕ Описание по умолчанию")
    work.save()


@pytest.fixture
def default_another_one_work():
    work = Work(name="Третья работа!", description="НЕ Описание по умолчанию")
    work.save()


@pytest.fixture
def default_another_two_work():
    work = Work(name="Четвёртая работа!", description="НЕ Описание по умолчанию")
    work.save()


@pytest.fixture
def works_group(
    default_work,
    default_another_work,
    default_another_one_work,
    default_another_two_work,
):
    pass


@pytest.mark.django_db
def test_works_list_api(works_group):

    client = APIClient()

    response = client.get("/api/works/")

    assert response.status_code == 200
    assert len(response.data) == 4
    assert response.data[0]["name"] == "Работа по умолчанию"


@pytest.mark.django_db
def test_works_list_api(works_group):

    client = APIClient()

    response = client.get("/api/works/best-works", follow=True)

    assert response.status_code == 200
    assert len(response.data) == 3
