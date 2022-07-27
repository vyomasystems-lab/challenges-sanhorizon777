
module sram(data_in,Wr,Rd,data_out,Addr);
  input [15:0]data_in;
  input Wr,Rd;
  output [15:0]data_out;
  input [4:0]Addr; //Address
  
  reg [15:0]data_out;
  reg [15:0] Mem [31:0]; // Memory declaration
  always@(Wr or Rd or Addr)
  	begin
      if(Wr==1'b1 && Rd==1'b0)
        Mem[Addr] = data_in;
      else if(Wr==1'b0 && Rd==1'b1)
        data_out = Mem[Addr+1];            //Bug inserted -> Addr+1 
      else
        data_out = 16'hz;
    end
 endmodule