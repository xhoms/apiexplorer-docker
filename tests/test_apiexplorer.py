#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for API Explorer Docker Images."""

import requests
requests.packages.urllib3.disable_warnings()

LOGIN_URL = 'https://localhost/login'


def token():
    r = requests.post(
        LOGIN_URL, verify=False,
        json={'email': 'admin', 'password': 'paloalto'}, timeout=5
    )
    response = r.json().get('response', {})
    return response.get('authentication_token', '')


TOKEN = token()


class TestApiExplorer:

    def test_login_page(self):
        r = requests.get(
            'https://localhost/login', verify=False, timeout=5
        )
        assert r.status_code == 200

    def test_index_page(self):
        r = requests.get(
            'https://localhost/index.html', verify=False, timeout=5,
            headers={'Authentication-Token': TOKEN}
        )
        assert r.status_code == 200

    def test_developer_page(self):
        r = requests.get(
            'https://localhost/developer', verify=False, timeout=5,
            headers={'Authentication-Token': TOKEN}
        )
        assert r.status_code == 200

    def test_settings_page(self):
        r = requests.get(
            'https://localhost/settings', verify=False, timeout=5,
            headers={'Authentication-Token': TOKEN}
        )
        assert r.status_code == 200

    def test_authorization_page(self):
        r = requests.get(
            'https://localhost/authorization', verify=False, timeout=5,
            headers={'Authentication-Token': TOKEN}
        )
        assert r.status_code == 200

    def test_queryexplorer_page(self):
        r = requests.get(
            'https://localhost/queryexplorer', verify=False, timeout=5,
            headers={'Authentication-Token': TOKEN}
        )
        assert r.status_code == 200

    def test_eventexplorer_page(self):
        r = requests.get(
            'https://localhost/eventexplorer', verify=False, timeout=5,
            headers={'Authentication-Token': TOKEN}
        )
        assert r.status_code == 200

    def test_directoryexplorer_page(self):
        r = requests.get(
            'https://localhost/directoryexplorer', verify=False,
            timeout=5, headers={'Authentication-Token': TOKEN}
        )
        assert r.status_code == 200
