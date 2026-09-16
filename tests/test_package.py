from importlib.metadata import version

from causallift import __version__


def test_package_version_matches_distribution_metadata() -> None:
    assert __version__ == version("causallift")
