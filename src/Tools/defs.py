from imports import *

# Criate a Line
def Line(MASTER, COLOR="#CCCCCC", HEIGHT=2, Y=(5, 5)):
    Separator = CTK.CTkFrame(
        master   = MASTER,
        height   = HEIGHT,
        fg_color = COLOR
    )
    Separator.pack(fill="x", pady=Y)

# 
def SelectLocaleDir(context):
    DirInicial = DesktopDir()

    path = filedialog.askdirectory(
        title      = context,
        initialdir = DirInicial
    )

    if path: return path

# Function to get the Desktop directory
def DesktopDir():
    home = os.path.expanduser("~")
        
    # Opções possíveis (em português e inglês)
    opcoes = ["Desktop", "Área de Trabalho", "Escritorio"]
        
    for nome in opcoes:
        caminho = os.path.join(home, nome)
        if os.path.exists(caminho):
            return caminho

    # Se nenhuma pasta padrão for encontrada, volta pro home
    return home

# Function to select a directory and update the Entry widget
def SelectFileDir(DIR, context):
    DirInicial = DesktopDir()

    file = filedialog.askopenfilename(
        title      = context,
        initialdir = DirInicial,
    )
    if file:
        DIR.configure(state="normal")
        DIR.configure(text_color = "#000000")
        DIR.delete(0, "end")
        DIR.insert(0, file)
        DIR.configure(state="readonly")

# Crite to PATH and .deb
def CreatePATH(

        DIR,

        AppName, 
        Version,
        Section,
        Priority,
        Architecture,
        Categories,
        Terminal,
        Maintainer,
        Description,
        DirIcon,
        DirExec,
    ):

    Package = AppName.replace(" ", "-").lower()
    FilePathName = f"{Package}_v{Version}"

    # Creating PATH
    os.makedirs(os.path.join(DIR, FilePathName), exist_ok=True)
    os.makedirs(os.path.join(DIR, FilePathName, "DEBIAN"), exist_ok=True)
    os.makedirs(os.path.join(DIR, FilePathName, "usr", "bin"), exist_ok=True)
    os.makedirs(os.path.join(DIR, FilePathName, "usr", "share", "applications"), exist_ok=True)
    os.makedirs(os.path.join(DIR, FilePathName, "usr", "share", "icons", "hicolor", "128x128", "apps"), exist_ok=True)

    # Muve files to PATH
    FinalFileIcon = os.path.join(DIR, FilePathName, "usr", "share", "icons", "hicolor", "128x128", "apps")
    FinalFileExec = os.path.join(DIR, FilePathName, "usr", "bin")

    shutil.copy(DirIcon, FinalFileIcon)
    shutil.copy(DirExec, FinalFileExec)

    Icon = os.path.basename(os.path.normpath(DirIcon)).replace(".", " ").split()[0]
    Exec = os.path.basename(os.path.normpath(DirExec))

    # Create file control
    ContentControl = f"""Package: {Package}
Version: {Version}
Section: {Section.lower()}
Priority: {Priority}
Architecture: {Architecture}
Maintainer: {Maintainer}
Description: {Description}
"""
    DirControl = os.path.join(DIR, FilePathName, "DEBIAN", "control")
    with open(DirControl, "w") as f:
        f.write(ContentControl)    

    # Create file .desktop
    ContentDesktop = f"""[Desktop Entry]
Name={AppName}
Exec={Exec}
Icon={Icon}
Type=Application
Categories={Categories}
Comment={Description}
Terminal={Terminal}
"""
    DirDesktop = os.path.join(DIR, FilePathName, "usr", "share", "applications", "app.desktop")
    with open(DirDesktop, "w") as f:
        f.write(ContentDesktop)


    # Create a file .deb
    subprocess.run(["dpkg-deb", "--build", FilePathName], cwd=DIR)

# Validations of Package Informations
def Validation(
        Package, 
        Maintainer, 
        Version,  
        Description,
    
        Icon,
        Exec,
    ):

    # Validation of Package
    def Validation_Package():

        if Package == "":
            return [False, "Error: Empty field!"]

        if not Package[0].isalpha(): 
            return [False, f'Error: "{Package[0]}" cannot be the first character of the App Name!' ]

        if len(Package) > 50:
            return [False, "Error: App Name is too long!"]
        
        for i in Package:
            if (not i.isalpha()) and (not i.isdigit()) and (i not in ["-", "+", "."]): 
                return [False, f'Error: "{i}" cannot be used in the App Name!']

        return [True, "Ok"]

    # Validation of Version
    def Validation_Version():

        if Version == "":
            return [False, "Error: Empty field!"]

        if not Version[0].isdigit():
            return [False, 'Error: The "Version" must start with a number!']

        for i in Version:
            if (not i.isalpha()) and (not i.isdigit() and (i not in [".", "+", "~", "-"])):
                return [False, f'Error: "{i}" cannot be used in the Version!']

            normalize = unicodedata.normalize("NFD", i)
            accent = any(unicodedata.category(c) == "Mn" for c in normalize)
            if accent: 
                return [False, f'Error: "{i}" cannot be used in the Version!']

        return [True, "Ok"]

    # Validation of Maintainer
    def Validation_Maintainer():
        if Maintainer == "":
            return [False, "Error: Empty field!"]
        
        if len(Maintainer.split()) != 3:
            return [False, "Error: Invalid format! : First_name Last_name <email@dominio.com>"]
        
        Name1 = Maintainer.split()[0]
        Name2 = Maintainer.split()[1]
        Gmail = Maintainer.split()[2]

        for i in Name1:
            if (i.isdigit()) or (not i.isalpha()):
                return [False, f'Error: "{i}" cannot be used!']
    
        for i in Name2:
            if (i.isdigit()) or (not i.isalpha()):
                return [False, f'Error: "{i}" cannot be used!']
    
        if Gmail[0] != "<" or Gmail[-1] != ">":
            return [False, 'Error: Email must be inside "<" and ">" : "<email>"']

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        VerGmail = re.match(pattern, Gmail.replace("<", "").replace(">", "")) is not None
        if not VerGmail: 
            return [False, f'Error: Invalid email!']

        return [True, "Ok"]

    # Validation of Description
    def Validation_Description():
        if Description == "":
            return [False, "Error: Empty field!"]

        return [True, "Ok"]


    def Validation_Icon():
        if Icon == "" or Icon == "Error: Empty field!":
            return [False, "Error: Empty field!"]
        
        if Icon :
            pass

        return [True, "Ok"]


    def Validation_Exec():
        if Exec == "" or Exec == "Error: Empty field!":
            return [False, "Error: Empty field!"]
        return [True, "Ok"]


    return [
        Validation_Package(),
        Validation_Maintainer(),
        Validation_Version(),

        Validation_Description(),

        Validation_Icon(),
        Validation_Exec(),
    ]
