# -*- coding: utf-8 -*-

import os

import pytest
from PyPDFForm import (
    InvalidFontSizeError, InvalidFormDataError, InvalidImageCoordinateError,
    InvalidImageDimensionError, InvalidImageError,
    InvalidImageRotationAngleError, InvalidModeError, InvalidPageNumberError,
    InvalidTemplateError, InvalidWrapLengthError, PyPDFForm)


@pytest.fixture
def pdf_samples():
    return os.path.join(os.path.dirname(__file__), "..", "..", "pdf_samples")


@pytest.fixture
def template_stream(pdf_samples):
    with open(os.path.join(pdf_samples, "sample_template.pdf"), "rb+") as f:
        return f.read()


@pytest.fixture
def image_stream(pdf_samples):
    with open(os.path.join(pdf_samples, "sample_image.jpg"), "rb+") as f:
        return f.read()


def test_invalid_template_error():
    try:
        PyPDFForm(b"BAD_TEMPLATE").fill({})
        assert False
    except InvalidTemplateError:
        assert True


def test_invalid_form_data_error(template_stream):
    try:
        PyPDFForm(template_stream).fill("NOT_A_DICT")
        assert False
    except InvalidFormDataError:
        assert True


def test_invalid_mode_error(template_stream):
    try:
        PyPDFForm(template_stream, simple_mode=1).fill({})
        assert False
    except InvalidModeError:
        assert True


def test_invalid_font_size_error(template_stream):
    try:
        PyPDFForm(template_stream, simple_mode=False).fill({}, font_size="12")
        assert False
    except InvalidFontSizeError:
        assert True


def test_invalid_wrap_length_error(template_stream):
    try:
        PyPDFForm(template_stream, simple_mode=False).fill({}, text_wrap_length="100")
        assert False
    except InvalidWrapLengthError:
        assert True


def test_invalid_image_error(template_stream):
    try:
        PyPDFForm(template_stream).draw_image(b"BAD_IMAGE", 1, 100, 100, 400, 225)
        assert False
    except InvalidImageError:
        assert True


def test_invalid_page_number_error(template_stream, image_stream):
    try:
        PyPDFForm(template_stream).draw_image(image_stream, 1.1, 100, 100, 400, 225)
        assert False
    except InvalidPageNumberError:
        assert True


def test_invalid_image_coordinate_error(template_stream, image_stream):
    try:
        PyPDFForm(template_stream).draw_image(image_stream, 1, "100", 100, 400, 225)
        assert False
    except InvalidImageCoordinateError:
        assert True

    try:
        PyPDFForm(template_stream).draw_image(image_stream, 1, 100, "100", 400, 225)
        assert False
    except InvalidImageCoordinateError:
        assert True


def test_invalid_image_dimension_error(template_stream, image_stream):
    try:
        PyPDFForm(template_stream).draw_image(image_stream, 1, 100, 100, "400", 225)
        assert False
    except InvalidImageDimensionError:
        assert True

    try:
        PyPDFForm(template_stream).draw_image(image_stream, 1, 100, 100, 400, "225")
        assert False
    except InvalidImageDimensionError:
        assert True


def test_invalid_image_rotation_angle_error(template_stream, image_stream):
    try:
        PyPDFForm(template_stream).draw_image(image_stream, 1, 100, 100, 400, 225, "90")
        assert False
    except InvalidImageRotationAngleError:
        assert True
