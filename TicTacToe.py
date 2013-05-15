#-*- coding:utf-8 -*-
import copy
import random


class ExpermentGeneration:
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.history = [copy.deepcopy(self.board)]

    def setBoard(self, board):
        self.board = board
        self.history.append(copy.deepcopy(self.board))

    def setPlayer(self, x, y):
        self.board[2-y][x] = 2

    def getBoard(self):
        return self.board

    def getHistory(self):
        return self.history

    def getRows(self, board=0):
        if board == 0:
            board = self.board
        return board

    def getColumns(self, board=0):
        if board == 0:
            board = self.board
        columns = []
        for x in xrange(0, 3):
            column = []
            column.append(board[0][x])
            column.append(board[1][x])
            column.append(board[2][x])
            columns.append(column)
        return columns

    def getDiagonals(self, board=0):
        if board == 0:
            board = self.board
        diagonal1 = []
        diagonal1.append(board[0][0])
        diagonal1.append(board[1][1])
        diagonal1.append(board[2][2])
        diagonal2 = []
        diagonal2.append(board[0][2])
        diagonal2.append(board[1][1])
        diagonal2.append(board[2][0])
        diagonals = [diagonal1, diagonal2]
        return diagonals

    def isFinish(self, board=0):
        if board == 0:
            board = self.board
        flage = True
        for x in xrange(0, 3):
            for y in xrange(0, 3):
                if board[x][y] == 0:
                    flage = False

        boardstatus = []
        for row in self.getRows(board):
            boardstatus.append(row)
        for colum in self.getColumns(board):
            boardstatus.append(colum)
        for diagonal in self.getDiagonals(board):
            boardstatus.append(diagonal)
        for boardstatu in boardstatus:
            empty = 0
            player1s = 0
            player2s = 0
            for i in boardstatu:
                if i == 0:
                    empty += 1
                elif i == 1:
                    player1s += 1
                elif i == 2:
                    player2s += 1
            if player1s == 3 or player2s == 3:
                flage = True

        return flage

    def getWinner(self, board=0):
        if board == 0:
            board = self.board
        if self.isFinish(board):
            boardstatus = []
            for row in self.getRows(board):
                boardstatus.append(row)
            for colum in self.getColumns(board):
                boardstatus.append(colum)
            for diagonal in self.getDiagonals(board):
                boardstatus.append(diagonal)
            for boardstatu in boardstatus:
                empty = 0
                player1s = 0
                player2s = 0
                for i in boardstatu:
                    if i == 0:
                        empty += 1
                    elif i == 1:
                        player1s += 1
                    elif i == 2:
                        player2s += 1

                if player1s == 3:
                    return 1

                elif player2s == 3:
                    return 2

            else:
                    return 0

    def printBoard(self, board=0):
        if board == 0:
            board = self.board
        printBoard = []
        for row in board:
            printRow = []
            for i in row:
                if i == 0:
                    printRow.append(' ')
                elif i == 1:
                    printRow.append('X')
                elif i == 2:
                    printRow.append('O')
            printBoard.append(printRow)

        print ''
        print printBoard[0][0] + '|' + printBoard[0][1] + '|' + printBoard[0][2]
        print '------'
        print printBoard[1][0] + '|' + printBoard[1][1] + '|' + printBoard[1][2]
        print '------'
        print printBoard[2][0] + '|' + printBoard[2][1] + '|' + printBoard[2][2]
        print ''


class PerformanceSystem:
    def __init__(self, board, weight, player):
        self.board = board
        self.player = player
        self.weight = weight

    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setBoard(self, board):
        self.board = board

    def getBoard(self, board):
        return self.board

    def getNextMove(self, player):
        possibilitys = []
        for x in xrange(0, 3):
            for y in xrange(0, 3):
                if self.board.getBoard()[x][y] == 0:
                    possibility = copy.deepcopy(self.board.getBoard())
                    possibility[x][y] = player
                    possibilitys.append(possibility)
                    #print 'possibility: '
                    #print possibility
        #print 'possibilitys:'
        #print possibilitys
        return possibilitys

    def randomMove(self, player):
        possibilitys = self.getNextMove(player)
        randomBoard = possibilitys[random.randint(0, len(possibilitys)-1)]
        #print 'randomBoard:'
        #print randomBoard
        self.board.setBoard(randomBoard)

    def bestMove(self, player):
        possibilitys = self.getNextMove(player)
        bestBoard = possibilitys[0]
        bestValue = self.evaluate(bestBoard)
        for possibility in possibilitys:
            value = self.evaluate(possibility)
            if value > bestValue:
                bestValue = value
                bestBoard = possibility
        self.board.setBoard(bestBoard)

    def evaluate(self, board):
        x = self.getFeatures(board)
        w = self.weight
        v = w[0]
        for i in xrange(1, 7):
            v += w[i]*x[i-1]
        return v

    def getFeatures(self, board):
        #x[0] 1X 2empty
        #x[1] 1O 2empty
        #x[2] 2X 1empty
        #x[3] 2O 1empty
        #x[4] 3X
        #x[5] 3O
        boardstatus = []
        for row in board:
            boardstatus.append(row)
        for x in xrange(0, 3):
            column = []
            column.append(board[0][x])
            column.append(board[1][x])
            column.append(board[2][x])
            boardstatus.append(column)
        diagonal1 = []
        diagonal1.append(board[0][0])
        diagonal1.append(board[1][1])
        diagonal1.append(board[2][2])
        boardstatus.append(diagonal1)
        diagonal2 = []
        diagonal2.append(board[0][2])
        diagonal2.append(board[1][1])
        diagonal2.append(board[2][0])
        boardstatus.append(diagonal2)

        x = [0, 0, 0, 0, 0, 0]
        for boardstatu in boardstatus:
            empty = 0
            player1s = 0
            player2s = 0
            for i in boardstatu:
                if i == 0:
                    empty += 1
                elif i == 1:
                    player1s += 1
                elif i == 2:
                    player2s += 1
            if player1s == 1 and empty == 2:
                x[0] += 1
            elif player2s == 1 and empty == 2:
                x[1] += 1
            elif player1s == 2 and empty == 1:
                x[2] += 1
            elif player2s == 2 and empty == 1:
                x[3] += 1
            elif player1s == 3:
                x[4] += 1
            elif player2s == 3:
                x[5] += 1
        return x


class Critic:
    def __init__(self, weight, player):
        self.weight = weight
        self.player = player
        self.board = ExpermentGeneration()
        self.updater = PerformanceSystem(self.board, self.weight, self.player)

    def setWeight(self, weight):
        self.weight = weight

    def setPlayer(self, player):
        self.player = player

    def getTrainingExample(self, history):
        trainingExamples = []
        for i in xrange(0, len(history)):
            #print history
            if self.board.isFinish(history[i]):
                if self.board.getWinner(history[i]) == self.player:
                    trainingExamples.append([self.updater.getFeatures(history[i]), 100])
                elif self.updater.board.getWinner(history[i]) == 0:
                    trainingExamples.append([self.updater.getFeatures(history[i]), 0])
                else:
                    trainingExamples.append([self.updater.getFeatures(history[i]), -100])
            else:
                if i+2 >= len(history):
                    if self.board.getWinner(history[len(history)-1]) == 0:
                        trainingExamples.append([self.updater.getFeatures(history[i]), 0])
                    else:
                        trainingExamples.append([self.updater.getFeatures(history[i]), -100])
                else:
                    trainingExamples.append([self.updater.getFeatures(history[i]), self.updater.evaluate(history[i+2])])
        return trainingExamples


class Generalizer:
    def __init__(self, performance, updateConstant=0.1):
        self.updater = performance
        self.updateConstant = updateConstant

    def setUpdateConstant(self, updateConstant):
        self.updateConstant = updateConstant

    def updateWeights(self, history, trainingExamples):
        for i in xrange(0, len(history)):
            w = self.updater.getWeight()
            vEst = self.updater.evaluate(history[i])
            x = trainingExamples[i][0]
            vTrain = trainingExamples[i][1]
            w[0] = w[0] + self.updateConstant*(vTrain - vEst)
            w[1] = w[1] + self.updateConstant*(vTrain - vEst)*x[0]
            w[2] = w[2] + self.updateConstant*(vTrain - vEst)*x[1]
            w[3] = w[3] + self.updateConstant*(vTrain - vEst)*x[2]
            w[4] = w[4] + self.updateConstant*(vTrain - vEst)*x[3]
            w[5] = w[5] + self.updateConstant*(vTrain - vEst)*x[4]
            w[6] = w[6] + self.updateConstant*(vTrain - vEst)*x[5]
            self.updater.setWeight(w)


board = ExpermentGeneration()
#weight1 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
weight1 = [0.4487364634869461, 6.8850317110019095, -30.716446979325386, 18.939174969105707, -49.81717447843381, 64.89761758557803, -112.17267055448487]
weight2 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
player1 = PerformanceSystem(board, weight1, 1)
player2 = PerformanceSystem(board, weight2, 2)
critic1 = Critic(weight1, 1)
#critic2 = Critic(weight2, 2)
generalizer1 = Generalizer(player1)
#generalizer2 = Generalizer(player2, 0.2)
player1wins = 0
player2wins = 0
draws = 0

for i in xrange(0, 6000):
    board = ExpermentGeneration()
    player1.setBoard(board)
    player2.setBoard(board)
    while not board.isFinish(board.getBoard()):
        player1.bestMove(1)
        if board.isFinish(board.getBoard()):
            break
        player2.randomMove(2)
        #player1.bestMove(2)
    board.printBoard()

    winner = board.getWinner()

    if winner == 1:
        print 'player1 win'
        player1wins += 1
    elif winner == 2:
        print 'player2 win'
        player2wins += 1
    elif winner == 0:
        print 'draw'
        draws += 1

    critic1.setWeight(player1.getWeight())
    generalizer1.updateWeights(board.getHistory(), critic1.getTrainingExample(board.getHistory()))
    #critic2.setWeight(player2.getWeight())
    #generalizer2.updateWeights(board.getHistory(), critic2.getTrainingExample(board.getHistory()))

print 'player1 win: ' + str(player1wins)
#print player1.getWeight()
print 'player2 win: ' + str(player2wins)
#print player2.getWeight()
print 'draw: ' + str(draws)

while True:
    board = ExpermentGeneration()
    player1.setBoard(board)
    player2.setBoard(board)

    while not board.isFinish():
        player1.bestMove(1)
        if board.isFinish():
            break
        board.printBoard()
        xval = input('x坐标 ( 0-2 ):')
        yval = input('y坐标 ( 0-2 ):')
        try:
            board.setPlayer(xval, yval)
        except:
            pass
    board.printBoard()
    winner = board.getWinner()

    if winner == 1:
        print 'computer win'
    elif winner == 2:
        print 'you win'
    elif winner == 0:
        print 'draw'

    critic1.setWeight(player1.getWeight())
    generalizer1.updateWeights(board.getHistory(), critic1.getTrainingExample(board.getHistory()))
    print player1.getWeight()
