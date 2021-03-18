"""
    Unit tests for the salt.modules.state module
"""

import pytest
import salt.loader_context
import salt.modules.state
from tests.support.mock import patch


def test_get_initial_pillar():
    """
    _get_initial_pillar returns pillar data not named context
    """
    ctx = salt.loader_context.LoaderContext()
    pillar_data = {"foo": "bar"}
    named_ctx = ctx.named_context("__pillar__", pillar_data)
    opts = {"__cli": "salt-call", "pillarenv": "base"}
    with patch("salt.modules.state.__pillar__", named_ctx):
        with patch("salt.modules.state.__opts__", opts):
            pillar = salt.modules.state._get_initial_pillar(opts)
            assert pillar == pillar_data
