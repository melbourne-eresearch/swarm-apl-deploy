"""
This script is for exporting SWARM's user data intor a CSV file.

Usage: python export_users.py [-h] <-u USERNAME> <-p PASSWORD> <-U URL>
"""

import argparse
import csv
import sys
from datetime import datetime
from time import time

import requests

CSV_FILENAME = "export-users-{}.csv"
CSV_HEADER = ["id", "username", "displayName", "email", "avatar", "group_code", "disabled", "add_question", "trainingStatus"]

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", type=str, help="Admin username", required=True)
parser.add_argument("-p", "--password", type=str, help="Admin password", required=True)
parser.add_argument("-U", "--url", type=str, help="SWARM base URL", required=True)
args = parser.parse_args()

swarm_base_url = args.url


def main():

    create_users_csv(
        get_existing_users(get_jwt_data(args.username, args.password)),
        datetime.fromtimestamp(time()).strftime("%Y-%m-%d-%H-%M-%S"))


def time_now():
    """
    Returns current time.

    :return: current time.
    """
    return datetime.fromtimestamp(time()).strftime("%Y-%m-%d %H:%M:%S")


def get_jwt_data(user, password):
    """
    Gets JWT token for API requests.

    :param user: username for authentication
    :param password: password for authentication
    :return: Authorization header in the format of "Bearer <JWT Access Token>"
    """
    auth_data = {"username": user, "password": password}

    print("{}: Getting JWT tokens from API ...".format(time_now()))
    try:
        r = requests.post(swarm_base_url + "/api/auth", json=auth_data)
        r.raise_for_status()
    except requests.exceptions.RequestException as ex:
        print("{}: Failed to get JWT tokens from API, reason {}".format(time_now(), ex))
        sys.exit()
    else:
        return dict(Authorization="Bearer {}".format(r.json().get("access_token")))


def get_existing_users(headers):
    """
    Gets all users information from SWARM API.

    :param headers: Authorization header in the format of "Bearer <JWT Access Token>"
    :return: A list of dictionaries represent user objects
    """
    print("{}: Loading existing user data from API ...".format(time_now()))
    try:
        r = requests.get(swarm_base_url + '/api/user', headers=headers, timeout=20000)
        r.raise_for_status()
    except requests.exceptions.RequestException as ex:
        print("{}: Failed to load existing users from API, reason {}".format(time_now(), ex))
    else:
        return r.json().get('data')


def create_users_csv(user_data, timestamp):
    """
    Export user data to a CSV file.

    :param user_data: A list of dictionaries represent user objects
    :param timestamp: the timestamp in the file name
    """
    filename = CSV_FILENAME.format(timestamp)

    with open(filename, "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")

        # Write header
        csv_writer.writerow(CSV_HEADER)

        # Write user data
        for data in user_data:
            csv_writer.writerow([
                data['id'], data['username'], data['displayName'], data['email'], data['avatar'], ",".join(
                    [group["code"] for group in data['userGroups']]), "y" if data['inactive'] else "",
                "y" if "ADD_QUESTION" in [permission["code"] for permission in data['permissions']] else "",
                "y" if data['trainingStatus'] else "n"
            ])
    print("The users have been exported to file '{}'".format(filename))


if __name__ == '__main__':

    main()
