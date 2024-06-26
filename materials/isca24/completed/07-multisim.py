"""
A small multisim example
"""

from gem5.prebuilt.riscvmatched.riscvmatched_board import RISCVMatchedBoard
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

from gem5.utils.multisim import add_simulator

board = RISCVMatchedBoard()

for workload in obtain_resource("riscv-getting-started-benchmark-suite"):
    board.set_workload(workload)
    simulator = Simulator(board=board, id=workload.get_id())

    add_simulator(simulator)