# Static Random Access Memory (SRAM)
  The verification enviroment is setup using Vyoma's UpTick Pro provided for the Hackathon.
  
  ![environment](https://user-images.githubusercontent.com/109404741/180979948-a87779ce-dbc2-4130-8cb1-ecaf071ceedc.PNG)

# Verification environment
  The CoCoTb based python test is explained below. The test drives inputs to the Design Under Test (sram module here) which takes in 5 bit input address (as Addr),
  1 bit Wr (as Write), 1 bit Rd (as Read) and 16 bit data (as data_in). There is a 16 bit data output (as data_out) which takes out data from a particular memory
  address when Read operation is executed.
  
  The memory was initialised with data for the 32 address locations (since address bit is of 5 bits) and data in each location is equal to the address location in 
  decimal. For example data at location 0 is 0b0 and data at location 12 is 0b1100.
  
  The following code was used to initialise the 32x16 memory:
  
  ![data](https://user-images.githubusercontent.com/109404741/180980900-c00a7041-248b-432f-80c4-077d0448591d.PNG)

  The following asserton statement was used to check for errors in the memory design:
  
  ![assert](https://user-images.githubusercontent.com/109404741/180981024-53ce49d4-9b25-4630-be0e-077469f6de59.PNG)

  After running the test case the following error was encountered:
  
  ![error](https://user-images.githubusercontent.com/109404741/180981102-bd9254be-5e92-4b92-a4d2-bdd5648c3700.PNG)
  
  So, there is an error in the SRAM design verilog file.
  
# Verification strategy
  For checking for errors I ran a loop from 0 to 31 and read data from the memory. To check wether the data at the output terminal (data_out) is equal to the data
  that was initialised the following code wss used:
  
  ![algorithm](https://user-images.githubusercontent.com/109404741/180981531-1e743a4a-3b97-495d-a6b8-179e6c56f6c0.PNG)
  
  In the code above data variable was initialised to zero and was checked for all the address locations starting from 0 to 31 and the DUT output was compared to the
  value data at each iteration. As from the previous section we know that the data stored at every location is same as the address location so data at the output must be
  equal to the value of data at each iteration in the above code output. After every iteration data is incremented by 1 to follow the pattern of the data actually stored 
  in the memory.
  
 # Bugs found
   From the above test case one bug was found in the design file (verilog file named as sram.v):
   
   ![bug](https://user-images.githubusercontent.com/109404741/180982429-744b46b8-7ee2-49cc-8d2d-22e027b33dd4.PNG)
   
   From the above code snippet marked with red we can see that the data at the output (data_out) is equal to the data present at the next higher address (Addr+1).
 
# Debug information
  In order to eliminate the design error 1 change is required to be done in the verilog design file:
  
  the line marked with red in the previous section must be changed to ->
  
  data_out = Mem[Addr];
   
   
   
   
   
   
   
   
