import pyrtl

def datapath(zero, lt, opcode):
    # TODO: implement logic to assign branch below using the specification in Q4.a)
    # For example: branch = zero & lt ~opcode
    branch = (
        ((opcode == 0) & lt) |
        ((opcode == 1) & ~lt) |
        ((opcode == 2) & zero) |
        ((opcode == 3) & ~zero)
    )
    return branch

if __name__ == "__main__":
    zero = pyrtl.Input(1, "zero")
    lt = pyrtl.Input(1, "lt")
    opcode = pyrtl.Input(2, "opcode")

    branch_out = datapath(zero, lt, opcode)

    branch = pyrtl.Output(1, "branch")
    branch <<= branch_out

    sim = pyrtl.Simulation()

    # Example test case below, this should PASS
    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 0})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")
    
    # TODO: write test cases here


    tests = [
        (0, 0, 0, 0),
        (0, 0, 1, 1),
        (0, 1, 1, 0),
        (1, 0, 2, 1),
        (0, 0, 2, 0),
        (0, 0, 3, 1),
        (1, 0, 3, 0)
    ]

    for z, l, op, expected in tests:
        sim.step({"zero": z, "lt": l, "opcode": op})
        assert sim.inspect("branch") == expected

    print("additional test passed")
