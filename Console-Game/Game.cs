using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    
    public new static void UpdatePosition(string key, out int changex, out int changey){      
      
      switch (key)
      {
          case "UpArrow":
              changey = -1;
              changex = 0; 
              break;
          case "DownArrow":
              changey = 1;
              changex = 0; 
              break;
          case "LeftArrow":
              changey = 0;
              changex = -1; 
              break;
          case "RightArrow":
              changey = 0;
              changex = 1; 
              break;
          default:
              changey = 0;
              changex = 0;               
              break;
      }

    }

    public new static char UpdateCursor(string key){
      
      

      switch (key){

          case "LeftArrow":
              return '<';
          case "RightArrow":
              return '>';
          case "UpArrow":
              return '^';
          case "DownArrow":
              return 'V';
          default:
              return '<';
      }
    }

    public new static int KeepInBounds(int coord, int max){

      
      
      if( coord < 0){
        return 0;
      } else if (coord > max) {
        return  max;
      } else {
        return coord;
      }
      

    }

  
    
    public new static bool DidScore(int x, int y, int tarx, int tary){

      if( x==tarx && y==tary ){
        return true;
      } else {
        return false;
      }

    }




  }
}