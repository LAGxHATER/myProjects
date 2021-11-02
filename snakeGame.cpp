#include <iostream>
#include <curses.h>
#include <unistd.h>

using namespace std;

bool gameOver;
int x, y, fruitX, fruitY, score;

//game area
const int width = 20;
const int height = 20;

//variables to make the tail
int tailX[100], tailY[100];
int nTail;

//snake control directions and directory 
enum Direction { STOP = 0, LEFT, RIGHT, UP, DOWN};
Direction dir; 

void Setup()
{
    gameOver = false;
    dir = STOP;

    //snake head spawn location
    x = width / 2;
    y = height / 2;

    //fruit spawn location
    fruitX = rand() % width;
    fruitY = rand() % height;

    //initial score
    score = 0; 
}

void Draw()
{   
    //clear linux terminal window
    system("clear");

    //printing top wall
    for(int i = 0; i < width + 2; i++)
    {
        cout << "#";
    }
    cout << endl;
    
    //printing side wall
    for(int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //print left wall
            if(j == 0)
            {
                cout << "#";
            }
            //printing snake head
            if(i == y && j == x)
            {
                cout << "8";
            }
            //printing fruit
            else if(i == fruitY && j == fruitX)
            {
                cout << "F";
            }
            else
            {   
                //printing tail
                bool print = false; 
                for(int k = 0; k < nTail; k++)
                {
                    if(tailX[k] == j && tailY[k] == i)
                    {
                        cout << "o";
                        print = true;
                    }
                }
                if(!print)
                    {
                        cout << " ";
                    }
            }           
            //print right wall
            if(j == width - 1)
            {
                cout << "#";
            }
        }
        cout << endl;
    }
    
    //printing bottom wall
    for(int i = 0; i < width + 2; i++)
    {
        cout << "#";
    }
    cout << endl;
    
    //print score
    cout << "Score: " << score << endl;
    
}

void Input()
{
    char key;
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);
    
    //reads players key input
    key = getch();
        switch(key)
        {
            case 'a':
                dir = LEFT;
                break;
            
            case 'd': 
                dir = RIGHT;
                break;

            case 's':
                dir = UP;
                break;
            
            case 'w':
                dir = DOWN;
                break;
            
            case 'x':
                gameOver = true;
                break;

        }
        endwin();
}

void Logic()
{
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = x;
    tailY[0] = y; 
    
    for(int i = 1; i < nTail; i++)
    {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }

    switch (dir)
    {
        case LEFT:
            x--;
            break;
        
        case RIGHT:
            x++;
            break;

        case UP:
            y++;
            break;

        case DOWN:
            y--;
            break;
        
        default:
            break;
    }
    //out of bounds ends game
    if (x > width || x < 0 || y > height || y < 0 )
    {
        gameOver = true;
        cout << "You died nigga!";
    }
        

    //hitting tail ends game
    for(int i = 0; i < nTail; i++)
    {
        if(tailX[i] == x && tailY[i] == y)
        {
            gameOver = true;
            cout << "You died nigga!";
        }
    }
    
    //when head coordinate meets fruit, make new random fruit and add 1 to score and 1 to tail
    if(x == fruitX && y == fruitY)
    {
        fruitX = rand() % width;
        fruitY = rand() % height;
        score++;
        nTail++;
    }
}


int main()
{
    Setup();
    while(!gameOver)
    {
        Draw();
        Input();
        Logic();
    }
    return 0;
}
