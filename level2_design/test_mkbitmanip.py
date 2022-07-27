# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x0     # Initializing source 1 input
    mav_putvalue_src2 = 0x0     # Initializing source 2 input
    mav_putvalue_src3 = 0x0     # Initializing source 3 input
    mav_putvalue_instr = 0x401070B3        # hexadecimal Instruction code for ANDN1
    for mav_putvalue_src3 in range(0,4294967296,1):                # Running a nested for loop comparing the values of all 3 inputs ranging from
        for mav_putvalue_src2 in range(0,4294967296,1):            # 0x00000000 to 0xffffffff
            for mav_putvalue_src1 in range(0,4294967296,1):

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    cocotb.log.info(f'src1 value ={hex(mav_putvalue_src1)}')    # Checking the value of source 1 for which error is occuring
    cocotb.log.info(f'src2 value ={hex(mav_putvalue_src2)}')    # Checking the value of source 2 for which error is occuring
    cocotb.log.info(f'src3 value ={hex(mav_putvalue_src3)}')    # Checking the value of source 3 for which error is occuring
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} for src1 values = {hex(mav_putvalue_src1)} and for src2 = {hex(mav_putvalue_src2)}'
    assert dut_output == expected_mav_putvalue, error_message
    
    
    
    
    
