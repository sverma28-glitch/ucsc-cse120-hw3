import pyrtl

if __name__ == "__main__":
    enable = pyrtl.Input(1, "enable")
    reset = pyrtl.Input(1, "reset")
    y = pyrtl.Register(2, "y")

    # TODO: define y.next logic below using the specification in Q4.b)
    # For example: y.next <<= y ^ 1 ...
    y.next <<= pyrtl.mux(
    reset,
    pyrtl.mux(enable, y, y + 1),
    0
)
    trace = pyrtl.SimulationTrace()
    sim = pyrtl.Simulation(tracer=trace)
    sim.step({"reset" : 1, "enable": 0})
    
    # TODO: write more sim.step() cases here and check if the waveform matches expected y.next value
    sim.step({"reset": 0, "enable": 1})
    sim.step({"reset": 0, "enable": 1})
    sim.step({"reset": 0, "enable": 0})
    sim.step({"reset": 0, "enable": 1})
    sim.step({"reset": 1, "enable": 1})
    sim.step({"reset": 0, "enable": 1})
    trace.render_trace()