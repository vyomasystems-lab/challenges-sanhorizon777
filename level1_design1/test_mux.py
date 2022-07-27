# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
    A1 = 1
    A2 = 2
    A3 = 3

    #input driving

    dut.inp0.value = A1
    dut.inp1.value = A2
    dut.inp2.value = A3
    dut.inp3.value = A1
    dut.inp4.value = A2
    dut.inp5.value = A3
    dut.inp6.value = A1
    dut.inp7.value = A2
    dut.inp8.value = A3
    dut.inp9.value = A1
    dut.inp10.value = A2
    dut.inp11.value = A3
    dut.inp12.value = A1
    dut.inp13.value = A2
    dut.inp14.value = A3
    dut.inp15.value = A1
    dut.inp16.value = A2
    dut.inp17.value = A3
    dut.inp18.value = A1
    dut.inp19.value = A2
    dut.inp20.value = A3
    dut.inp21.value = A1
    dut.inp22.value = A2
    dut.inp23.value = A3
    dut.inp24.value = A1
    dut.inp25.value = A2
    dut.inp26.value = A3
    dut.inp27.value = A1
    dut.inp28.value = A2
    dut.inp29.value = A3
    dut.inp30.value = A1

    for j in range(0,31,1):
        dut.sel.value = j
        await Timer(2, units='ns')
        
        #cocotb.log.info(f'Error at select input = {bin(j)}')

        error_message = f'Value mismatch at select input = {bin(j)}'
        assert dut.out.value == (j%3) + 1, error_message

    cocotb.log.info('##### CTB: Develop your test here ########')
