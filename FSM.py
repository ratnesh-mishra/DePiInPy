__author__ = 'ratnesh.mishra'
import asyncio
# FSM in python,  coding a Snake game

# Object Snake - (Alive, Dead, has_size)

# Game (states - (Initialize, setup, play, stop), score, snake, board, food)

from enum import Enum

class State(Enum):
    INITIALIZE = 0
    SETUP = 1
    PLAY = 2
    STOP = 3
    IDLE = 4


class Snake_State(Enum):
    ALIVE = 0
    DEAD = 1


class Snake:

    def __int__(self):
        self._size = 0
        self._state = Snake_State.ALIVE.value
        self.pos = None
        self.max_length = 0

    @property
    def Size(self):
        if self._state == Snake_State.ALIVE.value:
            return self._size

    @Size.setter
    def Size(self):
        if self._state == Snake_State.ALIVE.value and self._size < self.max_length:
            self._size += 1
        else:
            raise Exception('Size cannot be increased')


class Game:

    move = {'l': (-1, 0), 'r': (1, 0), 'u': (0, 1), 'd': (0, -1)}

    def __init__(self):
        self.state = 0
        self.snake = None
        self.score = 0
        self.level = 1
        self.result = 0

    @asyncio.coroutine
    def execute(self):
        while True:
            if self.state == State.INITIALIZE.value:
                self.initialize()

            elif self.state == State.SETUP.value:
                self.setup()

            elif self.state == State.PLAY.value:
                asyncio.async(self.play())

            elif self.state == State.STOP.value:
                self.print_results()
                self.state = State.IDLE.value

            elif self.state == State.IDLE.value:
                pass

    def initialize(self):
        self.score = 0
        self.snake = Snake()
        self.board = None
        self.food_pos = None
        self.state = State.SETUP.value

    def setup(self):
        self.board = []
        for i in range(8):
            self.board.append([0]*8)
        self.snake._size = 4
        self.snake.pos = self.get_snake_pos()
        self.food_pos = self.get_food_pos()
        self.state = State.PLAY.value

    @asyncio.coroutine
    def update_position(self, direction):

        """
        :param direction: direction in which snake is moving currently
        :Function : Keep checking position of snake , food and boundaries to keep increasing score or
        changing state to dead
        :return:
        """
        pass

    @asyncio.coroutine
    def play(self):
        while self.snake.state != Snake_State.DEAD.value:
            direction = input("Enter user Input") # input can be l,r,u,d
            if direction not in self.move.keys():
                print('Invalid Input')
            asyncio.async(self.update_position(direction))

    def print_results(self, result):

        if result == 'UPGRADED':
            print('Your Score was {} and level is now upgraded to {}'.format(self.score, self.level))
        elif result == 'FAILED':
            print('Your score was {} , however you failed to breach level {}'.format(self.score, self.level))


    def get_snake_pos(self):
        pass

    def get_food_pos(self):
        pass

if __name__ == '__main__':
    g = Game()
    asyncio.get_event_loop().run_until_complete(g.execute())