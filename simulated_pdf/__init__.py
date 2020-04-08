from ._version import get_versions

 __version__ = get_versions()["version"]  # noqa
del get_versions
from simulated_pdf import beamline


def initialize(user_ns, broker_name):
    import nslsii

    ret = nslsii.configure_base(user_ns, broker_name, configure_logging=False)

    bl = beamline.build_beamline()
    if set(user_ns).intersection(bl):
        overlap = set(user_ns).intersection(ret)
        raise ValueError(f"there are overlapping names {overlap}")

    user_ns.update(bl)

    return ret + list(bl)
