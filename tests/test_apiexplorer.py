#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for API Explorer Docker Images."""

import requests
requests.packages.urllib3.disable_warnings()


class TestApiExplorer:

    def test_login_page(self):
        r = requests.get(
            'https://localhost/login', verify=False, timeout=5
        )
        assert r.status_code == 200
