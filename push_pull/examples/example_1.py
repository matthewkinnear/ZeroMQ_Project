from push_pull.utils.client import create_connection, send_message
from utils.random_user import get_random_user


def example_usage():
    count = 0

    while count < 10:
        random_user = get_random_user()
        socket = create_connection()
        with socket:
            send_message(socket, random_user)
        count += 1
    return


if __name__ == "__main__":
    example_usage()
