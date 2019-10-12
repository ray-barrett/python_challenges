import challenge2
import pytest


@pytest.mark.parametrize(
    "email",
    [
        "clara@example.com",
        "john-doe23@example.com",
        "jane_35@example.com",
        "raybarrett@gmail.com",
        "a@b.c",
        "ray-barrett@gmail.com",
    ],
)
def test_valid_emails(email):
    assert challenge2.is_valid_email(email)


@pytest.mark.parametrize(
    "email",
    [
        "joe%bloggs@example.com",
        "ray.barrett@gmail.com",
        "ray_barrett@gmail.comm",
        "@gmail.com",
        "ray@.com",
        "ray@barrett.",
        "ray@barrettcom",
        "raybarrett",
        "john@doe.com ",
        " email@example.com",
    ],
)
def test_invalid_emails(email):
    assert not challenge2.is_valid_email(email)


@pytest.mark.parametrize(
    "email_list, expected_results",
    [
        (
            [
                "clara@example.com",
                "john-doe23@example.com",
                "jane_35@example.com",
                "raybarrett@gmail.com",
                "a@b.c",
                "ray-barrett@gmail.com",
            ],
            [
                "a@b.c",
                "clara@example.com",
                "jane_35@example.com",
                "john-doe23@example.com",
                "ray-barrett@gmail.com",
                "raybarrett@gmail.com",
            ],
        ),
        (
            [
                "joe%bloggs@example.com",
                "ray.barrett@gmail.com",
                "ray_barrett@gmail.comm",
                "@gmail.com",
                "ray@.com",
                "ray@barrett.",
            ],
            [],
        ),
        (
            [
                "clara@example.com",
                "joe%bloggs@example.com",
                "john-doe23@example.com",
                "jane_35@example.com",
                "ray.barrett@gmail.com",
                "raybarrett@gmail.com",
                "a@b.c",
                "ray-barrett@gmail.com",
                "@gmail.com",
                "ray@.com",
                "ray_barrett@gmail.comm",
                "ray@barrett.",
            ],
            [
                "a@b.c",
                "clara@example.com",
                "jane_35@example.com",
                "john-doe23@example.com",
                "ray-barrett@gmail.com",
                "raybarrett@gmail.com",
            ],
        ),
    ],
)
def test_validate_emails(email_list, expected_results):
    assert challenge2.validate_emails(email_list) == expected_results
