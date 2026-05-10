CREATE TABLE contacts(
    id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    timezone TEXT DEFAULT 'Asia/Kolkata',
    unsubscribed BOOLEAN DEFAULT 0
);

CREATE TABLE templates(
    id TEXT PRIMARY KEY,
    name TEXT UNIQUE,
    subject TEXT,
    body_md TEXT,
    created_at TEXT
);

CREATE TABLE campaigns(
    id TEXT PRIMARY KEY,
    name TEXT,
    template_id TEXT,
    sender_name TEXT,
    sender_email TEXT,
    created_at TEXT
);

CREATE TABLE reminders(
    id TEXT PRIMARY KEY,
    title TEXT,
    contact_id TEXT,
    campaign_id TEXT,
    start_at_utc TEXT,
    rrule TEXT,
    active BOOLEAN DEFAULT 1,
    last_fired_at_utc TEXT
);

CREATE TABLE messages(
    id TEXT PRIMARY KEY,
    campaign_id TEXT,
    contact_id TEXT,
    scheduled_at_utc TEXT,
    sent_at_utc TEXT,
    provider_msg_id TEXT,
    status TEXT,
    subject TEXT,
    body_rendered_html TEXT,
    error TEXT
);