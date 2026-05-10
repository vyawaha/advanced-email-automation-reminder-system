import pandas as pd


def load_contacts(path="data/contacts.csv"):
    return pd.read_csv(path)


def load_reminders(path="data/reminders.csv"):
    return pd.read_csv(path)