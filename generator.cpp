#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
#include <fstream>
#include <ctime>        // std::time
#include <cstdlib>      // std::rand, std::srand
using namespace std;
string prefix[4]={"S","H","C","D"};
string deck[416] = {"SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","SA","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","HA","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","CA","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK"};
int main () {
	std::srand ( unsigned ( std::time(0) ) );

	ofstream ott("100000deck__.txt");
	int counter=0;
	while(counter!=100000){
		random_shuffle(deck,deck+416);
		counter++;
		
		for(int i=0;i<416;i++){
			ott<<deck[i]<<" ";
		}
		ott<<"\n";
	}
  

  

  

  return 0;
}
