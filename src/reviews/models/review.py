"""
This file is part of the OpenCallerDB Project.
Copyright © 2024-2024, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the GPL-2 license attached.
See the LICENSE file for the full license.

Created on: 2024-05-05

Author: Penaz
"""
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import Truncator
from reviews.libs.constants import (EVALUATION_CHOICES, CATEGORIES)


class Review(models.Model):
    """
    The review model: saves a review from a user about a certain phone
    number
    """

    number = models.PositiveIntegerField(
        verbose_name=_("Phone Number"),
        help_text=_(
            "Phone number, including country code, excluding the "
            "'+' symbol, no spaces"
        )
    )

    evaluation = models.CharField(
        max_length=3,
        choices=EVALUATION_CHOICES,
        verbose_name=_("Evaluation"),
        help_text=_("Evaluate your experience with this number")
    )

    category = models.CharField(
        max_length=3,
        choices=CATEGORIES,
        verbose_name=_("Category"),
        help_text=_("The category you would put this number under")
    )

    title = models.CharField(
        max_length=128,
        verbose_name=_("Title"),
        help_text=_("A short description of your experience with this number")
    )

    detail = models.TextField(
        verbose_name=_("Full Review"),
        help_text=_("Describe your experience with this number in detail")
    )

    def __str__(self):
        return Truncator(self.phone_number).chars(100)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ("number",)
