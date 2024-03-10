#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 1: Seasons of Love

Description: Tests for Seasons program
"""

import pytest
from datetime import datetime
from seasons import Age


class TestAge:

    def test_valid_date_of_birth(self):
        """Test if Age can be initialized with a valid date of birth in right format"""
        dob = "1990-01-01"
        age = Age(dob)
        assert age.dob == datetime.strptime(dob, "%Y-%m-%d").date()

    def test_invalid_date_of_birth(self):
        """Test if Age raises a ValueError if initialized with an invalid date of birth"""
        dob = "2022-13-40"
        dob_2 = "January 1, 1990"
        with pytest.raises(SystemExit):
            Age(dob)
            Age(dob_2)

    def test_age_in_minutes(self):
        """Test if Age print correct age in minutes with right dob"""
        age = Age("1990-01-01")
        age_2 = Age("2024-01-01")
        age_3 = Age("2023-01-01")
        age_4 = Age("2023-12-31")
        age_5 = Age("2022-01-01")
        age_6 = Age("2022-12-31")
        assert age.age_in_minutes() == 17981280
        assert age_2.age_in_minutes() == 99360
        assert age_3.age_in_minutes() == 624960
        assert age_4.age_in_minutes() == 100800
        assert age_5.age_in_minutes() == 1150560
        assert age_6.age_in_minutes() == 626400
