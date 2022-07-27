

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
@cocotb.test()
async def test_sram(dut):
    """Test for SRAM"""

    wr = 1
    rd = 0
    data = 0 #Initialising variable as data input to SRAM

    for address in range(0,32,1):
        dut.Wr.value = wr     # writing into memory
        dut.Rd.value = rd
        dut.Addr.value = address
        dut.data_in.value = data
        data = data+1
        await Timer(2,units='ns')

    await Timer(3,units='ns')

    wr = 0
    rd = 1
    data = 0  #initializing data variable or comparing with DUT output

    for address in range(0,32,1):
        dut.Wr.value = wr
        dut.Rd.value = rd    #Reading from SRAM
        dut.Addr.value = address
        await Timer(3,units='ns')

        #obtaining DUT output
        dut_output = dut.data_out.value

        cocotb.log.info(f'DUT OUTPUT = {bin(dut_output)}')
        cocotb.log.info(f'Expected value = {bin(data)}')
        cocotb.log.info(f'Error occured at address = {hex(address)}')

        # comparison
        error_message = f'Value mismatch DUT = {bin(dut_output)} does not match MODEL = {bin(data)}'
        assert dut_output == data, error_message

        await Timer(3,units='ns')
        data = data+1


