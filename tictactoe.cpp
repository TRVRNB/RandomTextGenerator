#include <iostream>
#include <cstring>
// 9/23/25 Tic Tac Toe


struct Board {
  // they need to be 4 long for /0
  // i could probably use a map for this, but i wanted to try out structs
  char a[4] = "---";
  char b[4] = "---";
  char c[4] = "---";
};

void print_line(char* line){
  // prints out a line of tic tac toe
  for (int i = 0; i < 3; i++){
    std::cout << ' ' << line[i];
  }
  std::cout << "\n" << std::flush;
  return;
}

void print_board(Board &board){
  // prints the board and its coordinates
  std::cout << "  1 2 3 \n";
  
  char* a = board.a;
  std::cout << "a";
  print_line(a);
  char* b = board.b;
  std::cout << "b";
  print_line(b);
  char* c = board.c;
  std::cout << "c";
  print_line(c);
  
  return;
}

char check_line(char* line){
  // returns ' ' if there is no connection of 3, otherwise returns the player char
  if (line[0] == 'O' || line[0] == 'X'){ // only need to check the first one
    if (line[0] == line[1] && line[0] == line[2]){ // if all 3 chars are the same
      return line[0];
    }
  } else {
    return ' '; // default case
  }    
  return ' ';
}

void concatenate3(char* text, char x1, char x2, char x3){
  // makes concatination in check_lines easier
  std::cout << text;
  text[0], text[1], text[2] = x1, x2, x3;
  std::cout << text;
  return;
}

char check_lines(Board &board){
  // runs check_line for every possible line
  char lines[8][4]; // array of char arrays, each representing a line
  concatenate3(lines[0], board.a[0], board.a[1], board.a[2]);
  std::cout << lines[0];
  return 'a';  
}

int main(){
  Board board;
  std::cout << "O goes first.";
  short turn = 0;
  
  bool running = true;
  while (running){
    // main loop
    std::cout << '\n';
    char turnchars[3] = "OX";
    print_board(board);
    
    bool valid = false;
    while (not valid){
      char input[3];
      std::cin >> input;
      valid = true; // assume it is true, unless the default case runs
      char turn_char = turnchars[turn];
      int num = input[1] - '0' - 1;// apparently this works because the digits are sorted in ascii
      // and it uses the ascii codes when converting to int, so (int)'9' - '0' = 9
      switch (input[0]){
      case 'a':
	if (board.a[num] != '-'){
	    std::cout << "Invalid placement.\n";
	    valid = false;
	    break;
	  }
	board.a[num] = turn_char;
	break;
      case 'b':
	if (board.b[num] != '-'){
	    std::cout << "Invalid placement.\n";
	    valid = false;
	    break;
	  }
	board.b[num] = turn_char;
	break;
      case 'c':
	if (board.c[num] != '-'){
	    std::cout << "Invalid placement.\n";
	    valid = false;
	    break;
	  }
	board.c[num] = turn_char;
	break;
      default: // repeat this input
	std::cout << "Try: a1, b2, c1, a3\n" << std::flush;
	valid = false;
      }
    }
      
    check_lines(board);
    turn = 1 - turn; // this is a sketchy way of alternating between 1 and 0
  }



  
  return 0;
}
