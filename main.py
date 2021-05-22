from tkinter import Menu, Text, Tk, END, filedialog, messagebox, RAISED, Y, PhotoImage
import subprocess, os, math,pathlib, argparse, webbrowser

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="Shows what type of file you are editing example python(py) or php(php)")
arguments = parser.parse_args()
def set_executor(operator='py'):
    global executor, extension
    functions = [
        (
            'python', 
            [
                'py'
            ]
        ),
        (
            'node', 
            [
                'js'
            ]
        ), 
        (
            'php',
            [
                'php'
            ]
        ),
        (
            'C/C++',
            [
                'c',
                'cpp'
            ]
        )
    ]
    for name, extension in functions:
        for limitedExtension in extension:
            if operator == limitedExtension:
                executor = name
                extension = limitedExtension
    try:
        menu_bar.delete("Server (localhost: 8000)")
    except:
        pass
    if executor == 'php' or executor == 'html':
        try:
            menu_bar.add_command(label='Server (localhost: 8000)', command=server, accelerator="Ctrl+L")
            compiler.config(menu=menu_bar)
            compiler.bind('<Control-l>', server)
            compiler.bind('<Control-L>', server)
        except:
            pass
    
passedArg = arguments.type
if(passedArg is not None):
    extension_lists = [
        (
            'python', 
            [
                'py'
            ]
        ), 
        (
            'node', 
            [
                'js'
            ]
        ), 
        (
            'php',
            [
                'php'
            ]
        ),
        (
            'C/C++',
            [
                'c',
                'cpp'
            ]
        )
    ]
    for compilerName, exten in extension_lists:
        if compilerName == passedArg or passedArg in exten:
            if compilerName != passedArg:
                set_executor(passedArg)
            else:
                set_executor(exten[0])
else:
    executor = 'python'
    extension = 'py'
# os.system('cls')
act = pathlib.Path(__file__).parent.absolute()
pathlike = os.path.join(act, 'icon.ico')

Font_tuple = ("Segoe UI", 10, "normal")
compiler = Tk()
compiler.minsize(1000, 300)
compiler.maxsize(None, 800)
compiler.title('Python Programmer | Root ({})'.format(executor.capitalize()))
compiler.iconbitmap('icon.ico')
compiler.geometry('1000x700')
file_path=''
# Function
def set_file_path(path):
    global file_path
    file_path = path
def savaandrun(_=''):
    save_file()
    run()
def astr(_=''):
    "Run Fucntion without Prompting to be executed"
    try:
        if len(extension) > 0:
            execten = extension[0]
        else:
            execten = extension
        if execten == 'c':
            execten = 'cpp'
        _filename = 'tempcode.myide.{}'.format(execten)
        with open(_filename, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
        run(fileloc=_filename)
    except Exception:
        code_out.configure(state='normal')
        code_out.insert('1.0','Execution Error\n')
        code_out.configure(state='disabled')
def run(_='',datatype='normal', fileloc='def'):
    if fileloc == 'def':
        fileloc = file_path
    if datatype=='normal':
        if fileloc == '':
            save_as()
        command = f'{executor} {fileloc}'
        cd = False
        if executor == 'C/C++':
            filename = ''
            if '.c' in str(fileloc):
                filename = fileloc.replace('.c', '') #.split('/')[-1]
            elif '.cpp' in str(fileloc):
                filename = fileloc.replace('.cpp', '')# .split['/'][-1]
            command = f'g++ {fileloc} -o {filename}'
            cd = True
        subprocess.run(['powershell.exe', '-Command', command])
        if cd:
            os.startfile(f"{filename}.exe")
        # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # output, error = process.communicate()
        # if error:
        #     code_out.configure(fg='red')
        # else:
        #     code_out.configure(fg='white')
        code_out.configure(state='normal')
        # code_out.insert('1.0', output)
        code_out.insert('1.0', 'Successfull\n')
        # code_out.insert('1.0',  error)
        code_out.configure(state='disabled')
        # code_out.insert('1.0', 'Output\n')
def file(_=''):
    print("Null")
def save_as(_=''):
    saved = filedialog.asksaveasfilename(title='Save File as', defaultextension='.{}'.format(extension), filetypes=(('Default', extension), ('Python', '*.py'), ('JavaScript', '*.js'), ('php', '*.php'), ('C/C++', ('c', 'cpp')),('All Files', ('*.*'))))
    try:
        with open(saved, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
        code_out.configure(state='normal')
        code_out.insert('1.0',f'File {saved} has been saved\n\n')
        code_out.configure(state='disabled')
        set_file_path(saved)
        set_executor(str(saved).split('/')[-1].split('.')[-1])
        compiler.title('Python Programmer | {} ({})'.format(saved, executor.capitalize()))
    except Exception:
        code_out.configure(state='normal')
        code_out.insert('1.0','Sorry! File cannot be created\n')
        code_out.configure(state='disabled')
def open_files(_=''):
    saved = filedialog.askopenfilename(title='Open Files', filetypes=(('Default', extension), ('Python', '*.py'), ('JavaScript', '*.js'), ('php', '*.php'), ('C/C++', ('c', 'cpp')) ,('All Files', '*.*')))
    try:
        with open(saved, 'r') as file:
            code = file.read()
            editor.delete('1.0', END)
            editor.insert('1.0', code)
    except Exception:
        code_out.configure(state='normal')
        code_out.insert('1.0', 'Cannot Open File')
        code_out.configure(state='disabled')
    set_file_path(saved)
    set_executor(str(saved).split('/')[-1].split('.')[-1])
    compiler.title('Python Programmer | {} ({})'.format(saved, executor.capitalize()))
def clear_func(_=''):
    code_out.configure(state='normal')
    code_out.delete('1.0', END)
    code_out.configure(state='disabled')
    subprocess.run(['powershell', '-Command', 'clear'])
def server(port=8000):
    os.startfile("{}\\Server.bat".format(act))
    webbrowser.open("http://localhost:8000/");
def save_file(_=''):
    if file_path == '':
        save_as()
    else:
        try:
            with open(file_path, 'w') as file:
                code = editor.get('1.0', END)
                file.write(code)
                code_out.configure(state='normal')
                code_out.insert('1.0','File has been saved\n\n')
                code_out.configure(state='disabled')
        except Exception:
            code_out.configure(state='normal')
            code_out.insert('1.0',f'Cannot Save the File\n')
            code_out.configure(state='disabled')
def create_new_doc(_=''):
    saved = filedialog.asksaveasfilename(title='Create New File', filetypes=(('Default', extension), ('Python Files', '*.py'), ('JavaScript', '*.js'), ('php', '*.php'), ('C/C++', ('c', 'cpp')), ('All Files', '*.*')))
    with open(saved, 'w') as file:
        code_out.configure(state='normal')
        code_out.insert('1.0',f'File {saved} has been created\n\n')
        code_out.configure(state='disabled')
        print('File: ', file.name)
    editor.delete('1.0', END)
    set_file_path(saved)
    set_executor(str(saved).split('/')[-1].split('.')[-1])
    compiler.title('Python Programmer | {} ({})'.format(saved, executor.capitalize()))
def clearRun(_=''):
    astr()
    clear_func()
menuarrays = [
    ('File', [('New File', create_new_doc, 'Ctrl+N'), ('separator', '', '') ,('Open', open_files, 'Ctrl+O'), ('Save', save_file, 'Ctrl+S'), ('Save as', save_as, 'Ctrl+Shift+S'), ('separator', '', ''), ('Run', run, 'Ctrl+R'), ('separator', '', ''),('Settings', file, ''), ('Close', exit, 'Ctrl+Q')]),
    ('Run', [('Run', astr, ''), ('Save and Run', savaandrun, 'Ctrl+Shift+A'), ('Clear and Run', clearRun, '')]),
]
global menu_bar
menu_bar = Menu(compiler)
menu_bar.configure(font = Font_tuple)
for top, name in menuarrays:
    barname = 'bar_{}'.format(str(name).lower())
    barname = Menu(menu_bar, tearoff=0)
    # barname.add_command(label=name, command=functions)
    for actname, func, acc in name:
        if actname == 'separator':
            barname.add_separator()
        else:
            barname.add_command(label=actname, command=func, accelerator=str(acc))
    menu_bar.add_cascade(label=top, menu=barname)
    # menu_bar.bind_all('<Control-o>', open_files)
menu_bar.add_command(label='Clear Console', command=clear_func, accelerator='Ctrl+C')
if executor == 'php' or executor == 'html':
    menu_bar.add_command(label='Server (localhost: 8000)', command=server, accelerator="Ctrl+L")
    compiler.bind('<Control-l>', server)
    compiler.bind('<Control-L>', server)
compiler.config(menu=menu_bar)
compiler.bind('<Control-o>', open_files)
compiler.bind('<Control-O>', open_files)
compiler.bind('<Control-N>', create_new_doc)
compiler.bind('<Control-n>', create_new_doc)
compiler.bind('<Control-S>', save_file)
compiler.bind('<Control-s>', save_file)
compiler.bind('<Control-Shift-S>', save_as)
compiler.bind('<Control-Shift-s>', save_as)
compiler.bind('<Control-R>', astr)
compiler.bind('<Control-r>', astr)
compiler.bind('<Control-q>', exit)
compiler.bind('<Control-Q>', exit)
compiler.bind('<Control-C>', clear_func)
compiler.bind('<Control-c>', clear_func)
compiler.bind('<Control-Shift-R>', savaandrun)
compiler.bind('<Control-Shift-r>', savaandrun)

# TEXT INPUT
editor = Text(
    background='#333',
    foreground='white',
    pady=5,
    padx=5,
    insertbackground='white',
    width=compiler.winfo_width(),
)
editor.configure(font = Font_tuple)
# editor.configure()
editor.pack(fill=Y, expand=True)

code_out = Text(
    cursor='arrow', 
    state='disabled',
    background='#222',
    pady=5,
    padx=5,
    insertbackground='white',
    width=compiler.winfo_width(),
    height=7
)
code_out.configure(font = Font_tuple)
code_out.pack()
compiler.mainloop()