
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# DELIVERY CHARGE TEST CASES

def test_invalid_distance_zero():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)


def test_invalid_distance_above_limit():
    with pytest.raises(ValueError):
        delivery_charge(16, 200, False)


def test_free_delivery():
    assert delivery_charge(5, 500, False) == 0


def test_nearby_delivery():
    assert delivery_charge(2, 200, False) == 20


def test_medium_distance_delivery():
    assert delivery_charge(5, 200, False) == 40


def test_far_distance_delivery():
    assert delivery_charge(10, 200, False) == 60


def test_rainy_delivery():
    assert delivery_charge(2, 200, True) == 50


# COUPON TEST CASES

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300


def test_welcome_coupon_not_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)


def test_coupon_below_minimum_order():
    assert apply_coupon(150, "SAVE50", False) == 150


def test_save50_coupon():
    assert apply_coupon(300, "SAVE50", False) == 250


def test_welcome_coupon_first_order():
    assert apply_coupon(500, "WELCOME", True) == 400


# ESTIMATED TIME TEST CASES

def test_normal_delivery_time():
    assert estimated_time(5, False, False) == 35


def test_peak_hour_delivery():
    assert estimated_time(5, True, False) == 45


def test_busy_restaurant_delivery():
    assert estimated_time(5, False, True) == 50


def test_peak_hour_and_busy_restaurant():
    assert estimated_time(5, True, True) == 65
