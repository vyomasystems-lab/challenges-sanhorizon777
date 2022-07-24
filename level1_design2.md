# Sequence detector
  The verification enviroment is setup using vyoma's UpTick Pro provided for Hackathon.
  
  ![Environment](https://user-images.githubusercontent.com/109404741/180653592-dc81656f-e24b-4b80-8363-9c367f65c25b.PNG)

# Verification environment
  The CoCoTb based python test is explained below. The test drives inputs to the Design Under Test (Sequence Detector module) which takes in 1 bit
  input which gives the input sequence and a 1 bit reset input which will reset the output of the detector.
  
  The values that were provided to drive the input terminal (inp_bit) and reset input are shown below:
  
  ![Input values](https://user-images.githubusercontent.com/109404741/180654055-8d8b610f-bf57-4ff4-97d7-b08f92e50ee3.PNG)

  The following assertion statement was used to check wether the Design Under Test (DUT) is giving output 1 when a sequence 1011 is given
  at the sequence input terminal (inp_bit):
  
  ![Assert statement](https://user-images.githubusercontent.com/109404741/180654211-d84d1d8d-f249-426b-956d-31acc3e2ee94.PNG)
  
  After running the test case, the test failed.
  
  ![Error](https://user-images.githubusercontent.com/109404741/180654593-973bf0d9-3e93-431a-a78b-bdd6a66b372f.PNG)
  
# Verification strategy
  In order to find the bug in the verilog design file, state diagram was used to check the validitiy of the switch case used in the verilog file.
  The state diagram is as follows : 
  
  ![SEQ_1011](https://user-images.githubusercontent.com/109404741/180655429-02a7d32f-6804-4291-873e-95f60d828664.PNG)
  
  In order to check wether the sequence detector is working or not, an input sequence of 101011 is sent. So, at the end of the sequence the Detector must
  reach the state marked as SEQ_1011 and produce an output 1. But, instead the detector didn't produce an output bit 1 which means it didn't reach the state
  SEQ_1011. 
  This means that there is an error in the switch statemets used in the verilog file.
  
# Bugs found
  The following bugs were found after carefully comparing the state diagram with the switch cases from the verilog file. They are marked below:
  
  ![Bugs](https://user-images.githubusercontent.com/109404741/180655753-f11bbfaa-2202-4335-b126-cbed62b4b175.PNG)
  
  In the above code snippet:
  1. Bug 1 - This line is marked as a bug because according to the state diagram if the detector is in SEQ_1 state and the input bit (inp_bit) is 1
    then the system should stay in state SEQ_1.
  2. Bug 2 - This line is marked as a bug because according to the state diagram if the detector is in SEQ_101 state and the input bit (inp_bit) is 0
    then the system should move to state SEQ_10.
  3. Bug 3 - This line is marked as a bug because according to the state diagram if the detector is in SEQ_1011 state and the input bit is 1 then the 
     system should move to state SEQ_1 and if the input bit is 0 then the detector should move to state SEQ_10.
     
 # Debug information
   From the above test cases the following changes are required to be done:
   1. The line marked as Bug 1 it should be changed from next_state = IDLE; to next_state = SEQ_1;
   2. The line marked as Bug 2 it should be changed from next_state = IDLE; to next_state = SEQ_10;
   3. The line marked as Bug 3 it should be changed from next_state = IDLE; to the following code:
      
      SEQ_1011:
      
      begin
      
        if(inp_bit==1)
        
          next_state = SEQ_1;
          
        else
        
          next_state = SEQ_10;
          
       end
  
  

  
  
  
  
  
