# Minghong Xu 81491461
import tkinter
import point
import othello

# CCCC99
# CC9933
# 996600

FONT = ('Times New Roman', 16)


class InforDialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        
        size_label = tkinter.Label(
            master = self._dialog_window, text = 'What size of game do you want to play?',
            font = FONT)
        size_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_label = tkinter.Label(
            master = self._dialog_window, text = 'Row Number(even number from 4 to 16):',
            font = FONT)
        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._row_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = FONT)
        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        column_label = tkinter.Label(
            master = self._dialog_window, text = 'Column Number(even number from 4 to 16):',
            font = FONT)
        column_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._column_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = FONT)
        self._column_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)        

        turn_label = tkinter.Label(
            master = self._dialog_window, text = 'Turn(W or B):',
            font = FONT)
        turn_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._turn_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = FONT)
        self._turn_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E) 

        win_label = tkinter.Label(
            master = self._dialog_window, text = 'Win condition(< or >):',
            font = FONT)
        win_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._win_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = FONT)
        self._win_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E) 

        button_frame = tkinter.Frame(master = self._dialog_window)
        
        button_frame.grid(
            row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = FONT,
            command = self._on_ok_button)
        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = FONT,
            command = self._on_cancel_button)
        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False
        self._row = ''
        self._col = ''
        self._turn = ''
        self._win = ''

    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_row(self) -> str:
        return self._row

    def get_col(self) -> str:
        return self._col

    def get_turn(self) -> str:
        return self._turn

    def get_win(self) -> str:
        return self._win

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._row = self._row_entry.get()
        self._col = self._column_entry.get()
        self._turn = self._turn_entry.get()
        self._win = self._win_entry.get()
        self._dialog_window.destroy()

    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()

        
class OthelloApplication:
    def __init__(self):
        self._turn = ''
        self._root_window = tkinter.Tk()

        start_button = tkinter.Button(
            master = self._root_window, text = 'Start', font = FONT,
            command = self.get_infor)
        start_button.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N)

        self._white_text = tkinter.StringVar()
        self._white_text.set('White:')
        white_label = tkinter.Label(
            master = self._root_window, textvariable = self._white_text,
            font = FONT)
        white_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S)

        self._black_text = tkinter.StringVar()
        self._black_text.set('Black:')
        black_label = tkinter.Label(
            master = self._root_window, textvariable = self._black_text,
            font = FONT)
        black_label.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.S)

        self._turn_text = tkinter.StringVar()
        self._turn_text.set('Turn:')
        turn_label = tkinter.Label(
            master = self._root_window, textvariable = self._turn_text,
            font = FONT)
        turn_label.grid(
            row = 4, padx = 10, pady = 10,
            sticky = tkinter.S)
        
        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 0)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        
        self._row = 0
        self._col = 0
        self._canvas = None
        self._board = []
        self._ok_button = None
        self._gamestate = None
        self._wincondition = ''

        self._init_text = tkinter.StringVar()
        self._init_text.set('Welcome!')
        init_label = tkinter.Label(
            master = self._root_window, textvariable = self._init_text,
            font = FONT)
        init_label.grid(
            row = 1, column = 1, padx = 1, pady = 1,
            sticky = tkinter.W)

                
        
    def run(self) -> None:
        self._root_window.mainloop()

    def get_infor(self) -> None:
        dialog = InforDialog()
        dialog.show()
        if dialog.was_ok_clicked():
            self._row = int(dialog.get_row())
            self._col = int(dialog.get_col())
            self._turn = dialog.get_turn()
            self._wincondition = dialog.get_win()
            self.draw_canvas()
        for i in range(self._row):
            row = []
            for j in range(self._col):
                row.append('.')
            self._board.append(row)
        self._turn_text.set('Turn: '+ self._turn)




    def draw_canvas(self) -> None:
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = self._col*40, height = self._row*40,
            background = '#996600')
        self._canvas.grid(
            row = 2, column = 0, rowspan = 2, columnspan = 2,
            padx = 10, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self.draw_line()
        
        self._canvas.bind('<Button-1>', self.click_white)
        self._canvas.bind('<Configure>', self.canvas_resized)
        
        self._init_text.set('Place initial white discs:')
        self._ok_button = tkinter.Button(
            master = self._root_window, text = 'OK', font = FONT,
            command = self._init_ok_command)
        self._ok_button.grid(row = 1, column = 2, padx = 1, pady = 1)

    def draw_line(self):
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        d_x = canvas_width/self._col
        d_y = canvas_height/self._row
        for i in range(1, self._col):
            self._canvas.create_line(
                i*d_x, 0, i*d_x, self._row*d_y,
                fill = 'black')
        for j in range(1, self._row):
            self._canvas.create_line(
                0, j*d_y, self._col*d_x, j*d_y,
                fill = 'black')
        
    def click_white(self, event: tkinter.Event) -> str:
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        click_point = point.from_pixel(
            event.x, event.y, width, height)
        row = 0
        row_unit = 1/(self._row)
        col = 0
        col_unit = 1/(self._col)
        for i in range(self._row):
            if click_point.frac()[1] > i*row_unit and click_point.frac()[1] < (i+1)*row_unit:
                row = i
        for j in range(self._col):
            if click_point.frac()[0] > j*col_unit and click_point.frac()[0] < (j+1)*col_unit:
                col = j
        if self._board[row][col] == '.':
            self._board[row][col] = 'W'
        self.draw_circle(self._board)

    def click_black(self, event: tkinter.Event) -> str:
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        click_point = point.from_pixel(
            event.x, event.y, width, height)
        row = 0
        row_unit = 1/(self._row)
        col = 0
        col_unit = 1/(self._col)
        for i in range(self._row):
            if click_point.frac()[1] > i*row_unit and click_point.frac()[1] < (i+1)*row_unit:
                row = i
        for j in range(self._col):
            if click_point.frac()[0] > j*col_unit and click_point.frac()[0] < (j+1)*col_unit:
                col = j
        if self._board[row][col] == '.':
            self._board[row][col] = 'B'
        self.draw_circle(self._board)

    def _init_ok_command(self):
        self._init_text.set('Place initial black discs:')
        self._ok_button = tkinter.Button(
            master = self._root_window, text = 'OK', font = FONT,
            command = self._ingame_ok_command)
        self._ok_button.grid(row = 1, column = 2, padx = 1, pady = 1)
        self._canvas.bind('<Button-1>', self.click_black)

    def _ingame_ok_command(self):
        self._init_text.set('In game...')
        self._ok_button.grid(row = 1, column = 2, padx = 1, pady = 1)
        self._gamestate = othello.GameState(self._row, self._col, self._board, self._turn)
        self._board = self._gamestate.board
        self._canvas.bind('<Button-1>', self.move)
        self._canvas.bind('<Configure>', self.canvas_resized)

        self._ok_button = tkinter.Button(
            master = self._root_window, text = 'change turn', font = FONT,
            command = self._change_turn)
        self._ok_button.grid(row = 1, column = 2, padx = 1, pady = 1)

    def move(self, event: tkinter.Event):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        click_point = point.from_pixel(
            event.x, event.y, width, height)
        row = 0
        row_unit = 1/(self._row)
        col = 0
        col_unit = 1/(self._col)
        for i in range(self._row):
            if click_point.frac()[1] > i*row_unit and click_point.frac()[1] < (i+1)*row_unit:
                row = i
        for j in range(self._col):
            if click_point.frac()[0] > j*col_unit and click_point.frac()[0] < (j+1)*col_unit:
                col = j
        if self._gamestate.move(row, col) == True:
            self.draw_circle(self._board)
        self._white_text.set('White:' + str(self._gamestate.wnumber))
        self._black_text.set('Black:' + str(self._gamestate.bnumber))
        self._turn_text.set('Turn:' + self._gamestate.turn)

        if self._gamestate.wnumber + self._gamestate.bnumber == self._row * self._col \
               or self._gamestate.wnumber == 0 \
               or self._gamestate.bnumber == 0:
            self._init_text.set('Winner is' + self._gamestate.winner(self._wincondition))

    def draw_circle(self, board):
        self._canvas.delete(tkinter.ALL)
        self.draw_line()
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        d_x = canvas_width/self._col
        d_y = canvas_height/self._row
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'W':
                    self._canvas.create_oval(j*d_x, i*d_y,
                                             (j+1)*d_x, (i+1)*d_y,
                                             fill = 'white', outline = 'white')
                elif board[i][j] == 'B':
                    self._canvas.create_oval(j*d_x, i*d_y,
                                             (j+1)*d_x, (i+1)*d_y,
                                             fill = 'black', outline = 'black')

    def canvas_resized(self, event: tkinter.Event):
        self.draw_circle(self._board)
        self.draw_line()

    def _change_turn(self):
        self._gamestate.opposite_turn()
        self._turn_text.set('Turn:' + self._gamestate.turn)
        
if __name__ == '__main__':
    OthelloApplication().run()
