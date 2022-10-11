from tkinter import * 


def click(key):
    if key == 'Enter':
        result = str(entry.get())
        printing= Tk()
        printing.title('결과')
        print_entry = Entry(printing, fg='white', width=50, bg='black', justify='center', )
        print_entry.grid(row=0, column=4, columnspan=10)
        print_entry.insert(END, result)         # 기록한 문자열 print***********
    elif key == 'space': 
        entry.insert(END, ' ')                  # space 키*******
    elif key == 'shift1':
        row_index = 1
        col_index = 0
        for button_text in button_shift:
            Button(tk, text=button_text, width=5, command = lambda t= button_text : click(t)).grid(row=row_index, column=col_index)
            col_index += 1
            if col_index > 10:
                row_index += 1
                col_index = 0
    elif key == 'shift2':
        row_index = 1
        col_index = 0
        for button_text in button_list:
            Button(tk, text=button_text, width=5, command = lambda t= button_text : click(t)).grid(row=row_index, column=col_index)
            col_index += 1
            if col_index > 10:
                row_index += 1
                col_index = 0
    elif key == '한':
        row_index = 1
        col_index = 0
        for button_text in button_kor:
            Button(tk, text=button_text, width=5, command = lambda t= button_text : click(t)).grid(row=row_index, column=col_index)
            col_index += 1
            if col_index > 10:
                row_index += 1
                col_index = 0
    elif key == '영':
        row_index = 1
        col_index = 0
        for button_text in button_list:
            Button(tk, text=button_text, width=5, command = lambda t= button_text : click(t)).grid(row=row_index, column=col_index)
            col_index += 1
            if col_index > 10:
                row_index += 1
                col_index = 0
    elif key == '←':
        entry.delete(len(entry.get())-1, END)   # backspace 키*******
    else:
        entry.insert(END, key)                  # 한글자씩 기록


tk = Tk()

entry = Entry(tk, width=25, bg='white')
entry.grid(row=0, column=0, columnspan=4)



button_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '←', 
                'shift1', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'Enter', 
                'shift2', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'space', '한', '영']

button_shift = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '←', 
                'shift1', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Enter', 
                'shift2', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'space', '한', '영']

button_kor = ['ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ', '←', 
                'shift1', 'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', 'Enter',
                'shift2', 'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ', 'space', '한', '영']

row_index = 1
col_index = 0
for button_text in button_list:
    Button(tk, text=button_text, width=5, command = lambda t= button_text : click(t)).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 10:
        row_index += 1
        col_index = 0

tk.mainloop()
