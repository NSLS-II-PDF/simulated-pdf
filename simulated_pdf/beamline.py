import ophyd.sim as sim
import numpy as np
import functools


def build_beamline():
    def work_function(mtr):
        v = mtr.get().readback
        return np.exp(-(v * v) / 15)

    x = sim.SynAxis(name="x")
    det = sim.SynSignal(name="det", func=functools.partial(work_function, x))
    det.kind = "hinted"
    return {obj.name: obj for obj in [x, det]}
