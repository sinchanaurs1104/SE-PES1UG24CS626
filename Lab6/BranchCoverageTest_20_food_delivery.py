
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# DELIVERY CHARGE TEST CASES

def test_invalid_distance_above_limit():
    with pytest.raises(ValueError):
        delivery_charge(16, 200, False)


def test_valid_distance_upper_boundary():
    assert delivery_charge(15, 200, False) == 60


def test_free_delivery():
    assert delivery_charge(5, 500, False) == 0


def test_nearby_delivery():
    assert delivery_charge(3, 200, False) == 20


def test_medium_distance_delivery():
    assert delivery_charge(5, 200, False) == 40


def test_far_distance_delivery():
    assert delivery_charge(10, 200, False) == 60


def test_raining():
    assert delivery_charge(2, 200, True) == 50


def test_not_raining():
    assert delivery_charge(2, 200, False) == 20


# COUPON TEST CASES

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300


def test_save50_coupon():
    assert apply_coupon(300, "SAVE50", False) == 250


def test_welcome_coupon_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_welcome_coupon_not_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)


def test_order_below_minimum():
    assert apply_coupon(150, "SAVE50", False) == 150


def test_order_at_minimum():
    assert apply_coupon(200, "SAVE50", False) == 150


# ESTIMATED TIME TEST CASES

def test_normal_delivery():
    assert estimated_time(5, False, False) == 35


def test_peak_hour():
    assert estimated_time(5, True, False) == 45


def test_busy_restaurant():
    assert estimated_time(5, False, True) == 50


def test_peak_and_busy():
    assert estimated_time(5, True, True) == 65
