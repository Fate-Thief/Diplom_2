from faker import Faker


def new_user_body():
    fake = Faker()
    return {"email": fake.email(), "password": fake.password(), "name": fake.name()}
