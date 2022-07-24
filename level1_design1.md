# Multiplexer Design Verification
  
  The verification enviroment is setup using Vyoma's UpTick Pro provided for the Hackathon.
  
  ![Verification environment](https://user-images.githubusercontent.com/109404741/180613085-0c2363c3-6f3a-4159-9873-a3b3ea179834.PNG)

# Verification environment

  The CoCoTb based python test is explained below. The test drives inputs to the Design Under Test (mux module here) which takes in 5 bit select
  input and 2 bit data at its 31 input terminals.
  
  The values are assigned to the input ports using:
  
  ![mux inp23](https://user-images.githubusercontent.com/109404741/180613407-c5df745a-c1e1-4340-bb0c-562947382988.PNG)
  ![mux inp31](https://user-images.githubusercontent.com/109404741/180613413-b2f55872-1be3-46cd-9034-6054a71f6184.PNG)
  
  The assert statement is used to compare the expected value with the Multiplexer (DUT) output. On doing this the following error was observed.
  
  ![MUX error 1](https://user-images.githubusercontent.com/109404741/180613560-ec2b2a84-e48e-4a4d-bb76-18814493d88d.PNG)
  
  On analysing the above error we can see that the expected output is not equal to the DUT output for a select input bit combination of 01100.
  After fixing the error another error was observed in the Multiplexer design. The error was as follows:
  
  ![MUX error 2](https://user-images.githubusercontent.com/109404741/180613679-4d18655e-8122-4185-886f-710ee2c64e47.PNG)

  From the above assertion error we can see that the expected output is not equal to the DUT output for a select input bit combination of 11110.
  
# Verification strategy
  
  The Verilog switch case statement has the following default case used for MUX design:
   
  ![Default statement for mux](https://user-images.githubusercontent.com/109404741/180613949-1e21bff2-62f1-4e6f-89bb-af170d610c55.PNG)
  
  Here we can see that the default statement has an output of 0. So in order to avoid any false verification I have avoided using 0 (in 2bit 00 combination) 
  as an input to the input terminals of the Multiplexer. I have considered 1 (in binary as 01), 2 (in binary as 10) and 3 (in binary as 11) as the inputs
  to the MUX input terminals. 
  
  From the input driving points we can see that I have provided the inputs as 1,2,3,1,2,3,...... and so on serially to the input terminals inp0, inp1, inp2, inp3, 
  ... respectively.
  
  The following code snippet was used for locating the select input for which the DUT failed the verification test.
  
  ![main code snippet for MUX](https://user-images.githubusercontent.com/109404741/180614304-ba47fe5d-ed5f-4446-a7e6-4f330fb802a3.PNG)
  
  Here, I ran a loop for the variable 'j' from 0 to 30 (31 values) and assigned it to the sel (select) input of the Multiplexer. In the assertion statement
  for every value of 'j', I divided it by 3 and took the remainder and added a 1 to it to avoid the value 0 as the remainder, so that the values which are
  used to compare the DUT output are the same ones that are provided to the MUX input terminals which are 1,2 and 3. Also the values will follow the same order 
  as provided to the input terminal inp0, inp1, inp2,....
  
# Bugs found

  From the above test cases the following two bugs were found in the verilog code.
  
  ![inp12 error](https://user-images.githubusercontent.com/109404741/180614655-d1fcd65e-e9c6-4fd2-b90c-de573eba99f5.PNG)

  ![inp30 error](https://user-images.githubusercontent.com/109404741/180614659-6edbf434-f008-4a03-b875-333afeb56de7.PNG)
  
  In the first snippet we can see that for select input combination 0b01101 inp12 is assigned. But, for inp12 select input combination of 0b01100 is the correct
  bit combination.
  
  In the second snippet we can see that there is no select input combination written for inp30. So for any value at inp30 the output will always be 0, as the default
  case is 0.
 
# Debug information

  From the above test cases the following two changes are needed to be done:
  
  1) The select input combination for inp12 should be changed from 0b01101 to 0b01100. 
  
  2) The select input combination for inp30 should be introduced as 0b11110 as follows : 
     5'b11110: out = inp30;
